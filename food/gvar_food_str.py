!gvar edit 90227aba-8de2-4b9b-90ae-b66ce02939cc

# This module generates all food strings.

basic_opt = ["food_help", "forage", "check", "feed"]
err_opt = ["bad_food", "few_food", "few_args", "not_num"]

def get_str(opt, arglist):
  args = arglist.split("|")
  using(
    basic="94d72fa5-62a7-4602-b613-be571b467f6e",
    err_str="34948358-f244-44b7-9c23-d186e008b471"
  )
  if (opt in basic_opt):
    return basic.get_str(opt, arglist)
  elif (opt in err_opt):
    return err_str.get_str(opt, arglist)
  else:
    return "Bad food_str opt " + opt
def cap(str):
  return str.capitalize()