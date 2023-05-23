import unittest

from test.proto import service_pb2, service_pb2_grpc


class ServiceTest(unittest.TestCase):
    def test_service(self):
        message = service_pb2.HelloRequest()
        self.assertIsNotNone(message)

        service = service_pb2_grpc.HelloServiceServicer()
        self.assertIsNotNone(service)



