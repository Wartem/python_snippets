from collections import defaultdict
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import datetime
import functools
import numpy as np

import matplotlib.pyplot as plt

mod_pages = [
    "https://gta5-mods.com/scripts/vehicle-remote-central-locking",
    "https://gta5-mods.com/scripts/family-friendly-free-roaming",
    "https://gta5-mods.com/scripts/neutralized-adult-textures",
    "https://gta5-mods.com/scripts/spawn-where-you-died",
    "https://gta5-mods.com/scripts/team-up",
    "https://gta5-mods.com/scripts/tunable-home-radio",
    "https://gta5-mods.com/scripts/cautious-drivers",
    "https://gta5-mods.com/scripts/auto-skip-radio-stations",
    "https://gta5-mods.com/scripts/muted-speech-and-pain",
    "https://gta5-mods.com/scripts/playercannotbedraggedout",
]


def pauser(base_func):
    @functools.wraps(base_func)
    def extended_func(*args):
        # print("sleeping!")
        time.sleep(2)
        # print("awake!")
        return base_func(*args)

    return extended_func


def get_num_in_str(num_str):
    # print("before", num_str)
    num_str = num_str.replace(".", "").replace(",", "")
    # print("after", num_str)
    return int(re.search("\d+", num_str).group(0))


@pauser
def check_page(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, "html.parser")

    mod = soup.find(class_="col-sm-7 col-lg-8")

    num_comments = mod.find(class_="nav nav-tabs").text
    num_comments = get_num_in_str(num_comments)

    num_downloads = mod.find(class_="num-downloads").text
    num_downloads = get_num_in_str(num_downloads)

    return {
        "Datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Mod": url[url.rfind("/") + 1 :].title(),
        "Downloads": num_downloads,
        "Comments": num_comments,
    }


def save_to_csv(dict_: dict, day_):
    dataFrame = pd.DataFrame(dict_, index=[day_])
    dataFrame.to_csv("mod_stats.csv", mode="a", header=False)


def run_mod_pages():
    # hash_ = hex(hash(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    day_ = datetime.datetime.now().strftime("%Y-%m-%d")
    time_ = datetime.datetime.now().strftime("%H:%M:%S")

    total = len(mod_pages)
    for i, url in enumerate(mod_pages):
        print(f"{(i/total)*100}% done.")
        dict_ = check_page(url)
        save_to_csv(dict_, day_)


def matplotout():
    df = pd.read_csv("mod_stats.csv")

    mod_dict = {} #defaultdict(list)
    
    all_mod_names = df["Name"].unique()

    for i in range(len(df) - 1):
        date_ = df.iloc[i, 0]
        mod_name = df.iloc[i, 2]
        num_of_comments = df.iloc[i, 4]
        
        mod_dict.setdefault(mod_name, []).append([date_, num_of_comments])
    
    for name in all_mod_names:
        for mod in mod_dict[name]:
            date_ = mod[0]
            num_of_comments = mod[1]
            print(date_, name, "comments:", num_of_comments)
            
        #print([s[1] for s in mod_dict[name]], name)
        col = (np.random.random(), np.random.random(), np.random.random())
        plt.plot([s[0] for s in mod_dict[name]], [s[1] for s in mod_dict[name]], color=col, label=name)
        # linestyle="dashed", marker='x'
            
        print("\n" * 2)

    plt.xticks(rotation=25)
    plt.xlabel("Dates")
    plt.ylabel("Number of comments")
    plt.title("Mod Comments Report", fontsize=20)
    plt.grid()
    plt.legend()
    plt.show()
    

def main():

    run_mod_pages()
    matplotout()
    
if __name__ == "__main__":
    main()
