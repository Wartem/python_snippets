""" Usage from terminal: python -m pytest """

import snippets
import html_parser
import sys
import requests
import bs4

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
    ''' snippet.emailRegex() '''
    html_parser.findInfoOnSite()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if(sys.argv[1] == "2"):
            RunOther()
        else:
            print("Unknown command")
    else:
        main()

def replace_last(line: list) -> list:
    #return list[len(line)-1].append(l in line for l in range(len(line)-2))
    #return list[len(line)-1].append(lambda x: x )
    #[x for x in mylist if x%2 == 1]
    #return list[len(line)-1].append(x for x[:len(line)-2]) in line
    #return list(str(line[len(line)-1]))#.append([x for x in line[:-1]])
    #return [x for x in line[:-1]]
    #value_when_true if condition else value_when_false
    return line if len(line) <= 1 else list(line[-1:]) + list(line[:len(line)-1])#+ [x for x in line[:-1]]

def all_the_same(elements: List[Any]) -> bool:
    for e in range(1, len(elements)):
        if elements[e] != elements[e-1]:
            return False
    return True

#var = [expression1] if [condition] else [expression2]
#foo = [x for x in bar if x.occupants > 1]
#[thing for thing in list_of_things] 

#def all_the_same(elements: List[Any]) -> bool:
    #"return e for e range(1, len(elements))
    #return e for e in range(1, len(elements)) if elements[e] == elements[e-1]
