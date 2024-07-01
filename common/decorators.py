import time
import logging

from functools import wraps
from typing import (
    Callable,
    ParamSpec,
    TypeVar,
)


F_Spec = ParamSpec("F_Spec")
F_Return = TypeVar("F_Return")


def execution_time(logger: logging.Logger) -> Callable[
    [Callable[F_Spec, F_Return]],
    Callable[F_Spec, F_Return]
]:
    """
    Декоратор для логирования времени выполнения функции
    """
    def decorator(func: Callable[F_Spec, F_Return]) -> Callable[F_Spec, F_Return]:
        @wraps(func)
        def wrapper(
            *args: F_Spec.args,
            **kwargs: F_Spec.kwargs
        ) -> F_Return:
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            total_time = end_time - start_time

            logger.info(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
            return result
        return wrapper
    return decorator

