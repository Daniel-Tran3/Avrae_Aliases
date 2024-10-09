!alias pet embed <drac2>
# This alias runs pet commands.
args = [arg.lower() for arg in &ARGS&]
using(
  food_tool="ff73e875-3eaa-4428-9fbd-10b338bf0d90",
  pet_update="56609ad0-58b3-4bd5-83d2-4e284b725b64",
  pet_tool="a9c39477-1c7f-4ce0-9b94-31697defe31e",
  food_command="ee1899fe-5b89-4866-99fd-0aab0d9c93f1",
  base_command="e2a58452-3cfd-475e-b925-1707147384e3",
  err_check="2bf76324-9590-456e-bcf6-2d17bd0cf923"
)
base_opts = ["name", "check", "release", "exercise", "play", "stats", "type", "update", "manual"]
food_opts = ["feed"]
known_opts = base_opts + food_opts
pet_tool.make_pet()
food_tool.make_food()
pet_update.update()
arg_json = dump_json(args)
output = base_command.handle(dump_json([]))
err_check_input = f"{arg_json}"
err_str = err_check.error_check(err_check_input).split("|")
error = int(err_str[0])
if (error == 1):
  output = err_str[1]
if (error == 0 and len(args) > 0):
  if (args[0] in base_opts):
    output = base_command.handle(arg_json)
  if (args[0] in food_opts):
    output = food_command.handle_pet(arg_json)
</drac2>
-title "Pet"
-desc "{{ output }}"