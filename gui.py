import random
import tkinter as tk
from tkinter.ttk import *
from tkinter import Canvas, font
from typing import Text
from PIL import Image, ImageTk
import time

#Modules
import infos
import cards

def initialize():
    dict = {}
    players = ["Player", "CPU"]
    attrib = ["hp", "dmg"]
    attrib_val = [15, 3]

    for player in players:
        dict[player] = {attrib[j]: attrib_val[j] for j in range(len(attrib))}
        dict[player]["hand"] = []
        dict[player]["status"] = []

    dict["Player"]["pwr"] = {
        "shocked": 0,
        "rage": 0,
        "thorns": 0,
    }
    dict["CPU"]["pwr"] = {
        "shocked": 0,
        "burned": 0,
        "trapped": False
    }
    dict["turn"] = 0,
    dict["wins"] = 0
    dict["enemies"] = list(range(4))
    return dict

def reset_game_dict():
    players = ["Player", "CPU"]
    for player in players:
        game_dict[player]["dmg"] = 3
        game_dict[player]["hand"] = []
        game_dict[player]["status"] = []

    game_dict["Player"]["pwr"] = {
        "shocked": 0,
        "rage": 0,
        "thorns": 0,
    }
    game_dict["CPU"]["pwr"] = {
        "shocked": 0,
        "burned": 0,
        "trapped": False
    }

def start_window():
    window = tk.Tk()
    window.title("Castle of Cards")
    winWidth = window.winfo_screenwidth()
    winwHeight = window.winfo_screenheight()
    window.configure(width=winWidth, height=winwHeight)
    window.attributes("-fullscreen", True)

    global game_dict
    game_dict = initialize()

    bg = tk.Canvas(window, bg="#658ecf", width=winWidth, height=winwHeight, highlightthickness=0)
    bg.pack()

    #Game Logo
    img = Image.open("img/pixel_art/logo.png")
    resize_img = img.resize((800, 800))
    img = ImageTk.PhotoImage(resize_img)
    logo = bg.create_image(winWidth/2, winwHeight/3, image=img)

    #Escape Key
    esc_icon = Image.open("img/escape_key.png")
    resize_icon = esc_icon.resize((30, 30))
    esc_icon = ImageTk.PhotoImage(resize_icon)

    frame_buttons = tk.Frame(bg, bg="#658ecf")
    frame_buttons.place(relx=0.1, rely=0.65, relwidth=0.8, relheight=0.45)

    button_options = [
        {"text":"START", "font":("Gotham Black", 15), "bg":"Grey", "width":20, "padx":10, "pady":10, "bd": 0, "command":lambda:choose_character_window(bg, winWidth, winwHeight)},
        {"text":"HOW TO PLAY", "font":("Gotham Black", 15), "bg":"Grey", "width":20, "padx":10, "pady":10, "bd": 0, "command":lambda:instructions(window, esc_icon)},
        {"text":"QUIT", "font":("Gotham Black", 15), "bg":"Red", "width":20, "padx":10, "pady":10, "bd": 0, "command":quit}
    ]
    for i, options in enumerate(button_options):
        tk.Button(frame_buttons, **options).grid(row=i, column=0, pady=5)
        frame_buttons.grid_columnconfigure(0, weight=1)

    window.mainloop()

def choose_character_window(prev_window, screenWidth, screenHeight):
    bg = tk.Canvas(prev_window, width=screenWidth, height=screenHeight, highlightthickness=0)
    bg.pack(fill="both", expand=1)

    frame_placard = tk.Frame(bg, width=screenWidth, height=screenHeight/10, bg="#007DA1")
    frame_placard.place(relx=0, rely=0)
    tk.Label(frame_placard, text="PLAYER SELECT", font=("Gotham Black", 70), fg="white", bg="#007DA1").place(relx=0.5, rely=0.45, anchor="center")

    global start_bg
    start_bg = tk.PhotoImage(file="img/start_bg.png")

    char_bg = bg.create_image(screenWidth/2, screenHeight/2, image=start_bg, anchor="nw")
    bg.move(char_bg, -screenWidth/2, -screenHeight/2)

    rectangle = bg.create_rectangle(275, 600, 1010, 1100, outline="", width=5)
    bg.move(rectangle, 750, -350)

    char_name = bg.create_text(1055, 340, text="", font=("Gotham Black", 70), fill="#F9F871", anchor="nw")
    char_description = bg.create_text(1055, 445, text="", font=("Gotham", 20), fill="white", anchor="nw")
    char_ability_text = bg.create_text(1055, 520, text="", font=("Galyon Bold", 20), fill="white", anchor="nw")
    ability_icon_width = 50
    ability_icon_height = 50
    char_ability_icon = bg.create_image(ability_icon_width/2, ability_icon_height/2, anchor="nw")
    bg.move(char_ability_icon, 1050, 540)
    char_ability = bg.create_text(1135, 565, text="", font=("Gotham Black", 30), fill="white", anchor="nw")

    char_img_width = 1400
    char_img_height = 1400
    char_img = bg.create_image(char_img_width/2, char_img_height/2, anchor="nw")
    bg.move(char_img, -700, -650)

    frame_characters = tk.Frame(bg, bg="#A2ACBD")
    frame_characters.place(relx=0.5, rely=0.85, relwidth=0.2715, relheight=0.0975, anchor="center")

    #IMAGES ON BUTTONS
    #Berserker Icon
    global berserker_icn
    berserker_icn = Image.open("img/berserker_icon.png")
    resize_berserker_icn = berserker_icn.resize((95, 95))
    berserker_icn = ImageTk.PhotoImage(resize_berserker_icn)

    #Ranger Icon
    global ranger_icn
    ranger_icn = Image.open("img/ranger_icon.png")
    resize_ranger_icn = ranger_icn.resize((95, 95))
    ranger_icn = ImageTk.PhotoImage(resize_ranger_icn)
    
    #Mage Icon
    global mage_icn
    mage_icn = Image.open("img/mage_icon.png")
    resize_mage_icn = mage_icn.resize((95, 95))
    mage_icn = ImageTk.PhotoImage(resize_mage_icn)

    #Assassin Icon
    global asssasin_icn
    asssasin_icn = Image.open("img/assassin_icon.png")
    resize_assassin_icn = asssasin_icn.resize((95, 95))
    asssasin_icn = ImageTk.PhotoImage(resize_assassin_icn)

    #Tank Icon
    global tank_icn
    tank_icn = Image.open("img/tank_icon.png")
    resize_tank_icn = tank_icn.resize((95, 95))
    tank_icn = ImageTk.PhotoImage(resize_tank_icn)

    commands = {
        0: lambda:showCharacter1(bg, char_bg, char_img, char_img_width, char_img_height, rectangle, char_name, char_description, char_ability_text, char_ability_icon, ability_icon_width, ability_icon_width, char_ability, lockin_bt),
        1: lambda:showCharacter2(bg, char_bg, char_img, char_img_width, char_img_height, rectangle, char_name, char_description, char_ability_text, char_ability_icon, ability_icon_width, ability_icon_width, char_ability, lockin_bt),
        2: lambda:showCharacter3(bg, char_bg, char_img, char_img_width, char_img_height, rectangle, char_name, char_description, char_ability_text, char_ability_icon, ability_icon_width, ability_icon_width, char_ability, lockin_bt),
        3: lambda:showCharacter4(bg, char_bg, char_img, char_img_width, char_img_height, rectangle, char_name, char_description, char_ability_text, char_ability_icon, ability_icon_width, ability_icon_width, char_ability, lockin_bt),
        4: lambda:showCharacter5(bg, char_bg, char_img, char_img_width, char_img_height, rectangle, char_name, char_description, char_ability_text, char_ability_icon, ability_icon_width, ability_icon_width, char_ability, lockin_bt),
    }
    
    button_options = [
        {
            "width": 90,
            "height": 90,
            "image": character,
            "bd": 2,
            "bg": "#A2ACBD",
            "anchor": "center",
            "command": commands[i]
        }
        for i, character in enumerate([berserker_icn, ranger_icn, mage_icn, asssasin_icn, tank_icn])
    ]
    
    for i, options in enumerate(button_options):
        button = tk.Button(frame_characters, **options)
        button.grid(row=0, column=i, padx=3.5, pady=5)

    lockin_bt = tk.Button(bg, command=lambda:play(bg, screenWidth, screenHeight, char_name), text="PLAY", font=("Gotham Black", 20), padx=20, pady=10)

