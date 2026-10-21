# C080b — Redistributed-H all-order allocation actual-word exclusion

## Hypotheses

Use L055's complete indexed pairs (J_i,H_i), 0<=i<=24, replacing
only H_0=40 by 39 and H_24=32670621 by 32670622, exactly as in
L079. Fix indexed nonnegative integers b_i with
sum_i b_i=B=9250245 and attach a_i=2+18b_i to outgoing row i.
Let pi be any permutation of {0,...,24}.

For the shortcut map T(n)=n/2 at even positive integers and
T(n)=(3n+1)/2 at odd positive integers, letters E and O specify
actual input parities. Suppose the chronological words

\[
W_{\pi(k)}=(OOEO)^{J_{\pi(k)}}O^{H_{\pi(k)}}E^{a_{\pi(k)}}
\quad(0\le k<25)
\]

form an actual closed concatenation starting at a positive integer.
Require every junction to be positive, odd and 20 modulo 27, and
every final even tail to be exact. Each pair and allocation stays
attached to its own outgoing row. Repeated periods and coincident
junctions are allowed. There is no minimum-location, least-root,
first-return, H-guard, seed or primitive/count-ray premise.

## Conclusion

No such actual closed concatenation exists, in any cyclic order over
this full integer allocation simplex.

This is a local RESEARCH/REPRODUCTION specialization of audited C078a
under the prior SPECIALIZE assessment
`drafts/literature/2026-10-18-redistributed-h-actual-word-application.md`.
It gives a restricted actual-cycle exclusion for this explicit changed
table, without a claim of progress beyond the inspected general machinery.
The separate critical audit below found no defect. Real survivor feasibility, other
tables, universal entry, unrestricted cycles, divergence and universal
eventual descent remain unresolved. Both original rational witnesses
and Attempts 026–031 remain valid.

## Proof

Apply C078a with r=25, B=9250245 and tau=2. The explicit L055
data have strictly increasing integer J_i, starting with J_0=8>=2.
After exactly the two stated replacements, every H_i is an integer
at least 39, hence at least 3. Thus the basic table domains match.
We use L055 only for its explicit pair data, not its original-table
feasible witness or any additional real-system guard.

L079's audited conclusion supplies every C077a data test retained
by C078a on precisely this changed table and budget. These comprise
all order tests and preceding certificate inequalities; all support
tests and preceding inequalities, mandatory since B>0; the unconditional
cutoff tests; and all cutoff boundary tests and preceding inequalities,
mandatory since tau<=B. In particular the positive-Lambda bounds,
negative tail-2 offsets, first-displacement margins, residual support
cap, early tail-20 offsets, next-input margins, both eta bounds,
uniform-domain bound, every incoming-prefix bound, complete inverse-prefix
sum and strict boundary margin are supplied. The O, S and C constants
remain independent choices. No test is inferred merely from actuality
or from the unchanged total H.

The same table and budget give K=397573379, N=630138897 and
Lambda=N log2-K log3>0, as certified in L079. Consequently the
integer denominator Delta=2^N-3^K in C078a, using L078's definitions,
is positive and nonzero. The words are finite and nonempty.

The entire independent arithmetic premise of C078a is

\[
\Delta\nmid\Phi(t)\quad
\text{for every }t\in\mathbb Z\text{ with }0\le t\le9250245,
\ t<2.
\]

This parameter set is exactly {0,1}. At both parameters L078 uses
literal order and b_i=0 for i<=22, b_23=t, b_24=B-t. L080 uses
exactly these allocations, the same changed pairs and the same complete
chronological numerator and denominator at the normalized unshifted
row-0 cut. Its audited conclusion proves Delta does not divide Phi(t)
for both candidates. Invoke that conclusion directly; no new modular
calculation is required. In particular modulus 25 is not being asserted
to divide Delta. The closing tail is included in L080's numerator and
denominator definitions at both parameters.

Finally, the proposed words and allocations in the hypotheses are
exactly C078a's actual language: 25 occurrences, the same indexed
nonnegative integer allocation of total B, attached tails 2+18b_i,
an arbitrary permutation, actual closure, positive odd residue-20
junctions and exact tails. Hence every premise of C078a is satisfied.
Its audited occurrencewise necessity supplies all lower-domain inputs,
exact shifted endpoints and non-strict own-input J guards, including
the closing edge and any tail equal to 2. No necessity theorem is
reproved or strengthened in this specialization.

