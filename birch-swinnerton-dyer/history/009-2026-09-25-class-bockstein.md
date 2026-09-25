# 2026-09-25 — Ordinary Bockstein vanishing does not distinguish Kummer classes

Preserved existing changes and all inactive branches. Rechecked the
Clay page and Wiles's displayed rank assertion; the scope is unchanged.
The [saved test](../drafts/2026-09-25-class-bockstein-test.md) states
the gap, intended use, threshold, and discriminating test before the
calculation. This tests an individual class, beyond the previously
excluded representation-level contractions.

[L009](../lemmas/L009-class-bockstein-and-strict-local-derivative.md)
computes the global connecting cocycle and its ordinary Selmer
refinement. Under the existing auxiliary hypotheses the latter
vanishes on all of S, because it changes conjugation sign and the
dual minus Selmer space is zero. Every ordinary class lifts to first
order, including the classes whose Kummer membership is unknown.
This agrees with Castella--Hsieh's known first-height vanishing; the
new notebook consequence is that the proposed test adds no constraint.

The local-condition audit is essential: a strict class's unique
invariant ordinary lift has a local derivative Delta_d in D^-.
That scalar is zero exactly when a strict lift exists. Its value
cannot be inferred from the ordinary obstruction or fiber map alone.
No value for the actual kappa or Kummer implication is claimed.
The source and duality qualifications are retained in
[the foundation](../foundations/10-selmer-bockstein-duality.md),
including the original volume's web-reader size limitation.

Checked the cup-product sign, semilinear conjugation, self-dual
Poitou--Tate pairing, ordinary quotient invariants, local lifting
sequence, uniqueness of the invariant lift, and the opposite signs
of its derivative and allowable corrections. The c = 0 and c != 0
linear diagrams check both outcomes of the strict criterion, without
claiming arithmetic realization. No numerical or library check was
needed; Mathlib coverage is explicitly not checked.

Decision: reject ordinary first-order lifting as the missing Kummer
test; preserve the result in [the failed attempt](../ATTEMPTS/007-ordinary-bockstein-kummer-test.md).
The reason for a further local test is the precise remaining scalar,
whose actual value could either eliminate this refinement or supply
a new local constraint. Its necessity for rational points would still
need proof. The rank bound remains r <= 2, short of r >= 2, and
nonvanishing from complex analytic rank, auxiliary existence, and
higher ranks remain unresolved.

The new DAG row uses L006 for the dimension and strict class, and
L008 for the actual normalized anticyclotomic summand and tangent.
The duality and analytic-rank-zero results are named external inputs.
PROOF.md records the changed distinction between ordinary and strict
lifting; PROGRESS.md retains the sole concrete continuation action.
The shared checker passed with 9 nodes and 7 edges after compacting
PROOF.md to its 100-line limit; the mathematical input review confirms
both new direct inputs. `git diff --check -- .` also passed.

Step BSD-2026-09-25-009-class-bockstein is NEGATIVE, with new evidence
against a specified test. STATUS remains IN_PROGRESS; no complete
candidate exists. Exploration turns without an advance or informative
negative result remain 0 of 3.
