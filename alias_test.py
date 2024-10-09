!alias setter embed <drac2>
args = [arg.lower() for arg in &ARGS&]
using(
  set_mod="3bdeec16-5b37-44c8-9bf4-c93e14e680ff"
)
set_mod.set_uvar_val(dump_json(args))
output = f"Successfully set {args[0]}!"
</drac2>
-title "Setter"
-desc "{{ output }}"