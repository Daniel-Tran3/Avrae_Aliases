!gvar edit 8b9a0003-7782-46ff-ae69-cc7451cedecb

name_dict = {"cram": "Cramming", "energy": "Energy Drink", "drink": "Energy Drink", "late": "Late Night Snack", "night": "Late Night Snack", "snack": "Late Night Snack", "open": "Open Notes", "notes": "Open Notes", "teacher": "Teacher's Pet", "pet": "Teacher's Pet", "are you sure": "Are You Sure You Want To Do That?", "you want to do that": "Are You Sure You Want To Do That?", "calculated": "Calculated Comedy Club", "comedy": "Calculated Comedy Club", "club": "Calculated Comedy Club", "giving": "Giving 110%", "110": "Giving 110%", "research": "Research Recall", "recall": "Research Recall", "careful": "Careful Planning", "planning": "Careful Planning", "seek": "Seek The Truth", "truth": "Seek The Truth", "science": "Science Rules!", "rules": "Science Rules!", "camaraderie": "Camaraderie Club"}
cost_dict = {"Cramming": 5, "Energy Drink": 5, "Late Night Snack": 5, "Open Notes": 3, "Student Gossip": 3, "Teacher's Pet": 4, "Are You Sure You Want To Do That?": 4, "Calculated Comedy Club": 4, "Giving 110%": 5, "Research Recall": 3, "Careful Planning": 3, "Seek The Truth": 4, "Science Rules!": 5, "Camaraderie Club": 5}


def get_name(input):
  if (input in name_dict.keys()):
    return name_dict[input]
  else:
    for name in cost_dict.keys():
      if (input.lower() == name.lower()):
        return name
  return input