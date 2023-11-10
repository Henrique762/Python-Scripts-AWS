import os
import boto3
import sys
from cloudfront_function import cloudfront
from eks_function import clustereks
from commands_linux import arquivo_cf, arquivo_eks, pastas
import time

# Obtenha o diretório atual do describe_alb.py
current_dir = os.path.dirname(os.path.abspath(__file__))
 
# Construa o caminho para a "linuxscripts" e adicione ao sys.path
linuxscripts_path = os.path.join(current_dir, '..', 'linuxscripts')
sys.path.append(linuxscripts_path)

##### Input de Informações ######
service = str(input('Digite o nome do serviço que deseja as informações (CloudFront, ALB ou EKS):'))
account = str(input('Insira o ID da Conta:'))
region = str(input('Insira a região:'))

path_pasta = pastas(account, service)

if service == 'CloudFront':
    cloudfront(path_pasta, region)


elif service == 'EKS':
    clustereks(path_pasta, region)
##elif serviço == 'ALB':
##    albescolha1 = str(input('Você deseja informação de Todos os Recursos?(s/n)'))
##    if albescolha1 == 's':
##        arquivo_temporario = 'temp_resources.txt'
##        os.system("aws elbv2 describe-load-balancers --region us-east-1 | grep LoadBalancerName | awk -F'\"' '{{print $4}}' > {}".format(arquivo_temporario))
##        read_arq = open(arquivo_temporario)
##        for alb in read_arq:
##            print(alb)
##            print(f"aws elbv2 describe-load-balancers --names {alb} --output json > testes/alb_{alb}.json")
##    elif albescolha1 == 'n':
##        name_alb = str(input('Digite o nome dos ALBs separados por vírgula ",":'))
##        albs = name_alb.split(',')
##        for alb in albs:
##            os.system(f'aws elbv2 describe-load-balancers --names {alb} --region {region} --output json > Contas/{account}/ALB/alb_{alb}.json')
##    else:
##        print('Responda só (s/n)')
##        pass
##elif serviço == 'VPC':
##    pass
print('Dá uma olhada na pasta "Contas"')