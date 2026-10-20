from typing import Any


class FindDriverUseCase:
    async def execute(self, message: dict[str, Any]) -> None:
        ride_id = message["ride_id"]

        print(f"Searching driver for ride {ride_id}")

        # TODD: implement driver search
