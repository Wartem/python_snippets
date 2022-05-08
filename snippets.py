import re
from datetime import date
import random
import sys

class PySnippets:

    def swapNumbers(self, a, b):
        print("a = " + str(a) + ". " + "b = " + str(b))
        a = a + b
        b = a - b
        a = a - b
        print("After swap: a = " + str(a) + ". " + "b = " + str(b))
        return True

    def factorial(self, num):
        if num == 1:
            return 1
        else:
            return num * self.factorial(num - 1)

    def isNumberPrimeCalc(self, num):
        if num == 0 or num == 1:
            return False
        if num == 2:
            return True

        for i in range(2, num, 1):
            if num % i == 0:
                return False
            else:
                return True

    def isNumberPrime(self, num):
        if self.isNumberPrimeCalc(num):
            print(f"Yes, {num} is a prime")
        else:
            print(f"No, {num} is not a prime")

    def getFibonacciNumber(self, num):
        if num <= 1:
            return num
        return self.getFibonacciNumber(num-1) + self.getFibonacciNumber(num-2)

    def findTheNextLowestNumber(self, a_list):
        lowestNum = sys.maxsize
        secondLowestNum = sys.maxsize

        for num in a_list:
            if int(float(num)) < lowestNum:
                secondLowestNum = lowestNum
                lowestNum = num
            elif int(float(num)) < secondLowestNum:
                secondLowestNum = num

        print(f"The second lowest number is {secondLowestNum}")
        print(f"The lowest number is {lowestNum}")

    def removeWhiteSpaces(self, string):
        print(re.sub("\s,", "", string))

    def reverseString(self, string):
        print("Reverse string:")
        print(f"{string} reversed is {string[::-1]}")

    def stringContainsVowel(self, string):
        print("True, Contains Vowel") if re.search(
            ".+[aeiou].*", string) else print("False, Contains Vowel")
        """ if re.search(".+[aeiou].*", string): print("True")  """
        """ else: print("False") """

    def checkIfStringContainsAnotherString(self, string, substring):
        print(f"Yes, {string} contains {substring}") if substring in string else print(
            f"No, {string} does not contain {substring}")

    def sortList(self):
        a_list = [24, -11, 73, 2, -66, -36, -84, 9]
        print(sorted(a_list, reverse=False))

    def reverseDictionary(self):
        x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
        return dict(sorted(x.items(), key=lambda item: item[1]))

    def mergeTwoLists(self, list1, list2):
        print(list1 + list2)

    def getTodaysDate(self):
        today = date.today()
        print("Today's date is: ", today)

    def randomizeNames(self):
        friends = [
            'Berit',
            'Karl',
            'Ricky',
            'Steve',
            'Keith',
            'Mario',
            'Roger',
            'Amy']

        print(random.choice(friends))

    def translatePhrase(self, phrase):
        translation = ""
        for letter in phrase:
            """ if letter in "AEIOUaeiou": """
            if letter.lower() in "aeiou":
                if letter.isupper():
                    translation = translation + "G"
                else:
                    translation = translation + "g"
            else:
                translation = translation + letter
        return translation

        """ print(translate(input("Enter a phrase: "))) """

    def isEmailValid(self):
        email = input("What's your .edu email? ").strip()

        """ . means something after it. """
        """ ..* means 0 or more characters """
        """ .+ means one or more after it. """
        """ .* means 0 or more after it. """
        """ \ escape char """
        """ ^ means start of string. """
        """ $ matches the end of the string or just before the newline at the end of the string. """

        if re.search("^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
            print(f"{email} " + "is valid")
        else:
            print(f"{email} " + "is not valid")
            
    def countWordsInfile(self):
        dictT = dict()
        textFile = open("example_text.txt", "r")
        """ lines = textFile.readlines() """

        lines = textFile.read()
        textFile.close()
        words = lines.split()
        """  if word not in dictT: """

        for word in words:
            dictT[word] = dictT.get(word, 0) + 1
            
        dictT = dict(sorted(dictT.items(), key=lambda item: item[1]))
        for key, value in dictT.items():
            print(key, '->', value)
            
        return len(dictT) > 0
            
    def writeToFile(self):
        file = open("testfile.txt","w") 
        file.write("Hello World \n") 
        file.write("This is a new text file.") 
        file.close() 
            
    

