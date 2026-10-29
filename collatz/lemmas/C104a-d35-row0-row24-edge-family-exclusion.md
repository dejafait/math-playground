# C104a — d35 row0/row24 allocation-edge exclusion

## Hypotheses

Use all 25 indexed pairs in L055's literal table, changing only
H_0=5 and H_24=32670656. Let B=9250245 and let m be an integer
with 1<=m<=B. Set

\[
b_0=m,\quad b_{24}=B-m,\quad b_1=\cdots=b_{23}=0,
\qquad a_i=2+18b_i,\qquad \kappa=23/11.
\]

For G_i=(27/16)^{J_i}(3/2)^{H_i} and
Q_i=(12/11)(3/2)^{H_i}+1, suppose real s_0,...,s_25 satisfy

\[
s_i\ge540/11\ (0\le i<25),\quad s_{25}=s_0,\quad
s_{i+1}=2^{-a_i}(G_i s_i-Q_i)+\kappa\ (0\le i<25),
\tag{1}
\]

with the own-input non-strict J and strict H guards

\[
4J_i\log2\le\log s_i+\log(11/4),\qquad
H_i\log2<\log s_i+J_i\log(27/16)\quad(0\le i<25).
\tag{2}
\]

All logarithms are natural. No minimum, seed, integer junction,
residue, exact valuation, realization or primitive-period premise
is imposed. Repeated periods remain permitted. In particular m=B
is included and has closing tail a_24=2.

## Conclusion

No such tuple exists, for every integer m in the full interval above.
More specifically, writing s_1(m) for the row1 coordinate of the unique
real tuple satisfying the endpoint equations alone, that tuple has
positive shifted coordinates and

\[
s_1(m)\le s_1(1)<\frac{82225000004347}{2079}<60000000000,
\tag{3}
\]

whereas row1's non-strict J guard requires
s_1(m)>=(4/11)2^60=4611686018427387904/11. No verification of the
remaining guards or of the lower-domain bounds for this endpoint-only
tuple is asserted or needed after this necessary guard fails.

