def intro():
    global troll_health
    global player_health
    player_health = 3
    troll_health = 5
    print(art)
    print_typewriter(f"Greetings {player_name}. Im one of the ghosts here at Python Manor. \nThe troll has kidnapped your sister! There's many rooms for you to explore. \nYou need to find the key to the dungeon, defeat the troll and retrieve your sister. \nBut be careful! Some of the rooms may look nice but there are many deadly traps waiting for you. Good luck. \n\nBe aware, for Yes/No questions, you can answer with Y/N or yes/no") 
    print_typewriter("\n\n*door creaks* The doors open and you begin to walk into the gloomy manor")
    hallway()
congrats = '''
 _    _        _   _    ______                   _ 
| |  | |      | | | |   |  _  \                 | |
| |  | | ___  | | | |   | | | |___  _ __   ___  | |
| |/\| |/ _ \ | | | |   | | | / _ \| '_ \ / _ \ | |
\  /\  /  __/ | | | |   | |/ / (_) | | | |  __/ |_|
 \/  \/ \___| |_| |_|   |___/ \___/|_| |_|\___| (_)
                                                   
                                                   
'''
you_won = '''
__   __              _    _               _ 
\ \ / /             | |  | |             | |
 \ V /___  _   _    | |  | | ___  _ __   | |
  \ // _ \| | | |   | |/\| |/ _ \| '_ \  | |
  | | (_) | |_| |   \  /\  / (_) | | | | |_|
  \_/\___/ \__,_|    \/  \/ \___/|_| |_| (_)
                                            
                                            '''
dead = """

__   __           ______ _          _     _     _____ _     
\ \ / /           |  _  (_)        | |   | |   |  _  | |    
 \ V /___  _   _  | | | |_  ___  __| |   | |   | | | | |    
  \ // _ \| | | | | | | | |/ _ \/ _` |   | |   | | | | |    
  | | (_) | |_| | | |/ /| |  __/ (_| |_  | |___\ \_/ / |____
  \_/\___/ \__,_| |___/ |_|\___|\__,_( ) \_____/\___/\_____/
                                     |/                     
                                                            
"""
art = """
  _____       _   _                   __  __                        
 |  __ \     | | | |                 |  \/  |                       
 | |__) |   _| |_| |__   ___  _ __   | \  / | __ _ _ __   ___  _ __ 
 |  ___/ | | | __| '_ \ / _ \| '_ \  | |\/| |/ _` | '_ \ / _ \| '__|
 | |   | |_| | |_| | | | (_) | | | | | |  | | (_| | | | | (_) | |   
 |_|    \__, |\__|_| |_|\___/|_| |_| |_|  |_|\__,_|_| |_|\___/|_|   
         __/ |                                                      
        |___/                                              
"""
def print_typewriter(text, delay=0.025):
  for char in text:
    print(char, end='', flush=True)
    time.sleep(delay)
game_complete = False
troll_health = 5
player_health = 3
player_name = input("What is your name? ")
inventory = []

def player_death():
    global player_health
    global game_complete
    inventory.clear()
    print(dead)
    start_again = input("Would you like to play again? ")
    if start_again.lower() == "yes" or start_again=="y":
        player_health = 3
        intro()
    elif start_again.lower() == "no" or start_again=="n":
        end_game()
    else:
        print_typewriter("\nInvalid Response")
        player_death()

def end_game():
    global game_complete
    game_complete = True
    print("Thank you for playing!\n\nGoodbye!")

