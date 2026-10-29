# L105 — d35 row0/row1/row24 allocation-triangle exclusion

## Hypotheses

Use the 25 indexed pairs of L055's literal table, replacing only
H_0=5 and H_24=32670656. Put B=9250245 and let m,u be integers with
m>=1, u>=1 and m+u<=B. Define

\[
b_0=m,\quad b_1=u,\quad b_{24}=B-m-u,\quad
b_2=\cdots=b_{23}=0,\qquad a_i=2+18b_i,\qquad\kappa=23/11.
\]

Let G_i=(27/16)^{J_i}(3/2)^{H_i} and
Q_i=(12/11)(3/2)^{H_i}+1. Suppose real s_0,...,s_25 satisfy

\[
s_i\ge540/11\quad(0\le i<25),\qquad s_{25}=s_0,
\qquad s_{i+1}=2^{-a_i}(G_i s_i-Q_i)+\kappa\quad(0\le i<25),
\tag{1}
\]

and the own-input non-strict J and strict H guards

\[
4J_i\log2\le\log s_i+\log(11/4),\qquad
H_i\log2<\log s_i+J_i\log(27/16)\quad(0\le i<25).
\tag{2}
\]

All logarithms are natural. There is no minimum, seed, integer-junction,
residue, exact-valuation, actual-word realization or primitive-period
premise. Coincident coordinates and repeated periods are permitted.
The entire closing-tail2 edge m+u=B is included.

## Conclusion

No such real tuple exists anywhere in the stated integer triangle.
The unique tuple satisfying the endpoint equations alone has positive
shifted coordinates and its row2 input satisfies, uniformly,

\[
s_2<\frac{3296101068718600000010143}{4851}<10^{21}.
\tag{3}
\]

Its necessary non-strict J_2=28 guard instead requires

\[
s_2\ge\frac4{11}2^{112}
=\frac{20769187434139310514121985316880384}{11}>10^{21}.
\tag{4}
\]

One failed necessary guard suffices; the other guards and lower-domain
bounds of the endpoint-only tuple are not individually certified.

This is RESEARCH/REPRODUCTION under the invocation-start SPECIALIZE
assessment `drafts/literature/2026-10-25-d35-row0-row1-row24-feasibility.md`.
It is local specialization of assessed finite-affine machinery, not
claimed progress beyond the inspected sources. Independent critical
audit on 2026-10-26 retained the result without mathematical repair;
its evidence and limitations are recorded below. Other supports, orders, entry, actual-word transfer,
divergence and universal descent remain open.

## Proof

### Shifted equations and matching the denominator

Set n_i=s_i-kappa and

\[
c_i=\frac{3^{3J_i+H_i}}{2^{4J_i+H_i+a_i}},\qquad
\eta_i=\kappa-\frac{12}{11}(16/27)^{J_i}
                   -(16/27)^{J_i}(2/3)^{H_i}.
\tag{5}
\]

Here J_i>=2,H_i>=3. The two subtracted quantities are positive and
their sum is strictly below 12/11+1=kappa. Thus 0<eta_i<kappa.
They are independent of m,u. Direct substitution in (1), using
Q_i/G_i equal to that sum, gives

\[
n_{i+1}=c_i(n_i+\eta_i).
\tag{6}
\]

This retains both subtractions inside tail division and kappa outside.
L055 supplies the literal table and finite-affine method; its different
witness, minimum, seed and guard margins are not imported.

The unchanged J sum is 66061058 and the changed H sum is still
199390205, since the modifications are -35 and +35. For every
parameter pair, sum b_i=B and sum a_i=50+18B=166504460. Hence

\[
K=\sum_i(3J_i+H_i)=397573379,\qquad
N=\sum_i(4J_i+H_i+a_i)=630138897.
\]

These are exactly the operands of L104's audited enclosure:

\[
\lambda_-:=\frac{10584}{10^{14}}<\Lambda:=N\log2-K\log3
 <\frac{10585}{10^{14}}=: \lambda_+<\frac12.
\tag{7}
\]

