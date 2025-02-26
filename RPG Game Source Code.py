from colorama import Fore, Back
import time
import msvcrt
import random
import os

# sharpen weapon could have more responses, one type of each food item, oasis has cactus, #runes make you immune to those elements, buffer before exit after win or loss

def init():
    # repeated functions for uses in init
    def buffer():
        while msvcrt.kbhit():
            msvcrt.getch()

    def death():
        for char in "You Die... You had " + str(sum(key in Backpack for key in ['Forest Rune', 'Ice Rune', 'Desert Rune'])) + " rune(s), restart the game to play again.":
            print(Fore.RED, char, end='', sep='', flush=True)
            time.sleep(0.01)
        print(Fore.RESET)
        input()
        quit()

    global Health, Backpack, player_row, player_col, Boat_Deployed
    Health = 100
    Backpack = {}
    Boat_Deployed = 0

    # Define the starting position of the player
    player_row = 5
    player_col = 6

    def Altar():
        global Health, Backpack
        gameprint("Your location is : The Altar")
        if sum(key in Backpack for key in ['Forest Rune', 'Ice Rune', 'Desert Rune']) == 3:
            gameprint("As you take your final steps through the treacherous lava cavern, the intense heat threatens to "
                      "overwhelm you. The ground beneath your feet is slick with molten rock, and the air is thick with "
                      "noxious fumes. You see a massive figure looming ahead of you. Colossus...")
            time.sleep(5)
            weapon, damage = choose_item_from_backpack()
            if damage > 10 and Health >= 150:
                gameprint("With your " + weapon + " in hand, you approach the towering figure of Colossus, "
                          "ready to do battle. The ground shakes with each of its footsteps, but you stand your ground, "
                          "determined to emerge victorious. As Colossus charges towards you, you dodge its massive fists "
                          "and strike back with your weapon. The clang of metal on rock echoes through the air as you "
                          "trade blows with the giant creature. Despite its immense size and strength, you find openings "
                          "in Colossus's defenses and continue to strike it with your weapon. Bit by bit, you wear it "
                          "down, until finally it lets out a deafening roar and crumples to the ground, defeated.")
                gameprint("As you approach the altar in the magma cavern, you can feel the intense heat emanating "
                          "from the molten rock surrounding it. The altar itself is carved from a single block of "
                          "obsidian, and its surface is smooth and reflective. Etched into the obsidian are strange, "
                          "glowing symbols that seem to pulse with an otherworldly energy.")
                gameprint("You reflect on your journey, knowing you have truly become a hero in every sense of the word...")
                for char in "Congratulations, restart the game to play again.":
                    print(Fore.LIGHTGREEN_EX, char, end='', sep='', flush=True)
                    time.sleep(0.1)
                print(Fore.RESET)
                input()
                quit()
            else:
                gameprint("With your " + weapon + " in hand, you approach the towering figure of Colossus, "
                                                  "ready to do battle. The ground shakes with each of its footsteps, but you stand your ground, "
                                                  "determined to emerge victorious. As Colossus charges towards you, you dodge its massive fists "
                                                  "and strike back with your weapon. The clang of metal on rock echoes through the air as you "
                                                  "trade blows with the giant creature. Despite its immense size and strength, you find openings "
                                                  "in Colossus's defenses and continue to strike it with your weapon. "
                                                  "Suddenly he stops attacking and takes off as the ground begins to "
                                                  "shake, you fall through the ground and into a pool of magma.")
                death()
        else:
            gameprint("You need the three runes to attract Colossus...")

    def Lava_caverns():
        global Health, Backpack
        gameprint("Your location is : Magma Caverns")
        responses = ['As you make your way down the rocky path, you can feel the ground beneath you getting warmer and '
                     'warmer. You soon realize that you are walking on top of a massive underground volcano!',
                     'The heat is almost unbearable as you traverse through the dark, winding tunnels. You can hear the '
                     'roar of molten magma echoing off the cavern walls, and you see flickering red light ahead.',
                     'You catch a whiff of sulfur in the air, and your eyes begin to water. You must be getting close to '
                     'the heart of the volcano.']
        gameprint(random.choice(responses))
        Health -= 15
        gameprint("Health: " + str(Health))
        if Health <= 0:
            gameprint("You lose your footing and slip on a patch of loose gravel. You tumble down the rocky slope, "
                      "slamming into jagged rocks along the way. You come to a stop at the edge of a massive magma lake, "
                      "with no way to climb back up. The intense heat and toxic gases quickly overwhelm you, and you "
                      "lose consciousness as you fall into the chasm.")
            death()
        if random.randint(1, 2) == 1:
            interaction = random.randint(1, 2)
            if interaction == 1:
                gameprint(
                    "You hear a loud roar from somewhere deep within the cavern. Suddenly, a massive fire elemental "
                    "appears before you, blocking your path. \n"
                    "What would you like to do:\n"
                    "Attack : Fight the fire elemental with a weapon from your backpack.\n"
                    "Run : Try to run from the fire elemental.")
                while True:
                    buffer()
                    playeri = input(Fore.GREEN + (">")).upper()
                    if playeri == "ATTACK":
                        weapon, damage = choose_item_from_backpack()
                        if damage > 8:
                            gameprint("You step forward to confront the fire elemental. It shoots a jet of flame at you, but you manage to dodge it and strike back with your " + weapon + ". The fire elemental screams in pain and charges at you again. You jump out of the way and hit it again with your " + weapon + ". After a few more blows, the fire elemental disintegrates into a cloud of ash.")
                            break
                        else:
                            gameprint("You strike the fire elemental with your " + weapon + ", but it seems to have no effect on the creature. The fire elemental retaliates with a massive burst of flame, engulfing you in a raging inferno. You try to run, but the heat is too intense, and you collapse as your body is consumed by the flames.")
                            death()
                    elif playeri == "RUN":
                        if random.randint(1, 2) == 1:
                            gameprint("As you try to flee from the fire elemental, you trip and fall, giving the fire "
                                      "elemental the opportunity to strike. It shoots a jet of flame at you, "
                                      "and you try to dodge, but the intense heat still burns your skin. You crawl "
                                      "away, trying to get back on your feet as the fire elemental closes in on you. "
                                      "You manage to find a small crevice in the rock and squeeze yourself inside "
                                      "just as the elemental blasts a wave of fire in your direction. You wait in the "
                                      "cramped space for what feels like hours until you're sure the creature has "
                                      "moved on.")
                            break
                        else:
                            gameprint("You turn and run as fast as you can, dodging flames and leaping over lava "
                                      "flows. The fire elemental pursues you, but you manage to outmaneuver it and "
                                      "lose it in the maze-like tunnels. You think you're safe, but suddenly, "
                                      "you hear a deafening roar behind you. You turn around and see the fire "
                                      "elemental charging at you with incredible speed. You try to run, but it's too "
                                      "late. The creature catches up to you and engulfs you in a raging inferno. You "
                                      "scream in agony as your body is consumed by the flames.")
                            death()
            if interaction == 2:
                gameprint(
                    "You come across a group of adventurers who are resting and eating. They greet you "
                    "warmly and offer to share some of their supplies with you."
                    "What would you like to do:\n"
                    "Rest : Rest with the adventurers and restore your health to 200.\n"
                    "Ask : Ask the adventurers about any dangers or treasures in the area.\n"
                    "Pass : Nothing")

                while True:
                    buffer()
                    playeri = input(Fore.GREEN + (">")).upper()
                    if playeri == "REST":
                        Health = min(Health + 20, 100)
                        gameprint(
                            "You rest with the adventurers. You feel refreshed and rejuvenated.")
                        gameprint("Health: " + str(Health))
                        break
                    elif playeri == "ASK":
                        gameprint("They talk of an ancient altar hidden deep within the heart of the volcano. "
                                  "They say that the altar has the power to restore the runes that once protected the "
                                  "land, but it is heavily guarded Colossus, whose purpose is "
                                  "to prevent the runes from being restored, and can only be defeated with the Maul.")
                        break
                    elif playeri == "PASS":
                        gameprint("You do nothing.")
                        break
                    else:
                        gameprint("Please only input one of the above options.")

    def Ocean():
        global Boat_Deployed
        gameprint("Your location is : Ocean")
        print(str(player_col) + str(player_row))
        if "Boat" not in Backpack and Boat_Deployed == 0:
            if player_col == 15:
                gameprint("You are swimming in the ocean. You are cold, and going any deeper without a boat would be fatal.")
            else:
                gameprint("As you swim deeper into the water, you feel your strength starting to fade. The current "
                          "becomes stronger and you struggle to keep your head above water. Despite your best "
                          "efforts, the water pulls you down and you begin to sink. Panic sets in as you try to swim "
                          "to the surface, but your body is too weak. The last thing you remember is the sound of the "
                          "waves crashing around you before everything goes black.")
                death()
        if Boat_Deployed == 1:
            if player_col == 15:
                gameprint("You climb back into the boat.")
            else:
                gameprint("You row your boat through the vast expanse of the ocean.")
        if "Boat" in Backpack:
            gameprint("As you finally put the boat in the water, you feel a sense of accomplishment. You can see the "
                      "vast ocean in front of you, the waves crashing against the shore. You take a deep breath and "
                      "climb aboard, feeling the boat gently sway beneath you.")
            del Backpack["Boat"]
            Boat_Deployed = 1

    def Paradise_entrance():
        gameprint("Your location is : Paradise")
        gameprint("As you row your boat further into the endless ocean, the sun beats down upon you relentlessly, "
                  "making you feel parched and exhausted. Just as you begin to lose hope, you see something in the "
                  "distance - a glimmer of light reflecting off a shiny object. Curiosity piqued, you row harder "
                  "towards it, hoping to find something useful. As you draw closer, you realize that what you thought "
                  "was a shiny object is actually a stretch of pristine white sand beach that seems to stretch on "
                  "endlessly. You pull your boat onto the shore and take a few cautious steps forward, "
                  "your eyes drinking in the sight before you. Everywhere you look, you see clear blue skies, "
                  "emerald-green forests, and colorful flowers in bloom. You realize that you have stumbled upon a "
                  "paradise that has been untouched by the chaos and destruction of the apocalyptic world you left "
                  "behind. Overwhelmed with joy and relief, you drop to your knees and thank whatever gods may be "
                  "listening for guiding you to this safe haven. As you explore the island further, you realize that "
                  "this is where you can finally start over and rebuild a new life for yourself.")
        for char in "Congratulations, restart the game to play again.":
            print(Fore.LIGHTGREEN_EX, char, end='', sep='', flush=True)
            time.sleep(0.1)
        print(Fore.RESET)
        input()
        quit()

    def Beach():
        gameprint("Your location is : Beach")
        responses = ['You walk along the sandy beach, the salty breeze blowing through your hair.', 'You can hear the crashing of waves against the shore and the distant sound of seagulls.', 'The sun is shining brightly, making the water sparkle and the sand warm underfoot.']
        gameprint(random.choice(responses))

    def Bunker():
        gameprint("Your location is : Bunker")
        gameprint("As you're walking through the city, you come across a large metal door set into the side of a "
                  "building. It looks like it leads to some kind of underground bunker. The door is rusted and there "
                  "are no signs of recent use, but it might be worth investigating.\n"
                  "What would you like to do:\n"
                  "Open : Open the door and investigate\n"
                  "Pass : Nothing")
        while True:
            buffer()
            playeri = input(Fore.GREEN + (">")).upper()
            if playeri == "OPEN":
                if "War Hammer" not in Backpack and "Maul" not in Backpack:
                    gameprint("You try the handle, it's not locked. You push it open and step inside, your eyes adjusting "
                              "to the darkness. You can barely make"
                              "out the outlines of shelves and crates lining the walls. As you start to explore, "
                              "you come across a large wooden chest. You pry it open and inside, you find a gleaming "
                              "War Hammer. Its weight feels good in your hand, and you sense the power it holds. Your eyes "
                              "wander to the other side of the room, where you see a boat. The pieces are "
                              "neatly arranged and waiting to be put together. The sight fills you with hope; maybe "
                              "there's a way off of this island...")
                    if sum(key in Backpack for key in ['Forest Rune', 'Ice Rune', 'Desert Rune']) > 1:
                        Backpack['War Hammer'] = {'Damage': 9}
                        gameprint("You add the War Hammer to your backpack")
                    else:
                        gameprint("You try to pick up the War Hammer, but do not possess the necessary runes to wield "
                                  "this item.")
                else:
                    gameprint("You try the handle, it's not locked. You push it open and step inside, your eyes "
                              "adjusting to the darkness. You can barely make out the outlines of shelves and crates "
                              "lining the walls.")
                if "Boat" not in Backpack and Boat_Deployed == 0:
                    gameprint("What would you like to do:\n"
                     "Take : Take the boat to the ocean (Be warned, carrying such a heavy object will drain your health fast)\n"
                     "Pass : Nothing")
                    while True:
                        buffer()
                        playeri = input(Fore.GREEN + (">")).upper()
                        if playeri == "TAKE":
                            Backpack['Boat'] = {'Amount':1}
                            gameprint("As you hoist the heavy boat onto your shoulders, you feel the weight bearing down "
                                      "on you. It's difficult to move and you have to constantly readjust.")
                            break
                        elif playeri == "PASS":
                            gameprint("You do nothing.")
                            break
                        else:
                            gameprint("Please only input one of the above options.")

                elif playeri == "PASS":
                    gameprint("You do nothing.")
                    break
                else:
                    gameprint("Please only input one of the above options.")

    def Abandoned_city_streets():
        global Health
        gameprint("Your location is : Abandoned City")
        responses = ["As you walk through the empty streets, the wind howls through the broken windows of the abandoned"
                  " buildings, sending shivers down your spine.", 'As you make your way down a quiet alleyway, '
                  "you suddenly hear the sound of footsteps behind you. You spin around, but there's nobody there. "
                  "Your heart racing, you continue on your way.", 'A sudden gust of wind blows a piece of paper '
                                                                  'against your leg. You pick it up and see that it '
                                                                  'is an old newspaper, dated several years ago. The '
                                                                  'headline reads "City Plunged Into Darkness".',
        "As you wander through the deserted streets, you can't shake the feeling that you're being watched. Every "
        "shadow seems to hold a hidden danger, and you find yourself looking over your shoulder at every turn."]
        gameprint(random.choice(responses))
        if random.randint(1, 2) == 1:
            interaction = random.randint(1, 3)
            if interaction > 1:
                Health -= 40
                if sum(key in Backpack for key in ['Forest Rune', 'Ice Rune', 'Desert Rune']) > 1 and Health > 40:
                    gameprint("As you're walking down the deserted streets, you suddenly hear a loud bang and feel a "
                              "sharp pain in your side. You look down and see blood seeping through your shirt. You "
                              "stumble and fall to the ground, struggling to stay conscious. You hear footsteps "
                              "approaching and see a group of raiders surrounding you. They search through your "
                              "backpack and they see the runes... Their expressions turn "
                              "from triumph to fear as they recognize the symbols etched onto the stones. They drop the"
                              " runes and quickly retreat, leaving you alone on the cold, empty streets.")
                    gameprint("Health: " + str(Health))
                else:
                    gameprint('''As you're walking down the deserted streets, you suddenly hear a loud bang and feel 
a sharp pain in your side. You look down and see blood seeping through your shirt. You stumble 
and fall to the ground, struggling to stay conscious. You hear footsteps approaching and see a 
group of raiders surrounding you. One of them leans down and sneers, "Looks like we got 
ourselves another victim. The bandits rifle through your backpack, 
taking everything of value, and then leave you lying there. Your vision blurs and fades, 
and the sounds of the city around you fade away into an eerie silence. You feel a sense of 
coldness spreading through your body, as if the life is draining out of you. You try to muster 
the strength to get up, but it's no use. Your body is limp, and you know that your 
time is running out. You close your eyes, resigned to your fate, as darkness engulfs you.''')
                    death()
            if interaction == 1:
                food = ['Tin Spaghetti', 'Preserved Tuna', 'Canned Baked Beans', 'Granola Bar', 'Crackers']
                food_not_in_backpack = [item for item in food if item not in Backpack] # item in 'food' not in backpack
                if food_not_in_backpack:
                    food_found = random.choice(food_not_in_backpack)
                    Backpack[food_found] = {'Health': 10}
                    gameprint("You walk down the abandoned street, the cracked pavement crunching under your feet. As "
                              "you turn a corner, you spot something on the ground: " + food_found + ". You "
                              "approach cautiously, scanning the area for any signs of danger. When you determine "
                              "that the coast is clear, you bend down and pick it up. You continue your "
                              "journey, feeling a bit more prepared for the challenges that lie ahead.")
                else:
                    gameprint("You find more food by the side of the street, but your backpack is already filled with "
                              "a variety of snacks that you've collected here. It seems like you'll have to make do "
                              "with what you have for now.")

    def Underworld_entrance():
        global Health
        gameprint("Your location is : Sandstone Chasm")
        if "Desert Rune" not in Backpack:
            gameprint("As you wander through the desert, your foot suddenly slips, and you find yourself teetering on the "
                      "edge of a deep ravine. The walls of the chasm are jagged and rough, and you can feel the heat "
                      "rising up from below. Looking down, you see nothing but darkness, and the sound of rushing air "
                      "echoes back up to you. Suddenly, you notice a strange flicker coming from somewhere far below. "
                      "It's impossible to tell what could be causing it.\n"
                      "What would you like to do:\n"
                      "Enter : Climb down the ravine\n"
                      "Pass : Nothing")
            while True:
                buffer()
                playeri = input(Fore.GREEN + (">")).upper()
                if playeri == "ENTER":
                    Health -= 30
                    if Health <= 0:
                        gameprint("As you begin to descend the ravine, you find that it's steeper than you initially "
                                  "thought. The rocks under your feet are loose and slippery, and you have to be careful "
                                  "not to lose your footing. Your heart is pounding as you inch your way down, "
                                  "one step at a time. The walls of the ravine loom high above you, casting deep shadows. "
                                  "The flicker you saw from above is still visible. As you get closer to the bottom, you feel that the "
                                  "walls of the ravine are jagged and uneven. Your hands are raw from gripping the rough "
                                  "rocks, and suddenly, you feel the rocks beneath your feet shift and give way. You "
                                  "try to grab onto something to stop your fall, but it's too late. You lose your "
                                  "footing and plummet to your demise.")
                        death()
                    else:
                        gameprint("As you begin to descend the ravine, you find that it's steeper than you initially "
                                  "thought. The rocks under your feet are loose and slippery, and you have to be careful "
                                  "not to lose your footing. Your heart is pounding as you inch your way down, "
                                  "one step at a time. The walls of the ravine loom high above you, casting deep shadows. "
                                  "The flicker you saw from above is still visible. As you get closer to the bottom, you feel that the "
                                  "walls of the ravine are jagged and uneven. Your hands are raw from gripping the rough "
                                  "rocks, and your legs ache from the strain of keeping your balance. Finally, "
                                  "you make it to the bottom of the ravine. As your eyes adjust to the dim light, "
                                  "you notice that the flicker is a faint yellow glow coming from somewhere in the distance. You can feel "
                                  "the warmth emanating from the source, and it seems to be drawing you closer. You "
                                  "carefully make your way towards the light, taking care not to trip on the uneven "
                                  "ground. After a few minutes of walking, you finally reach the source of the glow. "
                                  "It appears to be a small, glowing crystal embedded in the sandstone.")
                        weapon, damage = choose_item_from_backpack()
                        if damage > 7:
                            Backpack['Desert Rune'] = {'Amount': 1}
                            gameprint("You take out your trusty " + weapon + "and begin to pry the rune from the "
                                                                              "sandstone. It takes some effort, "
                                                                              "but eventually, with a satisfying "
                                                                              "snap, the rune comes loose from the "
                                                                              "sandstone.")
                            gameprint("You begin to climb back up the steep walls of the ravine, you feel a sense "
                                      "of accomplishment for having made it down to the bottom and retrieved the "
                                      "desert rune. The climb back up is arduous and requires a lot of effort, "
                                      "but you are determined to make it back to the top. Your hands grip the rough "
                                      "sandstone walls, and your feet find small footholds to push off from as you "
                                      "make your ascent. The sun beats down on you, but you keep going. Finally, "
                                      "after what feels like hours of climbing, you make it back to the top of the "
                                      "ravine. The experience has taken a toll on you. You feel exhausted and weak, "
                                      "and your vision blurs as you stumble forward.")
                            gameprint("Health: " + str(Health))
                        else:
                            gameprint("You heave with all your might but to no avail. It appears that your " + weapon + " is/are not strong enough to harvest this rune.")
                            gameprint("You begin to climb back up the steep walls of the ravine, you feel a sense "
                                      "of accomplishment for having made it down to the bottom and retrieved the "
                                      "desert rune. The climb back up is arduous and requires a lot of effort, "
                                      "but you are determined to make it back to the top. Your hands grip the rough "
                                      "sandstone walls, and your feet find small footholds to push off from as you "
                                      "make your ascent. The sun beats down on you, but you keep going. Finally, "
                                      "after what feels like hours of climbing, you make it back to the top of the "
                                      "ravine. The experience has taken a toll on you. You feel exhausted and weak, "
                                      "and your vision blurs as you stumble forward.")
                            gameprint("Health: " + str(Health))

                elif playeri == "PASS":
                    gameprint("You do nothing.")
                    break
                else:
                    gameprint("Please only input one of the above options.")
        else:
            gameprint("You have a strong memory of your time here in the past.")

    def Desert_wasteland():
        global Health
        gameprint("Your location is : Desert")
        interaction = random.randint(1, 6)
        if interaction == 1:
            gameprint("As you walk through the hot, sandy desert, you feel your throat becoming parched and your skin "
                      "burning under the relentless sun. You feel dehydrated and weak.")
            Health -= 5
            gameprint("Health: " + str(Health))
        elif interaction == 2:
            gameprint("Suddenly, you feel a faint vibration from beneath the sand. Before you know it, "
                      "a group of sand worms burst out from the ground and bite your leg. You manage to squash them "
                      "before they do any more damage.")
            Health -= 10
            gameprint("Health: " + str(Health))
        elif interaction == 4:
            gameprint("The harsh desert winds are starting to kick up, making it difficult to see and breathe. The sand whips up and stings your eyes and skin.")
            Health -= 10
            gameprint("Health:" + str(Health))
        elif interaction == 5:
            gameprint("You come across an oasis, surrounded by palm trees and a sparkling pool of water.\n"
                      "What would you like to do:\n"
                      "Rest : Get some rest and restore some health\n"
                      "Pass : Nothing")
            while True:
                buffer()
                playeri = input(Fore.GREEN + (">")).upper()
                if playeri == "REST":
                    Health += 15
                    gameprint("You get some rest, some of your health is restored to " + str(Health))
                    break
                elif playeri == "PASS":
                    gameprint("You do nothing.")
                    break
                else:
                    gameprint("Please only input one of the above options.")
        elif interaction == 6:
            gameprint("you hear a strange rustling sound behind you. You turn around and see a mummy, its bandages "
                      "flapping in the hot wind, shambling towards you with slow but determined steps. The mummy "
                      "raises its arms and lets out a menacing groan, clearly intent on attacking you.")
            weapon, damage = choose_item_from_backpack()
            if damage > 4:
                gameprint("You draw your " + weapon +
                      " and prepare to fight the undead creature. The mummy lashes out with a bronze, "
                      "curved sword,"
                      "but you manage to dodge its blows and strike back with a well-placed attack. The bandages "
                      "start to unravel, and the mummy emits a high-pitched scream as it crumbles into a pile of dust,"
                      "leaving nothing but its weapon lying on the ground.")
                if not any('Khopesh' in d for d in Backpack):
                    Backpack['Khopesh'] = {'Damage': 6}
                    gameprint("You add this weapon, a khopesh, to your backpack")
            else:
                gameprint("You draw your " + weapon +
                          " and prepare to fight the undead creature. The mummy lashes out with a bronze, "
                          "curved sword and hits stabs you in the face. You fall to the ground, pain overwhelming you.")
                death()
        elif interaction == 3:
            gameprint("In the distance, you see a group of bandits approaching. They demand that you hand over all "
                      "your valuables, or else face their wrath.\nWhat would you like to do:\n"
                      "Attack : Fight the bandits.\n"
                      "Handover : hand over a weapon from your backpack to the bandits.")
            while True:
                buffer()
                playeri = input(Fore.GREEN + (">")).upper()
                if playeri == "ATTACK":
                    weapon, damage = choose_item_from_backpack()
                    if damage > 6:
                        gameprint("As you draw your " + weapon + ", the bandits ready themselves for a fight. The leader "
                                  "steps forward, brandishing his own sword. You lock eyes and begin to circle each "
                                  "other warily. Suddenly, he lunges at you with his blade, but you parry the attack "
                                  "and counter with a quick jab. The other bandits move in to surround you, "
                                  "but you dodge their blows and strike back with a fierce combo. The fight "
                                  "rages on, with you and the bandits trading blows back and forth. Despite their "
                                  "numbers, you remain focused and determined. Finally, after what seems like an "
                                  "eternity, the bandits flee and leave you standing alone in the desert.")
                        break
                    else:
                        gameprint("As you draw your " + weapon + ", the bandits ready themselves for a fight. The leader "
                                  "steps forward, brandishing his own sword. You lock eyes and begin to circle each "
                                  "other warily. You fiercely battle the bandits, but their numbers and superior "
                                  "weapons prove to be too much. As you fight valiantly, you start to feel your "
                                  "strength fading, and eventually, you fall to the ground with a searing pain in "
                                  "your chest. You look up to see the bandits standing over you, laughing. They take "
                                  "your belongings and leave.")
                        death()
                elif playeri == "HANDOVER":
                        weapon, damage = choose_item_from_backpack()
                        if weapon == "Fists":
                            gameprint("As the bandits surround you, demanding that you hand over your valuables, "
                                      "you begin to search your backpack frantically, hoping to find something to "
                                      "give them. But as you dig through your belongings, you realize that you don't "
                                      "have anything of value to offer. The bandits grow impatient, and before you "
                                      "know it, they attack. You try to defend yourself, but it's no use. Overpowered "
                                      "and outnumbered, you fall to the ground with a searing pain in your chest.")
                            death()
                        else:
                            del Backpack[weapon]
                            gameprint("The bandits greedily snatch your " + weapon + " from your hands, inspecting it "
                                                                                    "with gleeful grins on their "
                                                                                    "faces. Satisfied with their new "
                                                                                    "acquisition, they give you one "
                                                                                    "last menacing look before "
                                                                                    "scurrying back further into the "
                                                                                    "desert.")
                            break
                else:
                    gameprint("Please only input one of the above options.")
        if Health <= 0:
            gameprint("You feel the scorching heat of the desert taking its toll on your body. As you stumble and "
                      "fall to the ground, you realize that you have pushed yourself too hard. The blinding sun and "
                      "the endless sand surround you as your vision fades to black. Your journey has come to an end.")
            death()

    def Ice_temple():
        gameprint("Your location is : Ice Temple")
        if "Ice Rune" not in Backpack:
            gameprint("The floor is slippery with ice, making it difficult to walk. As you make your way deeper into "
                      "the temple, you see a faint blue glow emanating from the walls. As you approach the source of "
                      "the glow, you find a pedestal made of ice. ingrained in the pedestal sits a rune, carved from "
                      "a mysterious blue crystal.")
            weapon, damage = choose_item_from_backpack()
            if damage > 6:
                Backpack["Ice Rune"] = {'Amount': 1}
                gameprint("You approach the pedestal and examine the ice rune carefully. As you touch it, you feel a "
                          "cold energy flowing through your body. You decide to pry it out and after a few attempts, "
                          "the rune finally comes off the pedestal. Suddenly, the temperature in the room drops and "
                          "you feel a chill run down your spine. You quickly grab the rune and start making your way "
                          "out of the temple before the ceiling and walls behind you give way. As you leave the temple"
                          ", you feel a sense of relief.")
            else:
                gameprint("You heave with all your might but to no avail. It appears that your " + weapon + " is/are not strong enough to harvest this rune.")
        else:
            gameprint("You stare at the collapsed temple.")

    def Mountain_range():
        global Health
        gameprint("Your location is : Mountain Range")
        responses = ['You trudge through the snow, feeling the icy wind bite at your face. You can barely see '
                     'anything beyond the swirling white, but you know that danger lurks in these mountains.',
                     'Your breath comes out in clouds as you traverse the mountains. Your fingers and toes are numb, '
                     'and you can feel your strength ebbing away.',
                     'You hear a rumble in the distance. You look up and see an avalanche falling somewhere in the '
                     'distance.']
        gameprint(random.choice(responses))
        Health -= 10
        gameprint("Health: " + str(Health))
        if Health <= 0:
            gameprint("You come across a frozen lake, its surface glittering. But as you step onto the ice, you hear "
                      "it crack beneath your feet. You fall through. The shock of the cold makes it hard to move your "
                      "limbs, and you struggle to stay afloat. Despite your best efforts, your strength fades, "
                      "and you slip beneath the surface. Your vision blurs, and darkness engulfs you as you succumb "
                      "to the frozen water.")
            death()
        if random.randint(1, 3) == 1:
            interaction = random.randint(1, 2)
            if interaction == 1:
                gameprint(
                    "You catch a glimpse of something moving in the distance. As it gets closer, you realize it's a massive yeti.\n"
                    "What would you like to do:\n"
                    "Attack : Fight the yeti with a weapon from your backpack.\n"
                    "Run : Try to outrun the yeti")
                while True:
                    buffer()
                    playeri = input(Fore.GREEN + (">")).upper()
                    if playeri == "ATTACK":
                        weapon, damage = choose_item_from_backpack()
                        if damage > 5:
                            gameprint("You step forward to confront the yeti. It roars and swings its massive arm at "
                                      "you. You dodge to the side and slash at the yeti with your sword. It snarls "
                                      "and charges at you again. You brace yourself and thrust your sword forward as "
                                      "the yeti charges. It impales itself on your blade and roars in pain. As the "
                                      "yeti falls to the ground, you feel a sense of relief and triumph.")
                            if 'Yeti Steak' not in Backpack:
                                Backpack['Yeti Steak'] = {'Health': 20}
                                gameprint("You add 'Yeti Steak' to your backpack.")
                            break
                        else:
                            gameprint("")
                            death()
                    elif playeri == "RUN":
                        if random.randint(1, 2) == 1:
                            gameprint("As you turn to run, your heart pounding in your chest, the yeti roars in "
                                      "frustration behind you. You sprint back through the path you came, not daring "
                                      "to look"
                                      "back, until you're sure you've put enough distance between you and the "
                                      "monster. As you catch your breath, you realize you narrowly escaped a terrible "
                                      "fate. But you know that you can't rest easy, as the yeti could be lurking just "
                                      "around the next bend.")
                            break
                        else:
                            gameprint("As you try to run from the yeti, your heart races with fear and "
                                      "adrenaline. The yeti's massive strides easily "
                                      "catch up to you, and it grabs you with its giant claws. You struggles "
                                      "to break free, but it's no use. The yeti's grip tightens, and you feel "
                                      "the icy breath of the beast on your face. With a final roar, "
                                      "the yeti finishes you off.")
                            death()

                    else:
                        gameprint("Please only input one of the above options.")
            if interaction == 2:
                gameprint("As you journey through the cold, you come across a small cave. As "
                          "you walk closer, you see a survivor inside working at a forge, sparks flying from his "
                          "hammer as"
                          "he sharpens a sword. He looks up and sees you, and beckons you over.\n"
                          '''"Hello there, traveler," he says with a smile. "I am a swordsmith, and I noticed your weapon could use some sharpening. I'd be happy to do it for you."\n'''
                          "What would you like to do:\n"
                          "Sharpen : Let the swordsmith sharpen one of your weapons\n"
                          "Pass : Nothing")
                while True:
                    buffer()
                    playeri = input(Fore.GREEN + (">")).upper()
                    if playeri == "SHARPEN":
                        weapon, damage = choose_item_from_backpack()
                        if weapon == "Stick":
                            del Backpack['Stick']
                            Backpack['Spear'] = {'Damage': 2}
                            gameprint("You sharpen your " + weapon + ". It looks much better now.")
                            break
                        elif weapon == "Rusty Sword":
                            del Backpack['Rusty Sword']
                            Backpack['Shiny Sword'] = {'Damage': 7}
                            gameprint("You sharpen your " + weapon + ". It looks much better now.")
                            break
                        elif weapon == "Khopesh":
                            del Backpack['Khopesh']
                            Backpack['Blade of the Desert King'] = {'Damage': 8}
                            gameprint("You sharpen your " + weapon + ". It looks much better now.")
                            break
                        elif weapon == "Rusty Sword":
                            del Backpack['War Hammer']
                            Backpack['Maul'] = {'Damage': 11}
                            gameprint("You sharpen your " + weapon + ". It looks much better now.")
                            break
                        elif weapon == "Fists":
                            break
                        else:
                            gameprint("This weapon cannot be sharpened.")
                            break
                    elif playeri == "PASS":
                        gameprint("You do nothing.")
                        break
                    else:
                        gameprint("Please only input one of the above options.")

    def Forest():
        global Health, Backpack
        gameprint("Your location is : Forest")
        responses = ['The forest is dense and dark, with towering trees blocking out much of the sunlight.', 'You notice the ground is covered in a thick layer of pine needles.', 'The forest is home to all manner of creatures, from small rodents to giant bears and wolves.', "The trees are so close together that it's difficult to see more than a few feet in any direction."]
        gameprint(random.choice(responses))
        Health -= 5
        gameprint("The forest takes a toll on your health: " + str(Health))
        if Health <= 0:
            gameprint("Your body weak and your mind clouded, you collapse to the ground, unable to move. Your last breath is drawn as you lay there, the sounds of the forest fading into silence around you.")
            death()
        if random.randint(1, 3) == 1:
            interaction = random.randint(1, 2)
            if interaction == 1:
                gameprint("You step on something crunchy, you have found a skeleton lying beneath you. It has a rusty sword\n"
                          "What would you like to do:\n"
                          "Pickup : Pickup the rusty sword\n"
                          "Pass : Nothing")
                while True:
                    buffer()
                    playeri = input(Fore.GREEN + (">")).upper()
                    if playeri == "PICKUP":
                        if not any('Rusty Sword' in d for d in Backpack):
                            Backpack['Rusty Sword'] = {'Damage': 5}
                            gameprint("You add a Rusty Sword to your backpack")
                        else:
                            gameprint("You already have this in your backpack.")
                        break
                    elif playeri == "PASS":
                        gameprint("You do nothing.")
                        break
                    else:
                        gameprint("Please only input one of the above options.")
            if interaction == 2:
                gameprint(
                    "A fierce howl echoes through the woods... A massive wolf charges towards you with bared teeth and glowing eyes.\n"
                    "What would you like to do:\n"
                    "Attack : Fight the wolf with a weapon from your backpack.\n"
                    "Run : Try to outrun the wolf")
                while True:
                    buffer()
                    playeri = input(Fore.GREEN + (">")).upper()
                    if playeri == "ATTACK":
                        weapon, damage = choose_item_from_backpack()
                        if weapon == "Fists":
                            gameprint("You try to dodge, but the wolf is too quick, it’s jaws clamp down on your arm "
                                      "drawing blood. You wrench your arm free, but the wolf has worked its jaws up "
                                      "to your neck. The wolf delivers a fatal blow.")
                            death()
                        else:
                            gameprint("You quickly draw the " + weapon + " and brace yourself for the impending attack. The "
                                      "wolf lunges at you with lightning speed, but you manage to dodge right, "
                                      "and counter with a swift blow... The wolf goes limp and collapses onto the "
                                      "forest floor.")
                            if 'Wild Dog Delight' not in Backpack:
                                Backpack['Wild Dog Delight'] = {'Health': 10}
                                gameprint("You add 'Wild Dog Delight' to your backpack.")
                            break
                    elif playeri == "RUN":
                        gameprint("You start to run, heart pounding in your chest as the wolf gives chase. Your feet "
                                  "pound against the forest floor as you weave through the trees. You manage to keep "
                                  "your pace steady and your movements fluid. After summoning all your strength, "
                                  "you finally outrun the wolf.")
                        break
                    else:
                        gameprint("Please only input one of the above options.")

    def Forest_heart():
        gameprint("Your location is : Forest Clearing")
        if "Forest Rune" not in Backpack:
            gameprint("As you wander into the heart of the forest, you stumble across a clearing and see a pulsing "
                      "green rock. As you approach it, you realise that it's a legendary rune, one of the three "
                      "powerful artifacts scattered across the land.")
            weapon, damage = choose_item_from_backpack()
            if damage > 4:
                Backpack['Forest Rune'] = {'Amount': 1}
                gameprint("You heave with all your might, your " + weapon + " pops the rune out of the rock. A blinding light surrounds you, and as it fades away you find yourself holding a small glowing rune in your hand. You don't know exactly what it does, but you sense that it's important. You tuck the rune safely into your backpack and continue on...")
            else:
                gameprint("You heave with all your might but to no avail. It appears that your " + weapon + " is/are not strong enough to harvest this.")
        else:
            gameprint("You walk back into the clearing where you harvested the Forest Rune.")

    def Backyard():
        gameprint("Your location is : Backyard")
        gameprint("The backyard is a cozy retreat, with lush grass, fragrant flowers, and a towering oak tree "
                  "providing shade and privacy.")

    def Road():
        gameprint("Your location is : Road")
        gameprint("The road stretches far east.")

    def Park():
        global Backpack, Health
        gameprint("Your location is : Park")
        responses = ['The sun is shining and a gentle breeze is blowing through the trees.', 'You can hear birds chirping in the distance.', 'You are surrounded by verdant foliage and the gentle rustling of leaves.', "You notice the well-manicured lawns and colorful flower beds."]
        gameprint(random.choice(responses))
        if random.randint(1, 3) == 1:
            if random.randint(1, 2) == 1:
                gameprint("You found a stick, what would you like to do:\n"
                          "Pickup : Pickup the stick\n"
                          "Pass : Nothing")
                while True:
                    buffer()
                    playeri = input(Fore.GREEN + (">")).upper()
                    if playeri == "PICKUP":
                        if not any('Stick' in d for d in Backpack):
                            Backpack['Stick'] = {'Damage': 2}
                            gameprint("You add a stick to your backpack")
                        else:
                            gameprint("You already have a stick in your backpack.")
                        break
                    elif playeri == "PASS":
                        gameprint("You do nothing.")
                        break
                    else:
                        gameprint("Please only input one of the above options.")
            else:
                gameprint("You see a rabbit, what would you like to do:\n"
                          "Attack : Attack the rabbit\n"
                          "Pass : Nothing")
                while True:
                    buffer()
                    playeri = input(Fore.GREEN + (">")).upper()
                    if playeri == "ATTACK":
                        if 'Rabbit Terrine' not in Backpack:
                            Backpack['Rabbit Terrine'] = {'Health': 5}
                            gameprint("You successfully hunt the rabbit and add 'Rabbit Terrine' to your backpack.")
                        else:
                            gameprint("You successfully hunt the rabbit.")
                        break
                    elif playeri == "PASS":
                        gameprint("You do nothing.")
                        break
                    else:
                        gameprint("Please only input one of the above options.")

    def Home():
        gameprint("Your location is : Home")
        gameprint("You are in the center of your home. \n"
                  "What would you like to do:\n"
                  "Rest : Get some rest and restore your health to 100\n"
                  "Pass : Nothing")
        while True:
            global Health
            buffer()
            playeri = input(Fore.GREEN + (">")).upper()
            if playeri == "REST":
                Health = 100
                gameprint("You get some rest, your health is now " + str(Health) + '.')
                break
            elif playeri == "PASS":
                gameprint("You do nothing.")
                break
            else:
                gameprint("Please only input one of the above options.")

    # Define the map as a matrix
    global game_map
    game_map = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                ['*', Ice_temple, Mountain_range, Mountain_range, Mountain_range, Forest, Forest, Forest,
                 Forest_heart, Forest, Forest, Forest, Lava_caverns, Lava_caverns, Lava_caverns, Lava_caverns,
                 Lava_caverns, Lava_caverns, Altar, '*'],
                ['*', Mountain_range, Mountain_range, Mountain_range, Mountain_range, Forest, Forest, Forest, Forest,
                 Forest, Forest, Forest, Lava_caverns, Lava_caverns, Lava_caverns, Lava_caverns, Lava_caverns,
                 Lava_caverns, Lava_caverns, '*'],
                ['*', Mountain_range, Mountain_range, Mountain_range, Mountain_range, Forest, Forest, Forest, Forest,
                 Forest, Forest, Forest, Lava_caverns, Lava_caverns, Lava_caverns, Lava_caverns, Lava_caverns, Lava_caverns, Lava_caverns, '*'],
                ['*', Mountain_range, Mountain_range, Mountain_range, Mountain_range, Forest, Backyard, Forest, Forest,
                 Forest, Forest, Forest, Lava_caverns, Lava_caverns, Lava_caverns, Lava_caverns,
                 Lava_caverns, Lava_caverns, Lava_caverns, '*'],
                ['*', Mountain_range, Mountain_range, Mountain_range, Mountain_range, Forest, Home, Road, Road, Road,
                 Road, Road, '*', '*', '*', '*', '*', '*', '*', '*'],
                ['*', Desert_wasteland, Desert_wasteland, Desert_wasteland, Desert_wasteland, Desert_wasteland, Park,
                 Park, Park, Park, Park, Park, '*', '*', '*', '*', '*', '*', '*', '*'],
                ['*', Desert_wasteland, Desert_wasteland, Desert_wasteland, Desert_wasteland, Desert_wasteland, Park,
                 Park, Park, Park, Park, Park, Beach, Beach, Ocean, Ocean, Ocean, Ocean, Ocean, '*'],
                ['*', Desert_wasteland, Desert_wasteland, Desert_wasteland, Desert_wasteland, Desert_wasteland,
                 Abandoned_city_streets, Abandoned_city_streets, Abandoned_city_streets, Abandoned_city_streets, Abandoned_city_streets, Abandoned_city_streets, Beach,
                 Beach, Ocean, Ocean, Ocean, Ocean, Ocean, '*'],
                ['*', Underworld_entrance, Desert_wasteland, Desert_wasteland, Desert_wasteland, Desert_wasteland,
                 Abandoned_city_streets, Abandoned_city_streets, Abandoned_city_streets, Abandoned_city_streets, Abandoned_city_streets, Abandoned_city_streets,
                 Beach, Beach, Ocean, Ocean, Ocean, Ocean, Ocean, '*'],
                ['*', Desert_wasteland, Desert_wasteland, Desert_wasteland, Desert_wasteland, Desert_wasteland, Abandoned_city_streets,
                 Abandoned_city_streets, Abandoned_city_streets, Abandoned_city_streets, Abandoned_city_streets, Abandoned_city_streets, Beach, Beach, Ocean,
                 Ocean, Ocean, Ocean, Ocean, '*'],
                ['*', Desert_wasteland, Desert_wasteland, Desert_wasteland, Desert_wasteland, Desert_wasteland, Abandoned_city_streets,
                 Abandoned_city_streets, Abandoned_city_streets, Bunker, Abandoned_city_streets, Abandoned_city_streets, Beach, Beach, Ocean,
                 Ocean, Ocean, Ocean, Paradise_entrance, '*'],
                ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
                ]

