# Cyclotomic specialization audit, 2026-09-24

## Selection recorded before the calculation

The shared instructions, local goal and checkpoint, whole argument overview,
and DAG were read. Existing local changes and the completed finite-Selmer
audit are preserved. The Clay page still links Wiles's statement of rank
equality, with the coefficient refinement stated separately; the recorded
scope remains applicable.

The gap is rank equality for arbitrary analytic order at least two. This
step tests the checkpoint's proposed intermediate target: recover the
Q_p-dimension of the base-field Selmer dual from the order at T = 0 of the
cyclotomic characteristic series, using good-ordinary control. A positive
result could feed an analytic-order comparison. The complex/p-adic analytic
comparison and the divisible part of Sha would still need justification.

This is distinct from L001: it examines a characteristic ideal of an entire
Iwasawa module, rather than a finite prefix of unmarked descent groups. The
standard module structure theorem may already show exactly what information
is lost, so no novelty is presumed.

## Discriminating test

Let Lambda = Z_p[[T]] and let X be a finitely generated torsion Lambda-module.
Compare ord_T char(X) with dim_Qp((X/TX) tensor Q_p). Continue an inference
from the characteristic ideal alone only if it determines that dimension.
Stop that inference if explicit modules have the same characteristic ideal
and different specialized dimensions, and isolate the extra condition that
restores equality.

The first candidate comparison is Lambda/(T^2) against (Lambda/(T))^2.
To retain even specialized dimensions, also compare (Lambda/(T^2))^2 with
(Lambda/(T))^4. These are algebraic models, with no asserted realization as
elliptic-curve Selmer duals. The expected distinction is between total length
at the prime (T) and the number of cyclic summands there.

## Source check and unfinished reasoning

[Ralph Greenberg, *Iwasawa Theory for Elliptic Curves*, Theorem 1.2,
printed page 4](https://arxiv.org/pdf/math/9809206#page=4) states Mazur's
good-ordinary control theorem with finite kernel and cokernel. Theorem 1.5,
printed page 5, supplies cotorsion over Q using modularity. Conjecture 1.12
and its discussion on printed pages 8-9 explicitly distinguish complete
reducibility from control; this is a standard missing condition to audit,
not a new claimed obstruction in the literature.

The calculation still to check at this save is localization at (T), including
why finite control errors disappear after tensoring with Q_p, and whether
the natural map from T-invariants to T-coinvariants detects equality.

## Completion of this saved calculation

[L002](../lemmas/L002-characteristic-order-specialization-defect.md) now
contains the full proof and explicit models. The characteristic-ideal-only
test is negative: it gives an upper bound, with an exact nonnegative module
defect. The natural invariant-to-coinvariant map is an isomorphism exactly
when that defect vanishes. The arithmetic application keeps the separate
Sha corank and analytic comparison explicit. No computation or arithmetic
realization of the models is needed for this algebraic conclusion.
