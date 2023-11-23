import sys
import os
 
# Obtenha o diretório atual do cloudfront_function.py
current_dir = os.path.dirname(os.path.abspath(__file__))
 
# Construa o caminho para a "linuxscripts" e adicione ao sys.path
linuxscripts_path = os.path.join(current_dir, '..', 'linuxscripts')
sys.path.append(linuxscripts_path)

from commands_linux import loadbalancer_file

import boto3


def loadbalancer(path_pasta, region):

    elbv1_client = boto3.client('elb', region_name=f'{region}')
    elbv2_client = boto3.client('elbv2', region_name=f'{region}')

    response = elbv2_client.describe_load_balancers()

    for load_balancer in response['LoadBalancers']:

        # Extrair informações
        name = 'null'
        project = 'null'
        environment = 'null'
        lbname = load_balancer['LoadBalancerName']
        arn = load_balancer['LoadBalancerArn']
        lbtype = load_balancer['Type']
        lbstate = load_balancer['State']['Code']
        lbscheme = load_balancer['Scheme']

        target_groups = elbv2_client.describe_target_groups(LoadBalancerArn=arn)
        tg = [tg_id['TargetGroupArn'] for tg_id in target_groups['TargetGroups']]

        vpc_id = load_balancer['VpcId']
        subnets = [subnet['SubnetId'] for subnet in load_balancer['AvailabilityZones']]
        availability_zone = [az['ZoneName'] for az in load_balancer['AvailabilityZones']]
        
        log = 'null'
        waf = 'null'

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
        
        #Verificar a existência de logs e WAF
        attribute_response = elbv2_client.describe_load_balancer_attributes(LoadBalancerArn=arn)
        for attribute in attribute_response['Attributes']:
            if attribute['Key'] == 'access_logs.s3.enabled':
                log = attribute['Value']
            elif attribute['Key'] == 'waf.enabled':
                waf = attribute['Value']

        #Create file
        output_file = f'{lbname}_loadbalancer.txt'
        loadbalancer_file(name, project, environment, lbname, arn, lbtype, lbstate, lbscheme, vpc_id, subnets, availability_zone, tg, log, waf, output_file, path_pasta)
    
    return {'message': 'created file with load balancer info'}