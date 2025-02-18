from typing import Generic, TypeVar, Callable

InputData = TypeVar("InputData")
OutputData = TypeVar("OutputData")


class Interactor(Generic[InputData, OutputData]):
    async def __call__(self, data: InputData) -> OutputData:
        raise NotImplementedError


InteractorT = TypeVar("InteractorT")
InteractorFactory = Callable[[], InteractorT]
