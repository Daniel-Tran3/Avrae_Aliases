!gvar edit 0303c251-43c4-43f8-9499-0b2d5fddb0f1

# This module generates user manual strings for pet commands.

setters = ["name", "type"]
energy = {"exercise": 10, "play": 1}
restore = {"feed": "food", "exercise": "fitness", "play": "social"}

def get_str(opt):
  output = f"Use `!pet {opt}` to "
  if (opt in setters):
    output += f"set your pet's {opt}!\nNote: this command can only accept one word arguments."
  elif (opt in restore):
    stat = restore[opt]
    output += f"restore your pet's {stat}!"
    if (opt == "feed"):
      output += f"\n When feeding your pet, you should also supply an integer and food type (see `!food` for more info), like so:"
      output += f"`\n!pet {opt} [integer] [food_type]`"
    if (opt in energy.keys()):
      output += f"\nNote: you must supply an integer, like so: `!pet {opt} [integer]`"
      output += f"\nUsing this command costs {energy[opt]} energy per point of {stat}!"
  elif (opt == "release"):
    output += "release your pet back into the wild...or just send it to a new owner. Imagine what you like!"
  elif (opt == "check"):
    output += "check on how your pet is doing!\nThey'll usually be doing an idle activity.\n"
    output += "If your pet is in need of care, this activity will hint at what's bothering them."
  elif (opt == "stats"):
    output += "list a detailed breakdown of every (non-time) statistic of your pet.\n"
    output += "These are: age, name, type, version, food, fitness, social, energy, and mood."
  elif (opt == "update"):
    output += "update your pet's version! You must supply your pet's current version as an argument.\n"
    output += "You should be able to obtain this using `!pet stats`. If version is not listed, then your version is 0.0"
  else:
    output += f"...oh? We don't have any data on {opt}, sorry!\n"
  return output