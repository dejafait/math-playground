"""Exact arithmetic check; group/core hypotheses are proved in L090."""
import json
from fractions import Fraction
from pathlib import Path


def valuations(n):
    result = {}
    for p in (2, 3, 5):
        exponent = 0
        while n % p == 0:
            n //= p
            exponent += 1
        result[str(p)] = exponent
    assert n == 1
    return result


gl3 = (3**2 - 1) * (3**2 - 3)
gl5 = (5**2 - 1) * (5**2 - 5)
gl4 = 2**4 * (2**2 - 1) * (2**2 - 2)
ambient = gl4 * gl3 * gl5
values = {
    "ambient_absolute": ambient,
    "literal_absolute": ambient // 8,
    "literal_relative": ambient // (8 * 6),
    "closure_absolute": ambient // 2,
    "closure_relative": ambient // (2 * 6),
    "C_0": 2 * gl3 * gl5,
    "delta": 2**12 * 3**3 * 5 * 6,
}
assert ambient % (8 * 6) == 0
assert values["closure_relative"] == 4 * values["C_0"]
assert 3 * values["closure_absolute"] == values["delta"]
certificate = {
    "hypotheses": "L090: full ambient product, stabilizer 8, core 2, [T:Q]=6",
    "values": {k: {"value": v, "valuations": valuations(v)} for k, v in values.items()},
    "relative_ratio": str(Fraction(values["closure_relative"], values["C_0"])),
    "absolute_ratio": str(Fraction(values["closure_absolute"], values["delta"])),
    "failures": [],
    "limitation": "Arithmetic only; no verification of local ramification or source applicability.",
}
destination = Path(__file__).with_name("certificate.json")
destination.write_text(json.dumps(certificate, indent=2) + "\n")
for name, value in values.items():
    print(f"{name}: {value}; v_2,v_3,v_5={tuple(valuations(value).values())}")
print(f"Relative actual/required: {values['closure_relative']}/{values['C_0']} = 4")
print(f"Absolute actual/required: {values['closure_absolute']}/{values['delta']} = 1/3")
print(f"Arithmetic failures: []; certificate: {destination}")
