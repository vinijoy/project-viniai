import chat_gpt.chatbot as cb
import chat_gpt.recommendation as rd
import chat_gpt.text_translation as tt
import chat_gpt.file_translation as ftt
import whisper.file_to_text as fst
import speach_translation.file_translation as fstt
import tts.text_to_speach as ts
import tts.file_to_speach as fts
import image_creation.image_creation as ic

# 초기 메뉴 실행 함수
def run_menu():
 while 1:
  # 메뉴 리스트 출력
  print('\nvini AI에 오신 것을 환영합니다.\n\n원하시는 메뉴를 선택해주세요.\n1. Chat Gpt 챗봇\n2. 번역\n3. 음성 텍스트 변환\n4. 자막 생성\n5. 텍스트 음성 변환\n6. 통역\n7. 이미지 생성')
  # 메뉴를 선택할 수 있는 입력란 출력
  menu_number = input('')
  # 1을 입력하면 Chat Gpt 챗봇 메뉴 실행
  if menu_number == '1':
   run_menu1()
  # 2를 입력하면 번역 메뉴 실행
  elif menu_number == '2':
   run_menu2()
  # 3을 입력하면 음성 텍스트 변환 메뉴 실행
  elif menu_number == '3':
   run_menu3()
  # 4를 입력하면 자막 생성 메뉴 실행
  elif menu_number == '4':
   run_menu4()
  # 5를 입력하면 텍스트 음성 변환 메뉴 실행
  elif menu_number == '5':
   run_menu5()
  # 6을 입력하면 통역 메뉴 실행
  elif menu_number == '6':
   run_menu6()
  # 7을 입력하면 이미지 생성 메뉴 실행
  elif menu_number == '7':
   run_menu7()
  # x를 입력하면 프로그램 종료
  elif menu_number == 'x':
   print('프로그램을 종료합니다.')
   exit() 
  # 이 외의 모든 입력값에 대해서는 현재 메뉴 재실행
  else:
   print('잘못 입력하셨습니다.')

# 번역 메뉴 실행 함수
def run_menu1():
 while 1:
  # 메뉴 리스트 출력
  print('\n1. Chat Gpt 챗봇\n2. 주제 추천')
  # 메뉴를 선택할 수 있는 입력란 출력
  menu_number = input('')
  # 1을 입력하면 Chat Gpt 챗봇 실행
  if menu_number == '1':
   cb.chatbot()
  # 2를 입력하면 주제 추천 실행
  elif menu_number == '2':
   rd.recommendation()
  # p를 입력하면 초기 메뉴 실행
  elif menu_number == 'p':
   run_menu()
  # x를 입력하면 프로그램 종료
  elif menu_number == 'x':
   print('프로그램을 종료합니다.')
   exit() 
  # 이 외의 모든 입력값에 대해서는 현재 메뉴 재실행
  else:
   print('잘못 입력하셨습니다.')

# 번역 메뉴 실행 함수
def run_menu2():
 while 1:
  # 메뉴 리스트 출력
  print('\n1. 텍스트 번역\n2. 파일 번역')
  # 메뉴를 선택할 수 있는 입력란 출력
  menu_number = input('')
  # 1을 입력하면 텍스트 번역 실행
  if menu_number == '1':
   tt.text_translation()
  # 2를 입력하면 파일 번역 실행
  if menu_number == '2':
   ftt.file_translation()
  # p를 입력하면 초기 메뉴 실행
  elif menu_number == 'p':
   run_menu()
  # x를 입력하면 프로그램 종료
  elif menu_number == 'x':
   print('프로그램을 종료합니다.')
   exit() 
  # 이 외의 모든 입력값에 대해서는 현재 메뉴 재실행
  else:
   print('잘못 입력하셨습니다.')

# 음성 텍스트 변환 메뉴 실행 함수
def run_menu3():
 while 1:
  # 메뉴 리스트 출력
  print('\n1. 파일 텍스트 변환')
  # 메뉴를 선택할 수 있는 입력란 출력
  menu_number = input('')
  # 1을 입력하면 파일 텍스트 변환 실행
  if menu_number == '1':
   fst.speach_to_text()
  # p를 입력하면 초기메뉴 실행
  elif menu_number == 'p':
   run_menu()
  # x를 입력하면 프로그램 종료
  elif menu_number == 'x':
   print('프로그램을 종료합니다.')
   exit() 
  # 이 외의 모든 입력값에 대해서는 현재 메뉴 재실행
  else:
   print('잘못 입력하셨습니다.')

# 자막 생성 메뉴 실행 함수
def run_menu4():
 while 1:
  # 메뉴 리스트 출력
  print('\n1. 파일 자막 생성')
  # 메뉴를 선택할 수 있는 입력란 출력
  menu_number = input('')
  # 1을 입력하면 파일 자막 생성 실행
  if menu_number == '1':
   fstt.file_translation()
  # p를 입력하면 초기메뉴 실행
  elif menu_number == 'p':
   run_menu()
  # x를 입력하면 프로그램 종료
  elif menu_number == 'x':
   print('프로그램을 종료합니다.')
   exit() 
  # 이 외의 모든 입력값에 대해서는 현재 메뉴 재실행
  else:
   print('잘못 입력하셨습니다.')

# 텍스트 음성 변환 메뉴 실행 함수
def run_menu5():
 while 1:
  # 메뉴 리스트 출력
  print('\n1. 텍스트 음성 변환\n2. 파일 음성 변환')
  # 메뉴를 선택할 수 있는 입력란 출력
  menu_number = input('')
  # 1을 입력하면 텍스트 음성 변환 실행
  if menu_number == '1':
   ts.text_to_speach()
  # 2를 입력하면 파일 음성 변환 실행
  if menu_number == '2':
   fts.file_to_speach()
  # p를 입력하면 초기메뉴 실행
  elif menu_number == 'p':
   run_menu()
  # x를 입력하면 프로그램 종료
  elif menu_number == 'x':
   print('프로그램을 종료합니다.')
   exit() 
  # 이 외의 모든 입력값에 대해서는 현재 메뉴 재실행
  else:
   print('잘못 입력하셨습니다.')

# 통역 메뉴 실행 함수
def run_menu6():
 while 1:
  # 메뉴 리스트 출력
  print('\n1. 파일 통역')
  # 메뉴를 선택할 수 있는 입력란 출력
  menu_number = input('')
  # 1을 입력하면 파일 통역 실행
  if menu_number == '1':
   print('\n준비 중입니다.')
  # p를 입력하면 초기메뉴 실행
  elif menu_number == 'p':
   run_menu()
  # x를 입력하면 프로그램 종료
  elif menu_number == 'x':
   print('프로그램을 종료합니다.')
   exit() 
  # 이 외의 모든 입력값에 대해서는 현재 메뉴 재실행
  else:
   print('잘못 입력하셨습니다.')

# 이미지 생성 메뉴 실행 함수
def run_menu7():
 while 1:
  # 메뉴 리스트 출력
  print('\n1. 이미지 생성')
  # 메뉴를 선택할 수 있는 입력란 출력
  menu_number = input('')
  # 1을 입력하면 이미지 생성 실행
  if menu_number == '1':
   ic.image_creation()
  # p를 입력하면 초기메뉴 실행
  elif menu_number == 'p':
   run_menu()
  # x를 입력하면 프로그램 종료
  elif menu_number == 'x':
   print('프로그램을 종료합니다.')
   exit() 
  # 이 외의 모든 입력값에 대해서는 현재 메뉴 재실행
  else:
   print('잘못 입력하셨습니다.')
