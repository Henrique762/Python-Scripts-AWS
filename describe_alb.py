import os

##### Input de Informações ######
serviço = str(input('Digite o nome do serviço que deseja as informações (CloudFront, ALB ou VPC):'))
account = str(input('Insira o ID da Conta:'))
region = str(input('Insira a região:'))
##### Ciriação de Arquivos #####
caminho = os.getcwd()
arquivos = os.listdir(caminho)
if account in arquivos:
    pass
else:
    os.makedirs(f'Contas/{account}/{serviço}')

if serviço == 'Cloudfront':
    cfescolha1 = str(input('Você deseja informação de Todos os Recursos?'))
    pass
elif serviço == 'ALB':
    albescolha1 = str(input('Você deseja informação de Todos os Recursos?(s/n)'))
    if albescolha1 == 's':
        arquivo_temporario = 'temp_resources.txt'
        os.system("aws elbv2 describe-load-balancers --region us-east-1 | grep LoadBalancerName | awk -F'\"' '{{print $4}}' > {}".format(arquivo_temporario))
        read_arq = open(arquivo_temporario)
        for alb in read_arq:
            print(alb)
            print(f"aws elbv2 describe-load-balancers --names {alb} --output json > testes/alb_{alb}.json")
    elif albescolha1 == 'n':
        name_alb = str(input('Digite o nome dos ALBs separados por vírgula ",":'))
        albs = name_alb.split(',')
        for alb in albs:
            os.system(f'aws elbv2 describe-load-balancers --names {alb} --region {region} --output json > Contas/{account}/ALB/alb_{alb}.json')
    else:
        print('Responda só (s/n)')
        pass
elif serviço == 'VPC':
    pass




print('Dá uma olhada na pasta "Contas"')