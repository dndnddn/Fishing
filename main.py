from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# @app.get("/") # get method로 '/'에 해당하는  생성
# def root():
#     return {'Hello':'World!'} 

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    result = "Type a number"
    return templates.TemplateResponse("index.html", {"request": request, 'result': result})

@app.post ("/")
async def root(request:Request, num:int = Form(...)):
    result = num
    return templates.TemplateResponse("index.html", {"request": request, 'result': result})