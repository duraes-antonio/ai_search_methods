from typing import List, Set, Optional, Tuple

from src.application.util.measure import measure
from src.models.base import T
from src.models.search.search_function import SearchFunction, SearchResponse

State = Tuple[T, List[T]]


class DepthFirstSearch(SearchFunction):

    @measure
    def solve(self) -> Optional[SearchResponse]:
        frontier: List[State] = []
        frontier_set: Set[T] = set()
        visited: Set[T] = set()
        actions: List[T] = []

        current_state: T = self.problem.start_state()
        frontier_set.add(current_state)
        frontier.append((current_state, actions))

        while frontier:
            current_state, actions = frontier.pop()
            frontier_set.remove(current_state)

            if current_state in visited or current_state in frontier_set:
                continue

            if self.problem.is_goal_state(current_state):
                return SearchResponse(actions, len(actions), len(visited))

            visited.add(current_state)
            neighbors = self.problem.get_successors(current_state)

            for child_state in neighbors:
                if child_state in visited or child_state in frontier_set:
                    continue

                frontier.append((child_state, actions + [child_state]))
                frontier_set.add(child_state)

            if self.on_step:
                frontier_cells = [item for item, path in frontier]
                self.on_step(frontier_cells, visited)
