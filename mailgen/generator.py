#! python3
# Michi4
from typing import Union

from PIL import Image
import pyautogui
import sys
import time
import random
import string
import webbrowser
import ctypes
import re

CF_TEXT = 1  # Define constant for text format in clipboard.
kernel32 = ctypes.windll.kernel32  # Load kernel32.dll for system functions.
kernel32.GlobalLock.argtypes = [ctypes.c_void_p]  # Set argument type for GlobalLock to void pointer.
kernel32.GlobalLock.restype = ctypes.c_void_p  # Set return type of GlobalLock to void pointer.
kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]  # Set argument type for GlobalUnlock to void pointer.
user32 = ctypes.windll.user32  # Load user32.dll for user interface functions.
user32.GetClipboardData.restype = ctypes.c_void_p  # Set return type of GetClipboardData to void pointer.

"""---------------------------------------------------------------------------------------------------------------
-----Attention !!! Before runing this script switch your language(keyboard layout to English) to EN---------------
------------------------------------------------------------------------------------------------------------------
"""


def get_clip6digit() -> str:
    user32.OpenClipboard(0)
    try:
        if user32.IsClipboardFormatAvailable(CF_TEXT):
            data = user32.GetClipboardData(CF_TEXT)
            data_locked = kernel32.GlobalLock(data)
            text = ctypes.c_char_p(data_locked)
            value = text.value
            kernel32.GlobalUnlock(data_locked)
            return str(re.findall(r'(\d{6})', (str(value))))
    finally:
        user32.CloseClipboard()


def get_mail() -> Union[str, bool]:
    user32.OpenClipboard(0)
    try:
        if user32.IsClipboardFormatAvailable(CF_TEXT):
            data = user32.GetClipboardData(CF_TEXT)
            data_locked = kernel32.GlobalLock(data)
            text = ctypes.c_char_p(data_locked)
            value = text.value
            kernel32.GlobalUnlock(data_locked)
            match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', str(value))
            if match is not None:
                adress = str(match.group(0))
                if "@yomail.info" in adress or "@10mail.org" in adress:
                    # Only thouse domains was working,
                    # the others like @emlhub.com, @spymail.one, @freeml.net, @10mail.tk, @dropmail.me,
                    # @minimail.gq, @emlpro.com, @zeroe.ml, @emltmp.com etc.
                    # cause an error during registration:
                    # ""Email address verification temporarily disabled for this email domain.
                    #  Please try another verification method.""
                    return adress
            return False
    finally:
        user32.CloseClipboard()


def randomize(_option_, _length_) -> str:
    if _length_ > 0:

        # Options:
        #       -p      for letters, numbers and symbols
        #       -s      for letters and numbers
        #       -l      for letters only
        #       -n      for numbers only
        #       -m      for month selection
        #       -d      for day selection
        #       -y      for year selection

        if _option_ == '-p':
            string._characters_ = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+'
        elif _option_ == '-s':
            string._characters_ = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        elif _option_ == '-l':
            string._characters_ = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        elif _option_ == '-n':
            string._characters_ = '1234567890'
        elif _option_ == '-m':
            string._characters_ = 'JFMASOND'

        if _option_ == '-d':
            _generated_info_ = random.randint(1, 28)
        elif _option_ == '-y':
            _generated_info_ = random.randint(1950, 2000)
        else:
            _generated_info_ = ''
            for _counter_ in range(0, _length_):
                _generated_info_ += random.choice(string._characters_)

        return _generated_info_

    else:
        return 'error'


if __name__ == "__main__":
    webbrowser.open('https://google.com')
    time.sleep(5)
    pyautogui.keyDown('ctrlleft')
    pyautogui.keyDown('shift')
    pyautogui.typewrite('p')
    time.sleep(5)
    pyautogui.keyUp('ctrlleft')
    pyautogui.keyUp('shift')
    pyautogui.typewrite('https://account.proton.me/signup?plan=free\n')
    time.sleep(6)
    # Username
    _username_ = randomize('-s', 3)+randomize('-s', 3)+randomize('-s', 3)
    pyautogui.typewrite(_username_ + '\t\t\t')
    print("Username:" + _username_)

    # Password
    _password_ = randomize('-p', 16)
    pyautogui.typewrite(_password_ + '\t' + _password_ + '\t')
    print("Password:" + _password_)

    pyautogui.typewrite('\n')
    time.sleep(5)
    pyautogui.typewrite('\t\t\t\n')

    pyautogui.keyDown('ctrlleft')
    pyautogui.typewrite('t')
    pyautogui.keyUp('ctrlleft')

    time.sleep(10)
    pyautogui.typewrite('https://dropmail.me/\n')

    pyautogui.keyDown('shift')
    pyautogui.keyDown('down')
    pyautogui.keyUp('down')
    pyautogui.keyUp('shift')
    time.sleep(10)

    newMail = True
    while True:
        if not newMail:
            pyautogui.keyDown('ctrlleft')
            pyautogui.typewrite('r')
            pyautogui.keyUp('ctrlleft')
            time.sleep(5)
        pyautogui.keyDown('ctrlleft')
        pyautogui.press('a')
        pyautogui.keyUp('ctrlleft')
        pyautogui.keyDown('ctrlleft')
        pyautogui.typewrite('c')
        pyautogui.keyUp('ctrlleft')
        newMail = get_mail()
        if newMail:
            print("10 min mail: " + newMail[1:])
            break

    pyautogui.keyDown('ctrlleft')
    pyautogui.keyDown('shiftleft')
    pyautogui.typewrite('\t')
    pyautogui.keyUp('ctrlleft')
    pyautogui.keyUp('shiftleft')
    time.sleep(1)
    pyautogui.typewrite(newMail[1:])
    pyautogui.typewrite('\n')

    time.sleep(10)
    pyautogui.keyDown('ctrlleft')
    pyautogui.typewrite('\t')
    pyautogui.keyUp('ctrlleft')
    time.sleep(15)

    pyautogui.keyDown('ctrlleft')
    pyautogui.typewrite('a')
    pyautogui.keyUp('ctrlleft')
    pyautogui.keyDown('ctrlleft')
    pyautogui.typewrite('c')
    pyautogui.keyUp('ctrlleft')

    pyautogui.keyDown('ctrlleft')
    pyautogui.keyDown('shiftleft')
    pyautogui.typewrite('\t')
    pyautogui.keyUp('ctrlleft')
    pyautogui.keyUp('shiftleft')
    time.sleep(5)
    pyautogui.typewrite(str(get_clip6digit()) + '\n')

    time.sleep(5)
    pyautogui.typewrite('\n')
    time.sleep(5)
    pyautogui.typewrite('\t\t\t\t\n')
    time.sleep(1)
    pyautogui.typewrite('\t\n')

    print(_username_ + "@proton.me:" + _password_)

    logfile = open("accLog.txt", "a")
    logfile.write(_username_ + "@proton.me:" + _password_ + "\n")
    logfile.close()

    # CHAPTCHA
    # pyautogui.typewrite('\t')
    # pyautogui.typewrite('\t')
    # pyautogui.typewrite('\t')
    # pyautogui.typewrite('\t')
    # pyautogui.typewrite('\t')
    # pyautogui.typewrite('\t')
    # pyautogui.typewrite('\t')

    # pyautogui.typewrite('\n')
