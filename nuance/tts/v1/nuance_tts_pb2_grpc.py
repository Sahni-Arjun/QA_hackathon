# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from nuance.tts.v1 import nuance_tts_pb2 as nuance_dot_tts_dot_v1_dot_nuance__tts__pb2


class SynthesizerStub(object):
    """
    The Synthesizer service offers these functionalities:
    - GetVoices: Queries the list of available voices, with filters to reduce the search space.  
    - Synthesize: Synthesizes audio from input text and parameters, and returns an audio stream. 
    - UnarySynthesize: Synthesizes audio from input text and parameters, and returns a single audio response. 
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetVoices = channel.unary_unary(
                '/nuance.tts.v1.Synthesizer/GetVoices',
                request_serializer=nuance_dot_tts_dot_v1_dot_nuance__tts__pb2.GetVoicesRequest.SerializeToString,
                response_deserializer=nuance_dot_tts_dot_v1_dot_nuance__tts__pb2.GetVoicesResponse.FromString,
                )
        self.Synthesize = channel.unary_stream(
                '/nuance.tts.v1.Synthesizer/Synthesize',
                request_serializer=nuance_dot_tts_dot_v1_dot_nuance__tts__pb2.SynthesisRequest.SerializeToString,
                response_deserializer=nuance_dot_tts_dot_v1_dot_nuance__tts__pb2.SynthesisResponse.FromString,
                )
        self.UnarySynthesize = channel.unary_unary(
                '/nuance.tts.v1.Synthesizer/UnarySynthesize',
                request_serializer=nuance_dot_tts_dot_v1_dot_nuance__tts__pb2.SynthesisRequest.SerializeToString,
                response_deserializer=nuance_dot_tts_dot_v1_dot_nuance__tts__pb2.UnarySynthesisResponse.FromString,
                )


class SynthesizerServicer(object):
    """
    The Synthesizer service offers these functionalities:
    - GetVoices: Queries the list of available voices, with filters to reduce the search space.  
    - Synthesize: Synthesizes audio from input text and parameters, and returns an audio stream. 
    - UnarySynthesize: Synthesizes audio from input text and parameters, and returns a single audio response. 
    """

    def GetVoices(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Synthesize(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnarySynthesize(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SynthesizerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetVoices': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVoices,
                    request_deserializer=nuance_dot_tts_dot_v1_dot_nuance__tts__pb2.GetVoicesRequest.FromString,
                    response_serializer=nuance_dot_tts_dot_v1_dot_nuance__tts__pb2.GetVoicesResponse.SerializeToString,
            ),
            'Synthesize': grpc.unary_stream_rpc_method_handler(
                    servicer.Synthesize,
                    request_deserializer=nuance_dot_tts_dot_v1_dot_nuance__tts__pb2.SynthesisRequest.FromString,
                    response_serializer=nuance_dot_tts_dot_v1_dot_nuance__tts__pb2.SynthesisResponse.SerializeToString,
            ),
            'UnarySynthesize': grpc.unary_unary_rpc_method_handler(
                    servicer.UnarySynthesize,
                    request_deserializer=nuance_dot_tts_dot_v1_dot_nuance__tts__pb2.SynthesisRequest.FromString,
                    response_serializer=nuance_dot_tts_dot_v1_dot_nuance__tts__pb2.UnarySynthesisResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'nuance.tts.v1.Synthesizer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Synthesizer(object):
    """
    The Synthesizer service offers these functionalities:
    - GetVoices: Queries the list of available voices, with filters to reduce the search space.  
    - Synthesize: Synthesizes audio from input text and parameters, and returns an audio stream. 
    - UnarySynthesize: Synthesizes audio from input text and parameters, and returns a single audio response. 
    """

    @staticmethod
    def GetVoices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nuance.tts.v1.Synthesizer/GetVoices',
            nuance_dot_tts_dot_v1_dot_nuance__tts__pb2.GetVoicesRequest.SerializeToString,
            nuance_dot_tts_dot_v1_dot_nuance__tts__pb2.GetVoicesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Synthesize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/nuance.tts.v1.Synthesizer/Synthesize',
            nuance_dot_tts_dot_v1_dot_nuance__tts__pb2.SynthesisRequest.SerializeToString,
            nuance_dot_tts_dot_v1_dot_nuance__tts__pb2.SynthesisResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnarySynthesize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nuance.tts.v1.Synthesizer/UnarySynthesize',
            nuance_dot_tts_dot_v1_dot_nuance__tts__pb2.SynthesisRequest.SerializeToString,
            nuance_dot_tts_dot_v1_dot_nuance__tts__pb2.UnarySynthesisResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)