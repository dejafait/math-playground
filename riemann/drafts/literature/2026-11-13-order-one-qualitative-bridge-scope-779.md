# Source screen: the missing order-one hypothesis — completed step780

TARGET: Assess whether an even real entire function of order one with F(0)=1, a nonnegative integrable cosine density with all moments, positive gamma_n in F(t)=sum(-1)^n gamma_n t^(2n)/n!, strict alternating differences of log(gamma_n) from order two, and Stieltjes moment sequences (gamma_n^(-c)) for every c>0 must have every logarithmic H_d positive semidefinite, or whether a known obstruction defeats this implication.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step780 searched order-one coefficient/inverse-moment, Laguerre-Polya, Lee-Yang and hypergeometric obstruction terminology; read Sokal's primary finite obstruction case and compared the recorded KPS sufficient-class stop. Queries and duplicate checks below; no joint-property counterexample or novelty is inferred.
SOURCE_EVIDENCE: Sokal JMAA515(2022)126432 p1/order formula, AppendixA Propositions6-7 pp5-6 and equations12-14 p6; KPS AIF74(2024) Theorem4.4/(4.14) p396 and Section5.2.6 pp416-417; Berg math/0412340v1 Theorems5.1-5.2 pp14-15; NIST DLMF16.5.2,10.9.4,10.16.9,5.9.16 with parameter domains; details below.
COMPARISON: KPS requires extra separated Bernstein-Pick structure. Sokal supplies a different hypergeometric logarithmic-moment obstruction family, but neither source checks every displayed coefficient/cosine premise together with this H_d convention. C040b remains an exhausted order4/3 finite test.
GAP: The implication remains undecided locally; the bounded remaining specialization is one fixed hypergeometric joint-property/H_1 test. Its density, exact order, strict all-order differences, every-real-c moment laws and determinant remain obligations. Actual-Xi claims remain unaudited.
REASON: Sources identify an independently testable fixed order-one comparison instead of rescheduling the unpaid all-degree implication or extending C040b; no new mathematics was derived this turn.
LITERATURE_REASON: Essential target change from one fixed order4/3 model/matrix to a class-level order-one implication; the prior assessment explicitly excluded Xi's order-one growth.

In this proposed comparison define G(w)=sum(-1)^n gamma_n w^n/n!,
S_k=-k[w^k]log G(w) using the normalized germ at0, and
H_d=(S_(i+j+2))_(0<=i,j<=d). The coefficient difference premise is
(-1)^(r-1)Delta^r log(gamma_n)>0 for every n>=0 and r>=2;
the moment premise covers every real c>0. A cosine density means
F(t)=integral_0^infinity m(u)cos(tu)du on real t, m>=0,
integral m=1 and all nonnegative moments finite. Entire order one
is an exact growth requirement; no exponential-type bound is assumed.

The step780 invocation was literature-only. Its assigned scope was to compare the exact implication with
standard entire-function growth, Laguerre-Polya/Lee-Yang and coefficient
moment criteria, and check the already recorded sufficient-class and
generic-positivity stops before assessing any new theorem application.
Retrieve exact primary hypotheses and any essential proof case rather
than extrapolating from the finite model. A source merely restating
all logarithmic Hankel signs, or imposing them as a premise, is no
independent bridge. Distinguish a known class counterexample from one
that satisfies all displayed coefficient quantifiers.

This target asks for source comparison, not a new lemma, numerical
model sweep, proof of the implication or audit of Kawano's certificates.
The source screen must end with an import/obstruction or one bounded,
independently testable follow-up. If only the same unpaid all-degree
sign remains, stop that implication route; do not reschedule source
search without new evidence. No mathematical conclusion about this
class is asserted here.

The gap is L030-L032/C032a. Actual-Xi structure, truth of any imported
coefficient result, all-degree signs and shifted/global assembly remain
unresolved. A creative proof attempt is not yet justified: an independent
order-one mechanism and adequate source coverage are both missing.
No cross-notebook input is proposed; full Mathlib coverage is unchecked.

## Primary comparison and essential cases inspected

