import menu as m
from authorization import *

def recommendation():
 client = OpenAI(
  api_key = os.getenv('API_KEY')
 )
 model = "gpt-4"
 messages = [
   {"role": "system", "content": "당신은 모든 질문에 답할 수 있습니다. 당신의 이름은 챗친입니다. 당신은 세계 최고의 작문가입니다."}
 ]
 while 1:
  prompt = input("\n주제 생성을 위한 키워드를 입력하세요: ")
  if prompt == 'p':
   m.run_menu1()
  elif prompt == 't':
   m.run_menu()
  elif prompt == 'x':
   print('프로그램을 종료합니다.')
   exit()
  elif prompt == '':
   continue
  else:
   messages.append(
   {"role": "user", "content": prompt+'에 대한 주제 10 개만 추천해주세요.'}
   )
   print('\n잠시만 기다려주세요.\n')
   chat_completion = client.chat.completions.create(
   model=model,
   messages=messages
   )
   answer = chat_completion.choices[0].message.content
   print(answer+'\n')
