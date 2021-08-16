from application.get_b_score_service import GetBScoreService
from application.get_investment_money_service import GetInvestmentMoneyService
from application.get_j_score_service import GetJScoreService
from proto import creport_pb2 as pb2, creport_pb2_grpc as pb2_grpc


class CreportController(pb2_grpc.CreportServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):
        message = request.message
        print(message)
        j_score = GetJScoreService().get_score(company_name=message)
        print(j_score)
        b_score = GetBScoreService().get_score(company_name=message)
        print(b_score)
        invest_money = GetInvestmentMoneyService().get_money(company_name=message)
        print(invest_money)
        result = {'j_score': j_score, 'b_score': b_score, 'invest_money': invest_money, 'sales': 'sales', 'received': True}
        print(result)

        return pb2.MessageResponse(**result)
