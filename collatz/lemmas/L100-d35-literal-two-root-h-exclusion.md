# L100 — The two literal d35 endpoint roots fail row18's H guard

## Hypotheses

Take L055's 25 indexed pairs in literal order, changing only H_0=5
and H_24=32670656. Let B=9250245, kappa=23/11 and t in {0,1}.
Set a_i=2 for 0<=i<=22, a_23=2+18t and a_24=2+18(B-t).
Consider real s_0,...,s_25 satisfying s_25=s_0 and every endpoint,
including closure,

\[
s_{i+1}=2^{-a_i}\left((27/16)^{J_i}(3/2)^{H_i}s_i
                  -(12/11)(3/2)^{H_i}-1\right)+\kappa.
\tag{1}
\]

No guard, lower domain, minimum, seed, integer junction, parity, residue,
exact valuation, primitive count or actual-word realization is assumed.
All logarithms are natural.

## Conclusion

Each specified t has exactly one real cyclic endpoint tuple. It is
positive rational, every n_i=s_i-kappa exceeds 47, and

\[
\log s_{18}+693015\log(27/16)-3295208\log2
<-\frac{172437107269}{12500000000}<0.
\tag{2}
\]

Thus each root fails its own outgoing row18 strict H guard. This tests
only these two fixed roots; it supplies no d35 allocation/order
reduction, cutoff at other parameters, assembly or actual-word transfer.
Universal eventual descent remains unresolved.

This is a local RESEARCH/REPRODUCTION specialization under the prior
SPECIALIZE assessment
`drafts/literature/2026-10-24-d35-literal-two-root-h-test.md`.
It claims no new general result beyond the inspected affine/analytic
sources. The separate step454 audit below found no defect. Attempt032, the failed
full sufficient-test package and both original d0 witnesses remain valid.

## Proof

### Independent endpoint premises

Only H_0 and H_24 change, by opposite amounts. The table retains
strictly increasing J_i>=8 and H_i>=5. Direct sums give

\[
K=397573379,\quad N=630138897,\quad
0<\lambda_-:=10584/10^{14}<\Lambda=N\log2-K\log3
<\lambda_+:=10585/10^{14}<1.
\tag{3}
\]

The two last-tail pairs are (2,166504412) and (20,166504394), each
with complete tail sum 166504460. Both changing tails occur in N and
the full cyclic product. L084's completed all-member audit covers the
independent analytic and endpoint data at d35; the present certificate
also recomputes (3).

Use only L077 (3) and its independent endpoint proof (7)–(10), with

\[
c_i(t)=3^{3J_i+H_i}/2^{4J_i+H_i+a_i(t)},\quad
C_i(t)=\prod_{j<i}c_j(t),\quad C_0=1,
\]
\[
\eta_i=\kappa-(16/27)^{J_i}(12/11+(2/3)^{H_i}),\qquad
D=\exp(\Lambda)-1>\Lambda>\lambda_->0.
\]

Every eta_i lies strictly between 0 and kappa. More precisely,
monotonicity of the subtracted positive powers and the actual table give

\[
\eta_i\ge\eta_0=142223884206271/68630377364883>2,
\qquad 2(1-\lambda_+)/\lambda_+=39999999995766/2117>47.
\]

Thus L077's independent endpoint hypotheses hold with e=2, without
its cutoff boundary tests or any O/S tests. Its formulas are

\[
S(t)=\sum_{j=0}^{24}\eta_j/C_j(t),\qquad n_0=S(t)/D,
\qquad n_i=C_i(t)\left(S(t)/D+\sum_{j<i}\eta_j/C_j(t)\right).
\tag{4}
\]

