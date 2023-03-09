def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()


def encode(password):
    encoded_password = ""
    for char in password:
        char = int(char) + 3
        if char >= 10:
            char -= 10
        encoded_password += str(char)
    return encoded_password


if __name__ == "__main__":
    while True:
        menu()
        print("Please enter an option: ", end="")
        option = int(input())
        if option == 1:
            print("Please enter your password to encode: ", end="")
            password = input()
            encoded_password = encode(password)
            # encode password
            print("Your password has been encoded and stored!")
            print(encoded_password)
        elif option == 2:
            # decode encoded_password
            pass
        elif option == 3:
            break
