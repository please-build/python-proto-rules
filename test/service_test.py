import unittest

from test.proto import service_pb2, service_grpc


class ServiceTest(unittest.TestCase):
    def test_service(self):
        message = service_pb2.HelloRequest()
        self.assertIsNotNone(message)

        service = service_grpc.HelloServiceStub(None)
        self.assertIsNotNone(service)

