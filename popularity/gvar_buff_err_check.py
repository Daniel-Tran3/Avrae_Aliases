!gvar edit 13e7b4ba-2121-4be7-a9dd-7a7b7c556e70

pop_arglens = {"search": 2, "buy": 3, "donate": 4, "set": 2}

def pop_err_check(arg_json):
  using(
    err_str="34948358-f244-44b7-9c23-d186e008b471",
    buffs="3ef2b289-b512-4267-839c-1abe61a60c8e"
  )
  args = load_json(arg_json)
  u_cred = int(get_uvar("u_cred"))
  err_arg_str = "0|no_err|no_err"
  if (len(args) > 0):
    if (args[0] in pop_arglens.keys() and len(args) < int(pop_arglens[args[0]])):
      err_arg_str = f"1|few_args|{args[0]}"
    elif (args[0] == "donate" or args[0] == "set"):
      try:
        num = int(args[1])
        if (args[0] == "donate" and num > u_cred):
          err_arg_str = f"1|few_cred|{args[0]}.{num}"
      except ("ValueError", "TypeError"):
        err_arg_str = f"1|not_num|{args[1]}"
    elif (args[0] == "buy"):
      cost = buffs.get_cost(args[1])
      if (cost == 0):
        err_arg_str = f"1|bad_buff|{args[1]}"
      else:
        if (cost > u_cred):
          name = buffs.get_name(args[1])
          err_arg_str = f"1|few_cred|{args[0]}.{name}.{cost}"
  err_args = err_arg_str.split("|")
  error = int(err_args[0])
  opt = err_args[1]
  str_arg = err_args[2].replace(".", "|")
  return f"{error}|{err_str.get_str(opt, str_arg)}"