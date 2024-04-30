# Backend side

## Requirements

### To generate requirements.txt use
```
make req-make
```


### To run the server use


```
make uvi-local
```




## Things to implement later in development

- [x] Testing w/ Postman or Starlette
- [ ] ~~Migrating to Django (?)~~
- [ ] PyNest microservices
- [ ] Migrating to Golang instead of Python
- [ ] ???


## For logging add /logs directory in /server


## To make SSL certificate

```
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
```


## Python version - 3.12
