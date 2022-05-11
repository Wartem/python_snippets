''' from test_snippets import main '''

import requests
import bs4

def findInfoOnSite(site):
    base_url = site
    r = requests.get(base_url)
    soup = bs4.BeautifulSoup(r.text,features="html.parser")

    while(True):
        print("Welcome")
        print("Enter a menu or feature by typing the corresponding number")
        print("Write 'Quit' to exit")
        print("1. Print all of the HTML")
        print("2. Print header of class")
        menu = input("Write a menu number")
        if menu == 1:
            soup.prettify()
        elif menu == 2:
            className = input("Enter a class name")
            print(soup.find(class_=className).h2.text)
        
        for container in soup.find_all(class_=className): 
            print(f"{len(container)} containers found")
            if container.h3: 
                print(container.h3.text.replace("\n", " ").strip())
            else: 
                print(container.contents[0].strip())
        print("findInfoOnSite done")

if __name__ == "__main__":
    print("Run functions from other files")