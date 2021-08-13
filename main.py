import random

class Main:
    def __init__(self):
        self.count = 0
        self.nums = []
        self.win = False


    def init(self):
        while True:
            temp = input("How many digits?").replace(" ", "")
            if not self.isNumber(temp):
                print("Not a number.")
                continue

            temp = int(temp)
            if temp <= 0:
                print("Numbers below 0 are not possible.")
                continue
            if 10 <= temp:
                print("The maximum number is 9 digits.")
                continue

            self.count = temp
            self.makeAnswerNumber(self.nums, self.count, 1, 9)
            break


    def makeAnswerNumber(self, lst, cnt, min, max):
        while len(lst) < cnt:
            n = random.randint(min, max)
            if n in lst:
                continue
            lst.append(n)


    def run(self):
        self.init()
        print("Rule: A game of matching the number created using N natural numbers between 1 and 9.")
        print("Same number not used multiple times.")
        print("Start Numeric Baseball.")
        self.play()


    def play(self):
        while not self.isWin():
            numbers = self.getNumbersToTry()
            result = self.check(numbers)
            self.printResult(result)
            if result["strike"] == self.count:
                self.gameWin()


    def getNumbersToTry(self):
        while True:
            temp = self.enterNumber()
            if temp:
                return temp


    def enterNumber(self):
        number = input("Enter %d number(s): " % self.count).replace(" ", "")
        if not self.isNumber(number):
            print("Not a number.")
            return False
        if not self.checkLenNumber(number):
            print("Not a number of exact lengths.")
            return False
        if self.isDuplicatedNumber(number):
            print("Duplicate number found.")
            return False
        if self.zeroInNumber(number):
            print("Has zero.")
            return False
        return number


    def isNumber(self, number):
        try:
            int(number)
        except:
            return False
        return True


    def checkLenNumber(self, number):
        if len(str(number)) != self.count:
            return False
        return True


    def isDuplicatedNumber(self, numbers):
        numList = self.ChangeNumberIntoInt(numbers)
        for i in range(len(numList)):
            for j in range(len(numList)):
                if i != j and numList[i] == numList[j]:
                    return True
        return False


    def zeroInNumber(self, number):
        if "0" in number:
            return True
        return False


    def check(self, numbers):
        numList = self.ChangeNumberIntoInt(numbers)
        print("Your numbers : ", end='')
        print(numList)
        strikeCnt = self.countStrike(numList)
        ballCnt = self.countBall(numList)
        return {"strike": strikeCnt, "ball": ballCnt}


    def ChangeNumberIntoInt(self, numbers):
        return list(map(int, list(str(numbers))))


    def countBall(self, numList):
        ball = 0
        for i in range(len(self.nums)):
            for j in range(len(numList)):
                if i != j and self.nums[i] == numList[j]:
                    ball += 1
        return ball


    def countStrike(self, numList):
        strike = 0
        for i in range(len(self.nums)):
            if self.nums[i] == numList[i]:
                strike += 1
        return strike


    def printResult(self, result):
        if result["ball"] == 0:
            print("No ball ", end="")
        else:
            print("%d Ball(s) " % result["ball"], end="")

        if result["strike"] == 0:
            print("No Strike")
        else:
            print("%d Strike(s)" % result["strike"])


    def gameWin(self):
        print("It's correct!")
        self.win = True


    def isWin(self):
        return self.win


if __name__ == "__main__":
    main = Main()
    main.run()