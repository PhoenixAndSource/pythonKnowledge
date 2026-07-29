from anonymous_poll import AnonymousPoll

def test_store_single_vote():
    """Test that a vote is stored correctly."""
    poll_question = "What is your favorite ice cream flavour?"
    dessert_poll = AnonymousPoll(poll_question)
    dessert_poll.store_poll_votes('Matcha')
    assert 'Matcha' in dessert_poll.poll_votes


import pytest
from anonymous_poll import AnonymousPoll

@pytest.fixture
def dessert_poll(): 
    """A poll available to all test functions."""
    poll_question = "What is your childhood dream dessert?"
    dessert_poll = AnonymousPoll(poll_question)
    return dessert_poll
def test_store_single_vote(dessert_poll):
    """Test that single vote is store correctly."""
    dessert_poll.store_poll_votes('in the clouds')
    assert 'in the clouds' in dessert_poll.poll_votes

def test_store_three_votes(dessert_poll):
    """Test that three votes are stored correctly."""
    votes = ['Matcha', 'Red Bean Ice', 'Lychee']
    for vote in votes:
        dessert_poll.store_poll_votes(vote)

    for vote in votes:
        assert vote in dessert_poll.poll_votes