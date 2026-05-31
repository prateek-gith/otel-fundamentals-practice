import logging
import os

from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor


logger = logging.getLogger(__name__)


def setup_telemetry(app, engine):
    resource = Resource.create({
        "service.name": os.getenv(
            "SERVICE_NAME",
            "fastapi-otel-app"
        )
    })

    provider = TracerProvider(
        resource=resource
    )

    trace.set_tracer_provider(provider)

    otlp_exporter = OTLPSpanExporter(
        endpoint="jaeger:4317",
        insecure=True
    )

    span_processor = BatchSpanProcessor(
        otlp_exporter
    )

    provider.add_span_processor(
        span_processor
    )

    FastAPIInstrumentor.instrument_app(app)

    SQLAlchemyInstrumentor().instrument(
        engine=engine
    )

    LoggingInstrumentor().instrument(
        set_logging_format=True
    )

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    logger.info(
        "OpenTelemetry initialized"
    )