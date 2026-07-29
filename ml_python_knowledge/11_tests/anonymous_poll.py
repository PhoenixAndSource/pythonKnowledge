class AnonymousPoll:
    """Gather anonymous votes for poll."""

    def __init__(self, poll_question):
        """Store poll_question, and get ready to store votes."""
        self.poll_question = poll_question
        self.poll_votes = []

    def show_poll_question(self):
        """Show the poll question."""
        print(self.poll_question)

    def store_poll_votes(self, new_vote):
        """Store a vote for the poll."""
        self.poll_votes.append(new_vote)

    def show_outcome(self):
        """Show all the votes that we have received."""
        print("Poll results.")
        for vote in self.poll_votes:
            print(f"- {vote}")



