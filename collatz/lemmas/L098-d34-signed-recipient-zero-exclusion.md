# L098 — Literal d34 recipient-zero exclusion with the signed offset

## Hypotheses

Take L055's 25 indexed pairs, changing only H_0=6 and H_24=32670655.
Every J is unchanged; in particular J_0=8,J_1=15. Let b_i be
nonnegative integers with sum b_i=B=9250245 and put a_i=2+18b_i.
Use literal indexed order. Define

\[
\kappa=23/11,\quad G_i=(27/16)^{J_i}(3/2)^{H_i},\quad
Q_i=(12/11)(3/2)^{H_i}+1.
\]

Suppose real s_0,...,s_25 satisfy s_25=s_0, s_i>=540/11 and,
for every 0<=i<25,

\[
s_{i+1}=2^{-a_i}(G_i s_i-Q_i)+\kappa,\qquad
4J_i\log2\le\log s_i+\log(11/4).
\tag{1}
\]

All logarithms are natural. No minimum, seed, H guard, integer-junction,
parity, valuation, actual-word or primitive-count premise is imposed.
In particular no early-support reduction or failed full sufficient-test
conjunction is assumed.

## Conclusion

Every such tuple has b_0=0. More precisely, b_0>=1 would imply

\[
s_1<15000000,
\quad\text{whereas}\quad
s_1\ge4611686018427387904/11>400000000000000000.
\]

