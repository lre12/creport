from application.get_j_score_service import GetJScoreService
from infra import creport_pb2 as pb2, creport_pb2_grpc as pb2_grpc


class CreportController(pb2_grpc.CreportServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):
        message = request.message
        score = GetJScoreService().get_score(company_name=message)
        result = {'message': score, 'received': True}
        print(result)

        return pb2.MessageResponse(**result)
