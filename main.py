from fastapi import FastAPI
import app.routers.initRouter as Router
from fastapi.middleware.cors import CORSMiddleware
from app.middleware.cors import middleware


app = FastAPI()

app.include_router(Router.Router)

# app.add_middleware(
#     CORSMiddleware,
#     *middleware
# )