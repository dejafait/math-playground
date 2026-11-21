# Direct complete-kernel minimax residual — source comparison

TARGET: Assess source coverage for direct complete-kernel minimax residuals on the fixed equispaced band with TV budget exp(sqrt(n)).
CHECKED: 2026-11-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Step370 reused reviews364/365 and stops340/341; scoped November10-11 searches for Sion, semi-infinite duality, complex Chebyshev and constrained minimax found no other local assessment. External queries and inspected primary contracts are recorded below; no matching growing-n rate or novelty conclusion was established.
SOURCE_EVIDENCE: Sion (1958) Theorem3.4 p174, https://msp.org/pjm/1958/8-1/pjm-v8-n1-p14-p.pdf; Boyd–Vandenberghe (2004) Examples3.24/3.26 pp92-93, https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf; Shapiro author manuscript Theorem2.3 p6 and Lemma6.1 pp27-28, https://optimization-online.org/wp-content/uploads/2008/07/2028.pdf; Yang–Zhang–Zhang arXiv:2308.07636v1 Theorem2.1/proof(2.3)-(2.4), https://arxiv.org/html/2308.07636v1#S2. Audited C997c supplies the kernel; reviews364/365 supply reusable finite-sum background.
COMPARISON: General real convex minimax tools support investigating a complex-TV certificate after explicit realification; they do not pay the original budget or the required kernel-specific rate. The inspected complex discrete theorem has Haar, finite-node and unconstrained-coefficient qualifications; no automatic import to this kernel is justified. Previous Taylor/defect and scalar/spectral stops do not decide the complete residual.
GAP: The structured asymptotic estimate for E_n at budget exp(sqrt(n)) remains unpaid; a fixed-n dual contract or convergent discretization alone would not close it. No optimizer, kernel-specific dual identity, mesh bound or asymptotic witness is established in this source turn.
REASON: The changed integrated objective needed essential unread minimax/continuum coverage. That bounded source comparison is now complete enough to nominate one dual-witness attempt, with separate source approval next turn; there is no persistent retrieval blocker.
SCOPE: Source comparison for integer n>=2, fixed n+1 equispaced frequencies in E, and budget exp(sqrt(n)); future mathematical work must verify every specialization and retain complex phases and the complete kernel. No other grids, budgets or general-band impossibility are approved by this assessment.

## Step369 nomination, preserved

## Exact proposed test and downstream use

Use the COMPLETE C997c point kernel, written explicitly in C997q:

    k_n(c,z)=-2 exp(-cn/4) [integral_(cn)^(c(n+2)) g_n(t) exp(izt)dt
                           -integral_n^(n+2) g_n(t) exp(izt)dt],
    g_n(t)=((L_(n+1)^(2)(t)-1)/(n+1))*exp(-t/2)*cosh(3t/8).

Keep I=[7/4,9/4], E=[15/8,17/8], z_star=1+i/8,
gamma_(j,n)=15/8+j/(4n), 0<=j<=n. The proposed objective is

    E_n=inf_(sum_j |A_j|<=exp(sqrt(n)))
          sup_(c in I) |k_n(c,z_star)-sum_(j=0)^n A_j k_n(c,gamma_(j,n))|.

This defines a target, not a result about E_n. The sought threshold is
E_n<=C exp(-n/64), with C independent of n, for every sufficiently
large integer n. A construction meeting that threshold would provide
one paid positive-branch point approximation at a subexponential
original band-TV budget. It could be used in signed slope selection;
it does not supply actual-Xi positivity or selected-response transfer.
The fixed budget is a testable subfamily of all subexponential budgets;
failure under it would not exclude larger subexponential budgets.

The decisive later evidence would be a uniform primal certificate at
the threshold, or certified dual witnesses making
E_n/exp(-n/64) unbounded on an unbounded integer subsequence. No dual
identity, optimality condition or asymptotic witness is derived now.
Finite samples, condition numbers and solver output alone cannot prove
the continuum threshold or its failure. The source review should check
complex versus real separation, the coefficient-l1 constraint, the
original slope sup norm, and continuum discretization errors before
approving one bounded mathematical test. A generic energy bound in a
worst data direction does not settle this structured target.

## Mechanism comparison and preserved stops

Three possibilities were compared without undertaking another attempt:

1. Repeat or shift the centered Taylor construction. C997r now has an
   accepted audit of its fixed-center norm/defect dichotomy. No new
   estimate justifies a shifted-center reopening; preserve stop367.
