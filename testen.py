import json

items = json.loads('[{"id":1, "text": "Item 1"}, {"id":2, "text": "Item 2"}, {"id":3, "text": "Item 3"}]')
for item in items:
    print(item['text']) 

def greet(greeting, name):
    """Return a Greeting

    Args:
        greeting (String): Een groet
        name (String): Een naam

    Returns:
        string: een groet met een naam
    """
    return f'{greeting} {name}' 

print(greet('Hallo', 'wereld'))