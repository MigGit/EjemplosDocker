# Ejecutar Docker Compose

```sh
docker compose up -d
```

# Probar la aplicación

http://localhost:8080

# Inspeccionar los contenedores y volúmenes

```sh
docker compose ps
```

```sh
docker volume ls
docker volume inspect ejemplo2-docker-compose_dbdata
```

```sh
docker compose exec db cat ./data/demo.txt
```

# Detener los servicios

```sh
docker compose down
```