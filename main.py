
import time
import infos
from cards import *

def user_play(i):
    if user_shocked > 0:
        print("You are stunned.")
        return "stun"                                   #returns stun if stunned 
    else:
        user_card = i
        print("You used "+ user_card.capitalize() +".") #prints card used by player
        hand.remove(i)                                  #removes used card from hand
        return user_card                                #returns the card that player chose

#if you plan to place this in a different file,
#you need to know how to update list(cpu_hand) across different files
def cpu_play():
    while True:
        if cpu_trapped == True:
            print(enemy, "is trapped and unable to move.")
            return "trapped"                            #returns trap if trapped 
        elif cpu_shocked > 0:
            print(enemy, "is stunned.")
            return "stun"                               #returns stun if stunned 
        elif len(cpu_hand) == 0:
            cpu_hand.extend(enemy_get_cards(enemy_types[ran_enemy]))    #redraws cards if CPU is out of cards
        else:
            cpu_card = cpu_hand[0]                      #plays the first card in hand
            print (enemy, "used "+ cpu_card.capitalize() +".")  #prints card used by CPU
            cpu_hand.remove(cpu_hand[0])                #removes used card from hand
            return cpu_card                             #returns the card that CPU chose

#function that removes status from printed terminal if no longer present
#Ex. PLAYER  | HP: 15        DMG: 3 | RAGE  <-- Removes this Status
def user_status_remove(status):
    status = status.upper()
    #uses while loop because there are actually multiple occurences of status just not visible in printed terminal
    #Ex. #Ex. PLAYER  | HP: 15        DMG: 3 | RAGE * RAGE * RAGE <-- This is what it actually looks like
    #Explained further later
    while status in user_status:
        user_status.remove(status)

#Same function above but for CPU
def cpu_status_remove(status):
    status = status.upper()
    while status in cpu_status:
        cpu_status.remove(status)

#sets variables to their default value
#function might be difficult to place in different files because of globals
def initialize():
    global user_dmg,cpu_dmg,user_shocked,user_rage,user_thorns              #global allows variables to be updated outside the function
    global cpu_shocked,cpu_burned,cpu_trapped,cpu_hand,hand,user_status     #but global variables won't work if function is split into
    global cpu_status,turn,user_display_status,cpu_display_status           #different files(modules)

    user_dmg,cpu_dmg = 3,3                                  #tuple assignments to shorten code
    user_rage,user_thorns,user_shocked = 0,0,0
    cpu_shocked,cpu_burned,cpu_trapped = 0,0,False
    cpu_hand,hand,user_status,cpu_status  = [],[],[],[]
    turn = 0
    user_display_status = " * ".join(set(user_status))
    cpu_display_status = " * ".join(set(cpu_status))