This is local RESEARCH/REPRODUCTION under the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-25-d35-row0-row24-edge-family.md`.
It specializes assessed finite-affine machinery and audited L104;
it is not a novelty claim beyond the sources checked. Independent critical
audit on 2026-10-25 retained the statement without repair, as recorded
below. This excludes only this literal allocation edge;
other positive-row0 support, arbitrary order, entry, actual-word
transfer, divergent trajectories and universal descent remain open.

## Proof

### Exact parameter dependence and denominator applicability

For each parameter put n_i=s_i-kappa and use the shifted affine
specialization of L055 and L104:

\[
c_i(m)=\frac{3^{3J_i+H_i}}{2^{4J_i+H_i+a_i(m)}},\qquad
\eta_i=\kappa-\frac{12}{11}(16/27)^{J_i}
                  -(16/27)^{J_i}(2/3)^{H_i}.
\tag{4}
\]

Substitution in (1) gives n_(i+1)=c_i(m)(n_i+eta_i), with
0<eta_i<kappa. The positivity proof in L104 uses only J_i>=2,H_i>=3,
which hold unchanged; the eta_i do not depend on tails or m. This
retains both subtractions inside the tail division and kappa outside.

With delta=m-1, the only changed tails relative to L104 are
a_0(m)=20+18delta and a_24(m)=166504394-18delta. Consequently

\[
c_0(m)=c_0(1)2^{-18\delta},\qquad
c_{24}(m)=c_{24}(1)2^{18\delta},\qquad
c_i(m)=c_i(1)\ (1\le i\le23).
\tag{5}
\]

The two factors cancel in the full product. Direct sums from L055's
table, with the stated H changes canceling each other, give for every m

\[
K=\sum(3J_i+H_i)=397573379,\qquad
N=\sum(4J_i+H_i+a_i(m))=630138897.
\]

Indeed sum b_i=B, so sum a_i=50+18B independently of m. Thus L104's
audited enclosure applies to the identical real number

\[
\Lambda=N\log2-K\log3,\qquad
0<10584/10^{14}<\Lambda<10585/10^{14}<1/2.
\tag{6}
\]

In particular P_25=product c_i(m)=exp(-Lambda) is independent of m
and belongs to (0,1). The denominator D=exp(Lambda)-1 is positive
and independent of m. No enclosure for a changed logarithm expression
is being presumed.

### Cut1 root and uniform comparison

Order the rows t_0,...,t_24=(1,2,...,24,0), and define
P_0(m)=1 and P_k(m)=product_(j<k)c_(t_j)(m). Let

\[
\mathcal B_1(m)=\sum_{k=0}^{24}\frac{\eta_{t_k}}{P_k(m)}.
\]

The exact finite composition used in L104 gives

\[
n_1(m)=\frac{\mathcal B_1(m)}{D}.
\tag{7}
\]

To check its full endpoint specialization here, the coordinate at
input t_k is P_k(m)[n_1(m)+sum_(j<k)eta_(t_j)/P_j(m)]. Dividing
successive expressions by their prefixes gives exactly each recurrence
in (4). After all25 rows the value is
P_25[n_1(m)+mathcal B_1(m)]=n_1(m), by (7). The chronological
outgoing indices are 2,...,24,0,1, so row24-to-row0 and row0-to-row1
are both present. Conversely closure forces (7) since D>0. This proves
uniqueness and existence of the endpoint-only tuple. Every shifted
coordinate is positive because every factor, eta_i and n_1(m) is
positive. No minimum, seed or domain premise was introduced.

For 0<=k<=23, the prefix P_k uses only rows1,...,k, all of which
are unchanged in (5). Thus P_k(m)=P_k(1) for all those24 prefixes,
including the input prefix of row24. The last prefix, before row0,
must instead use the exact full-product identity:

\[
P_{24}(m)=\frac{\exp(-\Lambda)}{c_0(m)},\qquad
P_{24}(m)^{-1}=c_0(1)\exp(\Lambda)2^{-18\delta}.
\tag{8}
\]

In exponent form this last prefix is
3^397573350 / 2^(630138858-18m); it includes row24's actual tail.
No lower growth bound for c_24(m) is required. Put
A=sum_(k=0)^23 eta_(t_k)/P_k(1)>0. Equations (5) and (8) now give
the exact parameter formula

\[
\mathcal B_1(m)
=A+\eta_0 c_0(1)\exp(\Lambda)2^{-18(m-1)}.
\tag{9}
\]

Since m>=1, its final factor belongs to (0,1]. All other terms in
(9) and D are fixed and positive, so
mathcal B_1(m)<=mathcal B_1(1) and n_1(m)<=n_1(1). Adding the
same kappa proves s_1(m)<=s_1(1). Equality occurs at m=1; the
comparison is strict for m>1. At m=B, a_24=2 and the final factor
in (9) is 2^-166504392, still strictly positive. Hence this endpoint
is included without a limiting argument or a presumed large closing
tail. The other endpoint m=1 is exactly audited L104.

L104's conclusion supplies the strict rational bound in (3). To recall
its actual threshold comparison, J_1=15 is unchanged, so exponentiating
its own-input non-strict J guard gives
s_1(m)>=(4/11)2^60. This exceeds the uniform coarse cap by
4611685358427387904/11>0, contradicting (3). One violated necessary
guard proves the claimed infeasibility; no assertions about the other
guards are substituted for this contradiction.

### Evidence, sources and qualifications

`python3 scripts/postspell-word-count/certify_d35_row0_row24_family.py`
writes `scripts/postspell-word-count/d35-row0-row24-family-certificate.json`.
It records the complete changed table with affine-in-m tails and
exponents, all25 cut1 prefixes, both allocation endpoints, the imported
L104 Lambda interval and full rational cap/guard operands. All273
finite checks pass, with no failures or parameter samples. The complete
prefix list, endpoint records, bound operands and summary were inspected
with the scoped JSON inspector. Endpoint bookkeeping is not an
exhaustive parameter test; (5)–(9) prove uniformity. The certificate
reproduces the small rational comparisons but imports L104's audited
log enclosure, without claiming an independent recertification or audit.

The precise external finite-affine input already assessed for L055 and
L104 is Halbeisen–Hungerbuehler, *Optimal bounds for the length of
rational Collatz cycles*, Acta Arithmetica78 (1997),227–239,
DOI10.4064/aa-78-3-227-239,
[Lemma2, pp.228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Only finite composition and the nonzero-denominator fixed point are
used; the changed block parameters and their uniform comparison are
justified above. No general coding theorem is reproved. L104's audited
enclosure and exponential comparisons reuse the positive-real coverage
of [DLMF4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.5.8–4.5.11](https://dlmf.nist.gov/4.5), recorded version1.2.8.
Their argument and denominator hypotheses remain unchanged by (6).

The targeted duplicate/failure comparison found L104's fixed m=1
case, C103a's different b0=0 scope and L098's different H data, rather
than an existing full-edge proof. Neither C103a nor L098 is an input.
Attempt032's failed sufficient offset package remains preserved and
does not imply feasibility here. L055 is used for its table and affine
construction only; its different d0 witness, minimum and seed are not
imported. Both d0 witnesses and unfinished work are preserved.

### Independent critical audit — 2026-10-25

This separate RESEARCH/REPRODUCTION audit uses the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-25-c104a-edge-family-critical-audit.md`.
No mathematical defect was found. The statement, proof and direct
mathematical inputs L055 and L104 are retained. This verifies a local
specialization of the cited machinery, not a result beyond those sources.

