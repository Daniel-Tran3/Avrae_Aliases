!gvar edit fc374787-4fd7-4336-8336-0cef0f425004

keys = ["Cramming", "Energy Drink", "Late Night Snack", "Open Notes", "Student Gossip", "Teacher's Pet"]

def get_str(opt, arg_json):
  args = load_json(arg_json)
  u_cred = get_uvar("u_cred")
  u_pop = get_uvar("u_popularity")
  using(
    long_str="f1f1fd81-9b4a-49ea-ac2e-33345f21982b",
    buff_tools="3ef2b289-b512-4267-839c-1abe61a60c8e"
  )
  if (opt == "pop_help"):
    output = long_str.get_str(opt, "")
  elif (opt == "stats"):
    output = f"You have {u_cred} credits!\nYou have {u_pop} popularity!\n"
  elif (opt == "list"):
    output = "Listing all Mission Buffs:\n"
    for key in keys:
      output += get_buff(key)
  elif (opt == "search"):
    key = buff_tools.get_name(args[1])
    output = f"Searching for Mission Buff {key}:"
    if (key in keys):
      output += get_buff(key)
    else:
      output = f"\nBuff {key} not found!"
  elif (opt == "buy"):
    key = buff_tools.get_name(args[1])
    cost = buff_tools.get_cost(key)
    output = f"You bought {key} for {cost} credits!\n"
    output += f"All proceeds go to the acclaim of {args[2]}\n\n"
    output += get_str("stats", arg_json)
    output += "See your buff's effects below!\n"
    output += get_buff(key)
  elif (opt == "donate"):
    output = f"You donated {args[1]} to building club {args[2]}!\n"
    output += f"All proceeds go to the acclaim of {args[3]}\n"
  else:
    output = "Bad get_str (buff) option " + opt
  return output
def get_buff(key):
  using(
    long_str="f1f1fd81-9b4a-49ea-ac2e-33345f21982b",
    buff_tools="3ef2b289-b512-4267-839c-1abe61a60c8e"
  )
  output = f"\nName: {key}\n"
  output += f"Cost: {buff_tools.get_cost(key)}\n"
  output += f"Description: {long_str.get_str('desc', key)}\n"
  output += f"*{long_str.get_str('ftext', key)}*\n"
  return output
