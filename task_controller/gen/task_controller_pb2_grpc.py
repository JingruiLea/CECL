# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from task_controller.gen import task_controller_pb2 as task__controller_dot_gen_dot_task__controller__pb2


class DataManagerStub(object):
    """The task controller service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddTask = channel.unary_unary(
                '/DataManager/AddTask',
                request_serializer=task__controller_dot_gen_dot_task__controller__pb2.AddTaskReq.SerializeToString,
                response_deserializer=task__controller_dot_gen_dot_task__controller__pb2.AddTaskResp.FromString,
                )
        self.StopTask = channel.unary_unary(
                '/DataManager/StopTask',
                request_serializer=task__controller_dot_gen_dot_task__controller__pb2.StopTaskReq.SerializeToString,
                response_deserializer=task__controller_dot_gen_dot_task__controller__pb2.StopTaskResp.FromString,
                )
        self.GetTaskInfo = channel.unary_unary(
                '/DataManager/GetTaskInfo',
                request_serializer=task__controller_dot_gen_dot_task__controller__pb2.GetTaskInfoReq.SerializeToString,
                response_deserializer=task__controller_dot_gen_dot_task__controller__pb2.GetTaskInfoResp.FromString,
                )
        self.UpdateTask = channel.unary_unary(
                '/DataManager/UpdateTask',
                request_serializer=task__controller_dot_gen_dot_task__controller__pb2.UpdateTaskReq.SerializeToString,
                response_deserializer=task__controller_dot_gen_dot_task__controller__pb2.UpdateTaskResp.FromString,
                )


class DataManagerServicer(object):
    """The task controller service definition.
    """

    def AddTask(self, request, context):
        """Add a task
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

    def GetTaskInfo(self, request, context):
        """Get task information
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTask(self, request, context):
        """Update task information
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddTask': grpc.unary_unary_rpc_method_handler(
                    servicer.AddTask,
                    request_deserializer=task__controller_dot_gen_dot_task__controller__pb2.AddTaskReq.FromString,
                    response_serializer=task__controller_dot_gen_dot_task__controller__pb2.AddTaskResp.SerializeToString,
            ),
            'StopTask': grpc.unary_unary_rpc_method_handler(
                    servicer.StopTask,
                    request_deserializer=task__controller_dot_gen_dot_task__controller__pb2.StopTaskReq.FromString,
                    response_serializer=task__controller_dot_gen_dot_task__controller__pb2.StopTaskResp.SerializeToString,
            ),
            'GetTaskInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTaskInfo,
                    request_deserializer=task__controller_dot_gen_dot_task__controller__pb2.GetTaskInfoReq.FromString,
                    response_serializer=task__controller_dot_gen_dot_task__controller__pb2.GetTaskInfoResp.SerializeToString,
            ),
            'UpdateTask': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTask,
                    request_deserializer=task__controller_dot_gen_dot_task__controller__pb2.UpdateTaskReq.FromString,
                    response_serializer=task__controller_dot_gen_dot_task__controller__pb2.UpdateTaskResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DataManager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataManager(object):
    """The task controller service definition.
    """

    @staticmethod
    def AddTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataManager/AddTask',
            task__controller_dot_gen_dot_task__controller__pb2.AddTaskReq.SerializeToString,
            task__controller_dot_gen_dot_task__controller__pb2.AddTaskResp.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/DataManager/StopTask',
            task__controller_dot_gen_dot_task__controller__pb2.StopTaskReq.SerializeToString,
            task__controller_dot_gen_dot_task__controller__pb2.StopTaskResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTaskInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataManager/GetTaskInfo',
            task__controller_dot_gen_dot_task__controller__pb2.GetTaskInfoReq.SerializeToString,
            task__controller_dot_gen_dot_task__controller__pb2.GetTaskInfoResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataManager/UpdateTask',
            task__controller_dot_gen_dot_task__controller__pb2.UpdateTaskReq.SerializeToString,
            task__controller_dot_gen_dot_task__controller__pb2.UpdateTaskResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
