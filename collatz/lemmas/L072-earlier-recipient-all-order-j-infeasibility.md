# L072 — Earlier-recipient all-order J-subsystem infeasibility

## Hypotheses

Use exactly the 25 indexed pairs J_i,H_i in L055. Choose integers
0<=j<=21 and 1<=t<=9250244, and attach tails

\[
a_j=20,\qquad a_{23}=2+18t,\qquad
a_{24}=166504394-18t,\qquad a_i=2\quad(i\notin\{j,23,24\}).
\]

Let pi be any permutation of {0,...,24}, keeping each triple intact.
Suppose real s_0,...,s_25 obey s_25=s_0, s_k>=540/11 and, at every
chronological position 0<=k<=24, the exact endpoint and own-input guard

\[
s_{k+1}=2^{-a_{\pi(k)}}\left((27/16)^{J_{\pi(k)}}
 (3/2)^{H_{\pi(k)}}s_k-(12/11)(3/2)^{H_{\pi(k)}}-1\right)+23/11,
\tag{1}
\]
\[
4J_{\pi(k)}\log2\le\log s_k+\log(11/4).             \tag{2}
\]

Logarithms are natural. These are only L051's endpoint/domain/J
conditions. No minimum location, growing-row, H/seed, integer, parity,
residue, exact-valuation, actual-word or primitive/count-ray premise is
imposed. Repeated periods and coincident junctions remain allowed.

## Conclusion

No such tuple exists for any admitted j,t or cyclic order. After rotation
to a smallest designated input, every nonliteral order fails its first
displaced row's J guard by more than
629441541677/50000000000>12.58. In literal order the row-24
right-minus-left guard margin strictly decreases with t and is below
-474883782659/125000000000<-3.79 already at t=1, uniformly in j.

This is a local RESEARCH/REPRODUCTION under the pre-existing SPECIALIZE
assessment `drafts/literature/2026-10-16-earlier-recipient-all-order-j-feasibility.md`.
It specializes inspected finite affine/logarithm machinery and audited
local methods, without claiming progress beyond the sources checked.
The separate critical audit below found no defect in this scope. No actual-word application is
assembled; other allocations, entry, unrestricted cycles, divergence and
universal eventual descent remain open. The known rational witnesses
have different allocations and remain valid.

## Proof

### Coordinate match, counts and minimum rotation

For indexed row i put

\[
c_i=3^{3J_i+H_i}/2^{4J_i+H_i+a_i},\qquad
\eta_i=23/11-(12/11)(16/27)^{J_i}
                  -(16/27)^{J_i}(2/3)^{H_i}.
\]

The table has J_i,H_i>0, so 0<eta_i<23/11. With
n_k=s_k-23/11>=47, substitution in (1) gives exactly
n_(k+1)=c_(pi(k))(n_k+eta_(pi(k))). Indeed c_i times the two
subtracted terms in eta_i is precisely
2^(-a_i)((12/11)(3/2)^H_i+1), retaining both shifts.

The standard formal affine input is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta Arith.
78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The saved assessment inspected the statement and essential induction
cases. Only formal affine composition and its nonzero-denominator root
formula are imported. The displayed coordinate calculation justifies
this specialization; there is no reproof of general coding or inference
of integer/parity realization.

Since j,23,24 are distinct, the complete tail sum is
44+20+(2+18t)+(166504394-18t)=166504460. L055's full table gives
sum J_i=66061058, sum H_i=199390205, hence unchanged totals
K=397573379, N=630138897, in every order. L055's audited bound gives

\[
0<\lambda_-:=10584/10^{14}<\Lambda=N\log2-K\log3
 <10585/10^{14}<1,\qquad \prod_i c_i=e^{-\Lambda}.   \tag{3}
\]

Multiplying all 25 unshifted endpoints, including closure, cancels the
positive n factors and gives
Lambda=sum_k log(1+eta_(pi(k))/n_k). For m=min n_k, the strict
inequality log(1+x)<x at x>0 therefore yields

\[
\min s_k=m+23/11
 <575/(11\lambda_-)+23/11
 =7187500000030429/14553<500000000000<e^{27}.        \tag{4}
\]

