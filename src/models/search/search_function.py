from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Iterable, Optional, Callable, Generic

from src.models.base import T
from src.models.problem.search_problem import SearchProblem

ExternalCallback = Callable[[Iterable[T], Iterable[T]], None]


class SearchResponse(Generic[T]):
    def __init__(self, path: List[T], cost: int, steps_count: int):
        self.path = path
        self.cost = cost
        self.steps_count = steps_count


class SearchFunction(ABC, Generic[T]):

    def __init__(self, problem: SearchProblem[T]):
        """
        :param problem: Callback que recebe a fronteira e os nós já visitados.
        :return: Resultado da busca com o caminho, custo e número de passos.
        """
        self.problem = problem

    @abstractmethod
    def solve(self, step_callback: Optional[ExternalCallback] = None) -> Optional[SearchResponse]:
        """
        Executa o algoritmo de busca e a cada passo invoca o callback.
        :param step_callback: Callback que recebe a fronteira e os nós já visitados.
        :return:
        """
        pass
