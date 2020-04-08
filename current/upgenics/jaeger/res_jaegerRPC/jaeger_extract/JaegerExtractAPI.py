import pymongo
from datetime import datetime
import pika
import json
from flask import jsonify
from bson.objectid import ObjectId


# Distributed Tracing
from opentracing_instrumentation.request_context import get_current_span, span_in_context
import jaegerTracing
tracer = jaegerTracing.getTracerInstance()
from opentracing.propagation import Format



class TestExtract():
    

    def extractSpan(self):

        span_ctx = tracer.extract(format=Format.TEXT_MAP, carrier={})
        span = tracer.start_span(operation_name='extractSpan', child_of= span_ctx)

        return "Server2"