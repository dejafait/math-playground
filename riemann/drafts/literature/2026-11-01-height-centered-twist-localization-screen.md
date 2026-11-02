# Height-centered arithmetic localizer: completed source comparison

TARGET: Assess whether height-centered Dirichlet-polynomial weights of length N<=T^(1/11-epsilon) can localize L619's signed average to a 1/log T interval, retaining the twisted-source error and coefficient-uniform concentration costs.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the named signed-window, joint-law and paired-height assessments; searched Dirichlet-polynomial concentration, microscopic interval mass and Montgomery–Vaughan mean squares; retrieved the original mean-square corollary, its proof passage and an author restatement, then compared Hughes–Young's individual-twist hypotheses and error. Exact queries and access qualifications appear below; no novelty or exhaustive absence claim.
SOURCE_EVIDENCE: Montgomery–Vaughan, Hilbert's inequality, JLMS (2) 8 (1974), Corollary 3/(1.11), p. 75, Section 4 p. 82, https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf; readable formula checked in Vaughan's 2025 Math 597-05 Chapter 26, PDF p. 10, https://personal.science.psu.edu/rcv4/597-5f25/Class597-26.pdf#page=10; Hughes–Young arXiv:0709.2345v2 Theorem 1.1/(9)–(17), printed pp. 3–5, https://arxiv.org/pdf/0709.2345v2#page=3, including all six terms and holomorphy remarks.
COMPARISON: The primary mean-square theorem supplies coefficient-uniform quadratic normalization, and Hughes–Young supplies a uniform individual-twist error. Neither source states the exact weighted microscopic mass fraction or its error summed under this notebook's coefficient normalization. These are bounded specializations of known inputs, not grounds for claiming new arithmetic mathematics or a twisted version of L619's positive form.
GAP: Apply the mean-square input to the fixed smooth denominator and elementary finite-dimensional numerator bound; justify height translation, coprime reduction and the actual coefficient-summed Hughes–Young remainder. No resulting concentration rate or summed error has been derived this turn. Transfer to signed W U_P^2 remains outside the approved diagnostic.
REASON: Essential source coverage for the saved concentration-and-error test is now adequate. A later mathematical step may specialize these inputs for the same target, importing their arithmetic proofs; it may not assume concentration, main-term positivity or signed localization.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED because the primary coefficient-uniform mean-square input and comparison with the twisted error had not been inspected; this turn fills that specific missing scope.
SCOPE: Fixed 0<epsilon<1/11, H=T, X in [T,2T], the fixed nonnegative smooth w of L619, a fixed u0 in (0,1) with w(u0)>0, t0=X+u0 T, N<=T^(1/11-epsilon), and M(t)=sum_(n<=N) a_n exp(-it log n) with sum |a_n|^2=1; coefficients may depend on T,t0. No inverse mollifier or assumed jet probability law.

The original nomination below is retained. This literature-only turn
supplies source coverage; it does not perform its mathematical diagnostic.
No new mathematics about this family was derived during the L619 audit
or this source review.

The bounded diagnostic is the maximum, over the stated coefficient
vectors, of the fraction of the w_XT |M|^2 mass in
|t-t0|<=1/(2 log T). A pure height-concentration mechanism would
need a fraction bounded away from zero, as well as a controlled
Hughes–Young remainder after summing the twists with their actual
coefficient weights. Do not assume that the length condition alone
controls that summed remainder. Any needed coprime reduction must
be justified from the primary theorem.

The source comparison below identifies a covered bounded test
with its unresolved assumptions. A vanishing concentration upper
bound would stop this pure height-weight mechanism; it would not
exclude every joint arithmetic-and-jet weighting. A positive weight
concentration result would still require control of the actual signed
integrand and its completion. Neither outcome is assumed here.

Essential local inputs for any later application are L619, L018 and
L471. L477/L575 and the joint-law/mollifier stops are contrasts only.
Reuse `2026-11-01-signed-short-interval-hardy-correlation-screen.md`,
`2026-10-31-joint-hardy-jets-negative-mass.md` and the narrow
paired-height comparison before searching. The primary concentration
input inspected below is now available for citation. No cross-notebook
input or matching Mathlib coverage is asserted.

## Main gap and decision boundary

The main gap remains actual-Xi all-degree mixed positivity, including
initial signs at unbounded heights. The intermediate test asks whether
this pure height weight can resolve a prospective negative interval.
Its downstream use is to accept or reject that necessary feature before
developing a signed twisted-moment transfer. That transfer, higher signs,
multiplicities, endpoints and effective height overlap remain unresolved.

Reused the signed-window source comparison, joint-law failure boundaries
and paired-height theorem comparison named above. Read L619's hypotheses,
conclusion and admissible-parameter section. L477/L575 are contrasts, not
concentration inputs. The earlier finite-law and mollifier stops do not
decide this precise coefficient-normalized weight test; no earlier answer
was found in those scoped checks.

Continue with one bounded specialization of the cited inputs. A vanishing
maximal microscopic mass fraction stops this pure height-weight localizer;
a controlled arithmetic error cannot repair that failure. If concentration
survives, signed-integrand transfer is a separate uncovered target. This
is not a stop on every arithmetic/jet weight.

## Primary mean-square input