def configItems(bg, char_bg, char_bg_img, char_img, char_image, rectangle, char_name, char_name_txt, char_description, char_description_txt, char_ability_text, char_ability_icon, char_ability_icon_img, char_ability, char_ability_txt):
    bg.itemconfig(char_bg, image=char_bg_img)
    bg.itemconfig(char_img, image=char_image)
    bg.itemconfig(rectangle, outline="white")
    bg.itemconfig(char_name, text=char_name_txt)
    bg.itemconfig(char_description, text=char_description_txt)
    bg.itemconfig(char_ability_text, text="UNIQUE CARD:")
    bg.itemconfig(char_ability_icon, image=char_ability_icon_img)
    bg.itemconfig(char_ability, text=char_ability_txt)

def showCharacter1(bg, char_bg, char_img, char_img_width, char_img_height, rectangle, char_name, char_description, char_ability_text, char_ability_icon, icon_width, icon_height, char_ability, lockin_bt):
    global bg1
    bg1 = tk.PhotoImage(file="img/berserker_bg.png")
    
    global char1
    char1 = Image.open("img/berserker_main.png")
    resize_char1 = char1.resize((char_img_width, char_img_height))
    char1 = ImageTk.PhotoImage(resize_char1)

    global icon1
    icon1 = Image.open("img/rage_icon.png")
    resize_icon1 = icon1.resize((icon_width, icon_height))
    icon1 = ImageTk.PhotoImage(resize_icon1)

    lockin_bt.place(relx=0.5, rely=0.75, anchor="center")

    char_name_txt = infos.berserker()["name"].upper()
    char_description_txt = infos.berserker()["description"].capitalize()
    char_ability_txt = infos.berserker()["unique_card"]
    configItems(bg, char_bg, bg1, char_img, char1, rectangle, char_name, char_name_txt, char_description, char_description_txt, char_ability_text, char_ability_icon, icon1, char_ability, char_ability_txt)

def showCharacter2(bg, char_bg, char_img, char_img_width, char_img_height, rectangle, char_name, char_description, char_ability_text, char_ability_icon, icon_width, icon_height, char_ability, lockin_bt):
    global bg2
    bg2 = tk.PhotoImage(file="img/ranger_bg.png")
    
    global char2
    char2 = Image.open("img/ranger_main.png")
    resize_char2 = char2.resize((char_img_width, char_img_height))
    char2 = ImageTk.PhotoImage(resize_char2)

    global icon2
    icon2 = Image.open("img/trap_icon.png")
    resize_icon2 = icon2.resize((icon_width, icon_height))
    icon2 = ImageTk.PhotoImage(resize_icon2)

    lockin_bt.place(relx=0.5, rely=0.75, anchor="center")

    char_name_txt = infos.ranger()["name"].upper()
    char_description_txt = infos.ranger()["description"].capitalize()
    char_ability_txt = infos.ranger()["unique_card"]
    configItems(bg, char_bg, bg2, char_img, char2, rectangle, char_name, char_name_txt, char_description, char_description_txt, char_ability_text, char_ability_icon, icon2, char_ability, char_ability_txt)

def showCharacter3(bg, char_bg, char_img, char_img_width, char_img_height, rectangle, char_name, char_description, char_ability_text, char_ability_icon, icon_width, icon_height, char_ability, lockin_bt):
    global bg3
    bg3 = tk.PhotoImage(file="img/mage_bg.png")

    global char3
    char3 = Image.open("img/mage_main.png")
    resize_char3 = char3.resize((char_img_width, char_img_height))
    char3 = ImageTk.PhotoImage(resize_char3)

    global icon3
    icon3 = Image.open("img/burn_icon.png")
    resize_icon3 = icon3.resize((icon_width, icon_height))
    icon3 = ImageTk.PhotoImage(resize_icon3)

    lockin_bt.place(relx=0.5, rely=0.75, anchor="center")

    char_name_txt = infos.mage()["name"].upper()
    char_description_txt = infos.mage()["description"].capitalize()
    char_ability_txt = infos.mage()["unique_card"]
    configItems(bg, char_bg, bg3, char_img, char3, rectangle, char_name, char_name_txt, char_description, char_description_txt, char_ability_text, char_ability_icon, icon3, char_ability, char_ability_txt)

