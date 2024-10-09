!alias portents embed <drac2>
ch = character()
args = [arg.lower() for arg in &ARGS&]
def crit(d20):
  return f"**{d20}**" if d20 == 1 or d20 == 20 else d20

ch = character()
args = [arg.lower() for arg in &ARGS&]
p1 = roll("1d20")
p2 = roll("1d20")
output = "Please specify a valid argument."
footer = ""
old_arr = load_json(get_uvar("u_port", []))
new_arr = dump_json([str(p1), str(p2)])

real = ch.cc_exists("Portent")
valid = real or "on" in args

if valid:
  if (len(args) > 0):
    if ("reset" in args):
      if real:
        ch.set_cc("Portent", 2)
      str1 = crit(p1)
      str2 = crit(p2)
      output = f"Rolling 2d20... {str1} and {str2}!"
      set_uvar("u_port", new_arr)
    elif ("list" in args):
      if (len(old_arr) > 0):
        output = f"Your portents are {old_arr}."
      else:
        output = "You are out of portents."
    elif ("spend" in args):
      if (args[1] in old_arr):
        old_arr.remove(args[1])
        set_uvar("u_port", dump_json(old_arr))
        if real:
          ch.set_cc("Portent", ch.get_cc("Portent") - 1)
        output = f"Spent portent {args[1]}. Portents are now {old_arr}."
      else:
        output = f"Could not find {args[1]} in portents {old_arr}."
    elif ("wipe" in args):
      if real:
        ch.set_cc("Portent", 0)
      set_uvar("u_port", dump_json([]))
      output = "Wiped your portents."
else:
  output = "You do not have portents."
  footer = "Use '!portents on' to bypass this."


</drac2>
-title "{{ ch.name }}'s Portents"
-desc "{{ output }}"
-color {{ color }}
-footer "{{ footer }}"