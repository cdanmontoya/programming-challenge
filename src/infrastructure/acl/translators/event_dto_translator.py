from src.domain.events.event import Event
from src.infrastructure.acl.dto.events.integration_event import EventDto, IntegrationEvent
from src.infrastructure.config.observability.correlation_id.correlation_id import correlation_id_ctx_var


def of(event: Event) -> EventDto:
    return EventDto(
        id=event.id,
        occurred_on=event.occurred_on,
        source=event.source,
        name=event.name,
        version=event.version,
        data=event.data,
    )


def to_json(event: Event) -> str:
    dto = of(event)

    return IntegrationEvent(
        event=dto, correlation_id=correlation_id_ctx_var.get()
    ).model_dump_json()
