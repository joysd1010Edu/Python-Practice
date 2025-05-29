computer=-1;
library={
    "rock":-1,
    "paper":0,
    "scissors":1
}
reversedLibrary={
    -1:"rock",
    0:"paper",
    1:"scissors"
}
while True:
    player=input("Enter 'exit' to exit\nEnter rock, paper, or scissors: ").lower()
    if player=='exit':
        print("Exiting the game.")
        break
    elif player not in library:
        print("Invalid input. Please enter rock, paper, or scissors.")
        continue
   
    print(f"computer chose {reversedLibrary[computer]} and you chose {reversedLibrary[library[player]]}.")
    if library[player] == computer:
        print("It's a tie!")
    elif library[player] == computer + 1 or (library[player] == computer - 2):
        print("You win!")
    else:
        print("You lose!")




