label scene1_0:

    # Set initial scene/bg
    scene bg_tavern
    with fade

    # Custom name of character *hard* written in

    # A view with a person speaking has two aspects, the speaker name, and the text
    # To make one of these, simply have the first part be the name of who is speaking in quotes,
    # Then add the text after.
    "Innkeeper" "What was your name again?"

    # Using the i reference for Ishamel

    # If the character was declared in script.rpy, then you can use the reference shown there
    # i for Ishmael, a for Ahab, etc.
    i "Uh..."
    pause 3.0
    i "Call me Ishmael"

    # No speaker is treated as narrative or inner-monologue
    "I had just arrived at the spouter-inn.  It was the only place that possibly had room for me"

    # Transition in sprites/characters *with* some transition

    # Show *image name* at *location*
    # This method adds the sprites to the view
    # The With *something* is the transition, ease in, enter from right
    # things like that
    show queequeg_reg at right
    with easeinright

    q "I have a room"

    # similar to move characters out
    hide queequeg_reg at right
    with easeoutright

    "looks like I have a room"

    # Go to new scene
    # The jump *some label elsewhere* tells it where to go at the end of a scene
    # Scenes are pretty arbitrary, so it works as we define it, probably based on a scene.
    # Technically it is all one script
    jump scene1_1

