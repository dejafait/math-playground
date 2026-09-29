# Rank-zero Kato representative and its first-order lift

Date: 2026-09-26. Working record saved before the detailed test.

## Scope and continuation test

The approved target is the exact Next action assessed SPECIALIZE in
[the prior review](literature/2026-09-26-current-target.md). Keep all
L009--L011 hypotheses, including the Q_p coefficient restriction,
the nonzero generalised Kato class, and L(E^K,1) != 0.

The main gap remains q(kappa) = 0; the achieved bound r <= 2 still
lacks r >= 2. The intermediate target is to identify L011's relaxed
minus generator using the rank-zero twist's Beilinson--Kato class,
then test its obstruction for the inverse anticyclotomic deformation
1 - epsilon d. A computed obstruction or an actual lift would decide
the dual strict-lifting test. Even that would leave its relationship
to Kummer membership and the unrestricted BSD target unresolved.

Import the assessed reciprocity theorem. Do not reprove Kato's
construction or infer a lift from its cyclotomic family. L009's
ordinary lifting, L010's scalar ambiguity, and L011's formal-duality
countermodel have already excluded those shortcuts. Normalizing the
representative alone does not close the arithmetic obstruction.

The test must retain restriction to K, the twist identification,
both split local terms, and the inverse character. Continue only
with an arithmetic relation controlling the obstruction or a global
lift; an expression in the same unknown derivative is incomplete.
Exploration turns used on entry: 1 of 3.

## Completed test

[L012](../lemmas/L012-rank-zero-kato-obstruction-descent.md) records
the full normalization and descent calculation. The restriction w
of the twist's Kato class is anti-invariant and has nonfinite
localization. It therefore generates R^-. Both split local terms
contribute the same scalar lambda != 0, so the normalization is
w/(2 lambda), not w/lambda. The imported reciprocity statement is
isolated in [the foundation](../foundations/11-rank-zero-kato-reciprocity.md).

The mixed pairing is 2 lambda t_d(x). This is still the unknown
functional in L011. Nonvanishing of lambda determines neither its
value nor the value of the global obstruction. The cyclotomic
connecting class lies in a vanished minus H^2 space; the requested
anticyclotomic class lies in the surviving plus space. No passage
between these two directions has been obtained.

The descent calculation specifies a four-dimensional representation
W_d fitting in 0 -> V -> W_d -> V tensor chi_K -> 0. The class
z_tw lifts to H^1(Q,W_d) exactly when the original relaxed lift
exists. Its connecting class is -tilde_d cup z_tw. The natural
epsilon action anticommutes with conjugation, so this descent is
not the A-linear rank-two deformation required by the previously
checked universal-deformation theorem. The proof checks the group
law, connecting-map sign, and restriction in both directions.

## Assessment and route decision

Outcome: EXPLORATION, classification REPRODUCTION. The arithmetic
representative and the required extension are now specified, but
the discriminating test is unresolved. No global lifting cochain,
nonzero obstruction evaluation, rational point, or improved rank
bound was obtained. The step is not an advance beyond the checked
literature. Exploration turns used: 2 of 3, including the prior
source-review turn.

Reciprocity normalization alone has now exhausted its role. A
constructive Euler-system specialization into this explicit W_d
would supply different information. Its theorem match must be
reviewed before any such calculation; an Eisenstein specialization
of a Beilinson--Flach family is only an unscreened lead. No existence
of that family, regular specialization, or correct extension is
asserted here. The exploration budget is not renewed by this change.

The main gap q(kappa) = 0, the missing lower bound r >= 2, and the
unproved relation of strict lifting to Kummer membership remain.
Auxiliary existence, nonvanishing from m(E) = 2 alone, and higher
ranks also remain outside the achieved result. No complete candidate
argument has appeared.

## Mathlib

Full coverage and supporting coverage: **not checked**. The precise
source links and qualifications are retained in L012 and its foundation.
