import datetime
#...initialize looping variable, assume 'yes' as the first answer
date = datetime.datetime.now()
continueYN = "yes"
 
while continueYN == "yes":
   #...get temperature input from the user
   sDegreeF = input("Enter next temperature in degrees Fahrenheit (F):")


   #writing the inputed temperature to the log-- "log.txt"
   log = open("log.txt", "a")
   log.write("Temperature entered: {}F|time: {}\n".format(sDegreeF, date.strftime("%c")))
   log.close()
   #...convert text entry to number value that can be used in equations
   nDegreeF = int(sDegreeF)
 
   #...convert temperature from F to Celsius
   nDegreeC = (nDegreeF - 32) * 5 / 9
 
   print ("Temperature in degrees C is:{}".format(nDegreeC))
 
   #...check for temperature below freezing..
   if nDegreeC < 0:
      print ("Pack long underwear!")

   if nDegreeF == 50:
       print("Ahh, just right...")   
 
   #...check for it being a hot day...
   if nDegreeF > 80:
      print ("Remember to hydrate!")
 
   continueYN = raw_input("Input another?")
   #print (continueYN4)
#exit the program
