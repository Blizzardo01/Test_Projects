from urllib.request import urlopen as open


#Customizable tags to search for
url = input("what website would you like to scrape from? ")
decode = input("What decoding method would you like to use? ")
start = input("what starting position would you like to search for? ")
end = input("what ending position would you like to search for? ")

#opening website
html = open(url)
readfile = html.read().decode(f"{decode}")

#gathering the indexes
start_index = readfile.find(f"{start}")
end_index = readfile.find(f"{end}")
startpos = start_index + len(f"{start}")
endpos = end_index + len(f"{end}")

#extracting the information
isScraping = readfile[startpos:endpos]


print("Here is the information you requested!")
print("--------------------------------------")
print(isScraping)