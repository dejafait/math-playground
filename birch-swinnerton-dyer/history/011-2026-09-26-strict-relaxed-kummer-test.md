# 2026-09-26 — The strict Kummer test retains a relaxed obstruction

Preserved the existing L010 changes and all inactive branches; other
notebooks were not edited. Rechecked the Clay page and Wiles's page-2
rank assertion, with the refinement still separate. The
[saved test](../drafts/2026-09-26-strict-relaxed-kummer-test.md)
states the gap, proposed use, threshold, and prior failures.

[L011](../lemmas/L011-strict-relaxed-pairing-on-kummer-vectors.md)
derives the strict/relaxed pairing and its determinant on the strict
vector formed from rational P,Q. The relaxed minus space has dimension
one despite the vanished ordinary minus space. The determinant is
independent of the local lift choice, and its vanishing is equivalent,
in the rational rank-two test, to lifting the normalized relaxed minus
class along the inverse anticyclotomic deformation.

The formal-duality test fails: dual complexes and an injective
logarithm on a rational lattice permit a nonzero determinant even
when the formal Kummer space is all of S. This supplies new evidence
beyond L009's localization diagram, but is not an arithmetic example.
Necessity for actual rational points remains undecided. Recorded the
specific failed inference in [the attempt](../ATTEMPTS/009-formal-duality-strict-kummer-vanishing.md).

The effect on the main gap is diagnostic: no new point or rank bound,
and q(kappa) = 0 is still missing. The bound remains r <= 2, short of
r >= 2. The reason to test an arithmetic relaxed class is the newly
isolated global obstruction -d cup z^-. Its possible rank-zero Kato
representative offers a concrete source to check, while its usual
cyclotomic variation must not be mistaken for the required direction.

Checked the cone sign, dual local conditions, inverse character,
absence of local H^0 terms, eigenspace dimensions, determinant
independence, and the rational-lattice qualification. The exact check
`python3 scripts/strict-relaxed/check_model.py` passed for both zero
and nonzero obstruction. The shared documentation checker passed
with 11 nodes and 10 edges; `git diff --check -- .` passed. Mathlib
coverage remains not checked. The source qualifications and direct
links are retained in the expanded duality foundation.

The two new direct DAG inputs are L005's Kummer/logarithm facts and
L009's invariant lifts and local derivative. The duality is a named
external input. PROOF.md records the changed obstruction; PROGRESS.md
is the sole current checkpoint and concrete next-action record.

Step BSD-2026-09-26-011-strict-relaxed-kummer is NEGATIVE for a
specified formal inference, not for arithmetic necessity or BSD.
STATUS remains IN_PROGRESS; no complete candidate exists. Exploration
turns without an advance or informative negative result remain 0 of 3.
