import os

def pastas(account: str, service: str):
    caminho = os.getcwd()
    diretorio = f'{caminho}/Contas/{account}/{service}'
    if os.path.exists(diretorio):
        pass
    else:
        os.makedirs(f'Contas/{account}/{service}')    
    return diretorio


def arquivo_cf( id: str, domainname: str, arn: str, sslcertificate: str, logbucket: str, logprefix: str, cookielogin: str, priceclass: str, webaclid: str, originname: str, origindomain: str, path_pasta: str ):
    output_file = f"{path_pasta}/{id}_cloudfront.txt"
    if os.path.exists(output_file):
        with open(output_file, "w") as file:
            file.truncate(0)  #Remove o conteúdo do arquivo
    ##else:
    ##    with open(output_file, "w") as file:
    ##        file.write(f"Load Balancer File '{account_id}'")
    with open(output_file, "w") as file:
        file.write(f"""
Distribution ID: {id}
ARN: {arn}
Domain Name: {domainname}
SSL Certificate: {sslcertificate}
Log Bucket: {logbucket}
Log Prefix: {logprefix}
Cookie Logging: {cookielogin}
Price Class: {priceclass}
AWS WAF: {webaclid}
Origins:
    Origin Name: {originname}
    Origin Domain: {origindomain}
""")
        
def arquivo_eks( id: str, arn: str, version: str, endpoint: str, rolearn: str, vpcid: str, subnets: str, sgs: str, sgscluster: str, logs: str, path_pasta: str ):
    output_file = f"{path_pasta}/{id}_eks.txt"
    if os.path.exists(output_file):
        with open(output_file, "w") as file:
            file.truncate(0)  #Remove o conteúdo do arquivo
    ##else:
    ##    with open(output_file, "w") as file:
    ##        file.write(f"Load Balancer File '{account_id}'")
    with open(output_file, "w") as file:
        file.write(f"""
Name Cluster: {id}
ARN: {arn}
Version: {version}
Endpoint: {endpoint}
Role ARN: {rolearn}
Vpc ID: {vpcid}
Subnets: {subnets}
Securitys Groups: {sgs}
Cluster Security Groups: {sgscluster}
Logging: {logs}

NodeGroups:
""")
        
def nodegroup_infos(id, name, arn, version, rolearn, subnets, capacitytype, asgnodegroups, scalingconfig, instancetype, file):
    ##output_file = f"{path_pasta}/{id}_eks.txt"
    ##with open(output_file, "a") as file:
    file.write(f"""
Name Nodegroup: {name}
Name Cluster: {id}
ARN: {arn}
Version: {version}
Role ARN: {rolearn}
Subnets: {subnets}
Capacity Type = {capacitytype}
Auto Scaling = {asgnodegroups}
Scaling Configs: {scalingconfig}
Instance Type = {instancetype}
""")

