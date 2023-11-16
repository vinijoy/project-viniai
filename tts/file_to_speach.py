import menu as m
from dotenv import load_dotenv
import os
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)
import datetime as dt
import re
from openai import OpenAI

def file_to_speach():
 while 1:
  text_file_name = input("텍스트 파일명: ")
  if text_file_name == 'p':
   m.run_menu()
  elif text_file_name == 'x':
   print('프로그램을 종료합니다.')
   exit()
  elif text_file_name == '':
   continue
  else:
   choose_voice(text_file_name)

def choose_voice(text_file_name):
 client = OpenAI(
  api_key = os.getenv('API_KEY')
 )
 model="tts-1-hd"
 voice=""
 try:
  with open('sources/text/'+text_file_name, 'r') as file:
   print('파일을 일고 있습니다.')
   text = file.read()
 except FileNotFoundError:
  print("파일을 찾을 수 없습니다.")
  file_to_speach()
 while 1:
  prompt2 = input("사용할 음성을 고르세요.\n1. Alloy\n2. Echo\n3. Fable\n4. Onyx\n5. Nova\n6. Shimmer\n")
  if prompt2 == '1':
   voice = "alloy"
  elif prompt2 == '2':
   voice = "echo"
  elif prompt2 == '3':
   voice = "fable"
  elif prompt2 == '4':
   voice = "onyx"
  elif prompt2 == '5':
   voice = "nova"
  elif prompt2 == '6':
   voice = "shimmer"
  elif prompt2 == 'x':
   print('프로그램을 종료합니다.')
   exit() 
  elif prompt2 == '':
   continue
  else:
   print('잘못 입력하셨습니다.')
   continue
  print('\n잠시만 기다려 주세요.\n')
  response = client.audio.speech.create(
   model=model,
   voice=voice,
   input=text,
  )
  new_text_file_name = re.sub(".{4}$", "", text_file_name)
  today_default = dt.datetime.today()            # 현재 날짜 가져오기
  today = today_default.strftime("%Y%m%d%H%M%S")  # YYYY/mm/dd HH:MM 형태의 시간 출력
  path = 'tts/results/file to speach/'+new_text_file_name+'_'+voice+'_'+today+'.mp3'
  response.stream_to_file(path)
  print(path+'에 저장했습니다.\n')
  file_to_speach()
