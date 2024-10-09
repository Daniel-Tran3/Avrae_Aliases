!gvar edit 712955e6-33c7-483c-8de8-a8db26b6530b

# This module generates buff flavortext.
desc = {"Cramming": "You gain expertise in one skill that you are already proficient in as you rush to learn something you never studied for.", "Energy Drink": "Your speed increases by 5 feet for the mission.", "Late Night Snack": "As a bonus action once on a mission you can eat a snack you prepared earlier and heal one Hit Die plus your con mod plus 1d4.", "Open Notes": "You gain proficiency in one language, skill, tool, or weapon of your choice you’re not already proficient in as you piece together ideas of some new idea in your notes.", "Student Gossip": "As an action once on a mission you can whisper a rumor about a person within five feet of you, rolling an Intimidation or Persuasion check against their Insight, and if the target rolls equal to or lower then they are Frightened by you for 1 minute.", "Teacher's Pet": "Once on a mission when you fail an Intelligence, Wisdom, or Charisma check or save, then you can choose to succeed as your ability to become someone’s favorite gives you a bit of grace."}

ftext = {"Cramming": "The 'due' date is the 'do' date!", "Energy Drink": "If you drink two 5-hour-energy potions, do you have energy for 10 hours or 2x the energy for 5 hours?", "Late Night Snack": "Hey, does anyone know what's open at midnight?", "Open Notes": "And thank Teadara for the existence of cheat sheets.", "Student Gossip": "Okay, so this is kiiinda a secret, but Lovebug told me that Glamour said she overheard Tulip and Atorus talking about how Sylvia said...", "Teacher's Pet": "I mean, some professors are really chill if you get to know them!"}

def get_desc(key):
    return f"{desc[key]}" if key in desc.keys() else "Bad description key."

def get_ftext(key):
    return f"{ftext[key]}" if key in ftext.keys() else "Bad ftext key."