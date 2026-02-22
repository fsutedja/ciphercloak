from fastapi import FastAPI #lets Python run a website and respond to browser requests
from fastapi import Form #reads what the user typed into the website form
from fastapi import Request

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates #so python can insert values to HTMl templates
from fastapi.staticfiles import StaticFiles  #css

#import cipher functions
from app.ciphers import (
    caesar_encrypt,
    caesar_decrypt,
    affine_encrypt,
    affine_decrypt
)

#create web server
app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

#when user visits homepage
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse( #render index.html in user's browser
        "index.html",
        {
        "request": request,
        "result": "",
        "error": "",
        "cipher": "caesar",
        "mode": "encrypt",
        "text": "",
        "shift": 0,
        "a": 1,
        "b": 0,
        "preserve_case": True,
        }
    )

@app.post("/", response_class=HTMLResponse)
async def process(
    request: Request,
    cipher: str = Form(...),
    mode: str = Form(...),
    text: str = Form(...),
    shift: int = Form(0),
    a: int = Form(1),
    b: int = Form(0),
    preserve_case: str = Form(None),
):
    keep_case = (preserve_case == "on")

    result = ""
    error = ""

    try:
        if cipher == "caesar":
            if mode == "encrypt":
                result = caesar_encrypt(text, shift, keep_case)
            else:
                result = caesar_decrypt(text, shift, keep_case)

        elif cipher == "affine":
            if mode == "encrypt":
                result = affine_encrypt(text, a, b, keep_case)
            else:
                result = affine_decrypt(text, a, b, keep_case)

    except Exception as e:
        error = str(e)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": result,
            "error": error,
            
            "cipher": cipher,
            "mode": mode,
            "text": text,
            "shift": shift,
            "a": a,
            "b": b,
            "preserve_case": keep_case,
        }
    )