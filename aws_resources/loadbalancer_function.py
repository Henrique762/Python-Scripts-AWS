import sys
import os
 
# Obtenha o diretório atual do cloudfront_function.py
current_dir = os.path.dirname(os.path.abspath(__file__))
 
# Construa o caminho para a "linuxscripts" e adicione ao sys.path
linuxscripts_path = os.path.join(current_dir, '..', 'linuxscripts')
sys.path.append(linuxscripts_path)

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
        lbstate = load_balancer['State']
        lbscheme = load_balancer['Scheme']
        vpc_id = load_balancer['VpcId']
        subnets = load_balancer['AvailabilityZones']
        availability_zone = [az['ZoneName'] for az in load_balancer['AvailavilityZones']]

        #Verificação de TAGs básicas
        for tag in load_balancer['Tags']:
            if tag['Key'] == 'Name':
                name = tag['Value']
            elif tag['Key'] == 'Project':
                project = ['Value']
            elif tag['Key'] == 'Environment':
                environment = ['Value']

        #Create file
        output_file = f'{lbname}_loadbalancer.txt'
        commands_linux.loadbalancer_file(name, project, environment, lbname, lbtype, lbstate, lbscheme, vpc_id, subnets, availability_zone, output_file)
    
    return {'message': 'created file with load balancer info'}

loadbalancer()