!gvar edit bac2cf89-d7fd-4b49-817d-be831ee2ba54

def get_desc(key):
  using(
    desc1="0399a217-aad0-4c52-b169-30e777510f61",
    desc2="7db1315a-b0ab-45d5-bd57-60b6dc90c353"
  )
  desc1_keys = ["Cramming", "Energy Drink", "Late Night Snack", "Open Notes", "Student Gossip", "Teacher's Pet", "Are You Sure You Want To Do That?", "Calculated Comedy Club", "Giving 110%", "Research Recall"]
  desc2_keys = ["Careful Planning", "Seek The Truth", "Science Rules!", "Camaraderie Club"]
  result = ""
  if key in desc1_keys:
    result = desc1.get_desc(key)
  if key in desc2_keys:
    result = desc2.get_desc(key)
  return f"{result}" if result != "" else "Bad description total key."