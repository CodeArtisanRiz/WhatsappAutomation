from time import time
import pywhatkit as w
import time
import pyautogui
import keyboard as k


number = "+Country code + Number"
message = "Test Message"
time = "22.50"
hr = 23
min = 18
w.sendwhatmsg(number,message,hr, min)
pyautogui.click(1050, 950)
time.sleep(2)
k.press_and_release('enter')
