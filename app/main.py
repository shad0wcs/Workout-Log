from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def first_endpoint():
    return {'message': 'first endpoint'}