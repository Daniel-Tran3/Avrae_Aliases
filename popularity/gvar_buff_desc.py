!gvar edit bac2cf89-d7fd-4b49-817d-be831ee2ba54

def get_desc(key):
  desc = {}
  desc["Cramming"] = "You gain expertise in one skill that you are already proficient in as you rush to learn something you never studied for."
  desc["Energy Drink"] = "Your speed increases by 5 feet for the mission."
  desc["Late Night Snack"] = "As a bonus action once on a mission you can eat a snack you prepared earlier and heal one Hit Die plus your con mod plus 1d4."
  desc["Open Notes"] = "You gain proficiency in one language, skill, tool, or weapon of your choice you’re not already proficient in as you piece together ideas of some new idea in your notes."
  desc["Student Gossip"] = "As an action once on a mission you can whisper a rumor about a person within five feet of you, rolling an Intimidation or Persuasion check against their Insight, and if the target rolls equal to or lower then they are Frightened by you for 1 minute."
  desc["Teacher's Pet"] = "Once on a mission when you fail an Intelligence, Wisdom, or Charisma check or save, then you can choose to succeed as your ability to become someone’s favorite gives you a bit of grace."
  desc["Are You Sure You Want To Do That?"] = "Once per mission as an action you can cast the Augury spell with no components."
  desc["Calculated Comedy Club"] = "Proficiency Bonus times per mission, you can gain advantage on a roll if you make a relevant C Club pun."
  return f"{desc[key]}" if key in desc.keys() else "Bad description key."