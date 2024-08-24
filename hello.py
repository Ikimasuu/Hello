def main():
    name = get_name().strip()
    age = get_age().strip()
    print(f"My name is {name}, I'm {age} years old")
    
def get_name():
    return input("What's your name?! ")

def get_age():
    return input ("What's your age?")
    
main()
