from fastapi import FastAPI
import os
import socket

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "message": "Привет! Это мой первый DevOps проект!",
        "host": socket.gethostname(),
        "env_var": os.getenv("MY_ENV_VAR", "Переменная не задана"),
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}
