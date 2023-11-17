import menu as m
from dotenv import load_dotenv
import os
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)
import datetime as dt
from openai import OpenAI

def file_translation():
 while 1:
  audio_file_name = input('\n오디오 파일명: ')
  if audio_file_name == 'p':
   m.run_menu4()
  elif audio_file_name == 'x':
   print('프로그램을 종료합니다.')
   exit()
  elif audio_file_name == '':
   continue
  else:
   arrive_language(audio_file_name)

def arrive_language(audio_file_name):
 client = OpenAI(
  api_key = os.getenv('API_KEY')
 )
 model = "gpt-4"
 today_default = dt.datetime.today()            # 현재 날짜 가져오기
 today = today_default.strftime("%Y%m%d%H%M%S")  # YYYY/mm/dd HH:MM 형태의 시간 출력
 path = 'audio_translation/results/audio translation result_'+today+'.txt'
 messages = [
  {"role": "system", "content": "당신은 모든 질문에 답할 수 있습니다. 당신의 이름은 language master입니다. 당신은 세계 최고의 언어학자입니다."}
 ]
 try:
  audio_file= open('sources/audio/'+audio_file_name, "rb")
  print('\n오디오를 분석 중입니다.\n')
  transcript = client.audio.transcriptions.create(
   model="whisper-1", 
   file=audio_file
  )
  script = transcript.text
 except FileNotFoundError:
  print("파일을 찾을 수 없습니다.")
  audio_translation()
 while 1:
  language = input("도착언어를 입력하세요: ")
  if language == 'p':
   m.run_menu()
  elif language == 'x':
   print('프로그램을 종료합니다.')
   exit()
  elif language == '':
   continue
  else:
   messages.append(
    {"role": "user", "content": script+'를 '+language+'로 번역해주세요.'}
   )
   print('\n번역 중입니다.\n')
   chat_completion = client.chat.completions.create(
    model=model,
    messages=messages
   )
   answer = chat_completion.choices[0].message.content
   f = open(path, 'a')
   f.write(answer+'\n')
   f.close()
   print(path+'에 저장했습니다.\n')
  file_translation()
