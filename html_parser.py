''' from test_snippets import main '''

import requests
from bs4 import BeautifulSoup
import re

def correctUrl(URL):
    if re.search("(\W|^)http(\W|$)", str(URL), re.IGNORECASE):
        return URL
    else:
        return "https://" + URL
    
def findInfoOnSite():
    
    """ "https://www.wartem.se" """
    while(True):
        print("Welcome")
        print("Enter a menu or feature by typing the corresponding number")
        print("Write 'Quit' to exit")
        print("1. Print a site page's HTML")
        print("2. Print header of class")
        menu = input("Write a menu number ").strip()
        className = ""
        
        if menu == "Quit":
            print("Break")
            break
        
        if(menu == "1" or menu == "2"):
            base_url = input("Enter website adress/URL: ")
            base_url = correctUrl(base_url)
            print("Searching " + base_url)
        
            r = requests.get(base_url)
            soup = BeautifulSoup(r.content,'html.parser')
        
        if menu == "1":
            print("HTML code:\n" + soup.prettify())
        elif menu == "2":
            try:
                className = input("Enter a class name ")
                h2 = soup.find(class_=className).h2

                if(h2):
                    print(f"First {className} found H2: " + h2) if h2.text else print("No H2 found")
                    for classSearched in soup.find_all(class_=className): 
                        print(f"{len(classSearched)} {className}")
                        if classSearched.h3: 
                            """ print(classSearched.h3.text.replace("\n", " ").strip()) """
                            print("H3 = " + classSearched.h3.text)
                        else: 
                            print("contents: " + classSearched.contents[0].strip())
                else:
                    print(f"No '{className}' H2 found")
            except:
                print("Something went wrong.") 
        
        print("findInfoOnSite done")

if __name__ == "__main__":
    print("Run functions from other files")