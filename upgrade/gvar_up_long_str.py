!gvar edit 5234df18-b7b4-491f-8fa9-a66e7e066745

def get_str(opt, key):
  if (opt == "help"):
    output = f"This command helps you view and manage your upgrade pool UP!\n"
    output += f"Use `!upgrade stats` to view your DTP and UP.\n"
    output += f"Use `!upgrade set [num]` to set your UP to `num`!\n"
    output += f"Use `!upgrade convert [num] ` to convert `num` of your DTP to UP!\n"
    output += f"Use `!upgrade list` to see all available class and retraining options!\n"
    output += f"Use `!upgrade buy [type] [category] [specific]` to purchase an upgrade with UP.\n"
    output += f"`type` should be either 'class' or 'retrain', `category` should be a category like "
    output += f"'Armor' for class or 'maneuver' for retrain. `specific` is optional, but you can specify "
    output += f"what type of class / retraining you're getting - like 'heavy' for a class in armor, or 'trip' "
    output += f"for a retraining in Battle Master Maneuver."
  else:
    output = "Bad long string (buff) option " + opt
  return output
    