def kitchen():
    global inventory
    global player_health
    print_typewriter("\nYou are in the kitchen, there is a cat in the corner. \nThe kitchen is completely trashed but the water is running.")
    kitchen_action = input("\nYou can feed the cat, have a drink of water, you can look in the drawers or leave. \nWhat would you like to do: ")
    if kitchen_action == "feed the cat":
        print("\nThere are two bowls. Which would you like to use?")
        cat_food = random.randint(1,2)
        feed_the_cat = int(input("\nBowl 1 or 2? "))
        if feed_the_cat == cat_food:
            print_typewriter("\nThe cat turns to you while you pour the food. It's eyes are completeley black. \nThe cat is possessed and attacks you. You die")
            player_death()
        elif feed_the_cat != cat_food:
            print("\nThe cat begins to eat...")
            kitchen()
        else:
            print("Invalid Response")
            kitchen()
    elif kitchen_action == "have a drink of water" or kitchen_action=="have a drink" and player_health < 4:
        print_typewriter("\nAhhh refreshing")
        player_health += 1
        print_typewriter("\nYour health is now 4\n")
        kitchen()
    elif kitchen_action == "have a drink of water" or kitchen_action=="have a drink" and player_health > 3:
        print("\nAhhh refreshing")
        kitchen()
    elif kitchen_action == "look in the drawers" and inventory.count("throwing knife")<1:
        print_typewriter("\nYou look through the drawers and appear to find some rusty utensils and hidden next to those is an old set of throwing knives")
        inventory.append("throwing knife")
        inventory.append("throwing knife")
        inventory.append("throwing knife")
        print("\nYou have taken the throwing knives\nYour inventory now consists of:", inventory)
        kitchen()
    elif kitchen_action == "look in the drawers" and inventory.count("throwing knife")>0:
        print_typewriter("\nThere is nothing else to see here")
        kitchen()
    elif kitchen_action == "leave":
        hallway()
    else:
        print_typewriter("\nInvalid response") 
        kitchen()

def books():
   global book_list
   global my_book
   book_list = ["\nTo Kill a Mockingbird", "\nIt", "\nPet Sematary", "\nDracula", "\nThe Exorcist", "\nThe Troop", "\nThe Ritual", "\nThe Haunting of Hill House", "\nThe Turn of The Screw", "\nIn The Eyes of Darkness" ]

def study():
    books()
    global book_list
    global my_book
    global inventory
    print_typewriter("\nYou enter the study. It is a dimly lit room with a bookcase on the back wall. There is a desk in the corner.")
    study_action = input("You can explore the desk or you can explore the bookcase. You can also leave. \nWhat would you like to do?: ")
    if study_action == "explore the desk" and inventory.count("dagger") < 1:
        print_typewriter("\nYou open the drawers. They are filled with old diaries by a young woman. Underneath you find an old folded up piece of parchment")
        print_typewriter("\nOn the parchment you read a text that says:")
        riddle = "I am strong enough to smash ships, but I fear the Sun. What am I?"
        answer = input(riddle + "\nAnswer: ")
        if answer == "ice":
                  print_typewriter("\nIn the compartment you discover a small dagger.")
                  inventory.append("dagger")
                  print("\nYou have taken the dagger\nYour inventory now consists of:", inventory)
                  study()
        while answer != "ice":
             answer = input("Incorrect, try again. ")
             if answer == "ice":
                 print_typewriter("\nIn the compartment you discover a small dagger.")
                 inventory.append("dagger")
                 print("\nYou have taken the dagger\nYour inventory now consists of:", inventory)
                 study()
        #^this needs to lead to the riddle and make the riddle
    elif study_action == "explore the desk" and inventory.count("dagger")>0:
        print_typewriter("\nThere is nothing else to see here.")
        study()
    elif study_action == "leave":
        hallway()
    elif study_action == "explore the bookcase" or study_action == "explore bookcase":
        study_action = input("Would you like to pick up a book?: ")
        if study_action.lower() == "yes" or study_action== "y":
            print_typewriter("\nWhich one?")
            print_typewriter(book_list)
            book_choice = input("\n\nWhich book do you wish to try?: ")
            my_book = "The Exorcist"
            if book_choice.lower() == my_book.lower():
                print_typewriter(f"\nIt seems that {my_book} has started to open a secret passage...")
                secret_room()
            elif book_choice.lower() == "dracula":
                upstairs()
            else:
               while book_choice.lower() != my_book.lower() and book_choice.lower() != "dracula":
                   print_typewriter("\nThis book is old and dusty")
                   book_choice = input("\nWhich book do you wish to try now?: ")
               if book_choice.lower() == my_book.lower():
                   print_typewriter(f"\nIt seems that {my_book} has started to open a secret passage...")
                   secret_room()
        elif study_action.lower() == "no" or study_action=="n":
            study()
        elif study_action == "leave":
            hallway()
    else:
        print_typewriter("\nInvalid response")
        study()