The nonzero fixed-point denominator makes this the unique real endpoint
tuple. All coefficients are rational and positive. The unchanged
tail2 rows0–22 have factors at least 19683/8192>2, so L077 gives
n_i>=n_0>47 through i=23. For i=24 its independent formula is
n_24=eta_24/D+C_24(0)A(1+D)2^(-18t)/D, where
A=sum_(j<24)eta_j/C_j(0)>0. Hence n_24>eta_24/D>47 too.
Here D<lambda_+/(1-lambda_+) is L077's strict series comparison.
No growth of a varying row or minimum location is used. Closure repeats
n_0. In particular every logarithm below exists, and all inputs are
positive rationals.

The formal affine input is Halbeisen–Hungerbuehler, *Optimal bounds for
the length of rational Collatz cycles*, Acta Arithmetica 78 (1997),
227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
as already specialized in L077. The integer exponents specify a finite
nonempty formal word; (3) supplies its nonzero denominator. No coding
reproof or integer-parity realization converse is needed. The reused
positive-real analytic inputs are [DLMF 4.5.1](https://dlmf.nist.gov/4.5.E1),
[4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.2.19](https://dlmf.nist.gov/4.2.E19), in the domains recorded by
the prior assessment. All arguments here are positive. The existing
rational remainder scheme is applied without a new analytic theorem.

### Complete incoming sum and replacement cap

L083's full O/S/C-dependent conclusion is unavailable at d35. Specialize
only its early cap/margin proof (6)–(9), after independently licensing
(4). These two specified roots require no reduction from a larger family.

Use L084's H incoming construction at m=1 with

\[
w=10^8(2/3)^{34},\quad L_0=1,\quad L_i=w2^{i-1}\ (1\le i\le24).
\tag{5}
\]

Exact arithmetic gives c_0=3^29/2^39>w>1. Rows1–23 have unchanged
J>=15,H>=72 and actual tails at most20. L084's audited weaker tail38
comparison gives c_i>=3^117/2^170>2. The present certificate additionally
checks all 46 actual log(c_i/2) lower endpoints at the two roots.
Induction gives C_i(1)>=L_i for every incoming i=0,...,24.
Prefixes i<=23 are independent of t; C_24(t)=C_24(0)2^(-18t).
Consequently C_i(t)>=L_i at both roots, including the row23 tail20
at t=1. No lower bound is imposed on C_25=exp(-Lambda)<1; the
closing tail stays in D.

The actual minimum is L_*=1. Retain all 25 reciprocal terms:

\[
Q=\kappa\sum_{i=0}^{24}1/L_i
=\kappa\left(1+\frac2w(1-2^{-24})\right),
\]
\[
R_H=Q/\lambda_-+Q+\kappa/L_*
=\frac{844750639734024151594364496473033303743}
{41946166641358610104320000000}.
\tag{6}
\]

Exact comparisons yield

\[
20138923467<R_H<20138923468<U:=21000000000
<P_{40}(24)<\exp(24),
\tag{7}
\]

where P_40(24)=sum_(k=0)^40 24^k/k! equals
202750314819830504045671593478515759301/
7661655986496068058455078125 and has floor 26462988572.
The exponential series has strictly positive omitted terms.
Thus U=21000000000,T=24 is a certified replacement. The failed
old cap U=20000000000 and all failed full-package tests are preserved.

By eta_j<kappa, (5) and D>lambda_-, the complete S and every proper
partial sum in (4) are nonnegative and strictly below Q. Therefore
for each incoming i=0,...,24,

\[
0<\frac{s_i}{C_i(t)}
=\frac{S(t)}D+\sum_{j<i}\frac{\eta_j}{C_j(t)}+\frac\kappa{C_i(t)}
<Q/\lambda_-+Q+\kappa/L_*<\exp(24).
\tag{8}
\]

Every divisor is positive. This includes the empty partial sum and
the final incoming input. Taking logarithms gives
log s_i<24+log C_i(t), without assuming any guard, seed or minimum.

### Fresh own-input row18 bound and full amplified error

At both parameters the changed incoming prefix gives
A_18=sum_(j<18)(3J_j+H_j)=6078889 and
D_18=sum_(j<18)(4J_j+H_j+a_j)=6862806.
Both varying rows come later, and the outgoing pair remains
(J_18,H_18)=(693015,3295208). Thus P=A_18+3J_18=8157934 and
R=D_18+4J_18+H_18=12930074 are positive.

Use ell=693147180559/10^12<log2 and log3<u=1098612288669/10^12.
Then (8), at the outgoing row's own input, gives

\[
\begin{aligned}
\log s_{18}+J_{18}\log(27/16)-H_{18}\log2
&<24+P\log3-R\log2\\
&<24+Pu-R\ell=-172437107269/12500000000<0.
\end{aligned}
\tag{9}
\]

The certificate uses all 100 positive logarithm terms for x=2,3,
z=(x-1)/(x+1), with upper remainder 2z^201/[201(1-z^2)].
Let their outward intervals be [l_2,h_2],[l_3,h_3]. It verifies
(3) with [N l_2-K h_3,N h_2-K l_3], retaining both amplified
remainders. The complete excess E of the rational expression in (9)
over its logarithmic expression is

\[
E=P(u-\log3)+R(\log2-\ell),\qquad
0<P(u-h_3)+R(l_2-\ell)<E
<P(u-l_3)+R(h_2-\ell)<1/50000.
\tag{10}
\]

All terms and these full rational endpoints are retained and checked;
no large coefficient error is omitted. The stored analytic interval
bounds 24+P log3-R log2, not the actual root margin from both sides.
The strict normalized cap proves that this expression is an upper
bound for the actual margin. One negative necessary H margin excludes
each root regardless of all other guard verdicts. Neither L095's d34
conclusion nor L084's negative bound with its failed cap is a premise.

Run `python3 scripts/postspell-word-count/certify_d35_two_root_h.py`.
The complete rational evidence is
`scripts/postspell-word-count/d35-two-root-h-certificate.json`.
All 424 comparisons pass, with no failures. It stores the L055 source
path/hash, full changed table, both complete allocations and closing
exponents, all 25 incoming bounds and reciprocal terms, all 46 actual
nonzero-row factor intervals, analytic terms/remainders, amplified errors,
and every comparison's operands and difference. The exact cap,
exponential lower sum and both full row18 interval/error records were
also inspected. This construction is not an independent critical audit.

The bounded test succeeds within its exact scope. Early-support,
last-pair cutoff and cyclic-order reduction remain independent d35 gaps;
these two roots are not asserted to exhaust any feasible larger family.
Actual-word transfer and universal eventual descent are not supplied.

### Independent critical audit — 2026-10-24, step454

This RESEARCH/REPRODUCTION proof audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-24-d35-two-root-h-critical-audit.md`.
It found no defect in precisely the two literal d35 endpoint roots.
This secures an existing local input; it supplies no additional exclusion
or mathematical discovery beyond the cited affine/analytic sources.

**Endpoint licensing and closure.** A separate transcription matches all
25 canonical L055 pairs and changes only the two stated H entries. Both
complete tails, (2 repeated 24 times,166504412) and (2 repeated 23 times,
20,166504394), give the stated K,N and tail sum. Increasing J>=8 and
H>=5 give eta_i>=eta_0>2 and eta_i<kappa, including row24, by monotonicity
of the subtracted positive powers. Fresh Lambda enclosures and the domain
bound license precisely L077 (3), independently of cutoff tests (4)–(5),
the full O/S/C conjunction, guards or a minimum/seed premise.

Substituting s_i=n_i+kappa gives n_(i+1)=c_i(n_i+eta_i).
Division by C_(i+1)=c_i C_i gives the summand eta_i/C_i, not
eta_i/C_(i+1). All 25 summands enter closure and C_25=exp(-Lambda)
gives n_0=S/D with D>0. Thus the positive rational tuple is the unique
real solution. The unchanged tail2 rows0–22 have c_i>2, giving
n_0,...,n_23>47. Separately,
n_24=eta_24/D+C_24(0)A(1+D)2^(-18t)/D>eta_24/D>47,
using A>0 and D<lambda_+/(1-lambda_+). No growth of a varying row
or location of the minimum is needed.

**Incoming sum and changed cap.** Exact c_0>w>1 and all 46 actual
log(c_i/2) intervals for i=1,...,23 at t=0,1 are independently checked,
including row23's tail20 and every amplified error. Induction proves
all 25 C_i(t)>=L_i>0. Prefixes through i=23 are unchanged; incoming
C_24(t)=C_24(0)2^(-18t). The compensating closing tail remains in D,
without a C_25>=1 premise. All reciprocals and their complete finite sum
are regenerated, and actual L_*=1 is checked. The exact bounds are
20138923467<R_H<20138923468<21000000000<P_40(24)<exp(24);
the old 20000000000 cap still fails. Since eta_i<kappa, full S and
every proper partial sum are strictly below Q. Bounding the three terms
in (8) proves the strict cap at every incoming input, including i=0,24.
Only L083's early proof cases are used after independent endpoint
licensing; its full all-order theorem is unavailable.

**Own-input sign and complete errors.** Fresh row18 prefix sums give
A=6078889,D=6862806 at both roots; both varying rows occur later.
Its outgoing pair is still (693015,3295208), giving positive
P=8157934,R=12930074. Upper log3 and lower log2 therefore give exactly
24+Pu-R*ell=-172437107269/12500000000<0. The full positive excess
in (10) is bounded above by 1/50000. The analytic interval encloses an
upper expression for the actual H margin, not the actual margin from
both sides; strict cap (8) supplies the necessary link. One negative
own-input margin contradicts the strict H guard regardless of other
guard verdicts.

All 100 terms for each log2/log3 series, both remainder bounds and all
41 exponential terms are regenerated by recurrences in their cited
positive-real domains. As a second cancellation check, 120-term intervals
[a,b] for log2 and [c,d] for log(3/2) give
[(N-K)a-Kd,(N-K)b-Kc] strictly inside the first Lambda enclosure and
(lambda_-,lambda_+). Since P-R<0, the alternative row18 interval is
[24+(P-R)b+Pc,24+(P-R)a+Pd], strictly inside the first upper-expression
interval. Both complete alternative errors are saved. These apply the
assessed series scheme; no new analytic theorem or floating point sign
test is used. L095's d34 verdict is not a premise.

**Evidence and verdict.** Run
`python3 scripts/postspell-word-count/audit_d35_two_root_h.py`.
The independent script neither imports nor runs the constructor. It
reconstructs every non-check construction field and separately replays
all 424 stored comparisons, their exact differences and verdicts, checking
unique names and truth. All 5205 comparisons pass, with zero failures;
this includes recursive data/report checks, not 5205 distinct mathematical
claims. Complete evidence is
`scripts/postspell-word-count/d35-two-root-h-audit-certificate.json`.
The exact cap, exponential lower sum, complete row18 interval/error record
and alternative Lambda interval were also inspected in full. The original
construction certificate is unchanged. Neither previews nor success
flags substitute for complete verification and the proof-case review.

The continuation test passes: retain L100's original scope. Attempt032,
the failed full-package data and both d0 witnesses remain valid. No
allocation/order/cutoff reduction, family exhaustion, integer/parity
realization or actual-word transfer is supplied. Universal eventual
descent remains unresolved. The argument and direct inputs are unchanged,
so PROOF.md and DAG.md are not edited for audit status alone; this section
supersedes their pending L100-audit wording only.

## Mathlib

Full matching coverage for this d35 changed-cap specialization has not
been checked. Supporting affine, finite-sum, log and exponential facts
are not a full matching theorem. Unknown coverage is not evidence of
absence. No external Lean build or Lean verification is claimed.
