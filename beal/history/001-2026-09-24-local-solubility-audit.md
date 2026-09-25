# 2026-09-24 — Initial scope audit and local-obstruction test

STEP_ID: beal-2026-09-24-001-primitive-local-solubility

The notebook had no prior lemmas or local unfinished changes. The primary statement was corroborated on Mauldin's accessible page; the nominated AMS endpoint returned 403. Exact scope and source limitations are in [the source audit](../foundations/01-target-and-scope.md). Equal-exponent nonexistence, fixed-signature finiteness, and the located uniform signature theorems were distinguished in [standard results](../foundations/02-standard-results.md).

The bounded test asked whether unrestricted congruences could eliminate an entire signature. [L001](../lemmas/L001-primitive-local-solubility.md) supplies a decisive negative: at least one primitive class survives every modulus, and nonzero primitive solutions exist separately over every Z_p. The required threshold was zero surviving classes. This is a route obstruction, not a new integer-solution exclusion or a counterexample to Beal.

The proof was checked at the boundary k=s+1, for p dividing z, and for p=2; the binomial remainder is divisible by the next required power. The bounded exact-arithmetic check passed 170 finite-representative cases and 1,625 prime/signature lifting cases to precision p^20, including 375 cases with p dividing z and 29,525 digit corrections. Reproduction: `python3 scripts/local-solubility/check_lifts.py`; output is in [results.json](../scripts/local-solubility/results.json). These checks exercise the construction rather than search for Beal solutions.

The assessment is NEGATIVE, with zero exploration turns outstanding. The unrestricted congruence approach is closed in [Attempt 001](../ATTEMPTS/001-unrestricted-congruence-obstruction.md). The reason for changing direction toward global signature reduction is that local existence is automatic, while fixed-signature finiteness still falls short of global nonexistence. The main gap remains unchanged. No complete candidate has appeared.
