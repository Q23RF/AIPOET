from PIL import Image, ImageDraw, ImageFont
import requests
import os
from dotenv import load_dotenv, dotenv_values 
load_dotenv()

def write_on_img(message):
  img = Image.open("static/2.jpg")
  font = ImageFont.truetype('static/莫大毛筆-Regular.ttf', 85)
  imgDraw = ImageDraw.Draw(img)
  width = 1748
  textWidth, textHeight = imgDraw.textsize(message, font=font)
  xText = (width-textWidth)/2
  yText = 435

  imgDraw.multiline_text((xText, yText), message, font=font, fill=(50, 50, 50), spacing=32, align="center")
  return img

def send_line(message):
	token = os.getenv("LINE_TOKEN")
	headers = { "Authorization": "Bearer " + token }
	data = { 'message': '\n'+message }
	requests.post("https://notify-api.line.me/api/notify",
	    headers = headers, data = data)