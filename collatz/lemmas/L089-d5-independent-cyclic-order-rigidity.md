# L089 — d=5 independent cyclic-order rigidity

## Hypotheses

Take all 25 indexed pairs of L055, changing only H_0=35 and
H_24=32670626. Every J is unchanged. Put r=25, B=9250245 and
kappa=23/11. Let b_i be nonnegative integers with sum b_i=B,
a_i=2+18b_i, and let pi be any permutation of {0,...,24}.
Suppose real s_0,...,s_25 satisfy s_25=s_0, s_k>=540/11 and,
for every 0<=k<25,

\[
s_{k+1}=2^{-a_{\pi(k)}}(G_{\pi(k)}s_k-Q_{\pi(k)})+\kappa,
\quad G_i=(27/16)^{J_i}(3/2)^{H_i},
\quad Q_i=(12/11)(3/2)^{H_i}+1,
\]
\[
4J_{\pi(k)}\log2\le\log s_k+\log(11/4).
\]

Each outgoing indexed row keeps its allocation and own input.
All logarithms are natural. There is no H guard, seed, minimum-location,
integer-junction, actual-word, parity, residue, exact-valuation or
primitive-count premise.

## Conclusion

Every feasible cyclic order is a rotation of 0,...,24. More precisely,
rotation to any smallest designated junction makes pi the identity.
This holds over the full nonnegative integer allocation simplex,
including allocations with closing tail 2.

This is a local RESEARCH/REPRODUCTION under the prior SPECIALIZE
assessment `drafts/literature/2026-10-20-d5-independent-cyclic-order.md`.
It applies an existing audited sufficient criterion; it establishes no
new ordering mechanism or result beyond that criterion and its finite
data. The separate critical audit below found no defect within this scope. It asserts neither
feasibility nor a real-system, integer-cycle or actual-word exclusion.
Universal eventual descent remains unresolved.

## Proof

Apply L075 independently, without the full C077a conjunction.
The indexed pairs are exactly L084's d=5 table. The L055 J table gives
2<=J_0<...<J_24, and every changed or unchanged H_i is at least 35.
Opposite H changes preserve the totals, so L084's audited values give
K=sum(3J_i+H_i)=397573379 and
N=sum(4J_i+H_i)+2r+18B=630138897, exactly L075 (1).

Use L084's independent O constants

\[
\lambda=10584/10^{14}=1323/12500000000000,\quad T=27,
\quad\ell=693147180559/10^{12},\quad
u=1098612288669/10^{12},\quad v=2.
\]

The following matches every L075 data hypothesis. The exact finite
operands are in `scripts/postspell-word-count/h-transfer-family-certificate.json`,
at `/tables/4/O`; their existing independent reconstruction is proved
in L084's step-337 audit and stored in
`scripts/postspell-word-count/h-transfer-family-audit-certificate.json`.
These are imported audited inputs, not a new certificate calculation.

* L075 (2): L084's positive Lambda enclosure gives 0<lambda<Lambda.
  Its analytic audit certifies 0<ell<=log2, log3<=u and
  log(11/4)<=2. The O cap is exactly
  U=23r/(11lambda)+23/11=7187500000030429/14553.
  The audited inequalities are U<500000000000<P(27)<exp(27),
  where P(27)=sum_(j=0)^40 27^j/j!. Thus U<=exp(T).
  This uses the O cap, without any S/C/H cap.
* L075 (3): the row0 tail-2 offset is exactly
  -150093939512297169/377957122048<0. Every other row has
  H_i>=72, so its offset is at most the certified value
  -67585198634721895314242333308740579/51946031311566097350656<0.
  The enclosure direction follows because
  81/44-(3/11)(3/2)^H decreases with H. L084's audit verifies
  these complete O records, including the changed final row.
  This is a tail-2 offset condition; the failed tail-20 support
  condition at row0 is unused.
* L075 (4)–(5): the saved O records contain every k=0,...,23,
  with A_k=sum_(i<k)(3J_i+H_i) and
  D_k=sum_(i<k)(4J_i+H_i+2) for this changed table.
  L084's audit reconstructs every indexed operand and margin.
  Their minimum is 629441541677/50000000000>12.58>0.
  The empty prefix has A_0=D_0=0; the final eligible prefix has
  A_23=144318707,D_23=162928784. These are the d=5 prefixes,
  not the d=0 benchmark. All 24 required tests therefore pass.

