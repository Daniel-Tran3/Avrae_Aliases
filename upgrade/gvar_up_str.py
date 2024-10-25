!gvar edit 7331f9ca-8042-44ae-8f8f-59d0a9ab730f

def get_str(opt, arg_json):
  args = load_json(arg_json)
  u_dtp = get_uvar("u_dtp")
  u_up = get_uvar("u_up")
  using(
    long_str="5234df18-b7b4-491f-8fa9-a66e7e066745",
    tool="418edcab-2b22-4a13-b0d5-8c064777aa5a"
  )
  class_costs = load_json(tool.get_class_costs())
  retrain_costs = load_json(tool.get_retrain_costs())
  if (opt == "help"):
    output = long_str.get_str(opt, "")
  elif (opt == "stats"):
    output = f"You have {u_dtp} DTP!\nYou have {u_up} UP in your upgrade pool!\n"
  elif (opt == "set"):
    output = f"You now have {u_up} UP in your upgrade pool!\n"
  elif (opt == "convert"):
    output = f"Converted {args[1]} DTP! You now have {u_dtp} DTP and {u_up} UP in your upgrade pool!\n"
  elif (opt == "list"):
    output = "Listing all classes:\n"
    for uclass in class_costs.keys():
      output += uclass + ": " + class_costs[uclass] + " UP\n"
    output += "\nListing all retraining options:\n"
    for retrain in retrain_costs.keys():
      output += retrain + ": " + retrain_costs[retrain] + " UP\n"
  elif (opt == "buy"):
    utype = args[1].lower()
    key = tool.get_name(utype, args[2])
    spec = ""
    if (len(args) > 3):
      spec = f" ({args[3].capitalize()})"
    cost = tool.get_cost(utype, key)
    output = f"You bought {utype.capitalize()}: {key}{spec} for {cost} UP!\n"
    output += f"You now have {get_uvar('u_up')} UP!"

  else:
    output = "Bad get_str (up) option " + opt
  return output