!gvar edit 34948358-f244-44b7-9c23-d186e008b471

# This module generates error strings.

def get_str(opt, arglist):
  known = 1
  args = arglist.split("|")
  if (opt == "few_args"):
    output = "Not enough args for option " + args[0]
  elif (opt == "not_num"):
    output = "Need numerical arg, not " + args[0]
  elif (opt == "few_energy"):
    output = f"{args[0]} is not enough to raise {args[1]} by {args[2]}!"
  elif (opt == "bad_food"):
    output = f"{args[0]} is not a valid type of food!"
  elif (opt == "few_food"):
    amt = int(args[0])
    amt_plural = "foods" if (amt != 1) else "food"
    output = f"Can't feed your pet {args[0]} {args[1]} {amt_plural} if you only have {args[2]}!\n"
  elif (opt == "bad_buff"):
    output = f"Couldn't find mission buff " + args[0] + "!\nPlease refer to the list in the popularity document in important-links!"
  elif (opt == "few_cred"):
    u_cred = get_uvar("u_cred", 0)
    if (args[0] == "donate"):
      output = f"Cannot donate {args[1]} credits, "
    else:
      output = f"Cannot buy buff {args[1]}, which costs {args[2]} credits, "
    outupt += f"when you only have {u_cred}!"
  elif (opt == "no_err"):
    output = f"No errors detected!\n"
  else:
    output = "Bad err_str opt " + opt
  output += f"\nIf you're having trouble, please use the basic help text to see how to format your command!"
  return output
def cap(str):
  return str.capitalize()