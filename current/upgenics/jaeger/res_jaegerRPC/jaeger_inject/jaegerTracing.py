
# Jaeger Tracing 
import sys
import time
import logging
import random
from jaeger_client import Config
from opentracing_instrumentation.request_context import get_current_span, span_in_context
from os import getenv

# JAEGER_HOST = getenv('JAEGER_HOST', 'localhost')
JAEGER_HOST = getenv('JAEGER_HOST', 'jaeger')

# Service name
SERVICE_NAME = 'jaegerinject'

def init_tracer(service):
            log_level = logging.DEBUG
            logging.getLogger('').handlers = []
            logging.basicConfig(format='%(asctime)s %(message)s', level=log_level)

            # Create configuration object with enabled logging and sampling of all requests.
            config = Config(config={'sampler': {'type': 'const', 'param': 1},
                                    'logging': True,
                                    'local_agent': {'reporting_host': JAEGER_HOST}},
                            service_name=service)
            return config.initialize_tracer()

def getTracerInstance():
        return tracer


tracer = init_tracer(SERVICE_NAME)