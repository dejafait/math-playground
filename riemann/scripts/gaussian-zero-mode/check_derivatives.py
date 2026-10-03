"""Exact rational audit of the differential identities used in L357."""

from fractions import Fraction as Q


def add_term(result, key, coefficient):
    result[key] = result.get(key, Q(0)) + coefficient
    if not result[key]:
        del result[key]


def logarithmic_derivative(terms):
    """D_u on e^(u/2) x^p f^(j)(x+eps), with D_u x=2x."""
    result = {}
    for (power, order), coefficient in terms.items():
        add_term(result, (power, order), (Q(1, 2) + 2 * power) * coefficient)
        add_term(result, (power + 1, order + 1), 2 * coefficient)
    return result


def dual_derivative(terms):
    """D_t on t^power psi^(order)(1/t)."""
    result = {}
    for (power, order), coefficient in terms.items():
        add_term(result, (power - 1, order), power * coefficient)
        add_term(result, (power - 2, order + 1), -coefficient)
    return result


def show(terms):
    return [(str(power), order, str(coefficient))
            for (power, order), coefficient in sorted(terms.items())]


def main():
    generator = {(0, 0): Q(1)}
    second = logarithmic_derivative(logarithmic_derivative(generator))
    operator = {key: 2 * value for key, value in second.items()}
    add_term(operator, (0, 0), -Q(1, 2))
    assert operator == {(1, 1): Q(12), (2, 2): Q(8)}
    epsilon_derivative = {(power, order + 1): value
                          for (power, order), value in operator.items()}
    assert epsilon_derivative == {(1, 2): Q(12), (2, 3): Q(8)}
    print('P(e^(u/2) f(x+eps)) / e^(u/2):', show(operator))
    print('eps derivative / e^(u/2):', show(epsilon_derivative))

    dual = {(Q(-1, 2), 0): Q(1)}
    expected = [
        {(Q(-3, 2), 0): -Q(1, 2), (Q(-5, 2), 1): -Q(1)},
        {(Q(-5, 2), 0): Q(3, 4), (Q(-7, 2), 1): Q(3),
         (Q(-9, 2), 2): Q(1)},
        {(Q(-7, 2), 0): -Q(15, 8), (Q(-9, 2), 1): -Q(45, 4),
         (Q(-11, 2), 2): -Q(15, 2), (Q(-13, 2), 3): -Q(1)},
    ]
    for order, answer in enumerate(expected, start=1):
        dual = dual_derivative(dual)
        assert dual == answer
        assert all(power == -(Q(order) + inner_order + Q(1, 2))
                   for power, inner_order in dual)
        print(f'R derivative {order} (power, psi order, coefficient):', show(dual))

    zero_mode_power = -Q(1, 2)
    zero_mode_coefficient = -Q(1, 2)
    zero_mode_derivatives = []
    for _ in range(3):
        zero_mode_coefficient *= zero_mode_power
        zero_mode_power -= 1
        zero_mode_derivatives.append(zero_mode_coefficient)
    assert zero_mode_derivatives == [Q(1, 4), -Q(3, 8), Q(15, 16)]
    assert 12 * Q(3, 8) + 8 * Q(15, 16) == 12
    alpha = Q(5, 2)
    weighted_envelope_integral = 2 / alpha + 4 / alpha**3
    assert weighted_envelope_integral == Q(132, 125)
    print('Zero-mode derivative coefficients:', list(map(str, zero_mode_derivatives)))
    print('Weighted envelope integral:', weighted_envelope_integral)
    print('Exact derivative and normalization audit passed; no sign is tested.')


if __name__ == '__main__':
    main()
