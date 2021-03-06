# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from message_hub.gen import message_hub_pb2 as message__hub_dot_gen_dot_message__hub__pb2


class MessageHubStub(object):
    """The message hub service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendTask = channel.unary_unary(
                '/MessageHub/SendTask',
                request_serializer=message__hub_dot_gen_dot_message__hub__pb2.SendTaskReq.SerializeToString,
                response_deserializer=message__hub_dot_gen_dot_message__hub__pb2.SendTaskResp.FromString,
                )
        self.RunTask = channel.unary_unary(
                '/MessageHub/RunTask',
                request_serializer=message__hub_dot_gen_dot_message__hub__pb2.RunTaskReq.SerializeToString,
                response_deserializer=message__hub_dot_gen_dot_message__hub__pb2.RunTaskResp.FromString,
                )
        self.StopTask = channel.unary_unary(
                '/MessageHub/StopTask',
                request_serializer=message__hub_dot_gen_dot_message__hub__pb2.StopTaskReq.SerializeToString,
                response_deserializer=message__hub_dot_gen_dot_message__hub__pb2.StopTaskResp.FromString,
                )


class MessageHubServicer(object):
    """The message hub service definition.
    """

    def SendTask(self, request, context):
        """Send a new task to edges.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RunTask(self, request, context):
        """Run a task on edges.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopTask(self, request, context):
        """Stop a task
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MessageHubServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendTask': grpc.unary_unary_rpc_method_handler(
                    servicer.SendTask,
                    request_deserializer=message__hub_dot_gen_dot_message__hub__pb2.SendTaskReq.FromString,
                    response_serializer=message__hub_dot_gen_dot_message__hub__pb2.SendTaskResp.SerializeToString,
            ),
            'RunTask': grpc.unary_unary_rpc_method_handler(
                    servicer.RunTask,
                    request_deserializer=message__hub_dot_gen_dot_message__hub__pb2.RunTaskReq.FromString,
                    response_serializer=message__hub_dot_gen_dot_message__hub__pb2.RunTaskResp.SerializeToString,
            ),
            'StopTask': grpc.unary_unary_rpc_method_handler(
                    servicer.StopTask,
                    request_deserializer=message__hub_dot_gen_dot_message__hub__pb2.StopTaskReq.FromString,
                    response_serializer=message__hub_dot_gen_dot_message__hub__pb2.StopTaskResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MessageHub', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MessageHub(object):
    """The message hub service definition.
    """

    @staticmethod
    def SendTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MessageHub/SendTask',
            message__hub_dot_gen_dot_message__hub__pb2.SendTaskReq.SerializeToString,
            message__hub_dot_gen_dot_message__hub__pb2.SendTaskResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RunTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MessageHub/RunTask',
            message__hub_dot_gen_dot_message__hub__pb2.RunTaskReq.SerializeToString,
            message__hub_dot_gen_dot_message__hub__pb2.RunTaskResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MessageHub/StopTask',
            message__hub_dot_gen_dot_message__hub__pb2.StopTaskReq.SerializeToString,
            message__hub_dot_gen_dot_message__hub__pb2.StopTaskResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
