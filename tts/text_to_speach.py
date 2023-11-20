import menu as m
import datetime as dt
from authorization import *

def text_to_speach():
 while 1:
  prompt = input("\n음성으로 변환할 텍스트를 입력하세요: ")
  if prompt == 'p':
   m.run_menu5()
  elif prompt == 't':
   m.run_menu()
  elif prompt == 'x':
   print('프로그램을 종료합니다.')
   exit()
  elif prompt == '':
   continue
  else:
   choose_voice(prompt)

def choose_voice(prompt):
 client = OpenAI(
  api_key = os.getenv('API_KEY')
 )
 model="tts-1-hd"
 voice=""
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
   input=prompt,
  )
  today_default = dt.datetime.today()            # 현재 날짜 가져오기
  today = today_default.strftime("%Y%m%d%H%M%S")  # YYYY/mm/dd HH:MM 형태의 시간 출력
  path = 'tts/results/text to speach/text to speach result_'+voice+'_'+today+'.mp3'
  response.stream_to_file(path)
  print(path+'에 저장했습니다.\n')
  text_to_speach()
