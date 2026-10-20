import json
from aio_pika.abc import AbstractRobustQueue

from movex_worker.application.handlers import RideRequestHandler
from movex_worker.application.interfaces.messaging import (
    MessageConsumer,
)

from movex_worker.infrastructure.messaging.rabbitmq_connection import RabbitMQConnection


class RabbitMQConsumer(MessageConsumer):
    def __init__(
        self,
        connection: RabbitMQConnection,
        handler: RideRequestHandler,
    ) -> None:
        self._connection = connection
        self._handler = handler

    async def consume(self) -> None:
        channel = self._connection.channel

        queue: AbstractRobustQueue = await channel.declare_queue(
            "movex.ride.requested",
            durable=True,
        )

        await queue.bind(
            self._connection.exchange,
            routing_key="ride.requested",
        )

        async with queue.iterator() as messages:
            async for message in messages:
                async with message.process():
                    payload = json.loads(message.body)
                    await self._handler(payload)