2. Resume scalar damping or spectral cutoff of a continuum representer.
   C997j/k and stops340/341 leave an operator-specific target spectral
   tail unpaid. No new tail estimate is available, so do not repeat
   the same algebraic regularization or sampled eigenvalue experiment.
3. Optimize the complete residual itself under an explicit original-TV
   cap, with all coefficients free. Select this materially different
   objective for source assessment. It retains cancellation inside the
   moving integral and does not impose small D, small Delta separately,
   exact homogeneity, or a Taylor coefficient rule.

Stops314/315 concerned the full-quartet assay and uncertified fitting
or an inadequate interpolation envelope. They prohibit treating another
fit as a certificate; they do not establish a lower bound for this
complete positive-branch minimax objective. The new test must use a
uniform continuum primal/dual certificate. The exact-chain stop364,
packet stops and their stated audit qualifications are preserved;
none is broadened into a ban on arbitrary band measures.

The next literature step should reuse reviews364/365 for finite-sum
background and seek only the changed, essential minimax contracts.
This is neither approval to derive previously uncovered mathematics
now nor a claim of source blockage. If comparison shows an existing
quantitative theorem covers the target, cite it precisely; if only
general duality is available, identify the remaining kernel-specific
estimate before approving a research target. Do not repeat retrieval
attempts or start an unconstrained approximation survey.

Essential local input is C997c; C997q supplies notation, and its
(1)-(2) were directly checked in C997r's step369 audit. The broader
C997q proof, C997j/k and prior failed constructions are not essential
theorem inputs to this nomination. Preserve every zero, both beta
terms, K's -1, both windows and both endpoints of I. No nonvanishing,
zero simplicity or numerical bulk onset is assumed. C997a(8), selected
and both-sign transfer, assay/reconstruction, complements/regulators,
L993, unpaid L984(H), L966/L968 forcing and L030-L032/C032a positivity
remain open. No cross-notebook input. Full matching Mathlib coverage
is unknown and has not been searched for this new objective.

At step369 this assessment was REVIEW_REQUIRED. The source comparison
below supersedes that readiness statement only. No mathematical
exploration attempt or supervisor counter reset is claimed.

## Step370 bounded source review

LITERATURE_REASON: The saved target replaces separate defect/boundary control by the complete integrated residual; reviews364/365 do not cover its complex coefficient-TV constrained continuum minimax contract.

The main gap is still L030-L032/C032a actual-Xi positivity, L966/L968
signed forcing and unpaid L984(H). The intermediate test remains exactly
E_n above, rather than approximation of the bare exponential. Its
possible use is one positive-branch point bridge for signed slope
selection. Independent transfer and realization gaps remain unpaid.

### Queries, inspected sources, and comparison

Queries used on 11 November2026 were: `Shapiro semi infinite programming
duality discretization 2009 compact Slater measures theorem`; `complex
Chebyshev approximation l1 constrained coefficients duality measure
minimax`; `site.gatech.edu Shapiro "Semi-infinite programming, duality"
pdf`; `"Sion" "On general minimax theorems" pdf 1958`; `"Laguerre"
"kernel" "minimax" "total variation"`; and `"complex" "Chebyshev"
"coefficient" "l1" constraint continuum`. These bounded searches found
general contracts, not a matching rate theorem. Failed search is not
evidence of novelty or impossibility.

