"""Exact finite tests for mixed (2,1)/(3,1) prefixes; no convergence claim."""

import itertools
import json


def word_data(word):
    total_odd = 0
    total_steps = 0
    offset = 0
    for odd_run in word:
        offset = 3**odd_run * offset + (3**odd_run - 2**odd_run) * 2**total_steps
        total_odd += odd_run
        total_steps += odd_run + 1
    multiplier = 3**total_odd
    modulus = 2 ** (total_steps + 1)
    residue = (pow(multiplier, -1, modulus) * (2**total_steps - offset)) % modulus
    assert 0 < residue < modulus and residue % 2 == 1
    return total_odd, total_steps, multiplier, offset, modulus, residue


def direct_block(start):
    assert start > 0 and start % 2 == 1
    current = start
    odd_run = 0
    even_run = 0
    states = []
    while current % 2:
        current = (3 * current + 1) // 2
        odd_run += 1
        states.append(current)
    while current % 2 == 0:
        current //= 2
        even_run += 1
        states.append(current)
    return odd_run, even_run, current, states


def valuation_two(value):
    assert value > 0
    return (value & -value).bit_length() - 1


def check():
    words_checked = 0
    witnesses_checked = 0
    shortcut_transitions = 0
    minima = []
    previous_minimum = 0
    for length in range(1, 13):
        best = None
        for word in itertools.product((2, 3), repeat=length):
            _, steps, multiplier, offset, modulus, residue = word_data(word)
            words_checked += 1
            if best is None or residue < best[0]:
                best = (residue, word, modulus)
            for lift in (0, 1, 7):
                start = residue + lift * modulus
                current = start
                for odd_run in word:
                    actual_odd, actual_even, endpoint, states = direct_block(current)
                    shortcut_transitions += len(states)
                    assert (actual_odd, actual_even) == (odd_run, 1), (word, start)
                    assert min(states) > current >= start, (word, start)
                    current = endpoint
                assert current * 2**steps == multiplier * start + offset
                witnesses_checked += 1
        minimum, best_word, best_modulus = best
        assert minimum >= previous_minimum
        previous_minimum = minimum
        minima.append({
            "K": length,
            "word_count": 2**length,
            "minimum_start": minimum,
            "minimizing_word": list(best_word),
            "word_modulus": best_modulus,
            "single_type_2_minimum": 2 ** (3 * length + 1) - 5,
        })

    complete_periods = []
    for length in range(1, 4):
        common_modulus = 2 ** (4 * length + 1)
        word_residues = [
            (word, *word_data(word)[-2:])
            for word in itertools.product((2, 3), repeat=length)
        ]
        matched = 0
        for start in range(1, common_modulus, 2):
            current = start
            actual_word = []
            actual_is_allowed = True
            for _ in range(length):
                a, b, current, states = direct_block(current)
                shortcut_transitions += len(states)
                actual_word.append(a)
                if a not in (2, 3) or b != 1:
                    actual_is_allowed = False
            predicted_words = [
                word for word, modulus, residue in word_residues
                if start % modulus == residue
            ]
            assert len(predicted_words) <= 1
            assert bool(predicted_words) == actual_is_allowed, (length, start)
            if actual_is_allowed:
                assert tuple(actual_word) == predicted_words[0]
                matched += 1
        assert matched == 3**length
        complete_periods.append({
            "K": length,
            "modulus": common_modulus,
            "odd_starts_checked": common_modulus // 2,
            "allowed_starts": matched,
        })

    repetition_cases = 0
    for length in range(1, 5):
        for word in itertools.product((2, 3), repeat=length):
            _, steps, multiplier, offset, _, _ = word_data(word)
            denominator = 2**steps
            coefficient = multiplier - denominator
            assert coefficient > 0 and coefficient % 2 == 1 and offset % 2 == 1
            starts = set(range(1, 512, 2))
            # Include long exact repetitions, not only predominantly immediate exits.
            for repetitions in (1, 2, 3, 8):
                *_, modulus, residue = word_data(word * repetitions)
                starts.update((residue, residue + modulus))
            for start in sorted(starts):
                shifted = coefficient * start + offset
                expected = (valuation_two(shifted) - 1) // steps
                current = start
                for repetition in range(expected + 1):
                    realized_word = True
                    for odd_run in word:
                        actual_odd, actual_even, endpoint, states = direct_block(current)
                        shortcut_transitions += len(states)
                        if (actual_odd, actual_even) != (odd_run, 1):
                            realized_word = False
                            break
                        current = endpoint
                    if repetition < expected:
                        assert realized_word, (word, start, expected, repetition)
                        assert (coefficient * current + offset) * denominator ** (repetition + 1) == (
                            multiplier ** (repetition + 1) * shifted
                        )
                    else:
                        assert not realized_word, (word, start, expected)
                repetition_cases += 1

    return {
        "result": "PASS",
        "scope": "Exact finite arithmetic only; no divergent lower bound or convergence follows.",
        "words_checked": words_checked,
        "representatives_and_lifts_checked": witnesses_checked,
        "fixed_word_repetition_cases_checked": repetition_cases,
        "shortcut_transitions_checked": shortcut_transitions,
        "minima": minima,
        "complete_periods": complete_periods,
    }


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))
