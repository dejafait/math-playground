# Source review: summable displacements and the complete logarithmic mean

TARGET: Assess the head-tail mechanism for A_n(e)>=A_n(0)-o(n) when L666 uses truncations of one fixed real l1 displacement sequence with cap 1/8, retaining L657's complete charges.
CHECKED: 2026-11-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 114 made nine bounded queries on quantitative Mahler continuity, growing-degree logarithmic integrability, summable perturbations and lattice/product logarithms; reused the inspected step 97/104/110 source comparisons and checked L657/L666/L692/L694 and step 105's recorded failure. No inspected matching theorem or fixed-l1 countersequence was found; no novelty inference follows.
SOURCE_EVIDENCE: Dimitrov--Habegger, arXiv:1909.06051v2, Appendix A, Lemmas A.3--A.5, pp.45--48 (A.4--A.5 proof cases reinspected); Brunault--Guilloux--Mehrabdollahei--Pengo, arXiv:2203.12259v2, Sections 2.2--2.5 p.3, Theorem 4.6 and Remarks 4.7--4.9 pp.9--10, Proposition 4.10 and proof p.11. Boyd's fixed-degree continuity, root integrability and Lev's construction are reused with the scope recorded below.
COMPARISON: The sharper small-value estimate retains the slice term-count parameter kappa and coefficient normalization; its regularization bound and the coefficient Holder bound retain growing term-count dependence. Neither covers the dense fixed-l1 tail of L666. L692's sharper sparse inequality is available for the head, but does not estimate the tail. Fixed-polynomial monomial substitution and infinite Fourier cancellation are different hypotheses.
GAP: Establish or obstruct the stated head-tail complete-logarithm limit, with all degrees, normalization and negative logarithmic mass paid; the head-to-baseline passage must also be explicitly checked using L692's sharper inequality. No estimate uniform in growing n, exchange of n and L limits, or target counterexample is established here.
REASON: Essential primary comparison is adequate for one bounded mathematical attempt at the saved target. EXPLORE licenses the family-specific test, not a favorable conclusion or a known-result import. There is no essential access blocker; this literature-only step derives no new result and changes no lemma or mathematical script.
LITERATURE_REASON: Fixed summable truncations and a growing-degree head-tail logarithmic limit lie outside L694's ready infinite-gap audit and require this separate comparison; unchanged Mahler and Fourier inputs are reused.
SCOPE: Exactly TARGET and the sufficient tail test below, for each fixed real l1 profile with cap 1/8, n=12q+3, original unit masses, fixed anchor, all M moments, full j=0 product, denominator angle 1/u and L657's complete charges. One analytic head-tail attempt or rigorous fixed-profile countersequence test is covered. No uniform bound over profiles, tail rate, circle-root separation, derivative interchange or full-cube conclusion is preapproved.

The proposal below records the state before step 114. The completed review
at the end supersedes its pending source-gate language; its mathematical
claims remain proposed and unproved.

## Exact proposed mathematical test

Fix a real sequence e=(e_m) indexed by Z with sum_m |e_m|<infinity
and sup_m |e_m|<=1/8. It is fixed as n grows; no n-dependent selection
or uniform tail rate is assumed. For n=12q+3 use only -2q<=m<2q in
L666's family:

    x=-5/4, R=11/8, U=R^2, h_n=27/(10n), M=n/3,
    a_m=x+i*h_n*(m+1/2+e_m),  Z_e={x} union {a_m},
    B_u(v)=product_(0<=j<n) R*(v-(j/n)*u)/(U-(j/n)*v/u),
    W_a(u)=B_u(x)/B_u(a),
    G_(n,e)(u,zeta)=R^(-1)*sum_(a in Z_e) W_a(u)
                          *sum_(0<=k<M)(a*zeta/R)^k,
    A_n(e)=mean_(|u|=1) mean_(|zeta|=1) log|G_(n,e)(u,zeta)|.

Means are normalized. The proposed inequality means

    liminf_(q->infinity) [A_(12q+3)(e)-A_(12q+3)(0)]/(12q+3) >= 0

for each fixed such e. A remainder may depend on e. Every mass remains
one; retain the fixed anchor, all M moments, j=0, the conjugated
denominator angle and all zeros. L657's complete identity
A_n=m_0+Z_n-P_n must remain applicable, including circle zeros and
exceptional slices. This paragraph defines a target, not a theorem.

The proposed mechanism splits a fixed head |m|<=L from its dense small
l1 tail. L692 suggests paying for the head through exact spatial
annihilation; a separate analytic/logarithmic argument would have to
control the tail while the degree and rational products grow. No
uniform-in-degree continuity estimate, lower logarithmic bound or
exchange of n and L limits is asserted here. The exact truncation
e_m^(L)=e_m for |m|<=L and zero otherwise gives a discriminating
subtest: assess whether a justified estimate can make

    lim_(L->infinity) limsup_(q->infinity)
       [A_(12q+3)(e^(L))-A_(12q+3)(e)]_+/(12q+3) = 0.

This is a proposed sufficient tail test to assess, not a derived result
or an approved mathematical subtarget. Its applicability and relation
to the head payment must be checked before approval.

