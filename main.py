from fastapi import FastAPI, Request
import app.routers.initRouter as Router
import app.models.models as models 



app = FastAPI()

app.include_router(Router.Router)



