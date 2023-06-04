# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name, greeting='Hello, <name>!'):
    return greeting.replace("<name>", str(name))

print(greet("Travolta"))

def force(mass, body='earth'):
    gravity_per_body = {
        'sun': 275,
        'jupiter': 24.9,
        'neptune': 11.1,
        'saturn': 10.4,
        'earth': 9.8,
        'uranus':8.9,
        'venus': 8.9,
        'mas': 3.7,
        'mercury':3.7,
        'moon': 1.6,
        'pluto':0.6,

    }
    gravity = gravity_per_body[body]
    return mass * gravity


print(force(10, 'pluto'))


def pull(m1,m2,d2):
    force = float(6.674*10**-11) * ((m1 * m2)/(d2*d2))
    return force

print(pull(800,1500,3))
