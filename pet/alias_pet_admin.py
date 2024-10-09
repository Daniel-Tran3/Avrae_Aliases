!alias pet_admin embed <drac2>
# This alias runs pet commands.
args = [arg.lower() for arg in &ARGS&]
using(
  pet_tool="a9c39477-1c7f-4ce0-9b94-31697defe31e"
)
pet_tool.make_pet()
pet_dict = load_json(get_uvar("wu_pet"))
if (len(args) > 0):
  if (args[0] == "get"):
    if (len(args) > 1):
      output = f"Your pet's {args[1]} is {pet_dict[args[1]]}!"
    else:
      output = "Have to tell me what you're trying to get, y'know!"
  elif (args[0] == "set"):
    if (len(args) > 2):
      pet_dict[args[1]] = args[2]
      set_uvar("wu_pet", dump_json(pet_dict))
      output = f"Set {args[1]} to {args[2]}!"
    else:
      output = "Have to tell me what you're trying to get, y'know!"
  else:
    output = "Try a different command - only 'get' and 'set' are allowed!"
</drac2>
-title "Pet"
-desc "{{ output }}"