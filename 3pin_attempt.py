pin = 4321
attempt = 0
while True:
  attempt +=1
  pin = int(input("Enter PIN: "))
  if pin == 4321:
      print("Access granted")
      break
  print("Incorrect PIN")
  if attempt == 3:
      print("Account locked")
      break