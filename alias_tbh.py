!alias tbh embed <drac2>
args = [arg.lower() for arg in &ARGS&]
tbhs = load_json(get_svar("tbh_list"))
chars = []
for key in tbhs.keys():
  chars.append(key)
event = randint(0,100)
if (event == 0):
  num = len(chars)
  random = 1
  output = f"Special event: TBH Mob! You get attacked by {num} tbhs!\n# "
elif (event == 1):
  output = f"Special event: Siblings!\n# "
  random = 0
  names = ["Norm", "Kelsie"]
  num = len(names)  
else:
  num = 1
  random = 1
  output = "# "

count = 0
for i in range(0,num,1):
  if (random == 0):
    name = names[i]
  else:
    char_idx = randint(0, len(chars))
    name = chars[char_idx]
  char_tbh = tbhs[name]
  output += f"{char_tbh} "
  count = count + 1
  if (count == 10):
    count = 0
    output += "\n # "


</drac2>
-title "Surprise TBH!"
-desc " {{ output }} "