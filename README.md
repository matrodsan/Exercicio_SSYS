<h1 align="center"><img src="https://www.ssys.com.br/wp-content/uploads/2020/09/ssys-logo-site.png"/><br>Exercicio_SSYS</h1>
<p align="center">API com rotas definidas e funções definidas para cumprimento do desafio.</p>
<div style="display: inline_block" align="center">
  <img src="https://img.shields.io/badge/%20-python-brightgreen?colorA=ffd43b&colorB=306998&style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/%20-FastAPI-brightgreen?colorA=006e63&colorB=009688&style=for-the-badge&logo=FastAPI&logoColor=ffffff"/>
  <img src="https://img.shields.io/badge/%20-SQLite-brightgreen?colorA=003B57&colorB=0087c7&style=for-the-badge&logo=SQLite&logoColor=ffffff"/>
</div>

## Intro
 A princípio, o desafio propôs algumas tarefas que percebi serem mais fáceis de serem resolvidas através do FastAPI, um web framework em Python. Apesar de não estar com a linguagem em dia, lancei mão de um tutorial que me ajudou a resolver as tarefas propostas pelo desafio. Confira:
> :memo: **Tutorial:** https://giovannireisnunes.wordpress.com/2020/07/31/utilizando-o-fastapi-parte-1/.

Outro motivo que me levou a utilizar essa plataforma é meu nível de conhecimento em Django, banco de dados e API, que posso dizer ser relativamente básico. Deste modo, essa framework me permitiu entregar o necessário para a conclusão do desafio.


## Índice
* [O desafio](#o-desafio)
* [Insatalação](#instalação)


## O desafio
Crie o CRUD do gerenciador de empregados SSYS contendo as rotas fornecidas:

* GET /employees/ (lista de funcionários)
* POST /employees/ (criação de funcionário)
* UPDATE /employees/ID/ (atualização do funcionário)
* DELETE /employees/ID/ (exclusão de funcionário)
* GET /employees/ID/ (detalhe do funcionário)

Relatórios:

* GET /reports/employees/salary/ (deve conter os resgistros mais baixo, mais alto e a média dos salário)
* GET /reports/employees/age/ (deve conter os resgistros mais jovem, mais velho e a média das idades)

Antes de prosseguirmos, um mecanismo de autenticação foi solicitado e vale ressaltar que a própria plataforma possui ferramentas que possibilitam a criação deste mecanismo de autenticação.


## Instalação
Para instalar todas as dependências, execute o seguinte comando:
```
$ pip3 install -r requirements.txt
```


## Execução
O seguinte comando executa o servidor:
```
$ uvicorn main:app --reload
```


## Populando o banco
O banco deve ser criado através da execução da API em main.py e populado após sua criação através do SQLite para começarmos o projeto com um banco já populado. Para popular o banco execute:
```
$ sqlite3 db.sqlite3 < database/base.sql
```

## Informações de autenticação (Basic Auth)
```
username: ssys
password: testessys
```


## Utilizando as rotas e o CRUD
Acessando a rota http://127.0.0.1:8000/docs (ou outra rota, caso o administardor assim defina) você verá a documentação interativa automática da API gerada pela framework. Deste modo, será possível realizar todas as requisições a partir de uma interface limpa, intuitiva e moderna.
