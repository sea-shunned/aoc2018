from itertools import cycle
import sys

class Cart():
    # Store the tracks
    tracks = []
    # Define where to move next
    dir_symbols = {
        ">": (1, 0),
        "<": (-1, 0),
        "^": (0, -1),
        "v": (0, 1)
    }
    # Store the carts
    carts = []
    # Store the changes for each turn scenario
    turn_symbols = {
        "left": {
            "<": "v",
            ">": "^",
            "v": ">",
            "^": "<"
        },
        "straight": {
            "<": "<",
            ">": ">",
            "v": "v",
            "^": "^"
        },
        "right": {
            "<": "^",
            ">": "v",
            "v": "<",
            "^": ">"
        }
    }

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        # Create a cycle for the movement order
        self.turn_dir = cycle(["left", "straight", "right"])
        # Get the initial direction symbol
        self.direction = direction
        # Get the initial symbol with which to fill the track in after moving
        self.replace_symbol = {
            ">": "-",
            "<": "-",
            "^": "|",
            "v": "|"
        }[direction]
        # Boolean to track if a cart has crashed (then ignore it)
        self.crashed = False

    def turn(self, new_x, new_y, new_pos):
        # Get the new direction for the appropriate turn
        if new_pos == "+":
            self.direction = self.turn_symbols[next(self.turn_dir)][self.direction]
        # Otherwise go into this mess and set the new direction
        else:
            if (self.direction == ">" and new_pos == "\\") or (self.direction == "<" and new_pos == "/"):
                self.direction = "v"
            elif (self.direction == ">" and new_pos == "/") or (self.direction == "<" and new_pos == "\\"):
                self.direction = "^"
            elif (self.direction == "v" and new_pos == "\\") or (self.direction == "^" and new_pos == "/"):
                self.direction = ">"
            elif (self.direction == "v" and new_pos == "/") or (self.direction == "^" and new_pos == "\\"):
                self.direction = "<"
            else:
                raise ValueError(f"Don't understand {self.direction} and {new_pos}")
        # Actually move the cart now the new direction is set
        self.move(new_x, new_y, new_pos)

    def move(self, new_x, new_y, new_pos):
        # Replace the track with the right (old) symbol
        Cart.tracks[self.y][self.x] = self.replace_symbol
        # Store the next symbol to fill in
        self.replace_symbol = Cart.tracks[new_y][new_x]
        # Store new coordinates
        self.x = new_x
        self.y = new_y
        # Update the tracks with the cart symbol
        Cart.tracks[self.y][self.x] = self.direction
    
    def step(self):
        # Get the new position
        delta_x, delta_y = Cart.dir_symbols[self.direction]
        new_x, new_y = self.x + delta_x, self.y + delta_y
        # Get the symbol at the new position
        new_pos = Cart.tracks[new_y][new_x]
        # Depending on this position, do the appropriate thing
        # Crash
        if new_pos in "><v^":
            print(f"Crash at {new_x},{new_y}")
            # Replace the cart
            Cart.tracks[self.y][self.x] = self.replace_symbol
            # Set the crashed flag
            self.crashed = True
            # Check which other carts are involved
            for cart in Cart.carts:
                if (cart.x == new_x and cart.y == new_y):
                    # Replace the cart
                    Cart.tracks[cart.y][cart.x] = cart.replace_symbol
                    # Set the crashed flag
                    cart.crashed = True
        # Turn
        elif new_pos in "\\/+":
            self.turn(new_x, new_y, new_pos)
        # Simple move
        elif new_pos in "|-":
            self.move(new_x, new_y, new_pos)
        else:
            raise ValueError(f"Unrecognised symbol: {new_pos}")
        
    @classmethod
    def update_carts(cls):
        # Each cart steps one-by-one
        for cart in cls.carts:
            # Only look at those still not crashed
            if not cart.crashed:
                cart.step()
        # Order the carts top-down, left-right
        cls.carts = sorted(cls.carts, key= lambda cart: (cart.y, cart.x))
        # Keep a counter of how many uncrashed carts we have after each tick
        cls.alive = len([i for i in cls.carts if not i.crashed])

    @classmethod
    def initialise_carts(cls):
        # Create the cart instances
        for y, line in enumerate(cls.tracks):
            for x, val in enumerate(line):
                if val in "^v><":
                    cls.carts.append(cls(x, y, val))

# Read in the data
with open("input.txt","r") as f:
    data = f.read().splitlines()
# Store the tracks
for line in data:
    Cart.tracks.append(list(line))
# Initialise the carts
Cart.initialise_carts()
# Set up alive variable
Cart.alive = len(Cart.carts)
# Keep going until 1 remains
while Cart.alive > 1:  
    Cart.update_carts()
# Get the coordinates of the survivor
for cart in Cart.carts:
    if not cart.crashed:
        print(cart.x, cart.y)
