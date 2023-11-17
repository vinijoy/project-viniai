import menu as m
from dotenv import load_dotenv
import os
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)
import pyperclip as pc
from openai import OpenAI

def image_creation():
 client = OpenAI(
  api_key = os.getenv('API_KEY')
 )
 while 1:
  image_explaining = input("\n생성할 이미지를 묘사해 주세요: ")
  if image_explaining == 'p':
   m.run_menu7()
  elif image_explaining == 'x':
   print('프로그램을 종료합니다.')
   exit()
  elif image_explaining == '':
   continue
  else:
   print('\n잠시만 기다려 주세요.\n')
   response = client.images.generate(
    model="dall-e-3",
    prompt=image_explaining,
    size="1024x1024",
    quality="standard",
    n=1,
   )
   image_url = response.data[0].url
   pc.copy(image_url)
   print("생성된 이미지의 URL을 클립보드에 복사했습니다.\n")