init()

# move the player north
def move_north():
    global player_row
    if game_map[player_row - 1][player_col] != '*':
        player_row -= 1
        return True
    else:
        return False
# move the player south
def move_south():
    global player_row
    if game_map[player_row + 1][player_col] != '*':
        player_row += 1
        return True
    else:
        return False
# move the player west
def move_west():
    global player_col
    if game_map[player_row][player_col - 1] != '*':
        player_col -= 1
        return True
    else:
        return False
# move the player east
def move_east():
    global player_col
    if game_map[player_row][player_col + 1] != '*':
        player_col += 1
        return True
    else:
        return False
# nice printing
def gameprint(input):
    for char in input:
        print(Fore.CYAN, char, end='', sep='', flush=True)
        time.sleep(0.01)
    print(Fore.RESET)
# removes keystokes inputted during prints
def buffer():
    while msvcrt.kbhit():
        msvcrt.getch()
# allows the player to choose a weapon, food or drop something
def choose_item_from_backpack():
    global item_damage
    while True:
        items_with_damage = []
        for item in Backpack:
            if isinstance(Backpack[item], dict) and 'Damage' in Backpack[item]:
                items_with_damage.append(item)

        if not items_with_damage:
            gameprint("You don't have any items in your backpack that can cause damage.")
            return "Fists", 1
        else:
            gameprint("Choose an item from your backpack that can cause damage:")
            for i, item in enumerate(items_with_damage):
                gameprint(f"{i + 1} : {item}")
            buffer()
            playeri = input(Fore.GREEN + (">")).upper()
            if playeri.isdigit() and int(playeri) in range(1, len(items_with_damage) + 1):
                item_name = items_with_damage[int(playeri) - 1]
                item_damage = Backpack[item_name]['Damage']
                return item_name, item_damage
            else:
                gameprint("This input is not recognised, please only input one of the above responses.")
