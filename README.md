# Backend do projeto py-classifica-legal

Esse repositório é parte do [post](https://netoferraz.github.io/o-eu-analitico/deep%20learning/nlp/data%20product/fastapi/docker/cloud/azure/2020/08/03/gov-data-product-p5.html) detalhando o deploy da solução.

É recomendável usar a solução *on-promise*, já que não há certeza de quanto tempo a aplicação [online](https://pylegalclassifier.azurewebsites.net/docs) estará disponível.

## 1. Build da imagem docker

`docker build -t pylegalclassifier .`

## 2. Executar o serviço

`docker run -d -p 8081:8081 pylegalclassifier`

## 3. Consultas à API.

Segue abaixo um exemplo de consulta ao serviço.

```bash
curl \
  --header "Content-Type: application/json" \
  --request POST \
  --data '{"ementa":"Institui o Comitê de Governança Digital e Segurança da Informação da Presidência da República."}' \
  http://localhost:8081/predict
```

## 3.1 Exemplo de output
`{"tags":["AMBITO","COMPETENCIA","COMPOSIÇÃO","CRIAÇÃO"]}`
