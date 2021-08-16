from application.get_b_score_service import GetBScoreService


def test_get_b_score_then_return_score():
    score = GetBScoreService().get_score("토스")
    assert isinstance(score, str)