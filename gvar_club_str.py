!gvar edit 0324b280-3bad-4b5d-aac7-252906024c5e

def footer():
  footer = f"Check the Credit Automator Google Sheet for more info!\n"
  footer += f"Current clubs need 50 / 150 acclaim to unlock their first / second buffs!\n"
  footer += f"In-progress clubs need 30 credits to become official!\n"
  footer += f"Updated as of November 3, 4:42 PM PST"
  return footer

def main():
  curr_clubs = {"Arcane Vocation (AV) Club": 50, "C Club": 133, "Journalism": 50, "Mortals & Mansions Club": 50, "Scenemo Kidz": 7, "Science Club": 126, "Sports Club": 93, "Thespian Society": 0}
  new_clubs = {}

  output = "Current Clubs (Alphabetically)\n"
  for club_name in curr_clubs.keys():
    output += club_name + ": " + curr_clubs[club_name]
    thresh = 50 if curr_clubs[club_name] < 50 else 150
    output += " / " + thresh + "\n"

  output += "\nIn-Progress Clubs (Alphabetically)\n"
  for club_name in new_clubs.keys():
    output += club_name + ": " + new_clubs[club_name] + " / 30\n"

  return output
