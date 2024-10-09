!gvar edit 85009056-bd62-478c-994e-6aa39cf97f53

# This module generates strings that do not require arguments for food commands.

def get_str(opt):
  #using(
  #  manual_mod="0303c251-43c4-43f8-9499-0b2d5fddb0f1"
  #)
  if (opt == "food_help"):
    help_output = "Looking for food to feed your pet with?\n"
    help_output += "Use `!food forage` to find some food of some randomly determined rarity!\n"
    help_output += "Use `!food check` to return a list of all foods that you currently have.\n"
    return help_output
  else:
    return "Bad no_arg_str opt."