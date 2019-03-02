def alphabet_position(letter):
    return ord(letter)

def rotate_character(char, rot):
    if len(char) == 1:
        if char.isalpha():
            index = alphabet_position(char) #get ascii number of char
            rot_index = (index + rot) #shift char to the right by rot
            if char == char.lower(): #figure out if char is uppercase or lowercase       
                while rot_index > 122:
                    rot_index = rot_index - 26
            else:
                while rot_index > 90:
                    rot_index = rot_index - 26
            return chr(rot_index)
        else:
            return char