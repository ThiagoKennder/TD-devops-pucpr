from fastapi  import FastAPI

app = FastAPI()

#http://127.0.0.1:8000/
@app.get("/helloword")
async def root():
    return {"message": "Hello World"}

#http://127.0.0.1:8000/teste1
@app.get("/teste2")
async def teste2():
    return {"teste1": "testando 2"}