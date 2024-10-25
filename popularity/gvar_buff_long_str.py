!gvar edit f1f1fd81-9b4a-49ea-ac2e-33345f21982b

def get_str(opt, key):
  using(
    dict_mod="712955e6-33c7-483c-8de8-a8db26b6530b"
  )
  if (opt == "pop_help"):
    output = f"This command helps you view and manage your credits and popularity!\n"
    output += f"Use `!popularity stats` to view your credits and popularity.\n"
    output += f"Use `!popularity list` to generate a list of every available mission buff.\n"
    output += f"Use `!popularity search [buff]` to find a specific mission buff (one-word only, please!)\n"
    output += f"Use `!popularity buy [buff] [club to raise acclaim]` to buy a buff, raising acclaim for a club of your choice!\n"
    output += f"Use `!popularity buy [buff] [club to raise acclaim]` to buy a buff, raising acclaim for a club of your choice!\n"
    output += f"Use `!popularity set [num]` to set your popularity!\n"
    output += f"Use `!popularity donate [num] [club to create] [club to raise acclaim]` to donate [num] credits towards creating a club, "
    output += f"also choosing a club to raise acclaim for!\nNote: If you would like to split your acclaim, please make a note underneath the command!\n"
    output += f"When specifying an argument with more than two words, please put it in quotation marks!"
  elif (opt == "desc"):
    output = dict_mod.get_desc(key)
  elif (opt == "ftext"):
    output = dict_mod.get_ftext(key)
  else:
    output = "Bad long string (buff) option " + opt
  return output
    