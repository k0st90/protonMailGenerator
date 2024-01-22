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


#receiving 6 digit passowrd from the clipboard
def getClip6digit(user32:ctypes.WinDLL, kernel32:ctypes.WinDLL, CF_TEXT:int=1) -> str:
    try:
        user32.OpenClipboard(0)
        try:
            if user32.IsClipboardFormatAvailable(CF_TEXT):
                data = user32.GetClipboardData(CF_TEXT)
                data_locked = kernel32.GlobalLock(data)
                text = ctypes.c_char_p(data_locked)
                value = text.value
                kernel32.GlobalUnlock(data_locked)
                digits = re.findall(r'(\d{6})', (str(value)))
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
                match = re.search(r'[\w\.-]+(?:\+[\w\.-]*)?@[\w\.-]+\.\w+', str(value))
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
        print(username+"@proton.me:" + password)
        return username, password
    except:
        return
    
#create account 
def create_acc(username:str, password:str) -> None:
    try:
        webbrowser.open('https://account.proton.me/signup?plan=free')
        time.sleep(5)
        pyautogui.typewrite(username + '\t\t\t')
        print("Username:" + username)
        pyautogui.typewrite(password + '\t' + password + '\t')
        print("Password:" + password)
        pyautogui.typewrite('\n')
        time.sleep(5)
    except:
        return

#get temporary email address email
def get_email(user32:ctypes.WinDLL, kernel32:ctypes.WinDLL, CF_TEXT:int=1) -> None:
    pyautogui.typewrite('\t\t\t\n\t\t')
    time.sleep(5)
    pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('t'); pyautogui.keyUp('ctrlleft')
    time.sleep(10)
    # pyautogui.typewrite('https://dropmail.me/\n') Email address verification temporarily disabled for this email domain. Please try another verification method. I've chosen another site
    pyautogui.typewrite('https://www.emailnator.com/\n')
    time.sleep(10)
    while True:
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        mail = getMail(user32, kernel32, CF_TEXT)
        if mail and "@gmail" in mail:
            print("10 min mail: " + mail[1:])
            pyautogui.click(x=950, y=798)
            time.sleep(3)
            pyautogui.click(x=950, y=798)
            time.sleep(5)
            break
        else:
            pyautogui.keyDown('ctrlleft'); pyautogui.typewrite('r'); pyautogui.keyUp('ctrlleft')
            time.sleep(5)
    pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('\t'); pyautogui.keyUp('ctrlleft')
    time.sleep(5)
    pyautogui.typewrite(mail[1:])
    pyautogui.typewrite('\t\n')
    time.sleep(5)
    pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('\t'); pyautogui.keyUp('ctrlleft')
    time.sleep(60)
    pyautogui.keyDown('ctrlleft'); pyautogui.typewrite('r'); pyautogui.keyUp('ctrlleft')
    time.sleep(10)
    pyautogui.click(x=761, y=736)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    code = getClip6digit(user32, kernel32, CF_TEXT)
    pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('\t'); pyautogui.keyUp('ctrlleft')
    pyautogui.typewrite(code)
    pyautogui.typewrite('\t\n')
    
if __name__ == '__main__':
    user32, kernel32 = clibboard_setup()
    username, password = create_username_password('-p')
    create_acc(username, password)
    get_email(user32, kernel32)