import boto3
import sys
import os
 
# Obtenha o diretório atual do cloudfront_function.py
current_dir = os.path.dirname(os.path.abspath(__file__))
 
# Construa o caminho para a "linuxscripts" e adicione ao sys.path
linuxscripts_path = os.path.join(current_dir, '..', 'linux_scripts')
sys.path.append(linuxscripts_path)

from commands_linux import arquivo

cf_client = boto3.client('cloudfront', region_name='us-east-1')
    
def cloudfront(path_pasta):

    cfescolha = str(input('Você deseja informação de Todos os Recursos?'))

    if cfescolha == 's':
        response = cf_client.list_distributions()
        ##for cf in response['DistributionList']['Items'][0]['Id']:
        for cf in response['DistributionList']['Items']:
            cf = cf['Id']
            response = cf_client.get_distribution(
                Id= f'{cf}'
            )
            print(cf)
            domainname = response['Distribution']['Id']
            id = response['Distribution']['DomainName']
            arn = response['Distribution']['ARN']
            sslcertificate = 'null'
            ##sslcertificate = response['Distribution']['DistributionConfig']['ViewerCertificate']['ACMCertificateArn']
            logbucket = response['Distribution']['DistributionConfig']['Logging']['Bucket']
            logprefix = response['Distribution']['DistributionConfig']['Logging']['Prefix']
            cookielogin = str(response['Distribution']['DistributionConfig']['Logging']['IncludeCookies'])
            priceclass = response['Distribution']['DistributionConfig']['PriceClass']
            webaclid = response['Distribution']['DistributionConfig']['WebACLId']
            originname = response['Distribution']['DistributionConfig']['Origins']['Items'][0]['Id']
            origindomain = response['Distribution']['DistributionConfig']['Origins']['Items'][0]['DomainName']
            arquivo(domainname, id, arn, sslcertificate, logbucket, logprefix, cookielogin, priceclass, webaclid, originname, origindomain, caminho)

    elif cfescolha == 'n':
        lista_id_cf = str(input('Digite o ID da Distribuição separados por vírgula ",":'))
        lista_id_cf = lista_id_cf.split(',')
        for cf in lista_id_cf:
            print(f'Esse é o id{cf}')
            response = cf_client.get_distribution(
                Id= f'{cf}'
            )
            domainname = response['Distribution']['Id']
            id = response['Distribution']['DomainName']
            arn = response['Distribution']['ARN']
            sslcertificate = response['Distribution']['DistributionConfig']['ViewerCertificate']['ACMCertificateArn']
            logbucket = response['Distribution']['DistributionConfig']['Logging']['Bucket']
            logprefix = response['Distribution']['DistributionConfig']['Logging']['Prefix']
            cookielogin = str(response['Distribution']['DistributionConfig']['Logging']['IncludeCookies'])
            priceclass = response['Distribution']['DistributionConfig']['PriceClass']
            webaclid = response['Distribution']['DistributionConfig']['WebACLId']
            originname = response['Distribution']['DistributionConfig']['Origins']['Items'][0]['Id']
            origindomain = response['Distribution']['DistributionConfig']['Origins']['Items'][0]['DomainName']

            arquivo(domainname, id, arn, sslcertificate, logbucket, logprefix, cookielogin, priceclass, webaclid, originname, origindomain, path_pasta)