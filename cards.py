import random
#Assigning and generating cards

def get_values():
    handint = []  # empty list where integers will be appended
    while len(handint) < 5:
        n = random.randint(1, 8)  # (1,8) allows only a max of 2 copies of any common card type in a single hand
        if n not in handint:  # prevents repeating values
            handint.append(n)
    modulohand = [x % 4 for x in handint]  # converts values into usable indices
    return modulohand  # returns list of integers(0-3)d

# list containing common cards
cardtype = ["attack", "block", "boost", "shock"]

def get_cards():
    common_cards = []  # empty list where common cards will be appended
    val = get_values()  # list containing indices from get_values()
    for e in val:
        card = cardtype[e]  # gets a card based on the iterated index
        common_cards.append(card)  # appends card to list(common_cards)
    return common_cards  # returns common_cards


# dictionary containing unique cards of classes
unique_cards = {"berserker": "rage", "ranger": "trap", "mage": "burn", "assassin": "cleave", "tank": "thorns"}


def get_hand(role):
    user_hand = get_cards()
    user_hand.append(unique_cards[role])  # adds unique card to hand based on chosen class
    return user_hand  # returns hand with added unique card


# dictionary containing disabled cards of enemies
disabled_enemy_cards = {"slime": "block", "orc": "shock", "bandit": "boost", "undead": "attack", "overlord": "none"}


def enemy_get_cards(kind):
    enemy_hand = get_cards()  # gets common cardds
    invalid_card = disabled_enemy_cards[kind]  # assigns invalid from the dict(disabled_enemy_cards)
    while invalid_card in enemy_hand:  # removes certain cards depending on the enemy type
        enemy_hand.remove(invalid_card)
    return enemy_hand  # returns edited hand

def role_check():  # recursion function that checks if input in choosing a class is correct
    role = input("Enter the letter of your choice: ").lower()
    if role in ["a", "b", "c", "d", "e"]:
        return role
    else:
        print("Invalid input.")
        corrected_role = role_check()
        return corrected_role