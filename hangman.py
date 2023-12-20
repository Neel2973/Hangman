import random
import words
import art
end_of_game = False
word_list = words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives=6

print(art.logo)
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print("You've already entered the letter previously.")

    for position in range(word_length):
        letter = chosen_word[position]
       
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives-=1
        stages = art.stages
        print(stages[lives])
    if lives==0:
        print("You lose")
        end_of_game = True
        print(f"The correct answer is {chosen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    