def showCharacter4(bg, char_bg, char_img, char_img_width, char_img_height, rectangle, char_name, char_description, char_ability_text, char_ability_icon, icon_width, icon_height, char_ability, lockin_bt):
    global bg4
    bg4 = tk.PhotoImage(file="img/assassin_bg.png")

    global char4
    char4 = Image.open("img/assassin_main.png")
    resize_char4 = char4.resize((char_img_width, char_img_height))
    char4 = ImageTk.PhotoImage(resize_char4)

    global icon4
    icon4 = Image.open("img/cleave_icon.png")
    resize_icon4 = icon4.resize((icon_width, icon_height))
    icon4 = ImageTk.PhotoImage(resize_icon4)

    lockin_bt.place(relx=0.5, rely=0.75, anchor="center")

    char_name_txt = infos.assassin()["name"].upper()
    char_description_txt = infos.assassin()["description"].capitalize()
    char_ability_txt = infos.assassin()["unique_card"]
    configItems(bg, char_bg, bg4, char_img, char4, rectangle, char_name, char_name_txt, char_description, char_description_txt, char_ability_text, char_ability_icon, icon4, char_ability, char_ability_txt)

def showCharacter5(bg, char_bg, char_img, char_img_width, char_img_height, rectangle, char_name, char_description, char_ability_text, char_ability_icon, icon_width, icon_height, char_ability, lockin_bt):
    global bg5
    bg5 = tk.PhotoImage(file="img/tank_bg.png")
    
    global char5
    char5 = Image.open("img/tank_main.png")
    resize_char5 = char5.resize((char_img_width, char_img_height))
    char5 = ImageTk.PhotoImage(resize_char5)

    global icon5
    icon5 = Image.open("img/thorns_icon.png")
    resize_icon5 = icon5.resize((icon_width, icon_height))
    icon5 = ImageTk.PhotoImage(resize_icon5)

    lockin_bt.place(relx=0.5, rely=0.75, anchor="center")

    char_name_txt = infos.tank()["name"].upper()
    char_description_txt = infos.tank()["description"].capitalize()
    char_ability_txt = infos.tank()["unique_card"]
    configItems(bg, char_bg, bg5, char_img, char5, rectangle, char_name, char_name_txt, char_description, char_description_txt, char_ability_text, char_ability_icon, icon5, char_ability, char_ability_txt)

def play(prev_window, screenWidth, screenHeight, char_name):
    bg = tk.Canvas(prev_window, width=screenWidth, height=screenHeight, bg="#1e2224", highlightthickness=0)
    bg.pack()
    char_name = prev_window.itemcget(char_name, "text")

    global greeting_img
    greeting_img = Image.open("img/greetings.png")
    resize_grt_img = greeting_img.resize((1000, 1000))
    greeting_img = ImageTk.PhotoImage(resize_grt_img)

    grt_img = bg.create_image(400, 400, image=greeting_img, anchor="nw")
    bg.move(grt_img, -270, -300)
    greetings_txt = bg.create_text(100, 100, text="Welcome to Castle of Cards.\nThe Overlord has been\nexpecting you.\nHow long will you hold up?", font=("Gotham Black", 40), fill="white")
    bg.move(greetings_txt, 1300, 350)
    rectangle = bg.create_rectangle(275, 600, 1090, 1000, outline="white", width=5)
    bg.move(rectangle, 715, -350)

    wins = game_dict["wins"]
    tk.Button(bg, text="Continue", font=("Gotham Black", 20), padx=10, pady=10, command=lambda:floor(bg, screenWidth, screenHeight, char_name, wins)).place(relx=0.675, rely=0.65, anchor="nw")

def floor(prev_window, screenWidth, screenHeight, char_name, wins):
    bg = tk.Canvas(prev_window, width=screenWidth, height=screenHeight, bg="grey", highlightthickness=0)
    bg.pack()

    img_width_intro = 750
    img_height_intro = 750
    img_width_play = 500
    img_height_play = 500
    
    print(game_dict)

    if wins < 3:
        ran_enemy = random.choice(game_dict["enemies"])
        picked_enemy = generate_enemy(ran_enemy)
        game_dict["enemies"].remove(ran_enemy)
        game_dict["CPU"]["hp"] = 10
    else:
        picked_enemy = generate_enemy(4)
        game_dict["CPU"]["hp"] = 15

    reset_game_dict()               #Reset Stats from dictionary
    game_dict["turn"] = 0           #Reset turns

    global enemy_bg
    enemy_bg = tk.PhotoImage(file=picked_enemy["bg_location"])
    bg.create_image(screenWidth/2, screenHeight/2, image=enemy_bg)

    global enemy_intro
    enemy_intro = Image.open(picked_enemy["img_location"])
    resize_enemy_intro = enemy_intro.resize((img_width_intro, img_height_intro))
    enemy_intro = ImageTk.PhotoImage(resize_enemy_intro)

    entrance = bg.create_rectangle(-screenWidth, screenHeight/4, 0, (3/4)*screenHeight, fill="orange", outline="")
    enemy_intro_img = bg.create_image(-screenWidth+200, screenHeight/7, image=enemy_intro, anchor="nw")
    enemy_intro_txt = bg.create_text(-screenWidth+900, screenHeight/2.75, text="FLOOR " + str(wins+1) + ":\n" + picked_enemy["name"], font=("Gotham Black", 80), fill="white", anchor="nw")
    x_velocity = 40
    while bg.coords(entrance)[0] < 0:
        bg.move(entrance, x_velocity, 0)
        bg.move(enemy_intro_img, x_velocity, 0)
        bg.move(enemy_intro_txt, x_velocity, 0)
        bg.update()
        time.sleep(0.01)
    time.sleep(2.5)
    while bg.coords(entrance)[0] != screenWidth:
        bg.move(entrance, x_velocity, 0)
        bg.move(enemy_intro_img, x_velocity, 0)
        bg.move(enemy_intro_txt, x_velocity, 0)
        bg.update()
        time.sleep(0.01)

    global player
    player = Image.open(show_character_play(char_name.lower()))
    resize_player = player.resize((img_width_play, img_height_play))
    player = ImageTk.PhotoImage(resize_player)

    global enemy_play_img
    enemy_play_img = Image.open(picked_enemy["play_location"])
    resize_enemy_play_img = enemy_play_img.resize((img_width_play, img_height_play))
    enemy_play_img = ImageTk.PhotoImage(resize_enemy_play_img)

    player_play = bg.create_image(-400, 200, image=player, anchor="nw")
    enemy_play = bg.create_image(screenWidth-200, 200, image=enemy_play_img, anchor="nw")

    while bg.coords(player_play)[0] < 200 and bg.coords(enemy_play)[0] > 1020:
        bg.move(player_play, x_velocity, 0)
        bg.move(enemy_play, -x_velocity, 0)
        bg.update()
        time.sleep(0.01)

    game_dict["Player"]["hand"] = cards.get_hand(char_name.lower())
    game_dict["CPU"]["hand"] = cards.enemy_get_cards(picked_enemy["name"].lower())

    show_player_health_bar(bg)
    show_enemy_health_bar(bg)
    show_player_dmg_bar(bg)
    show_enemy_dmg_bar(bg)

    show_cards(bg, char_name, picked_enemy)

    """
    if floor_ctr != 3:
        floor_ctr += 1
        floor(bg, screenWidth, screenHeight, char_name, floor_ctr)
    else:
        print("yey")
    """

