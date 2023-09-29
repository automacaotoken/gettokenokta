# Aplicação de Recuperação de Token a partir de E-mail

![Imagem da Aplicação](https://exemplo.com/imagem.png)

## Funcionamento

Esta é uma aplicação simples que permite recuperar um token de autenticação a partir de um e-mail. A aplicação é construída em Python utilizando o framework Flask e a biblioteca imapclient para se conectar à conta de e-mail Gmail do usuário.

### Como Funciona

1. Conecta-se à conta de e-mail Gmail do usuário utilizando as credenciais fornecidas (endereço de e-mail e senha).

2. Realiza uma busca nos e-mails da caixa de entrada pelo último e-mail que contenha um assunto específico definido pelo usuário (no exemplo, o assunto é "Token: ").

3. Recupera o assunto desse e-mail encontrado.

4. Extrai um token de autenticação de 6 dígitos do assunto do e-mail.

5. Retorna o token recuperado em formato JSON como resposta.

Se ocorrer algum erro durante qualquer um desses passos, a aplicação retornará uma resposta JSON com uma mensagem de erro e um status HTTP 500 (Erro Interno do Servidor).

## Métodos da API

A aplicação possui os seguintes métodos:

### `connect_to_gmail(email_address, password)`

Este método é responsável por conectar-se à conta de e-mail Gmail do usuário utilizando as credenciais fornecidas.

### `search_email_by_subject(client, search_subject)`

Este método realiza uma busca nos e-mails da caixa de entrada pelo último e-mail que contenha o assunto especificado.

### `fetch_email_subject(client, email_id)`

Este método recupera o assunto de um e-mail específico com base no seu ID.

### `extract_token_from_subject(email_subject)`

Este método extrai um token de autenticação de 6 dígitos do assunto do e-mail. Ele utiliza uma expressão regular para encontrar o código numérico no assunto do e-mail.

## Exemplo de Uso

Para obter um token, faça uma requisição GET para o endpoint `/token`. Certifique-se de fornecer o endereço de e-mail e a senha corretos no código da aplicação.

Exemplo de requisição:

### GET /token


Exemplo de resposta de sucesso:

```json
{
    "message": "Token obtido com sucesso",
    "token": "123456"
}
