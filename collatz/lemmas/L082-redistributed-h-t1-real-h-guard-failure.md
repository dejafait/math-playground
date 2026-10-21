# L082 — Redistributed-H t=1 root fails its own-input H guard

## Hypotheses

Use L055's complete indexed 25-row pair table, changing only H_0=39
and H_24=32670622 as specified in L079. Keep literal order and set
a_i=2 for 0<=i<23, a_23=20 and a_24=166504394. Test exactly L051
(1)–(4), with natural logarithms. No feasible tuple, minimum location,
integer/parity/valuation realization or primitive orbit is assumed.
Only this fixed allocation (t=1) is considered.

Put kappa=23/11 and define the exact factored rational quantities

\[
c_i=\frac{3^{3J_i+H_i}}{2^{4J_i+H_i+a_i}},\quad
\eta_i=\kappa-\frac{12}{11}(16/27)^{J_i}
                    -(16/27)^{J_i}(2/3)^{H_i},\quad
C_i=\prod_{j<i}c_j,\quad C_0=1,
\]
\[
R=\sum_{i=0}^{24}\frac{\eta_i}{C_i},\quad
n_0=\frac{R}{2^N/3^K-1},\quad
n_i=C_i\left(n_0+\sum_{j<i}\frac{\eta_j}{C_j}\right),\quad
s_i=n_i+\kappa,\quad h_i=\log s_i.                 \tag{1}
\]

Denominator positivity and uniqueness are proved below, rather than
assumed as feasibility premises.

## Conclusion

The unique cyclic endpoint root (1) violates L051's own-input strict
H guard at row 18. With J_18=693015 and H_18=3295208,

\[
h_{18}+J_{18}\log(27/16)-H_{18}\log2
< -\frac{457745289}{50000000000}<0,                 \tag{2}
\]

where the required margin is strictly positive. Hence this fixed
ordered tuple has no solution to the full L051 (1)–(4) system.
Other guards need not be classified after one necessary failure.

