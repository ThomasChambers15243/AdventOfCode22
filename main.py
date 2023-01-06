
def DayOne():

    with open("dayOneInput.txt") as dayOneInput:
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



if __name__ == '__main__':
    print(DayOne())

