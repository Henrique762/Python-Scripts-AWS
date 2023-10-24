import os

name_alb = str(input('Digite o nome dos ALBs separados por vírgula ",":'))
region = str(input('Insira a região:'))
albs = name_alb.split(',')
caminho = os.getcwd()
arquivos = os.listdir(caminho)

if 'albs' in arquivos:
    pass
else:
    os.mkdir('albs')

for alb in albs:
    salvando_arquivo = os.system(f'aws elbv2 describe-load-balancers --names {alb} --region {region} --output json > albs/alb_{alb}.json')

print('Dá uma olhada na pasta "albs"')