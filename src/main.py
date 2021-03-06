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
		blank = requests.get("https://firebasestorage.googleapis.com/v0/b/predit-f5df7.appspot.com/o/20210902_135555.png?alt=media&token=b568ecb6-00e0-4402-9762-f70be784335a")
		with open("blank.png","wb") as f:
			f.write(blank.content)
			f.close()
	img = Image.open("./blank.png")
	draw = ImageDraw.Draw(img)
	try:
		with open("font.ttf","rb") as font:
			font.close()
	except Exception:
		font = requests.get("https://firebasestorage.googleapis.com/v0/b/predit-f5df7.appspot.com/o/api%2Ffont.ttf?alt=media&token=b60345c8-17d9-4f82-ab8c-a12b59cb4b98")
		with open('font.ttf', 'wb') as f:
			f.write(font.content)
			f.close()

	font = ImageFont.truetype("font.ttf", 200)
	lines = textwrap.wrap(text, width=7)
	if len(lines) > 1:
		draw.text((300, 850),"Only 7 character Allow.",fill="#604af0",font=font)
	else:
		draw.text((303, 853), text, font =font, fill = (33,36,28)) 
		draw.text((275, 850),text,fill="#49dbdd",font=font, stroke_width=5, stroke_fill="#030401")
		
		
		
		
	img.save("hi.png")
	file_like = open("./hi.png", mode="rb")
	return StreamingResponse(file_like, media_type="image/png")


@app.get("/mia",response_class=FileResponse,tags=["Fake trump Tweet"])
async def mia(text: Optional[str]=None):

	try:
		img = Image.open("./mis.png")
	except Exception:
		miss = requests.get("https://firebasestorage.googleapis.com/v0/b/predit-f5df7.appspot.com/o/miss.jpg?alt=media&token=0445bac4-4587-4fe4-814f-3e72e81ac661")
		with open("miss.jpg","wb") as f:
			f.write(miss.content)
			f.close()
	img = Image.open("./miss.jpg")
	draw = ImageDraw.Draw(img)
	try:
		with open("fonts.ttf","rb") as font:
			font.close()
	except Exception:
		font = requests.get("https://firebasestorage.googleapis.com/v0/b/predit-f5df7.appspot.com/o/font.ttf?alt=media&token=cf309e4a-b273-4598-9dba-c24ab9a0a889")
		with open('fonts.ttf', 'wb') as f:
			f.write(font.content)
			f.close()

	font = ImageFont.truetype("fonts.ttf", 20)
	lines = textwrap.wrap(text, width=1000)
	if len(lines) > 1:
		draw.text((15, 62),"Only 60 character Allow.",fill="#604af0",font=font)
	else:
		draw.text((140, 140),text,fill="#000066",font=font)
	img.save("hi.png")
	file_like = open("./hi.png", mode="rb")
	return StreamingResponse(file_like, media_type="image/png")

