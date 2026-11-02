# Two-frequency signed arithmetic form: completed source comparison

TARGET: Assess source coverage for a uniform Gram formula or spectral sign test for integral w_XT W |a_1+a_p p^(-it)|^2 (c0 Z+c1 Z'/log T)^2, with p prime in [T^(1/22),2T^(1/22)], retaining all six twisted main terms and the Xi completion.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the signed-window and height-weight assessments and checked the L575, joint-character, mollifier and pure-height stops; searched exact signed/twisted and amplified-Laguerre terminology and read the primary theorem scopes below. No exact amplified signed Gram theorem was identified in the sources inspected; no novelty or exhaustive absence claim.
SOURCE_EVIDENCE: Hughes–Young arXiv:0709.2345v2 Theorem 1.1/(11)–(17), printed pp. 3–5, Section 6.5 Lemma 6.9/(139)–(155), pp. 22–24; bramble_trace paper 36 v4 Theorem 6/(20)–(23) and Section 7/Theorem 8; Bettin–Bui–Li–Radziwill arXiv:1609.02539v1 Theorems 1.1–1.2, pp. 2–4; Bui–Hall–Subira Jorge arXiv:2511.14415v1 Theorem 1.1, Section 3/Theorem 3.1 and Section 4.6 Cauchy passage; bramble_trace paper 41 v4 Theorems 2–2a. Exact URLs, hypotheses, inspected cases and limits below.
COMPARISON: Hughes–Young provides an admissible finite-twist complex-shift source for this coefficient convention. The untwisted positive kernel and stronger amplified theorems do not directly decide the growing-prime signed Xi form. A bounded specialization, rather than a new arithmetic theorem or assumed Gram representation, is justified.
GAP: The later calculation must bound the growing-prime local factors on collision-safe shift contours, extract the fixed Hardy jets, retain absolute phase and Xi-curvature errors, and compare the resulting spectral margin with those errors. No matrix, local-factor estimate, spectral sign or completed-Xi asymptotic is established here.
REASON: Essential source coverage is sufficient for one finite-twist specialization. Import the arithmetic theorem and reuse L619 for its untwisted application; do not reprove the divisor theorem or infer a sign from nonnegative amplifier weights.

LITERATURE_REASON: The invocation-start assessment was REVIEW_REQUIRED for the new growing-prime signed scope; the missing local arithmetic-factor, coefficient-normalization and amplified-sign comparisons are supplied in this turn.
SCOPE: Literature-only review of the original nominated form, with H=T, X in [T,2T], prime p in [T^(1/22),2T^(1/22)], arbitrary normalized complex (a_1,a_p) and normalized real (c0,c1). The original nomination below is preserved as historical scope; its pending-review language is superseded by the completed comparison.

Use the w,T,X conventions of L619 with H=T, W=D_1(Xi;t)/A(t)^2,
Z=-Xi/A and L=log T from L471. Normalize
|a_1|^2+|a_p|^2=1, c0^2+c1^2=1, with a_1,a_p complex and
c0,c1 real. The displayed integral is real. This specifies a source
question, not a claimed asymptotic or a derived finite matrix.

Main gap: pointwise first signs at unbounded heights and all-degree
mixed positivity for actual Xi. Downstream use: a source-controlled
arithmetic signed form can test a constraint invisible to pure height
mass. A negative main direction would need a proved error smaller
than its size before implying any actual sign failure; nonnegativity
would give only an averaged constraint, with localization and higher
signs still unresolved. No resolution or candidate is nominated.

Bounded source test: inspect the exact primary six-term arithmetic
factors and relevant amplified signed-form theorem statements, reuse
the existing assessments, and decide whether they supply a known
nonnegative Gram representation or enough uniform error control for
one later two-frequency spectral test. Stop or rescope if a known
result already settles that test, or if the proposed leading scale
cannot be distinguished from the source error. Do not compute the
new form before this comparison. Check the L575, joint-law and pure
height stops as contrasts; do not transfer them to this new scope.

This is preparation for a possible new sign-sensitive mechanism,
not yet a justified creative proof attempt. It may turn out to be
routine specialization or a known obstruction; choose proof-purpose
routing only after the source comparison. No source approval is
claimed merely from writing this assessment.

Mathlib: full matching coverage not checked. No cross-notebook input.

## Completed comparison — 1 November 2026

### Relevance and local overlap

The precise unresolved main claim remains actual-Xi all-degree mixed
positivity, including pointwise first signs at unbounded heights. The
intermediate target is the sign and source error of this arithmetic
signed average. It can test a correlation absent from a pure height
weight. Even a uniform positive answer would leave exceptional heights,
localization, higher signs and RH unresolved. No RH candidate is proposed.

Reused the completed signed-window and height-centered assessments;
read the full L619 proof, L620's statement and relevant twist argument,
L471's amplitude/Hardy normalization, and L575's statement. Read the
joint-two-prime, short-mollifier and pure-height failure records in
ATTEMPTS. Reused the joint-Hardy-law and paired-height source assessments.
L575 stops a particular absolute fixed-square defect; L620 stops pure
height concentration. The fixed log-2/log-3 cubic positive measure and
specified short mollifier concern different observables/limits. None
provides this growing-prime, fourth-degree signed statistic. Preserve all
those stops; a historical stop is not transferred to the present scope.
L619 and L620 remain unaudited in their full stated scopes.

### Primary arithmetic input and its exact limits

C. P. Hughes and M. P. Young, *The twisted fourth moment of the Riemann
zeta function*, J. reine angew. Math. 641 (2010), 203–236,
[arXiv:0709.2345v2, Theorem 1.1/(11)–(17), printed pp. 3–5](https://arxiv.org/pdf/0709.2345v2#page=3).
The retrieved PDF labels itself v2, 27 September 2007, with a separate
26 November 2024 compilation date. This is the version inspected.

It treats integral w(t)(h/k)^(-it) times four zeta factors, two at
positive height with shifts alpha,beta and two at negative height
with shifts gamma,delta. It assumes coprime h,k, hk<=T^(2/11-eta),
complex shifts O(1/log T), nonnegative smooth w supported in [T/2,4T]
with j-th derivative O_j(T0^(-j)), and
T^(1/2+eta)<<T0<<T. The stated absolute remainder is
O(T^(3/4+eta)(hk)^(7/8)(T/T0)^(9/4)); the prefactor
1/sqrt(hk) belongs only to the complete six-term main integral.
The introductory paragraph before (12) explicitly permits shift
 differentiation. The remarks after (17) explain complete-sum holomorphy
and point to CFKRS Lemma 2.5.1. They do not assert positivity of its
signed derivatives. All six permutations in (17) were inspected.

The arithmetic factor is the common four-zeta quotient (12) times
the finite Euler product (14). Import (14) exactly: its h-side
increments the (gamma,delta) divisor function, and its k-side increments
(alpha,beta). Read Section 6.5, Lemma 6.9 and its full geometric-series
proof (139)–(155), printed pp. 22–24, including the h/k interchange.
The series definition (14), rather than separately singular closed
quotients at coincident shifts, is an appropriate source for the later
uniformity check. No expansion or estimate of this factor at a growing
prime was made here. In particular p^(-alpha) is not replaced by 1;
small shifts alone do not license discarding its dependence on p.
The underlying divisor theorem, arithmetic identities and complete
permutation-sum holomorphy are named imports, not independently audited.

The support and smoothing match H=T in the current form. The source
allows individual growing twists, and L620 already handles the sign
and coefficient convention. A future application still must exhibit
one fixed positive eta with a uniform length margin for every twist
in the finite square, retaining both conjugate cross terms. Using the
individual theorem avoids an unjustified coefficient-growth corollary.
This is a source applicability comparison, not a derived signed formula.

### Why stronger or positive statements do not supply the answer

bramble_trace, *Signs and uniform filtered positivity in fourth moments
of Hardy's function*, [paper 36, displayed v4, 21 October 2026](https://rstation.ai/problems/riemann_hypothesis/papers/36),
Theorem 6/(20)–(23) proves a positive quadratic form for a real linear
derivative filter. Its sine-kernel proof and Theorem 8's opening
explicitly use the untwisted case h=k=1. Reuse the full Section 7
phase/complex-contour comparison recorded in the signed-window review
and L619. It is not a signed positivity theorem for an extra arithmetic
amplifier. Its scalar coefficient margin can be retained in a later
perturbation test; no amplified Gram representation is imported.

S. Bettin, H. M. Bui, X. Li and M. Radziwill, *A quadratic divisor problem
and moments of the Riemann zeta-function*, JEMS 22 (2020), 3953–3980,
[arXiv:1609.02539v1, Theorems 1.1–1.2, printed pp. 2–4](https://arxiv.org/pdf/1609.02539v1#page=2).
Read the complex-shift, smooth-support and coefficient hypotheses,
the complete six-term conclusion, its error
O_epsilon(T^(1/2+2vartheta+epsilon)+T^(3/4+vartheta+epsilon)),
and the remarks on averaging and length vartheta<1/4. Its Dirichlet
polynomial is sum alpha_n/n^s with alpha_n<<n^epsilon, and similarly
for the second coefficient sequence. The present convention is
sum a_n n^(-it). Matching it on the half-line introduces sqrt(n)
in the source coefficients. Consequently the displayed theorem cannot
be invoked directly with an implied coefficient constant uniform in
this normalized growing-prime family. Rescaling and tracking constants
would be extra work; it is unnecessary because individual Hughes–Young
twists already cover the bounded test. No coefficient-uniform improved
error is imported from this stronger length theorem. Theorem 1.2's
smoothed diagonal structure also does not state signed Gram positivity.
Its arithmetic proof was not re-audited; only its exact theorem scope
and explanatory remarks are used in this comparison.

H. M. Bui, R. R. Hall and M. Subira Jorge, *Amplified fourth moment of
the Riemann zeta-function and applications*,
[arXiv:2511.14415v1, 18 November 2025](https://arxiv.org/html/2511.14415v1),
Theorem 1.1, uses four amplifier factors from the specific family
sum_(n<=y) d_r(n) P(log(y/n)/log y)n^(-s), fixed polynomial P,
r in N, y=T^vartheta and vartheta<1/8. Read its small complex-shift
uniformity, Section 3/Theorem 3.1 source use and Section 4.6's
normalized Cauchy extraction. The theorem's error is
O(T(log T)^(4(r+1)^2-1)). This is not a statement for arbitrary sparse
normalized coefficients or for the present two-amplifier signed
Laguerre product. Neither its long integral expression nor its
zero-gap application is a universal signed Gram certificate.
This resolves the earlier unread amplified-fourth-moment lead for
this comparison; no new large-gap or amplifier-family target is chosen.

bramble_trace, *Generalized Laguerre positivity at growing orders*,
[paper 41, displayed v4, 24 October 2026, Theorems 2–2a/(6a)–(7B)](https://rstation.ai/problems/riemann_hypothesis/papers/41),
was checked after its v3 appeared in exact signed/amplified searches.
Theorem 2 has arbitrary n^(-it) coefficients and a positive arithmetic
mean, but requires m=2p+1 with m/log T tending to a fixed
alpha in (0,1/2), length T^theta with theta<nu-rho(alpha),
H=T^nu and fixed parameters. Theorem 2a also fixes a positive limiting
order ratio and has a complementary length range. These are quadratic
Laguerre means at growing order, not the present fixed first-order
four-factor statistic. Letting alpha tend to zero or absorbing the
Z/Z' observer into an independent Dirichlet polynomial is not authorized.
Only this excluding theorem scope is used; no proof or new zero-free
claim from paper 41 is imported, and the fixed-half-plane baseline
need not be reopened for this target.

### What the next mathematical test may and may not do

The precise difference from a citation is a fixed finite-twist
specialization with the full Hardy/Xi transfer. Use L619's fixed
untwisted comparison and L471's zero-safe identity, with every
coefficient normalization explicit. On normalized shift variables,
keep complete holomorphic sums on separated contour radii before
extracting the derivatives; do not differentiate a remainder stated
only on real shifts. The prime factors require their own uniform
bound there. Keep log p/log T in their exponentials. Retain
Cauchy factors for the ordinary derivative orders and use the
normalization by log T for the jet observer.

The raw source error to specialize remains
T^(3/4+eta)(hk)^(7/8), since H=T. The signed integral's comparison
scale is T(log T)^6 from L619. A prospective negative spectral
conclusion requires an absolute error smaller than that negative
margin, not merely an o(1) remainder of unknown relevance. The
1/log T Hardy phase cost need not be small relative to a decaying
off-diagonal arithmetic term; in that case it cannot certify the
term's fine sign. A coarser perturbation test of the full positive
diagonal margin is a permissible alternative within this same
spectral question. The arithmetic-size and error comparisons are
left for the mathematical turn, including any exponent arithmetic.

For completion use the identity in L471,
W=Z'^2-Z Z''-(log A)'' Z^2, including real zeros. L619 retains
its curvature error and a positive coefficient margin. The new
arithmetic weight must be included in the absolute bounds. No
curvature sign, vanishing negative mass, localization or uniform
pointwise positivity follows just from these source inputs.

Continue with one bounded calculation if the contour/local-factor
bounds and absolute errors permit a spectral decision. Stop this
specific growing-prime sign-detection mechanism if uniform positivity
is certified; retain an informative failure if the errors mask the
candidate margin. A negative formal direction would require a
separate exact-hypothesis/error review before any claim about actual
Xi signs. No matrix, bound or sign has been calculated in this turn.

The continuation is nominated in
[the specialization assessment](2026-11-01-two-frequency-signed-specialization.md).
Its newly written ready coverage remains subject to the supervisor's
separate next-turn approval. This does not alter the completed review.
A creative central attempt is not yet justified: this finite-twist
specialization is reproduction, and an independent mechanism capable
of removing exceptional heights has not been supplied. Do not label
it creative to meet a routing preference or repeat it after its test
settles without a materially different input.

### Search/access record and classification

Queries actually used included: `"Hardy" "Laguerre" "amplifier"
positivity fourth moment`; `"amplified fourth moment" "derivatives"
Hardy function`; `"Hughes" "Young" "twisted fourth moment" arithmetic
factors 0709.2345`; `"Hardy" "Laguerre" "amplified" positivity`;
`"Hardy" "signed" "twisted fourth moment"`; `"Laguerre" "Dirichlet
polynomial" positivity`; and `"Z'" "ZZ" "Gram" "Hughes"`.
Nonmatching orthogonal-polynomial and other general hits were not
used as evidence. No search failure proves absence or novelty.
The requested 1609.02539v2 HTML returned 404; its v1 primary PDF was
retrieved and its exact theorem read, so there is no essential source
access blocker. Other primary sources were readable through browsing;
no local PDF download or screenshot verification is claimed.

Completed kind LITERATURE, classification NOVELTY_UNCHECKED, task
literature_comparison, outcome EXPLORATION. The new evidence is the
exact scope comparison and adequate source base for a finite-twist
test, not a new mathematical input or an RH advance. Mathematical
exploration usage is zero in this literature-only step; no counters
or supervisor state are changed. Mathlib matching coverage is
unchecked/unknown, not claimed absent. No cross-notebook input.
