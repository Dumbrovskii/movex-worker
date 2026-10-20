import asyncio

from movex_worker.application.use_cases import (
    FindDriverUseCase,
)
from movex_worker.application.handlers import (
    RideRequestHandler,
)
from movex_worker.infrastructure.messaging import (
    RabbitMQConnection,
)
from movex_worker.infrastructure.messaging import (
    RabbitMQConsumer,
)


async def main() -> None:
    connection = RabbitMQConnection()

    try:
        await connection.connect()

        use_cases = FindDriverUseCase()
        handler = RideRequestHandler(use_cases)
        consumer = RabbitMQConsumer(connection, handler)

        await consumer.consume()
    finally:
        await connection.close()


if __name__ == "__main__":
    asyncio.run(main())
