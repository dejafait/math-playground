# L095 — The two literal d34 endpoint roots fail row18's H guard

## Hypotheses

Take L055's 25 indexed pairs in literal order, changing only
H_0=6 and H_24=32670655. Fix B=9250245, kappa=23/11 and
t in {0,1}. Set a_i=2 for 0<=i<=22, a_23=2+18t and
a_24=2+18(B-t). Consider real s_0,...,s_25 with s_25=s_0
and every endpoint, including closure,

\[
s_{i+1}=2^{-a_i}\left((27/16)^{J_i}(3/2)^{H_i}s_i
              -(12/11)(3/2)^{H_i}-1\right)+\kappa.
\tag{1}
\]

No J/H guard, lower-domain condition, minimum, seed, integer junction,
parity, residue, exact valuation, primitive count or actual-word
realization is assumed. All logarithms are natural.

## Conclusion

For each specified t there is exactly one real cyclic endpoint tuple.
It is positive rational, every n_i=s_i-kappa exceeds 47, and

\[
\log s_{18}+693015\log(27/16)-3295208\log2
<-\frac{1338950347341}{100000000000}<0.
\tag{2}
\]

Thus both specified roots fail their own outgoing row18 strict H guard.
This excludes these two roots only. It supplies no d34 allocation/order
reduction, cutoff for other parameters, integer-cycle exclusion or
actual-word transfer. Universal eventual descent remains unresolved.

