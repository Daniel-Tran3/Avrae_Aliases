!gvar edit 3ef2b289-b512-4267-839c-1abe61a60c8e

# This module manipulates buff stats

cost_dict = {"Cramming": 5, "Energy Drink": 5, "Late Night Snack": 5, "Open Notes": 3, "Student Gossip": 3, "Teacher's Pet": 4, "Are You Sure You Want To Do That?": 4, "Calculated Comedy Club": 4, "Giving 110%": 5, "Research Recall": 3, "Careful Planning": 3, "Seek The Truth": 4}

def get_name(input):
  using(
    names="8b9a0003-7782-46ff-ae69-cc7451cedecb"
  )
  return names.get_name(input)
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