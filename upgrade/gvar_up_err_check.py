!gvar edit d5e43e21-db7f-44c2-9951-206ed5d78d4a

arglens = {"convert": 2, "set": 2, "buy": 3}

def err_check(arg_json):
  using(
    err_str="34948358-f244-44b7-9c23-d186e008b471",
    tool="418edcab-2b22-4a13-b0d5-8c064777aa5a"
  )
  args = load_json(arg_json)
  u_dtp = int(get_uvar("u_dtp"))
  err_arg_str = "0|no_err|no_err"
  if (len(args) > 0):
    if (args[0] in arglens.keys() and len(args) < int(arglens[args[0]])):
      err_arg_str = f"1|few_args|{args[0]}"
    elif (args[0] == "set" or args[0] == "convert"):
      try:
        num = int(args[1])
        if (args[0] == "convert" and num > u_dtp):
          err_arg_str = f"1|few_dtp|{num}.{u_dtp}"
      except ("ValueError", "TypeError"):
        err_arg_str = f"1|not_num|{args[1]}"
    elif (args[0] == "buy"):
      cost = tool.get_cost(args[1], args[2])
      u_up = int(get_uvar("u_up"))
      if (cost == 0):
        err_arg_str = f"1|bad_upgrade|{args[1]}: {args[2]}"
      else:
        if (cost > u_up):
          name = tool.get_name(args[1], args[2])
          err_arg_str = f"1|few_up|{args[1]}: {name}.{cost}"
  err_args = err_arg_str.split("|")
  error = int(err_args[0])
  opt = err_args[1]
  str_arg = err_args[2].replace(".", "|")
  return f"{error}|{err_str.get_str(opt, str_arg)}"