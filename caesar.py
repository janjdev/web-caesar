from helpers import alphabet_position, rotate_character

def encrypt(mess, num):
    encryption = ""
    for char in mess:
        encryption += rotate_character(char, num)
    return encryption

def main():
    mess = input("Please, enter your message. ")
    num = int(input("Please, enter a number for encryption. "))
    print(encrypt(mess, num))

if __name__ == "__main__":
    main()
    
