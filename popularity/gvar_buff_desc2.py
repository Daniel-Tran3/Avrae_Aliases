!gvar edit 7db1315a-b0ab-45d5-bd57-60b6dc90c353

def get_desc(key):
  desc = {}
  desc["Careful Planning"] = "Once per mission, you can ignore the cost of the material components of a spell worth up to 50 times your level."
  desc["Seek The Truth"] = "Once per mission can select a creature or an object as the subject of your investigation. If you select a creature, you gain advantage on Insight, Perception, and Survival checks made against that creature, as well as Deception, Intimidation, and Persuasion checks to gather information from your subject. If you choose an object, you have advantage on Intelligence checks to understand its function and use, as well as to learn information about the object, such as its history or significance."
  desc["Science Rules!"] = "You can use your reaction to mimic one of the following spells with a gadget: Absorb Elements, Feather Fall, or Shield. You can use this reaction a number of times on a mission equal to your proficiency bonus. You can not stack this ability with the spells that are being mimicked."
  desc["Camaraderie Club"] = "As a Bonus Action give an ally within 30 ft of you advantage on their next attack roll."
  return f"{desc[key]}" if key in desc.keys() else "Bad description 2 key."