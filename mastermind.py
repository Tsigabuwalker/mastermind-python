import random

class Mastermind:
    def __init__(self):
        self.colors = ['R', 'G', 'B', 'Y', 'O', 'P']  # Red, Green, Blue, Yellow, Orange, Purple
        self.code_length = 4
        self.secret_code = self.generate_code()

    def generate_code(self):
        return [random.choice(self.colors) for _ in range(self.code_length)]

    def get_feedback(self, guess):
        correct_position = sum(1 for i in range(self.code_length) if guess[i] == self.secret_code[i])
        correct_color = sum(min(guess.count(color), self.secret_code.count(color)) for color in set(guess)) - correct_position
        return correct_position, correct_color

    def play(self):
        print("Welcome to Mastermind!")
        print("Guess the color code using the following colors:")
        print(", ".join(self.colors))
        print("Type your guess as a sequence of letters (e.g., RGBY).")
        
        attempts = 10
        while attempts > 0:
            guess = input(f"You have {attempts} attempts left. Enter your guess: ").upper()
            
            if len(guess) != self.code_length or any(c not in self.colors for c in guess):
                print(f"Invalid input. Please enter exactly {self.code_length} colors from {', '.join(self.colors)}.")
                continue
            
            correct_position, correct_color = self.get_feedback(guess)
            print(f"Correct colors in the correct position: {correct_position}")
            print(f"Correct colors in the wrong position: {correct_color}")

            if correct_position == self.code_length:
                print("Congratulations! You've guessed the correct code!")
                break

            attempts -= 1

        if attempts == 0:
            print(f"Sorry, you've run out of attempts. The secret code was: {''.join(self.secret_code)}")

if __name__ == "__main__":
    game = Mastermind()
    game.play()