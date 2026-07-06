computer = "rock"
player = input("Choose Rock, Paper or Scissors: ").lower()
if player == "rock":
    print("It's a tie!")
elif player == "paper":
    print("You win!")
elif player == "scissors":
    print("You lose!")
else:
    print("Invalid choice")
