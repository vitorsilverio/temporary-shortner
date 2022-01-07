from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Union
from dotenv import load_dotenv
from datetime import timedelta
import validators
load_dotenv()
import app.shortner as shortner

expiration_time = timedelta(seconds=shortner.expiration_time)

app = FastAPI(title="Temporary Shortner")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def shorten(request: Request, url: str = Form(...)):
    if not validators.url(url):
        return templates.TemplateResponse("index.html", {"request": request, "error": "Invalid URL"}, status_code=400)
    shortened_url = shortner.shorten(url)
    return templates.TemplateResponse("index.html", {"request": request, "url": shortened_url, "expiration_time": expiration_time})

@app.get("/{short_url}", response_class=Union[RedirectResponse,HTMLResponse])
async def redirect(request: Request, short_url: str):
    try:
        url = shortner.get_url(short_url)
        return RedirectResponse(url)
    except ValueError:
        return templates.TemplateResponse("index.html", {"request": request, "error": "Not found!"}, status_code=404)