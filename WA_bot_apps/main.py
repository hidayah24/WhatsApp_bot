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
    def nav_input_pesan(self):
        try:
            position = pt.locateOnScreen('klip2.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(100, 10, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except TypeError:
            try:
                position = pt.locateOnScreen('klip.png', confidence=.6)
                pt.moveTo(position[0:2], duration=self.speed)
                pt.moveRel(100, 10, duration=self.speed)
                pt.doubleClick(interval=self.click_speed)
            except Exception as e:
                print('Exception (nav_input_pesan)', e)

    #menavigasi chat/pesan
    def nav_pesan(self):
        try:
            position = pt.locateOnScreen('klip2.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(48, -48, duration=self.speed)
        except TypeError:
            try:
                position = pt.locateOnScreen('klip.png', confidence=.6)
                pt.moveTo(position[0:2], duration=self.speed)
                pt.moveRel(10, -50, duration=self.speed)
            except Exception as e:
                print('Exception (nav_input_pesan)', e)

wa_bot = WhatsApp(speed=.5, clik_speed=.2)
sleep(3)
wa_bot.nav_pesan()
