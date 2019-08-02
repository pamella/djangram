# :rocket: Djangram (django + instagram)
Repositório do sistema elaborado para as aulas do curso de Django, realizado na Jornada de Cursos 2019 do [@CITiUFPE](https://github.com/citiufpe).

## Deploy
* Deploy realizado no Heroku (link abaixo)
```bash
https://djangram.herokuapp.com/
```

## Material de apoio
* [Slides](https://docs.google.com/presentation/d/1sCEYy_X6CcBXsYG0vXJsIuFzy1n9NiflDpMIuDY2VVM/edit#slide=id.g5d9a19172a_0_0)
* [Requisitos do projeto](https://gist.github.com/pamella/e4eb1427a242b75be17bd29e25e54377)

Obs.: Nas anotações dos slides, há links de referência e aprofundamento.

## Como utilizar
* Clone o projeto para seu computador
  ```bash
  $ git clone https://github.com/pamella/djangram.git
  ```
* Inicie um ambiente virtual e instale as dependências
  ```bash
  $ python3 -m venv env
  $ source env/bin/activate
  $ pip install -r requirements.txt
  ```
* Rode as migrações
  ```bash
  $ python manage.py migrate
  ```
* Inicie o servidor
  ```bash
  $ python manage.py runserver
  ```
  