def upstairs():
    import random
    if inventory.count("Golden Easter Egg") > 0:
        print("\nWhat are you doing here?! You've already beaten my game!\n\nYou have been teleported back to the study")
        study()
    elif inventory.count("Golden Easter Egg") <1:
        print("\nGreetings weary traveller!\n\nI am the famous wizard of Python Manor.\n\nComplete my game for a secret prize! Fail and you may not like the consequences...")
        random_number = random.randint(1, 100)
        attempts = 8
        while attempts > 0:
            guess = int(input("Guess the number between 1 and 100: "))

            if guess == random_number:
                print("\nCorrect! You guessed correctly! Take your prize!")
                inventory.append("Golden Easter Egg")
                print("\nYou have taken the Golden Easter Egg\nYour inventory now consists of:", inventory)
                print("\nYou have been teleported back to the study")
                study()
                break
            else:
                if guess < random_number:
                    attempts -=1
                    print(f"\nYour guess is too low!\nYou have {attempts} attempts left!\n")
                elif guess > random_number:
                    attempts -=1
                    print(f"\nYour guess is too high!\nYou have {attempts} attempts left!\n")

        if attempts == 0:
            print("\nSorry, you ran out of attempts. The correct number was", random_number)
            print("The wizard waves his magical wand and you explode into a pile of goo!\n\nYou have died!")
            player_death()

def living_room():
    global inventory
    print_typewriter("You enter the living room. \nYou turn the light on. There is 2 sofas and dusty, old curtains and a dark figure on the sofa")
    print_typewriter("\nA GHOST APPEARS!")
    print_typewriter("\nIf you answer correctly, I will allow you to leave this room with your life")
    # print_typewriter("What's big, scary and has three wheels? ")
    riddle = "\nWhat's big, scary and has three wheels?"
    answer = input(riddle + "\nAnswer: ")
    if answer.lower() == "a monster with a tricycle" or answer.lower() == "a monster on a tricycle" or answer.lower() == "monster with a trycicle" or answer.lower() == "monster on a trycicle":
        print_typewriter("\nCongratulations, you have solved my spooky riddle. I will let you escape with your life this time... \n...but for now take this sword and use it well")
        inventory.append("sword")
        print("\nYou have taken the sword\nYour inventory now consists of:", inventory)
        hallway()
    else:
     print_typewriter("\nThat is incorrect, please try again")
     while answer != "a monster with a tricycle":
        answer = input("Incorrect, try again! ")
        if answer == "a monster with a tricycle":
            print_typewriter("\nCongratulations, you have solved my spooky riddle. I will let you escape with your life this time... but for now take this sword and use it well")
            inventory.append("sword")
            print("\nYou have taken the sword\nYour inventory now consists of:", inventory)
            hallway()

import random
def dungeon():
    global inventory
    global descriptions
    global dungeon_description
    descriptions = [
    "The dungeon is damp and cold, with walls covered in slimy moss.",
    "As you enter the dungeon, a pungent smell of decay fills your nostrils.",
    "You hear the faint sound of dripping water echoing through the dungeon.",
    "The dungeon is dimly lit by flickering torches, casting eerie shadows on the walls.",
    "As you walk deeper into the dungeon, the floor becomes increasingly slick and treacherous.",
    "You hear the skittering of countless tiny legs, and suddenly spiders swarm out from the shadows.",
    "A chill runs down your spine as you sense a dark presence lurking in the dungeon.",
    "You come across a room filled with grotesque spiderwebs, obscuring your view of what lies beyond.",
    "The dungeon seems to go on forever, twisting and turning in a labyrinthine maze."]
    dungeon_description = random.choice(descriptions)
    print_typewriter(dungeon_description + " The air is thick with the scent of strange, unidentifiable odors. You can see countless spiders scurrying across the walls and ceilings, their webs stretching across the corridors like a labyrinth. The thought of what else might be lurking in the shadows sends shivers down your spine.")
    def dungeon_gate():
        has_key = input("The gate is locked.\nDo you have the key? ")
        if has_key.lower() == "yes" or has_key=="y":
            if inventory.count("dungeon key") > 0:
                print_typewriter("\nYou enter the dungeon. The troll has 5 lives and is slow. \nYou can use any weapons you have collected to try to kill the troll.\n\n(When trying to attack the troll, use 'attack troll with [insert weapon name]'")
                troll_room()
            else:
                print_typewriter("\nYou do not have the key.")
                hallway()
        elif has_key.lower() == "no" or "n":
            print_typewriter("\nYou need to find the key")
            hallway()
        else:
            print_typewriter("\nInvalid Response")
            dungeon_gate()
    dungeon_gate()

