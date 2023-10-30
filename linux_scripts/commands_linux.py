import os

def arquivo( id: str, domainname: str, arn: str, sslcertificate: str, logbucket: str, logprefix: str, cookielogin: str, priceclass: str, webaclid: str, originname: str, origindomain: str ):
    arq = str(f""" cat << EOF > cloudformation.txt
Distribution ID: {domainname}
ARN: {arn}
Domain Name: {id}
SSL Certificate: {sslcertificate}
Log Bucket: {logbucket}
Log Prefix: {logprefix}
Cookie Logging: {cookielogin}
Price Class: {priceclass}
AWS WAF: {webaclid}
Origins:
    Origin Name: {originname}
    Origin Domain: {origindomain}
EOF""")
    os.system(arq)