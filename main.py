from fastapi import FastAPI
import app.routers.initRouter as Router



app = FastAPI()

app.include_router(Router.Router)
