import random

# defined variables
name = input("Write your name: ")
question = input("Ask a question that you can answer with yes or no: ")
answer = ""

# getting random number
random_number = random.randint(1, 11)

# defining control flow
if random_number == 1:
    answer = "Yes - definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
elif random_number == 10:
    answer = "Not really"
elif random_number == 11:
    answer = "Never."
else:
    answer = "Error"

# defining control flow for case that there is no name
if name == "":
    name = "Anonym"

# defining a control flow for case that there is no question
if question == "":
    question = "Please ask a question"

print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answer)
