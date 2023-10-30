import sys
import os

# Obtenha o diretório atual do cloudfront_function.py
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construa o caminho para a "linuxscripts" e adicione ao sys.path
linuxscripts_path = os.path.join(current_dir, '..', 'linuxscripts')
sys.path.append(linuxscripts_path)

import boto3

cf_client = boto3.client('cloudfront')

def cloudfront():
    response = cf_client.get_distribution(
        Id='E3E2ZJ5KM4U3TY'
    )
    id = response['Distribution']['Id']
    domainname = response['Distribution']['DomainName']
    arn = response['Distribution']['ARN']
    #sslcertificate =
    #logbucket =
    #logprefix =
    #cookielogin =
    #priceclass =
    webaclid = response['DistributionConfig']['Webaclid']
    originname = response['DistributionConfig']['Origin']['Id']
    origindomain = response['DistributionConfig']['Origin']['DomainName']
    


    commands_linux.arquivo(domainname, id, arn, webaclid, originname, origindomain)

cloudfront()