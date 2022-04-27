import pyautogui as pt
import pyperclip as pc
from time import sleep
from bot_chat import response

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
            pt.moveRel(40, -48, duration=self.speed)
        except TypeError:
            try:
                position = pt.locateOnScreen('klip.png', confidence=.6)
                pt.moveTo(position[0:2], duration=self.speed)
                pt.moveRel(33, -50, duration=self.speed)
            except Exception as e:
                print('Exception (nav_input_pesan)', e)

    # Meng-copy pesan
    def get_pesan(self):
        pt.tripleClick()
        sleep(self.speed)
        with pt.hold('ctrl'):
            pt.press('c')
        sleep(1)

        self.massage = pc.paste()
        pt.click()
        print('Isi pesan: ', self.massage)

    def kirim_pesan(self):
        try:
            if self.massage != self.last_massage:
                bot_response = response(self.massage)
                print('Jawaban: ', bot_response)
                pt.typewrite(bot_response, interval=.1)
                pt.typewrite('\n')

                # mengisi pesan lama
                self.last_massage = self.massage
            else:
                print('Tidak ada pesan baru...')
        except Exception as e:
            print('Exception (kirim_pesan): ',e)

wa_bot = WhatsApp(speed=.5, clik_speed=.2)
sleep(3)

wa_bot.nav_pesan_baru()
wa_bot.nav_pesan()
wa_bot.get_pesan()
wa_bot.nav_input_pesan()
wa_bot.kirim_pesan()
