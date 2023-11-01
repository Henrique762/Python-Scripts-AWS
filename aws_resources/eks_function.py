import boto3
import sys
import os
 
# Obtenha o diretório atual do eks_function.py
current_dir = os.path.dirname(os.path.abspath(__file__))
 
# Construa o caminho para a "linuxscripts" e adicione ao sys.path
linuxscripts_path = os.path.join(current_dir, '..', 'linux_scripts')
sys.path.append(linuxscripts_path)

from commands_linux import arquivo_eks, nodegroup_infos

path_pasta = '/home/hq/Estudos/Python-Scripts-AWS/contas'
region = 'us-east-1'
def clustereks(path_pasta, region):

    eks_client = boto3.client('eks', region_name=f'{region}')

    ekscluster = str(input('Você deseja informação de Todos os Recursos?'))

    if ekscluster == 's':
        list_clusters = eks_client.list_clusters()
        
        for clusters in list_clusters['clusters']:
            eks = clusters

            response = eks_client.describe_cluster(
            name=f'{eks}'
            )
            list_nodegroups = eks_client.list_nodegroups(
            clusterName=f'{eks}'
            )
            for nodegroup in list_nodegroups['nodegroups']:
                response_nodegroup = eks_client.describe_nodegroup(
                clusterName=f'{eks}',
                nodegroupName=f'{nodegroup}'
                )
                namenodegroup =  response_nodegroup['nodegroup']['nodegroupName']
                nodegrouparn =  response_nodegroup['nodegroup']['nodegroupArn']
                nodegroupsubnets =  response_nodegroup['nodegroup']['subnets'] 
                noderole = response_nodegroup['nodegroup']['nodeRole']
                nodegroupversion =  response_nodegroup['nodegroup']['version']
                capacitytype =  response_nodegroup['nodegroup']['capacityType']
                scalingconfig =  response_nodegroup['nodegroup']['scalingConfig']
                instancetype =  response_nodegroup['nodegroup']['instanceTypes']
                asgnodegroups =  response_nodegroup['nodegroup']['resources']['autoScalingGroups']
            
            ######## Cluster #################
                name = response['cluster']['name']
                arn = response['cluster']['arn']
                version = response['cluster']['version']
                endpoint = response['cluster']['endpoint'] 
                rolearn = response['cluster']['roleArn']
                vpcid = response['cluster']['resourcesVpcConfig']['vpcId']
                subnets = response['cluster']['resourcesVpcConfig']['subnetIds'][0]
                securitygroups = response['cluster']['resourcesVpcConfig']['securityGroupIds'][0]
                clustersecuritygroup = response['cluster']['resourcesVpcConfig']['clusterSecurityGroupId']
                logging_types =  response['cluster']['logging']['clusterLogging'][0]['types']
                
                arquivo_eks(name, arn, version, endpoint, rolearn, vpcid, subnets, securitygroups, clustersecuritygroup, logging_types, path_pasta)
                nodegroup_infos(eks, namenodegroup, nodegrouparn, nodegroupversion, noderole, nodegroupsubnets, capacitytype, asgnodegroups, scalingconfig, instancetype, path_pasta)

            
    
    elif ekscluster == 'n':
        lista_name_eks = str(input('Digite o nome dos Clusters separados por vírgula ",":'))
        lista_name_eks = lista_name_eks.split(',')
        for eks in lista_name_eks:
            response = eks_client.describe_cluster(
            name=f'{eks}'
            )

            name = response['cluster']['name']
            arn = response['cluster']['arn']
            version = response['cluster']['version']
            endpoint = response['cluster']['endpoint'] 
            rolearn = response['cluster']['roleArn']
            vpcid = response['cluster']['resourcesVpcConfig']['vpcId']
            subnets = response['cluster']['resourcesVpcConfig']['subnetIds'][0]
            securitygroups = response['cluster']['resourcesVpcConfig']['securityGroupIds'][0]
            clustersecuritygroup = response['cluster']['resourcesVpcConfig']['clusterSecurityGroupId']
            logging_types =  response['cluster']['logging']['clusterLogging'][0]['types']

            arquivo_eks(name, arn, version, endpoint, rolearn, vpcid, subnets, securitygroups, clustersecuritygroup, logging_types, path_pasta)

            list_nodegroups = eks_client.list_nodegroups(
            clusterName=f'{eks}'
            )
            for nodegroup in list_nodegroups['nodegroups']:
                response_nodegroup = eks_client.describe_nodegroup(
                clusterName=f'{eks}',
                nodegroupName=f'{nodegroup}'
                )
                namenodegroup =  response_nodegroup['nodegroup']['nodegroupName']
                nodegrouparn =  response_nodegroup['nodegroup']['nodegroupArn']
                nodegroupsubnets =  response_nodegroup['nodegroup']['subnets'] 
                noderole = response_nodegroup['nodegroup']['nodeRole']
                nodegroupversion =  response_nodegroup['nodegroup']['version']
                capacitytype =  response_nodegroup['nodegroup']['capacityType']
                scalingconfig =  response_nodegroup['nodegroup']['scalingConfig']
                instancetype =  response_nodegroup['nodegroup']['instanceTypes']
                asgnodegroups =  response_nodegroup['nodegroup']['resources']['autoScalingGroups']
                
                nodegroup_infos(eks, namenodegroup, nodegrouparn, nodegroupversion, noderole, nodegroupsubnets, capacitytype, asgnodegroups, scalingconfig, instancetype, path_pasta)



clustereks(path_pasta, region)