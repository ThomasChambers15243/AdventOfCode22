
def DayOne(input):

    with open(input) as dayOneInput:
        # Lines of input and individual elfs cals
        lines = []
        elfCal = []

        # Read input lines into lines[]
        for line in dayOneInput:
            if line == '\n':
                lines.append(-1)
            else:
                lines.append(int(line[:-1]))

        # Find total of individual elf cals and load them into elfCal
        runningTotal = 0
        lines.append(-1)
        for el in lines:
            if el > -1:
                runningTotal += el
            else:
                elfCal.append(runningTotal)
                runningTotal=0

        # Find the top 3 elfs with largest cal total and return it
        stack = []
        for i in range(3):
            largestTotal = 0;
            for j in range(0,len(elfCal)):
                if elfCal[j] > largestTotal:
                    largestTotal = elfCal[j]
                    location = j
            stack.append(largestTotal)
            del(elfCal[location])

        return (stack[-1] + stack[-2] + stack[-3])
def DayTwo(input):
    with open(input) as daysInput:

        # ROCK PAPER SCISSORS
        opp = ['A','B','C']
        points = { "win" : 6, "loose" : 0, "draw" : 3}

        # Points for the hands that would be played
        lossingHandPoints = {"A" : 3, "B" : 1, "C" : 2}
        winningHandPoints = {"A" : 2, "B" : 3, "C" : 1}

        rounds = []
        score = 0

        # Read lines and remove \n
        for line in daysInput:
            rounds.append(line[:-1])

        # Calculate score for each round and add it to the running total for the player
        # X == Loose
        # Y == Draw
        # Z == Win

        for round in rounds:
            oppTurn = round[0]
            playerTurn = round[2]

            # Loose
            if playerTurn == 'X':
                score += lossingHandPoints[oppTurn]
            # Draw, plus one so that index represents value of hand played
            elif playerTurn == 'Y':
                score += opp.index(oppTurn) + points["draw"] + 1
            # Win
            else:
                score += winningHandPoints[oppTurn] + points["win"]
        return(score)
def DayThree(input):
    with open(input) as fInput:
        # Holds all commons in rucksack
        totalCommons = []

        # GetLines into their rucksack
        for rucksack in fInput:
            # Split each rucksack into its compartmeants
            firstHalf = rucksack[: int(((len(rucksack))/2))]
            secondHalf = rucksack[len(firstHalf): ]

            # Holds common types between the two halfs
            compartmeantCommons = []

            for i in firstHalf:
                for j in secondHalf:
                    if i == j and i not in compartmeantCommons:
                        compartmeantCommons.append(i)

            # Allows for more than one common item
            for i in compartmeantCommons:
                totalCommons.append(i)

        # Find and total up the priority of each common item
        totalCount = 0
        for char in totalCommons:
            # Lower Case, else Upper
            # Subtract a part so that their natural ascii numbers make up their values
            if ord(char) > 90:
                totalCount+= ord(char) - 96
            else:
                totalCount+= ord(char) - 38
    # Return Total
    return totalCount

if __name__ == '__main__':
    # print(DayOne("inputs/dayOneInput.txt"))
    # print(DayTwo("inputs/dayTwoInput.txt"))
    print(DayThree("inputs/dayThreeInput.txt"))

