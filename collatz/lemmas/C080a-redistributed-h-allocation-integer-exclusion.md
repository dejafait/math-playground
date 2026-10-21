# C080a — Redistributed-H all-order allocation integer exclusion

## Hypotheses

Use L055's indexed pairs (J_i,H_i), 0<=i<=24, replacing only
H_0=40 by 39 and H_24=32670621 by 32670622, exactly as in L079.
Let b_i>=0 be integers with sum b_i=B=9250245 and attach
a_i=2+18b_i to indexed row i. Let pi be any permutation of
{0,...,24}. Put kappa=23/11 and

\[
G_i=(27/16)^{J_i}(3/2)^{H_i},\qquad
Q_i=(12/11)(3/2)^{H_i}+1.
\]

Require real s_0,...,s_25 with s_25=s_0, s_k>=540/11 and,
for every 0<=k<=24,

\[
s_{k+1}=2^{-a_{\pi(k)}}(G_{\pi(k)}s_k-Q_{\pi(k)})+\kappa,
\qquad
4J_{\pi(k)}\log2\le\log s_k+\log(11/4).
\tag{1}
\]

Logarithms are natural. Each outgoing row retains its indexed pair,
allocation and own input. These are only endpoint/domain/non-strict J
conditions; no H guard, seed, minimum location, actual-word, parity,
residue, exact-valuation or primitive/count-ray premise is imposed.

## Conclusion

No tuple satisfying (1) has all unshifted junctions s_k-kappa integral.
More precisely, let z be the unique position with pi(z)=0. Every such
tuple has s_z-kappa nonintegral. This does not assert nonintegrality
at every junction or at a predetermined chronological position zero.

This is a local RESEARCH/REPRODUCTION application under
`drafts/literature/2026-10-18-redistributed-h-integer-exclusion-assembly.md`.
It assembles audited inputs, without claiming progress beyond the checked
general affine/divisibility machinery. The separate critical audit below
found no defect in this restricted assembly.
It asserts neither existence nor infeasibility of the real survivors.
Actual-word transfer, other tables, entry, unrestricted cycles, divergence
and universal eventual descent remain unresolved. Both original-table
rational witnesses and Attempts 026–031 remain valid.

## Proof

Apply L078 with r=25, B=9250245 and tau=2. L079 certifies every
independent C077a data test required by L078 on precisely this changed
table: all order tests, all support tests (mandatory since B>0), and
both the unconditional cutoff package and its boundary package
(mandatory since tau<=B). In particular the increasing integer J_i>=2,
integer H_i>=3, positive-Lambda bounds, all negative tail-2 offsets,
all order margins, residual support cap, all early tail-20 offsets and
next-input margins, both endpoint eta bounds, uniform-domain bound,
every incoming-prefix bound, complete inverse-prefix sum and strict
boundary margin are supplied by L079. Its O, S and C certificates
are retained as independent choices. No test is inferred from another
test or from the unchanged total H alone.

The definitions G_i,Q_i, the arbitrary permutation, attached integer
allocations and their total B, lower domain, closure and every own-input
non-strict guard in (1) are exactly C077a (6), as required by L078.
L079's table has K=397573379, N=630138897 and Lambda>0. Thus
L078's Delta=2^N-3^K is a positive nonzero integer, with exactly
the definitions used by L080.

The entire arithmetic hypothesis of L078 ranges over

\[
\{t\in\mathbb Z:0\le t\le9250245,\ t<2\}=\{0,1\}.
\]

For both parameters, its test allocation is b_i=0 for i<=22,
b_23=t, b_24=B-t. These are precisely L080's allocations, with the
same changed pairs, literal chronology, complete weights and closing
tails. L080 proves Delta does not divide Phi(t) for each of these
two parameters. Hence every candidate in L078's arithmetic hypothesis
is covered. We invoke that nondivisibility conclusion directly;
modulus 25 is not asserted to divide Delta. In particular no new
residue calculation, modular division or cancellation theorem is needed.
The affine input underlying L078 and L080 is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Its formal finite-word fixed-point identity is already specialized and
audited in those inputs; reproving it would add no step here.

