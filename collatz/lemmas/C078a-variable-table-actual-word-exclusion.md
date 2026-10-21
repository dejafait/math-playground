# C078a — Conditional variable-table actual-word exclusion

## Hypotheses

Retain every table and certified data hypothesis of L078, hence all of
C077a's hypotheses on the same table and budget. Explicitly, r>=3,
B,tau>=0 are integers, 2<=J_0<...<J_(r-1) are integers and H_i>=3
are integers. Require all C077a order tests (2) and their preceding
certificate inequalities, its support tests (3) and their preceding
inequalities when B>0, its cutoff tests (4) always, and its cutoff
tests (5) and their preceding inequalities when tau<=B. The three
sets of certificate constants remain independent. In particular cutoff
test (4), which is L077 (3), remains required when tau>B. No test is
inferred from actuality or from a different certificate.

Use L078 (1)–(3) to define the integer totals K,N, the positive integer
Delta=2^N-3^K, the complete chronological integer numerator Phi(t) and
the candidate set

\[
\mathcal S=\{t\in\mathbb Z:0\le t\le B,\ t<\tau\}.
\]

Require its full arithmetic hypothesis L078 (4): Delta does not divide
Phi(t) for every t in S. This is an independent assumption, not a
certificate established here. For an empty S it is vacuous. Justified
divisor/nonzero-residue certificates as specified in L078 suffice;
common zero residues give no conclusion.

Let T(n)=n/2 for even positive integers and T(n)=(3n+1)/2 for odd
positive integers. Letters E and O specify actual input parities for
this shortcut map. Fix indexed nonnegative integers b_i with sum_i b_i=B,
attach a_i=2+18b_i to outgoing row i, and let pi be any permutation
of {0,...,r-1}. The proposed chronological word at position k is

\[
W_{\pi(k)}=(OOEO)^{J_{\pi(k)}}O^{H_{\pi(k)}}E^{a_{\pi(k)}}.
\tag{1}
\]

It is required to be actual in a closed concatenation starting at a
positive integer n_0, with every junction positive, odd and 20 modulo
27, and every final even tail exact. Repeated periods and coincident
junctions are allowed. There is no least-root, first-return,
primitive-period, minimum-location, H-guard, seed or count-ray premise.
All logarithms are natural.

## Conclusion

No such actual closed concatenation exists, for any of these indexed
integer allocations and any cyclic order.

