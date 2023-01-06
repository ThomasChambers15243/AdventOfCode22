
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
        player = ['X','Y','Z']
        points = { "player" : 6, "opp" : 0, "draw" : 3}
        rounds = []
        score = 0

        # Read lines and remove \n
        for line in daysInput:
            rounds.append(line[:-1])

        # Calculate score for each round and add it to the running total for the player
        for round in rounds:
            oppTurn = opp.index(round[0])
            playerTurn = player.index(round[2])
            total = oppTurn + playerTurn

            # Calculate the result
            # ROCK 1
            # PAPER 2
            # SCISSORS 3
            #
            #
            # 0 + 1 = 1
            # 0 + 2 = 2
            # 1 + 2 = 3

            if total == 2*oppTurn:
                result = 'draw'
            elif total == 1:
                if oppTurn == 0:
                    result = 'player'
                else:
                    result = 'opp'
            elif total == 2:
                if oppTurn == 0:
                    result = 'opp'
                else:
                    result = 'player'
            else:
                if oppTurn == 1:
                    result = 'player'
                else:
                    result = 'opp'

            if result != "opp":
                score += points[result]
            score += playerTurn+1

        return(score)

if __name__ == '__main__':
    #print(DayOne("dayOneInput.txt"))
    print(DayTwo("dayTwoInput.txt"))

