# Desafio Pub Future

Opa! Esse aqui é o repositorio para o Programa de Formação da Proway em conjuto com a Pública Tecnologia, este projeto foi feito em Python(Django), JavaScipt(AJAX), HTML, CSS, e Bootstrap. Sendo necessario baixar somento o Python e PIP para a utilização do codigo. **Só lembrando que quando cadastrando alguma coisa devera seguir as instruções seguidas, se não o programa irá dar erro e não fazer as operações necessarias.**
Ps: Um amigo tentou rodar meu programa e deu um *erro* na criação da receita, e só deu erro na maquina dele outras pessoas rodaram o programa e deu tudo certo, mas não faço ideia como concertar :(

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
O codigo é formado por 3 diretorios principais: mainpage, profiles, e Publica. O diretorio publica possui todos os arquivos necessarios usador globalmente, como por exemplo o ```url.py``` que possui todas as urls globais
