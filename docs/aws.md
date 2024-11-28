# AWS

[Clique aqui](https://github.com/RaulRangelMB/Cloud-Projeto-24.2) para acessar o repositório do projeto

Vídeo do projeto funcionando pela AWS:

<video controls width="800">
  <source src="img/videodeployaws.mp4" type="video/mp4">
  Seu navegador não suporta vídeos embutidos.
</video>

## Configuração do Cluster EKS

[Clique aqui](http://ad85d9fe678ee45198899e28fd849e1e-1790702094.us-east-2.elb.amazonaws.com/docs) para acessar a documentação da API

### Implantação dos Pods

#### Banco de Dados (PostgreSQL)

Arquivo **`db-deployment.yml`**:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: postgres
  labels:
    app: postgres
spec:
  replicas: 1
  selector:
    matchLabels:
      app: postgres
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
      - name: postgres
        image: postgres:17
        env:
        - name: POSTGRES_USER
          value: "usuario"
        - name: POSTGRES_PASSWORD
          value: "senha"
        - name: POSTGRES_DB
          value: "banco"
        ports:
        - containerPort: 5432
---
apiVersion: v1
kind: Service
metadata:
  name: postgres
spec:
  ports:
    - port: 5432
  selector:
    app: postgres
```

#### Aplicação web

Arquivo **`web-deployment.yml`**:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: apirest
spec:
  replicas: 2
  selector:
    matchLabels:
      app: apirest
  template:
    metadata:
      labels:
        app: apirest
    spec:
      containers:
      - name: apirest
        image: raulrangelmb/api-coin:latest
        imagePullPolicy: Always
        env:
        - name: DATABASE_URL
          value: "postgresql://usuario:senha@postgres:5432/banco"
        - name: SECRET_KEY
          value: "secret_key"
        ports:
        - containerPort: 8000
---
apiVersion: v1
kind: Service
metadata:
  name: apirest-service
spec:
  type: LoadBalancer
  ports:
    - port: 80
      targetPort: 8000
  selector:
    app: apirest
```