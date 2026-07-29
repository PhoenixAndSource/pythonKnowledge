from anonymous_poll import AnonymousPoll

# Decide on your poll question, and create a survey.
poll_question = "What is your favorite childhood dessert?"
dessert_poll = AnonymousPoll(poll_question)

# Show the poll question, and store votes to poll_question.
dessert_poll.show_poll_question()
print("Enter 'quit' anytime to quit.\n")
while True:
    vote = input("Dessert: ")
    if vote == 'quit':
        break
    dessert_poll.store_poll_votes(vote)

# Show poll outcome.
print("\nThank you for sharing your vote!")
dessert_poll.show_outcome()
