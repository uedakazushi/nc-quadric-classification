"""Independently differentiate boundary potentials and check their critical overlaps."""

from collections import defaultdict
from functools import cache
from itertools import product

from sympy import S, cancel, symbols

WEIGHT = {"x": 1, "y": 1, "z": 2}
LEADING_WORDS = {"x": "zy", "y": "zx", "z": "yx"}


def weight(path):
    return sum(WEIGHT[letter] for letter in path)


def cyclic_derivatives(cycles):
    derivatives = defaultdict(lambda: defaultdict(lambda: S.Zero))
    for initial_vertex, word, coefficient in cycles:
        vertex = initial_vertex
        assert weight(word) == 4
        for position, letter in enumerate(word):
            remainder = word[position + 1 :] + word[:position]
            derivatives[letter, vertex][remainder] += coefficient
            vertex = (vertex + WEIGHT[letter]) % 4
    return derivatives


def make_rules(cycles):
    derivatives = cyclic_derivatives(cycles)
    rules = {}
    for vertex in range(4):
        for letter, leading_word in LEADING_WORDS.items():
            removed_source = (vertex - WEIGHT[letter]) % 4
            relation = derivatives[letter, removed_source]
            leading_coefficient = relation[leading_word]
            assert leading_coefficient != 0
            rules[vertex, leading_word] = {
                word: -coefficient / leading_coefficient
                for word, coefficient in relation.items()
                if word != leading_word and coefficient != 0
            }
    return rules


def check_overlaps(cycles):
    rules = make_rules(cycles)

    @cache
    def normalize(vertex, word):
        for position in range(len(word) - 1):
            source = (vertex + weight(word[:position])) % 4
            if (source, word[position : position + 2]) in rules:
                return reduce_at(vertex, word, position)
        return {word: S.One}

    def reduce_at(vertex, word, position):
        source = (vertex + weight(word[:position])) % 4
        result = defaultdict(lambda: S.Zero)
        for replacement, coefficient in rules[source, word[position : position + 2]].items():
            replaced = word[:position] + replacement + word[position + 2 :]
            for normal_word, value in normalize(vertex, replaced).items():
                result[normal_word] += coefficient * value
        simplified = {word: cancel(value) for word, value in result.items()}
        return {word: value for word, value in simplified.items() if value != 0}

    for vertex in range(4):
        left = reduce_at(vertex, "zyx", 0)
        right = reduce_at(vertex, "zyx", 1)
        assert left == right, (vertex, left, right)


def main():
    a2, b2 = symbols("a2 b2", nonzero=True)
    upper = symbols("upper")
    quartics = ["".join(word) for word in product("xy", repeat=4)]
    quartic_coefficients = symbols("h:16")
    cycles = []
    for vertex in range(4):
        cycles.append((vertex, "yxz", a2 if vertex == 2 else S.One))
        cycles.append((vertex, "xyz", -b2 if vertex == 2 else -S.One))
    cycles.append((2, "xxz", upper))
    cycles.extend((0, word, coefficient) for word, coefficient in zip(quartics, quartic_coefficients))
    check_overlaps(cycles)
    print("PASS: all four boundary overlaps, with generic triangular coefficients and quartic terms")


if __name__ == "__main__":
    main()