def card_img_map():
    card_width = 200
    card_height = 300
    
    global attack_card_img
    attack_card_img = Image.open("img/attack_card.png")
    resize_attack_card_img = attack_card_img.resize((card_width, card_height))
    attack_card_img = ImageTk.PhotoImage(resize_attack_card_img)

    global block_card_img
    block_card_img = Image.open("img/block_card.png")
    resize_block_card_img = block_card_img.resize((card_width, card_height))
    block_card_img = ImageTk.PhotoImage(resize_block_card_img)

    global boost_card_img
    boost_card_img = Image.open("img/boost_card.png")
    resize_boost_card_img = boost_card_img.resize((card_width, card_height))
    boost_card_img = ImageTk.PhotoImage(resize_boost_card_img)
    
    global burn_card_img
    burn_card_img = Image.open("img/burn_card.png")
    resize_burn_card_img = burn_card_img.resize((card_width, card_height))
    burn_card_img = ImageTk.PhotoImage(resize_burn_card_img)
    
    global cleave_card_img
    cleave_card_img = Image.open("img/cleave_card.png")
    resize_cleave_card_img = cleave_card_img.resize((card_width, card_height))
    cleave_card_img = ImageTk.PhotoImage(resize_cleave_card_img)

    global rage_card_img
    rage_card_img = Image.open("img/rage_card.png")
    resize_rage_card_img = rage_card_img.resize((card_width, card_height))
    rage_card_img = ImageTk.PhotoImage(resize_rage_card_img)

    global shock_card_img
    shock_card_img = Image.open("img/shock_card.png")
    resize_shock_card_img = shock_card_img.resize((card_width, card_height))
    shock_card_img = ImageTk.PhotoImage(resize_shock_card_img)

    global thorns_card_img
    thorns_card_img = Image.open("img/thorns_card.png")
    resize_thorns_card = thorns_card_img.resize((card_width, card_height))
    thorns_card_img = ImageTk.PhotoImage(resize_thorns_card)

    global trap_card_img
    trap_card_img = Image.open("img/trap_card.png")
    resize_trap_card_img = trap_card_img.resize((card_width, card_height))
    trap_card_img = ImageTk.PhotoImage(resize_trap_card_img)

    card_img_dict = {
        "attack": {
            "variable": attack_card_img,
        },
        "block": {
            "variable": block_card_img
        },
        "boost": {
            "variable": boost_card_img
        },
        "burn": {
            "variable": burn_card_img
        },
        "cleave": {
            "variable": cleave_card_img
        },
        "rage": {
            "variable": rage_card_img
        },
        "shock": {
            "variable": shock_card_img
        },
        "thorns": {
            "variable": thorns_card_img
        },
        "trap": {
            "variable": trap_card_img
        }
    }
    return card_img_dict

def show_cards(bg, char_name, enemy):
    frame = tk.Frame(bg, bg=enemy["frame_color"])
    frame.place(relx=0.5, rely=0.80, anchor="center")

    card_dict = card_img_map()

    card_imgs = [card_dict[i] for i in game_dict["Player"]["hand"]]
    
    commands = {
        0: lambda:clickCard(bg, frame, char_name, enemy, game_dict["Player"]["hand"][0], card_dict[game_dict["Player"]["hand"][0]]["variable"]),
        1: lambda:clickCard(bg, frame, char_name, enemy, game_dict["Player"]["hand"][1], card_dict[game_dict["Player"]["hand"][1]]["variable"]),
        2: lambda:clickCard(bg, frame, char_name, enemy, game_dict["Player"]["hand"][2], card_dict[game_dict["Player"]["hand"][2]]["variable"]),
        3: lambda:clickCard(bg, frame, char_name, enemy, game_dict["Player"]["hand"][3], card_dict[game_dict["Player"]["hand"][3]]["variable"]),
        4: lambda:clickCard(bg, frame, char_name, enemy, game_dict["Player"]["hand"][4], card_dict[game_dict["Player"]["hand"][4]]["variable"]),
        5: lambda:clickCard(bg, frame, char_name, enemy, game_dict["Player"]["hand"][5], card_dict[game_dict["Player"]["hand"][5]]["variable"])
    }

    button_options = [
        {
            "width": 200,
            "height": 300,
            "image": card["variable"],
            "bd": 2,
            "anchor": "center",
            "command": commands[i]
        }
        for i, card in enumerate(card_imgs)
    ]

    for i, options in enumerate(button_options):
        button = tk.Button(frame, **options)
        button.grid(row=0, column=i, padx=10, pady=5)