This is local RESEARCH/REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-10-23-d34-literal-two-root-h-test.md`. The new
local certificate specializes existing affine and normalized-cap proof
cases; no new general theorem beyond the inspected sources is claimed.
The separate step-418 critical audit below found no defect. Attempt 032 and both original d0
rational witnesses remain unchanged.

## Proof

### Independent endpoint hypotheses and imported inputs

The table has strictly increasing J_i>=8 and H_i>=6. Both allocations
match L077's last-pair definitions exactly. The changed H entries sum
to their original sum, and direct summation gives

\[
K=397573379,\quad N=630138897,\quad
0<\lambda_-:=10584/10^{14}<\Lambda=N\log2-K\log3
<\lambda_+:=10585/10^{14}<1.
\tag{3}
\]

L084's completed all-member analytic audit already covers these
enclosures at d34, independently of its failed full sufficient-test
package. The present certificate also recomputes them. At t=0 the last
tails are (2,166504412); at t=1 they are (20,166504394). Each full
tail list sums to 166504460. Both changing tails, including the closing
tail, occur in N and the full cyclic multiplier.

Use only the independent endpoint conclusion and proof of L077
(3),(7)–(10). Define

\[
c_i(t)=3^{3J_i+H_i}/2^{4J_i+H_i+a_i(t)},\quad
C_i(t)=\prod_{j<i}c_j(t),\quad C_0=1,
\]
\[
\eta_i=\kappa-(16/27)^{J_i}(12/11+(2/3)^{H_i}),\qquad
D=\exp(\Lambda)-1>\Lambda>\lambda_->0.
\]

The eta bounds required by L077 hold: 0<eta_i<kappa for all rows,
and the exact eta_0 at (J,H)=(8,6) exceeds 2. Since J_24>=J_0 and
H_24>=H_0, monotonicity of the subtracted powers gives
eta_24>=eta_0>2. Finally
2(1-lambda_+)/lambda_+=39999999995766/2117>47.
Thus L077 (3) applies with e=2, without its boundary rejection tests
or any O/S tests. It supplies the unique real endpoint tuple and

\[
S(t)=\sum_{j=0}^{24}\frac{\eta_j}{C_j(t)},\quad
n_0=S(t)/D,\quad
n_i=C_i(t)\left(S(t)/D+\sum_{j<i}\eta_j/C_j(t)\right),
\quad n_i=s_i-\kappa.
\tag{4}
\]

All coefficients are rational and the fixed-point denominator is
nonzero; hence the unique tuple is rational and positive. L077 also
gives n_i>47 at every input. Its unchanged tail-2 prefixes handle
i<=23, while its separate positive-coefficient final-input formula
gives n_24>eta_24/D>47. No growth of a varying row or minimum
location is assumed. In particular every logarithm used below exists.
The closing multiplier C_25=exp(-Lambda)<1 stays in D; it is not
an incoming lower-bound premise.

The formal finite-word affine input is imported from Halbeisen–
Hungerbuehler, *Optimal bounds for the length of rational Collatz
cycles*, Acta Arithmetica 78 (1997), 227–239, DOI
10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
as already specialized in L077. The integer row exponents specify a
finite nonempty formal word and (3) supplies its nonzero denominator.
No coding reproof or integer-parity realization converse is used.
The assessed positive-real analytic inputs are
[DLMF 4.5.1](https://dlmf.nist.gov/4.5.E1),
[4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.2.19](https://dlmf.nist.gov/4.2.E19); the positive arguments here
are in their assessed domains. Apply their existing rational remainder
scheme, rather than reprove an analytic theorem.

### Replacement normalized-input cap

L083's full theorem cannot be invoked: its O/S/C conjunction fails
at d34, as L084 and Attempt 032 record. Instead specialize only its
earlier fixed-root cap/margin proof cases (6)–(9), with (4) justified
independently above. The two fixed parameters need no reduction from
a larger allocation family.

Use the incoming data of L084's H package at m=1:

\[
w=10^8(2/3)^{33},\quad L_0=1,\quad
L_i=w2^{i-1}\quad(1\le i\le24),\quad L_*:=\min_iL_i=1.
\tag{5}
\]

Here w>1, and row0 has c_0=3^30/2^40>w. All rows1–23 have
unchanged J>=15,H>=72 and actual tail at most 20. L084's audited
weaker tail-38 comparison c_i>=3^117/2^170>2 therefore applies;
the present certificate also checks each actual log(c_i/2)>0 at both
parameters using its complete exponents. Induction gives
C_i(1)>=L_i for all incoming indices0–24. For i<=23 the incoming
prefix is independent of t, while C_24(t)=C_24(0)2^(-18t).
Consequently C_i(t)>=L_i at both roots. This uses no lower bound
on C_25 and retains row23's tail20 when t=1.

Retain the complete finite reciprocal sum, rather than replacing it
by a truncated prefix or importing C's different last denominator:

\[
Q=\kappa\sum_{i=0}^{24}\frac1{L_i}
=\kappa\left(1+\frac2w(1-2^{-24})\right),
\]
\[
R_H=Q/\lambda_-+Q+\kappa/L_*
=\frac{419693935179938468251189621018264434581}
{20973083320679305052160000000}.
\tag{6}
\]

Exact rational comparisons give

\[
20011074612<R_H<20011074613<
U:=21000000000<P_{40}(24)<\exp(24),
\tag{7}
\]

where P_40(24)=sum_(k=0)^40 24^k/k! has floor 26462988572.
Its positive omitted terms justify the strict exponential comparison.
Thus the replacement pair is U=21000000000,T=24. The old U=20*10^9
still fails; a new logarithmic threshold is unnecessary because the
new U remains below exp(24). This changes neither the old failed
full package nor any other table's constants.

By eta_j<kappa and the complete incoming bounds, 0<S(t)<Q.
Every proper partial sum in (4), including the empty one, is
nonnegative and strictly below Q. Since D>lambda_-, for each
incoming i=0,...,24,

\[
0<\frac{s_i}{C_i(t)}
=\frac{S(t)}D+\sum_{j<i}\frac{\eta_j}{C_j(t)}
                      +\frac{\kappa}{C_i(t)}
<Q/\lambda_-+Q+\kappa/L_*<\exp(24).
\tag{8}
\]

Every denominator is positive. Hence log s_i<24+log C_i(t).
No J/H guard, seed or minimum premise entered the cap.

### Own-input row18 and complete analytic error

Direct summation of the changed prefix at either t gives

\[
A_{18}=\sum_{j<18}(3J_j+H_j)=6078890,\qquad
D_{18}=\sum_{j<18}(4J_j+H_j+a_j)=6862807.
\]

This prefix is independent of t because both varying rows come later.
Its outgoing pair stays J_18=693015,H_18=3295208. Put
P=A_18+3J_18=8157935 and R=D_18+4J_18+H_18=12930075.
Use the independently certified bounds
ell=693147180559/10^12<log2 and log3<u=1098612288669/10^12.
Both P,R are positive, so (8) implies

\[
\begin{aligned}
\log s_{18}+J_{18}\log(27/16)-H_{18}\log2
&<24+P\log3-R\log2\\
&<24+Pu-R\ell
=-1338950347341/100000000000<0.
\end{aligned}
\tag{9}
\]

The row18 coefficients and the rational upper expression are freshly
computed here; L093's d<=33 conclusion is not a premise at d34.
Both roots therefore fail this strict H guard, whether or not any
other guard holds. This does not assert that these roots exhaust any
larger feasible d34 family.

For explicit error control, the certificate uses the already assessed
100-term positive logarithm sum, for x=2,3 and z=(x-1)/(x+1),
with upper remainder 2z^201/[201(1-z^2)]. Let [l_2,h_2] and
[l_3,h_3] be these outward intervals. It checks (3) using
[N l_2-K h_3,N h_2-K l_3], retaining both amplified remainders.
For row18 the excess of the rational upper expression over
24+P log3-R log2 is exactly

\[
E=P(u-\log3)+R(\log2-\ell),
\]

and the complete rational interval retained on disk satisfies

\[
0<P(u-h_3)+R(l_2-\ell)<E
<P(u-l_3)+R(h_2-\ell)<1/50000.
\tag{10}
\]

Thus no large coefficient or truncation error is dropped in (9).
The expression interval in the certificate bounds 24+P log3-R log2;
it is not claimed to enclose the actual root margin from both sides.

Reproduce with
`python3 scripts/postspell-word-count/certify_d34_two_root_h.py`.
The full certificate is
`scripts/postspell-word-count/d34-two-root-h-certificate.json`.
It retains the source table/hash, exact changed table, all analytic
terms/remainders, all 25 incoming bounds and reciprocal terms, both
complete allocations and closing exponents, all 46 actual nonzero-row
factor intervals, row18 coefficients/errors and every comparison's
operands and difference. All 368 comparisons pass. This construction
supports the specialization; its separate independent audit is recorded
below. No other row's H guard or other d value is tested.

### Independent critical audit — 2026-10-23, step 418

This RESEARCH/REPRODUCTION proof audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-23-d34-two-root-h-critical-audit.md`.
It finds no defect within the exact two-root scope. This validates an
existing local input, without adding an exclusion or claiming progress
beyond the inspected affine/analytic sources. Universal eventual descent
remains unresolved. The relevant continuation test was to correct or narrow
the result on any missing premise, invalid enclosure or incorrect sign;
none was found in the proof or complete evidence checked here.

