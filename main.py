# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name, greeting='Hello, <name>!'):
    greeting = greeting.replace("<name>", str(name))
      
    print(greeting)

greet("Travolta")

def force(mass, body="Earth"):
    gravity_factor = 9.8
    # if body == "Earth": gravity_factor = (9.8)
    if body == "sun": gravity_factor = (274)
    if body == "jupyter": gravity_factor = (24.9)
    if body == "neptune": gravity_factor = (11.1)
    if body == "saturn": gravity_factor = (10.4)
    if body == "uranus": gravity_factor = (8.8)
    if body == "venus": gravity_factor = (8.8)
    if body == "mars": gravity_factor = (3.7)
    if body == "mercury": gravity_factor = (3.7)
    if body == "moon": gravity_factor = (1.6)
    if body == "pluto": gravity_factor = (0.6)



    force = mass * gravity_factor
    return force

print(force(33,"Mars"))
print(force(33,"Earth"))

def pull(m1,m2,d2):
    force = float(6.674*10**-11) * ((m1 * m2)/(d2*d2))
    return force

print(pull(800,1500,3))