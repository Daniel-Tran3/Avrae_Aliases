!gvar edit a9c39477-1c7f-4ce0-9b94-31697defe31e

# This module manipulates pet stats and returns an altered json.

stat_max = {"food": 100, "fitness": 5, "social": 100}
energy_costs = energy_costs = {"fitness": 10, "social": 1}

def make_pet():
  pet_dict = {"name": "", "food": 100, "fitness": 5, "social": 100, "energy": 100, "tob": time(), "age": 0, "last_check": time(), "mood": "content", "type": "Animal", "version": "1.1"}
  set_uvar_nx("wu_pet", dump_json(pet_dict))
def reset(trait, arg):
  pet_dict = load_json(get_uvar("wu_pet"))
  pet_dict[trait] = arg.capitalize()
  set_uvar("wu_pet", dump_json(pet_dict))
def restore(stat, arg):
  pet_dict = load_json(get_uvar("wu_pet"))
  old_stat = int(pet_dict[stat])
  pet_dict[stat] = min(int(pet_dict[stat]) + int(arg), stat_max[stat])
  spent = int(pet_dict[stat]) - old_stat
  if (stat in energy_costs.keys()):
    pet_dict["energy"] -= spent * energy_costs[stat]
  set_uvar("wu_pet", dump_json(pet_dict))
def update():
  using(
    updater="52b122d4-94cf-4520-b39b-bcc3e3eb267c"
  )
  return updater.update()