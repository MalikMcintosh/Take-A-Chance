print('Welcome to everyone\'s favorite game, "Take A Chance At Life"!')
name = input('What is your name?: ')
gender = input('Are you a boy or a girl? (It really does not matter either way.): ')

print('Ok, ' + name + ', Let\'s begin!')
print('The rules are simple, we will giving you a choice on which setting you would like to live in. ')
print()
genre = input('Choose: Fantasy, Sci-Fi, Rom/Com, or Action')
if genre == 'action':
    print('This is the Action path.')
    actionRole = input('Would you like to be an Assassin, a Berserker, a Valkyrie, or a Treasure Hunter?');
    print('Guildsmate: Welcome ,'+ name + ',This is the Salem guilds headquarters. ')
    print('We recieved a requests today. It\'s for, Goblin slaying.')
    mission = input('Choose: Goblin');
    print('Alrighty then,' + mission + ',it is. Just sign your name here and be on your way.')
    if mission == 'goblin':
        print('Scene: Your walking down a dirt path towards the Calhamaji Mountain.')
        print('Please Help Me!!!!!')
        print('Narrator: Hmm it seems like someone requires urgent assistance. Will you help them or will you keep heading towards the mission?')
        choice1 = input('Save, Don\'t')
        if choice1 == 'save':
            print('I\'m coming to save you!')
            print('Please kind entity my caravan was attacked by a group of goblins.')
            print('they kidnapped my daughter you must help me get her back.')
            print('I am far too weak to retrieve her.')
            print('Narrator: You Sprinted towards the mountain at top speed.')
            print('Narrator: You have reached the mountains base entrance. There are two paths within the cave which way will you go left or right?')
            path = input('left, right')
            if path == 'left':
                print('Narrator: Aha you\'ve found the goblins dungeon.')
                print('The girl should be in one of the cells.')
                print('Whilst searching the cells you alerted the goblin horde and were torn to shreds.')
                print('Oof That\'s tuff luck right there.')
                print('You got the bad ending.')
            elif path == 'right':
                print('Narrator: Aha you have found the goblins nest.')
                print('If you are careful you may be able to slay most of them without setting off any alarms.')
                print('You manage to kill all but one goblin.')
                print('In fear for it\'s life it tells you where the kidnapped girl is.')
                print('After tearing the goblins head off you go towards the girls cage and release her.')
                print('Girl: Thank you so much esteemed hero I can finally return my mother.')
                print('Aye lad you have saved the child that was very heroic of you.')
                print('Gratzie you got the good ending.')

        elif choice1 == 'don\'t':
            print('Narrator: Ah so you choose the path of the coward.')
            print('Well im sure the lass will be fine.')
            print('You reach the entrance to the mountain')
            print('There are two paths within the cave which way will you go left or right?')
            path = input('left,right')
            if path == 'left':
                print('Aha you have found the goblins dungeon.')
                print('While searching the dungeon for any prisoners you are greeted by a horde of goblins.')
                print('They knock you out and strip you of your gear.')
                print('You are now trapped as their prisoner.')
                print('Prisoner ending achieved!')
            elif path == 'right':
                print('Narrator: Aha yo found the goblins nest. Though it doesn\'t seem that any are here.')
                print('You search the nest for any items and hear a crowd of goblins entering the cave.')
                print('You hide in a corner and wait for the goblins to fall asleep before you strike.')
                print('Nightfall comes and you make your move severing the heads of the goblins.')
                print('After your done you faintly hear the sobbing of a girl nearby.')
                print('You find this girl inside a cell within the goblins Dungeon and decide to release her.')
                print('You send her on her way without telling her your name and she goes on to tell the tale of her hero.')
                print('Unknown hero ending achieved')
elif genre == str('sci-fi'):
    print("Alright " + name + ". Here are the rules. Your story changes depending on what job you choose.")
    print(
        "You're aboard the Starship Destiny, flying through space. After the events of the Great War, all that's left of humanity live on this spaceship who's only job is to float around in space in a predetermined path.")
    print("As a technician, your job is to make sure the ship doesn't malfunction.")
    DecisionOne = input(
        "After years of peace, you hear what sounds like a scream coming from the control room. Do you go to invesigate it or not? (Type yes or no.)")
    if DecisionOne == str("yes"):
        print(
            "You stand up to go investigate. You've never heard a noise like that come out the control room before. Is something broken?")
        print(
            "The control room would usually buzz to life when you step inside it. But when you step inside, you see it's already been lit. That makes the sight of the blood puddle by the doorway all the more jarring.")
        print(
            "The screen comes from the corner of the room, and you race towards the sound. There sits a " + gender + ", rubbing at the wound on her stomach. She wears the same uniform as you, but most jarringly, she has your face.")
        DecisionTwo = input(
            "They look up at you, tears in their eyes, and beg for you help. Do you help them? (Type yes or no.)")
        if DecisionTwo == str("yes"):
            print(
                "You nod, and reach for them. You pull them up and place a hand over the wound, asking how that happened.")
            print(
                "They tell you that their father did it, their creator. You don't know what that could possibly mean, but you don't question it.")
            print(
                "You lift them up and walk them out out of the room. They're bleeding pretty bad, and you can't help but wonder what did this to them. Or how they were created. Or whatever the hell is going on.")
            print("'You take her back to your office, resting her against the desk. 'What should I do?' you ask.")
            DecisionThree = input("Their answer startles you. 'Kill me.' What do you say? (Type yes or no.)")
            if DecisionThree == str("yes"):
                print(
                    "'Thank you,' she responds, 'I'm in so much pain. My existence is a lie. I just wanted to meet you. My sister.")
                print(
                    "'But who made you? Who are you?' You ask, because you need to know before you grant her last wish.")
                print(
                    "My name was 4A. That was what he called me. The doctor. When I learned I was a copy, I wanted nothing more than to see you.")
                print(
                    "They place a shard of bloody broken glass in your hand. 'I used it to kill the doctor,' they say, 'But not before he got me. I want you to be the one.'")
                print(
                    "It's terrible, but you feel bad for her, and you want to oblidge. So you drag the shard of glass across her throat. It's messy, but quick, and they die with a smile on their face.")
                print("The story ends here.")
            if DecisionThree == str("no"):
                print("They frown, but don't move. 'Why won't you grant me my final wish?'")
                print(
                    "'I can't just kill you!' you answer, but she turns away. My name was 4A. That was what he called me. The doctor. When I learned I was a copy, I wanted nothing more than to see you.")
                print(
                    "'I killed him for you. But now...I wish I hadn't.' Her last words sting, but she dies before you get to answer her.")
                print("The story ends here.")
            if DecisionTwo == str("no"):
                print(
                    "They frown, anger flashing in their eyes. 'But we're family!' she howls, and lunges on top of you.")
                print(
                    "You try to push them off, but they're too fast. Too strong. Her teeth dig into your throat and you spend your last moments choking on your own blood.")
                print("The story ends here. You died.")
        elif DecisionOne == str("no"):
            print(
                "Oh well, you think, shrugging off the noise and going back to your computer. You type away, emailing the pilot that everything looks alright from the tech side.The scream suddenly gets louder though, and you finally turn around.")
            print(
                "There's a bald " + gender + " someone dressed like you, with your face, and that's the last thought you have before they lift their knife into the air and stab you in the chest.")
            print("The story ends here. You died.")
elif genre == str('Fantasy'):
    print()
elif genre == str('Rom/Com'):
    print()
