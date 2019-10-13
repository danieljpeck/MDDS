label scene1_1:

    "I made it here I guess"

    show queequeg_reg at right
    with easeinright 

    # q being queequeg
    q "Do you want to stay with me?"

    # A menu
    # The menu here shows how to add a dialogue choice in the game
    # You can have many different answers to the same question
    # Not all dialogues need to have lasting effects
    # Sometimes having one just to have a different sentence come out of the asker is sufficient
    menu:

        # Here we are using the variable that tracks queequegs affection for the player
        # We are setting it higher as he is warmed up to our gung ho
        "Yes, I do":
            $ queequegCharm += 1
            jump stay

        "Of course not":
            jump dontStay

label stay:
    q "yay"
    jump stayAnyway

label dontStay:
    q "boo"
    jump stayAnyway

label stayAnyway:
    q "there are no other rooms so you are stuck"
    "dang it!"

    # Using the flag we set earlier.  These can be used to help support choices.
    # Over time if you support Queequeg in ways he wants to be supported, you will gain affection etc.
    # This is checking if we were nice earlier
    if queequegCharm >= 1:
        "Queequeg seems charmed"
        "Probably because I was nice before"
    else:
        "Queequeg seems mad"
        "Probably because I was mean before"
    "But maybe we will get on well"

return