!gvar edit 94d72fa5-62a7-4602-b613-be571b467f6e

# This module generates basic food strings.
needs_json = ["check", "forage", "feed"]

def get_str(opt, arglist):
  args = arglist.split("|")
  if (opt in needs_json):
    food_dict = load_json(get_uvar("wu_food"))
    satchel = food_dict["satchel"]
    satchel_json = dump_json(satchel)
  using(
    no_arg_str="85009056-bd62-478c-994e-6aa39cf97f53"
  )
  if (opt == "food_help"):
    return no_arg_str.get_str(opt)
  elif (opt == "forage"):
    output = f"Congratulations! You found 1 {args[0]} food.\n"
    output += find_rarity(args[0], satchel_json)
    return output
  elif (opt == "check"):
    output = ""
    for key in satchel.keys():
      output += find_rarity(key, satchel_json)
    return output
  elif (opt == "feed"):
    remaining = find_rarity(args[1], satchel_json)
    return f"Used up {args[0]} unit(s) of {args[1]} food! {remaining}\n"
  else:
    return "Bad basic food_str opt " + opt
def cap(str):
  return str.capitalize()
def find_rarity(key, satchel_json):
  satchel = load_json(satchel_json)
  amt = int(satchel[key])
  amt_plural = "foods" if (amt != 1) else "food"
  return f"You have {amt} {key} {amt_plural}.\n"