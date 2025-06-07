from fastapi import FastAPI

app = FastAPI()

posts =  []

@app.get("/")
def read_root():
    return {"Hola": "Bienvenido a mi Proyecto"}

@app.get("/posts")
def get_posts():
    return posts