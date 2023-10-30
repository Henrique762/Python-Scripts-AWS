import os

def arquivo( id: str, domainname: str, arn: str, sslcertificate: str, logbucket: str, logprefix: str, cookielogin: str, priceclass: str, webaclid: str, originname: str, origindomain: str, path_pasta: str ):
    output_file = f"{caminho}/{id}_cloudfront.txt"
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

def pastas(account: str, service: str):
    caminho = os.getcwd()
    diretorio = f'{caminho}/Contas/{account}/{service}'
    if os.path.exists(diretorio):
        pass
    else:
        os.makedirs(f'Contas/{account}/{service}')    
    return diretorio