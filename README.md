<h1 align ='center'>BOOK WISE</h1>

Essa é uma aplicação BOOK WISE com objetivo de facilitar a gestão de uma biblioteca. 

## Endpoints
A API possue endpoints para cadastrar seu usuario (colaboradores da bibliote e estudantes), realizar login, cadastrar livros e suas copias e  realizar empréstimo dos livros disponíveis.

<a href="https://insomnia.rest/run/?label=BookWise%20API&uri=https%3A%2F%2Fgithub.com%2FBookWise-API%2Fbookwise-api%2Fblob%2Fmain%2FBookWise_InsomniaProject" target="_blank"><img src="https://insomnia.rest/images/run.svg" alt="Run in Insomnia"></a>

<blockquote> Para importar o JSON no Insomnia é só clicar no botão "Run in Insomnia". Depois é só seguir os passos que ele irá importar todos os endpoints em seu insomnia.
</blockquote>
<br>

A url base da API é https://api-bookwise.onrender.com/api

# Criação de usuário Estudante:

POST /users/ - FORMATO DA REQUISIÇÃO
<br>
USER - ESTUDANTE

```json
{
	"name": "Kenzinho",
	"username": "kenzinho",
	"email": "kenzinho@kenzie.com.br",
	"password": "1243"
}
```
Caso dê tudo certo, a resposta será assim:
POST /users/  - FORMATO DA RESPOSTA - STATUS 201
```json
{
	"id": 1,
	"username": "kenzinho",
	"email": "kenzinho@kenzie.com.br",
	"name": "Kenzinho",
	"blocked_until": null,
	"is_admin": false
}
```

# Login:

POST /users/login/ - FORMATO DA REQUISIÇÃO
```json
{
	"username": "anac",
	"password": "1243"
}
```

Caso dê tudo certo, a resposta será assim:

POST /users/login/ - FORMATO DA RESPOSTA - STATUS 200
```json
{
	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5MTY5NjE1MiwiaWF0IjoxNjg5MTA0MTUyLCJqdGkiOiI1MGZhYmVkZjA0NDA0OWJmYTI0MjU0NTllYTQ2MjgyNyIsInVzZXJfaWQiOjF9.oAF7N6Xzm1iVJHiOaFyi1rPksdaKMBO5DqDyEKuekpQ",
	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg5MTkwNTUyLCJpYXQiOjE2ODkxMDQxNTIsImp0aSI6IjhhY2Q5M2YwMTkxMTQ5NTU4M2E5YjA3YzI3YTU2MTM4IiwidXNlcl9pZCI6MX0.9Q0nQt6vQjO7H0JOT8Tio6qRvp0dfmH8uCoKkvkk5eI"
}
```

Com essa resposta, vemos que temos o token, dessa forma você pode guardar o token no localStorage para fazer a gestão do usuário no seu frontend.

# Rotas que não necessitam de autorização:

GET /books/ - FORMATO DA REQUISIÇÃO (Rota do tipo GET para listar todos os livros cadastrados)

Não tem corpo da requisição

Caso dê tudo certo, a resposta será assim:

GET  /books/ - FORMATO DA RESPOSTA - STATUS 200
```json
{
	"count": 2,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": 1,
			"title": "Teste",
			"author": "Teste",
			"description": "Teste",
			"number_of_copies": 5,
			"copies": [
				{
					"id": 1,
					"book_id": 1,
					"is_borrowed": false
				},
				{
					"id": 2,
					"book_id": 1,
					"is_borrowed": false
				},
				{
					"id": 3,
					"book_id": 1,
					"is_borrowed": false
				},
				{
					"id": 4,
					"book_id": 1,
					"is_borrowed": false
				},
				{
					"id": 5,
					"book_id": 1,
					"is_borrowed": false
				}
			]
		},
		{
			"id": 2,
			"title": "Teste1",
			"author": "Teste1",
			"description": "Teste1",
			"number_of_copies": 5,
			"copies": [
				{
					"id": 6,
					"book_id": 2,
					"is_borrowed": false
				},
				{
					"id": 7,
					"book_id": 2,
					"is_borrowed": false
				},
				{
					"id": 8,
					"book_id": 2,
					"is_borrowed": false
				},
				{
					"id": 9,
					"book_id": 2,
					"is_borrowed": false
				},
				{
					"id": 10,
					"book_id": 2,
					"is_borrowed": false
				}
			]
		}
	]
}
```
<h2>Rotas que necessitam de autorização</h2>

