from typing import Any

from movex_worker.application.use_cases import FindDriverUseCase


class RideRequestHandler:
    def __init__(self, use_case: FindDriverUseCase) -> None:
        self._use_case = use_case
    
    async def __call__(self, message: dict[str, Any]) -> Any:
        await self._use_case.execute(message)