**Endpoint proof cases and exact scope.** The canonical L055 table was
parsed afresh, subtracting 34 from H_0 and adding 34 to H_24; all other
pairs match. Both complete allocations have their stated closing tails,
integer exponents, total tail 166504460, K=397573379 and N=630138897.
No old d<=33 verdict or failed full C077a conjunction is an input.

Substituting s=n+kappa in (1) gives precisely
n_(i+1)=c_i(n_i+eta_i). Dividing this equation by C_(i+1)=c_i C_i
shows that its additive term is eta_i/C_i, not eta_i/C_(i+1).
After all 25 equations, n_25/C_25=n_0+S. Since n_25=n_0 and
C_25=exp(-Lambda), this gives (4) with D=exp(Lambda)-1.
The positive Lambda enclosure certifies a nonzero denominator, so
uniqueness is among all real solutions. The formulas solve every edge
and closure and are rational with strictly positive coefficients.

The exact eta_0 comparison passes with e=2. Every table row has
J_i>=8,H_i>=6; the two subtracted powers decrease as either parameter
increases, giving eta_i>=eta_0>2, in particular at row24, while
eta_i<kappa. This is stronger than the two endpoint eta premises needed
from L077. Its independent endpoint proof needs (3), not its boundary
cutoff tests (4)–(5). For unchanged rows0–22 the actual tail is 2,
so their factors exceed 2 and each of n_1,...,n_23 exceeds n_0>47.
For the last input L077's separate formula is

\[
n_{24}=\eta_{24}/D+C_{24}(0)A(1+D)2^{-18t}/D,
\qquad A=\sum_{j<24}\eta_j/C_j(0)>0.
\]

It gives n_24>eta_24/D>47 independently of growth in row23.
The strict upper bound D<lambda_+/(1-lambda_+) gives exactly the
domain lower bound printed in the proof. The closing edge repeats n_0.
Thus every logarithm exists without a guard, seed or minimum premise.
These checks specialize the already cited finite affine formulas; they
do not reprove a coding theorem or invoke a realization converse.

