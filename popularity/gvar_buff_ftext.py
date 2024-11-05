!gvar edit 0f3535c1-1978-45a1-ac81-8cf589df8343

# This module generates buff flavortext.

def get_ftext(key):
  ftext = {}
  ftext["Cramming"] = "The 'due' date is the 'do' date!"
  ftext["Energy Drink"] = "If you drink two 5-hour-energy potions, do you have energy for 10 hours or 2x the energy for 5 hours?"
  ftext["Late Night Snack"] = "Hey, does anyone know what's open at midnight?"
  ftext["Open Notes"] = "And thank Teadara for the existence of cheat sheets."
  ftext["Student Gossip"] = "Okay, so this is kiiinda a secret, but Lovebug told me that Glamour said she overheard Tulip and Atorus talking about how Sylvia said..."
  ftext["Teacher's Pet"] = "I mean, some professors are really chill if you get to know them!"
  ftext["Are You Sure You Want To Do That?"] = "When the Mansion Manager gives you a way out, you take it."
  cc = "CC: Careful Consultatory Counselor's Council\n"
  cc += "Cheekily cheat! Cheerily celebrate! Collaboratively concoct! Craftily collude! Conveniently communicate! Cause chuckles!\n"
  cc += "Curious? Come courageously chase cavalcading club-created comedy!"
  ftext["Calculated Comedy Club"] = cc
  ftext["Giving 110%"] = "Push past your limits! Just one more rep!"
  ftext["Research Recall"] = "Hey, wait a minute! Wasn't the Science Club writing a paper on this?"
  ftext["Careful Planning"] = "Measure twice, cast once."
  ftext["Seek The Truth"] = "Nothing gets between a journalist and their scoop!"
  return f"{ftext[key]}" if key in ftext.keys() else "Bad ftext key."