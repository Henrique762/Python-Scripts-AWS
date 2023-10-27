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



