#sample python code to delete cloudformation stacks
import boto3

#stack_list = ['j8-000', 'j8-001', 'j8-002', 'j8-003', 'j8-004', 'j8-005', 'j8-006', 'j8-007', 'j8-008', 'j8-009', 'j8-010', 'j8-011', 'j8-012', 'j8-013', 'j8-014', 'j8-015', 'j8-016', 'j8-017', 'j8-018', 'j8-019', 'j8-020', 'j8-021', 'j8-022', 'j8-023', 'j8-024', 'j8-025', 'j8-026', 'j8-027', 'j8-028', 'j8-029', 'j8-030', 'j8-031', 'j8-032', 'j8-033', 'j8-034', 'j8-035', 'j8-036', 'j8-037', 'j8-038', 'j8-039', 'j8-040', 'j8-041', 'j8-042', 'j8-043', 'j8-044', 'j8-045', 'j8-046', 'j8-047', 'j8-048', 'j8-049', 'j8-050']
#stack_list = ['curvclab', 'shankar', 'tomasstackname', 'curvc', 'j8dc-romanb', 'abeishere', 'my-jira-8-v2', 'j8dc', 'Javier', 'disisabe', 'jr', 'romanb', 'sopel-jira-8-1', 'MyJira8', 'jvgtuser015', 'awesomecow', 'j8dc-user-009', 'chrisk', 'Summit19TestStack', 'friendlyname', 'j8dc-test-dt', 'ask056', 'Victor', 'aaa-068', 'zjhayes', 'Teen-Titans-Go', 'andyr', 'burak', 'user-065', 'xantiriad', 'Jira8DC', 'Aety-Stack']

stack_list = ['j8dc-000', 'j8dc-001', 'j8dc-002', 'j8dc-003', 'j8dc-004', 'j8dc-005', 'j8dc-006', 'j8dc-007', 'j8dc-008', 'j8dc-009', 'j8dc-010', 'j8dc-011', 'j8dc-012', 'j8dc-013', 'j8dc-014', 'j8dc-015', 'j8dc-016', 'j8dc-017', 'j8dc-018', 'j8dc-019', 'j8dc-020', 'j8dc-021', 'j8dc-022', 'j8dc-023', 'j8dc-024', 'j8dc-025', 'j8dc-026', 'j8dc-027', 'j8dc-028', 'j8dc-029', 'j8dc-030', 'j8dc-031', 'j8dc-032', 'j8dc-033', 'j8dc-034', 'j8dc-035', 'j8dc-036', 'j8dc-037', 'j8dc-038', 'j8dc-039', 'j8dc-040', 'j8dc-041', 'j8dc-042', 'j8dc-043', 'j8dc-044', 'j8dc-045', 'j8dc-046', 'j8dc-047', 'j8dc-048', 'j8dc-049', 'j8dc-050', 'j8dc-051', 'j8dc-052', 'j8dc-053', 'j8dc-054', 'j8dc-055', 'j8dc-056', 'j8dc-057', 'j8dc-058', 'j8dc-059', 'j8dc-060', 'j8dc-061', 'j8dc-062', 'j8dc-063', 'j8dc-064', 'j8dc-065', 'j8dc-066', 'j8dc-067', 'j8dc-068', 'j8dc-069', 'j8dc-070', 'j8dc-071', 'j8dc-072', 'j8dc-073', 'j8dc-074', 'j8dc-075', 'j8dc-076', 'j8dc-077', 'j8dc-078', 'j8dc-079', 'j8dc-080', 'j8dc-081', 'j8dc-082', 'j8dc-083', 'j8dc-084', 'j8dc-085', 'j8dc-086', 'j8dc-087', 'j8dc-088', 'j8dc-089', 'j8dc-090']

client = boto3.client('cloudformation',region_name='us-west-2')

for stack in stack_list:
	response = client.delete_stack(
		StackName = stack,
		)
	print ('Deleting stack with name %s' % stack)
	print (response)