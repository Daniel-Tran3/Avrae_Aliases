!gvar edit 418edcab-2b22-4a13-b0d5-8c064777aa5a

class_names = {"exp": "Expertise", "lang": "Language"}
retrain_names = {"battle": "Battle Master Maneuver", "battlemaster": "Battle Master Maneuver", "maneuver": "Battle Master Maneuver", "fighting": "Fighting Style", "style": "Fighting Style", "infusion": "Known Infusion", "pact": "Pact Boon", "boon": "Pact Boon"}

class_costs = {"Armor": 12, "Expertise": 24, "Language": 8, "Skill": 12, "Tool": 4, "Weapon": 4}
retrain_costs = {"Battle Master Maneuver": 3, "Class": 16, "Fighting Style": 4, "Invocation": 3, "Known Infusion": 3, "Metamagic": 3, "Pact Boon": 4, "Skill": 4, "Spell": 3, "Subclass": 12}

def get_name(utype, input):
  if (utype == "class"):
    if (input in class_names.keys()):
      return class_names[input]
    else:
      for name in class_costs.keys():
        if (input.lower() == name.lower()):
          return name
  else:
    if (input in retrain_names.keys()):
      return retrain_names[input]
    else:
      for name in retrain_costs.keys():
        if (input.lower() == name.lower()):
          return name
  return input
def get_cost(utype, input):
  buff_name = get_name(utype, input)
  if (utype == "class"):
    if (buff_name in class_costs.keys()):
      return class_costs[buff_name]
    else:
      return 0
  else:
    if (buff_name in retrain_costs.keys()):
      return retrain_costs[buff_name]
    else:
      return 0
def buy(utype, input):
  cost = int(get_cost(utype, input))
  old_up = int(get_uvar("u_up", 0))
  new_up = old_up - cost
  set_uvar("u_up", new_up)
def convert(num):
  num = int(num)
  old_dtp = int(get_uvar("u_dtp"), 0)
  old_up = int(get_uvar("u_up"), 0)
  new_dtp = old_dtp - num
  new_up = old_up + num
  set_uvar("u_dtp", new_dtp)
  set_uvar("u_up", new_up)
def get_class_costs():
  return dump_json(class_costs)
def get_retrain_costs():
  return dump_json(retrain_costs)