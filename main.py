# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

gravitational_constant = 6.674E-11

gravity_dict = {
    "sun": 274.0,
    "jupiter": 24.9, 
    "neptune": 11.2,
    "saturn": 10.4,
    "earth": 9.8,
    "uranus": 8.9,
    "venus": 8.9,
    "mars": 3.7,
    "mercury": 3.7,
    "moon": 1.6,
    "pluto": 0.6
}

# Part 1: Greet Template
def greet(fName, fGreet = "Hello, <name>!"):
    fResult = fGreet.replace("<name>", fName)
    return fResult

# Part 2: Force
def force(mass, body = "earth"):
    fGravity = gravity_dict.get(body)
    return (mass * fGravity)

# Part 3: Gravity
def pull(m1, m2, d):
    fResult = gravitational_constant * ((m1 * m2) / d**2)
    return fResult

# -----------------------------------------------------------------------------------------------
# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.

if __name__ == "__main__":
    # Part 1:
    print(greet('Doc'))
    print(greet('Bob', "What's up, <name>!"))

    # Part 2: 
    print(force(10, "earth"))
    print(force(10, "moon"))

    # Part 3:
    print(pull(800, 1500, 3))
    print(pull(0.1, 5.972E+24, 6.371E+6))

