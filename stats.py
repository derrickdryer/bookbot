def get_num_words(text: str):
  words = text.split()
  return len(words)

def get_times_char(text: str):
  char_dict = {}
  
  for char in text:
    key = char.lower()
    if key in char_dict:
      char_dict[key] += 1
    else:
      char_dict[key] = 1
  return char_dict

def sort_dict(d: dict):
  new_dict = []

  for key, value in d.items():
    new_dict.append({"char": key, "num": value})

  return sorted(new_dict, key=lambda x: x["num"], reverse=True)