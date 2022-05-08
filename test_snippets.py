""" Usage from terminal: python -m pytest """

import snippets
import sys

snippet = snippets.PySnippets()


def main():
    print("Start assertion tests")
    #assert 
    snippet.swapNumbers(10, 5)
    #assert 
    snippet.factorial(50)
    #assert 
    snippet.isNumberPrimeCalc(36)
    #assert 
    snippet.isNumberPrime(95)
    #assert 
    snippet.getFibonacciNumber(9)
    #assert 
    snippet.findTheNextLowestNumber([2,4,1,6,7,8,4,3,2,4])
    #assert 
    snippet.removeWhiteSpaces("Remove White Spaces From This String")
    #assert 
    snippet.reverseString("Python")
    #assert 
    snippet.stringContainsVowel("Konstantinopelopansk")
    #assert 
    snippet.checkIfStringContainsAnotherString("Lambert", "Amber")
    #assert 
    snippet.sortList()
    #assert 
    print(snippet.reverseDictionary())
    #assert 
    snippet.mergeTwoLists(["Klas", "Anders"], ["Sven", "Nils, Börje"])
    #assert 
    snippet.getTodaysDate()
    #assert 
    snippet.randomizeNames()
    #assert 
    snippet.countWordsInfile()
    #assert 
    print(snippet.translatePhrase("Lektion"))
    #assert 
    snippet.isEmailValid()
    #assert
    snippet.writeToFile()

def RunOther():
    snippet.findInfoOnSite("https://www.wartem.se")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if(sys.argv[1] == "2"):
            RunOther()
        else:
            print("Unknown command")
    else:
        main()
