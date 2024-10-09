!alias food embed <drac2>
# This alias runs food commands.
args = [arg.lower() for arg in &ARGS&]
using(
  food_tool="ff73e875-3eaa-4428-9fbd-10b338bf0d90",
  food_str="90227aba-8de2-4b9b-90ae-b66ce02939cc",
  base_command="ee1899fe-5b89-4866-99fd-0aab0d9c93f1"
)
base_opts = ["forage", "check"]
known_opts = base_opts
food_tool.make_food()
output = food_str.get_str("food_help", "")
comm_out = ""
if (len(args) > 0):
  if (args[0] in base_opts):
    output = base_command.handle_food(dump_json(args))
</drac2>
-title "Food"
-desc "{{ output }}"