## Relevance, comparisons and stopping test

The main gap remains actual-Xi all-degree mixed positivity. The nearer
route gap is L666's full independent-cube logarithmic control. A fixed
summable profile is an intermediate subfamily, not the full cube. L694
provides such a profile with an infinite Fourier gap. Establishing the
displayed inequality would test whether that gap can generate a linear
finite loss; refuting it rigorously could identify a concrete obstruction
to this route. Neither outcome alone supplies Xi realization, H/support
transfer or the required full-cube bound.

This differs from step 105's unresolved direct signed-contour descent:
the new hypothesis is a fixed summable profile and the proposed test is
an analytic head-tail limit, with complete logarithms retained. It also
differs from L692: the tail may change every available node. Do not
identify small l1 norm with exact finite support, or pointwise function
closeness with logarithmic-mean closeness near zeros.

For the separate source review, search this exact stability statement,
stronger Mahler/logarithmic-integrability results with degree dependence,
and known counterexamples. Reuse the inspected Lev material and the
notebook's existing Mahler sources where their hypotheses apply; read
only the relevant primary theorem statements and essential cases. No
specific new theorem is yet a checked input. Full Mathlib coverage for
this target is unchecked.

Continue only with an applicable import or a source-assessed bounded
test for the displayed limit. Abandon this head-tail closure if a
rigorous fixed l1 countersequence gives a loss >=c*n along an unbounded
subsequence for some c>0, or if the required lower-log control fails
under the actual hypotheses. Preserve any weaker informative obstruction;
a finite numerical example is not such a countersequence.

If no known theorem covers the tail estimate but the review identifies
an explicit test, this is a prospective proof_attempt/creative target:
the precise obstruction is the negative logarithmic part at growing
degree despite small displacement mass. Its downstream importance is
the unresolved finite-charge transfer, and the displayed head-tail
limit is the bounded test. Source comparison comes first; do not label
a known specialization creative. Step 113 does not approve or attempt
this new mechanism.

## Completed review — 3 November 2026, step 114

### Primary comparison and applicability

