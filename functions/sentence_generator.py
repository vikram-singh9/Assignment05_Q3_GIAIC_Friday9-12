def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
        print("I am excited to add this", word, "to my vast collection of them!")
    elif part_of_speech == 1:
        print("It's so nice outside today it makes me want to", word + "!")
    elif part_of_speech == 2:
        print("Looking out my window, the sky is big and", word + "!")

def main():
    word = input("Please type a noun, verb, or adjective: ")
    part_of_speech = int(input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "))
    make_sentence(word, part_of_speech)

main()