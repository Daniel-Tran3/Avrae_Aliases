!gvar edit 3ef2b289-b512-4267-839c-1abe61a60c8e

# This module manipulates buff stats

name_dict = {"cram": "Cramming", "energy": "Energy Drink", "drink": "Energy Drink", "late": "Late Night Snack", "night": "Late Night Snack", "snack": "Late Night Snack", "open": "Open Notes", "notes": "Open Notes", "teacher": "Teacher's Pet", "pet": "Teacher's Pet"}

cost_dict = {"Cramming": 5, "Energy Drink": 5, "Late Night Snack": 5, "Open Notes": 3, "Student Gossip": 3, "Teacher's Pet": 4}

def get_name(input):
  if (input in name_dict.keys()):
    return name_dict[input]
  else:
    for name in cost_dict.keys():
      if (input.lower() == name.lower()):
        return name
  return input
def get_cost(input):
  buff_name = get_name(input)
  if (buff_name in cost_dict.keys()):
    return cost_dict[buff_name]
  else:
    return 0
def buy(input):
  cost = int(get_cost(input))
  old_cred = int(get_uvar("u_cred", 0))
  old_pop = int(get_uvar("u_popularity", 0))
  new_cred = old_cred - cost
  new_pop = old_pop + cost
  set_uvar("u_cred", new_cred)
  set_uvar("u_popularity", new_pop)
def donate(donation):
  donation = int(donation)
  old_cred = int(get_uvar("u_cred", 0))
  old_pop = int(get_uvar("u_popularity", 0))
  new_cred = old_cred - donation
  new_pop = old_pop + donation
  set_uvar("u_cred", new_cred)
  set_uvar("u_popularity", new_pop)