# 2026-09-25 — Points and a p-adic coefficient certify rank

Preserved the existing edits, identifiers, and inactive branches. Read
the full overview and DAG before the detailed proofs, and rechecked the
Clay source with unchanged scope. The
[saved selection and test](../drafts/2026-09-25-point-coefficient-certificate.md)
identify the gap, additional arithmetic input, and success threshold.

[L004](../lemmas/L004-point-coefficient-rank-certificate.md) establishes
the proposed matching certificate. Its
[source audit](../foundations/05-kato-divisibility.md) retains non-CM E
and good-ordinary p >= 5. Kato's divisibility up to a power of p suffices
for the T-order comparison; no residual-surjectivity assumption remains
after the checked representation case split. The original Kato PDF
exceeded the retrieval limit, so the elliptic translation is explicitly
cited through the directly checked Stein--Wuthrich statements.

The discriminating test succeeds: matching independent points and a
certified nonzero coefficient force both recorded defects to vanish.
The unmatched bound still leaves a gap of n-k, which the statement
retains. Finite p-primary Sha and nondegenerate cyclotomic height are
conclusions in the matching case, not hidden assumptions. Lower
coefficient vanishing follows mathematically; finite numerical zeros
are not used. The mechanism already appears in the cited literature
and is recorded as a standard arithmetic input, not new general
mathematics or a complete candidate proof of BSD.

Decision: retain this certificate and turn toward producing its lower
bound from complex analytic rank two. The proposed lead is
[Darmon--Rotger, *Elliptic curves of rank two and generalised Kato classes* (2016)](https://link.springer.com/article/10.1186/s40687-016-0074-9).
It has not been imported as a rational-point existence theorem. The
reason for this direction is that another restatement of the matching
criterion supplies neither independent rational points nor a comparison
with m(E). Whether the construction can provide rational, independent
Kummer classes is a concrete test; its success is not presumed.

Mathematical review checked the classical Selmer module, primitive
ordinary L-function, generator coordinate, non-CM and prime scope,
divisibility direction, power-of-p issue, independence modulo torsion,
the k = n = 0 case, and the finite-precision exclusion of zero. L002
supplies the exact defect formula and L003 supplies consequences of
equality; both are genuine direct inputs. No numerical computation
or Mathlib lookup was required for this step.

The required command
`python3 ../scripts/docs/check_structure.py --problem birch-swinnerton-dyer`
passed with four nodes, three genuine direct mathematical edges, valid
links, and compact overviews. `git diff --check -- .` passed. Bytecode
writing was disabled for the shared checker. Structural validation does
not establish the correctness of the cited arithmetic theorems.

Completed step BSD-2026-09-25-004-point-coefficient-certificate is ADVANCE:
a standard arithmetic certificate now addresses the two explicit defects.
Uniform certificate production and the complex analytic comparison are
still missing. STATUS remains IN_PROGRESS. Exploration turns without
an advance or informative negative result remain 0 of 3.
