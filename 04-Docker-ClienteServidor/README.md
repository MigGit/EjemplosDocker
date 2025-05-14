
Construir las imágenes

```sh
docker build -t mi-api ./app
docker build -t mi-cliente ./client
```

Crear una red Docker personalizada
```sh
docker network create mi-red
```

inicia la API y ponle nombre app
```sh
docker run -d --name app --network mi-red -p 5000:5000 mi-api
docker run -d --name appCliente --network mi-red mi-api
```

Valida servicio 5000
```sh
wget 127.0.0.1:5000
```

corre el cliente
```sh
docker run --rm --network mi-red mi-cliente
```