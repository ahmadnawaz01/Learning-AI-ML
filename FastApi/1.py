from fastapi import FastAPI


app=FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello, my name is ahmad nawaz"}


@app.get("/about")
def about():
    return {"message":" hey i am learning fastapi and i am currently enjoyed it"}