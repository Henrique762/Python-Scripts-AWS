import os

def arquivo( id: str, domainname: str, arn: str, webaclid: str, originname: str, origindomain: str ):
    arq = str(f""" cat << EOF >> cloudformation.txt
Name:
Distribution ID: {id}
ARN: {arn}
Domain Name: {domainname}
SSL Certificate:
Log Bucket:
Log Prefix:
Cookie Logging:
Price Class:
AWS WAF: {webaclid}
Origins:
    Origin Name: {originname}
    Origin Domain: {origindomain}
EOF""")
    os.system(arq)


def loadbalancer_file(name: str, project: str, env: str, lbname: str, lbtype: str, lbstate: str, lbscheme: str, vpc_id: str, subnets: str, azs: str, output_file: str):
    #Verificação da existência do arquivo
    if os.path.exists(output_file):
        with open(output_file, "w") as file:
            file.truncate(0)  #Remove o conteúdo do arquivo

        print(f"Conteúdo do arquivo {output_file} foi removido.")
    else:
        with open(output_file, "w") as file:
            file.write(f"Load Balancer File '{account_id}'")

        print(f"O arquivo {output_file} foi criado com conteúdo inicial.")

    with open(output_file, "w") as file:
        file.write(f"""\n
                   Name: '{name}'
                   Project: '{project}'
                   Environment: '{env}'
                   Load Balancer Name: '{lbname}'
                   Type: '{lbtype}'
                   State: '{lbstate}'
                   Scheme: '{lbscheme}'
                   
                   Network
                   VpcId: '{vpc_id}'
                   Subnets: '{subnets}'
                   Availability Zone: '{azs}'\n""")
    return {'message': f'file {output_file} created'}