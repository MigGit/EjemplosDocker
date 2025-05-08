Ejemplo de servidor MySQL

Desplegar imagen MySQL

```sh
docker pull mysql
docker run -p 3306:3306 --name ejemplo-mysql -e MYSQL_ROOT_PASSWORD=pw-secreto -d mysql
```

Prueba de acceso al servidor puerto por defecto 33006

```sh
docker exec -it ejemplo-mysql mysql -uroot -ppw-secreto
```

Documentación

[MySQL](https://hub.docker.com/_/mysql)
