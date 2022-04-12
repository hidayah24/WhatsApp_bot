import pyautogui as pt
# import pyperclip as pc
from time import sleep

class WhatsApp:
    #Defines the starting values
    def __init__(self, speed=.5, clik_speed=.4):
        self.speed = speed
        self.click_speed = clik_speed
        self.massage = ''
        self.last_massage = ''

    # Menavigasi pesan baru
    def nav_pesan_baru(self):
        try:
            position = pt.locateOnScreen('pesan_baru.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-100, 0, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_pesan_baru)', e)

wa_bot = WhatsApp(speed=.5, clik_speed=.2)
sleep(3)
wa_bot.nav_pesan_baru()