Finally the proposed tuple's allocation and permutation hypotheses
are precisely those of L075. Its endpoint equation, lower domain,
closure and non-strict own-input J guard are exactly L075 (6)–(7),
including every occurrence and the final edge. No data certificate
is substituted for these tuple hypotheses. All hypotheses now match,
so L075's conclusion proves the stated cyclic-order rigidity directly.
Its existing proof retains all actual allocated tails in the product
and compares them at actual lower-domain inputs only. Its rotation
moves each outgoing row and allocation with its own input and keeps
the old closing edge and new closing edge. Hence neither an assumed
minimum at indexed row0 nor a lost cut is introduced by this application.

No general affine identity, analytic inequality or first-displacement
argument is reproved here. The underlying formal affine identity used
by L075 is Halbeisen–Hungerbuehler, *Optimal bounds for the length of
rational Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239, section 2, equations (2)–(4), Lemma 2,
pp. 228–229 ([primary paper](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf)).
Only its formal real affine scope is used through L075; no parity or
integer realization transfers. L084 supplies the already audited
analytic certificate application, not unverified numerical estimates.

Attempt 032 still stops the full O/S/C/H conjunction at d=5.
The independent O implication does not require its failed S datum.
Both original d=0 rational witnesses remain valid. C088a is only
prospective downstream motivation: no assembly with its literal
exclusion is made here, and no actual-word consequence is inferred.

### Independent critical audit — 2026-10-20, step 369