This is a conditional application of an audited arithmetic criterion,
not a new-table certificate or an unconditional exclusion for arbitrary
tables. It is a local REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-10-18-variable-table-actual-word-application.md`,
exactly its COVERED_TARGET. Its separate critical audit below found no defect.
Universal entry, unrestricted cycles, divergence and universal eventual
descent remain unresolved.

## Proof

### Actual chronological inputs and the lower domain

Suppose a concatenation satisfying the hypotheses exists. Write

\[
\ell_k=4J_{\pi(k)}+H_{\pi(k)}+a_{\pi(k)},\quad
v_0=0,\quad v_k=\sum_{h<k}\ell_h,\quad n_k=T^{v_k}(n_0).
\]

Since pi is a permutation and sum_i a_i=2r+18B, v_r is exactly
L078's total N. Closure gives n_r=n_0. At position k the outgoing
pair and tail are precisely those of row pi(k), with input n_k and
output n_(k+1). No row is detached from its allocation or input.

For every k, write n_k=20+27u_k with u_k an integer. Positivity
forces u_k>=0, since u_k<=-1 would give n_k<=-7. Oddness forces
u_k odd, so u_k>=1 and n_k>=47. Put kappa=23/11 and
s_k=n_k+kappa. Consequently

\[
s_k\ge540/11>0\quad(0\le k\le r),\qquad s_r=s_0.
\tag{2}
\]

In particular n_0>1. Chronologically relabeling the parameters by pi
therefore satisfies all L041 actual-language hypotheses: r>=3, J>=2,
H>=3, independent integer tails a>=2 congruent to 2 modulo 18,
positive odd residue-20 junctions, exact tails and closure. Only that
lemma's elementary section “Each occurrence's own prefix and the
transfer to the next” is used. None of its cycle-count estimates or
imported primitive-cycle thresholds is invoked.

### Match every endpoint and own-input guard

Fix any 0<=k<r, abbreviate i=pi(k), J=J_i,H=H_i,a=a_i, and set
y=T^{4J}(n_k), w=T^{4J+H}(n_k). The occurrencewise necessity in
L041, using L031's arbitrary-tail finite identities, gives

\[
y+1=(27/16)^J s_k-12/11,\qquad
2^H(w+1)=3^H(y+1),\qquad w=2^a n_{k+1},
\]
\[
v_2(11n_k+23)=4J+2.
\tag{3}
\]

These are existing actual-word necessities, not an integer-realization
converse. Their hypotheses hold for this particular occurrence, also
at k=r-1 where n_(k+1)=n_r=n_0 is the positive odd closing endpoint,
and when a=2. No estimate requiring a growing varying-tail row is used.

The positive integer 11n_k+23=11s_k is divisible by 2^(4J+2).
It is therefore at least that power. Logarithm monotonicity, with the
positive domain (2), yields exactly the non-strict own-input guard

\[
4J_{\pi(k)}\log2\le\log s_k+\log(11/4).
\tag{4}
\]

Put G_i=(27/16)^{J_i}(3/2)^{H_i} and
Q_i=(12/11)(3/2)^{H_i}+1, as in C077a. Substituting (3) in the
actual endpoint gives w=G_i s_k-Q_i, hence

\[
s_{k+1}=2^{-a_{\pi(k)}}(G_{\pi(k)}s_k-Q_{\pi(k)})+\kappa.
\tag{5}
\]

Both subtractive terms in Q_i remain inside the tail factor. Since k
was arbitrary, (4)–(5) hold at all r occurrences, including the
chronological closing edge s_(r-1) to s_r=s_0. All tails, including
any tail equal to 2, stay attached to their own outgoing rows.

### Apply L078 at the actual indexed row-0 input

The same table, budget, cutoff, independent data certificates and full
survivor nondivisibility assumption are precisely those of L078.
Equations (2), (4) and (5) match all of C077a (6), the real tuple
to which L078 applies. The b_i are the required nonnegative integers
of total B, pi is a permutation, and no additional tuple premise
is missing. The necessary subsystem uses only the lower domain,
exact endpoints and non-strict own-input J guards.

If S is empty, L078 already excludes this feasible tuple by C077a's
necessary survivor conclusion. Otherwise let z be the unique position
with pi(z)=0. L078's audited normalization gives a parameter t in S
and the identity

\[
s_z-\kappa=x_0-\kappa=\frac{\Phi(t)}{\Delta}\notin\mathbb Z.
\tag{6}
\]

Here x_0=s_z is its normalized input of indexed outgoing row 0.
But s_z-kappa=n_z by our definition, and n_z is an actual positive
integer. This contradicts (6). Shifted integrality is neither assumed
nor needed, and z need not be chronological zero or a minimum.

No normalization step is added to L078: its C077a input already
rotates every outgoing row together with its input and allocation,
retaining all equations at both cuts. In its notation the old closing
edge is new edge r-1-z, and the new closing edge is old edge z-1
modulo r ending at z. Thus the tested coordinate is exactly the
actual integer n_z; neither a different cut nor a count-only match
has been substituted. This completes the conditional exclusion.

### Qualifications, boundaries and overlap

At r=3 all three occurrences remain present. At B=0 the only
pre-cutoff parameter is 0; it needs arithmetic coverage if tau>0,
while tau=0 has empty S. At B=1, S is empty for tau=0, is {0}
for tau=1 and is {0,1} for tau>1. Generally tau=1 leaves just 0,
tau=B>0 leaves 0,...,B-1, and tau>B requires arithmetic coverage
of every 0,...,B. Cutoff test C077a (4) remains required in this
last case. If t=B survives, the normalized final tail is 2; its
closing endpoint was never omitted. No empty rejection interval is
interpreted as a survivor-existence assertion.

All indices designate time occurrences. Repetition of a period or
equality of junction values removes no endpoint or guard and does
not affect the unique position carrying indexed row 0. The proof
uses no H guard, seed, minimum-location, distinguished tail,
primitive-count theorem or realization converse.

The precise upstream affine import remains Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The reused assessment inspected its primary statement and essential
printed proof cases. L078 retains the nonempty-word and nonzero-
denominator qualifications; here r>=3 makes the word nonempty and
its data tests imply Lambda>0 and Delta>0. No general affine,
parity-coding or integrality theorem is reproved in this application.

C074b already excludes its fixed table and budget; it is a comparison
precedent, not an additional input or another new exclusion here.
No tests for a new table, survivor arithmetic evaluations or feasible
survivors have been supplied. Both rational witnesses and Attempts
026–031 remain valid: those stops do not assert the independent
nondivisibility premise for arbitrary tables, and a rational endpoint
tuple is not an actual integer concatenation. The conclusion leaves
unrestricted cycles and universal eventual descent open.

### Independent critical audit — 2026-10-18, step 301

The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-18-variable-table-actual-word-critical-audit.md`,
exactly its COVERED_TARGET. This RESEARCH/REPRODUCTION audit found no
defect in the conditional application. It checks an existing local
input, without strengthening the theorem or claiming progress beyond
the inspected sources. The relevant upstream proofs and their audits
are imported; no benchmark or general affine theorem is reproved.