# use a healing item
def use():
    global item_health
    while True:
        items_with_health = []
        for item in Backpack:
            if isinstance(Backpack[item], dict) and 'Health' in Backpack[item]:
                items_with_health.append(item)

        if not items_with_health:
            gameprint("You don't have any items in your backpack that can restore health.")
            return "None", 0
        else:
            gameprint("Choose an item from your backpack that can restore health:")
            for i, item in enumerate(items_with_health):
                gameprint(f"{i + 1} : {item}")
            buffer()
            playeri = input(Fore.GREEN + (">")).upper()
            if playeri.isdigit() and int(playeri) in range(1, len(items_with_health) + 1):
                item_name = items_with_health[int(playeri) - 1]
                item_health = Backpack[item_name]['Health']
                return item_name, item_health
            else:
                gameprint("This input is not recognised, please only input one of the above responses.")
# drop an item
def drop():
    global Backpack
    if not Backpack:
        gameprint("You have nothing to drop.")
        return
    gameprint("Choose an item to drop:")
    for i, item in enumerate(Backpack):
        gameprint(f"{i + 1} : {item}")
    buffer()
    playeri = input(Fore.GREEN + (">")).upper()
    if playeri.isdigit() and int(playeri) in range(1, len(Backpack) + 1):
        item_name = list(Backpack.keys())[int(playeri) - 1]
        del Backpack[item_name]
        gameprint(f"You dropped {item_name}.")
    else:
        gameprint("This input is not recognised, please only input one of the above responses.")
