import pyautogui
import time
import random
import string
import webbrowser
import ctypes
import re

from generator import randomize

#setting up clipboard
def clibboard_setup() -> (ctypes.WinDLL, ctypes.WinDLL):
    kernel32 = ctypes.windll.kernel32
    kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
    kernel32.GlobalLock.restype = ctypes.c_void_p
    kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]
    user32 = ctypes.windll.user32
    user32.GetClipboardData.restype = ctypes.c_void_p

    return user32, kernel32


#receiving _ digit passowrd from the clipboard
def getClip_digit(user32:ctypes.WinDLL, kernel32:ctypes.WinDLL, digit_lenght:int, CF_TEXT:int=1) -> str:
    try:
        user32.OpenClipboard(0)
        try:
            if user32.IsClipboardFormatAvailable(CF_TEXT):
                data = user32.GetClipboardData(CF_TEXT)
                data_locked = kernel32.GlobalLock(data)
                text = ctypes.c_char_p(data_locked)
                value = text.value
                kernel32.GlobalUnlock(data_locked)
                digits = re.findall(rf'\b\d{{{digit_lenght}}}\b', (str(value)))
                if digits:
                    return str(digits[0])
                else:
                    return None
        finally:
            user32.CloseClipboard()
    except:
        return


#receiving _ email address from the clipboard 
def getMail(user32:ctypes.WinDLL, kernel32:ctypes.WinDLL, CF_TEXT:int=1) -> str:
    try:
        user32.OpenClipboard(0)
        try:
            if user32.IsClipboardFormatAvailable(CF_TEXT):
                data = user32.GetClipboardData(CF_TEXT)
                data_locked = kernel32.GlobalLock(data)
                text = ctypes.c_char_p(data_locked)
                value = text.value
                kernel32.GlobalUnlock(data_locked)
                match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', str(value))
                if match:
                    return match.group(0)
                else:
                    return None           
        finally:
            user32.CloseClipboard()
    except:
        return
    
#create usermane and password and write them into file
def create_username_password(option:str, length:int=8) -> (str, str):
    try:
        username = randomize(option, length) + randomize(option, length) + randomize(option, length)
        password = randomize(option, length)
        with open("accLog.txt", "a") as logfile:
            logfile.write(f"{username}@proton.me:{password}\n")
        return username, password
    except:
        return
    
# #create account 
# def create_acc(username, password):
#     webbrowser.open('https://account.proton.me/signup?plan=free')
# # time.sleep(5)







# pyautogui.typewrite(_username_ + '\t\t')
# print("Username:" + _username_)

# # Password
# _password_=randomize('-p',16)
# pyautogui.typewrite(_password_+'\t'+_password_+'\t')
# print("Password:" + _password_)

# pyautogui.typewrite('\n')
# time.sleep(5)
# pyautogui.typewrite('\t\t\t\n')

# pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('t'); pyautogui.keyUp('ctrlleft')

# time.sleep(10)
# pyautogui.typewrite('https://dropmail.me/\n')


# pyautogui.keyDown('shift');pyautogui.keyDown('down'); pyautogui.keyUp('down'); pyautogui.keyUp('shift')
# time.sleep(10)

# newMail = True
# while True:
#     if not newMail:
#         pyautogui.keyDown('ctrlleft'); pyautogui.typewrite('r'); pyautogui.keyUp('ctrlleft')
#         time.sleep(5)
#     pyautogui.typewrite('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t')
#     pyautogui.keyDown('ctrlleft')
#     pyautogui.keyDown('shiftleft')
#     pyautogui.keyDown('shiftright')
#     pyautogui.press('down')
#     pyautogui.keyUp('shiftleft')
#     pyautogui.keyUp('shiftright')
#     pyautogui.keyUp('ctrlleft')
#     pyautogui.keyDown('ctrlleft'); pyautogui.typewrite('c'); pyautogui.keyUp('ctrlleft')
#     newMail = getMail()
#     if newMail:
#         print("10 min mail: " + newMail)
#         break

# pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('\t'); pyautogui.keyUp('ctrlleft')
# time.sleep(1)
# #äpyautogui.typewrite(newMail)
# pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('v'); pyautogui.keyUp('ctrlleft')
# pyautogui.press('backspace')
# pyautogui.typewrite('\n')

# time.sleep(10)

# pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('\t'); pyautogui.keyUp('ctrlleft')
# time.sleep(1)

# #pyautogui.typewrite('\t\t\t\t\t\t\t\t\t\t\t\t\t\n')

# #time.sleep(5)


# pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('a'); pyautogui.keyUp('ctrlleft')
# pyautogui.keyDown('ctrlleft'); pyautogui.typewrite('c'); pyautogui.keyUp('ctrlleft')


# pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('\t'); pyautogui.keyUp('ctrlleft')
# time.sleep(5)
# pyautogui.typewrite(str(getClip6digit()) + '\n')


# time.sleep(5)
# pyautogui.typewrite('\n')
# time.sleep(5)
# pyautogui.typewrite('\t\t\t\t\n')
# time.sleep(1)
# pyautogui.typewrite('\t\n')

# print(_username_+"@proton.me:" + _password_)

# logfile = open("accLog.txt", "a")
# logfile.write(_username_ + "@proton.me:" + _password_ + "\n")
# logfile.close()



# CHAPTCHA
#pyautogui.typewrite('\t')
#pyautogui.typewrite('\t')
#pyautogui.typewrite('\t')
#pyautogui.typewrite('\t')
#pyautogui.typewrite('\t')
#pyautogui.typewrite('\t')
#pyautogui.typewrite('\t')

#pyautogui.typewrite('\n')