H. L. Montgomery and R. C. Vaughan, *Hilbert's inequality*, J. London
Math. Soc. (2) 8 (1974), 73–82,
[DOI 10.1112/jlms/s2-8.1.73](https://doi.org/10.1112/jlms/s2-8.1.73),
[author scan, Corollary 3/(1.11), p. 75](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf#page=3).
The hypothesis is sum n|b_n|^2 finite; the error constant is absolute.
For arbitrary finite complex coefficients the assertion is

    integral_0^Y |sum_(n<=N) b_n n^(it)|^2 dt
      =Y sum_(n<=N)|b_n|^2+O(sum_(n<=N) n|b_n|^2),  Y>0.

The original scan's extracted equations are incomplete. The formula was
independently read in R. C. Vaughan's author-hosted
[Math 597-05, Chapter 26, dated 2 October 2025, PDF p. 10](https://personal.science.psu.edu/rcv4/597-5f25/Class597-26.pdf#page=10),
which explicitly permits arbitrary complex coefficients. This is a
primary author restatement, not a search-snippet reconstruction.
Ivić, *Lectures on Mean Values of the Riemann Zeta Function* (TIFR,
1991), printed p. 6/(1.15), was also inspected and agrees; it is not
the primary input used to approve this test.

Read the original Theorem 2/Corollaries 2–3 hypotheses, pp. 74–75,
and their finite-sum proof passage in Section 4, p. 82: expansion and
integration of the square, two Hilbert forms for the off-diagonal, and
reduction from series to finite sums by mean-square convergence. Only
the finite case is needed. The underlying Hilbert inequality is imported,
not re-proved or independently audited. No optimal constant is needed.
The notes' weaker Theorem 26.A is only an upper bound and cannot replace
the two-sided error needed for the denominator.

Arbitrary finite coefficient vectors may be chosen anew at each T,t0.
The next specialization must explicitly handle the negative exponential,
height translation and nonconstant smooth weight. The source does not
state a weighted denominator for L619. Use a fixed positive subinterval
of w or justify weighted integration; do not silently replace that
denominator by T. Finite-dimensional Cauchy–Schwarz is an available
numerator estimate. Their combination, its uniform rate and any onset
remain mathematical work. A sharper concentration theorem is not an
essential missing source for this diagnostic.

## Primary twisted-moment scope

Reuse the six-term assessment in the signed-window review. Newly read
Hughes–Young (9)–(11), Theorem 1.1/(16)–(17) and its printed pp. 4–5
remarks. For a smooth nonnegative weight supported in [T/2,4T], with
j-th derivative O_j(T0^(-j)), its hypotheses are
T^(1/2+eta)<<T0<<T, coprime h,k with hk<=T^(2/11-eta), and four
complex shifts O(1/log T). The error for one twist is

    O(T^(3/4+eta) (hk)^(7/8) (T/T0)^(9/4)).

The 1/sqrt(hk) in (17) multiplies the main integral, not this error.
All six main terms retain their h,k-dependent arithmetic factors (14)–(15).
Only their complete sum is removable at shift collisions. No positivity
is imported for the twisted main expression, and the arithmetic proof
remains a named import.

The H=T weight is smooth on scale T and supported in [T,3T], fitting
the stated source scope. Choose eta with margin relative to the target's
fixed epsilon; do not silently identify them. Applicability to every
reduced twist, including the diagonal, must be checked in research.

The source writes M(1/2+it) in (9)–(10), whereas our polynomial is
sum a_n n^(-it). Match coefficient conventions explicitly: do not insert
an artificial 1/sqrt(mn) in our square expansion. Using the individual
twist theorem (16) avoids an unstated coefficient-growth assumption for
a summed corollary. The remark after (17) licenses summation but does
not state the coefficient-normalized error required here.

Next expand the finite square, reduce each ratio to coprime h,k, retain
coefficient multiplicities, sum absolute individual errors and compare
with the correct T scale. These algebra and exponent checks are
unperformed. Fixed-order normalized shift differentiation stays within
the complex-shift scope but must retain its Cauchy factors if used.
No differentiated twisted-Xi asymptotic is needed for the pure weight
screen, and none is approved here. L619's untwisted B_1(P) is not a
twisted main term; its curvature estimate is not automatically uniform
under the added weights. Concentration alone cannot transfer signed
W U_P^2 to a selected height.

## Search record and qualifications

Queries used included `Montgomery Vaughan 1974 Hilbert inequality mean
value Dirichlet polynomial T O sum n an squared pdf`, `Dirichlet
polynomials concentration short interval mean square Montgomery Vaughan
lower bound`, `Hilbert's Inequality Corollary 2 1974 Dirichlet`,
`Dirichlet polynomial concentration interval mean square`, `Dirichlet
polynomials mass short interval concentration`, and author-site searches
for the original paper. The exact original mean-square citation is
Corollary 3, not the Corollary 2 suggested by an early search lead.
Other returned short-interval and large-value results were leads only;
no stronger microscopic concentration theorem is attributed to them.
The primary inputs above suffice for an elementary comparison. A failed
exact-match search supplies no novelty claim.

The Wiley DOI endpoint was inaccessible. Browser PDF screenshots did
not supply inspectable images; a second interface explicitly reported
screenshot unavailability. A local download failed with DNS resolution
error. The original hypotheses/proof prose and the author's readable
formula were nevertheless retrieved through browsing; no essential
source blocker, visual verification or local PDF download is claimed.

Mathlib: full matching mean-square, concentration and twisted fourth-
moment coverage was not checked; no absence or formalization claim.
No new lemma, mathematical script, mass bound or summed error was
derived. The local progress is primary coverage for one bounded
specialization of the unchanged saved target, not a new mathematical
discovery or an RH candidate.
