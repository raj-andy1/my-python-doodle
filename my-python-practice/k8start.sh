#!/bin/sh

sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release

#download docker public key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

#install docker
sudo apt-get update
sudo apt-get install -y jq docker-ce docker-ce-cli containerd.io


#Download OSQUERY
curl -O https://pkg.osquery.io/deb/osquery_4.8.0-1.linux_amd64.deb

#Install OSQUERY
sudo dpkg -i osquery_4.8.0-1.linux_amd64.deb

#Copy OSQUERY sample config file
cp /usr/share/osquery/osquery.example.conf /etc/osquery/osquery.conf

#Get secret
/usr/local/bin/aws secretsmanager get-secret-value --secret-id arn:aws:secretsmanager:us-east-1:531915269918:secret:OsquerySecretForLinux-0Xwaj5 --region us-east-1 | jq --raw-output '.SecretString' | jq -r '.["kolide.enrollment_secret"]' > /etc/osquery/kolide.enrollment_secret

#Declare a variable to get AWS Account ID
ACCOUNTID=$(curl -s http://169.254.169.254/latest/dynamic/instance-identity/document | grep -oP '(?<="accountId" : ")[^"]*(?=")')
#Create OSQUERY config flag file
echo "--force=true
--host_identifier=hostname
--tls_hostname=fleet-server.services.atlassian.com
--config_plugin=tls
--config_tls_refresh=300
--enroll_tls_endpoint=/api/v1/osquery/enroll
--config_tls_endpoint=/api/v1/osquery/config
--enroll_secret_path=/etc/osquery/kolide.enrollment_secret
--logger_min_status=2
--aws_kinesis_stream=prod-logs
--aws_sts_arn_role=arn:aws:iam::915926889391:role/pipeline-prod-log-producer-$ACCOUNTID
--aws_region=us-east-1
--aws_sts_region=us-east-1
--aws_sts_session_name=osquery
" > /etc/osquery/osquery.flags

#Get OSQUERY version
OSQUERYVERSION=$(osqueryd --version | grep -Po '[0-9].[0-9].[0-9]*')

#Env file for OSQUERY
echo "FLAG_FILE="/etc/osquery/osquery.flags"
CONFIG_FILE="/etc/osquery/osquery.conf"
LOCAL_PIDFILE="/var/osquery/osqueryd.pidfile"
PIDFILE="/var/run/osqueryd.pidfile"
# Custom env vars decorators
OSQUERY_SERVICE=PracticeDevelopmentTeam
OSQUERY_ENV=osquery_fieldops
OSQUERY_SERVICE_VERSION=$OSQUERYVERSION
OSQUERY_DEPLOYMENT_ID=prod
" >/etc/sysconfig/osqueryd

#Configure the Docker daemon, in particular to use systemd for the management of the container’s cgroups
cat <<EOF | sudo tee /etc/docker/daemon.json
{
  "exec-opts": ["native.cgroupdriver=systemd"],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m"
  },
  "storage-driver": "overlay2"
}
EOF

#Restart Docker and enable on boot:
sudo /bin/systemctl enable docker
sudo /bin/systemctl daemon-reload
sudo /bin/systemctl restart docker

#Install Kubernetes
#Download the Google Cloud public signing key:
sudo curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg

#Add the Kubernetes apt repository
echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list

#Update apt package index, install kubelet, kubeadm and kubectl, and pin their version
sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl

#Start OSQUERY
sudo service osqueryd start