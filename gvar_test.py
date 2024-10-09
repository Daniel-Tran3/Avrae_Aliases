!gvar edit 3bdeec16-5b37-44c8-9bf4-c93e14e680ff

def set_uvar_val(argslist):
  args = load_json(argslist)
  set_uvar(args[0], args[1])