def is_he_dead():
    global troll_health
    global game_complete
    global player_health
    if troll_health <= 0:
        print_typewriter("\nYou have killed the troll and retrieved your sister!\nCongratulations!!\nThe End!")
        print(congrats)
        print(you_won)
        game_complete = True
    elif player_health <= 0 and inventory.count("Golden Easter Egg") > 0 and inventory.count("sword") + inventory.count("dagger") + inventory.count("throwing knife") > 0:
        print("You have died...\n...\n...\n... But wait! The Golden Egg has been sacrificed and you recieve one more life!")
        inventory.remove("Golden Easter Egg")
        player_health += 1
        troll_room()
    elif player_health <= 0 and inventory.count("Golden Easter Egg") > 0 and inventory.count("sword") + inventory.count("dagger") + inventory.count("throwing knife") < 1:
        game_complete = True
        print_typewriter("\nYou have died!")
        player_death()
    elif player_health <= 0 and inventory.count("Golden Easter Egg") < 1 :
        game_complete = True
        print_typewriter("\nYou have died!")
        player_death()
    else:
        None

def troll_room():
    import random
    global game_complete
    global inventory
    global troll_health
    global player_health
    sword_attack = random.randint(1,4)
    throwing_knife = random.randint(1,5)
    while game_complete != True:
        if game_complete == True:
            break
        elif inventory.count("sword") + inventory.count("dagger") + inventory.count("throwing knife") == 0:
            print_typewriter("\nThe troll sees you are empty handed and laughs. He lifts you up and eats you whole.\nYou have died!")
            player_health = 0
            is_he_dead()
            player_death()
        else:
            None
        action = input("\nWhat do you do? ")
        if troll_health < 2 and troll_health > 0:
            print_typewriter("\nThe troll is dazed....")
        if action.lower() == "attack troll with sword" and inventory.count("sword") > 0 and sword_attack <= 3:
            print_typewriter("\nYou attack the troll with your sword, it grimaces in pain and tries to retalliate. You move out of the way just in time")
            troll_health -= 2
            print_typewriter("\nTroll Health: " + str(troll_health))
            is_he_dead()
            sword_attack
        elif action.lower() == "attack troll with sword" and inventory.count("sword") > 0 and sword_attack == 4:
            print_typewriter("\nYour sword misses the troll! He hits you back and it takes you a moment to get back up.")
            player_health -= 1
            print_typewriter("\nPlayer Health: " + str(player_health))
            is_he_dead()
            sword_attack
        elif action.lower() == "attack troll with throwing knife" and inventory.count("throwing knife")>0:
            if throwing_knife > 3:
                print_typewriter("\nYou hit the troll with your throwing knife! He grunts in pain!")
                inventory.remove("throwing knife")
                troll_health -= 1
                print_typewriter("\nTroll health: " + str(troll_health))
                is_he_dead()
                throwing_knife
            else:
                print_typewriter("\nYour knife misses. The troll knocks you to your feet and it takes you a second to get back up")
                player_health -= 1
                print_typewriter("\nPlayer Health: " + str(player_health) + "\n")
                is_he_dead()
                throwing_knife
        elif action.lower() == "attack troll with dagger" and inventory.count("dagger")>0:
            dagger_attack = random.randint(1,5)
            if dagger_attack <=4 :
                print_typewriter("\nYou lunge towards the troll and plunge your dagger in its chest")
                troll_health -= 2
                print_typewriter("\nTroll Health: " + str(troll_health))
                is_he_dead()
                dagger_attack
            elif dagger_attack == 5:
                print_typewriter("\nThe troll grabs you just in time and throws you back")
                player_health -=1
                print_typewriter("\nPlayer Health: " + str(player_health))
                is_he_dead
                dagger_attack
        else:
            print_typewriter("\nI don't understand that command.")

