import menu as m
from dotenv import load_dotenv
import os
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)
import datetime as dt
import re
from openai import OpenAI

def file_translation():
 while 1:
  text_file_name = input("\n텍스트 파일명: ")
  if text_file_name == 'p':
   m.run_menu2()
  elif text_file_name == 'x':
   print('프로그램을 종료합니다.')
   exit()
  elif text_file_name == '':
   continue
  else:
   try:
    with open('sources/text/'+text_file_name, 'r') as file:
     print('\n파일을 일고 있습니다.')
     text = file.read()
     arrive_language(text_file_name, text)
   except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
    continue

def arrive_language(text_file_name, text):
 client = OpenAI(
  api_key = os.getenv('API_KEY')
 )
 model = "gpt-4"
 messages = [
  {"role": "system", "content": "당신은 모든 질문에 답할 수 있습니다. 당신의 이름은 language master입니다. 당신은 세계 최고의 언어학자입니다."}
 ]
 language = input("\n도착언어를 입력하세요: ")
 messages.append(
  {"role": "user", "content": text+'를 '+language+'로 번역해주세요.'}
 )
 print('\n잠시만 기다려주세요.\n')
 chat_completion = client.chat.completions.create(
  model=model,
  messages=messages
 )
 answer = chat_completion.choices[0].message.content
 new_text_file_name = re.sub(".{4}$", "", text_file_name)
 today_default = dt.datetime.today()            # 현재 날짜 가져오기
 today = today_default.strftime("%Y%m%d%H%M%S")  # YYYY/mm/dd HH:MM 형태의 시간 출력
 path = 'chat_gpt/results/file translation/'+new_text_file_name+'_'+today+'.txt'
 f = open(path, 'a')
 f.write(answer+'\n')
 f.close()
 print(path+'에 저장했습니다.')
 file_translation()
