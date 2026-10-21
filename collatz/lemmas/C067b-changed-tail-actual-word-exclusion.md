# C067b — Changed-tail actual-word exclusion

## Hypotheses

Let T(t)=t/2 for even positive integers and T(t)=(3t+1)/2 for odd
positive integers. O and E denote these branches with actual odd and
even input parities, respectively. Use the complete indexed J_j,H_j
table in L055's section “Explicit allocation and exact counts”, with
attached tails

\[
a_{23}=20,\qquad a_{24}=166504394,\qquad a_j=2\ (0\le j\le22).
\]

Let sigma be any permutation of {0,...,24}, interpreted cyclically.
At position k use the intact outgoing word

\[
W_k=(OOEO)^{J_{\sigma(k)}}O^{H_{\sigma(k)}}E^{a_{\sigma(k)}},
\qquad D_k=4J_{\sigma(k)}+H_{\sigma(k)}+a_{\sigma(k)}.
\]

Assume W_0...W_24 is actual at a positive integer n_0 and is closed:
with n_k=T^{D_0+\cdots+D_{k-1}}(n_0), one has n_25=n_0.
Every designated junction n_k, 0<=k<25, is positive, odd and
congruent to 20 modulo 27. Every final tail is exact. Repeated
representations and coincident junctions are allowed; no primitive-period,
least-root, first-return or relative-height assumption is imposed.

## Conclusion

No such actual closed concatenation exists, in any cyclic order of these
intact changed-tail rows.

This is a local RESEARCH/REPRODUCTION specialization under the prior
SPECIALIZE assessment
`drafts/literature/2026-10-14-changed-tail-actual-word-exclusion.md`.
It applies audited C067a using existing elementary wordwise necessity;
it claims no advance beyond the inspected source machinery. The separate
critical audit below found no defect within these hypotheses. Other allocations, unrestricted cycles,
entry, divergence and universal eventual descent remain unresolved.

## Proof

Suppose such a concatenation exists. The least positive odd integer
20 modulo 27 is 47: positive integers in that class are 20+27q,
q>=0, and oddness makes q odd and hence q>=1. Thus every n_k>=47.
Define s_k=n_k+23/11, including s_25=s_0. Then

\[
s_k\ge47+23/11=540/11,\qquad n_k=s_k-23/11\in\mathbb Z.
\tag{1}
\]

Every row of L055's complete table has J_j>=2 and H_j>=3. The
attached tails satisfy a_j>=2 and a_j=2 modulo 18, since
20=2+18 and 166504394=2+18*9250244. The parameters and actual
language therefore meet L041's hypotheses at r=25, retaining both
changed tails. In particular, its elementary section “Each occurrence's
own prefix and the transfer to the next” applies at each outgoing word.
Only that section's exact endpoint and J necessity are used here.

Fix any position k and abbreviate J=J_sigma(k), H=H_sigma(k),
a=a_sigma(k), n=n_k, m=n_(k+1) and s=s_k. Put
y=T^(4J)(n) and z=T^(4J+H)(n). The imported actual-word identities
from that L041 section give

\[
y+1=(27/16)^J s-12/11,\qquad
2^H(z+1)=3^H(y+1),\qquad z=2^a m.
\tag{2}
\]

Its necessity argument, justified upstream in L031's “Exact boundary
valuations, without assuming E^2 transport”, gives
v_2(11n+23)=4J+2. Applicability retains an odd actual endpoint m,
a>=2 and H>=3; it does not require a=2. Explicitly, z is even,
so (2) gives v_2(y+1)=H. Writing y+1=2^H u with u positive odd,
11y+23=4(11*2^(H-2)u+3) has valuation 2. L041's imported
identity 16^J(11y+23)=27^J(11n+23) yields the stated input
valuation. Positivity then implies 11n+23>=2^(4J+2), hence

\[
4J\log2\le\log s+\log(11/4).
\tag{3}
\]

The sign in (3) is non-strict, exactly as in C067a. Its J parameter
belongs to the outgoing row at input n_k, rather than an incoming row
or a differently selected junction.

Also (2) gives z=(3/2)^H(y+1)-1. Substitution and division by the
actual 2^a, followed by adding 23/11, give

\[
s_{k+1}=2^{-a_{\sigma(k)}}\left\{
(27/16)^{J_{\sigma(k)}}(3/2)^{H_{\sigma(k)}}s_k
-\frac{12}{11}(3/2)^{H_{\sigma(k)}}-1\right\}+\frac{23}{11}.
\tag{4}
\]

This includes both shifts and the exact attached tail. At k=24 the
output is s_25=s_0, so the closing edge is included. Equations
(3)–(4) hold at every position, without a rotation or minimum choice.

For completeness, the fixed totals in C067a also match. L055 gives
sum J_j=66061058 and sum H_j=199390205. Relative to its original
tails, the present tails add eighteen at row 23 and subtract eighteen
at row 24, so sum a_j=166504460 is unchanged. Thus

\[
K=3\sum J_j+\sum H_j=397573379,\qquad
N=4\sum J_j+\sum H_j+\sum a_j=630138897.
\]

These sums are invariant under sigma; no cycle-count inequality is
required. The tuple therefore satisfies precisely C067a's allocation,
domain, closure, all endpoints, all own-input J guards and integrality
of all unshifted junctions. Audited C067a excludes it, a contradiction.

The specialization checks applicability of existing wordwise identities;
it does not reprove general affine coding. The primary affine input
underlying the inspected local arguments is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The ready assessment already records the primary statement and proof-case
inspection; no new source retrieval or parity-realization converse is
needed because the words here are assumed actual.

