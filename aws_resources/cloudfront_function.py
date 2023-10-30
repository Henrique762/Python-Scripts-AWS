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

    

lista = ['EEHGHIG92SRKZ']
resposta = 's'


def cloudfront(resposta, lista):
    if resposta == 's':
        pass
    elif resposta == 'n':

        for cf in lista:
            print(f'Esse é o id{cf}')
            response = cf_client.get_distribution(
                Id={cf}
            )
            id = response['Distribution']['Id']
            domainname = response['Distribution']['DomainName']
            arn = response['Distribution']['ARN']
            sslcertificate = response['Distribution']['DistributionConfig']['ViewerCertificate']['ACMCertificateArn']
            logbucket = response['Distribution']['DistributionConfig']['Logging']['Bucket']
            logprefix = response['Distribution']['DistributionConfig']['Logging']['Prefix']
            cookielogin = str(response['Distribution']['DistributionConfig']['Logging']['IncludeCookies'])
            priceclass = response['Distribution']['DistributionConfig']['PriceClass']
            webaclid = response['Distribution']['DistributionConfig']['WebACLId']
            originname = response['Distribution']['DistributionConfig']['Origins']['Items'][0]['Id']
            origindomain = response['Distribution']['DistributionConfig']['Origins']['Items'][0]['DomainName']
    
            ##todos_recursos = [domainname, id, arn, sslcertificate, ##logbucket, logprefix, cookielogin, priceclass, webaclid, originname, origindomain]
    
            ##for recursos in todos_recursos:
                ##if recursos == None or recursos == '':
                   ## recursos = 'Não esta Habilitado'
    
    
            arquivo(domainname, id, arn, sslcertificate, logbucket, logprefix, cookielogin, priceclass, webaclid, originname, origindomain)


cloudfront(resposta, lista)

