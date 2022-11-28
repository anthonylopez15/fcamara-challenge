# Desafio FCamara

1. [Tecnologias](#tecnologias)
2. [Padrão de Projeto](#padrão-de-projeto)
3. [Rodar com Docker](#rodar-com-docker)
4. [Rotas](#rotas)
5. [Authentication](#authentication)
6. [Pytest](#pytest)
7. [Rodar localmente](#rodar-localmente)


## Tecnologias
- Python 3.8
- FastAPI
- docker-compose
- Pytest
- Pre-commit

## Padrão de Projeto
- Foi usado a [Clean architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) como padrão de projeto.
- Fluxo: `application <-> controllers <-> use case <-> repository/entity`.

## Rodar com Docker
- Rodar o projeto com docker-compose: `$ docker-compose up -d`
- Swagger ui link: http://localhost:8000/docs.

## Rotas
- path: `http://localhost:8000`
- websites: `/api/users/websites`
- Detail: `/api/users/detail`
- Search user:`/api/users?name=something`
- All Users:`/api/users/all`

## Authentication
- Deverá ser passado no headers como Bearer Token para validação:
- Valor: `hash_value_token_fake`
```shell
  $ Headers ->
  {
     "Authorization": "Bearer hash_value_token_fake"
  }
```

## Pytest
- `$ docker exec -it challenge-fcamara /bin/sh`
- `$ pytest -v`
- `$ exit`

## Rodar localmente
Para rodar localmente está sendo utilizado [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/basics.html) para criação do ambiente virtual e instalação das libs python. Para instalar o pipenv faça:
- Rode o comando como root ou administrador: `$ pip install pipenv`

Seguir os seguintes passos para rodar localmente:
- Clonar o projeto.
- Vá até a pasta root.
- Criar o ambiente virtual de desenvolvimento para o projeto: `$ pipenv shell`
- Instalar as libs a partir do arquivo "Pipfile": `$ pipenv install`
- Para ativar a biblioteca do pre-commit: `$ pre-commit install`
- Rodar o servidor: `$ uvicorn main:app --reload`