For clarity about the contradicted integer, write n_k for the actual
junction at chronological position k and s_k=n_k+23/11. Let z be
the unique position with pi(z)=0. C078a's normalization carries each
outgoing row with its own input and allocation. The old closing edge
becomes edge 24-z, and the new closing edge is old edge z-1 modulo
25; when z=0 the cuts coincide. Every endpoint and guard is retained.
Its conclusion tests precisely

\[
n_z=s_z-23/11=\Phi(t)/\Delta\notin\mathbb Z
\]

for the resulting t in {0,1}. But n_z is an actual positive integer.
This is the contradiction given by C078a. No chronological-zero or
minimum assumption, shifted integrality, assertion of individual
nonintegrality at every junction, or realization converse is used.
Repetitions and coincident junctions remain indexed time occurrences.

C080a is the already audited table-level conjunction of the same
certificates, a comparison rather than an additional mathematical input
to this direct C078a application. It did not assert the actual-word
consequence proved here. C074b concerns the original pair table and
does not substitute for any changed-table certificate.

The upstream formal affine import is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The ready assessment reuses the inspected primary hypotheses and
essential printed proof cases. C078a and L080 already specialize this
finite-word identity with the nonempty-word and nonzero-denominator
qualifications verified above. A reproof would add no necessary step.
No new source claim or additional arithmetic is imported here.

The original-table rational witnesses and failed arithmetic diagnostics
are unaffected: their data differ, and rational feasibility does not
give an actual integer concatenation. This exclusion supplies no
unrestricted cycle bound, entry theorem or eventual-descent argument.