A. D. Sokal, *When does a hypergeometric function pFq belong to the
Laguerre-Polya class LP+?*, J. Math. Anal. Appl.515(2022),126432,
[published author PDF](https://discovery.ucl.ac.uk/id/eprint/10150527/1/Sokal_1-s2.0-S0022247X22004462-main.pdf).
Read p1 (order1/(q-p+1), nonterminating parameters), AppendixA
Propositions6-7 p5, and the full alpha_3 case (12)-(14), p6.
Proposition6 assumes entire f with f(0)!=0 and concerns alternating
coefficients of f'/f, not reciprocal Taylor coefficients. Proposition7
is the formal Stieltjes continued-fraction criterion. Earlier nonzero
continued-fraction coefficients must be checked before using a negative one.
For a1=b1+delta, b1>0, 0<delta<1, the paper proves alpha_3<0
eventually in b2; its example b1=1,delta=1/2 has threshold52.4865... .
This suggests the single choice b2=100, requiring exact local verification.
Theorem5's unbounded-parameter statement alone cannot certify a prescribed
matrix. Conjecture8 is not imported. No assertion that the present
joint premises hold for the source example is made here.

[KPS Theorem4.4/(4.14),p396](https://www.numdam.org/item/10.5802/aif.3600.pdf),
and its Section5.2.6 proof, pp416-417, were compared. Its positive case
requires a Bernstein-Pick factor with the specified separation of zeros
and poles. The proof uses that separation in meromorphic continuation
of the reciprocal recurrence before applying Laguerre's theorem.
Coefficient moment divisibility alone does not supply that hypothesis.
Its negative case refers to the already recorded Mittag-Leffler family;
it is not a joint order-one counterexample. Reuse the exact earlier scope
decision in `2026-11-05-actual-xi-levy-certificate-comparison.md` and
`ATTEMPTS/2026-11-05-actual-xi-levy-sufficient-class-unpaid.md`.
No actual-Xi Levy construction or its supplements is reopened.

[Berg, math/0412340v1, Theorems5.1-5.2,printed14-15](https://arxiv.org/pdf/math/0412340v1),
already assessed in778, supplies all positive powers of gamma moments
(a)_n for a>0 and beta moments (a)_n/(b)_n for0<a<b.
Their Mellin domains are Re(z)>-a, including every nonnegative integer.
The primary statements and beta proof were checked; the gamma proof
coverage from778 is reused. The PDF labels arXiv v1/17December2004
and has internal date27August2018. Quotients outside the beta ordering
are not licensed. The prospective reciprocal-coefficient factorization
still needs verification, including real c>0.

NIST DLMF, online version1.2.8/release15September2026, checked13November2026:
[16.5.2](https://dlmf.nist.gov/16.5#E2) is the beta integral transform,
valid for p<=q and Re(b0)>Re(a0)>0 (principal branches, straight path).
[10.16.9](https://dlmf.nist.gov/10.16#E9) identifies J_nu with0F1;
[10.9.4](https://dlmf.nist.gov/10.9#E4) is the positive Poisson cosine
integral for Re(nu)>-1/2. The proposed nu=0 and beta parameters
a0=3/2,b0=100 are in these domains. An integrable cosine density
requires the actual change of variables and Tonelli argument;
positive definiteness alone is not a density proof.
[5.9.16](https://dlmf.nist.gov/5.9#E16), within Re(z)>0, is the
digamma integral. Differentiated use needs domination, endpoint
integrability and strictness for every finite-difference order at n=0.
These are specialization obligations, not missing primary-source access.

## Search and overlap record

Queries included `entire function order one infinitely log concave coefficients
reciprocal infinitely divisible Stieltjes moments Laguerre Polya`,
`Katsnelson polynomial sequences moment problem Mittag Leffler 2024 KPS Riemann xi`,
`1F2 real zeros 3a`, `Lee-Yang Fourier transform positive density entire order one
sufficient conditions`, `1F2 cosine beta integral 1/2`,
`Sokal 1F2 Stieltjes inverse`, and `hypergeometric infinitely divisible
Laguerre coefficients`. Search snippets were navigation only.
Dimitrov's Lee-Yang/Wronskian paper and later hypergeometric zero-region
papers are unread leads; no theorem from them is used or needed for
this fixed finite discriminator. No inspected theorem settles the
joint premises. This is not evidence of novelty. Shell PDF retrieval
failed DNS resolution; the needed primary text was accessible through
the web tool, so there is no essential source blocker.

Local checks targeted assessment778, C040b, assessment777's overlap
section, the November5 KPS stop and gamma-moment assessment, then
exact `52.4865`, `1F2`, beta-Bessel and hypergeometric-bridge phrases
in this notebook's literature/attempt/lemma folders. One older1F2
mention concerned fixed shifted common zeros, not these premises.
No sibling notebook was read. The initial notebook-only git status
output was excessive; subsequent inspection used exact paths.
All existing work is preserved.

## Bounded follow-up and stopping rule

Nominate only F(t)=1F2(3/2;1,100;-t^2/4), using the same
gamma/S/H conventions above, and its single2-by-2 H_1.
Check the joint premises and exact det(H_1)<0; do not infer the latter
from a decimal continued-fraction threshold. A complete negative
certificate would defeat the qualitative order-one implication, without
addressing stronger quantitative or actual-theta hypotheses. A favorable
matrix or failed premise ends this fixed test; no parameter/degree sweep.
Do not call the function a countermodel before those obligations are met.
The prospective scope is in `2026-11-13-fixed-beta-bessel-bridge-test-780.md`,
pending the separately required approval. No derivation or mathematical
script was made. Actual-Xi mixed positivity and shifted/global assembly
remain unresolved. This is source-guided reproduction, not creative
central mathematics. Full matching Mathlib coverage was not checked.
