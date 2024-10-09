!gvar edit afdce05f-1c61-4939-a54b-ec569dd17d38

# This module generates basic pet strings.

stat_max = {"food": 100, "fitness": 5, "social": 100, "energy": 100}
energy = ["fitness", "social"]
needs_json = ["stats", "check", "restore"]
no_show = ["tob", "last_check"]

def get_str(opt, arglist):
  args = arglist.split("|")
  if (opt in needs_json):
    pet_dict = load_json(get_uvar("wu_pet"))
  using(
    no_arg_str="7a38e055-78ee-48b3-a942-3ec9b03143d4",
    idle="49a609a7-05c0-453a-bace-c1282fd79775"
  )
  if (opt == "pet_help"):
    return no_arg_str.get_str(opt)
  elif (opt == "reset"):
    return f"{cap(args[0])} set to {cap(args[1])}."
  elif (opt == "stats"):
    output = ""
    for key in pet_dict.keys():
      if (key not in no_show):
        output += f"{cap(key)}: {pet_dict[key]}"
        output += f" / {stat_max[key]}\n" if (key in stat_max.keys()) else "\n"
    return output
  elif (opt == "check"):
    return idle.get_idle(pet_dict["name"], pet_dict["mood"])
  elif (opt == "release"):
    delete_uvar("wu_pet")
    return f"Released {args[0]} back into the wild! Hope they have a good life!"
  elif (opt == "restore"):
    name = pet_dict["name"]
    stat = args[0]
    stat_val = pet_dict[stat]
    output = f"Restored {args[1]} to {name}'s {stat}!\n{cap(stat)} is now {stat_val} / {stat_max[stat]}!\n"
    if (stat in energy):
      energy = pet_dict["energy"]
      energy_max = stat_max["energy"]
      output += f"Energy is now {energy} / {energy_max}!" 
    return output
  elif (opt == "manual"):
    return no_arg_str.get_str(args[0])
  elif (opt == "update"):
    return no_arg_str.get_str(args[0])
  else:
    return "Bad basic pet_str opt " + opt
def cap(str):
  return str.capitalize()