def dining_hall():
    print_typewriter("\nYou enter the dining room, inside you see a long table set for 12 people. \nThere's no-one in the room but a full suit of armor, a deer's head on the wall staring at you and a sea of cobwebs.")
    print_typewriter("\nWould you like to further explore the room? ")
    explore = input()
    if explore.lower() == "yes" or explore.lower()== "y":
        print_typewriter("\nYou find a light switch, a mysterious drink and a candle with a matchbox")
        print_typewriter("\nWhich would you like to examine? Switch, drink, candle or exit? ")
        while True:
         examine = input()
         if examine == "switch".lower():
            print_typewriter("\nThe light is broken\n")
         elif examine == "drink".lower():
            print_typewriter("\nThe drink was teleportation potion! \n\nYou're now in the dungeon right infront of the troll. You try to run but it grabs you and smashes you against the wall. \n\nYou have died. Please start again.\n")
            player_death()
         elif examine == "candle".lower():
            print_typewriter("\nThe candle starts burning lighting up the dark end of the room, to your horror you noitce a pile of human skulls piled up in the corner. \nA cat shoots out from under the tables & scampers out of the room.\n")
         elif examine == "exit".lower():
            hallway()
         else:
            print_typewriter("\nPlease try again\n")
    elif explore.lower() == "no" or explore.lower()=="n":
        print_typewriter("\nYou return to the hallway\n")
        hallway()
    else:
        print_typewriter("\nInvalid Response\n")
        dining_hall()

def hallway():
    print_typewriter("\nYou have entered the hallway.\n")
    print_typewriter("\nThere is 4 doors and a staircase: \nOne to the kitchen, living room, dining hall, study and a staircase descending to the dungeon.\n")
    hallway_input = (input("Where would you like to go? ")).lower()
    if hallway_input == "dining hall":
        dining_hall()
    elif hallway_input == "living room" and inventory.count("sword") <1:
        living_room()
    elif hallway_input == "living room" and inventory.count("sword") > 0:
        print_typewriter("\nThere is nothing else to do in here");
        hallway()
    elif hallway_input == "kitchen":
        kitchen()
    elif hallway_input == "study":
        study()
    elif hallway_input == "dungeon":
        dungeon()
    elif hallway_input != "dungeon" or hallway_input != "kitchen" or hallway_input != "dining hall" or hallway_input != "study" or hallway_input != "living room" or hallway_input != "the dungeon" or hallway_input != "the study" or hallway_input != "the dining hall":
        print_typewriter("\nYou cannot go there!");
        hallway()
    else:
        print_typewriter("\nYou cannot go there!");
        hallway()

import time

def secret_room():
     global inventory
     if inventory.count("dungeon key") > 0:
         print_typewriter("\nYou already have the dungeon key!\n You don't need to come in here, go find your sister!")
         study()
     else:
         time_limit = 20 #set time to 20 secs
     print_typewriter("\nYou enter the dimly lit, cobweb infested room. \nYou're immidiately drawn to a bright light coming from a large see through box on a table in the middle of the room. \nIt's a large gold key - could be important.")
     print(f"\nPress 'F' to access the code panel. You will have {time_limit} seconds to enter the code")
     start_time = None
     while True:
       if start_time is None and input().upper() == "F":
           start_time = time.time()
           print_typewriter("\nTo your relief you notice a clue etched into the side of the panel. It says (200 + 40) * 20")
           print_typewriter("\nEnter the 4 digit code: ")
       elif start_time is not None:
         code_input = input()
         end_time = time.time() #get time after user enters code
         elapsed_time = end_time - start_time #calculate how look it takes user
         if code_input == "4800" and elapsed_time <= time_limit:
          print_typewriter("\nSuccess! You've accessed the key & pocketed it for later.")
          inventory.append("dungeon key")
          print("\nYou have taken the dungeon key\nYour inventory now consists of:", inventory)
          study()
         elif elapsed_time > time_limit:
          print_typewriter("\nToo long! You fall through a trap to your demise")
          player_death() #Death - back to start
         else:
          print_typewriter("\nBig mistake! You fall through a trap to your demise")
          player_death() #Death - back to start
         break

intro()