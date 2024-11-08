import random

"""
This module implements an elementary cellular automaton following the "Rule 90"
definition.

Such an automaton is a 1D automaton, whose state is thus represented as a
list of boolean, each boolean indicating whether a given cell is dead (`False`)
or alive (`True`). Rule 90 defines the evolution of the automaton as follows:
- the cell at index `i` takes as value the exclusive or of the values at
  indices `i - 1` and `i + 1` at the previous time step;
- if neither indices exist, the state is unchanged; if only one of the indices
  exists then the cell takes the value at the existing index.

See https://en.wikipedia.org/wiki/Elementary_cellular_automaton

See https://en.wikipedia.org/wiki/Rule_90
"""


def init_random(width: int) -> list[bool]:
    """
    Return a random initial state for the automaton, `width` being the number
    of cells in the automaton.
    """
    pass  # TODO


def init_single_middle(width: int) -> list[bool]:
    """
    Return an initial state such that all cells are dead except the one in the
    middle which is live. `width` is the number of cells in the automaton.
    """
    pass  # TODO


def step(row: list[bool]) -> list[bool]:
    """
    Return the next state of the automaton by applying "Rule 90" (See module
    documentation above).
    """
    pass  # TODO


def convert(cell: bool, dead_repr: str, live_repr: str) -> str:
    """
    Convert `cell` into its textual representation, i.e. `dead_repr` if the
    cell is dead and `live_repr` if it is live.
    """
    pass  # TODO


def display(row: list[bool], dead_repr: str, live_repr: str) -> None:
    """
    Print the contents of `row` onto the standard output, using `dead_repr`
    and `live_repr` as the representation of respectively the dead and live
    cells.
    """
    pass  # TODO


def run(first_row: list[bool], num_steps: int, dead_repr: str, live_repr: str) -> None:
    """
    Simulate the automaton: first display `first_row` and then compute and
    display `num_steps` rows by repeatedly calling `step`. `dead_repr` and
    `live_repr` are the characters used to represent respectively dead and
    live cells.
    """
    pass  # TODO


ROW_WIDTH = 127
NUM_STEPS = 63

if __name__ == "__main__":
    run(
        init_single_middle(width=ROW_WIDTH),
        num_steps=NUM_STEPS,
        dead_repr=" ",
        live_repr="*",
    )
