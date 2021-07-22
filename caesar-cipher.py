
def encrypt(direction_in , plain_text, shift_number):
  cipher_text = ""
  if direction_in == "decode":
    shift_number *= -1
  for letter in plain_text:
    if letter in alphabet:
      letter_index = alphabet.index(letter)
      new_index = letter_index + shift_number
      cipher_text += alphabet[new_index]
    else:
      cipher_text += letter
    #print(alphabet[new_index], end = "")
  print(f"The {direction_in}d text is {cipher_text}")




alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 25

  encrypt(direction, text, shift)

  user_input = input("Do you want to continue type YES or NO :").lower()

  if user_input =="no":
    should_continue = False
