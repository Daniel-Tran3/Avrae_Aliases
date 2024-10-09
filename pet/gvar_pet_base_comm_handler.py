!gvar edit e2a58452-3cfd-475e-b925-1707147384e3

# This module handles basic pet commands.

opts = ["name", "check", "release", "feed", "exercise", "play", "stats", "type", "update"]
reset = ["name", "type"]
restore = {"exercise": "fitness", "play": "social"}

def handle(arg_json):
  using(
    pet_tool="a9c39477-1c7f-4ce0-9b94-31697defe31e",
    pet_str="f4b1258b-9a50-44cb-ad57-1bbaf3565b64"
  )
  args = load_json(arg_json)
  pet_dict = load_json(get_uvar("wu_pet"))
  opt = "pet_help"
  str_args = ""
  if (len(args) > 0):
    if (args[0] in opts):
      opt = args[0]
    if (args[0] in reset):
      opt = "reset"
      pet_tool.reset(args[0], args[1])
      str_args = f"{args[0]}|{args[1]}"
    elif (args[0] == "check" or args[0] == "stats"):
      str_args = ""
    elif (args[0] == "release"):
      str_args = pet_dict["name"]
      delete_uvar("wu_pet")
    elif (args[0] in restore.keys()):
      opt = "restore"
      stat = restore[args[0]]
      pet_tool.restore(stat, args[1])
      str_args = f"{stat}|{args[1]}"
    elif (args[0] == "update"):
      opt = "update"
      str_arglist = pet_tool.update().split("|")
      str_args = str_arglist[0]
    elif (args[0] == "manual"):
      opt = "manual"
      str_args = args[1]
  return pet_str.get_str(opt, str_args)