**All independent data premises.** The hypotheses explicitly retain
the complete table and certified data of L078, which retains all of
C077a. The integers r,B,tau,J_i,H_i and their inequalities agree.
C077a (2) and its preceding inequalities are the order tests, including
every negative tail-2 offset and displacement margin. For B>0 its
(3) and preceding inequalities are the support tests, including the
positive residual denominator, all negative tail-20 offsets and all
early-recipient margins. They are omitted only for B=0, as permitted
by C077a. Its (4) includes the positive upper/lower Lambda bounds,
both eta bounds and the uniform-domain inequality, even when tau>B.
Its (5) and preceding incoming-product, sum, cap and logarithm bounds
are required precisely when tau<=B. No independent certificate
constant is identified with one from another test set.

L078 (4) quantifies over exactly the integer set S={0<=t<=B, t<tau}.
C078a retains this entire premise. Actuality does not supply either
the data tests or any divisibility certificate. Since the same table
and budget define K,N and Delta, no denominator from a different
table is used. Positive Lambda from those tests gives Delta>0, as
already audited in L078. The source nonzero-denominator qualification
is therefore justified independently of a proposed actual tuple.

**Chronology and language.** A row has 4J+H+a shortcut letters and
3J+H odd letters. Its cumulative time difference is exactly ell_k,
so the word starting at n_k is its attached outgoing row pi(k).
Summing over the permutation gives
v_r=sum_i(4J_i+H_i)+2r+18B=N. The final output is n_r=n_0.
All a_i=2+18b_i are integers at least 2 and congruent to 2 modulo
18; closure, actual parities, odd residue-20 junctions and exact
tails are hypotheses. For every junction n_k=20+27u_k>0 forces
integer u_k>=0, and oddness forces u_k>=1. Thus n_k>=47 and
s_k=n_k+23/11>=540/11. This includes the final junction and
gives n_0>1. Chronological relabeling therefore satisfies all of
L041's actual-language hypotheses. Neither its later minimum
relabeling nor its count estimates are used in this application:
the finite own-prefix identities hold at each original occurrence.

**Own-input necessity and signs.** L041's inspected own-prefix
passage, supported by L031's finite identities, gives
2^H(w+1)=3^H(y+1), w=2^a n_(k+1), and
16^J(11y+23)=27^J(11n_k+23). These quantities are positive.
Since w+1 is odd, v_2(y+1)=H. For the positive odd integer
u=(y+1)/2^H, the identity
11y+23=4(11*2^(H-2)u+3) has valuation exactly 2 because H>=3.
The last finite identity therefore gives v_2(11n_k+23)=4J+2.
This checks the scope of the imported necessity, including a=2 and
k=r-1 with its actual odd endpoint n_0; it uses no closure converse.

