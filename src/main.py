from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from starlette.responses import FileResponse

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

import textwrap
import requests

import uvicorn

tags_metadata = [
    {
        "name": "Fake Modi Tweet",
        "description": "Send a GET request to ```https://lysea.herokuapp.com/tweet?text=```+your text. Thanks To [TechnoStone.xyz](https://www.technostone.xyz)",
    }]

app = FastAPI(
	title="Fake Modi Tweets API",
    description="I needed an api of fake Modi tweets for a meme but couldn't find it, so i made it. Thanks To [TechnoStone.xyz](https://www.technostone.xyz)",
    version="1.0.5",
    docs_url=None, 
    redoc_url="/",
    openapi_tags=tags_metadata)

origins = [
	"https://harmz.xyz/",
	"https://www.harmz.xyz/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
)


@app.get("/modi",response_class=FileResponse,tags=["Fake Modi Tweet"])
async def modi(text: Optional[str]=None):
	try:
		img = Image.open("./blank.png")
	except Exception:
		blank = requests.get("https://firebasestorage.googleapis.com/v0/b/predit-f5df7.appspot.com/o/tweet.png?alt=media&token=c58ab68f-f758-4403-8cc1-5eadab6f163b")
		with open("blank.png","wb") as f:
			f.write(blank.content)
			f.close()
	img = Image.open("./blank.png")
	draw = ImageDraw.Draw(img)
	try:
		with open("font.ttf","rb") as font:
			font.close()
	except Exception:
		font = requests.get("https://firebasestorage.googleapis.com/v0/b/faketrumptweets-8c438.appspot.com/o/font.ttf?alt=media&token=9b1a1497-4284-4a3d-8212-91179f4720ea")
		with open('font.ttf', 'wb') as f:
			f.write(font.content)
			f.close()

	font = ImageFont.truetype("font.ttf", 18)
	lines = textwrap.wrap(text, width=60)
	if len(lines) > 1:
		draw.text((15, 62),"Only 60 character Allow.",fill="#604af0",font=font)
	else:
		draw.text((15, 57),text,fill="#14171a",font=font)
	img.save("hi.png")
	file_like = open("./hi.png", mode="rb")
	return StreamingResponse(file_like, media_type="image/png")


@app.get("/mia",response_class=FileResponse,tags=["Fake trump Tweet"])
async def mia(text: Optional[str]=None):
	try:
		img = Image.open("./mis.png")
	except Exception:
		mis = requests.get("https://firebasestorage.googleapis.com/v0/b/predit-f5df7.appspot.com/o/mis.png?alt=media&token=d451e77b-6fd3-4eb3-9a45-059ff6929c39")
		with open("mis.png","wb") as f:
			f.write(mis.content)
			f.close()
	img = Image.open("./mis.png")
	draw = ImageDraw.Draw(img)
	try:
		with open("font.ttf","rb") as font:
			font.close()
	except Exception:
		font = requests.get("https://firebasestorage.googleapis.com/v0/b/faketrumptweets-8c438.appspot.com/o/font.ttf?alt=media&token=9b1a1497-4284-4a3d-8212-91179f4720ea")
		with open('font.ttf', 'wb') as f:
			f.write(font.content)
			f.close()

	font = ImageFont.truetype("font.ttf", 18)
	lines = textwrap.wrap(text, width=150)
	if len(lines) > 1:
		draw.text((15, 62),"Only 60 character Allow.",fill="#604af0",font=font)
	else:
		draw.text((15, 57),text,fill="#14171a",font=font)
	img.save("hi.png")
	file_like = open("./hi.png", mode="rb")
	return StreamingResponse(file_like, media_type="image/png")

