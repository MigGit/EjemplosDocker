Ejemplo de servidor SFTP

Desplegar imagen atmoz/sftp

```sh
docker run -p 22:22 -d atmoz/sftp foo:pass:::upload
```

```sh
User "foo" 
Password "pass
```

Prueba de acceso al servidor puerto por defecto 22

```sh
sftp foo@127.0.0.1
```

Documentación

[Docker HUB](https://hub.docker.com/r/atmoz/sftp/)