def clickCard(prev_window, frame, player, enemy, player_card, player_card_img):
    screenWidth = prev_window.winfo_width()
    screenHeight = prev_window.winfo_height()

    bg = tk.Canvas(prev_window, width=screenWidth, height=screenHeight, bg="grey", highlightthickness=0)
    bg.pack()

    global combat_bg
    combat_bg = tk.PhotoImage(file=enemy["bg_location"])
    bg.create_image(screenWidth/2, screenHeight/2, image=combat_bg)
    
    img_width_combat = 1200 
    img_height_combat = 1200

    global player_combat_img
    player_combat_img = Image.open(show_character_play(player.lower()))
    resize_player_combat_img = player_combat_img.resize((img_width_combat, img_height_combat))
    player_combat_img = ImageTk.PhotoImage(resize_player_combat_img)

    global enemy_combat_img
    enemy_combat_img = Image.open(enemy["play_location"])
    resize_enemy_combat_img = enemy_combat_img.resize((img_width_combat, img_height_combat))
    enemy_combat_img = ImageTk.PhotoImage(resize_enemy_combat_img)
    
    enemy_card = game_dict["CPU"]["hand"][0]
    card_img_dict = card_img_map()
    enemy_card_img = card_img_dict[game_dict["CPU"]["hand"][0]]["variable"]

    player_combat = bg.create_image(-300, -50, image=player_combat_img, anchor="nw")
    enemy_combat = bg.create_image(1050, -50, image=enemy_combat_img, anchor="nw")
    
    global continue_button
    continue_button = Image.open("img/continue_button.png")
    resize_continue_button = continue_button.resize((100, 100))

    dialogue_canvas = tk.Canvas(bg, width=screenWidth, height=screenHeight/3, bg=enemy["box_color"], highlightthickness=0)
    dialogue_canvas.place(relx=0.5, rely=0.9, anchor="center")
    rectangle = dialogue_canvas.create_rectangle(20, 20, screenWidth - 170, 270, outline="white", width=5)
    
    continue_button = ImageTk.PhotoImage(resize_continue_button)

    dialogue_text = dialogue_canvas.create_text(40, 40, font=("Gotham Black", 50), fill="white", anchor="nw", text="")

    game_dict["turn"] += 1

    player_dict = game_dict["Player"]
    cpu_dict = game_dict["CPU"]

    updated_texts = []

    #Player is stunned
    if player_card == "null":
        player_card = "stun"
        dialogue_canvas.itemconfig(dialogue_text, text="You are stunned.")
        updated_texts.extend([enemy["name"].title() + " used " + enemy_card.title()])
        button = tk.Button(bg, image=continue_button, bg=enemy["box_color"], bd=0, command=lambda:change_text(updated_texts, dialogue_canvas, dialogue_text, [bg], prev_window, player, enemy)).place(relx=0.95, rely=0.85, anchor="center")
    else:
        dialogue_canvas.itemconfig(dialogue_text, text="Player used " + player_card.title())
        bg.create_image(660, screenHeight/3, image=player_card_img, anchor="nw")
        game_dict["Player"]["hand"].remove(player_card)
        button = tk.Button(bg, image=continue_button, bg=enemy["box_color"], bd=0, command=lambda:change_text(updated_texts, dialogue_canvas, dialogue_text, [bg, frame], prev_window, player, enemy)).place(relx=0.95, rely=0.85, anchor="center")
    
    #CPU is stunned
    if cpu_dict["pwr"]["shocked"] > 0:
        enemy_card = "stun"
        dialogue_canvas.itemconfig(dialogue_text, text=enemy["name"].title() + " is stunned.")
        updated_texts.extend(["Player used " + player_card.title()])
    elif cpu_dict["pwr"]["trapped"] == True:
        enemy_card = "trapped"
        dialogue_canvas.itemconfig(dialogue_text, text=enemy["name"].title() + " is trapped and unable to move.")
        updated_texts.extend(["Player used " + player_card.title()])
    else:
         bg.create_image(1060, screenHeight/3, image=enemy_card_img, anchor="nw")
         game_dict["CPU"]["hand"].remove(enemy_card)
         updated_texts.extend([enemy["name"].title() + " used " + enemy_card.title()])

    #Both are stunned

    #Card Interactions
    '''Card interactions are arranged based on priority, it's not random.'''
    #Player uses Attack card interactions
    if player_card == "attack":
        #CPU reflects DMG with block
        if enemy_card == "block" and player_dict["pwr"]["rage"] <= 0:
            updated_texts.extend(["Damage reflected! You receive " + str(player_dict["dmg"]) + " DMG."])
            player_dict["hp"] -= player_dict["dmg"]
        
        #Player ignores block if ENRAGED
        elif enemy_card == "block" and player_dict["pwr"]["rage"] > 0:
            updated_texts.extend(["You ignore the " + enemy["name"].title() + "\b's block.\nYou deal " + str(player_dict["dmg"]) + " DMG.", "You restore " + str(player_dict["dmg"]) + " HP from your attack."])
            cpu_dict["hp"] -= player_dict["dmg"]
            player_dict["hp"] += player_dict["dmg"]//2

         #CPU reflects DMG with block, but Player also reflects DMG with thorns
        elif enemy_card == "block" and player_dict["pwr"]["thorns"] > 0:
            cpu_dict["hp"] -= cpu_dict["dmg"]//2
            player_dict["hp"] -= cpu_dict["dmg"]
            player_dict["dmg"] += cpu_dict["dmg"]//2
            updated_texts.extend([enemy["name"].title() + " deals " + str(cpu_dict["dmg"]) + " DMG.\nYou reflect " + str(cpu_dict["dmg"]//2) + " DMG and heal " + str(cpu_dict["dmg"]//2) + " HP because of thorns."])
            
        #Player ignores slime passive when ENRAGED
        elif player_dict["pwr"]["rage"] > 0 and enemy["name"].lower() == "slime":
            updated_texts.extend(["You ignore the Slime's passive and deal " + str(player_dict["dmg"]) + " DMG.", "You restore " + str(player_dict["dmg"]//2) + " HP from your attack."])
            cpu_dict["hp"] -= player_dict["dmg"]
            player_dict["hp"] += player_dict["dmg"]//2

        #Player attacks restore health when ENRAGED
        elif player_dict["pwr"]["rage"] > 0:
            updated_texts.extend(["You deal " + str(player_dict["dmg"]) + " DMG.", "You restore " + str(player_dict["dmg"]//2) + " HP from your attack."])
            cpu_dict["hp"] -= player_dict["dmg"]
            player_dict["hp"] += player_dict["dmg"]//2

        #Player only deals half DMG if enemy type is a slime
        elif enemy["name"] == "slime":
            updated_texts.extend(["You only deal " + str(player_dict["dmg"]//2) + " DMG because of the Slime's passive."])
            cpu_dict["hp"] -= player_dict["dmg"]//2

        #Else, deals player deals DMG
        else:
            updated_texts.extend(["You deal " + str(player_dict["dmg"]) + " DMG."])
            cpu_dict["hp"] -= player_dict["dmg"]
    
    #Player uses Block card interactions
    elif player_card == "block":
        #Player reflects Attack card DMG with block
        if enemy_card == "attack":
            print("Line 586")
            updated_texts.extend(["Damage reflected! The " + enemy["name"].title() + " receives " + str(cpu_dict["dmg"]) + " DMG."])
            cpu_dict["hp"] -= cpu_dict["dmg"]

        #Player reflects Shock card effect with block
        elif enemy_card == "shock":
            print("Line 593")
            updated_texts.extend(["Shock reflected! The " + enemy["name"].title() + " will be stunned next turn."])
            cpu_dict["pwr"]["shocked"] += 1
            cpu_dict["status"].append("stun")               #appends stun to list(cpu_status)

        #Else, nothing happens
        else:
            pass
    
    #Boost cards don't have special interactions
    elif player_card == "boost":
        print("Line 601")
        updated_texts.extend(["Your DMG is now increased to " + str(player_dict["dmg"] + 1)])
        player_dict["dmg"] += 1

    #Player uses Shock card interactions
    elif player_card == "shock":
        #CPU reflects Shock with Block
        if enemy_card == "block" and player_dict["pwr"]["rage"] <= 0:
            print("Line 609")
            updated_texts.extend(["Shock reflected! You will be stunned next turn."])
            player_dict["pwr"]["shocked"] += 1
            player_dict["status"].append("stun")        #appends stun to list(user_status)

        #Player ignores Shock while ENRAGED
        elif enemy_card == "block" and player_dict["pwr"]["rage"] > 0:
            print("Line 616")
            updated_texts.extend(["You ignore the " + enemy["name"].title() + "\b's block.\n" + enemy["name"].title() + " will be stunned\nnext turn."])
            cpu_dict["pwr"]["shocked"] += 1

        #Else, CPU is stunned next turn
        else:
            print("Line 622")
            updated_texts.extend([enemy["name"].title() + " will be stunned next turn."])
            cpu_dict["pwr"]["shocked"] += 1
            cpu_dict["status"].append("stun")           #appends stun to list(cpu_status)
    
    #Player uses Rage card
    elif player_card == "rage":
        print("Line 629")
        updated_texts.extend(["You are now ENRAGED! You ignore stun and \nshock cards and heal half of the damage you\ndeal!"])
        player_dict["pwr"]["rage"] += 4
    
    #Player uses Burn card, inflicts CPU with Burn status
    elif player_card == "burn":
        print("Line 635")
        updated_texts.extend([enemy["name"] + " has been inflicted with burn!"])
        cpu_dict["pwr"]["burned"] += 4

    #Player uses Trap card interaction
    elif player_card == "trap":
        #CPU blocks Trap with Block
        if enemy_card == "block":
            print("Line 643")
            updated_texts.extend([enemy["name"].title() + " deflected the trap!"])
        else:
            cpu_dict["status"].append("trap")           #appends trap to list(cpu_status)
            print("Line 647")
            updated_texts.extend([enemy["name"].title() + "\b's movements have been hindered.\nThe " + enemy["name"].title() + " will be unable to move next turn!"])
            cpu_dict["pwr"]["trapped"] = True  

    #Player uses Cleave card interactions
    elif player_card == "cleave":
        #CPU reflects Cleave card DMG with block
        if enemy_card == "block":
            print("Line 655")
            updated_texts.extend(["Special card reflected! You receive " + str(2*player_dict["dmg"]//2) + " DMG."])
            player_dict["hp"] -= 2*player_dict["dmg"]
        
        #Cleave only deals half DMG if enemy is a slime
        elif enemy["name"].lower() == "slime":
            print("Line 664")
            updated_texts.extend(["Double strike! But you only deal " + str(2*player_dict["dmg"]//2) + " DMG because of the Slime's passive."])
            cpu_dict["hp"] -= 2*player_dict["dmg"]//2

        #Else, Cleave deals double DMG value
        else:
            print("Line 670")
            updated_texts.extend(["Double strike! You deal " + str(2*player_dict["dmg"]) + " DMG."])
            cpu_dict["hp"] -= 2*player_dict["dmg"]

    #Player uses Thorns card
    elif player_card == "thorns":
        player_dict["status"].append("thorns")          #appends thorns to list(user_status)
        print("Line 677")
        updated_texts.extend(["Activated thorns! You now reflect DMG and heal when attacked."])
        player_dict["pwr"]["thorns"] += 2

    #Player is stunned
    elif player_card == "stun":
        player_dict["pwr"]["shocked"] -= 1              #reduces/removes stun duration
        if player_dict["pwr"]["shocked"] == 0:
            remove_status("stun", player_dict["status"])    #removes stun status from terminal print
        else:
            pass
    else:
        pass

    #CPU uses Attack card interactions
    if enemy_card == "attack":
        #Player reflects DMG with block, pass because interaction was already declared earlier
        if player_card == "block":
            pass
        
        #CPU takes reflected DMG if Player is in Thorns. Also, heals player of reflected DMG
        elif player_dict["pwr"]["thorns"] > 0:
            cpu_dict["hp"] -= cpu_dict["dmg"]//2
            player_dict["hp"] -= cpu_dict["dmg"]
            player_dict["hp"] += cpu_dict["dmg"]//2
            
            #Thorns negates overlord lifesteal passive
            if enemy == "overlord":
                print("Line 705")
                updated_texts.extend([enemy["name"].title() + " couldn't restore HP because of thorns."])
            updated_texts.extend([enemy["name"].title() + " deals " + str(cpu_dict["dmg"]) + " DMG.", "You reflect " + str(cpu_dict["dmg"]//2) + " DMG and heal " + str(cpu_dict["dmg"]//2) + " HP because of thorns."])
            player_dict["pwr"]["thorns"] -= 1           #reduces thorns duration

            if player_dict["pwr"]["thorns"] > 0:
                print("Line 711")
                updated_texts.extend(["You will continue to reflect DMG when attacked for the next " + str(player_dict["pwr"]["thorns"]) + " attack/s."])
            elif player_dict["pwr"]["thorns"] <= 0:
                remove_status("thorns", player_dict["status"])      #removes thorns status from terminal print
                print("Line 715")
                updated_texts.extend(["Thorns are now deactivated."])
            else:
                pass
        
        #CPU heals from attacks if enemy type is Overlord
        elif enemy == "overlord":
            print("Line 722")
            updated_texts.extend([enemy["name1"].title() + " deals " + str(cpu_dict["dmg"]) + " DMG and restores " + str(cpu_dict["dmg"]//2) + " HP."])
            player_dict["hp"] -= cpu_dict["dmg"]
            cpu_dict["hp"] += cpu_dict["dmg"]//2

        #Else, CPU deals DMG
        else:
            print("Line 728")
            updated_texts.extend([enemy["name"].title() + " deals " + str(cpu_dict["dmg"]) + " DMG."])
            player_dict["hp"] -= cpu_dict["dmg"]

    #CPU uses Block card, pass because interactions have already been declared earlier
    elif enemy_card == "block":
        pass

    #CPU uses Boost card
    elif enemy_card == "boost":
        print("Line 739")
        updated_texts.extend([enemy["name"].title() + " DMG is now increased to " + str(cpu_dict["dmg"] + 1)])
        cpu_dict["dmg"] += 1

    #CPU uses Shock card interactions
    elif enemy_card == "shock":
        #Shock card is reflected with block, pass because interaction has already been declared earlier
        if player_card == "block":
            pass
        
        #Player ignores Shock card while ENRAGED
        elif player_dict["pwr"]["rage"] > 0:
            print("Line 751")
            updated_texts.extend(["You ignore the " + enemy["name"].title() + " \b's shock"])
        
        #Else, CPU stuns the Player next turn
        else:
            print("Line 756")
            updated_texts.extend(["You will be stunned next turn"])
            player_dict["pwr"]["shocked"] += 1
            player_dict["status"].append("stun")        #appends stun to list(user_status)

    #CPU is trapped interactions
    elif enemy_card == "trapped":
        updated_texts.extend([enemy["name"].title() + " is trapped and unabled to move."])
        #Trap is removed if Player attacks
        if player_card == "attack":
            remove_status("trap", cpu_dict["status"])
            print("Line 766")
            updated_texts.extend(["The " + enemy["name"].lower() + " \b's trap has been broken."])
            cpu_dict["pwr"]["trapped"] = False
            #if CPU is trapped & stunned, also removes stun status
            if cpu_dict["pwr"]["shocked"] > 0:
                cpu_dict["pwr"]["shocked"] = 0
                remove_status("stun", cpu_dict["status"])       #removes stun status from terminal print
            else:
                pass
        #Player uses Shock while CPU is trapped
        elif player_card == "shock":
            cpu_dict["pwr"]["shocked"] += 1
            cpu_dict["status"].append("stun")                   #appends stun to list(cpu_status)                  
        
        #CPU is trapped & stunned, removes stun while trap remains
        elif cpu_dict["pwr"]["shocked"] > 0:
            cpu_dict["status"].append("trap")                   #appends trap to list(cpu_status)
            print("Line 783")
            updated_texts.extend([enemy["name"].title() + " is still trapped."])
            cpu_dict["pwr"]["shocked"] -= 1                     #reduces/removes stun duration
            if cpu_dict["pwr"]["shocked"] == 0:
                remove_status("stun", cpu_dict["status"])       #removes stun status from terminal print
            else:
                pass
        
        #Else, CPU is still trapped
        else:
            print("Line 793")
            updated_texts.extend([enemy["name"].title() + " is still trapped."])
    
    #CPU is stunned, reduces/removes stun duration
    elif enemy_card == "stun":
        cpu_dict["pwr"]["shocked"] -= 1                         #Uses integer in case Player was stunned twice
        if cpu_dict["pwr"]["shocked"] == 0:
            remove_status("stun", cpu_dict["status"])           #removes stun status from terminal print         
        else:
            pass
    else:
        pass
    
    #Player is enraged
    if player_dict["pwr"]["rage"] > 0:
        player_dict["pwr"]["rage"] -= 1                         #reduces rage duration
        if player_dict["pwr"]["rage"] > 0:
            player_dict["status"].append("rage")                #appends rage to list(user_status)
            print("Line 811")
            updated_texts.extend(["You stay enraged for " + str(player_dict["pwr"]["rage"]) + " turn/s."])
        else:
            remove_status("rage", player_dict["status"])        #removes rage status from terminal print
            print("Line 815")
            updated_texts.extend(["You are no longer enraged"])
    else:
        pass
    #CPU is inflicted with burn
    if cpu_dict["pwr"]["burned"] > 0:
        cpu_dict["hp"] -= 1                                     #reduces burn duration
        cpu_dict["pwr"]["burned"] -= 1
        print("Line 823")
        updated_texts.extend([enemy["name"].title() + " takes 1 DMG from burn."])
        #prints remaining duration of Burn status
        if cpu_dict["pwr"]["burned"] > 0:
            cpu_dict["status"].append("burn")                   #appends burn to list(cpu_status)
            print("Line 828")
            updated_texts.extend([enemy["name"].title() + " will continue to take DMG for " + str(cpu_dict["pwr"]["burned"]) + " turn/s."]) 
        else:
            remove_status("burn", cpu_dict["status"])           #removes burn status from terminal print
            print(enemy["name"].title() + " is no longer on fire.")
    else:
        pass
    
    #Enemy Passive effects & interactions
    #Orc passive triggers if turn count is divisible by 4
    if enemy["name"].lower() == "orc" and game_dict["turn"] % 4 == 0:
        print("Line 839")
        updated_texts.extend(["The Orc receives 3 HP from its passive."])
        cpu_dict["hp"] += 3

    #Bandit passive triggers if turn count is divisible by 4
    elif enemy["name"].lower() == "bandit" and game_dict["turn"] % 4 == 0:
        print("Line 846")
        updated_texts.extend(["The bandit steals your DMG by 1 due to its passive."])
        player_dict["dmg"] -= 1
        cpu_dict["dmg"] += 1

    #Undead passive triggers if turn count is divisible by 3
    elif enemy["name"].lower() == "undead" and game_dict["turn"] % 3 == 0:
        #Player negates healing of undead passive and restores a bit of hp when drained if thorns is active
        if player_dict["pwr"]["thorns"] > 0:
            updated_texts.extend(["The undead drains your HP by, " + str(cpu_dict["dmg"]) + " due to its passive."])
            player_dict["hp"] -= cpu_dict["dmg"]//2
            updated_texts.extend([enemy["name"].title() + " couldn't restore HP because of thorns."])
            player_dict["pwr"]["thorns"] -= 1
            if player_dict["pwr"]["thorns"] > 0:
                updated_texts.extend(["You will continue to reflect DMG when attacked for the next " + str(player_dict["pwr"]["thorns"]) + " attack/s."])
            elif player_dict["pwr"]["thorns"] <= 0:
                remove_status("thorns", player_dict["status"])
                print("Line 864")
                updated_texts.extend(["Thorns are now deactivated."])
            else:
                pass
        
        #Else, undead passive drains Player HP
        else:
            print("Line 873")
            updated_texts.extend(["The Undead drains your HP by, " + str(cpu_dict["dmg"]//2) + " due to its passive."])
            cpu_dict["hp"] += cpu_dict["dmg"]//2
            player_dict["hp"] -= cpu_dict["dmg"]//2
    else:
        pass

    #Check if win or lose
    player_win = game_dict["CPU"]["hp"] <= 0
    player_lose = game_dict["Player"]["hp"] <= 0
    if player_win or player_lose:
        if player_win:
            updated_texts.extend(["You have cleared the floor.", "You receive 8 HP."])
            game_dict["Player"]["hp"] += 8
            game_dict["wins"] += 1
        else:
            updated_texts.extend(["You lose!"])

def update(widgets, bg, player, enemy):
    player_hand = game_dict["Player"]["hand"]
    cpu_hand = game_dict["CPU"]["hand"]
    player_pwr = game_dict["Player"]["pwr"]

    #Check if win or lose
    player_win = game_dict["CPU"]["hp"] <= 0
    player_lose = game_dict["Player"]["hp"] <= 0
    if player_win:
        #prev_window, screenWidth, screenHeight, char_name, wins
        close_widget(widgets)
        floor(bg, 1920, 1080, player, game_dict["wins"])
    elif player_lose:
        end_credits()
    else:
        #PLAYER OR CPU RAN OUT OF CARDS
        if len(player_hand) == 0 and len(cpu_hand) == 0:
            player_hand.extend(cards.get_hand(player.lower()))
            cpu_hand.extend(cards.enemy_get_cards(enemy["name"].lower()))
        elif len(player_hand) == 0:
            player_hand.extend(cards.get_hand(player.lower()))
        elif len(cpu_hand) == 0:
            cpu_hand.extend(cards.enemy_get_cards(enemy["name"].lower()))

        #PLAYER IS UNABLE TO USE TURN
        if player_pwr["shocked"] > 0:
            frame = "null"
            player_card = "null"
            player_card_img = "null"
            clickCard(bg, frame, player, enemy, player_card, player_card_img)
        else:
            show_cards(bg, player, enemy)  

        close_widget(widgets)
        show_player_health_bar(bg)
        show_enemy_health_bar(bg)
        show_player_dmg_bar(bg)
        show_enemy_dmg_bar(bg)
        show_player_status(bg)

def show_player_health_bar(bg):
    hp_cnv = tk.Canvas(bg, bg="#1ab172", height=75, width=350, highlightthickness=0)
    hp_cnv.place(relx=0.15, rely=0.10, anchor="center")
    hp_cnv.create_text(20, 2, text="HP: " + str(game_dict["Player"]["hp"]), font=("Gotham Black", 50), fill="white", anchor="nw")

def show_enemy_health_bar(bg):
    hp_cnv = tk.Canvas(bg, bg="#1ab172", height=75, width=350, highlightthickness=0)
    hp_cnv.place(relx=0.85, rely=0.10, anchor="center")
    hp_cnv.create_text(20, 2, text="HP: " + str(game_dict["CPU"]["hp"]), font=("Gotham Black", 50), fill="white", anchor="nw")

def show_player_dmg_bar(bg):
    dmg_cnv = tk.Canvas(bg, bg="#b52d2d", height=75, width=350, highlightthickness=0)
    dmg_cnv.place(relx=0.15, rely=0.175, anchor="center")
    dmg_cnv.create_text(20, 2, text="DMG: " + str(game_dict["Player"]["dmg"]), font=("Gotham Black", 50), fill="white", anchor="nw")

def show_enemy_dmg_bar(bg):
    dmg_cnv = tk.Canvas(bg, bg="#b52d2d", height=75, width=350, highlightthickness=0)
    dmg_cnv.place(relx=0.85, rely=0.175, anchor="center")
    dmg_cnv.create_text(20, 2, text="DMG: " + str(game_dict["CPU"]["dmg"]), font=("Gotham Black", 50), fill="white", anchor="nw")

def show_player_status(bg):
    for i, status in enumerate(set(game_dict["Player"]["status"])):
        status_cnv = tk.Canvas(bg, width=85, height=40, highlightthickness=0, bg="#d59719")
        status_cnv.place(relx=0.15, rely=0.195+(i*0.05), anchor="center")
        status_cnv.create_text(5, 5, text=status.upper(), font=("Gotham Black", 20), fill="white", anchor="nw")
    
def instructions(program_window, icon):
    canvas = tk.Canvas(program_window, bg="white")
    canvas.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.8)

    tk.Button(canvas, bg="white", image=icon, bd=0, command=lambda:close_widget([canvas])).pack(anchor="ne")

def show_character_play(char_name):
    img_location = {
        "berserker": "img/berserker_play.png",
        "ranger": "img/ranger_play.png",
        "mage": "img/mage_play.png",
        "assassin": "img/assassin_play.png",
        "tank": "img/tank_play.png",
    }
    return img_location[char_name]

def generate_enemy(index):
    enemies = {
        0: {
            "name": "Slime",
            "img_location": "img/slime_main.png",
            "bg_location": "img/slime_bg.png",
            "play_location": "img/slime_play.png",
            "frame_color": "#53a785",
            "box_color": "#0085A9"
        },
        1: {
            "name": "Orc",
            "img_location": "img/orc_main.png",
            "bg_location": "img/orc_bg.png",
            "play_location": "img/orc_play.png",
            "frame_color": "#898172",
            "box_color": "#617C63"
        },
        2: {
            "name": "Bandit",
            "img_location": "img/bandit_main.png",
            "bg_location": "img/bandit_bg.png",
            "play_location": "img/bandit_play.png",
            "frame_color": "#8a2800",
            "box_color": "#B961A8"
        },
        3: {
            "name": "Undead",
            "img_location": "img/undead_main.png",
            "bg_location": "img/undead_bg.png",
            "play_location": "img/undead_play.png",
            "frame_color": "#848476",
            "box_color": "#5E7C67"
        },
        4: {
            "name": "Overlord",
            "img_location": "img/overlord_main.png",
            "bg_location": "img/overlord_bg.png",
            "play_location": "img/undead_play.png"
        }
    }
    return enemies[index]

def close_widget(widgets):
    for widget in widgets:
        widget.destroy()

def end_credits():
    print("Yey")

def remove_status(status, status_arr):
    while status in status_arr:
        status_arr.remove(status)

def change_text(msgs, cnv, txt, widgets, bg, player, enemy):
    print(game_dict)
    print(msgs)
    if len(msgs) == 0:
        update(widgets, bg, player, enemy)
    else:
        cnv.itemconfig(txt, text=msgs[0])
        msgs.pop(0)

if __name__ == "__main__":
    start_window()