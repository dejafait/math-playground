# L053 — Global triple small-principal batch admits an above-threshold trial

## Hypotheses

Use C001a's instance, any tuple width m>=1, and selected 68-element
agreement supports in H. Put n=1024, w=68, v=956,
N=binomial(1024,68), tau=65537^28/2^128 and T=floor(tau)+1.
Let V be the set of all 68-subsets of H. Moment coordinates x(D) are
real and indexed by subsets D of V of size at most three.

Consider exactly this relaxation: x(empty)=1; every moment is
nonnegative; a moment is zero if its family contains a distinct pair
intersecting in at least 64 points; every L020-incidence triple with
nonsingular actual-label matrix has moment zero; the augmented
empty/singleton union matrix is PSD; and for every A,B,C in V retain
the principal union matrix with indices {A}, {A,B}, {A,C}, removing
duplicate indices. The objective is sum_A x({A}). Pairs are free
variables in this relaxation. No full singleton-conditioned matrix,
anchor-free three-index matrix, complement matrix, extra scalar
Frechet inequality or degree-four coordinate is included.

The fixed trial uses L021's exact primal a_i, L022's p_0=1,
p_1=...=p_4=0 and p_i=a_i/(2 binomial(68,i)binomial(956,i)) for i>=5.
Set lambda=p_68>0 and U=binomial(1024,64)/binomial(68,64).

## Conclusion

The stated relaxation admits the following global rational trial of
objective M=(U+1)/2, with floor(M)>=T and 1383/1000<M/tau<1384/1000:

- x(empty)=1 and x({A})=rho=M/N.
- For distinct A,B at half-distance i=68-|A intersection B|,
  x({A,B})=rho*p_i.
- For distinct A,B,C at pair half-distances i,j,h, set x({A,B,C})=0
  if a distance belongs to {1,2,3,4} or the full L020 incidence occurs.
  Otherwise set x({A,B,C})=rho*p_i*p_j*p_h/lambda.

Boolean repetitions use the lower-order coordinate. The extra zero
includes realizable L020 triples: it is a choice of this trial, not a
constraint asserted for every list. It covers all actual nonsingular
L020 triples without averaging actual labels.

Consequently this batch alone cannot certify an integer list bound
below T. This is nonexclusion by a relaxation, not full degree-three
feasibility, a representing measure, a support packing or an unsafe
RS list. The 955–957 bracket and both 67/68-agreement safety gaps remain
unchanged. The separate critical proof review below retains this conclusion.

## Proof