The last comparison is L071's exact positive partial sum
sum_(q=0)^40 27^q/q!>500000000000, recomputed in the certificate.
The analytic inputs already covered by the assessment are
[DLMF 4.5.1](https://dlmf.nist.gov/4.5.E1) at positive eta/n and
[4.2.19](https://dlmf.nist.gov/4.2.E19) for the exponential series.
Neither location nor growth of a minimum is assumed. Rotate the inputs
and their outgoing rows together to a minimum occurrence. Every endpoint,
both cyclic cuts and each own-input guard are preserved, including ties
and repeated values. In these coordinates log s_0<27.

### Complete nonliteral-order exclusion

Suppose the rotated pi is not the identity. Its first displaced position
k is at most 23, and its displaced row r=pi(k) is greater than k: all
smaller rows have already occurred. Preceding rows are precisely the
literal rows i<k<=23, so i<=22. Their actual tails are <=20 and H_i>=40.
Consequently their shifted affine offsets are negative, since

\[
2^{-a_i}((12/11)(3/2)^{H_i}+1)
 >(12/11)(3/2)^{40}/2^{20}
 =36472996377170786403/3170534137668829184>23/11.    \tag{5}
\]

Thus s_(i+1)<c_i s_i along this literal prefix. Define

\[
A_k=\sum_{i<k}(3J_i+H_i),\quad
D_k^{(j)}=\sum_{i<k}(4J_i+H_i+2)+18\mathbf1_{j<k}.
\]

Positive endpoints and (4)–(5) give
log s_k<27+A_k log3-D_k^(j) log2. The varying rows 23 and 24
occur in none of these prefixes. Let D_k^(22) be the prefix exponent
used in L071. For every k<=23 and j<=21,

\[
D_k^{(j)}-D_k^{(22)}
 =18(\mathbf1_{j<k}-\mathbf1_{22<k})\ge0.            \tag{6}
\]

For k<=22 the second indicator is zero; at k=23 both indicators are one.
This proves the changed-prefix comparison uniformly, including j=0.

Put S=10^12, ell=693147180559 and u=1098612288669. L055/L064's
audited outward bounds give log2>ell/S and log3<u/S. Also
log(11/4)<2, since e^2>1+2+2=5>11/4. L071's complete 300
first-displacement comparisons establish

\[
4J_r\ell-29S-A_k u+D_k^{(22)}\ell
 \ge12588830833540>0\qquad(0\le k<r\le24).         \tag{7}
\]

This is an import of its numerical comparison, not its different-tail
exclusion conclusion. Its 24 adjacent cases cover all 300 pairs by
strict increase of J_r. Equation (6) only increases each margin. With
A_k,D_k^(j)>=0, decreasing log2 and increasing log3 bounds the guard's
right side upward; decreasing log2 bounds its left side downward. Hence

\[
\log s_k+\log(11/4)
 <29+(A_k u-D_k^{(j)}\ell)/S<4J_r\ell/S<4J_r\log2.
\]

The strict rejection margin exceeds 12588830833540/S>12.58.
This first-displacement partition covers every nonidentity permutation,
without enumerating permutations or assuming suffix growth.

### Literal root and uniform parameter monotonicity

It remains to reject the literal order for every j. Fix j and define
C_i(t)=prod_(r<i)c_r(t), C_0=1,
B(t)=sum_(i=0)^24 eta_i/C_i(t), and D=exp(Lambda)-1>0.
Formal affine composition, with the full closing tail retained, gives
the unique cyclic root and all its inputs:

\[
n_0(t)=B(t)/D,\qquad
n_i(t)=C_i(t)\left(n_0(t)+\sum_{r<i}\eta_r/C_r(t)\right).
\tag{8}
\]

Indeed the normalized increments are eta_i/C_i and
C_25=1/(1+D); closure forces (8). All these rationals are positive.
For reference coefficients only, use t=0 with the same fixed recipient j.
No guard feasibility at t=0 is asserted. Put

\[
x=2^{-18t},\quad C=C_{24}(0)>0,\quad
A=\sum_{i<24}\eta_i/C_i(0)>0.
\]

All C_i for i<=23 are independent of t; C_24=Cx, while C_25 is
constant because the last two tail changes cancel. Thus
B=A+eta_24/(Cx), and (8) gives exactly

\[
n_{24}(t)=\eta_{24}/D+C A(1+D)x/D.                 \tag{9}
\]

Every coefficient is positive. Therefore n_24, s_24 and the own-input
margin log s_24+log(11/4)-4J_24 log2 strictly decrease with t.
This transports L070's method after the actual recipient has been
retained in C and A; its old-allocation conclusion is not invoked.

### Uniform boundary rejection, including recipient zero

At t=1 every first-24 tail is <=20. For row 0, even at j=0,
c_0>=3^64/2^92>10^8/2^18>2. For rows 1 through 23, the table gives
J_i>=15,H_i>=72, so c_i>=3^117/2^152>2. Thus
C_i>(10^8/2^18)2^(i-1) for 1<=i<=24 and C_i>=1 for 0<=i<=24.
Using 0<eta_i<23/11 and the finite geometric sum,

\[
B(1)<B_+:=(23/11)(1+2\cdot2^{18}/10^8)=9031479/4296875.
\]

Since D>Lambda>lambda_-, (8) implies, at every i<=24,

\[
\frac{s_i(1)}{C_i(1)}
 <B_+/\lambda_-+B_++23/11
 =37631162507944991614/1894921875<20\cdot10^9.       \tag{10}
\]

This is L064's coarse rational bound with its growth hypotheses checked
afresh for both boundary tail-20 rows. The exact positive partial sum
sum_(q=0)^40 24^q/q!>20*10^9 gives log(20*10^9)<24. In particular
log s_24(1)<24+log C_24(1). This growth claim is used only at t=1,
not for the later contracting-row regime.

The first 24 rows contain exactly two extra sets of 18 halvings at this
boundary, irrespective of j. Hence

\[
p=\sum_{i<24}(3J_i+H_i)=271907921,\quad
q=\sum_{i<24}(4J_i+H_i+a_i(1))=306970784,
\quad q+4J_{24}=430963900.
\]

Using L064's audited log(11/4)<1011600911679/S, with the same signed
log2/log3 bounds as above, the boundary margin satisfies

\[
\begin{aligned}
\log s_{24}(1)+\log(11/4)-4J_{24}\log2
 &<24+p\log3-(q+4J_{24})\log2+\log(11/4)\\
 &<\frac{24S+271907921u-430963900\ell+1011600911679}{S}\\
 &=-474883782659/125000000000<-3.79<0.
\end{aligned}                                                    \tag{11}
\]

Equation (9) rejects the same own-input guard at every admitted t.
The extreme final tail is 2, and has remained in closure throughout.
Every literal and nonliteral order is therefore excluded.

### Evidence and limitations

Run `python3 scripts/postspell-word-count/certify_earlier_recipient.py`.
The full certificate is
`scripts/postspell-word-count/earlier-recipient-certificate.json`.
It stores all 25 pairs, all 22 supports' boundary tails, reference
prefixes and t-coefficients, all 6600 first-displacement operands,
all boundary guard operands and exact exponential terms. All 31 rational
and 226 table checks pass; all 6600 margins are positive. The complete
rational checks, worst-prefix records, boundary guard operands and
uniform bounds were inspected. Equations (6) and (9), not sampling,
supply the full recipient, parameter and order coverage. L071's audited
full comparison supplies the other displacement cases; the certificate
also recomputes them. No approximate closure or floating logarithm is used.

The known logarithm enclosures use the outward rational remainder for
the positive-real expansion [DLMF 4.6.4](https://dlmf.nist.gov/4.6.E4),
already inspected in the saved assessment and audited in L055/L064.
The only new arithmetic is the changed-support specialization. L064's
t=0 classification and L070/L071's old-family exclusions were not
transferred as conclusions. Attempts 026/031 and the modular-diagnostic
stops retain their scopes. No H guard, seed, integrality, actual-word
necessity bridge, primitive lower bound or closure converse is used.
The separate critical audit below verifies this scope; this is not a candidate
resolution of Collatz.

### Independent critical audit — 2026-10-16

The exact target was approved before this invocation by the SPECIALIZE
assessment `drafts/literature/2026-10-16-earlier-recipient-critical-audit.md`.
The audit found no defect. This is verification of the stated local
reproduction, not a stronger exclusion or an originality claim. The
primary affine and analytic citations above are reused within their
inspected domains. No general coding theorem is reproved.

**Endpoint specialization and invariant product.** Subtracting 23/11
from (1), then writing s=n+23/11, gives
c_i n+(23/11)c_i-2^(-a_i)((12/11)(3/2)^H_i+1).
The latter two terms equal c_i eta_i exactly. Positivity of J_i,H_i
makes each subtracted term in eta_i positive and their sum strictly less
than 12/11+1, so 0<eta_i<23/11. The domain gives n>=47. No actual
parity or integer premise enters this change of coordinate.

The independently transcribed full table agrees with L055 and has the
stated J,H sums. Because the recipient is distinct from 23 and 24,
the tail sum is 166504460 identically in t. Thus the full multiplier is
exactly 3^397573379/2^630138897 in any order. Independent rational
logarithm enclosures give the particularly narrow outward interval

\[
\frac{105843488431681}{10^{24}}<\Lambda
 <\frac{105843488431682}{10^{24}},
\]

strictly inside (lambda_-,lambda_+). Multiplication of all 25 endpoint
equations cancels each positive input exactly once against an output,
including closure and repeated occurrences. With m=min n_k,
log(1+eta_i/n_k)<eta_i/n_k<23/(11m) is valid at every occurrence.
Consequently Lambda<575/(11m), and lambda_->0 gives (4) in the
stated direction. The exact fraction, all 41 positive exponential terms
at 27, and both comparisons with 500000000000 were independently checked.

**Both cuts and every nonliteral order.** If the selected minimum is
old position q, new input k is old input (q+k) modulo 25 and carries
that old input's outgoing row. The old closing edge still occurs; the
new closing edge is old q-1 to q. Every guard remains attached to its
own input. Ties and coincident values cause no loss. This proves the
minimum rotation without assuming which indexed row carries it.

In a nonidentity permutation, the first displaced position k is at most
23 and its row r exceeds k, since all rows below k have been consumed.
Its prefix comprises exactly rows 0,...,k-1, all at most 22. Those
tails are at most 20 for every t and their H values are at least 40.
The exact offset bound (5) is strictly greater than 23/11; the discarded
positive 2^(-a_i) also preserves strictness. Thus s_(i+1)<c_i s_i
on precisely the edges used. No varying-tail row enters that induction.

For k<=22, the difference in (6) is 18 times the nonnegative indicator
of j<k; for k=23 both indicators are one. This proves every changed
prefix comparison, including j=0. At k=0 the empty prefix retains
log s_0<27. Nonnegative A_k,D_k justify increasing log3 and decreasing
the subtracted log2 to bound the right side upward. Decreasing log2
bounds the guard's positive left side downward. The bound log(11/4)<2
has the positive exponential-series justification already stated.

The independent program directly sums every prefix and reconstructs all
6600 pair operands. It also reconstructs L071's 300 imported comparisons
and checks all its 24 printed adjacent margins against the canonical
table. For fixed k, replacing r=k+1 by any r>k+1 increases the margin
by 4(J_r-J_(k+1))ell>0. The least scaled margin is 12588830833540,
giving exactly 629441541677/50000000000>12.58 after division by S.
The first-displacement argument covers all permutations; the 6600
comparisons are not a sampling claim about permutations or t.

**Literal coefficients and the whole interval.** For fixed j, dividing
n_(i+1)=c_i(n_i+eta_i) by C_(i+1)=c_i C_i gives normalized increment
eta_i/C_i. Thus n_25=C_25(n_0+B). Since C_25=1/(1+D), with D>0,
closure uniquely forces n_0=B/D. Every C_i, eta_i and B is positive,
so all defined inputs are positive and their logarithms exist. This is
only the formal affine fixed point, without a realization assertion.

The reference t=0 retains the actual fixed recipient j. Increasing t
changes no prefix C_i for i<=23, multiplies C_24 by x=2^(-18t),
and leaves C_25 unchanged. This follows directly from the two tail
coefficients +18 and -18, whose effects cancel only after the closing
row. The independently reconstructed exponent coefficients are zero
through prefix 23, +18 at prefix 24 and zero at prefix 25 for all j.
Writing A=sum_(i<24)eta_i/C_i(0) and C=C_24(0), substitution gives

\[
n_{24}=Cx\left(\frac{A+\eta_{24}/(Cx)}D+A\right)
       =\frac{\eta_{24}}D+\frac{CA(1+D)}D x.
\]

Both coefficients are strictly positive. Therefore n_24, s_24 and
its logarithmic guard margin strictly decrease with increasing t.
No growth assumption about either varying row is used here. The same
identity includes t=9250244, where a_24=2; a_23=166504394 there.
All intervening tails remain at least 2 by their displayed affine
formulas. The reference t=0 defines coefficients only and is not used
as a feasible tuple or an additional admitted parameter.

**Uniform boundary including j=0.** At t=1, the first 24 tails are
all at most 20, including both recipient j and row 23. The exact
comparisons 3^64/2^92>10^8/2^18>2 and 3^117/2^152>2 were
independently verified. Monotonicity in J,H with bases 27/16 and 3/2
greater than one justifies the second comparison for rows 1,...,23;
the first comparison explicitly covers the weakened row zero. Hence
C_i>(10^8/2^18)2^(i-1) for 1<=i<=24. Bounding each eta by 23/11
and summing the finite reciprocal-prefix geometric series gives exactly
B(1)<9031479/4296875. At every i<=24, the positive partial sum is
less than B, C_i>=1, and D>Lambda>lambda_-. Thus

\[
s_i/C_i=n_0+\sum_{r<i}\eta_r/C_r+23/(11C_i)
 <B_+/\lambda_-+B_++23/11
 =37631162507944991614/1894921875<20\cdot10^9.
\]

The independent exponential sum at 24 exceeds 20*10^9, proving
log s_24(1)<24+log C_24(1). This estimate uses boundary growth only.
Direct summation for every recipient gives p=271907921, q=306970784
and q+4J_24=430963900. The four signed integer operands in (11) are

\[
24000000000000,\quad 298721383397039647149,\quad
-298721412207710820100,\quad 1011600911679.
\]

Their sum divided by S is -474883782659/125000000000<-3.79.
The signs call for an upper bound on log3 and log(11/4), and a lower
bound on log2, exactly as used. Strict boundary rejection combined
with the positive-coefficient formula excludes every admitted t. A
single strictly failed non-strict guard suffices; no assertion about
H/seed guards or other literal guard margins is needed.

**Independent evidence and verdict.** Run
`python3 scripts/postspell-word-count/audit_earlier_recipient.py`.
It imports or executes no construction program. The full evidence is
`scripts/postspell-word-count/earlier-recipient-audit-certificate.json`,
including the preserved construction certificate's SHA256. The audit
separately transcribes L055's table, directly sums all changed prefixes,
and compares every stored boundary table, prefix exponent, t-coefficient,
pair operand, guard operand, rational check and table check. All 112
audit checks pass, including complete equality of all 22 supports' 6600
pair records and the 31 original rational comparisons; no failure occurred.

The independent logarithms use the already assessed DLMF 4.6.4 method:
for z=2,3,11/4 and x=(z-1)/(z+1), use
P=2 sum_(v=0)^159 x^(2v+1)/(2v+1) and
R=2x^321/(321(1-x^2)). Here 0<x<=1/2. The positive remainder
2 integral_0^x u^320/(1-u^2) du is strictly less than R, so
P<log z<P+R. Every term and remainder is exact rational and saved.
The signed endpoints N P_2-K(P_3+R_3) and
N(P_2+R_2)-K P_3 enclose Lambda and verify its cancellation-sensitive
bound independently of the construction's imported grid constants.

The complete rational comparison records, weakest-pair operands,
uniform root bounds, boundary guard operands, boundary-zero tail tables,
and full recipient-21 reference-prefix table were inspected. The program
checks all remaining records in full, not through previews. The symbolic
arguments above establish the entire order/parameter coverage and the
coefficient signs; arithmetic pass flags alone do not establish them.

No hypothesis, conclusion or direct mathematical dependency changed.
The L051 conventions, L055 table/count/log bounds, L064 coarse boundary
method, L070 root method and L071 comparisons are used only as described,
with their changed-support applicability checked here. L041 and every
actual-word application remain outside this audit. No H/seed, minimum
location, integer, parity, exact-valuation or primitive/count-ray premise
was added. Other allocations and universal eventual descent remain open;
full matching Mathlib coverage remains unchecked.

## Mathlib

Full matching coverage for this finite-table all-order exclusion is
unchecked. Supporting finite-product, rational, logarithm and exponential
facts are used informally; no matching Mathlib theorem or Lean build is
claimed. Unknown coverage is not evidence of absence.
