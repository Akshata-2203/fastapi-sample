from fastapi import FastAPI
from router.user_router import router
app=FastAPI()


app.include_router(router)