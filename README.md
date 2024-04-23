# Backend side

## Requirements

### To generate requirements.txt use pipreq, e.g.
```
pip install pipreq
python -m pipreqs.pipreqs [path/to/source] --force
```


### To run the server use

```
pip install uvicorn
uvicorn main:app --reload
```

OR

```
make uvi-local
```

### Redis
```
docker run --rm --name some-redis -p 6379:6379 redis:latest
```
Use this ^ to run redis locally
For this use case the redis url will be - redis://localhost:6379



## Things to implement later in development

- [x] Testing w/ Postman or Starlette
- [ ] Migrating to Django (?)
- [ ] Migrating to Golang instead of Python
- [ ] ???


## For logging add /logs directory in /server


## Python version - 3.12