# print_game_map function (thanks stackoverflow)
def print_game_map():
    global game_map, player_row, player_col
    location_names = {
        'Ice_temple': 'MT',
        'Mountain_range': 'MR',
        'Forest': 'FO',
        'Forest_heart': 'FH',
        'Lava_caverns': 'LC',
        'Altar': 'AL',
        'Backyard': 'BY',
        'Home': 'HM',
        'Road': 'RD',
        'Desert_wasteland': 'DE',
        'Park': 'PK',
        'Beach': 'BC',
        'Ocean': 'OC',
        'Abandoned_city_streets': 'AC',
        'Bunker': 'BU',
        'Underworld_entrance': 'SC',
        'Paradise_entrance': 'PA',
    }
    for row in range(len(game_map)):
        longest_in_row = max([len(location_names.get(str(item)[str(item).find(".", str(item).find(".") + 1) + 1:str(item).find(" at ")], '')) for item in game_map[row]])
        for col in range(len(game_map[0])):
            if row == player_row and col == player_col:
                print(Fore.GREEN + "{:<{}}".format("X", longest_in_row), end=' ')
            else:
                text = str(game_map[row][col])
                start = text.find(".", text.find(".") + 1) + 1
                end = text.find(" at ")
                location_name = text[start:end]
                short_name = location_names.get(location_name, location_name)
                print(Fore.CYAN + "{:<{}}".format(short_name, longest_in_row), end=' ')
        print()
