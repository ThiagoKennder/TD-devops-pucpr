from fastapi  import FastAPI
import random
app = FastAPI()

#http://127.0.0.1:8000/
@app.get("/")
async def root():
    return {"teste": True, "num_aleatorio": random.randint(0,20000)}

#http://127.0.0.1:8000/teste
@app.get("/teste")
async def teste():
    return {"teste1": "deu certo"}