<h3 align ='center'>COLABORADOR DA BIBLIOTECA</h3>
<h4>CADASTRO DOS COLABORADORES DA BIBLIOTECA</h4>
<h5>Informação Importante</h5>
<blockquote> Para utilização da API deve ser solicitado a criação de usuário admin que iria realizar o cadastro dos usuários que são colaboradores da biblioteca.
</blockquote>
POST /users/employee/ - FORMATO DA REQUISIÇÃO (Cadastro de usuário colaborador da biblioteca)

```json
{
  	"name": "Ana",
  	"username": "anac",
  	"email": "anac@kenzie.com.br",
  	"password": "1243",	
  	"is_admin": true
}
```

Caso dê tudo certo, a resposta será assim:
POST /users/employee/ - FORMATO DA RESPOSTA - STATUS 201
```json
{
	"id": 1,
	"username": "anac",
	"email": "anac@kenzie.com.br",
	"name": "Ana",
	"blocked_until": null,
	"is_admin": true
}

```

<h4>USUÁRIOS</h4>

<h5 align ='center'>PESQUISAR USUÁRIO POR ID</h5>
GET /users/id/ - FORMATO DA REQUISIÇÃO
<br>
Não tem corpo da requisição
<br>


<h5 align ='center'>EDITAR USUÁRIO</h5>
PATCH /users/id/ - FORMATO DA REQUISIÇÃO

```json
{
	"username": "usuario",
	"email": "usuario@kenzie.com.br",
	"name": "UserComomun"
}
```

<h5 align ='center'>DELETAR USUÁRIO</h5>
DELETE /users/id/ - FORMATO DA REQUISIÇÃO

<br>
Não tem corpo da requisição
<br>

<h4>LIVROS E COPIAS</h4>

<h5 align ='center'>CADASTRAR LIVRO E SUAS COPIAS</h5>
POST /books/register/ - FORMATO DA REQUISIÇÃO

```json
{
	"title": "Teste",
	"author": "Teste",
	"description": "Teste",
	"number_of_copies": 5
}
```

<h5 align ='center'>DELETAR LIVRO E SUAS COPIAS</h5>
DELETE /books/id/ - FORMATO DA REQUISIÇÃO
<br>
Não tem corpo da requisição
<br>

<h5 align ='center'>EDITAR LIVRO</h5>
PATCH /books/id/ - FORMATO DA REQUISIÇÃO

```json
{
	"title": "A volta dos que não foram 2",
	"author": "Um que foi e voltou",
	"description": "O enigma de voltar sem ter ido"
}
```
<h5 align ='center'>PESQUISAR LIVRO POR ID</h5>
GET /books/id/ - FORMATO DA REQUISIÇÃO
<br>
Não tem corpo da requisição
<br>


<h3 align ='center'>ESTUDANTE</h3>

<h4>EMPRESTIMO E DEVOLUÇÃO DOS LIVROS</h4>

<h5 align ='center'>EMPRESTIMO</h5>
PUT /copies/id/ - FORMATO DA REQUISIÇÃO

<br>
Não tem corpo da requisição
<br>

<h5 align ='center'>DEVOLUÇÃO</h5>
PUT /copies/id/ - FORMATO DA REQUISIÇÃO

<br>
Não tem corpo da requisição
<br>

<h4>SEGUIR LIVRO</h4>
Seguir um livro a fim de receber notificações no email conforme a disponibilidade/status do livro.

<h5 align ='center'>SEGUIR LIVRO</h5>
PUT /books/id/follow/ - FORMATO DA REQUISIÇÃO

<br>
Não tem corpo da requisição
<br>


