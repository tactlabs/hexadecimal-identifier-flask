import re

def hexa_check(color):
     # Your Hex

    match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color)

    if match:                      
        return True
    return False

k = hexa_check("#00FFFF")
print(k)