# fancy red printing on death
def death():
    for char in "You Die... You had " + str(sum(key in Backpack for key in ['Forest Rune', 'Ice Rune',
                                                                            'Desert Rune'])) + " rune(s), restart the game to play again.":
        print(Fore.RED, char, end='', sep='', flush=True)
        time.sleep(0.01)
    print(Fore.RESET)
    input()
    quit()
# prints all commands, has own function because it is used multiple times
def help():

    helpstr = '''N : move north
E : move east
S : move south
W : move west
HEALTH : shows your health (you can have up to 200 Health)
USE : Use an item to restore your Health
BACKPACK : shows the items you have as well as their stats
DROP : drop an item from your backpack
HOME : tells you where home is
MAP : Shows the map'''
    gameprint(helpstr)
# handles player input
def parse(playeri):
    global Health
    if 'Boat' in Backpack:
        Health -= 25
        if Health <= 0:
            gameprint("As you struggle to carry the boat, your legs begin to wobble beneath you. You "
                      "stumble and try to regain your balance, but it's too late. The boat crushes down on your head.")
            death()
        else:
            gameprint("The boat on your back saps away at your strength")
            gameprint("Health: " + str(Health))
    playeri = playeri.upper()
    # NORTH EAST SOUTH WEST
    if playeri == "NORTH" or playeri == "N":
        if move_north() == True:
            gameprint("You move north.")
            # strange code that calls a function with the name of where the player is
            game_map[player_row][player_col]()
        else:
            gameprint("The terrain is too treacherous to move in this direction.")
    elif playeri == "EAST" or playeri == "E":
        if move_east() == True:
            gameprint("You move east.")
            game_map[player_row][player_col]()
        else:
            gameprint("The terrain is too treacherous to move in this direction.")
    elif playeri == "SOUTH" or playeri == "S":
        if move_south() == True:
            gameprint("You move south.")
            game_map[player_row][player_col]()
        else:
            gameprint("The terrain is too treacherous to move in this direction.")
    elif playeri == "WEST" or playeri == "W":
        if move_west() == True:
            gameprint("You move west.")
            game_map[player_row][player_col]()
        else:
            gameprint("The terrain is too treacherous to move in this direction.")
    # INV
    elif playeri == "INV":
        gameprint("You have : " + str(Backpack))
    # HEALTH
    elif playeri == "HEALTH":
        gameprint("Your health : " + str(Health))
    # HOME
    elif playeri == "HOME":
        home_row, home_col = 5, 6  # coordinates of home
        row_diff = home_row - player_row
        col_diff = home_col - player_col
        row_direction = 'north' if row_diff < 0 else 'south'
        col_direction = 'west' if col_diff < 0 else 'east'
        row_steps = abs(row_diff)
        col_steps = abs(col_diff)
        gameprint(f"Your home is {row_steps} step(s) {row_direction} and {col_steps} step(s) {col_direction} from here...")
    # BACKPACK
    elif playeri == "BACKPACK":
        if not Backpack:
            gameprint("Your backpack is empty.")
            return
        gameprint("Backpack contents:")
        for item in Backpack:
            gameprint(f"{item}:")
            for key, value in Backpack[item].items():
                gameprint(f"  {key}: {value}")
    # USE
    elif playeri == "USE":
        itemname, healthamount = use()
        Health += int(healthamount)
        if Health > 200:
            Health -= int(healthamount)
            gameprint("You cannot have more than 200 Health")
        else:
            if itemname != "None":
                del Backpack[itemname]
                gameprint("You consume " + str(itemname) + ", your health is now: " + str(Health))
    # DROP
    elif playeri == "DROP":
        drop()
    # MAP
    elif playeri == "MAP":
        print_game_map()
    # HELP
    elif playeri == "HELP":
        help()
    else:
        gameprint("This input is not recognised.")


