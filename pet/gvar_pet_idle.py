!gvar edit 49a609a7-05c0-453a-bace-c1282fd79775

# This module generates commentary strings for idle pets.

content = {"0": " nuzzles your shoulder!", "1": " grins at you! ...well, to the best of its ability.", "2": " lays down on your lap!"}
hungry = {"0": " tries to get into your pockets.", "1": " gazes wistfully at your hand.", "2": " scratches at the floor."}
bored = {"0": " runs in circles in front of you.", "1": " jumps at you, nearly bowling you over!", "2": " tries to tug you somewhere."}
lonely = {"0": " lays down at your feet.", "1": " mopes listlessly.", "2": " whines at you."}
middle = {"content": content, "hungry": hungry, "bored": bored, "lonely": lonely}
suffix = {"content": "They seem very happy to see you! Good job!", "hungry": "Seems like they're waiting for food! Perhaps you should find some to __feed__ them?", "bored": "If they're that bored, maybe some __exercise__ would do some good?.", "lonely": "They seem lonely. Give 'em some attention and __play__ with 'em!"}

def get_idle(name, mood):
  idx = str(randint(0,3))
  mid_str = middle[mood][idx]
  last_str = suffix[mood] if (mood == "content") else "Hint: ||" + suffix[mood] + "||"
  return f"{name}{mid_str}\n{last_str}\n"