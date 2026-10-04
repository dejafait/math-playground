# Stark-contraction test at the fixed two-prime p^2 index

This mathematical attempt uses the unchanged COVERED_TARGET in
[the saved SPECIALIZE assessment](literature/2026-10-03-rank-zero-extra-relaxed-prime.md).
Only the already assessed Sakamoto 2022 source, Section 2.5, is reread;
no new source search or literature assessment is undertaken.

## Gap, intermediate target and discriminating test

The main gap remains the rational rank lower bound for analytic order
at least two. The present intermediate target is still classical lifting
of the two prescribed mod-p basis classes at the same P_(2,0) primes.
L016 leaves one alternating coefficient tau. Test whether the actual
rank-one to rank-zero Stark contraction supplies an additional constraint
forcing tau to zero. Such a constraint would settle this coefficient
depth; higher-depth lifting, rational membership, analytic production of
the minimal index, the determinant comparison and higher ranks remain open.

Continue automatic promotion from this mechanism only if contraction or
its divisor transitions force both transverse errors to vanish. A compatible
nonzero-error contraction diagram stops that deduction from the tested
data. This adds the p-local canonical module and determinant transition
maps to L016's localization model; it does not merely rerun reciprocity
or reopen the rational subtraction in ATTEMPTS/016.

## Reasoning saved before completion

Put R = Z/p^2 Z, G = H^1_(F_cl^N)(Q,E[p^2]) and
C = H^1_(F_can^N)(Q,E[p^2]). L016 makes G free on c_1,c_2.
The residual strict-at-N group is zero, by the residual localization
isomorphism. Sakamoto's Lemma 2.2 makes its level-two counterpart zero.
Theorem 2.1 should therefore make the singular p-local map phi fit into
a split exact sequence 0 -> G -> C -> R -> 0. Thus C is free of rank
three, and phi contraction sends det(C) isomorphically to det(G).
This needs checking against Section 2.5's exterior bidual conventions.

At N the actual rank-zero Stark component is a unit multiple of
c_1 wedge c_2, since delta_2(N) is a unit and the two finite coordinates
are units. Its singular contractions to one-prime indices have the forms
unit * p B c_2 and unit * p C c_1. Their finite scalar regulators vanish.
The two-step contraction to the empty index contains p^2 B C and is
zero in R even when tau is nonzero. The nonzero vectors must not be
mistaken for their zero scalar regulators.

For an exact test extend the previous model with a new basis vector w
at the p-singular line and phi(w) = 1, phi(c_i) = 0. Use
s_1 = (0,-p tau,0), s_2 = (p tau,0,0),
f_1 = (1,0,0), f_2 = (0,1,0) on (c_1,c_2,w).
The determinant c_1 wedge c_2 wedge w contracts to c_1 wedge c_2.
Track determinant signs so the p contraction commutes with both
auxiliary-prime transitions and both paths to the empty index agree.
The model is only the divisor subsystem at N; neither a full Stark/Kato
family nor an elliptic-curve realization is asserted.

## Mathlib

Full coverage of this specialization: **not checked**. Supporting exterior
bidual contraction, Poitou--Tate duality and Cartesian propagation:
**not checked**. Sakamoto's Theorem 2.1, Lemma 2.2, Definition 2.23 and
Section 2.5 are the previously assessed primary inputs, not a claimed
full-statement Mathlib match.

## Completion

[L017](../lemmas/L017-prime-deletion-stark-contraction-retains-p2-error.md)
checks the saved argument. The actual p-local sequence at N splits and
its determinant contraction is an isomorphism. The proper-divisor
Stark vectors are unit multiples of pB c_2 and pC c_1; they are nonzero
when tau is nonzero even though all proper scalar regulators vanish.
Their final contraction is p^2BC = 0 in R_2.

The model extends the canonical p-local module and every divisor map
at N, with coefficient compatibility and commuting rank-one/rank-zero
contractions. `scripts/prime-deletion/check_p2_stark_contraction.py`
passes exact Z/25Z checks for all five tau values. This does not extend
the full auxiliary-prime family or evaluate the actual tau.

The result is an informative NEGATIVE for automatic promotion from the
tested determinant and divisor package, classified as REPRODUCTION.
No rational-rank improvement or result beyond checked literature is
claimed. A stronger coefficient and analytic initial-value comparison
requires separate screening; none is calculated in this step.
