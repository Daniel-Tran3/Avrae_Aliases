!gvar edit 2bf76324-9590-456e-bcf6-2d17bd0cf923

# This module checks for errors in commands.

arglens = {"name": "2", "feed": "3", "exercise": "2", "play": 2, "type": 2, "manual": 2}
numerical = ["feed", "exercise", "play"]
energy_costs = {"exercise": 10, "play": 1}

def error_check(param_list):
  using(
    err_str="34948358-f244-44b7-9c23-d186e008b471"
  )
  params = param_list.split("|")
  args = load_json(params[0])
  pet_dict = load_json(get_uvar("wu_pet"))
  food_dict = load_json(get_uvar("wu_food"))
  satchel = food_dict["satchel"]
  err_arg_str = "0|no_err|no_err"
  if (len(args) > 0):
    if (args[0] in arglens.keys() and len(args) < int(arglens[args[0]])):
      err_arg_str = f"1|few_args|{args[0]}"
    if (args[0] in numerical):
      try:
        num = int(args[1])
      except ("ValueError", "TypeError"):
        err_arg_str = f"1|not_num|{args[1]}"
      if (args[0] == "exercise" or args[0] == "play"):
        energy = pet_dict["energy"]
        if (energy < num * energy_costs[args[0]]):
          err_arg_str = f"1|few_energy|{energy}.{args[0]}.{num}"
      if (args[0] == "feed"):
        if (args[2] in satchel.keys()):
          food_amt = int(satchel[args[2]])
          if (food_amt < num):
            err_arg_str = f"1|few_food|{num}.{args[2]}.{food_amt}"
        else:
          err_arg_str = f"1|bad_food|{args[2]}"
  err_args = err_arg_str.split("|")
  error = int(err_args[0])
  opt = err_args[1]
  str_arg = err_args[2].replace(".", "|")
  return f"{error}|{err_str.get_str(opt, str_arg)}"