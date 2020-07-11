from random import sample 
from time import sleep

islogin = False

def code():#驗證碼
    str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    code1 = ''.join(sample(str1, 4))
    
    return code1

def registered(): #帳號註冊
    register_aacount = input("輸入要註冊的帳號: ")
    sigh_up_password = input("輸入註冊的密碼: ")
    repassword = input("確認密碼: ")
    length = len(register_aacount)
    if sigh_up_password == repassword:
        with open('users.txt', 'a+') as asteram:
            asteram.seek(0,0)
            answer = asteram.read().split('\n')
            print(answer)
            for i in answer:
                if register_aacount not in i[:length]:
                    continue
                else:
                    print("此帳號已被使用")
                    break
            else:
                input_user = '{} {}\n'.format(register_aacount, sigh_up_password)
                asteram.write(input_user)
                print("註冊成功")
    else:
        print("密碼錯誤")

def login(): #帳號登入
    global islogin
    username = input("輸入帳號: ")
    password = input("輸入密碼: ")
    code1 = code()
    print("驗證碼", code1)
    if input("輸入驗證碼: ") == code1:
        rinput_user = '{} {}'.format(username, password)
        with open('users.txt', 'a+') as asteram:
            asteram.seek(0,0)
            while True:
                new_f1 = asteram.readline()
                n = new_f1.replace("\n", "")
                if not n:
                    print("帳號密碼錯誤")
                    print("返回首頁")
                    sleep(3)
                    break
                if n == rinput_user:
                    print("登入成功")
                    print("返回首頁")
                    sleep(3)
                    islogin = True
                    return True
                else:
                    continue
    else:
        print("驗證碼錯誤")

def verification(func):
    def wrapper():
        global islogin
        if islogin:
            func()
        else:
            print("用戶尚未登入")
            print("即將跳轉登入頁面...")
            sleep(3)
            islogin = login()
    return wrapper


@verification
def books():
    print("開始借書")

while True:
    body = '''
---歡迎使用圖書管理系統---
   輸入功能選項:
   1.註冊帳號
   2.登入帳號
   3.借書
   4.登出系統
-------------------------
'''
    print(body)
    n = int(input())
    if n == 1:
        registered()
    if n == 2:
        login()
    if n == 3:
        books()
    if n == 4:
        break