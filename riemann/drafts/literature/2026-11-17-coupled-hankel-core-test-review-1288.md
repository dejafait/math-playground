# Fixed rectangular coupled core test — prepared coverage1288

TARGET: Test whether C032f's unchanged A and B admit one common scalar-to-two-component compact-core differential intertwiner with real scalar p,q and real symmetric matrix P,Q of degree at most two, p(0)=P(0)=0, p>0 and P positive definite on the open half-line, using necessary kernel identities and exact coefficient comparison.
CHECKED: 2026-11-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse completed1288's bounded rectangular/matrix Hankel differential-intertwiner and bispectral searches and targeted duplicate/failure checks; exact queries and inspected scope are in drafts/working/2026-11-17-coupled-hankel-intertwiner-source-notes-1288.md. No adequate matching four-theta-kernel result was located, without claiming novelty or exhaustive coverage.
SOURCE_EVIDENCE: Casper-Grunbaum-Yakimov-Zurrian, arXiv:2302.05750v2 https://arxiv.org/html/2302.05750v2 Section2.3/(2.4), Definition5.3 and Proposition5.4 supply known square-matrix action, formal adjoint and compact-support Green calculus. Theorem6.1/proof(6.3) and Casper-Yakimov1807.09314v2 Theorem5.1 are inspected scope comparisons only. Blower0712.1013v1 Theorem2.1 proof(2.3)-(2.5) is reused from source-notes1284. Full hypotheses and links: source-notes1288.
COMPARISON: The sources cover the integration-by-parts mechanism, not this rectangular compatibility verdict; their square bispectral existence hypotheses are unverified here. The allowed difference is a fully justified compact-core rectangular adaptation followed by a fixed-theta finite coefficient test. C032h's identical scalar commutant exclusion does not settle the independent coupled output class.
GAP: Establish the necessary kernel equations with correct action order and endpoint handling, then obtain a rigorous contradiction or the exact surviving necessary conditions. Formal compatibility alone does not construct a spectral interface, prove a relative bound, decide delta or establish Xi signs.
REASON: This finite necessary-condition attempt can reject the changed auxiliary class before domain investment, or identify precisely what survives; no degree enlargement or automatic spectral transport is authorized. Newly written coverage awaits the supervisor's separate approval before mathematics.
SCOPE: C032e full positive smooth Psi and bound(8), C032f(1)-(5) with its accepted core/domain reduction, C032h as a contrast and stop1283 as preserved evidence; unweighted complex H and Y, one scalar input shared by both tilts, all four unchanged scalar kernels and the fixed c. Only local differential-expression identities on compact inputs.

Keep T_H f=-(p f')'+q f and T_Y g=-(P g')'+Q g. Both output
coefficient matrices may be nondiagonal. Do not change kernels, weights,
half-line, scalar input multiplicity or the specified degree. Do not
replace the two column kernels with a square bispectral Gram kernel.

The first obligation is the compact-core kernel identity, justified by
local smoothness, differentiation and Green's identity. The general
identity is known calculus; cite it precisely and prove only the needed
rectangular/action-convention adaptation. The source uses right matrix
action; the nominated output acts on columns on the left. The kernel
slices have no compact support, so use a justified cutoff if applying
Proposition5.4 as stated, and explain all endpoint brackets. No global
derivative-tail estimate or self-adjoint extension is required for a
local necessary test unless the subsequent reasoning actually uses it.

Then make one exact polynomial-coefficient compatibility attempt on
that necessary system. A contradiction already from a necessary subset
suffices, with no need to test every remaining equation. If only a subset
is checked and survives, report its unpaid equations explicitly. Include
linear p, constant q, nondiagonal P,Q and allowed leading-coefficient
degeneracies. Avoid unjustified divisions and invented tail asymptotics;
any additional analytic claim requires a proof from the covered local
theta inputs or fresh source coverage before dependent work.

Threshold: a rigorous contradiction rejects this fixed class; a fully
compatible identity supplies only a formal candidate requiring separate
domain and relative-bound assessment. An inconclusive finite test is
EXPLORATION, not an obstruction. After rejection park the class. After an
inconclusive attempt preserve its equations and require a materially new
input or refined discriminating test before repetition. Do not respond
by an automatic degree sweep or routine audit chain.

Potential downstream use remains organization of C032f(5)'s
B*B>=d^2 A*A comparison. Actual-range inclusion, a closed realization,
spectral multiplicity, a relative spectral estimate, delta, completed
source metric and transport, independently signed actual-Xi form,
initialization and every-degree assembly remain independent gaps.
Full matching Mathlib coverage is unchecked. This is auxiliary finite
development, not a central creative mechanism or an RH candidate.
