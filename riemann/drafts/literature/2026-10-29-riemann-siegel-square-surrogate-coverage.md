# Fixed-length Riemann--Siegel square surrogate: blocked source gate

TARGET: Test whether the fixed-length Riemann--Siegel square surrogate G_T defined in the assessment approximates D_1(Xi;t)/A(t)^2 with integrated absolute error o(T(log T)^3).
CHECKED: 2026-10-29
DECISION: SOURCE_BLOCKED
SEARCH_EVIDENCE: Completed bounded exact-square, differentiated Riemann--Siegel, absolute-mean and stronger Laguerre comparisons; reused the local Selberg and finite-jet failures. Inspected Blanc 2018, Ivic 2019 and bramble_trace v4 primary passages; earlier low-order primary proof retrieval failed. Queries and access outcomes below; no novelty inferred.
SOURCE_EVIDENCE: Blanc arXiv:1809.00735v1 Introduction, Theorem 1.1 and low/high-order proof split; Ivic, Banach Center Publ. 118 (2019), Section 4 p. 16 (4.3) and surrounding restrictions; bramble_trace paper 41 v4 Theorem 3 (7a)--(7d), Sections 8.2--8.3; Bui--Hall (1) reused through L471. Karatsuba 1985 full theorem/proof and Blanc 2015 low-order source remain unread, with access failures recorded below.
COMPARISON: Blanc's inspected theorem excludes fixed k=1,2 at large height; Ivic's frozen formula is on short intervals with a phase-aligned base, not [T,2T]; the inspected Laguerre absolute-mean comparator differs from G_T and retains full-scale error at fixed order. None supplies this absolute defect. Do not differentiate an uncontrolled remainder or replace the moving cutoff silently.
GAP: Essential low-order derivative/endpoint proof coverage for a direct Riemann--Siegel implementation remains missing; neither E(T)=o(T(log T)^3) nor a full-scale lower bound is established. No theorem deciding this exact square was located among inspected sources.
REASON: Park this dependent arithmetic attempt after bounded access failures and concrete scope mismatches. Resume independent mathematics using the unchanged ready C464c audit assessment; reopening this surrogate needs an accessible exact low-order source or a separately reviewed mechanism avoiding it. This review proves no new result.
SCOPE: Actual Xi and L471's exact A; real T tending to infinity, t in [T,2T], natural logarithms, fixed length floor(sqrt(T/(2pi))). No RH, simplicity, zero spacing, selected-energy bound, fixed-half-plane premise or unproved differentiated remainder.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED left essential primary differentiated-formula, fixed-length endpoint and absolute-defect coverage missing for this new target; this is its first completed external comparison, not repeat browsing of ready coverage.

## Exact proposed test, not a result

Use L471's notation W(t)=D_1(Xi;t)/A(t)^2. For T sufficiently large
define, purely as a candidate arithmetic surrogate,

    M_T=floor(sqrt(T/(2pi))),
    lambda(t)=(1/2)log(t/(2pi)),
    P_(1,T)(t)=sum_(1<=n<=M_T) (lambda(t)-log n)n^(-1/2-it),
    G_T(t)=4|P_(1,T)(t)|^2,
    E(T)=integral_T^(2T) |W(t)-G_T(t)| dt.

The bounded future test asks whether E(T)=o(T(log T)^3), or whether
a rigorous full-scale obstruction rules out this particular surrogate.
No expansion of W, remainder estimate or assertion about E is proved
in this nomination. In particular the choice of length and coefficient
4 has not been justified as an approximation. G_T is an explicitly
nonnegative square; a successful absolute approximation would offer a
route to the missing mean negative-mass saving. L476 explains how that
mean question also relates to the retained N_h, but a mean saving would
still not control individual heights, higher signs or mixed positivity.

The candidate mechanism keeps the actual arithmetic phases n^(-it)
and their mixed correlations with W. It is not a proposed deduction
from only second/fourth Hardy-jet moments. L472/L473's abstract-law
obstructions remain in force, as do L471's pair-quotient displacement
loss, L475's exponential band cost and the Selberg differentiated-
remainder mismatch. None of those failures has been proved here to
cover this particular square. Conversely they cannot be dismissed
without the source and overlap comparison.

