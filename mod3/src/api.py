from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
    <head>
        <title>Meu FastAPI</title>
    </head>
    <body style="background: radial-gradient(circle, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 0%, rgba(0,212,255,1) 100%);">
        <h1 style="color: Black; text-align: center;">IGTI DE-CLOUD</h1>
        <h2 style="color: White; text-align: center;">Criando API</h2>
    </body>
    </html>
    """


@app.get("/helthz")
async def helth():
    return {"message": "Hello World!"}
