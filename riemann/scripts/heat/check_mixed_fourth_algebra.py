"""Finite algebra sanity check; no asymptotic or RH certificate."""
import cmath
import itertools
import random

rng = random.Random(180)
for _ in range(1000):
    p, q = (complex(rng.uniform(-3, 3), rng.uniform(-3, 3)) for _ in range(2))
    theta = rng.uniform(-10, 10)
    a, d = cmath.exp(-0.5j * theta) * p, cmath.exp(-0.5j * theta) * q
    direct = a.real**2 * d.imag**2
    collected = (4 * abs(p)**2 * abs(q)**2
                 - 2 * (p**2 * q.conjugate()**2).real
                 + 4 * (cmath.exp(-1j * theta)
                        * (p**2 * abs(q)**2 - abs(p)**2 * q**2)).real
                 - 2 * (cmath.exp(-2j * theta) * p**2 * q**2).real) / 16
    expanded = 0j
    for signs in itertools.product((-1, 1), repeat=4):
        term = -signs[2] * signs[3] / 16
        for z, sign in zip((a, a, d, d), signs):
            term *= z if sign == 1 else z.conjugate()
        expanded += term
    assert abs(direct - collected) < 1e-10
    assert abs(direct - expanded) < 1e-10
print('Passed 1000 deterministic complex algebra cases.')
