# Desafio Rede Vistorias

## Instruções de instalação

1. Install python3 requirements
```
pip3 install -r requirements.txt
```
2. Make sure you have postres instaled and follow these steps:
```
sudo psql -U postgres
```
In postgres cli:
```
postgres=# CREATE USER “your_username” WITH PASSWORD “your_pass”;
postgres=# CREATE DATABASE db_name WITH OWNER your_username;
```
3. Create a .env file on the root directory of the project:
```
vim .env
```
write the db connection parameters and save the file:
```
DB_NAME=db_name
DB_USER=your_username
DB_PASS=your_pass
```
4. Run migrations
```
python3 manage.py makemigrations
python3 manage.py migrate
```
5. Finally insert the data on the created
```
psql -U postgres -d db_name < populate.sql
```
You are done!!
## Instruções de uso
```
python3 manage.py runserver
```
