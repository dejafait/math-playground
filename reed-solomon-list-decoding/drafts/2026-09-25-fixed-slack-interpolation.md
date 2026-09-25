# Fixed-slack interpolation audit — 2026-09-25

## Gap, target, and test

The existing scalar cover applies to solutions of a supplied differential
equation; no such equation has yet been justified for every received word.
This step tests whether, at A=k+ceil(gamma n) agreements, one can choose
nonzero Q(X,Y_0,...,Y_r) with r and total Y-degree bounded only by gamma,
and X-degree O_gamma(n), containing every degree-below-k candidate.
The plausible use is the existing cover and agreement count. A polynomial
sufficient field condition would still leave the exact boundary, all-field
scope, and the ABF source comparison unresolved.

The shared instructions, local goal/checkpoint, whole proof overview, DAG,
existing changes, relevant cover/count proofs, and failed q-polynomial
transfer were read. No existing lemma supplies this interpolant. The prior
failure concerns a bound growing with q, not this field-independent
construction. Existing unfinished work is retained.

The [prize statement](https://proximityprize.org/) was rechecked on September
25 and retains the base-field threshold and existence proviso. The source
under review is [TR26-169, September 5, 2026 version, Corollary 3.9 and
Lemma 4.1, printed pp. 16–17](https://eccc.weizmann.ac.il/report/2026/169/download#page=16).
Their underlying fixed-shape construction in Proposition 3.7 is sufficient
for this qualitative test; optimizing the derivative order is unnecessary.

The test passes if the local linear conditions have a nonzero common
kernel with uniform r and Y-degree, and every agreement forces enough
root multiplicity to make the substituted polynomial identically zero.
It fails if the kernel count, padding, or characteristic assumptions force
either of those parameters to grow with n. Achieved bounds will be compared
with epsilon* q, not merely called polynomial.

## Saved working reasoning

Set theta=gamma/2 and K=ceil((1-theta)A). Then K>=k, K<=A,
A/(K-1)>=(1-theta)^(-1), and K-1>=gamma n/4 once n is large.
It is enough to prove the fixed-shape dimension/rank ratio grows as
(K-1) r^eta for some eta>0 depending only on gamma. The source uses
multiplicity r^3; this will be denoted mu to avoid confusing it with the
interleaving width m. Choose r first, then n large enough that r<K.

The construction uses a derivative-tail monomial set cut off in both
weighted and ordinary degree. After X=alpha+T and Y_0=y+TU, a backward
Taylor change U=E+sum_j(-1)^(j+1)T^(j-1)Y_j exhibits a large explicit
kernel for the local constraints. This rank estimate, the strict
degree-versus-multiplicity inequality, and all rounding cases are the
remaining checks within this step. The small-message-degree case k-1<r
must be treated by its ambient affine cover, not an invalid use of L005.

## Completed result and checks

[L006](../lemmas/L006-fixed-slack-differential-interpolation.md) proves the
interpolation statement, including the underlying dimension and local-rank
estimates. Fix 1<c<s<(1-gamma/2)^(-1). The rank per received pair is at most
C_0 |T| mu^3 r^(-eta), where eta=1-1/c>0 and mu=r^3; the coefficient
dimension is at least a_0 |T|(K-1)mu^3. The explicit choice
r^eta>=8C_0/(a_0 gamma), followed by n>=ceil(4r/gamma), makes the total
rank at most half that dimension. Thus r is fixed before n.

The proof controls the derivative-tail enlargement by unit-cube volume
bounds and Markov's inequality on a simplex, with an explicit floor
estimate for W. The local kernel has a nonzero lowest T coefficient even
in small characteristic. Backward Hasse–Taylor identities give root
multiplicity mu at each agreement, and strict weighted degree below mu A
forces the differential identity. These arguments supply the required
scalar conclusion without relying on the optimized order calculation or
on a differential-equation root enumerator.

The exact checks cover ceiling boundaries, independence when binomial
coefficients vanish, the equality i+rb=mu at the recording cutoff, and
the strict multiplicity comparison. In characteristic two, the displayed
r=2 kernel vector still has a nonzero lowest coefficient. Interpolation
therefore has no hidden restriction on p. No numerical test or new
computational script was needed for these identities. Mathlib coverage
is not checked.

The immediate assembly is
[C006a](../lemmas/C006a-fixed-slack-list-certificate.md). It treats k-1<r
by an ambient degree-one cover instead of deleting derivative variables
from Q, which could annihilate it. Otherwise the existing scalar cover
applies under p>max(k-1,B_gamma). The DAG records only the mathematical
inputs used in this assembly; the interpolation proof itself has no
local lemma input.

## Threshold comparison and assessment

The certificate has beta=Delta_* sum_(a=0)^r n^a and list bound beta^m,
with beta<=C_gamma n^(5r+1). Thus q>=epsilon*^(-1) beta^m suffices at
radius 1-k/n-gamma. The constants are explicit but potentially enormous.
The exact safe grid index for a given field is not determined. Neither
epsilon* q>=1 nor extending a field of deficient characteristic implies
the certificate's hypotheses.

The discriminating test passes: this is ADVANCE, with exploration turns
0/3. The interpolation bottleneck is removed and a complete informal
partial certificate is assembled; no complete challenge candidate
appeared. The unresolved characteristic restriction now comes from the
solution cover, making agreement filtering on its Frobenius obstruction
a concrete different issue to investigate. Full target scope and the
ABF comparison remain qualified.
