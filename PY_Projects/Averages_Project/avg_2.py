toadd = "y"
goagain = "y"
ScoreList = []

def calculation(test_score, possible_points):
    test_score = input(int())
    possible_points = input(int())

    

#beginning
print("This Program Calculates your average percentage based on your scores \n Formula = Score Earned Total Possible points")

while goagain == "y".lower():

    while toadd == "y".lower():
        Score1, Score2 = [int(Score1) for Score1 in input("add a score").split()]
        final_percentage = Score1 / Score2 * 100
        addtolist = ScoreList.append(final_percentage)

        
        toadd = input("Would you like to add another score?")

    print(f"Your Calculated Average is {final_percentage}")
goagain = input("Would you like to go again?")