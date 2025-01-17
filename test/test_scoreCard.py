from src.scoreCard import ScoreCard


def test_repr():
    assert (
        repr(ScoreCard("8/549-XX5/53639/1/X"))
        == "Tu carta es: 8/ , 54 , 9- , X , X , 5/ , 53 , 63 , 9/ , 1/ , X"
    )


def test_todonumeros():
    assert ScoreCard("12345123451234512345").calculate_score() == 60


def test_nueve_fallos():
    assert ScoreCard("9-9-9-9-9-9-9-9-9-9-").calculate_score() == 90


def test_numeros_fallos():
    assert ScoreCard("9-3561368153258-7181").calculate_score() == 82


def test_numeros_strikes():
    assert ScoreCard("5/5/5/5/5/5/5/5/5/5/5").calculate_score() == 150


def test_diferentes():
    assert ScoreCard("12345123451234512345").calculate_score() == 60
    assert ScoreCard("9-9-9-9-9-9-9-9-9-9-").calculate_score() == 90
    assert ScoreCard("9-3561368153258-7181").calculate_score() == 82
    assert ScoreCard("9-3/613/815/-/8-7/8/8").calculate_score() == 131
    assert ScoreCard("X9-9-9-9-9-9-9-9-9-").calculate_score() == 100
    assert ScoreCard("9-9-9-9-9-9-9-9-9-X9-").calculate_score() == 100
    assert ScoreCard("X9-X9-9-9-9-9-9-9-").calculate_score() == 110
    assert ScoreCard("XX9-9-9-9-9-9-9-9-").calculate_score() == 120
    assert ScoreCard("XXX9-9-9-9-9-9-9-").calculate_score() == 141
    assert ScoreCard("9-9-9-9-9-9-9-9-9-XXX").calculate_score() == 111
    assert ScoreCard("XXXXXXXXXXXX").calculate_score() == 300
    assert ScoreCard("8/549-XX5/53639/9/X").calculate_score() == 149
    assert ScoreCard("8/549-XX5/53639/1/X").calculate_score() == 141
    assert ScoreCard("X5/X5/XX5/--5/X5/").calculate_score() == 175