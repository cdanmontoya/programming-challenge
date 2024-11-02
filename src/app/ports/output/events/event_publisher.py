from abc import ABC, abstractmethod
from collections.abc import Callable
from typing import Any

from src.domain.error import Error
from src.domain.events.event import Event


class EventPublisher(ABC):
    @abstractmethod
    def publish(self, event: Event) -> None:
        raise NotImplementedError


def publishes(successful_event: type[Event], error_event: type[Event]) -> Any:
    """
    Convenience method to avoid transforming manually to an Event and publishing the event every single time an event
    needs to be published. This assumes that the annotated method belongs to a class that has an _event_publisher
    attribute, and that the return value is the desired event payload.

    For more complex scenarios, such as publishing multiple events, use the EventPublisher directly

    :param successful_event: Class of the event to be published
    :param error_event: Class of the error event to be published in case that the function returns an Error.

    :return: The result of the function execution
    """

    def decorator(func: Callable[..., Callable[..., Any]]) -> Callable[..., Any]:
        def wrapper(self: object, *args, **kwargs) -> Any:
            result = func(self, *args, **kwargs)
            event_instance = (
                successful_event(result)
                if not isinstance(result, Error)
                else error_event(result)
            )
            self._event_publisher.publish(event_instance)
            return result

        return wrapper

    return decorator
