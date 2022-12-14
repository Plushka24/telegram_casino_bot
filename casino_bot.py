from threading import Thread
import telebot
from telebot import types
import time
import os
from keyboa import Keyboa
import random
import sqlite3
import requests
import json
from datetime import datetime
from yoomoney import Client
from yoomoney import Quickpay


class App:
    def __init__(self):
        self.token = ''
        self.ymoney_token = ""
        self.status_true = 'unbanned'
        self.status_false = 'banned'
        self.status_admin = 'admin'
        self.label = ''
        self.pust = ''
        self.bot=telebot.TeleBot(self.token)
        self.thread = Thread(target = self.init_bot)
        self.thread.start()
    def init_db(self):
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Data
                            (ID INTEGER, Balance INTEGER, Status TEXT, Game_history TEXT)""")
        self.conn.commit()
        self.conn.close

    def init_bot(self):
        
        @self.bot.message_handler(commands=['start'])
        def start_message(message):
            self.init_db()
            self.id = message.chat.id
            self.cursor = self.conn.cursor()
            self.check_id = self.cursor.execute('SELECT ID, ID FROM Data WHERE ID = ?', (self.id,))
            self.ch = self.cursor.fetchall()
            self.check_status = self.cursor.execute('SELECT Status, Status FROM Data WHERE ID = ?', (self.id,))
            self.cs = self.cursor.fetchall()
            try:
                self.b = self.cursor.execute('SELECT Balance, Balance FROM Data WHERE ID = ?', (self.id,))
                self.balance = str(self.cursor.fetchall())
                self.f = self.balance.index('(')
                self.c = self.balance.index(',')
                self.balance = int(self.balance[self.f+1:self.c])
                self.conn.commit()
                self.conn.close
            except:
                pass
            if str(self.ch) == '[]':
                if self.id == 881084072:
                    self.status_true = 'admin'
                    self.balance = 100000 #???????????? ????????????
                    self.cursor.execute(f"INSERT or IGNORE INTO Data VALUES(?, ?, ?, ?)", (self.id, self.balance, self.status_true, self.pust))
                    self.conn.commit()
                    self.conn.close()
                    self.markup1 = types.ReplyKeyboardMarkup(True, True)
                    self.button_1 = types.KeyboardButton("????????????")
                    self.button_2 = types.KeyboardButton("????????????????")
                    self.button_3 = types.KeyboardButton("????????????????????????????")
                    self.markup1.add(self.button_1, self.button_2, self.button_3)
                    self.bot.send_message(message.chat.id, "???????????? ???????????????????? ????????????????:", reply_markup=self.markup1)
                else:
                    self.status_true = 'unbanned'
                    self.balance = 0#???????????? ??????????
                    self.cursor.execute(f"INSERT or IGNORE INTO Data VALUES(?, ?, ?, ?)", (self.id, self.balance, self.status_true, self.pust))
                    self.conn.commit()
                    self.conn.close()
                    self.markup1 = types.ReplyKeyboardMarkup(True, True)
                    self.button_1 = types.KeyboardButton("????????????")
                    self.button_2 = types.KeyboardButton("????????????????")
                    self.button_3 = types.KeyboardButton("?????????????????")
                    self.markup1.add(self.button_1, self.button_2, self.button_3)
                    self.bot.send_message(message.chat.id, "???????????? ???????????????????? ????????????????:", reply_markup=self.markup1)
                    self.id = message.chat.id
            elif str(self.cs) == "[('admin', 'admin')]":
                self.b = self.cursor.execute('SELECT Balance, Balance FROM Data WHERE ID = ?', (self.id,))
                self.balance = str(self.cursor.fetchall())
                self.f = self.balance.index('(')
                self.c = self.balance.index(',')
                self.balance = int(self.balance[self.f+1:self.c])
                self.conn.commit()
                self.conn.close
                self.markup1 = types.ReplyKeyboardMarkup(True, True)
                self.button_1 = types.KeyboardButton("????????????")
                self.button_2 = types.KeyboardButton("????????????????")
                self.button_3 = types.KeyboardButton("????????????????????????????")
                self.markup1.add(self.button_1, self.button_2, self.button_3)
                self.bot.send_message(message.chat.id, "???????????? ???????????????????? ????????????????:", reply_markup=self.markup1)
            elif str(self.ch) != '[]':
                self.b = self.cursor.execute('SELECT Balance, Balance FROM Data WHERE ID = ?', (self.id,))
                self.balance = str(self.cursor.fetchall())
                self.f = self.balance.index('(')
                self.c = self.balance.index(',')
                self.balance = int(self.balance[self.f+1:self.c])
                self.conn.commit()
                self.conn.close
                self.markup1 = types.ReplyKeyboardMarkup(True, True)
                self.button_1 = types.KeyboardButton("????????????")
                self.button_2 = types.KeyboardButton("????????????????")
                self.button_3 = types.KeyboardButton("?????????????????")
                self.markup1.add(self.button_1, self.button_2, self.button_3)
                self.bot.send_message(message.chat.id, "???????????? ???????????????????? ????????????????:", reply_markup=self.markup1)
                

        @self.bot.message_handler(func=lambda message: True)
        def handle_message(message):
            self.init_db()
            if message.text == '????????????':
                markup = telebot.types.InlineKeyboardMarkup()
                markup.add(telebot.types.InlineKeyboardButton(text='??????????????', callback_data=1))
                markup.add(telebot.types.InlineKeyboardButton(text='????????????', callback_data=2))
                self.bot.send_message(message.chat.id, text = "?????????????? ????????:", reply_markup=markup)
            elif message.text == '????????????????':
                self.init_db()
                self.id = message.chat.id
                self.init_db()
                self.cursor = self.conn.cursor()
                self.get = self.cursor.execute('SELECT Balance, Balance FROM Data WHERE ID = ?', (self.id,))
                self.get_1 = str(self.cursor.fetchall())
                self.conn.commit()
                self.conn.close
                self.f = self.get_1.index('(')
                self.c = self.get_1.index(',')
                self.balance = int(self.get_1[self.f+1:self.c])
                markup = telebot.types.InlineKeyboardMarkup()
                markup.add(telebot.types.InlineKeyboardButton(text='??????????????', callback_data='deposit'))
                markup.add(telebot.types.InlineKeyboardButton(text='??????????', callback_data='withdraw'))
                self.text_balance = str("?????? ????????????: "+str(self.balance))
                self.bot.send_message(message.chat.id, self.text_balance, reply_markup=markup)
            elif message.text == '?????????????????':
                self.faq = '???????? "Fruits".\n ???????????????????? ????????????????????:\n '
                self.bot.send_message(message.chat.id, self.faq, reply_markup=markup)
            elif message.text == '???????????':
                self.init_db()
                self.cursor.execute("""UPDATE Data SET Balance = ? WHERE ID = ?""", (self.balance, self.id))
                self.conn.commit()
                self.conn.close
                self.bot.send_message(message.chat.id, "???????????? ???????????????????? ????????????????", reply_markup=self.markup1)
            elif message.text == 'Classic????':
                self.markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                self.button_respin = types.KeyboardButton("????????????")
                self.button_m = types.KeyboardButton("???????????")
                self.markup.add(self.button_respin, self.button_m)
                self.bot.send_message(message.chat.id,text = "????????: Classic????", reply_markup=self.markup)
                self.buttons = [ [{'50': 'bet1'}, {'100': 'bet2'}, {'200': 'bet3'}], [{'300': 'bet4'}, {'500': 'bet5'}, {'1000': 'bet6'}]]
                self.keyboard = Keyboa(items=self.buttons)
                self.bot.send_message(message.chat.id, text = "????????????:", reply_markup=self.keyboard())
            elif message.text == '????????????':
                self.init_db()
                self.id = message.chat.id
                self.init_db()
                self.cursor = self.conn.cursor()
                self.get = self.cursor.execute('SELECT Balance, Balance FROM Data WHERE ID = ?', (self.id,))
                self.get_1 = str(self.cursor.fetchall())
                self.conn.commit()
                self.conn.close
                self.f = self.get_1.index('(')
                self.c = self.get_1.index(',')
                self.balance = int(self.get_1[self.f+1:self.c])
                if self.balance - self.bet_change <= -1:
                    self.bot.send_message(message.chat.id, text = "???????????????????????? ?????????????? ???? ??????????.")
                else:
                    self.sent = self.bot.send_dice(message.chat.id, '????')
                    self.sent = str(self.sent)
                    self.sl1 = self.sent.index("'????', 'value': ")
                    self.sl2 = self.sent.index('}}}')
                    self.value = self.sent[self.sl1:self.sl2]
                    self.s3 = self.value.index(':')
                    self.value = int(self.value[self.s3+2:])
                    if self.value == 1 or self.value == 22 or self.value == 43 or self.value == 64:
                        time.sleep(2)
                        self.balance -= self.bet_change
                        self.balance += self.bet_change*3 # ?????????????? ?????? ???????????????? ?? ?????????????? ??????????
                        self.init_db()
                        self.cursor.execute("""UPDATE Data SET Balance = ? WHERE ID = ?""", (self.balance, self.id))
                        self.set_history = self.cursor.execute('SELECT Game_history FROM Data WHERE ID = ?', (self.id,))
                        self.set_history = str(self.cursor.fetchall())
                        print(self.set_history)
                        self.cursor.execute("""UPDATE Data SET Game_history = ? WHERE ID = ?""", (str(self.set_history)
                                                                                                  +"????????: Classic, ??????????????: -"+str(self.bet_change),
                                                                                                  self.id))
                        self.cursor.execute("""UPDATE Data SET Balance = ? WHERE ID = ?""", (self.balance, self.id))
                        self.conn.commit()
                        self.conn.close()
                        self.bot.send_message(message.chat.id, text = "??????????????????????! ???? ???????????? ??????????????! \n ????????????: " +str(self.balance))
                    else:
                        time.sleep(2)
                        self.balance -= self.bet_change
                        self.init_db()
                        self.cursor.execute("""UPDATE Data SET Balance = ? WHERE ID = ?""", (self.balance, self.id))
                        self.set_history = self.cursor.execute('SELECT Game_history FROM Data WHERE ID = ?', (self.id,))
                        self.set_history = str(self.cursor.fetchall())
                        self.cursor.execute("""UPDATE Data SET Game_history = ? WHERE ID = ?""", (str(self.set_history)+"????????: Classic, ????????????????: -"
                                                                                                  +str(self.bet_change), self.id))
                        self.cursor.execute("""UPDATE Data SET Balance = ? WHERE ID = ?""", (self.balance, self.id))
                        self.conn.commit()
                        self.conn.close()
                        self.bot.send_message(message.chat.id, text = "???? ???????????????? \n ????????????: " +str(self.balance))
                
                    self.bot.send_message(message.chat.id, text = "????????????:", reply_markup=self.keyboard())

            elif message.text == 'Fruits????':
                self.markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                self.button_menu = types.KeyboardButton("???????????")
                self.markup.add(self.button_menu)
                self.bot.send_message(message.chat.id,text = "????????: Fruits????", reply_markup=self.markup)
                self.buttons = [{'????????????:': 'label'}, [{'50': 'bet1'}, {'100': 'bet2'}, {'200': 'bet3'}], [{'300': 'bet4'}, {'500': 'bet5'}, {'1000': 'bet6'}],
                                {'??????????:':'lines'},[{'1': 'line1'}, {'2': 'line2'}, {'3': 'line3'}],
                                [{'????????????': 'spin'}]]
                self.keyboard = Keyboa(items=self.buttons)
                self.bot.send_message(message.chat.id, text = "??????????????????????\n??????????????????????\n??????????????????????", reply_markup=self.keyboard())
            elif message.text == 'Gems miner????':
                self.markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                self.button_menu = types.KeyboardButton("???????????")
                self.markup.add(self.button_menu)
                self.bot.send_message(message.chat.id,text = "????????: Gems miner????", reply_markup=self.markup)
                self.buttons = [{'????????????:': 'label'}, [{'50': 'bet1'}, {'100': 'bet2'}, {'200': 'bet3'}], [{'300': 'bet4'}, {'500': 'bet5'}, {'1000': 'bet6'}],
                                {'??????????:':'lines'},[{'1': 'line1'}, {'2': 'line2'}, {'3': 'line3'}],
                                [{'????????????': 'spin1'}]] 

    
                self.keyboard = Keyboa(items=self.buttons)
                self.bot.send_message(message.chat.id, text = "??????????????????????\n??????????????????????\n??????????????????????", reply_markup=self.keyboard())                
            elif message.text == '????????????????????????????':
                self.buttons = []
                self.cursor = self.conn.cursor()
                self.ids = self.cursor.execute('SELECT ID FROM Data')
                self.users = self.cursor.fetchall()
                for user in range (len(self.users)):
                    self.dictt = {}
                    self.user = self.users[user]
                    self.user = str(self.user)[1:-2]
                    self.dictt[str(self.user)] = "user" + str(user)
                    self.buttons.append(self.dictt)
                self.d = []
                self.keyboard = Keyboa(items=self.buttons)
                self.bot.send_message(message.chat.id, text = "????????????????????????:", reply_markup=self.keyboard())
            elif message.text == '???????????????? ????????????':
                self.bot.send_message(message.chat.id, text = "?????????????? ?????????? ??????????????.")
                self.bot.register_next_step_handler(message, give_balance)
        def give_balance(message):
            if message.text == '???????????????? ????????????':
                pass
            else:
                self.init_db()
                self.balance = int(message.text)
                self.cursor.execute("""UPDATE Data SET Balance = ? WHERE ID = ?""", (int(message.text), self.id))
                self.conn.commit()
                self.conn.close
                self.bot.send_message(message.chat.id, text = "???????????? ???????????????????")
                
        @self.bot.callback_query_handler(func=lambda call: True)
        def query_handler(call):
            if call.data == 'check_pay':
                pass
            elif call.data == '1':
                self.markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                self.button_4 = types.KeyboardButton("Gems miner????")
                self.button_5 = types.KeyboardButton("Classic????")
                self.button_6 = types.KeyboardButton("Fruits????")
                self.button_7 = types.KeyboardButton("???????????")
                self.markup.add(self.button_4, self.button_5, self.button_6, self.button_7)
                self.msg = self.bot.send_message(call.message.chat.id,text = "???????????? ????????:", reply_markup=self.markup)
            elif call.data == '2':
                self.markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                self.button_menu = types.KeyboardButton("???????????")
                self.markup.add(self.button_menu)
                self.bot.send_message(call.message.chat.id,text = "???????????? ???????????????????? ????????????????", reply_markup=self.markup)
                self.buttons = [[{'<3': 'b'}, {'3<': 'm'}], {'????????????:': 'label'}, [{'50': 'bet1'}, {'100': 'bet2'}, {'200': 'bet3'}], [{'300': 'bet4'}, {'500': 'bet5'}, {'1000': 'bet6'}],
                                [{'????????????': 'play'}]]
                self.keyboard = Keyboa(items=self.buttons)
                self.bot.send_message(call.message.chat.id, text = "????????: ????????????", reply_markup=self.keyboard())
    
            elif call.data == 'deposit':
                self.buttons = [[{'YooMoney': 'ym'}]]
                self.keyboard = Keyboa(items=self.buttons)
                self.bot.send_message(call.message.chat.id, text = "???????????? ?????????????????? ??????????????:", reply_markup=self.keyboard())
            elif call.data == 'ym': 
                self.buttons = [[{'100': 'q1'}, {'200':'q2'}], [{'500': 'q3'}, {'1000':'q4'}],[{'2000': 'q5'}]]
                self.keyboard = Keyboa(items=self.buttons)
                self.bot.send_message(call.message.chat.id, text = "???????????? ?????????? ????????????????", reply_markup=self.keyboard())
                
            elif call.data == 'q1':
                self.sum = 100
                self.label = str(random.randint(100000, 999999))
                self.client = Client(self.ymoney_token)
                self.user = self.client.account_info()
                self.cards = self.user.cards_linked
                self.quickpay = Quickpay(
                    receiver="4100117820521086",
                    quickpay_form="shop",
                    targets="Sponsor this project",
                    paymentType="SB",
                    sum=self.sum,
                    label = self.label
                    )
                self.keyboard = types.InlineKeyboardMarkup()
                self.url_button = types.InlineKeyboardButton(text="?????????????? ?? ????????????", url = str(self.quickpay.base_url))
                self.url_button_1 = types.InlineKeyboardButton(text="?????????????????? ????????????", callback_data='check_payment')
                self.keyboard.add(self.url_button, self.url_button_1)
                self.bot.send_message(call.message.chat.id, text = "???????????? ???????????????????? ????????????????:", reply_markup=self.keyboard)
            elif call.data == 'q2':
                self.sum = 200
                self.label = str(random.randint(100000, 999999))
                self.client = Client(self.ymoney_token)
                self.user = self.client.account_info()
                self.cards = self.user.cards_linked
                self.quickpay = Quickpay(
                    receiver="4100117820521086",
                    quickpay_form="shop",
                    targets="Sponsor this project",
                    paymentType="SB",
                    sum=self.sum,
                    label = self.label
                    )
                self.keyboard = types.InlineKeyboardMarkup()
                self.url_button = types.InlineKeyboardButton(text="?????????????? ?? ????????????", url = str(self.quickpay.base_url))
                self.url_button_1 = types.InlineKeyboardButton(text="?????????????????? ????????????", callback_data='check_payment')
                self.keyboard.add(self.url_button, self.url_button_1)
                self.bot.send_message(call.message.chat.id, text = "???????????? ???????????????????? ????????????????:", reply_markup=self.keyboard)
            elif call.data == 'q3':
                self.sum = 500
                self.label = str(random.randint(100000, 999999))
                self.client = Client(self.ymoney_token)
                self.user = self.client.account_info()
                self.cards = self.user.cards_linked
                self.quickpay = Quickpay(
                    receiver="4100117820521086",
                    quickpay_form="shop",
                    targets="Sponsor this project",
                    paymentType="SB",
                    sum=self.sum,
                    label = self.label
                    )
                self.keyboard = types.InlineKeyboardMarkup()
                self.url_button = types.InlineKeyboardButton(text="?????????????? ?? ????????????", url = str(self.quickpay.base_url))
                self.url_button_1 = types.InlineKeyboardButton(text="?????????????????? ????????????", callback_data='check_payment')
                self.keyboard.add(self.url_button, self.url_button_1)
                self.bot.send_message(call.message.chat.id, text = "???????????? ???????????????????? ????????????????:", reply_markup=self.keyboard)
            elif call.data == 'q4':
                self.sum = 1000
                self.label = str(random.randint(100000, 999999))
                self.client = Client(self.ymoney_token)
                self.user = self.client.account_info()
                self.cards = self.user.cards_linked
                self.quickpay = Quickpay(
                    receiver="4100117820521086",
                    quickpay_form="shop",
                    targets="Sponsor this project",
                    paymentType="SB",
                    sum=self.sum,
                    label = self.label
                    )
                self.keyboard = types.InlineKeyboardMarkup()
                self.url_button = types.InlineKeyboardButton(text="?????????????? ?? ????????????", url = str(self.quickpay.base_url))
                self.url_button_1 = types.InlineKeyboardButton(text="?????????????????? ????????????", callback_data='check_payment')
                self.keyboard.add(self.url_button, self.url_button_1)
                self.bot.send_message(call.message.chat.id, text = "???????????? ???????????????????? ????????????????:", reply_markup=self.keyboard)
            elif call.data == 'q5':
                self.sum = 1000
                self.label = str(random.randint(100000, 999999))
                self.client = Client(self.ymoney_token)
                self.user = self.client.account_info()
                self.cards = self.user.cards_linked
                self.quickpay = Quickpay(
                    receiver="4100117820521086",
                    quickpay_form="shop",
                    targets="Sponsor this project",
                    paymentType="SB",
                    sum=self.sum,
                    label = self.label
                    )
                self.keyboard = types.InlineKeyboardMarkup()
                self.url_button = types.InlineKeyboardButton(text="?????????????? ?? ????????????", url = str(self.quickpay.base_url))
                self.url_button_1 = types.InlineKeyboardButton(text="?????????????????? ????????????", callback_data='check_payment')
                self.keyboard.add(self.url_button, self.url_button_1)
                self.bot.send_message(call.message.chat.id, text = "???????????? ???????????????????? ????????????????:", reply_markup=self.keyboard)
            elif call.data == 'check_payment':
                self.history = client.operation_history(label=self.label)
                for operation in history.operations:
                    operation.operation_id
                    self.opst = operation.status
                    operation.datetime
                    operation.title
                    operation.pattern_id
                    operation.direction
                    self.amount = operation.amount
                    self.labelop = operation.label
                    operation.type
                if self.opst == 'success' and self.labelop == self.label:
                    self.bot.send_message(call.message.chat.id, text = "???????????? ??????????????!\n???????????? ????????????????.")
                    self.init_db()
                    self.cursor.execute("""UPDATE Data SET Balance = ? WHERE ID = ?""", (int(self.amount), call.message.chat.id))
                    self.conn.commit()
                    self.conn.close()
                    
            elif call.data == 'b':
                self.bet = 1
            elif call.data == 'm':
                self.bet = 2
            elif call.data == 'bet1':
                self.bet_change = 50
            elif call.data == 'bet2':
                self.bet_change = 100
            elif call.data == 'bet3':
                self.bet_change = 200
            elif call.data == 'bet4':
                self.bet_change = 300
            elif call.data == 'bet5':
                self.bet_change = 500
            elif call.data == 'bet6':
                self.bet_change = 1000
            elif call.data == 'play':
                self.id = call.message.chat.id
                self.init_db()
                self.b = self.cursor.execute('SELECT Balance, Balance FROM Data WHERE ID = ?', (self.id,))
                self.balance = str(self.cursor.fetchall())
                self.f = self.balance.index('(')
                self.c = self.balance.index(',')
                self.balance = int(self.balance[self.f+1:self.c])
                self.conn.commit()
                self.conn.close
                self.id = call.message.chat.id
                self.init_db()
                self.cursor = self.conn.cursor()
                self.get = self.cursor.execute('SELECT Balance, Balance FROM Data WHERE ID = ?', (self.id,))
                self.get_1 = str(self.cursor.fetchall())
                self.conn.commit()
                self.conn.close
                self.f = self.get_1.index('(')
                self.c = self.get_1.index(',')
                self.balance = int(self.get_1[self.f+1:self.c])
                if self.balance - self.bet <= 0:
                    self.bot.send_message(call.message.chat.id, text = "???????????????????????? ?????????????? ???? ??????????.")
                elif self.balance - self.bet > 0:
                    self.sent = self.bot.send_dice(call.message.chat.id, '????')
                    self.sent = str(self.sent)
                    self.sl1 = self.sent.index("'????', 'value': ")
                    self.sl2 = self.sent.index('}}}')
                    self.value = self.sent[self.sl1:self.sl2]
                    self.s3 = self.value.index(':')
                    self.value = int(self.value[self.s3+2:])
                    if self.bet == 1:
                        if self.value < 3:
                            time.sleep(4)
                            self.balance += self.bet_change
                            self.init_db()
                            self.cursor.execute("""UPDATE Data SET Balance = ? WHERE ID = ?""", (self.balance, self.id))
                            self.set_history = self.cursor.execute('SELECT Game_history FROM Data WHERE ID = ?', (self.id,))
                            self.set_history = str(self.cursor.fetchall())
                            
                            self.cursor.execute("""UPDATE Data SET Game_history = ? WHERE ID = ?""",
                                                (str(self.set_history)+"????????: ????????, ????????????: +"+str(self.bet_change), self.id))
                            self.conn.commit()
                            self.conn.close()
                            self.bot.send_message(call.message.chat.id, text = "???? ??????????????! \n ????????????: " +str(self.balance))
                        else:
                            time.sleep(4)
                            self.balance -= self.bet_change
                            self.init_db()
                            self.cursor.execute("""UPDATE Data SET Balance = ? WHERE ID = ?""", (self.balance, self.id))
                            self.set_history = self.cursor.execute('SELECT Game_history FROM Data WHERE ID = ?', (self.id,))
                            self.set_history = str(self.cursor.fetchall())
                            self.cursor.execute("""UPDATE Data SET Game_history = ? WHERE ID = ?""",
                                                (str(self.set_history)+"????????: ????????, ????????????????: -"+str(self.bet_change), self.id))
                            self.conn.commit()
                            self.conn.close()
                            self.bot.send_message(call.message.chat.id, text = "???? ???????????????? \n ????????????: " +str(self.balance))
                    else:
                        if self.value < 3:
                            time.sleep(4)
                            self.balance -= self.bet_change
                            self.init_db()
                            self.cursor.execute("""UPDATE Data SET Balance = ? WHERE ID = ?""", (self.balance, self.id))
                            self.set_history = self.cursor.execute('SELECT Game_history FROM Data WHERE ID = ?', (self.id,))
                            self.set_history = str(self.cursor.fetchall())
                            self.cursor.execute("""UPDATE Data SET Game_history = ? WHERE ID = ?""",
                                                (str(self.set_history)+"????????: ????????, ????????????????: -"+str(self.bet_change), self.id))
                            self.conn.commit()
                            self.conn.close()
                            self.bot.send_message(call.message.chat.id, text = "???? ???????????????? \n ????????????: " +str(self.balance))
                        else:
                            time.sleep(4)
                            self.balance += self.bet_change
                            self.init_db()
                            self.cursor.execute("""UPDATE Data SET Balance = ? WHERE ID = ?""", (self.balance, self.id))
                            self.set_history = self.cursor.execute('SELECT Game_history FROM Data WHERE ID = ?', (self.id,))
                            self.set_history = str(self.cursor.fetchall())
                            self.cursor.execute("""UPDATE Data SET Game_history = ? WHERE ID = ?""",
                                                (str(self.set_history)+"????????: ????????, ????????????: +"+str(self.bet_change), self.id))
                            self.conn.commit()
                            self.conn.close()
                            self.bot.send_message(call.message.chat.id, text = "???? ??????????????! \n ????????????: " +str(self.balance))
            elif call.data == 'spin':
                self.id = call.message.chat.id
                self.init_db()
                self.b = self.cursor.execute('SELECT Balance, Balance FROM Data WHERE ID = ?', (self.id,))
                self.balance = str(self.cursor.fetchall())
                self.f = self.balance.index('(')
                self.c = self.balance.index(',')
                self.balance = int(self.balance[self.f+1:self.c])
                self.conn.commit()
                self.conn.close
                if self.balance - self.bet_change <= -1:
                    self.bot.delete_message(call.message.chat.id, call.message.message_id)
                    self.bot.send_message(call.message.chat.id, text = "???????????????????????? ??????????????. \n ????????????: "+ str(self.balance))
                else:
                    self.balance -= self.bet_change
                    self.list = []
                    self.str_fruits = ''
                    self.fruit = {1: '????', 2: '????', 3: '????', 4: '????', 5: '????', 6: '????', 7: '????', 8: '????',}
                    for i in range(18): #???????????????????? ?????????????? ????????????
                        self.list.append(random.randint(1, 8))
                    for j in range(18):
                        if j == 0 or j == 6 or j == 12:
                            self.list[j] = '???'
                        elif j ==5  or j == 11 or j == 17:
                            self.list[j] = '???'
                        else:
                            self.list[j] = self.fruit[self.list[j]]
                    for k in range(18):
                        if k == 5 or k == 11:
                            self.str_fruits += self.list[k] + '\n'
                        else:
                            self.str_fruits += self.list[k]
                    if self.line == 1:
                        if self.str_fruits[3] == '????' or self.str_fruits[1]==  '????' or self.str_fruits[2]==  '????':
                            if self.str_fruits[1] == self.str_fruits[2] or self.str_fruits[2] == self.str_fruits[3] or self.str_fruits[3] == self.str_fruits[4]:
                                self.bet = self.bet_change*2
                                self.bbalance = self.balance+self.bet
                                self.init_db()
                                self.cursor.execute("""UPDATE Data SET Balance = ? WHERE ID = ?""", (self.bbalance, self.id))
                                self.conn.commit()
                                self.conn.close()
                                self.str_fruits += '\n ???? ??????????????!(2??)\n ????????????:' + str(self.bbalance)
                                self.balance = self.bbalance
                                self.bot.delete_message(call.message.chat.id, call.message.message_id)
                                self.bot.send_message(call.message.chat.id, self.str_fruits, reply_markup=self.keyboard())
                        elif self.str_fruits[3] == '????' or self.str_fruits[1]== '????' or self.str_fruits[2]== '????':
                            if self.str_fruits[1] == self.str_fruits[2] or self.str_fruits[2] == self.str_fruits[3] or self.str_fruits[3] == self.str_fruits[4]:
                                self.bet = self.bet_change*1.5
                                self.bbalance = self.balance+self.bet
                                self.init_db()
                                self.cursor.execute("""UPDATE Data SET Balance = ? WHERE ID = ?""", (self.bbalance, self.id))
                                self.set_history = self.cursor.execute('SELECT Game_history FROM Data WHERE ID = ?', (self.id,))
                                self.cursor.execute("""UPDATE Data SET Game_history = ? WHERE ID = ?""", (str(self.set_history)+"????????: Fruits, ????????????: +"+str(self.bet), self.id))
                                self.conn.commit()
                                self.conn.close()
                                self.str_fruits += '\n ???? ??????????????!(1.5??)\n ????????????:' + str(self.bbalance)
                                self.balance = self.bbalance
                                self.bot.delete_message(call.message.chat.id, call.message.message_id)
                                self.bot.send_message(call.message.chat.id, self.str_fruits, reply_markup=self.keyboard())
                        elif self.str_fruits[3] ==  '????' or self.str_fruits[1]== '????' or self.str_fruits[2]== '????':
                            if self.str_fruits[1] == self.str_fruits[2] or self.str_fruits[2] == self.str_fruits[3] or self.str_fruits[3] == self.str_fruits[4]:
                                self.bet = self.bet_change*1.3
                                self.bbalance = self.balance+self.bet
                                self.init_db()
                                self.cursor.execute("""UPDATE Data SET Balance = ? WHERE ID = ?""", (self.bbalance, self.id))
                                self.set_history = self.cursor.execute('SELECT Game_history FROM Data WHERE ID = ?', (self.id,))
                                self.cursor.execute("""UPDATE Data SET Game_history = ? WHERE ID = ?""", (str(self.set_history)+"????????: Fruits, ????????????: +"+str(self.bet), self.id))
                                self.conn.commit()
                                self.conn.close()
                                self.str_fruits += '\n ???? ??????????????!(1.3??)\n ????????????:' + str(self.bbalance)
                                self.balance = self.bbalance
                                self.bot.delete_message(call.message.chat.id, call.message.message_id)
                                self.bot.send_message(call.message.chat.id, self.str_fruits, reply_markup=self.keyboard())
                    
                    if self.line == 2:
                        if self.str_fruits[7] == '????' or self.str_fruits[8]==  '????' or self.str_fruits[8]==  '????':
                            if self.str_fruits[7] == self.str_fruits[8] or self.str_fruits[8] == self.str_fruits[9] or self.str_fruits[9] == self.str_fruits[10]:
                                self.bet = self.bet_change*2
                                self.init_db()
                                self.cursor.execute("""UPDATE Data SET Balance = ? WHERE ID = ?""", (self.balance+self.bet, self.id))
                                self.set_history = self.cursor.execute('SELECT Game_history FROM Data WHERE ID = ?', (self.id,))
                                self.set_history = str(self.cursor.fetchall())
                                self.cursor.execute("""UPDATE Data SET Game_history = ? WHERE ID = ?""", (str(self.set_history)+"????????: Fruits, ????????????: +"+str(self.bet), self.id))
                                self.conn.commit()
                                self.conn.close()
                                self.str_fruits += '\n ???? ??????????????!(2??)\n ????????????:' + str(self.balance)
                                self.bot.delete_message(call.message.chat.id, call.message.message_id)
                                self.bot.send_message(call.message.chat.id, self.str_fruits, reply_markup=self.keyboard())
                        elif self.str_fruits[7] == '????' or self.str_fruits[8]== '????' or self.str_fruits[9]== '????':
                            if self.str_fruits[7] == self.str_fruits[8] or self.str_fruits[8] == self.str_fruits[9] or self.str_fruits[9] == self.str_fruits[10]:
                                self.bet = self.bet_change*1.5
                                self.init_db()
                                self.cursor.execute("""UPDATE Data SET Balance = ? WHERE ID = ?""", (self.balance+self.bet, self.id))
                                self.set_history = self.cursor.execute('SELECT Game_history FROM Data WHERE ID = ?', (self.id,))
                                self.set_history = str(self.cursor.fetchall())
                                self.cursor.execute("""UPDATE Data SET Game_history = ? WHERE ID = ?""", (str(self.set_history)+"????????: Fruits, ????????????: +"+str(self.bet), self.id))
                                self.conn.commit()
                                self.conn.close()
                                self.str_fruits += '\n ???? ??????????????!(1.5??)\n ????????????:' + str(self.balance)
                                self.bot.delete_message(call.message.chat.id, call.message.message_id)
                                self.bot.send_message(call.message.chat.id, self.str_fruits, reply_markup=self.keyboard())
                        elif self.str_fruits[7] ==  '????' or self.str_fruits[8]== '????' or self.str_fruits[9]== '????':
                            if self.str_fruits[7] == self.str_fruits[8] or self.str_fruits[8] == self.str_fruits[9] or self.str_fruits[9] == self.str_fruits[10]:
                                self.bet = self.bet_change*1.3
                                self.init_db()
                                self.cursor.execute("""UPDATE Data SET Balance = ? WHERE ID = ?""", (self.balance+self.bet, self.id))
                                self.set_history = self.cursor.execute('SELECT Game_history FROM Data WHERE ID = ?', (self.id,))
                                self.set_history = str(self.cursor.fetchall())
                                self.cursor.execute("""UPDATE Data SET Game_history = ? WHERE ID = ?""", (str(self.set_history)+"????????: Fruits, ????????????: +"+str(self.bet), self.id))
                                self.conn.commit()
                                self.conn.close()
                                self.str_fruits += '\n ???? ??????????????!(1.3??)\n ????????????:' + str(self.balance)
                                self.bot.delete_message(call.message.chat.id, call.message.message_id)
                                self.bot.send_message(call.message.chat.id, self.str_fruits, reply_markup=self.keyboard())
                        if self.line == 3:
                            if self.str_fruits[13] == '????' or self.str_fruits[14]==  '????' or self.str_fruits[15]==  '????':
                                if self.str_fruits[13] == self.str_fruits[14] or self.str_fruits[14] == self.str_fruits[15] or self.str_fruits[15] == self.str_fruits[16]:
                                    self.bet = self.bet_change*2
                                    self.init_db()
                                    self.cursor.execute("""UPDATE Data SET Balance = ? WHERE ID = ?""", (self.balance+self.bet, self.id))
                                    self.set_history = self.cursor.execute('SELECT Game_history FROM Data WHERE ID = ?', (self.id,))
                                    self.set_history = str(self.cursor.fetchall())
                                    self.cursor.execute("""UPDATE Data SET Game_history = ? WHERE ID = ?""", (str(self.set_history)+"????????: Fruits, ????????????: +"+str(self.bet), self.id))
                                    self.conn.commit()
                                    self.conn.close()
                                    self.str_fruits += '\n ???? ??????????????!(2??)\n ????????????:' + str(self.balance)
                                    self.bot.delete_message(call.message.chat.id, call.message.message_id)
                                    self.bot.send_message(call.message.chat.id, self.str_fruits, reply_markup=self.keyboard())
                            elif self.str_fruits[13] == '????' or self.str_fruits[14]== '????' or self.str_fruits[15]== '????':
                                if self.str_fruits[13] == self.str_fruits[14] or self.str_fruits[14] == self.str_fruits[15] or self.str_fruits[15] == self.str_fruits[16]:
                                    self.bet = self.bet_change*1.5
                                    self.init_db()
                                    self.cursor.execute("""UPDATE Data SET Balance = ? WHERE ID = ?""", (self.balance+self.bet, self.id))
                                    self.set_history = self.cursor.execute('SELECT Game_history FROM Data WHERE ID = ?', (self.id,))
                                    self.set_history = str(self.cursor.fetchall())
                                    self.cursor.execute("""UPDATE Data SET Game_history = ? WHERE ID = ?""", (str(self.set_history)+"????????: Fruits, ????????????: +"+str(self.bet), self.id))
                                    self.conn.commit()
                                    self.conn.close()
                                    self.str_fruits += '\n ???? ??????????????!(1.5??)\n ????????????:' + str(self.balance)
                                    self.bot.delete_message(call.message.chat.id, call.message.message_id)
                                    self.bot.send_message(call.message.chat.id, self.str_fruits, reply_markup=self.keyboard())
                            elif self.str_fruits[13] ==  '????' or self.str_fruits[14]== '????' or self.str_fruits[15]== '????':
                                if self.str_fruits[13] == self.str_fruits[14] or self.str_fruits[14] == self.str_fruits[15] or self.str_fruits[15] == self.str_fruits[16]:
                                    self.bet = self.bet_change*1.3
                                    self.init_db()
                                    self.cursor.execute("""UPDATE Data SET Balance = ? WHERE ID = ?""", (self.balance+self.bet, self.id))
                                    self.set_history = self.cursor.execute('SELECT Game_history FROM Data WHERE ID = ?', (self.id,))
                                    self.set_history = str(self.cursor.fetchall())
                                    self.cursor.execute("""UPDATE Data SET Game_history = ? WHERE ID = ?""", (str(self.set_history)+"????????: Fruits, ????????????: +"+str(self.bet), self.id))
                                    self.conn.commit()
                                    self.conn.close()
                                    self.str_fruits += '\n ???? ??????????????!(1.3??)\n ????????????:' + str(self.balance)
                                    self.bot.delete_message(call.message.chat.id, call.message.message_id)
                                    self.bot.send_message(call.message.chat.id, self.str_fruits, reply_markup=self.keyboard())
                    self.bot.delete_message(call.message.chat.id, call.message.message_id)
                    self.bot.send_message(call.message.chat.id, self.str_fruits, reply_markup=self.keyboard())
                
                
            elif call.data == 'spin1':
                self.id = call.message.chat.id
                self.init_db()
                self.b = self.cursor.execute('SELECT Balance, Balance FROM Data WHERE ID = ?', (self.id,))
                self.balance = str(self.cursor.fetchall())
                self.f = self.balance.index('(')
                self.c = self.balance.index(',')
                self.balance = int(self.balance[self.f+1:self.c])
                self.conn.commit()
                self.conn.close
                if self.balance - self.bet_change <= -1:
                    self.bot.delete_message(call.message.chat.id, call.message.message_id)
                    self.bot.send_message(call.message.chat.id, text = "???????????????????????? ??????????????. \n ????????????: "+ str(self.balance))
                else:
                    self.balance -= self.bet_change
                    self.init_db()
                    self.cursor.execute("""UPDATE Data SET Balance = ? WHERE ID = ?""", (self.balance+self.bet_change, self.id))
                    self.conn.commit()
                    self.conn.close()
                    self.list = []
                    self.str_fruits = ''
                    self.fruit = {1: '????', 2: '????', 3: '????', 4: '????', 5: '????', 6: '???', 7: '????', 8: '???'}
                    for i in range(18): #???????????????????? ?????????????? ????????????
                        self.list.append(random.randint(1, 8))
                    for j in range(18):
                        if j == 0 or j == 6 or j == 12:
                            self.list[j] = '???'
                        elif j ==5  or j == 11 or j == 17:
                            self.list[j] = '???'
                        else:
                            self.list[j] = self.fruit[self.list[j]]
                for k in range(18):
                    if k == 5 or k == 11:
                        self.str_fruits += self.list[k] + '\n'
                    else:
                        self.str_fruits += self.list[k]
                if self.line == 1:
                    if self.str_fruits[3] == '????' or self.str_fruits[1]==  '????' or self.str_fruits[2]==  '????':
                        if self.str_fruits[1] == self.str_fruits[2] or self.str_fruits[2] == self.str_fruits[3] or self.str_fruits[3] == self.str_fruits[4]:
                            self.bet = self.bet_change*2
                            self.bbalance = self.balance+self.bet
                            self.init_db()
                            self.cursor.execute("""UPDATE Data SET Balance = ? WHERE ID = ?""", (self.bbalance, self.id))
                            self.set_history = self.cursor.execute('SELECT Game_history FROM Data WHERE ID = ?', (self.id,))
                            self.set_history = str(self.cursor.fetchall())
                            self.cursor.execute("""UPDATE Data SET Game_history = ? WHERE ID = ?""", (str(self.set_history)+"????????: Gems Miner, ????????????: +"+str(self.bet), self.id))
                            self.conn.commit()
                            self.conn.close()
                            self.str_fruits += '\n ???? ??????????????!(2??)\n ????????????:' + str(self.bbalance)
                            self.balance = self.bbalance
                            self.bot.delete_message(call.message.chat.id, call.message.message_id)
                            self.bot.send_message(call.message.chat.id, self.str_fruits, reply_markup=self.keyboard())
                    elif self.str_fruits[3] == '????' or self.str_fruits[1]== '????' or self.str_fruits[2]== '????':
                        if self.str_fruits[1] == self.str_fruits[2] or self.str_fruits[2] == self.str_fruits[3] or self.str_fruits[3] == self.str_fruits[4]:
                            self.bet = self.bet_change*1.5
                            self.bbalance = self.balance+self.bet
                            self.init_db()
                            self.cursor.execute("""UPDATE Data SET Balance = ? WHERE ID = ?""", (self.bbalance, self.id))
                            self.set_history = self.cursor.execute('SELECT Game_history FROM Data WHERE ID = ?', (self.id,))
                            self.set_history = str(self.cursor.fetchall())
                            self.cursor.execute("""UPDATE Data SET Game_history = ? WHERE ID = ?""", (str(self.set_history)+"????????: Gems Miner, ????????????: +"+str(self.bet), self.id)) 
                            self.conn.commit()
                            self.conn.close()
                            self.str_fruits += '\n ???? ??????????????!(1.5??)\n ????????????:' + str(self.bbalance)
                            self.balance = self.bbalance
                            self.bot.delete_message(call.message.chat.id, call.message.message_id)
                            self.bot.send_message(call.message.chat.id, self.str_fruits, reply_markup=self.keyboard())
                    elif self.str_fruits[3] ==  '????' or self.str_fruits[1]== '????' or self.str_fruits[2]== '????':
                        if self.str_fruits[1] == self.str_fruits[2] or self.str_fruits[2] == self.str_fruits[3] or self.str_fruits[3] == self.str_fruits[4]:
                            self.bet = self.bet_change*1.3
                            self.bbalance = self.balance+self.bet
                            self.init_db()
                            self.cursor.execute("""UPDATE Data SET Balance = ? WHERE ID = ?""", (self.bbalance, self.id))
                            self.set_history = self.cursor.execute('SELECT Game_history FROM Data WHERE ID = ?', (self.id,))
                            self.set_history = str(self.cursor.fetchall())
                            self.cursor.execute("""UPDATE Data SET Game_history = ? WHERE ID = ?""", (str(self.set_history)+"????????: Gems Miner, ????????????: +"+str(self.bet), self.id))
                            self.conn.commit()
                            self.conn.close()
                            self.str_fruits += '\n ???? ??????????????!(1.3??)\n ????????????:' + str(self.bbalance)
                            self.balance = self.bbalance
                            self.bot.delete_message(call.message.chat.id, call.message.message_id)
                            self.bot.send_message(call.message.chat.id, self.str_fruits, reply_markup=self.keyboard())
                    
                    elif self.line == 2:
                        if self.str_fruits[7] == '????' or self.str_fruits[8]==  '????' or self.str_fruits[8]==  '????':
                            if self.str_fruits[7] == self.str_fruits[8] or self.str_fruits[8] == self.str_fruits[9] or self.str_fruits[9] == self.str_fruits[10]:
                                self.bet = self.bet_change*2
                                self.init_db()
                                self.cursor.execute("""UPDATE Data SET Balance = ? WHERE ID = ?""", (self.balance+self.bet, self.id))
                                self.set_history = self.cursor.execute('SELECT Game_history FROM Data WHERE ID = ?', (self.id,))
                                self.set_history = str(self.cursor.fetchall())
                                self.cursor.execute("""UPDATE Data SET Game_history = ? WHERE ID = ?""", (str(self.set_history)+"????????: Gems Miner, ????????????: +"+str(self.bet), self.id))
                                self.conn.commit()
                                self.conn.close()
                                self.str_fruits += '\n ???? ??????????????!(2??)\n ????????????:' + str(self.balance)
                                self.bot.delete_message(call.message.chat.id, call.message.message_id)
                                self.bot.send_message(call.message.chat.id, self.str_fruits, reply_markup=self.keyboard())
                        elif self.str_fruits[7] == '????' or self.str_fruits[8]== '????' or self.str_fruits[9]== '????':
                            if self.str_fruits[7] == self.str_fruits[8] or self.str_fruits[8] == self.str_fruits[9] or self.str_fruits[9] == self.str_fruits[10]:
                                self.bet = self.bet_change*1.5
                                self.init_db()
                                self.cursor.execute("""UPDATE Data SET Balance = ? WHERE ID = ?""", (self.balance+self.bet, self.id))
                                self.set_history = self.cursor.execute('SELECT Game_history FROM Data WHERE ID = ?', (self.id,))
                                self.set_history = str(self.cursor.fetchall())
                                self.cursor.execute("""UPDATE Data SET Game_history = ? WHERE ID = ?""", (str(self.set_history)+"????????: Gems Miner, ????????????: +"+str(self.bet), self.id))
                                self.conn.commit()
                                self.conn.close()
                                self.str_fruits += '\n ???? ??????????????!(1.5??)\n ????????????:' + str(self.balance)
                                self.bot.delete_message(call.message.chat.id, call.message.message_id)
                                self.bot.send_message(call.message.chat.id, self.str_fruits, reply_markup=self.keyboard())
                        elif self.str_fruits[7] ==  '????' or self.str_fruits[8]== '????' or self.str_fruits[9]== '????':
                            if self.str_fruits[7] == self.str_fruits[8] or self.str_fruits[8] == self.str_fruits[9] or self.str_fruits[9] == self.str_fruits[10]:
                                self.bet = self.bet_change*1.3
                                self.init_db()
                                self.cursor.execute("""UPDATE Data SET Balance = ? WHERE ID = ?""", (self.balance+self.bet, self.id))
                                self.set_history = self.cursor.execute('SELECT Game_history FROM Data WHERE ID = ?', (self.id,))
                                self.set_history = str(self.cursor.fetchall())
                                self.cursor.execute("""UPDATE Data SET Game_history = ? WHERE ID = ?""", (str(self.set_history)+"????????: Gems Miner, ????????????: +"+str(self.bet), self.id))
                                self.conn.commit()
                                self.conn.close()
                                self.str_fruits += '\n ???? ??????????????!(1.3??)\n ????????????:' + str(self.balance)
                                self.bot.delete_message(call.message.chat.id, call.message.message_id)
                                self.bot.send_message(call.message.chat.id, self.str_fruits, reply_markup=self.keyboard())
                    elif self.line == 3:
                        if self.str_fruits[13] == '????' or self.str_fruits[14]==  '????' or self.str_fruits[15]==  '????':
                            if self.str_fruits[13] == self.str_fruits[14] or self.str_fruits[14] == self.str_fruits[15] or self.str_fruits[15] == self.str_fruits[16]:
                                self.bet = self.bet_change*2
                                self.init_db()
                                self.cursor.execute("""UPDATE Data SET Balance = ? WHERE ID = ?""", (self.balance+self.bet, self.id))
                                self.set_history = self.cursor.execute('SELECT Game_history FROM Data WHERE ID = ?', (self.id,))
                                self.set_history = str(self.cursor.fetchall())
                                self.cursor.execute("""UPDATE Data SET Game_history = ? WHERE ID = ?""", (str(self.set_history)+"????????: Gems Miner, ????????????: +"+str(self.bet), self.id))
                                self.conn.commit()
                                self.conn.close()
                                self.str_fruits += '\n ???? ??????????????!(2??)\n ????????????:' + str(self.balance)
                                self.bot.delete_message(call.message.chat.id, call.message.message_id)
                                self.bot.send_message(call.message.chat.id, self.str_fruits, reply_markup=self.keyboard())
                        elif self.str_fruits[13] == '????' or self.str_fruits[14]== '????' or self.str_fruits[15]== '????':
                            if self.str_fruits[13] == self.str_fruits[14] or self.str_fruits[14] == self.str_fruits[15] or self.str_fruits[15] == self.str_fruits[16]:
                                self.bet = self.bet_change*1.5
                                self.init_db()
                                self.cursor.execute("""UPDATE Data SET Balance = ? WHERE ID = ?""", (self.balance+self.bet, self.id))
                                self.set_history = self.cursor.execute('SELECT Game_history FROM Data WHERE ID = ?', (self.id,))
                                self.set_history = str(self.cursor.fetchall())
                                self.cursor.execute("""UPDATE Data SET Game_history = ? WHERE ID = ?""", (str(self.set_history)+"????????: Gems Miner, ????????????: +"+str(self.bet), self.id))
                                self.conn.commit()
                                self.conn.close()
                                self.str_fruits += '\n ???? ??????????????!(1.5??)\n ????????????:' + str(self.balance)
                                self.bot.delete_message(call.message.chat.id, call.message.message_id)
                                self.bot.send_message(call.message.chat.id, self.str_fruits, reply_markup=self.keyboard())
                        elif self.str_fruits[13] ==  '????' or self.str_fruits[14]== '????' or self.str_fruits[15]== '????':
                            if self.str_fruits[13] == self.str_fruits[14] or self.str_fruits[14] == self.str_fruits[15] or self.str_fruits[15] == self.str_fruits[16]:
                                self.bet = self.bet_change*1.3
                                self.init_db()
                                self.cursor.execute("""UPDATE Data SET Balance = ? WHERE ID = ?""", (self.balance+self.bet, self.id))
                                self.set_history = self.cursor.execute('SELECT Game_history FROM Data WHERE ID = ?', (self.id,))
                                self.set_history = str(self.cursor.fetchall())
                                self.cursor.execute("""UPDATE Data SET Game_history = ? WHERE ID = ?""", (str(self.set_history)+"????????: Gems Miner, ????????????: +"+str(self.bet), self.id))
                                self.conn.commit()
                                self.conn.close()
                                self.str_fruits += '\n ???? ??????????????!(1.3??)\n ????????????:' + str(self.balance)
                                self.bot.delete_message(call.message.chat.id, call.message.message_id)
                                self.bot.send_message(call.message.chat.id, self.str_fruits, reply_markup=self.keyboard())
                      
                    self.bot.delete_message(call.message.chat.id, call.message.message_id)
                    self.bot.send_message(call.message.chat.id, self.str_fruits, reply_markup=self.keyboard())
            elif call.data == 'game_history':
                self.init_db()
                self.cursor.execute('SELECT Game_history, Game_history FROM Data WHERE ID = ?', (self.id,))
                self.get_game_history = self.cursor.fetchall()
                self.get_game_history = str(self.get_game_history)
                self.conn.commit()
                self.conn.close()
                self.get_game_history = self.get_game_history.replace("[('',)]", "")
                self.get_game_history = self.get_game_history.replace(")]", "")
                self.get_game_history = self.get_game_history.replace("[(", "")
                self.get_game_history = self.get_game_history.replace("\\", "")
                self.get_game_history = self.get_game_history.replace("\\", "")
                self.get_game_history = self.get_game_history.replace("'", "")
                self.get_game_history = self.get_game_history.replace('"', "")
                self.bot.send_message(call.message.chat.id, text = "?????????????? ?????? ???????????????????????? "+str(self.special_id)+"\n"+
                                      self.get_game_history)
                
                
                
            elif call.data == 'ban':
                self.init_db()
                self.cursor.execute("""UPDATE Data SET Status = ? WHERE ID = ?""", (self.status_false, self.special_id))
                self.conn.commit()
                self.conn.close()
                self.bot.send_message(call.message.chat.id, text ="???????????????????????? "+str(self.special_id)+" ?????? ??????????????")
            elif call.data == 'balance_user':
                self.init_db()
                self.cursor = self.conn.cursor()
                self.get = self.cursor.execute('SELECT Balance, Balance FROM Data WHERE ID = ?', (self.id,))
                self.get_1 = str(self.cursor.fetchall())
                self.conn.commit()
                self.conn.close()
                self.f = self.get_1.index('(')
                self.c = self.get_1.index(',')
                self.get = self.get_1[self.f+1:self.c]
                self.bot.answer_callback_query(callback_query_id=call.id, text="???????????? ????????????????????????: " + str(self.get), show_alert=True)
                self.markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                self.button_change = types.KeyboardButton("???????????????? ????????????")
                self.button_m = types.KeyboardButton("???????????")
                self.markup.add(self.button_change, self.button_m)
                self.bot.send_message(call.message.chat.id, text = "????????????????:", reply_markup=self.markup)
                self.bot.delete_message(call.message.chat.id, call.message.message_id)
            elif call.data == 'set_admin':
                self.init_db()
                self.cursor.execute("""UPDATE Data SET Status = ? WHERE ID = ?""", (self.status_admin, self.special_id))
                self.conn.commit()
                self.conn.close
                self.bot.send_message(call.message.chat.id, "?? ?????? ?????????? ??????????: " + str(self.special_id))
            elif call.data == 'del_admin':
                self.init_db()
                self.cursor.execute("""UPDATE Data SET Status = ? WHERE ID = ?""", (self.status_true, self.special_id))
                self.conn.commit()
                self.conn.close
                self.bot.send_message(call.message.chat.id, str(self.special_id)+ ", ???????????? ???? ??????????.")
            elif call.data == 'unban':
                self.init_db()
                self.cursor.execute("""UPDATE Data SET Status = ? WHERE ID = ?""", (self.status_true, self.special_id))
                self.conn.commit()
                self.conn.close
                self.bot.send_message(call.message.chat.id, str(self.special_id)+ ", ????????????????")
            elif call.data == 'line1':
                self.line = 1
            elif call.data == 'line2':
                self.line = 2
            elif call.data == 'line3':
                self.line = 3
            else:
                self.text = str(call)
                self.id = 0
                self.a = self.text.index("{'inline_keyboard': [")
                self.b = self.text.index("}}}")
                self.text = self.text[self.a+1:self.b]
                self.find = self.text.find(':')
                self.text = self.text[self.find+2:]
                self.text = self.text.replace("'", '').replace('[{', '').replace('}]', '').replace(':', ',').replace('text,', '').replace('callback_data,', '').replace(' ', '').replace('[', '').replace(']', '').replace(',', ' ')
                self.listt = self.text.split()
                for j in range(len(self.listt)):
                    if call.data == "user" + str(j):
                        for q in range(len(self.listt)):
                            if self.listt[q] == call.data:
                                self.id = int(self.listt[q-1])
                                self.special_id = self.id
                            else:
                                continue
                    else:
                        continue
                for calll in range(len(self.users)):
                    self.user_id = "user" + str(calll)
                    if call.data == self.user_id:
                        self.init_db()
                        self.cursor = self.conn.cursor()
                        self.get = self.cursor.execute('SELECT Status, Status FROM Data WHERE ID = ?', (self.id,))
                        self.get_1 = str(self.cursor.fetchall())
                        self.conn.commit()
                        self.conn.close
                        self.f = self.get_1.index('(')
                        self.c = self.get_1.index(',')
                        self.status= self.get_1[self.f+1:self.c]
                        
                        if self.status == "'admin'":
                            self.buttons = [[{'??????': 'ban'}, {'????????????': 'balance_user'}], [{'?????????????? ??????': 'game_history'}], [{'?????????????? ??????????????' : 'del_admin'}]]
                        elif self.status == "'banned'":
                            self.buttons = [[{'??????': 'ban'}, {'????????????': 'balance_user'}], [{'?????????????? ??????': 'game_history'}], [{'??????????????????' : 'unban'}]]
                        elif self.status == "'unbanned'":
                            self.buttons = [[{'??????': 'ban'}, {'????????????': 'balance_user'}], [{'?????????????? ??????': 'game_history'}], [{'???????????? ??????????????' : 'set_admin'}]]
                        self.keyboard = Keyboa(items=self.buttons)
                        self.bot.send_message(call.message.chat.id, text = "????????????????????????: " + self.user_id + '\n'
                                                                'ID: ' + str(self.id) ,reply_markup=self.keyboard())
                    else:
                        continue

                    
        self.bot.infinity_polling()



if __name__ == '__main__':  
    example = App()
