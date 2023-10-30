import sys
import os
 
# Obtenha o diretório atual do cloudfront_function.py
current_dir = os.path.dirname(os.path.abspath(__file__))
 
# Construa o caminho para a "linuxscripts" e adicione ao sys.path
linuxscripts_path = os.path.join(current_dir, '..', 'linuxscripts')
sys.path.append(linuxscripts_path)

from commands_linux import loadbalancer_file

import boto3

elbv1_client = boto3.client('elb')
elbv2_client = boto3.client('elbv2')

def loadbalancer():

    response = elbv2_client.describe_load_balancers()

    for load_balancer in response['LoadBalancers']:

        # Extrair informações
        name = "null"
        project = "null"
        environment = "null"
        lbname = load_balancer['LoadBalancerName']
        lbtype = load_balancer['Type']
        lbstate = load_balancer['State']['Code']
        lbscheme = load_balancer['Scheme']
        vpc_id = load_balancer['VpcId']
        subnets = [subnet['SubnetId'] for subnet in load_balancer['AvailabilityZones']]
        availability_zone = [az['ZoneName'] for az in load_balancer['AvailabilityZones']]

        #Verificação de TAGs básicas
        tag_response = elbv2_client.describe_tags(
            ResourceArns= [load_balancer['LoadBalancerArn']]
        )
        for tag_description in tag_response['TagDescriptions']:
            for tag in tag_description['Tags']:
                if tag['Key'] == 'Name':
                    name = tag['Value']
                elif tag['Key'] == 'Project':
                    project = tag['Value']
                elif tag['Key'] == 'Environment':
                    environment = tag['Value']

        #Create file
        output_file = f'{lbname}_loadbalancer.txt'
        loadbalancer_file(name, project, environment, lbname, lbtype, lbstate, lbscheme, vpc_id, subnets, availability_zone, output_file)
    
    return {'message': 'created file with load balancer info'}

loadbalancer()