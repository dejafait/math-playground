"""Exact coefficient checks for the two-isogeny normalization in L005.

Run from the active notebook: python3 scripts/rm-degree-two/check_normalization.py
Only rational arithmetic is used. This checks coordinate scaling, not Hodge theory.
"""

from fractions import Fraction as Q


def forward_residual(c, d_squared):
    """Coefficients of y_new^2 - x_new(x_new^2 - 2a x_new + a^2-b).

    Here x_new=c*u, y_new=d*v and v^2=u(u^2-4a*u+4(a^2-b)).
    The four monomials are independent over Q.
    """
    return {
        "u^3": d_squared - c**3,
        "a*u^2": -4*d_squared + 2*c**2,
        "a^2*u": 4*d_squared - c,
        "b*u": -4*d_squared + c,
    }


def reverse_residual(c, d_squared):
    """Map the original fiber at t to the isogenous fiber at -t."""
    return {
        "x^3": d_squared - c**3,
        "a*x^2": 2*d_squared - 4*c**2,
        "b*x": d_squared - 4*c,
    }


def main():
    corrected = forward_residual(Q(1, 2), Q(1, 8))
    printed = forward_residual(Q(2), Q(8))
    reverse = reverse_residual(Q(2), Q(8))
    assert all(value == 0 for value in corrected.values())
    assert printed == {"u^3": 0, "a*u^2": -24, "a^2*u": 30, "b*u": -30}
    assert all(value == 0 for value in reverse.values())
    # The isogeny preserves dx/y; t -> -t contributes a minus sign.
    # The square of the resulting two-form multiplier is c^2/d^2.
    assert Q(1, 2)**2 / Q(1, 8) == 2
    assert Q(2)**2 / Q(8) == Q(1, 2)
    print("Corrected forward scaling: all four residual coefficients vanish.")
    print("Printed forward scaling: residual = -24*a*u^2 + 30*(a^2-b)*u.")
    print("Printed scaling in the reverse direction: all coefficients vanish.")
    print("Corrected two-form multiplier squared: 2 (degree compatibility).")


if __name__ == "__main__":
    main()