## Required separate source comparison and stopping test

Search for this exact square approximation, standard differentiated
Riemann--Siegel formulas and stronger known estimates or obstructions
for the corresponding mean absolute defect. Inspect primary theorem
hypotheses and the relevant endpoint/remainder proof cases. Specify
whether estimates concern ordinary Hardy derivatives, the fixed length
M_T or a moving length, and L1 or merely signed/second moments. Do not
differentiate an uncontrolled error or silently omit the changing
Riemann--Siegel endpoint when comparing a moving-length formula with
this fixed-length candidate. Retain the exact completion curvature from
L471 when passing between Hardy derivatives and W.

The discriminating scale is E(T)/(T(log T)^3). Agreement of signed
means is not enough. A lower bound E(T)>=c T(log T)^3 on an unbounded
sequence, with fixed c>0, would abandon this square-approximation
mechanism, not disprove a saving for N(T) or RH. A ready review may
approve a bounded arithmetic defect test even if its success is unknown;
inadequate essential source coverage must remain explicitly pending.
Do not replace this target with a new surrogate inside its research turn.

If separately approved, the arithmetic cancellation/obstruction test is
a candidate for proof_attempt/creative: its precise obstruction is the
uncontrolled absolute residual between W and this nonnegative arithmetic
square at the full T(log T)^3 scale. This would test a new mechanism for
mean first-sign failure, beyond the already checked generic moment and
absolute-pair routes. No creative attempt is approved or performed now;
the saved mathematical target first receives a literature_comparison
turn because its gate is REVIEW_REQUIRED. Full matching Mathlib coverage
is unchecked.

## Completed comparison and route decision (29 October 2026)

The mathematical target above is preserved. The outcome is NEGATIVE
about source applicability and continuation readiness, not a lower bound
on E(T), an obstruction theorem for this square, or progress beyond the
sources checked. No lemma, mathematical script, DAG or PROOF.md changed.

### Inspected statements and qualifications

