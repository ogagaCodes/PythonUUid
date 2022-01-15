from fastapi import FastAPI

from .routers import routes

app = FastAPI()


app.include_router(routes.router)



@app.get("/")
async def root():
    return {"message": "Hello UUID Generator!"}
