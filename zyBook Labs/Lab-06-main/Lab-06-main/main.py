def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encode(password):
    encoded_password = ""
    for char in password:
        # Convert the character to an integer and add 3
        new_char = (int(char) + 3) % 10

        # Append the new character to the encoded password
        encoded_password += str(new_char)

    return encoded_password


def decode(password):  # decodes encoded password
    decoded_password = ""
    for char in password:  # takes each number in encoded password
        char = int(char)
        if char < 3:
            char += 10  # ensures that there are no negatives
        char -= 3
        decoded_password += str(char)  # adds to empty string
    return decoded_password  # returns decoded password


if __name__ == "__main__":
    while True:
        menu()
        print("Please enter an option: ")
        option = int(input())
        if option == 1:
            print("Please enter your password to encode: ")
            password = input()
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
            print(encoded_password)
        if option == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
        elif option == 3:
            break