**Minimax interchange.** M. Sion, *On general minimax theorems*, Pacific
J. Math.8(1958),171-176, [Theorem3.4, p174](https://msp.org/pjm/1958/8-1/pjm-v8-n1-p14-p.pdf),
was read with its finite-cover/minimal-set proof and adjacent
semicontinuity counterexample, Remark3.6. For convex compact spaces M,N
and a real function upper semicontinuous/quasiconcave in M and lower
semicontinuous/quasiconvex in N, it equates sup-inf and inf-sup.
This supplies an interchange tool, not a quantitative approximation
bound. A future use must specify real scalar pairing, convex sets and
topologies and prove compactness and continuity; complex bilinearity
alone is insufficient. No application to E_n is proved here. The scan's
OCR misnumbers the following corollary; only Theorem3.4 is needed.

**Coefficient support functions.** S. Boyd and L. Vandenberghe,
*Convex Optimization*, Cambridge UP,2004,
[Examples3.24 and3.26, pp92-93](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf#page=106),
were read, including both cases in the norm-conjugate proof.
The conjugate of a set indicator is its support function; the conjugate
of a norm on finite-dimensional real space is the indicator of the
dual norm unit ball. These are the needed generic tools for handling
the coefficient cap. Their real-space formulation requires checking
the realification of the complex modulus norm, rather than replacing
it by separate real and imaginary absolute-value budgets. Neither
example bounds this kernel's approximation error. Such a norm
specialization needs only an applicability argument, not a new proof
of convex duality.

**Continuum qualifications.** A. Shapiro, *Semi-infinite programming,
duality, discretization and optimality conditions*, Optimization58
(2009),133-161; inspected the linked
[33-page author manuscript](https://optimization-online.org/wp-content/uploads/2008/07/2028.pdf),
using manuscript page numbers. Theorem2.3 p6 assumes a proper lower
semicontinuous convex objective, convex constraints, a finite primal
value, compact metric index space and jointly continuous constraints.
Under these assumptions Slater implies equal values and a nonempty
TV-bounded measure-dual solution set. Its proof is referred to
Bonnans–Shapiro, Section2.5.1, not reproduced there; that book passage
was not inspected. Lemma6.1 pp27-28 and its proof establish optimality
of accumulation points of epsilon-optimal discretized solutions when
epsilon and mesh vanish, assuming continuity of constraints and lower
semicontinuity of the objective. This is a fixed-problem assertion.
Section6 (6.2)-(6.3) and Theorem6.1 pp28-29 were also read: its rate
requires smoothness, growth, MFCQ, uniform Lipschitz and convergence
assumptions, all unchecked here. None supplies constants uniform in
our growing n. This source informs certificate requirements; no
unverified rate theorem is imported.

**Complex discrete comparison.** L. Yang, L.-H. Zhang and Y.-N. Zhang,
*The L_q-weighted dual programming of the linear Chebyshev approximation
and an interior-point method*,
[arXiv:2308.07636v1](https://arxiv.org/html/2308.07636v1#S2),15 August2023,
Theorem2.1, was inspected with the Haar definition, the real/imaginary
block representation(2.4), Slater duality proof and support-count
argument through(2.3)-(2.4) and the following paragraphs.
For a Haar basis of dimension d, at least d+1 distinct sampled nodes
and positive optimal error, it gives a probability-weighted L_q
dual equality for q>=1, with complementary slackness and at least
d+1 active weights. The coefficients there are unconstrained. Our
kernel columns have no proved Haar property, and our cap and continuum
objective differ. Thus its theorem is comparison evidence, not an
E_n certificate. Its subsequent q>1 uniqueness argument was only
partly inspected and is not used. The manuscript has apparent
notational slips in the coefficient-vector dimensions; its explicit
real/imaginary block formula, rather than those slips, was inspected.

Reusable Karmakar–Jordan and Tang–Garg–Kempf conclusions remain those
in review365, read locally this turn; no repeat external retrieval was
needed. Additional search hits on complex beamforming and constrained
discrete Chebyshev approximation were not read at theorem level and
are not inputs. One attempted arXiv /html/2308.07636v3 URL returned404;
v1 was accessible and is the version assessed. No access blocker
remains for the bounded continuation.

### Result and bounded continuation

DECISION EXPLORE concerns the unresolved quantitative objective.
The general tools are known imports; novelty of the kernel-specific
estimate is unestablished. The source review permits nomination of
one direct dual-witness test, not a claim that its asymptotic witness
exists. The new nomination is saved in
`2026-11-11-direct-kernel-dual-witness-review-370.md` and requires
separate approval next turn before mathematics. No new result was
derived, and no lemma, DAG edge or mathematical script was changed.

The discriminating evidence remains a uniform primal bound
E_n<=C exp(-n/64), or rigorous lower certificates with
E_n exp(n/64) unbounded on an unbounded integer subsequence. A generic
duality identity, a worst-data energy statement, or finite fits alone
is inconclusive. Original coefficient TV, complex target direction,
continuum slope norm and both windows must survive every certificate.
Do not promote failure of a defect sufficient condition to a residual
lower bound. Stop an unsuccessful witness mechanism unless an
informative obstruction or materially refined mechanism supports it.
Full matching Mathlib coverage remains unchecked/unknown. No
cross-notebook input, original advance or RH candidate is claimed.
