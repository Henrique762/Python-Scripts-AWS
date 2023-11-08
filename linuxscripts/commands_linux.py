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


def loadbalancer_file(name: str, project: str, env: str, lbname: str, arn: str, lbtype: str, lbstate: str, lbscheme: str, vpc_id: str, subnets: str, azs: str, tg: str, log: str, waf:str, output_file: str):
    #Verificação da existência do arquivo
    if os.path.exists(output_file):
        with open(output_file, "w") as file:
            file.truncate(0)  #Remove o conteúdo do arquivo
            file.write(f"Load Balancer File")
        print(f"Conteúdo do arquivo {output_file} foi removido.")

    else:
        with open(output_file, "w") as file:
            file.write(f"Load Balancer File")
        print(f"O arquivo {output_file} foi criado com conteúdo inicial.")

    # Converter as variáveis que podem ser listas em formato de lista
    subnets = subnets if isinstance(subnets, list) else [subnets]
    azs = azs if isinstance(azs, list) else [azs]
    tg = tg if isinstance(tg, list) else [tg]

    #Formatar as listas com "-"
    subnets_str = "\n- ".join(subnets)
    azs_str = "\n- ".join(azs)
    tg_str = "\n- ".join(tg)

    with open(output_file, "w") as file:
        file.write(f"""
Name: {name}
Project: {project}
Environment: {env}
Load Balancer Name: {lbname}
Type: {lbtype}
State: {lbstate}
Scheme: {lbscheme}

Target Groups
TG:
- {tg_str}

Network
VpcId: {vpc_id}
Subnets:
- {subnets_str}
Availability Zone:
- {azs_str}

Atributos
Logs: {log}
WAF: {waf}
""")
    return {'message': f'file {output_file} created'}