This is local RESEARCH/REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-10-23-d34-signed-recipient-zero.md`.
It specializes the inspected signed-offset mechanism at one changed
table, with no originality beyond the sources checked asserted.
The separate step438 critical audit below found no defect. Other recipients, cyclic-order
assembly, last-pair assembly, actual-word transfer and universal eventual
descent are not conclusions of this lemma.

## Proof

### Imported cap and matching its exact hypotheses

Import only L076's audited guard-conditioned cap proof (6)–(7), before
its later negative tail-20 offset test. L084's all-member independent
audit supplies its invariant analytic and residual/root-cap data at d34.
Its failing C/H test-allocation caps are different quantities and are
unused. L090 is a signed-comparison precedent, not a d34 theorem input.

The assessed finite real-affine input is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section2, equations (2)–(4), Lemma2, pp.228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The positive-real logarithm estimate in the imported cap is
[DLMF4.5.1](https://dlmf.nist.gov/4.5.E1), log(1+x)<x for x>0.
The prior assessment inspected the relevant primary hypotheses/proof
cases. No general affine or analytic theorem is reproved here; the
following checks justify only the changed table's applicability.

All H_i>=6>=3 and the strictly increasing J_i are unchanged. Opposite
H changes preserve sum H=199390205 and sum J=66061058. Every allocation
in the stated simplex has sum a=50+18B=166504460. Hence

\[
K=\sum_i(3J_i+H_i)=397573379,\quad
N=\sum_i(4J_i+H_i)+\sum_i a_i=630138897.
\]

L055 (2) and L084 (2)/its all-member audit therefore supply

\[
0<\lambda:=10584/10^{14}<\Lambda:=N\log2-K\log3<10585/10^{14}.
\tag{2}
\]

Put n_i=s_i-kappa>=47 and

\[
\eta_i=\kappa-(12/11)(16/27)^{J_i}
                  -(16/27)^{J_i}(2/3)^{H_i},\qquad c_i=2^{-a_i}G_i.
\]

Each subtracted term is positive and their sum is less than
12/11+1=kappa because the displayed powers lie in (0,1).
Thus 0<eta_i<kappa. Subtracting kappa in (1) gives
n_(i+1)=c_i(n_i+eta_i). The product is prod c_i=3^K/2^N,
including every allocated tail and the closing tail even if a_24=2.
These match precisely the positive full-cycle hypotheses of L076 (6).
That identity and cap proof apply with

\[
\Lambda=\sum_{i=0}^{24}\log(1+\eta_i/n_i),\qquad
n_i\ge(4\cdot2^{4J_i}-23)/11\ge(4\cdot2^{60}-23)/11\quad(i\ge1).
\]

Here the lower bounds are each occurrence's own non-strict J guard;
J_1=15 is the smallest J among i>=1. Consequently L076 (7) uses exactly

\[
E=\frac{552}{4611686018427387881},\qquad
\lambda-E=\frac{6101253702379434166563}
 {57646075230342348512500000000000}>0.
\]

L084's separately checked residual/cap data, also reproduced by the
finite rational calculation below, give

\[
s_0<R:=\frac{\kappa}{\lambda-E}+\kappa
=\frac{1325859730438202850942226985830949}{67113790726173775832193}
<U:=20000000000.
\tag{3}
\]

All quantities inverted in this cap are positive. The strictness is
inherited from the positive logarithm inequalities even if some J
guards are equalities. No H>=7 restriction occurs in this proof case;
H_0=6 is admitted. Neither a minimum nor growth of arbitrary later
rows is required. The unavailable tail-20 sign condition first enters
a later part of L076, which is not invoked.

### Signed comparison at the actual input

Suppose b_0>=1. Its integrality gives a_0>=20. At the actual input,
before any tail replacement,

\[
G_0s_0-Q_0=G_0(n_0+\eta_0)>0.
\]

Therefore replacement of a_0 by 20 can only increase the endpoint.
The tail-20 map has positive slope, so the strict cap (3) implies

\[
s_1\le2^{-20}(G_0s_0-Q_0)+\kappa
<F_{34}(U):=2^{-20}(G_0U-Q_0)+\kappa.
\tag{4}
\]

With J_0=8,H_0=6, the exact signed quantities are

\[
G_0=\frac{205891132094649}{274877906944},\quad
Q_0=\frac{2363}{176},\quad
\kappa-2^{-20}Q_0=\frac{385873605}{184549376}>0.
\tag{5}
\]

The positive offset is retained, rather than replaced by a negative
offset premise. In particular Q_0<kappa*2^20 is the preserved failure
of the old sufficient test. Direct substitution gives

\[
F_{34}(U)=\frac{22117214692422282938715}{1548112371908608}<15000000,
\]
\[
15000000-F_{34}(U)
=\frac{1104470886206837061285}{1548112371908608}>0.
\tag{6}
\]

For an additional check, factoring the same expression as in L090 gives
F_34(U)=2^(-20)(3/2)^6[(27/16)^8U-12/11]+kappa-2^(-20).
It agrees exactly with (6), retaining both subtractions inside the tail
division and kappa outside. No assertion about other d is needed.

Row1's own-input guard in (1), with J_1=15, instead requires

\[
s_1\ge(4/11)2^{60}=4611686018427387904/11>400000000000000000.
\tag{7}
\]

Equations (4), (6) and (7) contradict each other strictly at the same
input s_1. Hence b_0=0. All other allocations remain arbitrary: they
enter only the already matched full-cycle cap. This is a comparison
at an assumed solution's actual input, not a constructed comparison
trajectory, sampled root or assumption about later growth.

### Finite evidence and scope

Run `python3 scripts/postspell-word-count/certify_d34_recipient_zero.py`.
Full evidence is `scripts/postspell-word-count/d34-recipient-zero-certificate.json`.
All 20 exact checks pass, with zero failures. The complete changed
table, cap, signed comparison and every check record were inspected
in full. The certificate records actual/required operands, differences,
the preserved offset failure and agreement of both endpoint formulas.
The analytic enclosure (2) is imported, not newly certified by this
constructor. The written argument supplies the full-simplex quantifiers;
finite arithmetic alone is not an independent critical audit.

Attempt032, L084's failed S/C/H data, both original d0 rational witnesses
and prior unfinished work remain valid. This supplies only recipient
zero; recipients1–22, assembly with L097/C096a and broader actual-word
transfer remain unresolved. Universal eventual descent is still open.

### Independent critical audit — 2026-10-24, step438

The unchanged SPECIALIZE assessment
`drafts/literature/2026-10-24-d34-recipient-zero-critical-audit.md`
approved exactly this RESEARCH/REPRODUCTION proof audit. No defect was
found in the stated full-simplex recipient-zero implication. This secures
an existing local input; it adds no new recipient exclusion or theorem
beyond the inspected source machinery. The precise external citations
above and their previously inspected hypotheses are reused.

**Cap applicability.** Only the cap proof (6)–(7) of L076 is invoked,
not its theorem with the additional offset and margin tests. Its proof
uses J_i>=2,H_i>=3, the lower domain, all cyclic endpoints, the own-input
J guards, increasing J and a positive residual. The full L055 table,
with exactly the two specified H changes, satisfies these requirements:
H_0=6 is admissible and J_1=15 is the least nonzero-index J. No H>=7
premise or negative tail20 offset occurs before the cap inversion.
L084's all-member audit separately certifies this cap; its failed C/H
test-allocation caps are not the guard-conditioned quantity R.

For every admitted allocation, n_i>=47 and 0<eta_i<kappa. Thus the
unshifted recurrence has positive factors and full-product cancellation
is legitimate. In particular the product is over all 25 equations,
including the closing equation, and its exponent N contains the full
sum a_i=50+18B even when a_24=2. The opposite H changes leave both
K and N unchanged. The inherited analytic interval therefore concerns
exactly the present product. Applying each nonzero-index guard bounds
all 24 remaining positive logarithmic terms strictly by E in total.
The index-zero term is strictly below kappa/n_0. Hence the positive
residual lambda-E gives n_0<kappa/(lambda-E) and s_0<R<U.
Strictness survives equality in any J guard. Neither a distinguished
minimum nor an assumption about later-row growth has entered.

**Tail comparison and contradiction.** At the assumed solution's actual
input, G_0s_0-Q_0=G_0(n_0+eta_0)>0 before replacing any tail. Integer
b_0>=1 implies a_0>=20, so division by 2^20 provides an upper bound.
The positive slope G_0/2^20 and strict input cap then make (4) strict.
The independently rebuilt signed offset is positive, exactly as (5)
states; discarding it or invoking L076's failed offset test would be
invalid. The computation retains -(12/11)(3/2)^6 and -1 inside the
tail division, and +23/11 outside it. The actual s_1 in this comparison
is the outgoing input of indexed row1, whose non-strict guard requires
s_1>=2^62/11. The strict endpoint bound in (6) is incompatible with
that threshold. Arbitrary later allocations enter only the full cap,
so there is no sampling, prior early-support or last-pair assumption.

**Independent finite evidence.** Run
`python3 scripts/postspell-word-count/audit_d34_recipient_zero.py`.
The auditor neither imports nor executes the constructor. A separate
transcription of all 25 original pairs is compared with L055, and the
two changed rows are rebuilt explicitly. It recomputes the totals,
residual and cap, obtains row0's multiplier directly from its prime
exponents, and forms the endpoint with a single common integer
denominator. The factorized expression is a separate equality check.
All nine exact fractions displayed in (3), (5), (6), (7) and the
preceding residual calculation agree, including the strict endpoint
slack. Every stored construction comparison has freshly reconstructed
operands, relation, difference and verdict; exact key sets, array
lengths and ordered names guard against omission or duplication.

The complete evidence is
`scripts/postspell-word-count/d34-recipient-zero-audit-certificate.json`.
All 20 mathematical checks pass, with 398 comparison records and zero
failures or mismatches. The latter count includes structural and
repeated operand comparisons, not 398 distinct mathematical claims.
The complete changed table, cap, signed data, all 20 check records,
provenance and summary were inspected in full. The audit program
compares every mathematical construction field, source hash and
displayed fraction. Its record also preserves the exact construction
hash. The construction certificate is unchanged. The analytic Lambda
enclosure is an audited L055/L084 import, not independently recertified
by this finite audit; the quantified argument is the proof checked
above, not a consequence of the finite flags alone.

Attempt032, all failed S/C/H data and both original d0 witnesses remain
valid. The direct inputs L055,L076,L084 remain accurate, and no argument
has changed: DAG and PROOF.md need no status-only edit. This canonical
audit supersedes their earlier pending-audit description of L098.
Recipients1–22, assembly with L097/C096a, actual-word transfer and
universal eventual descent remain unresolved. No complete candidate
has been obtained, and no conclusion for other tables is asserted.

## Mathlib

Full matching coverage is unchecked, not absent. Supporting real-log,
affine and rational-arithmetic facts are not a formalization of this
complete quantified specialization. No Lean proof is claimed.
