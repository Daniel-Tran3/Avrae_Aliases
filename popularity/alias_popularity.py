!alias popularity embed <drac2>
# This alias runs popularity commands.
args = [arg for arg in &ARGS&]
using(
  err_check="13e7b4ba-2121-4be7-a9dd-7a7b7c556e70",
  pop_tool="3ef2b289-b512-4267-839c-1abe61a60c8e",
  pop_str="fc374787-4fd7-4336-8336-0cef0f425004"
)
base_opts = ["stats", "list", "search", "buy", "donate", "set"]
set_uvar_nx("u_cred", 0)
set_uvar_nx("u_popularity", 0)
arg_json = dump_json(args)
output = pop_str.get_str("pop_help", arg_json)
err_check_input = f"{arg_json}"
err_str = err_check.pop_err_check(err_check_input).split("|")
error = int(err_str[0])
if (error == 1):
  output = err_str[1]
if (error == 0 and len(args) > 0):
  if (args[0] in base_opts):
    opt = args[0]
    if (opt == "buy"):
      pop_tool.buy(args[1])
    elif (opt == "donate"):
      pop_tool.donate(args[1])
    elif (opt == "set"):
      set_uvar("u_popularity", args[1])
    output = pop_str.get_str(opt, arg_json)
</drac2>
-title "Popularity"
-desc "{{ output }}"