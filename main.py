print(" Welcome to the Rollercoast ! ")
height = int (input(" Enter your height in cm : "))

if height >= 120 :
   print (" You can ride ! ")
   age = int(input(" Enter your age : "))

   if age <= 12 :
    print(" Please pay 5$ ")
   elif age <= 18 :
    print(" Please pay 10$ ")  
   elif age <= 22 :
    print(" Please pay 15$ ")

   else :   
    print(" Please pay 20$ ")
   
else:
 print (" Sorry ! you can't ride. ")    