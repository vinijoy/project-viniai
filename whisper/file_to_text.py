import menu as m
from dotenv import load_dotenv
import os
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)
import datetime as dt
from openai import OpenAI

def speach_to_text():
 client = OpenAI(
  api_key = os.getenv('API_KEY')
 )
 while 1:
  today_default = dt.datetime.today()            # 현재 날짜 가져오기
  today = today_default.strftime("%Y%m%d%H%M%S")  # YYYY/mm/dd HH:MM 형태의 시간 출력
  path = 'whisper/results/speach to text result_'+today+'.txt'
  audio_file_name = input('\n오디오 파일명: ')
  if audio_file_name == 'p':
   m.run_menu3()
  elif audio_file_name == 'x':
   print('프로그램을 종료합니다.')
   exit()
  elif audio_file_name == '':
   continue
  else:
   try:
    audio_file= open('sources/audio/'+audio_file_name, "rb")
    print('\n오디오를 분석 중입니다.\n')
    transcript = client.audio.transcriptions.create(
     model="whisper-1", 
     file=audio_file
    )
   except FileNotFoundError:
    print("\n파일을 찾을 수 없습니다.\n")
    speach_to_text()
   f = open(path, 'a')
   f.write(transcript.text+'\n')
   f.close()
   print(path+'에 저장했습니다.\n')
