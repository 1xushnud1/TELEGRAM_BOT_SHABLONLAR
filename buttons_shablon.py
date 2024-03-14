from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

Buttonlar = [                                            # noqa
    [KeyboardButton(text=""), KeyboardButton(text="")],  # <
    [KeyboardButton(text=""), KeyboardButton(text="")],  # <----- Bu yerga asosiy buttonlarni nomini kiritasiz # noqa
    [KeyboardButton(text=""), KeyboardButton(text="")]   # <
]
Menu = ReplyKeyboardMarkup(keyboard=Buttonlar, resize_keyboard=True) # noqa

Birinchi_Button = [ # noqa                                     # Bu yerga teppadagi asosiy buttonlardan birinchisiga kiritadigan buttonlar #noqa
    [KeyboardButton(text=""), KeyboardButton(text="")],  # noqa
    [KeyboardButton(text=""), KeyboardButton(text="")],  # noqa
            [KeyboardButton(text="Back 🔙")]  # noqa # Bu orqaga qaytish buttoni

]
Birinchi_Button_Nomi = ReplyKeyboardMarkup(keyboard=Birinchi_Button, resize_keyboard=True) # noqa

Ikkinchi_Button = [ # noqa                                     # Bu yerga teppadagi asosiy buttonlardan ikkinchisiga kiritadigan buttonlar #noqa
    [KeyboardButton(text=""), KeyboardButton(text="")],  # noqa
    [KeyboardButton(text=""), KeyboardButton(text="")],  # noqa
            [KeyboardButton(text="Back 🔙")]  # noqa # Bu orqaga qaytish buttoni

]
Ikkinchi_Button_Nomi = ReplyKeyboardMarkup(keyboard=Ikkinchi_Button, resize_keyboard=True) # noqa

Uchinchi_Button = [ # noqa                                     # Bu yerga teppadagi asosiy buttonlardan uchinchisiga kiritadigan buttonlar #noqa
    [KeyboardButton(text=""), KeyboardButton(text="")],  # noqa
    [KeyboardButton(text=""), KeyboardButton(text="")],  # noqa
            [KeyboardButton(text="Back 🔙")]  # noqa # Bu orqaga qaytish buttoni

]
Uchinchi_Button_Nomi = ReplyKeyboardMarkup(keyboard=Uchinchi_Button, resize_keyboard=True) # noqa

Turtinchi_Button = [ # noqa                                     # Bu yerga teppadagi asosiy buttonlardan tortinchisiga kiritadigan buttonlar #noqa
    [KeyboardButton(text=""), KeyboardButton(text="")],  # noqa
    [KeyboardButton(text=""), KeyboardButton(text="")],  # noqa
            [KeyboardButton(text="Back 🔙")]  # noqa # Bu orqaga qaytish buttoni

]
Turtinchi_Button_Nomi = ReplyKeyboardMarkup(keyboard=Turtinchi_Button, resize_keyboard=True) # noqa

Beshinchi_Button = [ # noqa                                     # Bu yerga teppadagi asosiy buttonlardan beshinchisiga kiritadigan buttonlar #noqa
    [KeyboardButton(text=""), KeyboardButton(text="")],  # noqa
    [KeyboardButton(text=""), KeyboardButton(text="")],  # noqa
            [KeyboardButton(text="Back 🔙")]  # noqa # Bu orqaga qaytish buttoni

]
Beshinchi_Button_Nomi = ReplyKeyboardMarkup(keyboard=Beshinchi_Button, resize_keyboard=True) # noqa

Oltinchi_Button = [ # noqa                                     # Bu yerga teppadagi asosiy buttonlardan oltinchisiga kiritadigan buttonlar #noqa
    [KeyboardButton(text=""), KeyboardButton(text="")],  # noqa
    [KeyboardButton(text=""), KeyboardButton(text="")],  # noqa
            [KeyboardButton(text="Back 🔙")]  # noqa # Bu orqaga qaytish buttoni

]
Oltinchi_Button_Nomi = ReplyKeyboardMarkup(keyboard=Oltinchi_Button, resize_keyboard=True) # noqa
