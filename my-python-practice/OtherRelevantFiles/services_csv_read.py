# sample program to extract values from CSV file
import ast
import io
import json
import pandas as pd

plugins = {}
data = []
serviceNmList = []
service = {}

fileName = '/Users/arajagopalan/Downloads/Copy of FedRAMP Central Supporting Services - discovered-micros-svcs.csv'

df = pd.read_csv(fileName, index_col=0, header=2, usecols=[0,1])
print(df)
serviceName = df[0]