# originally I had multiple files so I had init() but later I combined them
init()
# clear console
os.system('cls')
# introduction, for debugging I made it skippable
skip = 12
if skip != 1:
    starttext1 = 'You are a brave adventurer who must embark on a perilous journey to find the 3 ancient runes that will stop the evil Colossus from infecting the island.'
    starttext2 = 'Legend has it that the ancient runes were hidden safely to prevent evil forces from using them. But now, evil forces have risen once again, and the runes must be found and brought together in a powerful altar to restore peace and harmony to the island.'
    starttext3 = 'Your quest to find the 3 ancient runes will take you through treacherous landscapes, dark caverns, and mysterious temples. Along the way, you will encounter fierce monsters, cunning bandits, and food and weapons that will aid you on your journey. But be warned, the path to the runes is fraught with danger, and you will need all of your skills, wits, and courage to succeed.'
    starttext4 = 'Are you ready to accept the challenge and become the hero that the land so desperately needs?'
    starttext5 = ' The fate of the world rests in your hands'
    for char in starttext1:
        print(Fore.CYAN, char, end='', sep='', flush=True)
        time.sleep(0.01)
    print(Fore.RESET)
    buffer()
    input(Back.GREEN + "press enter to continue..." + Back.RESET)
    os.system('cls')
    for char in starttext2:
        print(Fore.CYAN, char, end='', sep='', flush=True)
        time.sleep(0.01)
    print(Fore.RESET)
    buffer()
    input(Back.GREEN + "press enter to continue..." + Back.RESET)
    os.system('cls')
    for char in starttext3:
        print(Fore.CYAN, char, end='', sep='', flush=True)
        time.sleep(0.01)
    print(Fore.RESET)
    buffer()
    input(Back.GREEN + "press enter to continue..." + Back.RESET)
    os.system('cls')
    for char in starttext4:
        print(Fore.CYAN, char, end='', sep='', flush=True)
        time.sleep(0.01)
    time.sleep(0.8)
    for char in starttext5:
        print(Fore.CYAN, char, end='', sep='', flush=True)
        time.sleep(0.01)
    time.sleep(0.4)
    for i in range(1, 4):
        print(".", end='', sep='', flush=True)
        time.sleep(0.4)
    print(Fore.RESET)
    buffer()
    input(Back.GREEN + "press enter to continue..." + Back.RESET)
    os.system('cls')

    welcome = '''Welcome, you are currently at the center of your house. You have 100 health and no runes... Your 
health is vital for your survival, take regular rests in your home and eat food to keep it as high as it can possibly be. You 
never know what you might encounter.
Remember the objective. Find the runes 3 runes and bring them to the 
powerful altar before it is too late.

The game commands are as follows:'''

    gameprint(welcome)
    help()
    gameprint("\nNote that other commands will become available to you along your journey."
                     "\nIf you ever need more help, input 'HELP'.")
# game loop
while True:
    buffer()
    parse(input(Fore.GREEN + (">")))