1. [Blanc 2018 v1](https://arxiv.org/html/1809.00735v1), pp. 1--2,
   (1.1)--(1.4), Theorem 1.1; pp. 9--10, proof completion. With
   d=theta'(t), fixed c>1, its theorem assumes d<=k<=3d^2 and gives

       R_k=O(t^(-1/2)c^(k/d)d^k
                   +t^(-3/4)exp(k/(2d))k d^(k-1)).

   The preceding formula uses n<=sqrt(t/(2pi)), coefficient
   (d-log n)^k and phase theta(t)-t log n+k pi/2. The low-order
   assertion is explicitly referred to the 2015 paper, not proved by
   this theorem. The proof separately cites the earlier low-order
   bound when estimating eta_p. Thus substituting k=1 or 2 in the
   displayed theorem is invalid eventually. No RH assumption occurs
   in this inspected derivative statement. Neither a frozen M_T nor
   an absolute quadratic-defect theorem is stated.

2. [Ivic 2019, Section 4, printed p. 16, (4.3)](https://www.impan.pl/shop/en/publication/transaction/download/product/113095),
   DOI 10.4064/bc118-1, pp. 9--23. Read the proof opening and the
   complete paragraph preceding/following (4.3) in the primary PDF
   text. It freezes P=sqrt(T/(2pi)) after imposing
   T/2+pi/8=2pi K and T^epsilon<=H<=T^(1/6). Its error is
   O(T^(-1/4)log^(k+1)T); it refers to Karatsuba 1981 p. 59 and
   Ivic's 2013 book, Theorem 5.2, for the unsimplified derivative
   formula. This short-interval, phase-aligned statement does not
   authorize freezing the length over a dyadic interval. No such
   extension is derived here. PDF screenshot retrieval timed out;
   no visual formula verification or broader proof audit is claimed.

3. [bramble_trace, paper 41 displayed v4](https://rstation.ai/problems/riemann_hypothesis/papers/41),
   24 October 2026, Theorem 3 and Sections 8.2--8.3. For
   Q_n=n! ell_t^(-n) L_(n/2)[Z], its shrinking-shift statement is

       integral_T^(2T)|Q_n-2|zeta(1/2+n/ell_t+it)|^2|dt
          <<_b T log T/n^2,     even 2<=n<=b log T.

   The source also claims the normalized Xi version. Its comparator
   is not G_T. The stated relative conclusion needs n tending to
   infinity; fixed n retains full scale. Read the centered coefficient
   moments and absolute-mean Taylor remainder cases in Section 8;
   this scope comparison is not an independent audit or import.

4. [Bettin--Chandee--Radziwill, arXiv:1411.7764v1](https://arxiv.org/html/1411.7764v1),
   Introduction (1.1)--(1.2), Theorem 1, inspected as a stronger
   mixed-moment lead. It treats a smooth weighted unshifted
   |zeta(1/2+it)A(1/2+it)|^2 with a_n<<n^epsilon and
   polynomial length exponent below 17/33. Its stated theorem has
   no derivative variables or absolute residual. No differentiation,
   shifted extension or defect estimate is imported from it. Further
   proof extraction is unnecessary for this rejection of direct use.

L471 (7) remains the exact local identity
W=Z'^2-Z Z''-(log A)''Z^2, including real zeros. Its completion
curvature must be retained in any later application. L471 (8) supplies
ordinary second moments, not mixed correlations with P_(1,T).
L472/L473 obstruct inference from their specified finite jet data;
they do not prove failure of this arithmetic square. L476's audited
signed truncation does not supply its absolute defect either.

### Search, access record and stopping decision

Queries included `Hardy Z function derivatives Riemann Siegel formula
Z second derivative error Ivic`, `Riemann-Siegel derivatives remainder
theorem`, `"Riemann-Siegel" "square" "absolute error" Hardy`,
`"Hardy" "Laguerre" "Dirichlet polynomial" "absolute"`,
and the exact titles of Blanc's 2015 and Korolev's 2018 papers.
These located derivative and signed/twisted moment sources, not an
inspected theorem for this E(T). Failure to find a match establishes
no originality or impossibility.

Blanc, *Optimal upper bound for the maximum of the k-th derivative of
Hardy's function*, J. Number Theory 154 (2015), 105--117,
[DOI 10.1016/j.jnt.2015.02.009](https://doi.org/10.1016/j.jnt.2015.02.009), was inaccessible; the
ScienceDirect article S0022314X15000980 returned 403. Karatsuba
1985, *The Riemann zeta function and its zeros*, Russian Math.
Surveys 40:5, 23--82,
[DOI 10.1070/RM1985v040n05ABEH003682](https://www.mathnet.ru/eng/rm2762),
had Math-Net English PDF and getFT downloads time out; a link
variant redirected to the homepage. Indexed pp. 32--33 extracts
are retained only as leads, not inspected proof. The secondary
description of Korolev, *On the Riemann--Siegel formula for the
derivatives of the Hardy function*, St. Petersburg Math. J. 29:4
(2018), 581--601, DOI 10.1090/spmj/1508, identifies first
and second derivatives, but the attempted AMS/DOI and Math-Net
access did not supply its theorem/proof. It is likewise unread.
The shell has no external DNS access; it supplied no primary text.
No credentials, API keys, purchases or external messages were used.

The discriminating scale and abandonment test stay exactly as in the
original nomination: absolute o(T(log T)^3), or a rigorous positive
full-scale lower bound on an unbounded sequence. Neither is proved.
Essential source coverage is still absent, so no dependent research
attempt is approved. Park this implementation rather than repeatedly
trying the same inaccessible sources. Reopening requires accessible
low-order theorem/proof and endpoint control, or a separately assessed
arithmetic mechanism that avoids differentiated Riemann--Siegel.

The independent ready continuation is the already approved C464c
critical audit, under the unchanged assessment
`2026-10-26-c464c-critical-audit-coverage.md`. Its source gate is
SPECIALIZE; this turn does not perform that audit or modify its
assessment. It tests a parameter-sensitive tail input, not the
square-surrogate claim. Creative arithmetic work remains desirable
but is blocked here by missing essential coverage; an audit is not
relabeled creative. Full matching Mathlib coverage is unchecked.