This is local REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-10-18-redistributed-h-t1-real-feasibility.md`,
not a new general theorem beyond the inspected affine/analytic machinery.
The separate critical audit below found no defect in this single-root
exclusion. Both original rational witnesses,
L081's separate t=0 exclusion, the independent arithmetic and actual-word
exclusions, and Attempts 026–031 remain valid. No other allocation,
order or table is tested; universal eventual descent remains unresolved.

## Proof

### Exact root and complete closing product

Fresh summation of all rows, including both transferred tails, gives

\[
\sum J_i=66061058,\quad \sum H_i=199390205,
\quad\sum a_i=166504460,
\quad K=397573379,\quad L=232565518,\quad N=630138897. \tag{3}
\]

Every J_i>=2, H_i>=3 and a_i>=2, with a_i=2 modulo 18.
The numerical scaling choice d=1, K_0=K>225640000 and L_0=L>0
meets the explicit real-system count conditions. Exact rational
comparison gives N<(8/5)K+1725/1034. This asserts no primitive orbit.
The analytic certificate below freshly checks

\[
0<\lambda_-:=10584/10^{14}<\Lambda=N\log2-K\log3
<10585/10^{14}=: \lambda_+<1.                       \tag{4}
\]

Since both bases in eta_i's subtractions are between 0 and 1,
the sum subtracted is strictly between 0 and 12/11+1=kappa.
Thus 0<eta_i<kappa, all C_i>0 and R>0. The denominator in (1)
is exp(Lambda)-1>0, so all n_i and s_i are positive before logarithms.
The finite formula gives n_(i+1)=c_i(n_i+eta_i). Substituting
s_i=n_i+kappa and the displayed eta_i gives precisely L051 (4).
The totals (3) give C_25=3^K/2^N, including a_24=166504394.
Thus n_25=C_25(n_0+R)=n_0 by (1), proving exact closure.
Conversely closure of this affine recurrence forces
n_0=C_25(n_0+R); since 1-C_25>0, this root is unique.

The imported finite-word fixed-point identity is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Its nonempty finite formal word here has N letters and K odd letters;
(4) checks the nonzero denominator. The algebra above is the necessary
shifted-block specialization, without reproving general parity coding
or importing an integer-realization converse. Neither arithmetic
nonintegrality nor an actual-word exclusion is a premise here.

### Fresh bound including the tail-20 row

Row 0 has c_0=3^63/2^73>10^8 by exact integer comparison.
Rows 1 through 22 have tail 2, so the parameter floors imply

\[
c_i\ge(27/16)^2(3/2)^3/4=19683/8192>2.
\]

Row 23 instead has tail 20. Its actual parameters satisfy J_23>=8
and H_23>=39. As both bases exceed 1, they give the fresh bound

\[
c_{23}\ge(27/16)^8(3/2)^{39}/2^{20}
=3^{63}/2^{91}>2.                                \tag{5}
\]

No tail-2 bound is imposed on this changed row. Consequently
C_i>10^8*2^(i-1) for 1<=i<=24, and C_i>=1 for all input indices
0<=i<=24. This does not assert C_25>=1. Keeping every term of R,
the finite inverse-prefix sum gives

\[
0<R<\kappa\left(1+\frac{2}{10^8}\right)
=\frac{1150000023}{550000000}=:R_+.
\]

Here sum_(j=0)^23 2^(-j)<2; the tail transfer affects C_24 but (5)
still proves its stated lower bound. Since exp(Lambda)-1>Lambda>
lambda_-, for each input index 0<=i<=24 we obtain

\[
\frac{s_i}{C_i}
=n_0+\sum_{j<i}\frac{\eta_j}{C_j}+\frac{\kappa}{C_i}
<\frac{R_+}{\lambda_-}+R_++\kappa
=\frac{435606069410390910013}{22050000000}
<20000000000<e^{24}.                              \tag{6}
\]

The last inequality follows from the exact rational comparison
20000000000<sum_(k=0)^40 24^k/k!<exp(24). Therefore
h_i<24+log C_i for every needed input. This is a fresh root bound
with both changed tails retained, not an inherited t=0 witness bound.
No domain, minimum, seed or individual guard has been assumed.

### The necessary own-input failure

Directly summing rows 0 through 17 of this table gives
C_18=3^6078923/2^6862840. The decreased H_0 is included;
neither transferred tail nor increased H_24 belongs to this prefix.
Combining (6) with row 18's own J and H yields

\[
\begin{aligned}
h_{18}+J_{18}\log(27/16)-H_{18}\log2
&<24+(6078923+3\cdot693015)\log3\\
&\quad-(6862840+4\cdot693015+3295208)\log2\\
&=24+8157968\log3-12930108\log2.
\end{aligned}
\]

The certified bounds log3<1098612288669/10^12 and
log2>693147180559/10^12, with these coefficient signs, give

\[
24+8157968\log3-12930108\log2
<\frac{24000000000000+8157968\cdot1098612288669
                -12930108\cdot693147180559}{10^{12}}
=-\frac{457745289}{50000000000}<0.
\]

This proves (2). Every endpoint solution is the unique root already
bounded, so one failed necessary H guard excludes the full system.
The identical rational upper margin in L081 is a comparison only:
the t=1 closing product and incoming growth were recomputed here.

### Exact analytic certificate and verification scope

Reuse the already assessed L055/L079 analytic method based on
[DLMF 4.6.4](https://dlmf.nist.gov/4.6.E4),
[4.5.1](https://dlmf.nist.gov/4.5.E1) and
[4.2.19](https://dlmf.nist.gov/4.2.E19), recorded version 1.2.8
(2026-09-15). For x=2,3 set z=(x-1)/(x+1), m=100 and

\[
A(x)=2\sum_{k=0}^{99}\frac{z^{2k+1}}{2k+1},\quad
E(x)=\frac{2z^{201}}{201(1-z^2)},\quad U(x)=A(x)+E(x).
\]

The existing positive-tail remainder bound gives A(x)<log x<U(x)
for these 0<z<=1/2. The certificate checks
lambda_-<N A(2)-K U(3) and N U(2)-K A(3)<lambda_+;
all large-coefficient errors are retained. It also checks the outward
10^12 grid bounds used above and the full exponential partial sum.
No floating-point estimates enter a proof inequality.

Reproduce with
`python3 scripts/postspell-word-count/certify_redistributed_h_t1_real_feasibility.py`.
The complete exact rows, prefixes, logarithm terms/remainders, root
bounds, exponential terms, operands and comparison differences are in
`scripts/postspell-word-count/redistributed-h-t1-real-feasibility-certificate.json`.
All 153 certification checks pass; the mathematical failure is the H
guard, distinct from a failed certification check. The complete selected
root, failed-guard and parameter fields were inspected, including the
changed C_24 exponents (271907920,306970765). This verification is not
a separate critical audit. Integer-cycle lower bounds are not applied
to arbitrary real junctions. No other guards or parameters are decided.

### Independent critical audit — 2026-10-18, step 325

The prior SPECIALIZE assessment
`drafts/literature/2026-10-18-redistributed-h-t1-failure-critical-audit.md`
covers this audit only. The audit imports the cited finite affine identity
and positive-real analytic machinery, checking this changed-tail
specialization rather than reproving general parity coding. No defect
was found. This is local REPRODUCTION and independent validation of the
existing exclusion, not a new theorem beyond the inspected sources.

L051 (1)–(4) was inspected in full. Its H condition is strictly
H_i log2<h_i+J_i log(27/16) at each outgoing input. A failed condition
at input 18 suffices irrespective of the domain, designated minimum,
seed or other guards. L055's full indexed table was transcribed
independently and compared row by row; only the two H entries specified
by L079 were replaced. Both transferred tails were retained.

To check the coordinate substitution explicitly, write
Q_i=(12/11)(3/2)^{H_i}+1. Then
G_i eta_i=kappa G_i-Q_i, so
c_i(n_i+eta_i)+kappa
=2^{-a_i}(G_i s_i-Q_i)+kappa, exactly L051 (4).
Division by C_{i+1}=c_i C_i gives
n_{i+1}/C_{i+1}=n_i/C_i+eta_i/C_i, explaining every term in R.
The complete exponent sums give (K,N)=(397573379,630138897),
so C_25=exp(-Lambda), including the closing tail 166504394.
Positive eta and independently certified Lambda>0 imply R>0,
1-C_25>0, and the unique cyclic fixed point
n_0=C_25 R/(1-C_25)=R/(exp(Lambda)-1)>0.
Consequently every displayed n_i and s_i is positive before taking logs.
This proves uniqueness even without assuming a putative tuple is feasible.

The incoming estimates were checked separately: c_0=3^63/2^73>10^8;
rows 1,...,22 have c_i>=19683/8192>2; row23 has its actual tail 20
and J_23>=8, H_23>=39, giving c_23>=3^63/2^91>2.
Thus C_i>10^8 2^{i-1} for 1<=i<=24. The 24 nonzero-index
terms of R are all covered by the finite sum of 2^{-j}, 0<=j<=23.
Together with eta_i<kappa, this proves R<R_+ without omitting input24.
C_i>=1 is used only for inputs 0,...,24; it is false for C_25 and
is not used there. Since exp(Lambda)-1>Lambda>lambda_-, each
s_i/C_i is strictly below R_+/lambda_-+R_++kappa. Exact reconstruction
confirms the fraction in (6) and its strict comparison with 20*10^9.
All 41 positive terms of the exp(24) lower sum were independently
generated by the recurrence t_{k+1}=24t_k/(k+1), proving the last
comparison in (6). Hence h_i<24+log C_i at every needed input.

The first 18 rows were independently summed, giving precisely
(6078923,6862840) for the exponents of C_18. Its row18 own-input
parameters are (693015,3295208), giving coefficients
A=8157968>0 and D=12930108>0 in 24+A log3-D log2.
Neither transferred tail is in this prefix; both remain in the root's
closing product. The rational grid substitutions use the upper bound
for log3 and the lower bound for log2, with no reversed error sign.
Their exact resulting upper margin is -457745289/50000000000<0.

The independent script
`scripts/postspell-word-count/audit_redistributed_h_t1_real_failure.py`
does not import or run the original calculation script. It reconstructs
every parameter, input prefix, count, root-bound number, logarithm term,
remainder, exponential term, failed-guard field, and all 153 comparison
operands, signs and differences in the original disk certificate.
All 193 audit checks pass. It additionally generates 120-term logarithm
bounds by an odd-power recurrence. For each b=2,3 their positive omitted
tail is strictly below 2z^241/(241(1-z^2)), z=(b-1)/(b+1).
These are the same cited series and previously justified tail estimate,
at higher truncation order, not a new analytic lemma.

Writing these new lower and upper bounds as l_b,u_b, the independent
comparisons verify
lambda_-<N l_2-K u_3<N u_2-K l_3<lambda_+ and
24+A u_3-D l_2<-457745289/50000000000.
The full amplified widths N(u_2-l_2)+K(u_3-l_3) and
A(u_3-l_3)+D(u_2-l_2), all terms and exact operands are retained in
`scripts/postspell-word-count/redistributed-h-t1-critical-audit-certificate.json`.
Thus neither close cancellation nor an unexamined success flag is used
as proof. Reproduce with
`python3 scripts/postspell-word-count/audit_redistributed_h_t1_real_failure.py`.

The audit uses no t=0 root bound, old witness margin, arithmetic
nonintegrality or integer-cycle theorem on real junctions. L081 is
comparison only; the repeated rational upper margin is explained by
the common row18 prefix and separately verified normalized cap.
The unchanged-table witness in Attempt 026 and the different-order
failure in Attempt 031 do not conflict with these hypotheses; the
recorded comparisons of Attempts 027–030 remain applicable. Both
original witnesses are preserved. No other guard, allocation, order,
table, integer/parity/exact-valuation realization or primitive orbit is
decided. Universal eventual descent remains unresolved. Direct inputs
remain L051, L055 and L079; the ID-only DAG needs no change.

## Mathlib

Full matching coverage for this exact fixed-table real-system exclusion
has not been checked; this is not evidence of absence. The cited finite
affine and positive-real analytic identities support the informal proof.
No Lean build or formal verification is claimed.