Reuse the detailed primary-source assessment
`2026-11-03-independent-shift-mahler-homotopy.md`, especially Boyd,
*Uniform Approximation to Mahler's Measure in Several Variables*,
Canad. Math. Bull. **41** (1998), 125--128,
[theorem p.127 and (8)](https://doi.org/10.4153/CMB-1998-019-6).
Its continuity is in a fixed ambient degree. L657's permitted numerator
degrees grow with n; fixed-degree continuity alone cannot justify the
two ordered limits here. No general continuity theorem is reproved.

V. Dimitrov and P. Habegger, *Galois Orbits of Torsion Points near
Atoral Sets*, [arXiv:1909.06051v2](https://arxiv.org/pdf/1909.06051v2),
24 March 2022, Appendix A, pp.45--48, Lemmas A.3--A.5. Reuse A.3's
normalized small-value hypotheses; reinspected A.4's entire dyadic-tail
argument and A.5's proof, including constant polynomials. For nonzero
complex d-variable polynomials P,Q with at most k terms each, k>=2,
and maximum-coefficient norm, A.5 states

    delta=|P-Q|/|Q|<=1/2
      implies m(P)<=m(Q)+C(d,k)*delta^(1/(8(k-1))).

There is no algebraicity or atoral hypothesis in this lemma. The lower
comparison needs the reverse ordering and its relative-norm condition.
A.4's small-value log tail, for nonconstant |P|=1, is bounded by
O_(d,k)(r^(1/(4(k-1)))). These statements include torus zeros.
Neither identifies displacement l1 norm with relative coefficient
distance of the cleared numerators; neither supplies fixed constants
or exponents when k grows. Those applicability obligations remain open.

F. Brunault, A. Guilloux, M. Mehrabdollahei and R. Pengo,
*Limits of Mahler Measures in Multiple Variables*,
[arXiv:2203.12259v2](https://arxiv.org/pdf/2203.12259v2), 27 June 2022,
Sections 2.2--2.5 p.3, Theorem 4.6 pp.9--10, Remarks 4.7--4.9 p.10,
Proposition 4.10 and complete proof p.11. Use d for their variable
count, distinct from our n. For a Laurent polynomial P with k>=2
nonzero coefficients, maximum coefficient norm L_infinity(P), and
kappa the largest number of distinct powers occurring in any one
variable, Theorem 4.6 states, for 0<alpha<1 and r>0,

    mu_d{|P|<=r} <= C_1(d,k)*alpha^(1-d)
                         *(r/L_infinity(P))^((1-alpha)/(kappa-1)),
    C_1(d,k)=6k*(18*d*k^2)^(d-1).

Reused its normalization and slicing proof; checked the final
monomial-coefficient case and the comparisons in Remarks 4.7--4.9.
The sharper kappa replaces total term count only in the exponent;
it is not automatically bounded for L657's growing-degree numerator.
Remark 4.9 reports the sharp small-value order for
P_(d,b)=product_i(z_i-1)^b: r^(1/b)*|log r|^(d-1).
This is a source-reported general obstruction to ignoring multiplicity,
not a countersequence in the present displaced rational family.

For L_infinity(P)=1, Proposition 4.10 gives, for epsilon>0,

    0<= integral [log(|P|^2+epsilon)/2-log|P|] dmu_A
       <= C_2(d,k,alpha)*epsilon^((1-alpha)/(2(k-1))),
    C_2=12*k^2*(18*d*k^2)^(d-1)*alpha^(1-d)/(1-alpha).

Its matrix A is integer m-by-d with m<=d and rho(A)>diam(P).
Section 2.2 defines rho(A)=infinity for zero integer kernel;
Section 2.3 explicitly identifies mu_(I_d)=mu_d. Thus the ordinary
two-torus is within this statement. The layer-cake proof retains
the singular logarithm; it does not remove boundary zeros. The bound
still depends on normalized P and k. It is not a relative comparison
of our two endpoints, or a bound uniform in our growing degrees.
The paper's fixed-P monomial-substitution convergence theorem likewise
does not cover coefficients moved by independently prescribed e_m.
No such representation or specialization is asserted in this review.

The PDFs' text supplied the hypotheses and relevant cases above. One
page-image request timed out; accessible text and the earlier inspected
proofs suffice, so this is not an essential source blocker. Lueck's
width-dependent bound, Dobrowolski's theorem and random-polynomial
integrability are reference leads only, not independently imported
results. No unread lead is needed to license this bounded test.

### Local reuse, duplicates and failures

Inspected L657's complete numerator/denominator and integrability
statement and clearing proof; L666's exact family and rational factors;
L692's sparse statement and proof Sections 1--5; and L694's hypotheses,
conclusion and norm-construction scope. L692 (2) explicitly retains
the sharper loss 4L*log(5*n^2/(2*L^2)), in addition to its coarser
n/400 payment. This existing inequality, with its support/onset
conditions, is the appropriate head input for a future attempt;
the displayed n/100 corollary alone is insufficient for an o(n) claim.
This review does not prove the head-tail implication or a new corollary.

Reuse step 110's Lev comparison in
`2026-11-03-anchored-fourier-gap-summable-shifts.md` and L694's audited
scope. Summability and the infinite distributional gap provide no
finite rational or negative-log estimate. Step 104's nonuniform-kernel
assessment already distinguishes unit residues from reciprocal
generating functions and qualitative sine type from finite costs.
No further source extraction for those unchanged facts is necessary.

The recorded failure
`ATTEMPTS/2026-11-03-signed-canonical-correction-inconclusive.md`
and step 105's working record were inspected. Its finite optimized
vectors depend on n and its angular means are uncertified; it is
neither a fixed-l1 asymptotic counterexample nor evidence that the
tail limit holds. Do not repeat that screen as this turn's test.
The low-moment-origin closure record concerns a different transfer
cost, not complete logarithmic stability under the present hypothesis.
No existing proof of this target was located by these scoped checks.

### Search record and decision

New queries (exact strings, 3 November 2026):

- `Mahler measure quantitative continuity polynomial degree perturbation coefficients Holder exponent`
- `Mahler measure logarithmic integrability sparse polynomials Lawton small values degree bound`
- `"Mahler measure" "continuity" "degree" perturbation`
- `"summable" "perturbations" "Mahler" measure logarithmic`
- `"logarithmic" "polynomials" "uniform integrability" degree growing coefficients`
- `"Mahler measure" "summable" perturbation`
- `"logarithmic mean" "Blaschke" residues perturbation`
- `"Mahler measure" "perturbation" "degree" continuity exponential`
- `"lattice" "summable perturbations" "logarithmic" sine product`

Results returned the compared Mahler sources, unrelated root-separation
and integer-polynomial estimates, area-potential convergence,
random-polynomial statements and half-plane Blaschke-product log norms.
The last groups were screened as leads only: no inspected theorem from
them is used. No exact fixed-profile finite-transfer result was found
within this bounded search. This does not establish novelty.

EXPLORE is appropriate: a family-specific analytic test is justified,
whereas IMPORT or SPECIALIZE would incorrectly imply source coverage
of its missing tail estimate. A future attempt must check the proposed
head payment and its implication, then prove the displayed ordered
tail limit, give a useful explicitly qualified partial estimate, or
produce an actual fixed real l1 countersequence with linear loss along
an unbounded subsequence. A mere restatement of regularization,
pointwise closeness, or finite losses does not count as that evidence.
The tail test is sufficient only after the remaining head and limit
logic is justified. No uniform tail rate is assumed.

Recommend proof_attempt/creative for one such bounded test after the
supervisor's separate approval of this newly completed assessment.
The precise new obstruction is the negative logarithmic mass near zeros
of growing-degree responses despite a small summable displacement tail.
This matters to the finite-charge transfer from L694, while full-cube,
H/support, actual-Xi realization and mixed positivity remain separate.
Mathlib: reuse the supporting root-formula names recorded in the prior
Mahler assessment; full matching coverage for this head-tail target is
unchecked. No new formal-coverage claim or mathematical result is made.