Consequently the full product is P_25=exp(-Lambda) in (0,1),
independent of m,u, and D=exp(Lambda)-1>lambda_->0.
The positive-real exponential inequalities give
exp(Lambda)<=1/(1-Lambda)<1/(1-lambda_+)<2.
Their hypotheses hold by (7). This imports an enclosure for exactly
the same real number, not for a changed expression or sampled parameter.

### Exact cyclic root at the row2 input

For this calculation only, order the rows
(t_0,...,t_24)=(2,3,...,24,0,1). This cyclic cut does not change their
chronological adjacency. Define P_0=1,
P_k=product_{j<k}c_{t_j}, and

\[
\mathcal B_2=\sum_{k=0}^{24}\frac{\eta_{t_k}}{P_k}.
\]

Finite affine composition forces and defines

\[
n_2=\mathcal B_2/D.
\tag{8}
\]

Explicitly, write z_k for the shifted input at row t_k, and z_25 for
the output of row1. Dividing (6) by P_{k+1}=P_k*c_{t_k} gives
z_{k+1}/P_{k+1}=z_k/P_k+eta_{t_k}/P_k. Summing yields
z_25=P_25(z_0+mathcal B_2). Exact closure z_25=z_0 therefore gives
(8), because P_25^{-1}-1=D>0. Conversely, set z_0 by (8) and

\[
z_k=P_k\left(z_0+\sum_{j<k}\eta_{t_j}/P_j\right).
\]

Each successive equation is (6), and the same closure identity gives
z_25=z_0. The outgoing row indices are 3,...,24,0,1,2, retaining
row24-to-row0, row0-to-row1 and row1-to-row2. Returning these values
to their original indices and adding kappa satisfies every endpoint
in (1), including s_25=s_0. This proves existence and uniqueness for
the endpoint equations alone. All z_k are positive since every factor
and summand is positive. It does not assert their domain or guard
conditions, nor require a minimum or a primitive period.

### Uniform reciprocal-prefix estimate

Rows2,...,23 have unchanged tail2 and H_i>=6, J_i>0. Therefore

\[
c_i=(27/16)^{J_i}(3/2)^{H_i}/4
 >(3/2)^6/4=729/256>2\qquad(2\le i\le23).
\]

For k=0,...,22 the prefix P_k uses only these rows, so P_k>=2^k.
These are precisely the 23 prefixes before rows2,...,24. Thus

\[
\sum_{k=0}^{22}P_k^{-1}\le\sum_{k=0}^{22}2^{-k}
=\frac{8388607}{4194304}<2.
\tag{9}
\]

Do not apply that growth bound to row24. Its actual tail depends on
both parameters and may be2. Instead use the exact full product to
obtain the remaining two prefixes:

\[
P_{23}=\frac{\exp(-\Lambda)}{c_0c_1},\qquad
P_{24}=\frac{\exp(-\Lambda)}{c_1}.
\tag{10}
\]

Their numerator/denominator exponent pairs are respectively
(397573233,630138724-18m-18u) and
(397573262,630138763-18u). In particular these identities include
the actual row24 endpoint and tail, not a prefix of a different word.
The only remaining multipliers obey

\[
c_0(m)=\frac{3^{29}}{2^{57}}2^{-18(m-1)}
 \le\frac{3^{29}}{2^{57}}<\frac1{1000},
\qquad
c_1(u)=\frac{3^{117}}{2^{152}}2^{-18(u-1)}
 \le\frac{3^{117}}{2^{152}}<2^{34}.
\tag{11}
\]

The last two strict inequalities are finite integer comparisons:
1000*68630377364883<144115188075855872 and 3^117<2^186.
The factors multiplying these constants belong to (0,1] for every
m,u>=1. Combining (7),(10),(11) gives

\[
P_{23}^{-1}<2^{35}/1000,\qquad P_{24}^{-1}<2^{35}.
\tag{12}
\]

