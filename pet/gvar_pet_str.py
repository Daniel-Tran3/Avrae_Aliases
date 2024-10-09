!gvar edit f4b1258b-9a50-44cb-ad57-1bbaf3565b64

# This module generates all pet strings.

basic_opt = ["pet_help", "reset", "stats", "check", "release", "restore", "manual", "update"]
err_opt = ["few_args", "not_num", "few_energy"]

def get_str(opt, arglist):
  args = arglist.split("|")
  pet_dict = {}
  using(
    basic="afdce05f-1c61-4939-a54b-ec569dd17d38",
    err_str="34948358-f244-44b7-9c23-d186e008b471"
  )
  if (opt in basic_opt):
    return basic.get_str(opt, arglist)
  elif (opt in err_opt):
    return err_str.get_str(opt, arglist)
  else:
    return "Bad pet_str opt " + opt
def cap(str):
  return str.capitalize()