### Independent critical audit — 2026-10-18, step 317

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-18-redistributed-h-actual-word-critical-audit.md`.
This RESEARCH/REPRODUCTION audit found no defect in the stated
specialization. It verifies an existing restricted input, not a new
general theorem or progress beyond the inspected source machinery.
The audited C078a bridge and L079/L080 certificates are reused;
their arithmetic is not rerun in the absence of a mismatch.

**Table and independent data premises.** The complete displayed L055
table has strictly increasing J entries from 8 to 30998279. Replacing
only H_0=40 by 39 and H_24=32670621 by 32670622 gives exactly
the table in both L079 and L080; all H entries are at least 39.
The integers r=25, B=9250245 and tau=2 satisfy the C078a domains.
Since B>0 and tau<=B, both the support package and the cutoff
boundary package are mandatory. Comparing C078a's retained C077a
premises directly with L079 gives the following complete match.

| Required premise | Audited L079 evidence |
| --- | --- |
| Order positive Lambda lower bound, minimum cap and log enclosures | (3)–(6), lambda^O=lambda_-, T^O=27, ell^O=ell, u^O=u, v^O=2 |
| Every negative tail-2 offset and order margin | (7) and all 24 changed-prefix M_k^O, k=0,...,23; minimum >12.58 |
| Support residual positivity, root cap and log enclosures | (3)–(5), (8), E=552/(4*2^60-23)<lambda_-, U^S=20000000000, T^S=24, v^S=v |
| Every early tail-20 offset and next-input margin | (9) and all 23 M_j^S, j=0,...,22; minimum >9.72 |
| Unconditional cutoff Lambda, eta and domain tests | (4), eta_0>2, eta_24>=eta_0 and (10), with e^C=2 |
| Positive incoming-prefix bounds and the full inverse-prefix sum | (11), L_0^C=1, L_i^C=10^8*2^(i-1) for i=1,...,24, Q^C=kappa*(1+2/10^8) |
| Cutoff boundary cap, log bounds and final-row margin | (3)–(5), (12)–(13), T^C=24, v^C=v; margin <-4.20 |

The O, S and C choices remain independent. In particular v^O=2
is not substituted for v^S or v^C. The boundary allocation uses
row-23 tail 38; it is a test at tau=2, not one of the arithmetic
survivors. Its 25 incoming prefixes include the empty prefix and
input 24. Row 24 is absent only from those incoming prefixes; its
tail remains in the full product and closing endpoint. These tests
are certified data, not consequences of the proposed actual orbit.
The unchanged total H does not replace any changed-prefix test.

**Complete survivor premise and coordinate.** L079 supplies exactly
K=397573379, N=630138897 and 0<10584/10^14<Lambda. Thus
Delta=2^N-3^K is positive and nonzero before any fixed-point use.
All exponents describe finite nonempty words. The entire C078a
candidate set is {t integer: 0<=t<=9250245, t<2}={0,1}.
L080 uses precisely the same changed pairs, literal order and L078
definitions F_i, T_i(t), U_i and Phi(t), at the unshifted row-0 cut.
Its two tail pairs are (2,166504412) and (20,166504394), with all
earlier tails 2; the last tail is included in d_24 and N.

L080's audited direct conclusions Delta not dividing Phi(0) and
Delta not dividing Phi(1) therefore cover every candidate. Its residues
(16,5) and (7,5) modulo 25 give numerator valuation zero and
denominator valuation one at 5, as proved in that input. C080b
correctly invokes nondivisibility, without treating 25 as a divisor
of Delta, using a nonunit inverse or transferring an old numerator.
Neither this arithmetic nor C078a requires feasible survivors.

**Occurrencewise actual language.** For any hypothesized concatenation,
the indexed b_i are nonnegative integers of sum B, and each attached
tail a_i=2+18b_i is at least 2 and is 2 modulo 18. The map,
letter parities, word lengths, permutation, closure, exact tails and
positive odd residue-20 junctions are exactly C078a's hypotheses.
Writing the chronological input as n_k and s_k=n_k+23/11,
that audited bridge supplies s_k>=540/11 and, for i=pi(k),

\[
s_{k+1}=2^{-a_i}(G_i s_k-Q_i)+23/11,
\qquad 4J_i\log2\le\log s_k+\log(11/4).
\]

These are the same endpoint and non-strict own-input guard used in
the data criterion. Both terms of Q_i remain inside the tail factor.
The bridge applies at every occurrence, including k=24 with output
n_25=n_0 and any outgoing tail equal to 2. Its lower domain comes
from n_k>=47. No H guard, seed, cycle-count theorem or minimum
location is needed to obtain these necessities.

**Both cuts and the contradiction.** C078a, through L078, first obtains
literal cyclic order. Only then does the unique position z with
pi(z)=0 give pi((z+i) mod25)=i. Set x_i=s_((z+i) mod25)
for i<25 and x_25=x_0. Every rotated edge has the same outgoing
row, allocation and own input; when its old index is 24, its output
is s_25=s_0, which is the next rotated input. Thus the old closing
edge is new edge 24-z, while the new closing edge is old edge
(z-1) mod25. This includes z=0, when the cuts coincide, and z=24,
when the old closing edge becomes the first edge. No endpoint is lost.

For the resulting t in {0,1}, the cited normalized identity is
x_0-23/11=s_z-23/11=Phi(t)/Delta. The left side is exactly the
actual positive integer n_z. The right side is nonintegral by the
complete survivor premise. This is a contradiction at the same cut,
without shifted integrality, a chronological-zero or minimum-location
assumption, or nonintegrality at every individual junction. Repeated periods and
coincident values remain separate indexed time occurrences throughout.

**Scope, source and dependency check.** The direct mathematical inputs
remain L055's explicit data, C078a's conditional actual-word theorem,
L079's data tests and L080's two arithmetic conclusions, as in the
existing DAG. C080a is a checked comparison, not an additional input;
its theorem concerns real junctions and does not replace this actual-word
application. The precise Halbeisen–Hungerbuehler citation above is reused
with its finite nonempty-word and nonzero-denominator qualifications.
No general theorem is reproved and full matching Mathlib coverage remains
unchecked. Focused histories 313–316 record construction and audit-scope
approval, with no previous completed C080b audit.

Both original rational witnesses and Attempts 026–031 remain valid.
This audit establishes no survivor feasibility, other-table exclusion,
entry theorem, arbitrary-cycle control, divergence bound or universal
eventual descent. No argument or direct input changes, so PROOF.md and
DAG.md remain unchanged; this canonical audit supersedes the overview's
pending-audit wording for C080b.

## Mathlib

Full matching Mathlib coverage is **not checked**. Supporting affine,
finite-indexing, divisibility and logarithm facts do not constitute a
matching theorem for this changed table and actual language. No formal
verification or absence claim is made.