#function that contains card and passive interactions
#function might be difficult to place in different files because of globals
def match(c):
    global user_hp,user_dmg,user_shocked,user_rage,user_thorns,user_display_status      #global allows variables to be updated outside the function
    global cpu_hp,cpu_dmg,cpu_shocked,cpu_burned,cpu_trapped,cpu_display_status,turn    #but global variables won't work if function is split into

    card1 = user_play(c)    #card the player used
    card2 = cpu_play()      #card the CPU used

    time.sleep(1)
    #Card Interactions
    #Player uses Attack card interactions
    if card1 == "attack":
        #CPU reflects DMG with block
        if card2 == "block" and user_rage <= 0:
            print("Damage reflected! You receive", user_dmg,"DMG.")
            user_hp -= user_dmg

        #Player ignores block if ENRAGED
        elif card2 == "block" and user_rage > 0:
            print("You ignore the", enemy,"\b's block.")
            print("You deal", user_dmg,"DMG.")
            time.sleep(1.5)
            print("You restore", user_dmg//2,"HP from your attack.")
            cpu_hp -= user_dmg
            user_hp += user_dmg//2

        #CPU reflects DMG with block, but Player also reflects DMG with thorns
        elif card2 == "block" and user_thorns > 0:
            cpu_hp -= cpu_dmg//2
            user_hp -= cpu_dmg
            user_hp += cpu_dmg//2
            print(enemy, "deals", cpu_dmg,"DMG.")
            print("You reflect",cpu_dmg//2,"DMG and heal",cpu_dmg//2, "HP because of thorns.")

        #Player ignores slime passive when ENRAGED
        elif user_rage > 0 and enemy_passive == "slime":
            print ("You ignore the slime's passive and deal",user_dmg,"DMG.")
            time.sleep(1.5)
            print("You restore", user_dmg//2,"HP from your attack.")
            cpu_hp -= user_dmg
            user_hp += user_dmg//2

        #Player attacks restore health when ENRAGED
        elif user_rage > 0:
            print("You deal", user_dmg,"DMG.")
            time.sleep(1.5)
            print("You restore", user_dmg//2,"HP from your attack.")
            cpu_hp -= user_dmg
            user_hp += user_dmg//2

        #Player only deals half DMG if enemy type is a slime
        elif enemy_passive == "slime":
            print("You only deal", user_dmg//2,"DMG because of the slime's passive.")
            cpu_hp -= user_dmg//2

        #Else, deals player deals DMG
        else:
            print("You deal", user_dmg,"DMG.")
            cpu_hp -= user_dmg

    #Player uses Block card interactions
    elif card1 == "block":
        #Player reflects Attack card DMG with block
        if card2 == "attack":
            print("Damage reflected! The", enemy,"receives", cpu_dmg,"DMG.")
            cpu_hp -= cpu_dmg

        #Player reflects Shock card effect with block
        elif card2 == "shock":
            print("Shock reflected! The", enemy,"will be stunned next turn.")
            cpu_shocked += 1
            cpu_status.append("STUN")       #appends stun to list(cpu_status)

        #Else, nothing happens
        else:
            pass

    #Boost cards don't have special interactions
    elif card1 == "boost":
        print("Your DMG is now increased to", user_dmg+1)
        user_dmg += 1

    #Player uses Shock card interactions
    elif card1 == "shock":
        #CPU reflects Shock with Block
        if card2 == "block" and user_rage <= 0:
            print("Shock reflected! You will be stunned next turn.")
            user_shocked += 1
            user_status.append("STUN")      #appends stun to list(user_status)

        #Player ignores Shock while ENRAGED
        elif card2 == "block" and user_rage > 0:
            print("You ignore the", enemy,"\b's block.")
            print(enemy, "will be stunned next turn.")
            cpu_shocked += 1

        #Else, CPU is stunned next turn
        else:
            print(enemy, "will be stunned next turn.")
            cpu_shocked += 1
            cpu_status.append("STUN")       #appends stun to list(cpu_status)

    #Player uses Rage card
    elif card1 == "rage":
        print("You are now ENRAGED! You ignore Stun & Shock cards and heal half of the damage you deal!")
        user_rage += 4

    #Player uses Burn card, inflicts CPU with Burn status
    elif card1 == "burn":
        print(enemy, "has been inflicted with burn!")
        cpu_burned += 4

    #Player uses Trap card interaction
    elif card1 == "trap":
        #CPU blocks Trap with Block
        if card2 == "block":
            print("The", enemy,"deflected the trap!")

        #Else, CPU is inflicted with Trap status
        else:
            cpu_status.append("TRAP")           #appends trap to list(cpu_status)
            print("The", enemy,"\b's movements have been hindered. The", enemy,"will be unable to move next turn!")
            cpu_trapped = True

    #Player uses Cleave card interactions
    elif card1 == "cleave":
        #CPU reflects Cleave card DMG with block
        if card2 == "block":
           print("Special card reflected! You receive", 2*user_dmg,"DMG.")
           user_hp -= 2*user_dmg

        #Cleave only deals half DMG if enemy is a slime
        elif enemy_passive == "slime":
            print("Double strike! But you only deal", 2*user_dmg//2,"DMG beacuse of the slime's passive.")
            cpu_hp -= 2*user_dmg//2

        #Else, Cleave deals double DMG value
        else:
            print("Double strike! You deal", 2*user_dmg,"DMG.")
            cpu_hp -= 2*user_dmg

    #Player uses Thorns card
    elif card1 == "thorns":
        user_status.append("THORNS")        #appends thorns to list(user_status)
        print("Activited thorns! You now reflect DMG and heal when attacked.")
        user_thorns += 2

    #Player is stunned
    elif card1 == "stun":
        user_shocked -= 1               #reduces/removes stun duration
        if user_shocked == 0:
            user_status_remove("stun")  #removes stun status from terminal print
        else:
            pass
    else:
        pass


    #CPU uses Attack card interactions
    if card2 == "attack":
        #Player reflects DMG with block, pass because interaction was already declared earlier
        if card1 == "block":
            pass

        #CPU takes reflected DMG if Player is in Thorns. Also, heals player of reflected DMG
        elif user_thorns > 0:
            cpu_hp -= cpu_dmg//2
            user_hp -= cpu_dmg
            user_hp += cpu_dmg//2
            print(enemy, "deals", cpu_dmg,"DMG.")

            #Thorns negates overlord lifesteal passive
            if enemy_passive == "overlord":
                print (enemy, "couldn't restore HP because of thorns.")
            time.sleep(1.5)
            print("You reflect",cpu_dmg//2,"DMG and heal",cpu_dmg//2, "HP because of thorns.")
            user_thorns -= 1     #reduces thorns duration

            #Prints remaining duration of Thorns
            if user_thorns > 0:
                print("You will continue to reflect DMG when attacked for the next",user_thorns,"attack/s.")
            elif user_thorns <= 0:
                user_status_remove("thorns")            #removes thorns status from terminal print
                print("Thorns are now disactivated.")
            else:
                pass

        #CPU heals from attacks if enemy type is Overlord
        elif enemy_passive == "overlord":
            print(enemy, "deals", cpu_dmg,"DMG and restores",cpu_dmg//2,"HP.")
            user_hp -= cpu_dmg
            cpu_hp += cpu_dmg//2

        #Else, CPU deals DMG
        else:
            print(enemy, "deals", cpu_dmg,"DMG.")
            user_hp -= cpu_dmg

    #CPU uses Block card, pass because interactions have already been declared earlier
    elif card2 == "block":
        pass

    #CPU uses Boost card
    elif card2 == "boost":
        print(enemy, "DMG is now increased to", cpu_dmg+1)
        cpu_dmg += 1

    #CPU uses Shock card interactions
    elif card2 == "shock":
        #Shock card is reflected with block, pass because interaction has already been declared earlier
        if card1 == "block":
            pass

        #Player ignores Shock card while ENRAGED
        elif user_rage > 0:
            print("You ignore the", enemy,"\b's shock.")
            time.sleep(1.5)

        #Else, CPU stuns the Player next turn
        else:
            print("You will be stunned next turn.")
            user_shocked += 1
            user_status.append("STUN")              #appends stun to list(user_status)

    #CPU is trapped interactions
    elif card2 == "trapped":
        #Trap is removed if Player attacks
        if card1 == "attack":
            cpu_status_remove("trap")               #removes trap status from terminal print
            print ("The", enemy,"\b's trap has been broken.")
            cpu_trapped = False
            #if CPU is trapped & stunned, also removes stun status
            if cpu_shocked > 0:
                cpu_shocked = 0
                cpu_status_remove("stun")            #removes stun status from terminal print
            else:
                pass
        #Player uses Shock while CPU is trapped
        elif card1 == "shock":
            cpu_shocked += 1
            cpu_status.append("STUN")               #appends stun to list(cpu_status)

        #CPU is trapped & stunned, removes stun while trap remains
        elif cpu_shocked > 0:
            cpu_status.append("TRAP")               #appends trap to list(cpu_status)
            print (enemy, "is still trapped.")
            cpu_shocked -= 1                        #reduces/removes stun duration
            if cpu_shocked == 0:
                cpu_status_remove("stun")           #removes stun status from terminal print
            else:
                pass

        #Else, CPU is still trapped
        else:
            print (enemy, "is still trapped.")

    #CPU is stunned, reduces/removes stun duration
    elif card2 == "stun":
        cpu_shocked -= 1                            #Uses integer in case Player was stunned twice
        if cpu_shocked == 0:
            cpu_status_remove("stun")               #removes stun status from terminal print
        else:
            pass
    else:
        pass

    #Player is enraged
    if user_rage > 0:
        user_rage -= 1          #reduces rage duration
        if user_rage > 0:
            user_status.append("RAGE")              #appends rage to list(user_status)
            print("You stay enraged for the next",user_rage,"turn/s.")
        else:
            user_status_remove("rage")              #removes rage status from terminal print
            print ("You are no longer enraged.")
    else:
        pass

    #CPU is inflicted with burn
    if cpu_burned > 0:
        cpu_hp -= 1
        cpu_burned -= 1         #reduces burn duration
        print(enemy, "takes 1 DMG from burn.")
        #prints remaining duration of Burn status
        if cpu_burned > 0:
            cpu_status.append("BURN")               #appends burn to list(cpu_status)
            print(enemy, "will continue to take DMG for",cpu_burned,"turn/s.")
        else:
            cpu_status_remove("burn")               #removes burn status from terminal print
            print(enemy, "is no longer on fire.")
    else:
        pass

    #Enemy Passive effects & interactions
    #Orc passive triggers if turn count is divisible by 4
    if enemy_passive == "orc" and turn % 4 == 0:
        print ("The orc receives 3 HP from its passive.")
        cpu_hp += 3

    #Bandit passive triggers if turn count is divisible by 4
    elif enemy_passive == "bandit" and turn % 4 == 0:
        print ("The bandit steals your DMG by 1 due to its passive.")
        user_dmg -= 1
        cpu_dmg += 1

    #Undead passive triggers if turn count is divisible by 3
    elif enemy_passive == "undead" and turn % 3 == 0:
        #Player negates healing of undead passive and restores a bit of hp when drained if thorns is active
        if user_thorns > 0:
            print ("The undead drains your HP by,", cpu_dmg//2 ,"due to its passive.")
            user_hp -= cpu_dmg//2
            print (enemy, "couldn't restore HP because of thorns.")
            time.sleep(2)
            print ("You restore", (cpu_dmg//2)//2,"HP because of thorns.")
            time.sleep(1.5)
            user_thorns -= 1        #reduces thorns status duration
            #prints thorns remaining duration
            if user_thorns > 0:
                print("You will continue to reflect DMG when attacked for the next",user_thorns,"attack/s.")
            elif user_thorns <= 0:
                user_status_remove("thorns")        #removes thorns status from terminal print
                print("Thorns are now deactivated.")
            else:
                pass

        #Else, undead passive drains Player HP
        else:
            print ("The undead drains your HP by,", cpu_dmg//2 ,"due to its passive.")
            cpu_hp += cpu_dmg//2
            user_hp -= cpu_dmg//2
    else:
        pass

    #prints active statuses as string
    #uses "set" to remove repeating occurences of statuses
    user_display_status = " * ".join(set(user_status))
    cpu_display_status = " * ".join(set(cpu_status))

    return None

"""
while True: #loops when wrong input is entered or game ends
    print("\n*Castle of Cards*")
    print("(A) PLAY\n(B) HOW TO PLAY\n(C) GAME ENCYCLOPEDIA\n(D) EXIT")
    select = input("Enter the letter of your choice: ").lower()
    #Play
    if select == "a":
        print("\nSelect a class you want to use.")
        print("(A) Berserker\t(B) Mage\t(C) Ranger\t(D) Assassin\t(E) Tank")
        #checks if input is correct and assigns selected class to the player
        #variable is called "role" and not "class" because class is a bad variable name(the more you know)
        role = role_check()                           
        enemy_types = ["slime", "orc", "bandit", "undead", "overlord"]  #list containing enemy types
        initialize()                                  #calls initialize()
        ran_enemy = random.randint(0,3)               #gets a random integer used to determine index of enemy type

        #enemy_types[ran_enemy] is used to assign enemy type
        #line below is just used for printing enemy type as text
        enemy = enemy_types[ran_enemy].capitalize()         
        enemy_passive = enemy_types[ran_enemy]  #assigns enemy passive
        user_hp = 15     #default player HP
        cpu_hp = 10      #default common monster HP, not included in initialize() because final boss HP is different
        wins = 0         #used for game progression

        #First Battle
        print("\nWelcome to the Castle of Cards. The Overlord has been expecting you.")       #Story text
        time.sleep(1)
        print("How long will you hold up?")
        time.sleep(1)
        print("\nFloor 1:",enemy)
        time.sleep(1.5)
        print("\nPLAYER \t| HP:", user_hp, "\tDMG:", user_dmg,"|")      #display Player stats
        print(enemy.upper(),"\t| HP:" , cpu_hp, "\tDMG:" , cpu_dmg,"|") #display CPU stats

        while True:
            #lose
            if user_hp <= 0:
                print("\nYou lose!")
                time.sleep(2)
                break

            #2nd & 3rd battle
            elif cpu_hp <= 0 and wins < 2:
                wins += 1                                       #used for game progression
                enemy_types.remove(enemy_types[ran_enemy])      #removes defeated enemy to prevent repeating encounters
                print ("\nYou have cleared floor",wins , "\b! You receive",8,"HP.") 
                time.sleep(1.5)
                user_hp += 8                                     #restore HP upon win
                print("You proceed to the next floor.\n\n")
                time.sleep(1.5)
                
                #new floor
                initialize()    #calls initialize()
                ran_enemy = random.randint(0,len(enemy_types)-2) #len(enemy_types)-2 because defeated enemy was removed from list(enemy_types)
                enemy = enemy_types[ran_enemy].capitalize()
                enemy_passive = enemy_types[ran_enemy]
                cpu_hp = 10                                      #default common monster HP
                print("Floor",wins+1,"\b:",enemy)                #prints current floor
                time.sleep(1.5)
                print("\nPLAYER \t| HP:", user_hp, "\tDMG:", user_dmg,"|")
                print(enemy.upper(),"\t| HP:" , cpu_hp, "\tDMG:" , cpu_dmg,"|")

            #Final Boss    
            elif cpu_hp <= 0 and wins == 2:
                wins += 1                                        #used for game progression
                print ("\nYou have cleared floor",wins , "\b! You receive",8,"HP.")
                time.sleep(1.5)
                user_hp += 8
                print("You proceed to the next floor.\n\n")
                time.sleep(1.5)

                #Final Boss
                initialize()    #calls initialize()
                ran_enemy = enemy_types.index("overlord")        #gets index of "overlord" used to set enemy type
                enemy = enemy_types[ran_enemy].capitalize()
                enemy_passive = enemy_types[ran_enemy]
                cpu_hp = 15                                      #default final boss HP
                print("Floor",wins+1,"\b: FINAL BOSS")
                time.sleep(1.5)
                print("\nPLAYER \t\t| HP:", user_hp, "\tDMG:", user_dmg,"|")
                print(enemy.upper(),"\t| HP:" , cpu_hp, "\tDMG:" , cpu_dmg,"|")

            #Final Boss Second Phase
            elif cpu_hp <= 0 and wins == 3:
                wins += 1
                print("\nYou have defeated the Overlord, but...")
                time.sleep(2)
                print("You know how some bosses have a second phase where they become stronger?")
                time.sleep(3)
                print("Well... That's exactly what's happening.")
                time.sleep(2)
                print("The Overlord comes back to life with 8 HP and gains +2 DMG!")
                time.sleep(2)
                print("You have rested for a bit and regained",4, "HP." )
                cont = input("\nPress Enter to continue:\n")
                user_hp += 4
                
                cpu_hp = 8
                cpu_dmg += 2
                print("Floor",wins,"\b: FINAL BOSS (SECOND PHASE)")
                time.sleep(1.5)
                print("\nPLAYER \t\t| HP:", user_hp, "\tDMG:", user_dmg,"|",user_display_status)
                print("OVERLORD \t| HP:" , cpu_hp, "\tDMG:" , cpu_dmg,"|",cpu_display_status)

            #Game finished
            elif cpu_hp <= 0 and wins == 4:
                print("\nCongratulations! You have cleared the Castle of Cards!")
                time.sleep(3)
                break

            #combat
            elif len(hand) != 0:
                delimeter = " | "
                print(delimeter.join(hand))             #prints cards in hand as string
                move = input("Play a card: ").lower()   #card input
                #valid card input
                if move in hand:
                    turn += 1                           #variable(turn) is used for certain passives
                    print()
                    match(move)                         #most important function call, CTRL + F: match(c) to easily find function
                    time.sleep(1.5)
                    print()
                    #prints stats a little different when against overlord
                    #because the length of the word "overlord" causes misalignments
                    if enemy_passive == "overlord":
                        print("\nPLAYER \t\t| HP:", user_hp, "\tDMG:", user_dmg,"|",user_display_status)
                        print("OVERLORD \t| HP:" , cpu_hp, "\tDMG:" , cpu_dmg, "|",cpu_display_status)
                    else:
                        print("PLAYER \t| HP:", user_hp, "\tDMG:", user_dmg,"|",user_display_status)
                        print(enemy.upper(),"\t| HP:" , cpu_hp, "\tDMG:" , cpu_dmg,"|",cpu_display_status)
                #invalid card input        
                elif move not in hand:                  
                    print ("\nThat card is not in hand.")
            else:
                hand = get_hand(role)                   #redraws cards if hand is empty

    elif select == "b":
        infos.howToplay()
        infos.back()
        
    elif select == "c":
        while True:
            print("\n(A) CLASSES\n(B) ENEMIES\n(C) COMMON CARDS\n(D) BACK")
            choice = input("Enter the letter of your choice: ").lower()
            if choice == "a":
                print ("\n(A) BERSERKER\n(B) MAGE\n(C) RANGER\n(D) ASSASSIN\n(E) TANK")
                role_info = input("Enter the letter of your choice: ").lower()
                #prints role information
                if role_info == "a":
                    infos.berserker()
                elif role_info == "b":
                    infos.mage()
                elif role_info == "c":
                    infos.ranger()
                elif role_info == "d":
                    infos.assassin()
                elif role_info == "e":
                    infos.tank()
                else:
                    pass
                infos.back()

            
            #Enemies       
            elif choice == "b":
                print ("\n(A) SLIME\n(B) ORC\n(C) BANDIT\n(D) UNDEAD\n(E) OVERLORD")
                enemy_info = input("Enter the letter of your choice: ").lower()
                #prints enemy information
                if enemy_info == "a":
                    infos.slime()
                elif enemy_info == "b":
                    infos.orc()
                elif enemy_info == "c":
                    infos.bandit()
                elif enemy_info == "d":
                    infos.undead()
                elif enemy_info == "e":
                    infos.overlord() 
                    time.sleep(2)
                else:
                    pass
                infos.back()

            elif choice == "c":
                print ("\n(A) ATTACK\n(B) SHOCK\n(C) BLOCK\n(D) BOOST")
                card_info = input("Enter the letter of your choice: ").lower()
                #prints card information
                if card_info == "a":
                    infos.attack()
                elif card_info == "b":
                    infos.shock()
                elif card_info == "c":
                    infos.block()
                elif card_info == "d":
                    infos.boost()
                else:
                    pass
                infos.back()

            elif choice == "d":
                break

    elif select == "d":
        exit()          #closes the program
    else:
        pass
"""