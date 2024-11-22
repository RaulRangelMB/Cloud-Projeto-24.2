# Endpoints

Abaixo estão os endpoints disponíveis na minha API RESTful.

## 1. Registro de Usuário

### URL

`POST /registrar`

### Descrição

Este endpoint permite que um usuário se registre na aplicação. Ele recebe os seguintes dados:

- `nome`: Nome do usuário (obrigatório)
- `email`: Email do usuário (obrigatório)
- `senha`: Senha do usuário (obrigatório)

Se o email já estiver registrado, a API retornará um erro 409. Se o registro for bem-sucedido, a API retornará um token JWT.

### Exemplo de Requisição

```json
{
  "nome": "Nome Exemplo",
  "email": "email@exemplo.com",
  "senha": "senha123"
}
```

### Exemplo de Resposta

```json
{
  "jwt": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImNsb3VkQGluc3Blci5lZHUuYnIiLCJleHAiOjE3MzIyNzc0Nzh9.DF2dEM5oT87uSGxIm-8GAq4OGiRHj5tz-MALn5nZLuI"
}
```

---

## 2. Login de Usuário

### URL

`POST /login`

### Descrição

Este endpoint permite que um usuário faça login na aplicação. Ele recebe os seguintes dados:

- `email`: Email do usuário (obrigatório)
- `senha`: Senha do usuário (obrigatório)

Se não for possível verificar o login, a API retornará um erro 401. SeSe o registro for bem-sucedido, a API retornará um token JWT.

### Exemplo de Requisição

```json
{
  "email": "email@exemplo.com",
  "senha": "senha123"
}
```

### Exemplo de Resposta

```json
{
  "jwt": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImNsb3VkQGluc3Blci5lZHUuYnIiLCJleHAiOjE3MzIyNzc0Nzh9.DF2dEM5oT87uSGxIm-8GAq4OGiRHj5tz-MALn5nZLuI"
}
```

---

## 3. Consulta

### URL

`GET /consultar`

### Descrição

Este endpoint permite que o usuário consulte dados externos da API CoinCap. Para utilizar este endpoint, o usuário deve fornecer um token JWT no cabeçalho da requisição. Se o token for válido, a API retornará dados filtrados da [CoinCap](https://https://docs.coincap.io).

- `nome`: Nome do usuário (obrigatório)
- `email`: Email do usuário (obrigatório)
- `senha`: Senha do usuário (obrigatório)

Se o email já estiver registrado, a API retornará um erro 409. Se o registro for bem-sucedido, a API retornará um token JWT.

### Exemplo de Requisição

```json
GET /consultar
Authorization: Bearer token_jwt
```

### Exemplo de Resposta

```json
[
  {
    "id": "bitcoin",
    "rank": 1,
    "symbol": "BTC",
    "name": "Bitcoin",
    "priceUsd": "---"
    (...)
  },
  {
    "id": "ethereum",
    "rank": 2,
    "symbol": "ETH",
    "name": "Ethereum",
    "priceUsd": "---"
    (...)
  },
  (...)
]
```

---