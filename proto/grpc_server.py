import grpc
from concurrent import futures
import creport_pb2_grpc as pb2_grpc

from presentation.creport_controller import CreportController


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_CreportServicer_to_server(CreportController(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
