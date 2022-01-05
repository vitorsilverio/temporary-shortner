from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Union


import app.shortner as shortner

app = FastAPI(title="Temporary Shortner")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def shorten(request: Request, url: str = Form(...)):
    url = shortner.shorten(url)
    return templates.TemplateResponse("index.html", {"request": request, "url": url})

@app.get("/{short_url}", response_class=Union[RedirectResponse,HTMLResponse])
async def redirect(request: Request, short_url: str):
    try:
        url = shortner.get_url(short_url)

        return RedirectResponse(url)
    except ValueError:
        return templates.TemplateResponse("index.html", {"request": request, "error": "Invalid short URL"})