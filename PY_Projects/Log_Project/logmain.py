import datetime 
date = datetime.datetime.now()
#add intro
YNQ = "yes"


while YNQ == "yes":

  stamp = input("what do you want to add to the log?")
  

  log = open("log.txt", "a")
  log.write(f"{stamp}|Time Entered - {date}\n")
  log.close()

  YNQ = input("Do you want to enter anything else:")
  