Equations (9),(12) and 0<eta_i<kappa show

\[
0<\mathcal B_2
 <\kappa\left(2+\frac{1001}{1000}2^{35}\right)
 =\frac{98883032061558}{1375}.
\]

Using D>lambda_- in (8) and then adding kappa gives exactly

\[
s_2<\frac{98883032061558/1375}{10584/10^{14}}+\frac{23}{11}
 =\frac{3296101068718600000010143}{4851}<10^{21}.
\]

This is uniform on the entire parameter triangle, not an inference
from its vertices. When m+u=B, a_24=2 and (10) still holds exactly;
all powers in (11) remain finite and positive. The point m=u=1 is
included. No limiting argument, discarded closing term, or C104a
edge monotonicity has been used.

At the same original input s_2, the non-strict J guard in (2), with
J_2=28, exponentiates to (4). Its lower bound exceeds 10^21 by
20769187434128310514121985316880384/11>0. This contradicts (3),
and proves infeasibility without any need to certify the other guards.

### Evidence, sources and qualifications

Reproduce the finite checks with
`python3 scripts/postspell-word-count/certify_d35_row0_row1_row24.py`.
It writes `scripts/postspell-word-count/d35-row0-row1-row24-certificate.json`
with the full changed table, affine exponent coefficients, all25 cut2
prefixes, triangle vertices, imported Lambda interval and exact bound
operands. All444 checks pass with no failures. The complete prefix,
vertex and bound records were inspected with the scoped JSON inspector.
The vertex checks are domain bookkeeping only. Uniformity and closure
are proved above; neither parameter sampling nor a certificate preview
establishes them. Logarithms are imported from audited L104 after exact
total matching, not independently recertified. This construction
certificate is not an independent critical audit or formal verification.

