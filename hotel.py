from collections import Counter
import sys

default_guest_list = ["David", "Per", "Bertil", "Arne"]


class Hotel:
    def __init__(self, name) -> None:
        self.guest_list = set()
        self.name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name) -> None:
        self._name = name

    def add_guest(self, guest) -> None:
        self._guest_list.add(guest)

    @property
    def guest_list(self) -> set:
        return self._guest_list

    @guest_list.setter
    def guest_list(self, guest_list) -> None:
        self._guest_list = guest_list

    def broadcast(self, times: int) -> str:
        return (self.name + "\n") * times


def main():
    hotel = Hotel("Lages")
    hotel.add_guest("Allan")
    hotel.add_guest("Berit")
    hotel.add_guest("Anders")
    hotel.add_guest("Bertil")
    hotel.add_guest("Berit")
    hotel.add_guest("Anders")
    hotel.add_guest("Allan")
    hotel.add_guest("Berit")
    hotel.add_guest("Arne")
    hotel.add_guest("Allan")
    hotel.add_guest("Berit")
    hotel.add_guest("Anders")
    hotel.guest_list.update(default_guest_list)
    hotel.guest_list = sorted(hotel.guest_list)
    for guest in hotel.guest_list:
        print(guest)
    # Set means no duplicates
    counter = Counter(hotel.guest_list)
    for key, value in counter.items():
        print(key, value, sep=" --> ", end=". | ")

    print(hotel.broadcast(4), end="")


if __name__ == "__main__":
     if len(sys.argv) == 1:
        main()
     else:
        if sys.argv[1] == "1":
            print("Test print!")
        elif len(sys.argv) >= 2:
            print("Input values:")
            for arg in sys.argv:
                if arg != sys.argv[0]:
                    print(arg)
        else:
            print("Instructions:", "1: test", "2: Print input", sep="\n")
