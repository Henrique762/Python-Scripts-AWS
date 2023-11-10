import os
import boto3
import sys
from aws_resources.cloudfront_function import cloudfront
from aws_resources.eks_function import clustereks
from aws_resources.loadbalancer_function import loadbalancer
from linuxscripts.commands_linux import arquivo_cf, arquivo_eks, pastas


##### Input de Informações ######
service = str(input('Digite o nome do serviço que deseja as informações (CloudFront, ALB ou EKS):'))
account = str(input('Insira o ID da Conta:'))
region = str(input('Insira a região:'))

path_pasta = pastas(account, service)

if service == 'CloudFront':
    cloudfront(path_pasta, region)

elif service == 'EKS':
    clustereks(path_pasta, region)

elif service == 'ALB':
    loadbalancer()

print('Dá uma olhada na pasta "Contas"')