The assessed finite-affine source is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*,
Acta Arithmetica78 (1997),227–239, DOI10.4064/aa-78-3-227-239,
[Lemma2, pp.228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Only finite composition and the nonzero-denominator fixed point are
used. The displayed algebra verifies applicability to these changed
shifted blocks and the cyclic cut; it does not reprove general coding
or supply integer realization. Reused positive-real analytic coverage
is [DLMF4.6.4](https://dlmf.nist.gov/4.6.E4) for L104's log enclosure
and [4.5.8–4.5.11](https://dlmf.nist.gov/4.5) for the exponential
comparisons, recorded version1.2.8. The denominator and argument
hypotheses are checked in (7). No fresh source retrieval is claimed.

The prior scoped comparison found no matching triangle verdict:
C104a has u=0, C103a assumes b0=0, L104 fixes m=1,u=0, and L098
changes the H data. These are scope contrasts, not imported triangle
conclusions. Attempt032's failed sufficient support package is preserved;
its failure did not imply feasibility. Both d0 witnesses and unfinished
work remain intact. Only L055 and L104 supply direct mathematical inputs.
This result has no actual-word transfer or unrestricted Collatz conclusion.

### Independent critical audit — 2026-10-26

This separate RESEARCH/REPRODUCTION audit uses the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-25-l105-triangle-critical-audit.md`.
No mathematical defect was found. The statement and proof are retained;
this verifies a local restricted input, not a new theorem beyond the
sources checked or a complete Collatz argument.

The shift was independently checked in the original endpoint:
n_(i+1)=c_i*n_i+c_i*kappa-2^(-a_i)*Q_i. Dividing Q_i by G_i
gives exactly the two subtractions in eta_i. Since J_i,H_i>0, each
power (16/27)^J_i and (2/3)^H_i lies strictly between zero and one.
Thus their weighted sum is strictly between zero and 12/11+1=kappa,
proving 0<eta_i<kappa without any hypothesis about the unknown inputs.

Independent transcription and summation of all25 literal rows, followed
by H0-=35,H24+=35, gives sum J=66061058 and sum H=199390205.
The affine tail coefficients sum to (166504460,0,0), where the last
two entries multiply m,u. Consequently the full product has exactly
K=397573379,N=630138897 for every allowed pair. These are L104's
audited operands, so (7) imports the same real Lambda. Its strict
positive lower bound and upper bound below1/2 imply D>lambda_->0
and exp(Lambda)<2 as used above. The audit does not claim a new log
enclosure; L104's complete independent-audit argument was read and
its enclosure reused only after this exact matching.

At cut2, the divided recurrence telescopes to
z25=P25*(z0+B2). Since P25=exp(-Lambda) is in (0,1), closure
forces the unique z0=B2/(P25^-1-1). Conversely the displayed
prefix formula in (8)'s proof satisfies every divided recurrence and
returns exactly to z0 after row1. All coordinates are positive from
positivity of this root, every prefix and every summand. The original
indices are retained on returning to s_i: rows24,0,1 have outputs
0,1,2 respectively. Thus no endpoint or closing equation is omitted.
This argument makes no minimum, seed or primitive-period assumption,
and permits coincident coordinates and repeated periods.

Every cut2 prefix was independently summed from its indicated subset
of rows. For k=0,...,22 the factors are exactly rows2,...,k+1,
all with tail2, J>0,H>=6. Hence c_i>729/256>2, proving the
first23 reciprocal bounds including the empty prefix. Their geometric
sum is exactly 8388607/4194304<2. The other prefixes have powers
(397573233,630138724-18m-18u) and
(397573262,630138763-18u). Adding respectively the powers of
c0*c1 and c1 gives exactly (K,N); this verifies (10), including
the row24 tail. It is never treated as an ordinary growth factor.

The remaining multipliers have denominator exponents 39+18m and
134+18u, and numerator exponents29 and117. Thus m,u>=1 give
exactly the maxima in (11), independently of each other. The complete
integer comparisons 1000*3^29<2^57 and 3^117<2^186 pass. Together
with exp(Lambda)<2 these prove both remaining reciprocal bounds.
This is a symbolic bound for every pair, not a vertex inference.
Substituting u=B-m into the row24 tail yields identically2, so the
entire closing edge is included without any limiting argument.

Full rational recomputation gives B2<98883032061558/1375 and
s2<3296101068718600000010143/4851<10^21. Independently the
row2 table value J2=28 makes its non-strict guard equivalent, on
positive s2, to s2>=20769187434139310514121985316880384/11.
This exceeds10^21 by the positive rational displayed in the proof.
The same original input s2 occurs in both comparisons. The strict
upper cap therefore contradicts the necessary non-strict guard;
other guards and domain lower bounds need not hold for this endpoint
tuple and are not asserted to have been verified.

Reproduce with
`python3 scripts/postspell-word-count/audit_d35_row0_row1_row24.py`.
It neither imports nor executes the construction program. The separate
`scripts/postspell-word-count/d35-row0-row1-row24-audit-certificate.json`
contains the independently matched table, all25 input prefixes and
the complete product, exact bound operands and1130 passing checks,
with no failures. It also replays all444 original finite comparisons
and their differences without trusting their saved pass flags.
Complete relevant prefix and bound records were inspected. These
checks accompany the symbolic uniformity and closure arguments above;
neither the check count nor parameter samples establish them.

The cited finite-affine and positive-real machinery remains unchanged;
the audit checks this specialization rather than reproving a general
coding theorem. L055 and L104 remain the only direct mathematical
inputs; no dependency is added. Attempt032 and the d0 witnesses remain
untouched. Other supports, order exhaustion, entry, actual-word transfer,
divergence and universal descent remain unresolved.

## Mathlib

Full matching coverage for this two-parameter infeasibility statement
has not been checked. L055's supporting affine and logarithmic references
are not a matching theorem for these changed guards and prefixes.
No absence claim is made. The proof remains informal; the separate
critical audit above is not formal verification or an actual-word transfer.
