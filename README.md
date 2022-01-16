# Desafio Pub Future

Opa! Esse aqui é o repositório para o Programa de Formação da Proway em conjunto com a Pública Tecnologia, este projeto foi feito em Python(Django), JavaScript(AJAX), HTML, CSS, e Bootstrap. Sendo necessário baixar somente o Python e PIP para a utilização do código. 

## Defeitos do Código
-  O codigo dará erro sempre que alguma formatação estiver errada, então por favor fique atento Datas, Numeros formatados do jeito certo
-  Um amigo tentou rodar um programa e deu um erro na criação da receita, e só deu erro na maquina dele outras pessoas rodaram o programa e deu tudo certo, mas não faço ideia como concertar :(
-  Quando estava fazendo o codigo estava dando muitos erros com saldo com float, mesmo que eu perca um pouco de pontos neste processo preferi trocar para somente aceitar numeros inteiros

## Rodando o programa:
Execute:
```bash
pip install -r requirements.TXT
cd src
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
## Analisando o programa:
O código é formado por 3 diretórios principais: mainpage, profiles, e Pública. O diretório pública possui todos os arquivos necessários usador globalmente, como por exemplo o ```url.py``` que possui todas as urls globais. Dentro da mainpage, profile possuem basicamente:
- ```Models``` Nesse arquivo aonde sera declarado as tabelas do banco de dados
- ```Admin``` Nesse arquivo aonde sera declarado as tabelas que serão mostradas no ```/admin/```
- ```Apps``` Arquivo de configuração de app, assim são chamados as diferentes partes do projeto, no meu caso existem dois mainpage e profiles
- ```Signals``` Não é um arquivo base django, toda vez que é criado um User na database um signal é ativado para criar um item na tabela Profile com um OneToOneField de um user.
- ```Urls``` Neste arquivo terá uma lista de cada URL,sendo um ```Path('url do site', função no arquivo views do mesmo diretorio, name='nome')```
- ```Views``` Aqui tera todas as funções logicas do backend do site
- ```Template``` Neste diretorio tera todos os HTML da página
## Admin
Por padrão o Django possui o /admin, para editar diretamente o usuario e ver como o banco de dados é feito, alem disso depois de logar dentro do /admin tente logar normalmente no site, e já tera algumas contas com receitas para testar o programa.
#### Usuario : ```ADMIN```
#### Senha : ```admin```