The positive integer 11n_k+23=11s_k is at least 2^(4J+2).
Taking logarithms and subtracting 2 log2 gives exactly
4J log2<=log s_k+log(11/4), with the non-strict sign and the
input of this same outgoing row. The other finite identity yields
w=(3/2)^H((27/16)^J s_k-12/11)-1=G_i s_k-Q_i.
Hence its actual next shifted input is
2^(-a_i)(G_i s_k-Q_i)+23/11. Both negative terms in Q_i
remain inside the tail factor. These are precisely C077a (6) at
every occurrence, including the original closing edge. There is
no growth, H-guard, seed or minimum-location condition in this match.

**Cuts and tested integer.** The actual s tuple, indexed b_i and pi
now satisfy every tuple premise of L078, as well as all its data and
arithmetic premises. Its audited C077a normalization first establishes
literal cyclic order, then chooses the unique z with pi(z)=0.
For rho_i=(z+i) mod r the outgoing row at x_i=s_(rho_i) is i,
and x_r=x_0. When rho_i=r-1, the original output s_r=s_0 is
the next rotated input; all other outputs are s_(rho_i+1).
Consequently the old closing edge is new edge r-1-z, and the new
closing edge starts at old position z-1 modulo r. At z=0 these
cuts coincide; at z=r-1 the old closing edge is the new first edge.
Every remaining z obeys the same formulas. Allocations and own-input
guards move with their outgoing rows. Coincident numerical junctions
do not affect this bijection of time occurrences.

L078 then identifies the normalized unshifted row-0 input with
Phi(t)/Delta for the resulting integer t in S. The coordinate is
x_0-23/11=s_z-23/11=n_z, which is an actual positive integer.
The full arithmetic premise makes that very quotient nonintegral.
This is the claimed contradiction. No shifted integer, different
chronological input or individual nonintegrality of every junction
has been substituted. For empty S, C077a instead already contradicts
feasibility; no quotient evaluation is required.

**Boundary cases and limitations.** At r=3, all three rows and
edges remain, with early index 0 and last pair 1,2. At B=0 only
t=0 is a pre-cutoff candidate; it requires arithmetic if tau>0
and is rejected before arithmetic if tau=0. At B=1 the survivor
sets for tau=0,1,>1 are respectively empty, {0}, {0,1}.
Generally tau=1 permits only 0, tau=B>0 permits 0,...,B-1,
and tau>B permits all 0,...,B while still requiring C077a (4).
At tau=B=0 the set is empty. If t=B survives, its last tail is
2 and the last endpoint and total length retain it. None of these
necessary-set descriptions asserts feasible guards or simultaneous
satisfiability of every data test. Repeated periods and equal
junctions remove no edge. No primitive-count theorem is invoked.

The precise upstream primary citation remains Halbeisen–Hungerbuehler
(1997), section 2 equations (2)–(4), Lemma 2, pp. 228–229, linked
above. The inspected source record and ready assessment cover its
formal affine use; nonempty words and positive denominators are
retained. L041 and L078 are exactly the direct inputs, as in the
unchanged DAG. C077a/L077 and L031 remain upstream, and C074b is
only a fixed-table precedent. Histories 290–300 contain the construction
and scope review but no earlier completed C078a critical audit.

Attempts 026–031 and both rational witnesses are unaffected. An
independent nondivisibility assumption does not prove the stopped
uniform-prime tests, and a rational witness is not an actual integer
concatenation. This audit provides no new-table tests, survivor
arithmetic or unconditional exclusion. Universal eventual descent
remains unresolved; this is not a complete Collatz candidate.

## Mathlib

Full matching theorem coverage is **not checked**. Finite indexing,
affine identities, dyadic divisibility and logarithm monotonicity would
be supporting facts, not a matching theorem for this conditional
variable-table application. No absence claim or formal verification
is made.
