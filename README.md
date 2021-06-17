# Cloud Guardians
Este repositório contem todo o projeto de engenharia de dados do grupo Cloud Guardians ensinado na academia de Cloud AWS oferecido pela Accenture e Gama Academy. Abaixo segue as instruções para que o projeto possa funcionar corretamente:

## Instalação de Dependências:
Você pode instalar corretamente todos as dependências, rodando o seguinte comando na raiz do projeto:
```cmd
pip install -r requirements.txt
```
** Caso você esteja utilizando ambientes virtuais, lembre-se de estar dentro do ambiente para efetuar a instalação correta das dependências

## Credenciais de Serviços
Para que o projeto possa realizar os processos de integração de dados nos serviços da AWS é necessário inserir as credenciais no arquivo ```credentials.ini```:
```
[boto3]
service_name = Insira_seu_service_name
region_name = insira_regiao_utilizada
aws_access_key_id = Insira_aqui_seu_key_id
aws_secret_access_key = Insira_aqui_seu_access_key

[RDS]
host = Insira_seu_host_RDS
user = Insira_seu_user
password = Insira_sua_senha
database = Insira_sua_DataBase

[S3]
bucket_name = Insira_bucket_name
```

* No indice de nome ```[boto3]``` você irá inserir as chaves de acesso/credenciais de longo prazo para um usuário do IAM, para mais informações você pode acessar a [documentação](https://docs.aws.amazon.com/pt_br/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey);
* No indice de nome ```[RDS]``` você irá inserir as credencias de acesso ao banco criado na estrutura AWS,para mais informações você pode acessar a [documentação](https://docs.aws.amazon.com/pt_br/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html);
* No indice de nome ```[S3]``` você irá inserir o nome do bucket criado na AWS, para mais informações você pode acessar a [documentação](https://docs.aws.amazon.com/pt_br/AmazonS3/latest/userguide/create-bucket-overview.html);

## Criação da base de dados
Para que o projeto posso funcionar corretamente o banco deve ser criado assim que o RDS for inicializado, para auxiliar nesta criação existe um script na pasta: ```.cloud_guardians/scripts_db/criacao_banco_api_covid.sql```
