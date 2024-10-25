!gvar edit 41a160d2-fa9f-46f2-b073-1e1d5e522f97

def chipgen(name):
  chip_txt = {"Dorito": "What a clean break! Now your orangle triangle is...a smaller, less impressive triangle."}
  chip_txt["Tortilla Chip"] = "Welp, lost that one in that salsa. Better go get more to make up for it."
  chip_txt["Pringle"] = "...honestly these things are super fragile anyways. Ever had a can of these without a broken one in it?\n...yeah, me neither."
  chip_txt["Silicon Chip"] = "...oh, that's not good. Dunno how you managed this one, but your phone isn't gonna be working for a bit."
  chip_txt["Zakuzaku Chip"] = "Sharp enough to cut som- hey, watch where you're swinging that thing!"
  chip_txt["Hirihiri Chip"] = "...one has to imagine that spicy chips would make for terrifying food fight ammo."

  chips = []
  for chip_name in chip_txt.keys():
    chips.append(chip_name)
  num_chips = len(chips)
  chip_idx = randint(0, num_chips)

  cracked_chip = chips[chip_idx]

  output = f"{name} cracked a...{cracked_chip}!\n\n{chip_txt[cracked_chip]}"
  return output
