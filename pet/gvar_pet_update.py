!gvar edit 56609ad0-58b3-4bd5-83d2-4e284b725b64

# This module updates a pet based on time passed since last check.

stats = {"food": "hourly", "fitness": "daily", "social": "hourly"}
threshold = {"food": 84, "fitness": 4, "social": 90}
moods = {"food": "hungry", "fitness": "bored", "social": "lonely"}
penalties = {"hourly": 0, "daily": 0}
minute = 60
hour = 3600
day = 86400

def update():
  mood = "content"
  pet_dict = load_json(get_uvar("wu_pet"))
  keys = pet_dict.keys()
  if ("age" in keys):
    pet_dict["age"] = floor((time() - pet_dict["tob"]) / day)
  if ("last_check" in keys):
    penalties["hourly"] = max(floor((time() - pet_dict["last_check"]) / hour), 0) 
    penalties["daily"] = max(floor((time() - pet_dict["last_check"]) / day), 0) 
  if ("energy" in keys):
    pet_dict["energy"] += max(floor((time() - pet_dict["last_check"]) / minute), 0)
    pet_dict["energy"] = min(pet_dict["energy"], 100)
  for stat in stats:
    if (stat in keys):
      pet_dict[stat] = max(int(pet_dict[stat]) - int(penalties[stats[stat]]), 0)
      if (int(pet_dict[stat]) < threshold[stat]):
        mood = moods[stat]
  pet_dict["mood"] = mood
  pet_dict["last_check"] = time()
  set_uvar("wu_pet", dump_json(pet_dict))