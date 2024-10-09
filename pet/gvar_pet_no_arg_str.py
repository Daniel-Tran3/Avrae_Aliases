!gvar edit 7a38e055-78ee-48b3-a942-3ec9b03143d4

# This module generates strings that do not require arguments for pet commands.

manual = ["name",  "type", "check", "stats", "update"]
manual = manual + ["release", "feed", "exercise", "play"]

def get_str(opt):
  using(
    manual_mod="0303c251-43c4-43f8-9499-0b2d5fddb0f1"
  )
  if (opt == "pet_help"):
    help_output = "To get started, you must first name your pet! Use `!pet name` to do that.\n"
    help_output += "Use `!pet manual`, followed by a command, to learn more about it!\n"
    help_output += "Current commands are: name, type, check, feed, exercise, play, release, stats, update.\n"
    help_output += "If you find that a command is not working, you may need to use `!pet update` (see manual).\n"
    return help_output
  elif (opt in manual):
    return manual_mod.get_str(opt)
  elif (opt == "updated"):
    return "Congrats! Your pet has been updated to the latest version."
  elif (opt == "newest"):
    return "Congrats! Your pet was already at the latest version."
  elif (opt == "not_found"):
    return "Sorry, we couldn't find any data for that version - please contact the programmer, and we'll get that fixed for you ASAP!"
  else:
    return "Bad no_arg_str opt."