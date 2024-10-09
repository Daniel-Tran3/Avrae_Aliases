!gvar edit ff73e875-3eaa-4428-9fbd-10b338bf0d90

# This module manipulates food stats and returns an altered json.
empty_satchel = {"common": 0, "uncommon": 0, "rare": 0, "epic": 0, "legendary": 0}
rarity_order = ["common", "uncommon", "rare", "epic", "legendary"]
thresholds = {"common": 1000, "uncommon": 300, "rare": 100, "epic": 10, "legendary": 1}
food_vals = {"common": 1, "uncommon": 5, "rare": 25, "epic": 50, "legendary": 100}

def make_food():
  food_dict = {"satchel": empty_satchel, "version": 1.0}
  set_uvar_nx("wu_food", dump_json(food_dict))
def acquire(opt):
  food_dict = load_json(get_uvar("wu_food"))
  satchel = food_dict["satchel"]
  if (opt == "forage"):
    rarity_val = randint(0,1000)
    final_rarity = "common"
    for rarity in rarity_order:
      if (rarity_val < thresholds[rarity]):
        final_rarity = rarity
    satchel[final_rarity] = satchel[final_rarity] + 1
    food_dict["satchel"] = satchel
    set_uvar("wu_food", dump_json(food_dict))
    return f"{final_rarity}"
  else:
    return f"Bad food acquiring option {opt}.\n"
def feed(num, ftype):
  num = int(num)
  pet_dict = load_json(get_uvar("wu_pet"))
  hunger = 100 - int(pet_dict["food"])
  curr_val = int(food_vals[ftype])
  spent = min(floor(hunger / curr_val), num)
  restored = spent * curr_val
  food_dict = load_json(get_uvar("wu_food"))
  satchel = food_dict["satchel"]
  satchel[ftype] -= spent
  food_dict["satchel"] = satchel
  set_uvar("wu_food", dump_json(food_dict))
  return f"{restored}|{spent}"