No H guard, seed, global minimum, primitive count, Rhin estimate or
published computational cycle cutoff enters this application. Their
qualifications remain on the broader L041/L051 background results.
Every use is at a time occurrence, so repeated periods and coincident
junctions change no premise. Both rational witnesses remain valid and
Attempts 027–031 retain their distinct old-allocation stops. The conclusion
excludes exactly this fixed allocation; it supplies neither an exclusion
of other 25-word allocations nor universal eventual descent.

### Independent critical audit — 2026-10-14

The approved RESEARCH/REPRODUCTION audit under
`drafts/literature/2026-10-14-changed-tail-actual-word-critical-audit.md`
found no defect. This is independent verification of the existing
applicability conjunction, not a new exclusion or a stronger result.
Audited C067a is reused without reopening its upstream numerical proofs.

**Allocation and domain.** The complete L055 table has 25 rows, each
with J>=2 and H>=3 (its smallest entries are J=8 and H=40).
The changed tails are attached to row labels, so a permutation preserves
each outgoing triple. There are 23 tails equal to 2, one equal to 20
and one equal to 166504394. Both exceptional tails are 2 modulo 18:
20=2+18 and 166504394=2+18*9250244. Thus every tail is at least 2,
and their sum is 46+20+166504394=166504460. The imported table sums
give 3*66061058+199390205=397573379 and
4*66061058+199390205+166504460=630138897, exactly C067a's K,N.
No numerical cycle lower bound is needed to identify these counts.

For each actual boundary, n_k=20+27q_k>0 forces the integer q_k>=0;
oddness makes q_k odd, hence q_k>=1. Thus n_k>=47, n_k is integral,
and s_k=n_k+23/11>=540/11. Closure supplies the same statements at
k=25 because n_25=n_0. In particular L041's n_0>1 requirement is
met. Actuality, the odd residue-20 junctions and exact tails meet its
remaining language hypotheses at r=25 without any primitive assumption.

**Arbitrary-tail necessity and guard sign.** Fix an arbitrary position,
including position 24, and retain that position's outgoing J,H,a.
L041's elementary wordwise identities, checked against L031's
arbitrary-tail passage, use y=T^(4J)(n), z=T^(4J+H)(n),
z=2^a m and 2^H(z+1)=3^H(y+1). Since a>=2 and m is a positive
integer, z is even and z+1 odd. Taking dyadic valuations therefore
gives v_2(y+1)=H; it does not require an E^2 tail. With
y+1=2^H u, u positive odd, H>=3 makes 11*2^(H-2)u even, so
11*2^(H-2)u+3 is odd. Consequently v_2(11y+23)=2.
The identity 16^J(11y+23)=27^J(11n+23) now gives
v_2(11n+23)=4J+2. Positivity yields
11s=11n+23>=2^(4J+2). Its logarithm is exactly
4J log2<=log s+log(11/4), with equality allowed. This checks the
guard at the outgoing input, with no shift of its index and no
assumption about that input being the minimum.

**Every endpoint and the closing edge.** Substituting the imported
y+1=(27/16)^J s-12/11 into z=(3/2)^H(y+1)-1 gives
z=(27/16)^J(3/2)^H s-(12/11)(3/2)^H-1.
Thus s_next=z/2^a+23/11 is exactly C067a (1), with the negative
12/11 term inside the division and the positive 23/11 shift outside.
For each 0<=k<24 the actual endpoint is n_(k+1). For k=24 it is
n_25=n_0, so this same calculation verifies the last equation with
s_25=s_0. No edge is lost at the cut. Row 23 keeps tail 20 and row
24 keeps tail 166504394 wherever sigma places them.

All original unshifted junctions s_k-23/11 are integers, rather than
only one selected junction. This is precisely the integrality premise
needed by C067a after its internal cyclic normalization. Its remaining
premises are the matched table, attached tails, counts, lower domain,
endpoints and non-strict J guards. C067a therefore gives the stated
contradiction for every sigma. Repeated periods or coincident junctions
do not change this argument: equations and guards are checked by time
position, and no distinct-value or primitive-period inference is used.

**Scope and limits.** L055 supplies the table, L041 supplies elementary
wordwise necessity, and audited C067a gives the contradiction. L031
is inspected upstream justification already contained in L041, not an
extra two-word closure premise. Neither H guards, a seed, a count ray,
global-minimum bounds nor computational cycle cutoffs enter. The precise
affine citation above is reused; the audit needs no general coding
reproof or parity-realization converse because the words are actual by
hypothesis. Attempts 027–031 concern different old-allocation diagnostics
and remain valid, as do both rational witnesses. No other allocation,
unrestricted cycle, entry or divergence conclusion follows. The proof
and its direct inputs needed no correction, so PROOF.md and DAG.md
remain unchanged. Full matching Mathlib coverage remains unchecked.

## Mathlib

Full matching Mathlib coverage and Lean builds for this actual-word
application were not checked. C067a records supporting valuation and
rational-reduction declarations in the pinned
[Mathlib PadicVal.Basic, commit 2da3ab0a20dc0c66f56a557e37df39f7d36cb953](https://github.com/leanprover-community/mathlib4/blob/2da3ab0a20dc0c66f56a557e37df39f7d36cb953/Mathlib/NumberTheory/Padics/PadicVal/Basic.lean).
Those supporting declarations do not constitute a full matching theorem
for this table, language or applicability conjunction. Unknown full
coverage is not evidence of absence.
