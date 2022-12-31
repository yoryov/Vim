#!/usr/bin/python3

import sys
import leopard
# another commit...
# a new change made with Vim

def add_animal(farm, animal):
    farm.add(animal)
    return farm

def main(animals):
    farm = set()
    for animal in animals:
        farm = add_animal(farm, animal)
    print("We've got some animals on the farm:",','.join(farm) + '.')

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Pass at least one animal!")
        sys.exit(1)
    main(sys.argv[1:]
