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
    player=input("Enter rock, paper, or scissors: ").lower()
   
    print(f"computer chose {reversedLibrary[computer]} and you chose {reversedLibrary[library[player]]}.")
    if library[player] == computer:
        print("It's a tie!")
    elif library[player]==computer+1 or (library[player]==computer+2):
        print("You win!")
    elif library[player]==computer-1 or (library[player]==computer-2):
        print("You lose!")
    elif player=='exit':
        print("Exiting the game.")
        break
    else:
        print("Invalid input. Please enter rock, paper, or scissors.")
        continue