**Known program and support specialization.** Import Polak,
*Semidefinite Programming Bounds for Constant-Weight Codes*,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1),
15 March 2017, Section 1.1 (1)–(3), Proposition 1.1 and its complete
indicator proof, printed p. 2. Its proof bounds A(n,d,w), retaining
the displayed-endpoint qualification in
[foundations/12](../foundations/12-global-degree-three-moment-source.md).
The nonnegative formulation is corroborated by Brouwer–Polak,
[arXiv:1709.02195v1](https://arxiv.org/pdf/1709.02195v1),
7 September 2017, Section 2 (1), p. 2. We specialize the known union
matrices at order three; no hierarchy theorem is reproved.

For any received array, L001 selects distinct supports for its whole
tuple list, with pair intersections at most 63; their binary distance
is at least 10. L020 excludes precisely the nonsingular triples under
its incidence hypotheses, in every extension-field tuple row and for
all m. The code's indicator coordinates therefore satisfy both these
zeros and the imported union-matrix conditions. Retaining principal
matrices preserves necessary PSD constraints. Thus the displayed
relaxation still provides an upper-bound method for this support
family, uniformly in m. We impose no extra incidence-zero condition
on arbitrary lists. The trial's stronger zero prescription is allowed
because all coordinates are free apart from the listed constraints.

**Orbit scope and Boolean coordinates.** Relative to anchor A, let
i=|A\B|, j=|A\C|, t=|(A\B) intersection (A\C)| and
s=|(B\A) intersection (C\A)|. Then h=i+j-t-s is B,C half-distance.
The eight disjoint regions, in this order, have sizes

  t, i-t, j-t, 68-i-j+t, s, i-s, j-s, 956-i-j+s.

They are respectively A-private, AC-only, AB-only, common, BC-only,
B-private, C-private and outside. Their nonnegativity is equivalent
to foundations/04's full actual-orbit ranges. Conversely any such
integer regions can be chosen inside H: they sum to 1024 and reconstruct
three 68-subsets. Thus every labeled triple is covered. The L020
incidence (common 61, each pair-only two, each private three) occurs
exactly at (i,j,t,s)=(5,5,3,2), with h=5. The same incidence is preserved
by every support permutation. Distances alone do not identify it:
other (5,5,5) orbits keep the product value.

When any half-distance is zero the two corresponding supports are
equal. Removing duplicate union-indices gives [1] for three equal
supports, and [1,p_b; p_b,p_b] for two distinct supports, after dividing
by rho. The triple moment is rho*p_b, not the distinct-triple formula.
For three distinct supports the normalized matrix is exactly

  K=[1,p_i,p_j; p_i,p_i,y; p_j,y,p_j],

where y is the prescribed normalized triple value. Hence the trial
defines one consistent symmetric function on support families; no
group average of an arbitrary labeled point is used.

**Full augmented pair matrix.** Import all Johnson eigenmatrix entries,
their shared eigenspaces and constant projector J/N from
[foundations/09](../foundations/09-global-pair-johnson-source.md):
Brouwer–Cioabă–Ihringer–McGinnis,
[arXiv:1709.09011v2](https://arxiv.org/pdf/1709.09011v2), Section 3,
opening formulas, p. 10; Brouwer–Haemers, *Spectra of Graphs*,
[author preprint](https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf),
Section 11.2, pp. 162–163. Its Theorem 2.7.1(i), p. 36, supplies the
Schur congruence, including singular lower blocks.

Let A_i be the distance-i relation matrices and P=sum_i p_i A_i.
The augmented matrix has leading entry 1, off-diagonal vector rho*1
and lower block rho*P. Its Schur complement is rho*P-rho^2*J.
Complete exact arithmetic reconstructs all 69 eigenvalues mu_j of P.
They are mu_0=M, mu_j=1/2 for 1<=j<=64, and respectively

  30789161673/26556181345, 787342157/801136197,
  478922161/478531017, 476380573/476387541

for j=65,66,67,68. All are positive. The constant Schur eigenvalue
is rho*(M-rho*N)=0; every nonconstant eigenvalue is rho*mu_j>0.
Thus the full augmented pair matrix is PSD, including its singular
constant coordinate. The row sum identity is checked as
sum_i binomial(68,i)binomial(956,i)p_i=M, not inferred by confusing
Schrijver's conditional normalization with a global moment.

**Complete retained principal PSD.** Write D for the least common
multiple of the p_i denominators, A_i=D*p_i, H=D^2*A_68>0 and
P_i=H*p_i. The triple numerator over H is A_i*A_j*A_h in the
permitted distinct case, zero in the forbidden/overridden cases,
and P_b for repetitions. For each distinct-support matrix H*K,
the saved seven principal-minor numerators are

  H, P_i, P_j,
  H*P_i-P_i^2, H*P_j-P_j^2, P_i*P_j-Y^2,
  H*P_i*P_j-H*Y^2-P_i^2*P_j-P_j^2*P_i+2*P_i*P_j*Y.

All are nonnegative. A size-r minor of the actual moment matrix is
(rho/H)^r times its saved numerator, a positive scaling. This certifies PSD:
Schur congruence with leading entry 1 reduces K to 1 and a symmetric
two-by-two matrix with diagonal p_i-p_i^2, p_j-p_j^2 and determinant
det K. Nonnegative diagonals and determinant suffice by completing
the square when the first diagonal is positive; when it is zero,
nonnegative determinant forces the off-diagonal zero and the remaining
diagonal is nonnegative. This elementary final sign implication is
included to explain the finite certificate, rather than reproving an
imported hierarchy. For repeated supports the complete one-/two-index
principal minors give the same conclusion. No positive pivot is
assumed when a diagonal vanishes.

The full certificate is
`scripts/finite-support/global-triple-principal-results.json`.
All 4761 ordered i,j entries retain their inclusive t,s ranges and
their full h-to-record maps, with the sole incidence override explicit.
There are 1500625 actual ordered orbits, 205 repeated-support orbits,
10232 pair-forbidden orbits and one ordered incidence-zero orbit.
The finite numerical cache has 29191 records, 83931 anchor evaluations
and all 586967 principal-minor numerators. Every original orbit selects
its exact record; this compression identifies evaluations only, not
independent variables or labeled constraints. All moments are
nonnegative and every required zero is present.

The independent verifier imports no constructor routines. It rebuilds
binomials by factorials and Johnson coefficients by polynomial
convolution, checks L021's 64 defining primal equations and exact L022
pair agreement, regenerates actual orbits from eight-region
nonnegativity, and reconstructs Boolean unions by explicit support
equality. It computes every saved principal minor by the determinant
permutation formula, instead of the constructor's closed formulas.
Every minor identity and sign, every orbit mapping, every record's use,
all six incidence permutations, all spectra and the constant Schur
coordinate are checked. Its 1934857 checks have no failures in
`scripts/finite-support/global-triple-principal-audit-results.json`.
The complete load-bearing arithmetic is checked, not a preview or
approximate eigenvalue. Reproduce from this notebook with
`python3 scripts/finite-support/global_triple_principal.py`, then
`python3 scripts/finite-support/audit_global_triple_principal.py`.

**Objective and limit of the result.** N*rho=M exactly. Independent
integer comparisons check floor(M)>=T, where

  T=2136899816051353757057904852229805411030924365970844208573659527927004771612162841121670742371612.

L022's exact ratio interval applies to this unchanged objective. An
upper bound on every feasible point of this relaxed program cannot
be less than M; even flooring cannot make it below T. This parks only
the specified small-principal batch as a sufficient threshold method.
No upper bound on other assignments, full conditioned feasibility,
representing measure, actual packing or common-center list follows.
The approved SPECIALIZE assessment is
`drafts/literature/2026-10-11-global-triple-small-principal-test.md`.
This is REPRODUCTION of known moment/spectral methods, with new local
diagnostic evidence and no claim of progress beyond the checked sources.

**Separate critical proof review (2026-10-12, step 171).** The approved
scope is the unchanged SPECIALIZE audit in
`drafts/literature/2026-10-11-global-triple-principal-critical-audit.md`.
The review retains the result, with no stronger feasibility claim.
The source imports above are reused; their hypotheses have not changed.
The following checks connect the complete arithmetic to the precise
necessary relaxation and its nonexclusion interpretation.

For a list at an arbitrary received array, choosing one 68-subset of
each simultaneous agreement set is injective: equal selected supports,
or an intersection of size at least 64, would identify every polynomial
row by L001. Three selected supports satisfying L020's incidence cannot
have its nonsingular matrix, since common-root division would identify
all three tuples row by row. These statements allow extra agreements,
any m>=1, and message coefficients in the ambient extension. The
indicator of this support family therefore satisfies precisely the
necessary zeros and imported union-matrix constraints. This includes an
empty support family. It does not justify zeroing realizable incidences
in the relaxation; that stronger choice remains confined to the trial.

Every original orbit is reconstructed from all eight nonnegative region
sizes. Their sum is 1024, and each reconstructed support has size 68,
so there is no additional label-capacity condition. The common/pair-only
and private sizes defining the override are symmetric under all six
support permutations. The remaining triple value is a symmetric function
of the distance multiset. This verifies that the orbit recipe defines
one moment for an unordered support family, without averaging a labeled
feasible point or identifying general variables. In particular the
nonoverridden (5,5,5) distance triples are retained.

The independent verifier's explicit Boolean set unions were checked
against all equality patterns: three equal supports give one index;
exactly two distinct supports give the indices {A} and {A,B}, after
renaming the second support if necessary. This remains true when the
two nonanchor supports coincide. Their normalized matrix is
[1,p_b; p_b,p_b], including p_b=0. Three distinct supports give exactly
K above, even if two distances coincide. All 205 repeated orbits and
all forbidden-distance orbits are included in the complete reconstruction.

The full augmented matrix is rho times the pair matrix in its lower
block, not the conditionally normalized pair matrix itself. Its row
sum and rho*N=M make the constant Schur coordinate zero; all 68 other
spectral coordinates are positive. The imported congruence inverts only
the leading 1. For the retained conditioned matrices, all seven minors
are checked when the dimension is three, and all applicable minors
when it is smaller. The zero-diagonal Schur case is explicitly covered
by the two-by-two determinant implication above; positivity of the full
determinant alone is not being substituted for PSD.

The inspected independent verifier was rerun on the complete certificate:
1934857 exact checks pass, covering every one of the 1500625 original
orbits, all 29191 records, 83931 numerical anchor evaluations, 586967
saved minor numerators, and all 69 spectral coordinates. It reconstructs
every minor value and sign, not merely counts or saved success flags.
No constructor routine is imported. The compression is exhaustive because
each original orbit has its checked map and every saved record is used.

An additional manuscript check,
`scripts/finite-support/critical_audit_global_triple.py`, compares all 69
explicit spectra claimed above with that full reconstruction, rebuilds
all pair values and the exact objective, checks 0<=p_i<=1 including the
Boolean cases, and separately verifies both strict ratio endpoints and
floor(M)>=T. All ten checks pass. Its complete exact evidence is in
`scripts/finite-support/global-triple-critical-audit-results.json`, with
the hash of the full reconstruction report. The positive integer gap is

  floor(M)-T = 818800418770273232490429181396452979859057164019424490617686087189734207909878938613163813838172.

Thus even flooring the relaxed optimum cannot yield an upper bound
below the smallest unsafe integer T. The conclusion concerns the
strength of this necessary relaxation, not existence of an integer
support family of size floor(M). Reproduce the critical verification
by running `python3 scripts/finite-support/audit_global_triple_principal.py`
and then `python3 scripts/finite-support/critical_audit_global_triple.py`.
This is local proof verification and reproduction of assessed methods,
not new mathematics beyond the sources checked. No defect was found in
the stated implications. Full conditioned PSD, representing measures,+a useful uniform bound and RS realization are still not established.

## Mathlib

The full matching global degree-three program, labeled support
specialization and this exact finite certificate are **not checked**
in Mathlib. Supporting Johnson spectral, Schur and Boolean-union
coverage is also not checked. The precise primary imports above and
the full rational verification supply the argument; unknown library
coverage is not evidence of absence.