This RESEARCH/REPRODUCTION proof audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-20-d5-independent-cyclic-order-critical-audit.md`.
The verdict is no defect in the complete L075 application, including its
statement about any smallest designated junction. This establishes local
reliability of an existing implication, not a new ordering theorem, a new
exclusion family or progress beyond the inspected source machinery.

**Coverage and imported evidence.** Reused the ready independent-order
source assessment, the complete L075 statement/proof and step-281 audit,
and L084's step-337 analytic and independent O reconstruction. The formal
affine source is the precise Halbeisen–Hungerbuehler citation above;
positive-real logarithm/product and series coverage is NIST DLMF
[4.5.1](https://dlmf.nist.gov/4.5.E1),
[4.2.19](https://dlmf.nist.gov/4.2.E19) and
[4.6.4](https://dlmf.nist.gov/4.6.E4), in the version recorded by the
ready assessment. No current-version claim or new source retrieval is
made. No scalar ordering optimizer, integer-realization converse or full
C077a conjunction is imported. Scoped histories 360–368 and d5 notes
contained no completed L089 audit; Attempt 032 was read and preserved.

The complete `/tables/4/O` of the construction certificate and
`/reconstructed_tables/4/O` of the independent audit certificate were
inspected with the JSON inspector's selected `--full` reads, including
all 25 offsets and all 24 margins, not a preview or only a PASS flag.
The complete reconstructed rows, counts, Lambda interval, relevant
logarithm endpoints/remainders and degree-40 exponential sum were also
inspected. The construction's SHA256 is
`7d1d3061646525d514ea06b191250e5ee9235efd48d17848e6a0d184e64c5955`,
matching the audit's recorded input hash.

The existing auditor's relevant code independently transcribes L055's
pairs, changes precisely the two H entries, sums every prefix, constructs
the rational offsets and margins, and regenerates the analytic intervals.
Its saved reconstruction and canonical step-337 verification are
imported audited inputs. That completed audit reports 354310 recursive
leaf comparisons and 2086 proof/report checks with zero mismatches;
these are historical verification counts, not checks rerun this turn.
No mathematical program or certificate was changed or rerun here.

**L075 (1): table and totals.** All 25 reconstructed pairs match L055
except exactly H_0=35,H_24=32670626. The unchanged J list is strictly
increasing from 8 to 30998279; H_0=35 and every other H_i>=72.
Thus all integer pair/domain hypotheses hold, with r=25>=3 and
B=9250245>=0. The opposite changes preserve sum H=199390205 and
sum J=66061058. Consequently K=3*66061058+199390205=397573379 and
N=4*66061058+199390205+50+18*9250245=630138897.
These are table/budget identities for every allocation. L055 contributes
its indexed pairs only; its witness, minimum, H/seed and primitive-count
conditions are not imposed on the d5 tuple.

**L075 (2): independent analytic tests.** The O constants, including
v=2 rather than another package's v, match the displayed constants
exactly. L084's 100-term logarithm intervals use
z=(x-1)/(x+1)=1/3,1/2,7/15 for x=2,3,11/4 and the positive
remainder bound 2*z^201/[201*(1-z^2)]. The complete Lambda endpoints
use N times the lower log2 endpoint minus K times the upper log3 endpoint,
and the opposite choices for the upper bound. Both integer coefficients
are positive; no amplified error is dropped. Their audited comparison
places Lambda strictly between 10584/10^14 and 10585/10^14.
The same analytic evidence gives ell<log2, log3<u and log(11/4)<2,
all in the directions required by (2).

The exact O cap is U=7187500000030429/14553<500000000000.
The complete degree-40 lower sum is

\[
P(27)=
\frac{1112436109266660239093546627471481746956608769015849}
{2106019961293006716393905717248000000000}
>500000000000.
\]

Its audited recurrence t_0=1, t_j=27*t_(j-1)/j produces
sum_(j=0)^40 t_j; all omitted exponential terms are positive.
Thus U<P(27)<exp(27). This matches the independent minimum cap
without any S, C or H cap and supplies every part of (2).

**L075 (3)–(5): complete offsets and changed prefixes.** In every saved
offset record H_floor=min(H_i,72)<=H_i. The expression
81/44-(3/11)(3/2)^H decreases with H, so the stored value is an
upper bound for the actual tail-2 offset. It is exact at rows 0 and 1.
The row0 fraction and common H_floor=72 fraction printed above are
both strictly negative. All 25 indices occur, including changed row24;
no tail-20 offset has replaced this test.

All 24 records have k=0,...,23, displaced row k+1, and the literal
tail-2 prefix sums of the changed pairs. Their exact reconstructed
formula is (D_k+4J_(k+1))*ell-A_k*u-29, which equals L075 (5)
because T+v=27+2. The empty record has A_0=D_0=0 and is the
minimum 629441541677/50000000000>12.58. The first nonempty
prefix is (A_1,D_1)=(59,69); the final one is
(144318707,162928784), with margin
40328772030610511117/10^12>0. Every intermediate record is
positive as well. For 1<=k<=23 both prefix sums are five below
the d0 values, since they include changed row0 and exclude row24;
the actual saved operands, rather than the d0 margins, are used.
Increasing J and ell>0 cover every j>k from these weakest cases.
The first displacement cannot occur only at position24, because a
permutation agreeing through position23 has its last row forced.
Thus neither the empty prefix nor the last possible displacement is
missing.

**L075 (6)–(7): tuple and both cuts.** L089's b_i are exactly the
nonnegative integers with sum B required by L075, so every
a_i=2+18b_i>=2 and sum a_i=166504460. Its G_i,Q_i,kappa, lower
domain s_k>=540/11, closing equality and own-input non-strict J guard
are identical to (6)–(7), at all 25 occurrences. These are hypotheses
on the proposed tuple, not consequences of the finite certificate.
In particular s_k-kappa>=47, so L075's positive-input product and
tail comparisons apply; neither integrality nor feasibility is assumed.
All actual tails enter its product, with ratio exp(-Lambda). The
negative offset needed for comparison is the tail-2 offset just checked,
not the possibly positive actual large-tail offset.

For any minimum occurrence q among positions 0,...,24, the rotated
input is x_k=s_((q+k) mod 25), with x_25=x_0 and outgoing row
rho(k)=pi((q+k) mod 25), retaining that row's indexed b and a.
The old closing edge occurs at rotated position (24-q) mod 25.
The new closing edge is the original edge (q-1) mod 25 into q.
Each is an original endpoint equation and retains its guard at its
own outgoing input. This also covers q=0 and a tail equal to 2 on
either edge. The domain and full allocation sum are unchanged.

L075 bounds log x_0<27 at this arbitrarily chosen minimum and its
first-displacement argument forces rho to be the identity. Thus its
stronger conclusion applies to any minimum occurrence, not merely to
an existentially selected one. No minimum at indexed row0, height
ordering, unique-minimum assumption or domain condition for an auxiliary
comparison trajectory was inserted. Repeated junction values are
permitted by the hypotheses and handled by the existing argument.

The argument, conclusion and direct mathematical inputs L055,L075,L084
are unchanged; DAG.md and PROOF.md are therefore unchanged for audit
status alone. This canonical audit supersedes their pending-audit
wording for L089. Attempt 032's failed S datum and both d0 witnesses
remain intact. No assembly with C088a, H/seed consequence, actual-word
transfer or all-order exclusion is proved in this step. Other tables,
entry, unrestricted cycles, divergence and universal eventual descent
remain unresolved.

## Mathlib

Full matching coverage for this fixed-table application has not been
checked. L075 and L084 record their coverage qualifications; supporting
finite-sum, logarithm and exponential facts do not constitute a matching
order-rigidity theorem. Unknown coverage is not absence. No Lean
verification is claimed.