L078 now applies. To make its tested coordinate explicit, its order
reduction first makes pi cyclically literal; only then normalize at
the unique z carrying indexed row 0. Write x_i=s_((z+i) mod25)
for 0<=i<25 and x_25=x_0. The old closing edge is new edge 24-z;
the new closing edge is old edge z-1 modulo 25. Thus both cuts,
all attached tails and every own-input guard remain present, including
when a closing tail is 2. Repeated junction values cause no change
to these indexed time occurrences. The normalized allocation has one
of the two tested parameters, and L078 gives at this same cut

\[
s_z-\kappa=x_0-\kappa=\Phi(t)/\Delta\notin\mathbb Z.
\]

If all original unshifted junctions were integers, s_z-kappa would
be an integer, a contradiction. This uses unshifted integrality only;
no location of a minimum, survivor feasibility or integer-realization
converse has been assumed. L055 supplies only the explicit pair data;
its original-table witness and the old prime-cancellation failures are
not transferred to this changed table. This completes the stated
table-level exclusion and no actual-word application.

### Independent critical audit — 2026-10-18, step 313

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-18-redistributed-h-integer-exclusion-critical-audit.md`.
This RESEARCH/REPRODUCTION audit found no defect. It independently checks
the conjunction and its quantifiers, using the already audited L078,
L079 and L080 conclusions. It does not rerun their arithmetic, reprove
the primary affine theorem cited above, or establish a new general result.
The source's finite nonempty-word and nonzero-denominator qualifications
remain those verified in L078 and L080. Full matching Mathlib coverage
remains unchecked.

**Exact table and all data hypotheses.** L055's displayed J entries are
strictly increasing from 8 to 30998279. Only its H entries at indices
0 and 24 change, from 40 and 32670621 to 39 and 32670622. Thus the
specified table is exactly L079's, with every H at least 39. The integer
parameters r=25, B=9250245 and tau=2 match L078 through C077a; support
and cutoff boundary tests are both mandatory. The following matches
every test family to the audited L079 evidence, rather than assuming
that unchanged totals imply unchanged prefixes. Equation numbers in the
right column are L079's.

| Required C077a data, retained by L078 | Matching L079 certificate |
| --- | --- |
| Positive order lower bound, minimum cap and logarithm enclosures | (3)–(6), with lambda^O=lambda_-, T^O=27, ell^O=ell, u^O=u and v^O=2 |
| Every negative tail-2 offset and all r-1 order margins | (7) and all 24 M_k^O in the changed-prefix table, including k=0 and 23; minimum >12.58 |
| E<lambda^S<=Lambda, residual cap and support log bounds | (3)–(5), (8), with E=552/(4*2^60-23), U^S=20000000000, T^S=24 and v^S=v |
| Every early tail-20 offset and next-input margin | (9) and all 23 M_j^S, j=0,...,22; minimum >9.72 |
| Both positive Lambda bounds below 1, both endpoint eta bounds and uniform domain test | (4), eta_0>2, eta_24>=eta_0 and (10), with e^C=2 |
| Every incoming-prefix lower bound at tau, positive constants and complete inverse-prefix sum | (11), L_0^C=1, L_i^C=10^8*2^(i-1) for 1<=i<=24 and Q^C=kappa*(1+2/10^8) |
| Boundary cap, log enclosures and strict final-row margin | (3)–(5), (12)–(13), T^C=24, v^C=v and margin <-4.20 |

These are independent permitted choices. In particular the order v=2
is not substituted for the sharper support/cutoff v. L079's step-305
audit covers all numerical comparisons, including the changed multiplier
3^63/2^73, endpoint eta_24, row-23 tail 38 at the cutoff boundary and
all 25 incoming terms. The last row is correctly absent from incoming
prefixes but present in Lambda and closure. C080a needs the conclusion
that these data tests hold, not the existence of a feasible test tuple.
No certificate family is omitted or deduced from the common total H.

**Quantified subsystem and the two cuts.** C080a (1) is precisely
C077a (6): G,Q,kappa agree; pi ranges over every permutation; each
nonnegative integer allocation remains attached to its outgoing row;
the sum is B; every input has the same lower domain, exact endpoint
and non-strict own-input J guard. The closing equation is included for
k=24. No H guard, seed or minimum premise is needed. Coincident real
values do not affect the distinct indexed positions of a permutation.

L078 first obtains cyclic literal order from C077a. Only then does
pi(z)=0 imply pi((z+i) mod25)=i. For each new edge i, its old input
index is k=(z+i) mod25. If k<24, its old output is s_(k+1);
if k=24, it is s_25=s_0. Both equal the new x_(i+1), using
x_25=x_0. The guard uses that same x_i and the same outgoing row i.
Solving k=24 gives the old closing edge's new index 24-z; setting
i=24 gives the new closing edge's old index (z-1) mod25. For z=0
the cuts coincide; for z=24 the old closing edge is new edge zero.
Thus the displayed indices cover the extremes as well as interior cuts.
Tails, including a possible tail 2, and all allocations are unchanged.

**Exhaustion and arithmetic match.** C077a, through L078, forces
b_0=...=b_22=0. Since b_23 is an integer and b_23+b_24=B,
its remaining parameter is t=b_23 in [0,B]. The cutoff t<2 leaves
exactly 0 and 1 as necessary candidates; neither is asserted feasible.
Both are within the closed interval, so no empty-range convention is
used. Their tails are precisely L080's: respectively (a_23,a_24)
=(2,166504412) and (20,166504394), with all earlier tails 2.

L079's totals K=397573379 and N=630138897 are exactly L078 (1)
and L080's totals, and Lambda>0 supplies positive nonzero Delta.
L080 uses L078's full F_i, T_i(t), U_i and Phi(t), on the same changed
table and literal order, rather than just the same totals. Its audited
conclusion supplies Delta not dividing Phi(t) for each candidate.
The residues (16,5) and (7,5) modulo 25 have numerator valuation zero
and denominator valuation one at 5, as already proved there. Hence
C080a correctly invokes direct nondivisibility, not L078's optional
certificate with the invalid proposed divisor 25. No modular inversion
or residue from the original table is used.

L078's conclusion tests x_0-kappa=Phi(t)/Delta at indexed row 0.
The rotation above gives x_0=s_z, so the nonintegral input is precisely
s_z-kappa. All-unshifted-integral junctions would include this input,
which is the claimed contradiction. It need not be the chronologically
first input or a minimum. Neither shifted integrality nor individual
nonintegrality of every junction has entered. The affine test-root
identity needs no feasible-survivor premise or realization converse.

**Scope and preserved results.** The direct inputs remain L055 for explicit
pairs, L078 for the criterion, L079 for every data test and L080 for
both arithmetic conclusions, exactly the existing DAG row. C077a's
package is used through those inputs. The assembly proves neither
survivor feasibility nor an actual-word consequence; no primitive count
or H/seed constraint is introduced. Both original rational witnesses and
Attempts 026–031 remain in their original scopes. This audit verifies a
relevant existing local input, not progress beyond the checked sources
or a resolution of universal eventual descent. Neither the argument nor
its direct mathematical inputs change, so PROOF.md and DAG.md are unchanged; this
canonical audit supersedes the overview's pending-audit wording.

## Mathlib

Full matching Mathlib coverage for this changed-table assembly is not
checked. The supporting affine and divisibility coverage recorded in
L078 and L080 is reused; no Lean verification or absence claim is made.
