import boto3
import sys
import os
# Obtenha o diretório atual do eks_function.py
current_dir = os.path.dirname(os.path.abspath(__file__))
 
# Construa o caminho para a "linuxscripts" e adicione ao sys.path
linuxscripts_path = os.path.join(current_dir, '..', 'linuxscripts')
sys.path.append(linuxscripts_path)

region = "us-east-1"

def vpcs(path_pasta, region):
    vpc_client = boto3.client('ec2', regin_name=f'{region}')
    