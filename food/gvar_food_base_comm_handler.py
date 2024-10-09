!gvar edit ee1899fe-5b89-4866-99fd-0aab0d9c93f1

# This module handles basic food commands.

opts = ["forage", "check"]
pet_opts = ["feed"]
acquire = ["forage"]

def handle_food(arg_json):
  using(
    food_tool="ff73e875-3eaa-4428-9fbd-10b338bf0d90",
    food_str="90227aba-8de2-4b9b-90ae-b66ce02939cc"
  )
  args = load_json(arg_json)
  opt = "food_help"
  str_args = ""
  if (len(args) > 0):
    if (args[0] in opts):
      opt = args[0]
    if (args[0] in acquire):
      comm_str  = food_tool.acquire(args[0])
      str_args = f"{comm_str}"
    elif (args[0] == "check"):
      str_args = ""
  return food_str.get_str(opt, str_args)

def handle_pet(arg_json):
  using(
    food_tool="ff73e875-3eaa-4428-9fbd-10b338bf0d90",
    food_str="90227aba-8de2-4b9b-90ae-b66ce02939cc",
    pet_tool="a9c39477-1c7f-4ce0-9b94-31697defe31e",
    pet_str="afdce05f-1c61-4939-a54b-ec569dd17d38"
  )
  args = load_json(arg_json)
  opt = "food_help"
  str_args = ""
  output = ""
  if (len(args) > 0):
    if (args[0] in pet_opts):
      opt = args[0]
      if (args[0] == "feed"):
        comm_str = food_tool.feed(args[1], args[2]).split("|")
        restored = comm_str[0]
        spent = comm_str[1]
        pet_json = pet_tool.restore("food", restored)
        food_str_args = f"{spent}|{args[2]}"
        pet_str_args = f"food|{restored}"
        output = pet_str.get_str("restore", pet_str_args)
  output += food_str.get_str(opt, food_str_args)
  return output