# Cloud-Projeto-24.2

## Sobre

Repositório para desenvolvimento do projeto de Computação em Nuvem

Feito por Raul Rangel Moraes Bezerra

Minha API faz uso de um endpoint da API da CoinCap, que fornece informações sobre o mercado de criptomoedas em tempo real. Esse serviço é utilizado para consultar dados sobre ativos digitais, como o valor atual de várias moedas. Através dessa integração, os usuários podem obter informações atualizadas sobre as dez criptomoedas com maior Market Cap através da minha aplicação.

## Como Rodar

Para rodar a aplicação localmente, clone esse repositório e rode o compose:

```
docker compose up
```

Após isso, os Endpoints estarão disponíveis em localhost:8000.

## Documentação

A documentação está disponível no GitHub Pages através [desse link](https://raulrangelmb.github.io/Cloud-Projeto-24.2/)

## Docker

A image da API está dispoível no DockerHub através [desse link](https://hub.docker.com/r/raulrangelmb/api-coin)

O arquivo compose.yaml se encontra na raiz do repositório, no mesmo diretório desse README.