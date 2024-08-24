def main():
    name = get_name().strip()
    print(f"My name is {name}")


def get_name():
    return input("What's your name? ")

main()