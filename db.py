import sqlite3
from libs_key import key_libs as lists


libs = dict(lists())

class btn_set:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def edit_key(self, name, var1, var2, var3):
        self.cursor.execute(f'UPDATE "key_settings" SET "key1"="{var1}" WHERE "btn_name"="{name}"')
        self.cursor.execute(f'UPDATE "key_settings" SET "key2"="{var2}" WHERE "btn_name"="{name}"')
        self.cursor.execute(f'UPDATE "key_settings" SET "key3"="{var3}" WHERE "btn_name"="{name}"')
        return self.conn.commit()

    def check_key_db(self, num, ordinal):
        name = eval('"BTN_PIN_{}"'.format(num))
        var = eval('"key{}"'.format(ordinal))
        re = self.cursor.execute(f'SELECT {var} FROM key_settings WHERE btn_name = "{name}"').fetchone()[0]
        inv_d = {value: key for key, value in libs.items()}
        return inv_d[re]

    def key_commands(self, pins):
        lb = self.cursor.execute(f'SELECT key1, key2, key3 FROM key_settings WHERE btn_name = "BTN_PIN_{pins}"').fetchone()
        return lb

    def save_colors_db(self, pins, color):
        name = eval('"BTN_PIN_{}"'.format(pins))
        self.cursor.execute(f'UPDATE "key_settings" SET "color_click"="{color}" WHERE "btn_name"="{name}"')
        return self.conn.commit()

    def check_colors(self, pins):
        name = eval('"BTN_PIN_{}"'.format(pins))
        re = self.cursor.execute(f'SELECT color_click FROM key_settings WHERE btn_name = "{name}"').fetchone()[0]
        return re

    def close(self):
        self.connection.close()
