!alias upgrade embed <drac2>
# This alias runs upgrade commands.
args = [arg for arg in &ARGS&]
using(
  err_check="d5e43e21-db7f-44c2-9951-206ed5d78d4a",
  up_str="7331f9ca-8042-44ae-8f8f-59d0a9ab730f",
  up_tool="418edcab-2b22-4a13-b0d5-8c064777aa5a"
)
base_opts = ["stats", "set", "list", "buy", "convert"]
set_uvar_nx("u_dtp", 0)
set_uvar_nx("u_up", 0)
arg_json = dump_json(args)
output = up_str.get_str("help", arg_json)
err_check_input = f"{arg_json}"
err_str = err_check.err_check(err_check_input).split("|")
error = int(err_str[0])
if (error == 1):
  output = err_str[1]
if (error == 0 and len(args) > 0):
  if (args[0] in base_opts):
    opt = args[0]
    if (opt == "set"):
      set_uvar("u_up", args[1])
    if (opt == "buy"):
      up_tool.buy(args[1], args[2])
    if (opt == "convert"):
      up_tool.convert(args[1])
    output = up_str.get_str(opt, arg_json)
</drac2>
-title "Upgrade Pool"
-desc "{{ output }}"