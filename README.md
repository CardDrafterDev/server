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



## Things to implement later in development

- [x] Testing w/ Postman or Starlette
- [ ] Migrating to Django (?)
- [ ] Migrating to Golang instead of Python
- [ ] ???


## For logging add /logs directory in /server


## Python version - 3.12