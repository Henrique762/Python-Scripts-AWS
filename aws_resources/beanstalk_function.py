import boto3
import sys
import os
# Obtenha o diretório atual do eks_function.py
current_dir = os.path.dirname(os.path.abspath(__file__))
 
# Construa o caminho para a "linuxscripts" e adicione ao sys.path
linuxscripts_path = os.path.join(current_dir, '..', 'linuxscripts')
sys.path.append(linuxscripts_path)

region = "us-east-1"

def beanstalk(path_pasta, region):
    beanstalk_client = boto3.client('elasticbeanstalk', regin_name=f'{region}')
    
    response = beanstalk_client.describe_environments()

    for environment in response['Environment']:
        ebs_name = environment['EnvironmentName']
        ebs_application = environment['ApplicaitonName']
        ebs_cname = environment['CNAME']
        ebs_environment_id = environment['EnvironmentId']
        ebs_so_and_Language = environment['SolutionStackName']
        ebs_arn = environment['EnvironmentArn']

        ebs_tier = environment['Tier']['Name']
        ebs_tier = environment['Tier']['Type']

        ebs_loadbalancer = environment['Resources']['LoadBalancer']['LoadBalancerName']

        #Create file
        output_file = f'{ebs_name}_ElasticBeasntalk.txt'