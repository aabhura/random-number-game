import random

num = 0
def generate_random_number()
  num = random.randint(0,1000)

def difference_from_answer(guess, answer)
  if guess = answer:
    return "Correct"
  elif guess > answer:
    return "Too high"
  else:
    return "Too low"

def make_a_guess(answer)
  guess = input("Enter a number: ")
  return difference_from_answer(guess, answer)