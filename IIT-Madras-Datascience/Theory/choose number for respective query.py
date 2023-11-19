import time
now = time.ctime()

#starting display
print(" ========================================== ")
print("|| choose number for the respective query ||")
print("||  1) hi                                 ||")
print("||  2) how are you?                       ||")
print("||  3) what is your name?                 ||")
print("||  4) how old are you?                   ||")
print("||  5) what is the time right now?        ||")
print(" ========================================== ")
#close display

qna = {
  "1":"hey",
  "2":"I am fine",
  "3":"my name is jarvis",
  "4":"I am 19 years of age",
  "5": now,
}
while True:
  qs = input()

  if(qs == "quit"):
      break

  else:
      print(qna[qs])