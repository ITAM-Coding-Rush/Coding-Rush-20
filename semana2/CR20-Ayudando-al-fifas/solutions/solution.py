sopita= input()
Ce=0
eRe=0
Siete=0
for i in sopita:
  if i == "C":
    Ce=Ce+1   
  if i == "R":
    eRe=eRe+1
  if i == "7":
    Siete=Siete+1
if(Ce>0 and eRe>0 and Siete>0):
  print("SIUUU")
else:
  print("Pancho está loquito")