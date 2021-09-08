my_favorite_toy = "Giffy"
guess= " "
guess_count = 0
guess_limit = 5
out_of_guesses = False

print("Welcome to My Favorite Toy Guessing Game!")

while guess != my_favorite_toy and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter your guess: ")
        guess_count +=1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Oops sorry! You are out of guesses")
else:
    print('Yay! Congratulations! You Win!')
