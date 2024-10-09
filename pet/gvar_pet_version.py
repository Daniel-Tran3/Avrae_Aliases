!gvar edit 52b122d4-94cf-4520-b39b-bcc3e3eb267c

# This module converts a pet from an older version to the current version.

known_versions = ["0.0", "1.0"]
current_version = "1.1"
compatible_keys = []
convert_keys = {}

def update():
  new_pet_dict = {"name": "", "food": 100, "fitness": 5, "social": 100, "energy": 100, "tob": time(), "age": 0, "last_check": time(), "mood": "content", "type": "Animal", "version": current_version}
  old_pet_dict = load_json(get_uvar("wu_pet"))
  old_version = "0.0"
  if ("version" in old_pet_dict.keys()):
    old_version = old_pet_dict["version"]
  for key in old_pet_dict.keys():
    if (key in new_pet_dict.keys()):
      compatible_keys.append(key)
  if (old_version == "0.0"):
    convert_keys = {"hunger": "food"}
  if (old_version in known_versions):
    for key in compatible_keys:
      new_pet_dict[key] = old_pet_dict[key]
    for key in convert_keys.keys():
      new_pet_dict[convert_keys[key]] = old_pet_dict[key]
    set_uvar("wu_pet", dump_json(new_pet_dict))
    return "updated"
  elif (old_version == current_version):
    return "newest"
  else:
    return "not_found"