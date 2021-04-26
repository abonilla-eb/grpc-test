import grpc
import asyncio

import rpc.test_pb2
import rpc.test_pb2_grpc


class TestService(rpc.test_pb2_grpc.TestServiceServicer):

    async def TestCall(
        self,
        request: rpc.test_pb2.TestRequest,
        context: grpc.aio.ServicerContext
    ) -> rpc.test_pb2.TestResponse:
        return rpc.test_pb2.TestResponse(
            test_string='qsd',
            test_enum=rpc.test_pb2.OTRAOP,
        )

async def run():
    server = grpc.aio.server()
    rpc.test_pb2_grpc.add_TestServiceServicer_to_server(TestService(), server)
    listen_addr = '0.0.0.0:50001'
    server.add_insecure_port(listen_addr)
    await server.start()
    try:
        await server.wait_for_termination()
    except KeyboardInterrupt:
        await server.stop(2)

if __name__ == '__main__':
    asyncio.run(run())
