# C101a — Literal d35 last-pair real-system exclusion

## Hypotheses

Use L055's complete 25 indexed pairs in literal order, changing only
H_0=5 and H_24=32670656. Fix B=9250245, kappa=23/11 and an
integer 0<=t<=B. Set a_i=2 for 0<=i<=22, a_23=2+18t and
a_24=2+18(B-t). Suppose real s_0,...,s_25 satisfy s_25=s_0,
s_i>=540/11 at every input i=0,...,24, and every endpoint

\[
s_{i+1}=2^{-a_i}\left((27/16)^{J_i}(3/2)^{H_i}s_i
                 -(12/11)(3/2)^{H_i}-1\right)+\kappa.
\tag{1}
\]

Require both guards at each outgoing row's own input:

\[
4J_i\log2\le\log s_i+\log(11/4),\qquad
H_i\log2<\log s_i+J_i\log(27/16).
\tag{2}
\]

All logarithms are natural. Equation (1) includes i=24 and closure,
including when a_24=2. No minimum, seed, junction integrality, parity,
residue, exact valuation, primitive count or actual-word realization
is assumed.

## Conclusion

No such real tuple exists for any integer 0<=t<=9250245.

This is a local RESEARCH/REPRODUCTION assembly under the prior SPECIALIZE
assessment `drafts/literature/2026-10-24-d35-last-pair-real-exclusion-assembly.md`.
It combines audited inputs and claims no new general mathematics beyond
the inspected sources. Its separate critical audit remains pending.
Early-support and cyclic-order reductions, actual-word transfer and
universal eventual descent remain unresolved. This is not a complete
Collatz candidate. Attempt032 and both original d0 witnesses remain valid.

## Proof

Assume a tuple as above exists. Keep its table, t, literal cut, full
tail list and all coordinates fixed throughout. The lower domain makes
all logarithms meaningful. On omitting only the H half of (2), the
tuple satisfies exactly L101 (1): all 25 endpoints, lower-domain bounds
and non-strict own-input J guards on the identical d35 table. Both
subtractions in (1) are inside tail division and kappa is outside,
as in L101; the i=24 equation closes at the same s_0. Import L101's
conclusion, secured by its completed step458 critical audit, without
rerunning its certificate.

If 2<=t<=B, L101 (2) gives

\[
\log s_{24}+\log(11/4)-4J_{24}\log2
<-8995174522561/500000000000<0.
\tag{3}
\]

The J half of (2) at that same s_24 requires the left side to be
nonnegative. This contradiction excludes the entire closed integer
interval 2<=t<=B. In particular t=B has
(a_23,a_24)=(166504412,2), and its closing endpoint is retained in
both statements. Thus t<2; integrality and nonnegativity leave exactly
t=0 or t=1.

Since 18B=166504410, the last two tails are (2,166504412) at t=0
and (20,166504394) at t=1. All earlier tails are 2. These are precisely
the two allocations in L100, with the identical table and literal cut.
Our full endpoints (1), including s_25=s_0, are L100 (1). L100,
secured by its completed step454 critical audit, establishes uniqueness
among all real endpoint tuples without assuming guard feasibility or
the lower domain. Consequently our hypothetical tuple is the very
endpoint tuple to which its H bound applies. In particular it has the
same s_18, not a coordinate at a different cut.

Row18 is unchanged from L055, with (J_18,H_18)=(693015,3295208).
For each of the remaining cases, L100 (2) gives

\[
\log s_{18}+693015\log(27/16)-3295208\log2
<-172437107269/12500000000<0.
\tag{4}
\]

The strict H half of (2) at the same outgoing row18 input requires
the left side of (4) to be strictly positive. This contradicts (4)
for both t=0 and t=1. These cases together with 2<=t<=B exhaust
the specified integer interval, proving the conclusion.

No survivor existence is asserted or needed: uniqueness identifies any
hypothetical endpoint tuple. There is no rotation, minimum/seed choice,
change of cut, integer-junction assumption or realization converse.
One necessary guard failure in each case suffices.

### Sources, overlap and qualifications

L055 supplies only its full pair table; its original-table witness,
minimum, seed and count premises are not used. The other direct inputs
are audited L100 and L101. C096a is a d34 precedent with different H
entries, not a theorem applied to d35. The scoped duplicate check and
prior assessment found no existing d35 assembly. Attempt032's failed
fixed package and the failed full O/S/C conjunction supply no premise
and remain recorded. No numerical or analytic calculation is added.

The upstream affine source is Halbeisen–Hungerbuehler, *Optimal bounds
for the length of rational Collatz cycles*, Acta Arithmetica 78 (1997),
227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp.228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The analytic sources are NIST DLMF
[4.5.1](https://dlmf.nist.gov/4.5.E1),
[4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.2.19](https://dlmf.nist.gov/4.2.E19), in the positive-real domains
and recorded version checked upstream in L100/L101 and the prior
assessment. Their finite-word, nonzero-denominator and positive-argument
applications are imported through those completed specializations.
No coding or analytic theorem needs reproof for this case assembly.

Only the literal last-pair subsystem is excluded. Other allocations,
nonliteral orders, actual-word transfer, other tables, unrestricted
cycles, divergence and universal eventual descent remain unresolved.

## Mathlib

Full matching coverage for this assembly and its finite d35 inputs is
unchecked. Supporting affine, logarithm and finite-case facts would not
by themselves be a matching theorem. Unknown coverage is not absence;
no Lean verification or external Lean build is claimed.
