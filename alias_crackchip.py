!alias crackchip embed <drac2>

using(
  chip_txt="41a160d2-fa9f-46f2-b073-1e1d5e522f97"
)

args = [arg for arg in &ARGS&]

name = "You"
if (len(args) > 0):
  name = args[0]

output = chip_txt.chipgen(name)

</drac2>
-title "Cracking Chips"
-desc "{{ output }}"