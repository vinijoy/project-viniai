import chat_gpt.chatbot as cb
import chat_gpt.recommendation as rd
import chat_gpt.translation as tl
import whisper.speach_to_text as st
import audio_translation.audio_translation as at
import tts.text_to_speach as ts
import tts.file_to_speach as fs
import image_creation.image_creation as ic

# 메뉴 실행 함수
def run_menu():
 while 1:
  print('\nvini AI에 오신 것을 환영합니다.\n\n원하시는 메뉴를 선택해주세요.\n1. Chat Gpt 챗봇\n2. 주제 추천\n3. 번역\n4. 음성 텍스트 변환\n5. 오디오 자막 생성\n6. 텍스트 음성 변환\n7. 파일 음성 변환\n8. 이미지 생성') # 메뉴 리스트 출력
  menu_number = input('') # 메뉴를 선택할 수 있는 입력란 출력
  # 1을 입력하면 Chat Gpt 챗봇 실행
  if menu_number == '1':
   cb.chatbot()
  # 2를 입력하면 주제 추천 실행
  elif menu_number == '2':
   rd.recommendation()
  # 3을 입력하면 번역 실행
  elif menu_number == '3':
   tl.translation()
  # 4를 입력하면 음성 텍스트 변환 실행
  elif menu_number == '4':
   st.speach_to_text()
  # 5를 입력하면 오디오 자막 생성 실행
  elif menu_number == '5':
   at.audio_translation()
  elif menu_number == '6':
   ts.text_to_speach()
  elif menu_number == '7':
   fs.file_to_speach()
  elif menu_number == '8':
   ic.image_creation()

  # x를 입력하면 안내 메시지 출력 후 프로그램 종료
  elif menu_number == 'x':
   print('프로그램을 종료합니다.')
   exit() 
  # 이 외의 모든 입력값에 대해서는 오류 메시지 출력 후 메뉴 실행
  else:
   print('잘못 입력하셨습니다.')
