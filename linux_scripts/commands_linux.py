import os

def arquivo(domainname: str, ):
    arq = str(f""" cat << EOF >> cloudformation.txt
Name:
Distribution ID:
ARN:
Domain Name: 
SSL Certificate:
Log Bucket:
Log Prefix:
Cookie Logging:
Price Class:
AWS WAF
Origins
EOF""")
    os.system(arq)



