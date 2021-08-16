from application.get_investment_money_service import GetInvestmentMoneyService


def test_get_investment_money_service():
    money = GetInvestmentMoneyService().get_money("큐피스트")
    assert isinstance(money, str)