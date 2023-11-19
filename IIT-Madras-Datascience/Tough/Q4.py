string = input()
if (len(string) % 2) != 0:
    word = string
else:
  if (string.endswith(".")):
    word = string.rstrip(".")
  else:
    word = string + "."
print(word[(len(word) // 2)-1:(len(word) // 2)+2])