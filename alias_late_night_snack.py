!alias lns embed <drac2>

ch = character()
d6_arr = ["Occultist", "Sorcerer", "Wizard"]
d8_arr = ["Artificer", "Bard", "Cleric", "Druid", "Monk", "Rogue", "Savant", "Warlock"]
d10_arr = ["Blood Hunter", "Fighter", "Paladin", "Ranger"]
d12_arr = ["Barbarian"]
hit_dice_dict = {"d6": d6_arr, "d8": d8_arr, "d10": d10_arr, "d12": d12_arr}
hit_dice = "d4"
hit_dice_type = "None"
for hit_dice_upgrade in hit_dice_dict.keys():
  for x in hit_dice_dict[hit_dice_upgrade]:
    if (ch.levels.get(x) > 0):
      hit_dice = hit_dice_upgrade
      hit_dice_type = x
hit_dice_text = f"Hit Die ({hit_dice_type})"
con_mod = constitutionMod
result = vroll(f"1{hit_dice}[*{hit_dice_text}*] + {con_mod}[*Constitution Mod*] + 1d4")
result_str = str(result)
total = result.total

output = f"With a roll of {result_str}, you heal {total} hp!\nMeals do hit different after midnight."

</drac2>
-title "Eating a Late Night Snack!"
-desc "{{ output }}"