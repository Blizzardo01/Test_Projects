import datetime.datetime.now() as time
#add intro
YNQ = "yes"


while YNQ == "yes":

  stamp = input("what do you want to add to the log?")
  stamp = complex(timestamp)

  log = open("log.txt", "a")
  log.write(f"{stamp}|Time Entered - {time.strftime("%c")}\n"
  log.close()

  YNQ = input("Do you want to enter anything else:")
  