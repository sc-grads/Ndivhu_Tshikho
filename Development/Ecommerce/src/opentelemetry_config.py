from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor
import logging

# Define a resource to represent this application
resource = Resource.create({"service.name": "ecommerce-backend"})

# Create a tracer provider
trace.set_tracer_provider(TracerProvider(resource=resource))

# Set up a Jaeger exporter
jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",  # Where Jaeger agent is running
    agent_port=6831,              # Jaeger agent port for traces
)

# Add a batch span processor to send traces to Jaeger
span_processor = BatchSpanProcessor(jaeger_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# Optional: Add console exporter to see traces in terminal
console_exporter = ConsoleSpanExporter()
trace.get_tracer_provider().add_span_processor(SimpleSpanProcessor(console_exporter))

# Instrument FastAPI for tracing
def init_tracing(app):
    FastAPIInstrumentor.instrument_app(app)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
