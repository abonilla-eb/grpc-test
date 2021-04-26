import grpc
import asyncio

import rpc.test_pb2
import rpc.test_pb2_grpc

from google.protobuf.struct_pb2 import Struct


async def run():
    async with grpc.aio.insecure_channel('localhost:50001') as channel:
        stub = rpc.test_pb2_grpc.TestServiceStub(channel)
        params = Struct()
        params.update({'hola': 'bb'})
        response = await stub.TestCall(rpc.test_pb2.TestRequest(
            test_string='asd',
            test_dict=params,
        ))
    print(f"Test response: {response}")

if __name__ == '__main__':
    asyncio.run(run())
