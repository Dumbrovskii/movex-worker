from abc import ABC, abstractmethod
from collections.abc import Awaitable, Callable
from typing import Any


class MessageConsumer(ABC):
    @abstractmethod
    async def consume(
        self,
        routing_key: str,
        handler: Callable[[dict[str, Any]], Awaitable[None]],
    ) -> None:
        pass
