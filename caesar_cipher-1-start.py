from distutils.command.bdist import show_formats
from main import position



alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'Decode' to decrypt:\n")

    text = input("Type you message:/n").lower()
    shift = int(input("Type the shift number: /n"))



def caeser (shift_amount,start_text,cipher_direction):


    end_text = ""

    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == "decode":
           shift_amount *= -1
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is {end_text}")

    
    caeser(shift_amount=shift,start_text=text,cipher_direction=direction)

    result = input("Type 'yes' if you want to go again. otherwise type 'no'.\n")
    if result == no:
        should_continue =False
        print("Good bye")



            






    


