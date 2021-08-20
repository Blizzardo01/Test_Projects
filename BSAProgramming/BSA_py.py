 
#...initialize looping variable, assume 'yes' as the first answer
continueYN = "yes"
 
while continueYN == "yes":
   #...get temperature input from the user
   sDegreeF = input("Enter next temperature in degrees Fahrenheit (F):")
 
   #...convert text entry to number value that can be used in equations
   nDegreeF = int(sDegreeF)
 
   #...convert temperature from F to Celsius
   nDegreeC = (nDegreeF - 32) * 5 / 9
 
   print (f"Temperature in degrees C is:{nDegreeC}")
 
   #...check for temperature below freezing..
   if nDegreeC < 0:
      print ("Pack long underwear!")

   if nDegreeF == 50:
       print("Ahh, just right...")   
 
   #...check for it being a hot day...
   if nDegreeF > 80:
      print ("Remember to hydrate!")
 
   continueYN = input("Input another?")
#exit the program