**All incoming factors, complete sum and changed cap.** Exact arithmetic
verifies c_0>w>1, and fresh outward logarithmic intervals verify
log(c_i/2)>0 for each of rows1–23 at each of t=0,1: all 46 comparisons,
including row23 with tail20. The weaker common tail38 comparison quoted
from L084 is also verified exactly. Induction therefore covers every
incoming index0–24 by the stated L_i. The exponent arrays independently
confirm that only incoming C_24 changes, by 2^(-18t). Neither incoming
bound discards the change in the closing tail: the complete exponents
at index25 still give K,N. No C_25>=1 premise is introduced.

All 25 reciprocals are retained. Their direct sum agrees with
1+(2/w)(1-2^(-24)), and the actual minimum bound is L_*=1.
The recomputed R_H agrees with (6) exactly and lies strictly between
20011074612 and 20011074613. Consequently the old U=20000000000
still fails, and the new U=21000000000 succeeds. Independently generating
t_0=1,t_k=24t_(k-1)/k gives all 41 positive exponential terms and

\[
P_{40}(24)=
\frac{202750314819830504045671593478515759301}
{7661655986496068058455078125}>21000000000.
\]

The omitted positive terms give P_40(24)<exp(24). Thus retaining T=24
is justified after changing U. With positive eta_i<kappa and D>lambda_-,
both complete S and every proper partial sum are strictly below Q.
This checks every inequality in (8), including i=0 and i=24, and proves
the normalized cap without assuming feasible J or H guards. L083's
early cap/margin proof is applicable here on its independently verified
premises; its later all-order conclusion is not invoked.

**Row18, signs and full analytic errors.** Both fresh prefix sums give
A_18=6078890,D_18=6862807. The varying rows are later, and the own
outgoing pair remains (693015,3295208). Thus P=8157935,R=12930075
are positive. Using an upper log3 and a lower log2 in T+P log3-R log2
is the correct outward direction. Every logarithm term and remainder
in the construction was regenerated by successive powers; all amplified
Lambda and row18 errors match. The complete error interval in (10) is
strictly positive and has upper endpoint below 1/50000. The rational
upper expression agrees exactly with (2) for both roots and is negative.
Its strict domination of the actual root margin follows from (8), not
from numerical evaluation of a root.

As a second analytic evaluation, independent 120-term intervals [a,b]
for log2 and [c,d] for log(3/2) give

\[
(N-K)a-Kd<\Lambda<(N-K)b-Kc,
\]
\[
24+Pc+(P-R)b<24+P\log3-R\log2
<24+Pd+(P-R)a.
\]

Here N-K=232565518>0 and P-R=-4772140<0; these signs fix the
outward endpoints. Both new intervals lie strictly inside the original
ones. Subtracting the second interval from the rational upper expression
again gives a positive error strictly below 1/50000, with no omitted
coefficient or remainder. This interval encloses the logarithmic upper
expression, not the actual root margin from both sides. The analytic
series are imported from the precise DLMF citations above in their
assessed positive-real domains; no fresh external theorem is required.

**Independent evidence and limitations.** Run
`python3 scripts/postspell-word-count/audit_d34_two_root_h.py`.
It neither imports nor executes the constructor. The full exact report is
`scripts/postspell-word-count/d34-two-root-h-audit-certificate.json`.
It reconstructs and compares every non-check record of the construction
certificate, including all arrays and their lengths, and separately
replays all 368 recorded comparisons and differences. All 2070 audit
comparisons pass. Full regenerated records, alternative analytic terms
and intervals, both allocations, all incoming bounds, the complete
reciprocal sum, amplified errors, operands and differences are retained
and checked programmatically, not accepted from success flags. The exact
R_H, full exponential lower sum, complete selected second-evaluation
row18 interval/error, summary and empty failure list were also inspected.

One negative own-input H margin rejects each endpoint root. It does not
establish that these are all feasible d34 parameters or orders, nor does
it invoke an integer-cycle theorem on real junctions. No other d value
or H row is tested. Allocation exhaustion, cyclic order, cutoff for
other parameters and actual-word transfer remain independent unresolved
steps. Attempt 032, L084's failed old caps and both original d0 witnesses
are preserved. The direct mathematical inputs and argument are unchanged;
DAG.md and PROOF.md are therefore not edited for audit status alone.
This canonical audit supersedes their older pending-audit prose for L095.

## Mathlib

Full matching coverage for this changed-cap two-root specialization has
not been checked. Supporting affine, finite-sum, real logarithm and
exponential facts are not a full matching theorem. Unknown coverage is
not evidence of absence. No Lean verification is claimed.