Direct substitution gives
n_(i+1)=2^(-a_i)G_i*n_i+2^(-a_i)(G_i*kappa-Q_i).
Since Q_i/G_i is exactly the sum of the two subtracted terms in (4),
this equals c_i(n_i+eta_i). All J_i>=2 and H_i>=3, so both powers
in those subtractions lie strictly between zero and one. Their sum
is positive and strictly below 12/11+1=kappa. Hence 0<eta_i<kappa,
independently of m, without any domain, minimum or realization premise.

The table was checked against L055 with precisely H0-=35,H24+=35.
In the independent parameter delta=m-1, the denominator exponents are
q0=57+18delta and q24=q24(1)-18delta; all others are constant.
Direct sums give K=397573379 and N=630138897 with zero parameter
slope. Thus the imported audited L104 enclosure is for exactly the
same Lambda, not an approximation at a sampled parameter. It proves
D=exp(Lambda)-1>lambda_->0 and P25=exp(-Lambda) in (0,1).

For the cut order t_k=1,...,24,0 let z_k be its input coordinate n.
Dividing each recurrence by P_(k+1)=c_(t_k)P_k gives
z_(k+1)/P_(k+1)-z_k/P_k=eta_(t_k)/P_k.
Summing all25 identities gives z25=P25(z0+B1). Exact closure
z25=z0 therefore forces z0=B1/D. Conversely the finite prefix
formula in the proof satisfies each divided equation and this closure.
The outgoing row indices are 2,...,24,0,1, explicitly retaining
row24-to-row0 and row0-to-row1. Every prefix and eta is positive;
the forced root and all n coordinates are positive. Thus uniqueness,
existence and positivity of the endpoint-only tuple hold for each
parameter. Its domain lower bounds and other guards are not presumed.

Independent direct resummation of each prefix gives zero delta slope
for k=0,...,23: their included rows are exactly1,...,k. At k=24
the exponents are (397573350,630138840-18delta), equivalently
(K-29,N-57-18delta). Hence P24=P25/c0 for every parameter,
including the actual closing tail. The last reciprocal prefix is
c0(1)*exp(Lambda)*2^(-18delta); eta0 is constant and positive.
This establishes (9) with a positive constant A and fixed positive D.
It proves the comparison uniformly, rather than from the two endpoints.
On 0<=delta<=9250244 all budgets are nonnegative and tails are
2 modulo18 and at least2. At delta=9250244 the closing tail is
exactly2 and the decay exponent is -166504392, still finite. No
limiting argument or lower growth premise for c24 has been used.

The imported cap was also checked from its exact operands. For rows
1,...,23, tail2 and H>=6 give c_i>729/256>2. Therefore the first24
reciprocal-prefix bounds sum to 16777215/8388608<2. Independently,
c0(1)=68630377364883/144115188075855872 and
c0(1)/(1-lambda_+)=9308590679915771484375/19546873380615407896887296
is strictly below1/500. L104's applicable positive-real exponential
bounds give B1<2093/500 and D>10584/10^14. Adding kappa to their
ratio gives exactly 82225000004347/2079<60000000000. Row1 has
J1=15 at the same input s1. Its non-strict J guard requires
(4/11)2^60=4611686018427387904/11, exceeding the coarse cap by
4611685358427387904/11>0. This one necessary guard contradicts
the uniform bound; no other guard or lower-domain certification is
needed. The strict H conventions and all endpoints remain hypotheses.

Reproduce the finite audit with
`python3 scripts/postspell-word-count/audit_d35_row0_row24_family.py`.
It writes `scripts/postspell-word-count/d35-row0-row24-family-audit-certificate.json`:
1172 passing checks, no failures, all25 resummed prefixes, both full
endpoint records, and complete rational operands. It recomputes all273
construction comparisons and their differences without trusting flags.
The full prefix, endpoint and bound records were inspected using the
scoped JSON inspector. The script imports L104's audited log enclosure
after checking identical totals; it does not recertify logarithms.
The symbolic proof above establishes uniformity and exact closure;
finite checks alone do not. Attempt032's insufficient support package,
both d0 witnesses and construction evidence remain preserved. Other
supports, order, entry and actual-word transfer have not been audited.

## Mathlib

Full matching coverage for this parameter-family infeasibility statement
has not been checked. L055 records supporting affine and logarithmic
coverage; this is not a matching theorem for the changed table or its
uniform bound. No absence claim is made. The symbolic proof is informal;
the rational/affine certificates do not constitute formal verification.
The separate informal critical audit is recorded above.
