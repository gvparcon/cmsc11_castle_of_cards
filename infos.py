#HOW TO

def back():  # function used to return to previous menu in Game Encyclopedia
    input("\nPress Enter to return: ").lower()
    pass

def howToplay():
    print("\nCOMBAT\n")
    print("> The Player will have 15 HP at the start of the playthrough.")
    print("> Common enemies will have 10 HP, while the Final Boss will have 15 HP.")
    print("> The first one to run out of HP loses.")
    print("> Both the player and the opponent will have a DMG value of 3 at start of the battle.")
    print("> The DMG value determines the damage dealt of certain cards and passives.")
    print("> Both the player and the opponent chooses a card each turn and plays it at the same time.")
    print("> Each card has its own effect (check Game Encyclopedia to learn about card effects).")
    print("> A hand contains 6 cards, 5 common cards and 1 unique card.")
    print("> When a hand runs out of cards, it is replenished.")
    print("> There can't be more than 2 copies of any card type in a single hand.")
    cont = input("\nPress Enter to continue.\n")
    print("GAME PROGRESSION\n")
    print("> The Castle of Cards will have 4 floors.")
    print("> The First 3 floors will contain a random enemy.")
    print("> You won't be able to fight enemies that have already been encountered in your playthrough.")
    print("> The 4th floor will contain the Final Boss: Overlord.")
    print("> The player restores 8 HP after every encounter, but the player's DMG value resets to 3.")
    print("> You need to clear all 4 floors to win the game.")


#CLASSES
    
def berserker():
    """
    print ("\nBERSERKER\n")
    print ("'Fearsome warrior that runs headlong into battles without mercy for his enemies.'")
    cont = input("\nPress Enter to continue. \n")
    print ("> UNIQUE CARD: Rage")
    print ("> Player becomes ENRAGED.")
    print ("> While enraged, player ignores block & shock cards for the next 3 turns.")
    print ("> Attacks also restore half of the damage dealt as HP.")
    print ("> The effects of this card trigger upon use.")
    """
    return {
        "name": "Berserker",
        "description": "Fearsome warrior that runs headlong into battles\nwithout mercy for his enemies.",
        "unique_card": "Rage",
        "unique_card_activated": "Player becomes ENRAGED",
    }

def mage():
    """
    print ("\nMAGE\n")
    print ("'The seeker of knowledge and the wizard whose hand cackles with inner power.'")
    cont = input("\nPress Enter to continue:\n")
    print ("> UNIQUE CARD: Burn")
    print ("> Inflicts the enemy with Burn.")
    print ("> Enemies with burn take 1 DMG every turn.")
    print ("> Burn status will last for 3 turns.")
    print ("> Cannot be deflected by Block cards.")
    print ("> The effects of this card trigger upon use.")
    """
    return {
        "name": "Mage",
        "description": "The seeker of knowledge and the wizard whose\nhand cackles with inner power.",
        "unique_card": "Burn",
        "unique_card_activated": "Player becomes ENRAGED",
    }

def ranger():
    """
    print ("\nRANGER\n")
    print ("Wise, cunning, and superb hunter with extraordinary skills in weaponry.'")
    cont = input("\nPress Enter to continue.\n")
    print ("> UNIQUE CARD: Trap")
    print ("> Enemy movements will be hindered by a trap.")
    print ("> Entrapped enemies are unable to use cards, but enemy passives will still trigger.")
    print ("> The trap will persist until the player uses an Attack card.")
    print ("> Can be deflected by Block cards.")
    print ("> The effects of this card trigger on next turn.")
    """
    return {
        "name": "Ranger",
        "description": "Wise, cunning, and superb hunter with\nextraordinary skills in weaponry.",
        "unique_card": "Trap",
        "unique_card_activated": "Player becomes ENRAGED",
    }
    

def assassin():
    """
    print ("\nASSASSIN\n")
    print ("'Steathly adventurer with menacing demeanor and insane combatting skills.'")
    cont = input("\nPress Enter to continue.\n")
    print ("> UNIQUE CARD: Cleave")
    print ("> Deal double of the player's DMG value to the enemy.")
    print ("> Can be deflected by Block Cards.")
    print ("> When deflected, the players receives the damage instead.")
    """
    return {
        "name": "Assassin",
        "description": "Steathly adventurer with menacing demeanor\nand insane combatting skills.",
        "unique_card": "Cleave",
        "unique_card_activated": "Player becomes ENRAGED",
    }

def tank():
    """
    print ("\nTANK\n")
    print ("'Bruly warrior decked out in a thick steel-clad armor.\nResilient and almost invincible in battlefields.'")
    cont = input("\nPress Enter to continue.\n") 
    print ("> UNIQUE CARD: Thorns")
    print ("> Covers the player's armor with thorns.")
    print ("> Attacking enemies will receive half of their damage dealt.")
    print ("> Player will also restore the reflected damage as HP.")
    print ("> Thorns will also negate the healing effects of enemy attacks that involve health restoration.")
    print ("> The effects of this card trigger upon use.")
    """
    return {
        "name": "Tank",
        "description": "Bruly warrior decked out in a thick steel-clad armor.\nResilient and almost invincible in battlefields.",
        "unique_card": "Thorns",
        "unique_card_activated": "Player becomes ENRAGED",
    }

#ENEMIES

def slime():
    print ("\nSLIME\n")
    print ("'Slimy and goey beings that roam around the castle.'")
    cont = input("\nPress Enter to continue.\n")
    print ("> Slimes are unable to use block cards.")
    print ("> But, they only receive half damage from Attack cards and Unique card: Cleave.")

def orc():
    print ("\nORC\n")
    print ("'Foul humanoid creatures that are created by the Overlord.\nThey are cruel, fearless, and designed to live for destruction.'")
    cont = input("\nPress Enter to continue:\n")
    print ("> Orcs are unable to use Shock cards.")
    print ("> But, they restore 3 HP every 4 turns.")

def bandit():
    print ("\nBANDIT\n")
    print ("'Hostile humans under the spell dark magic.'")
    cont = input("\nPress Enter to continue.\n")
    print ("> Bandits are unable to use boost cards.")
    print ("> But, they steal 1 DMG value from the player every 4 turns.")

def undead():
    print ("\nUNDEAD\n")
    print ("'Reanimated corpses of dead humans and are extremely violent beings.'")
    cont = input("\nPress Enter to continue.\n")
    print ("> The undead are unable to use attack cards.")
    print ("> But, they drain the player's HP every 3 turns.")
    print ("> Amount drained is based on half their DMG value.")
    print ("> The undead heal from the amount they drained.")
    print ("> The healing effect is negated if the player has THORNS.")

def overlord():
    print ("\nOVERLORD\n")
    print ("Data Unknown")


#CLASSES
    
def attack():
    print ("\nATTACK\n")
    print ("> Deal current DMG value to the opponent.")

def shock():
    print ("\nSHOCK\n")
    print ("> Stuns the opponent. Effect triggers on the NEXT TURN.")

def block():
    print ("\nBLOCK\n")
    print ("> Reflects the effect of Attack & Shock cards back to the opponent.")

def boost():
    print ("\nBOOST\n")
    print ("> Increases the user's current DMG value by 1.")
