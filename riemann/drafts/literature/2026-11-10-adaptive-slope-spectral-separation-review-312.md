# Degree-dependent signed slope separation — source assessment

TARGET: Assess whether degree-dependent signed slope measures of subexponential total variation can retain L997's selected quartet while uniformly suppressing the competing family 7/8+i*gamma for 7/4<=gamma<=9/4.
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Step313 completed bounded exact-kernel, norm-constrained filtering, extremal polynomial, quantitative Runge, superoscillation and propagation-of-smallness searches. Read primary statements and relevant proof cases below; reused the identified earlier assessments. No adequate match or decisive impossibility theorem was established, and no novelty follows.
SOURCE_EVIDENCE: Sete–Liesen arXiv:1502.07633v1 Propositions3.2–3.3 pp5–7; Candes–Fernandez-Granda arXiv:1203.5871v3 Theorem1.2 p5, Proposition2.1 pp15–16, PropositionA.1 p39; Kovrijkine math/0012186v1 Lemma1 pp4–6; Friedland–Yomdin Studia Math218(2013) Theorems1.1/1.3 pp27–30. Reuse review291 and the earlier Runge/superoscillation assessments on their stated scopes; details and access qualifications below.
COMPARISON: Polynomial minimax theory supplies continuum suppression in a polynomial class but no realization by these measures or TV cost. TV Fourier recovery uses a different measurement operator. Analytic propagation requires a justified normalized scalar family and complex-growth control; finite-exponential-sum bounds require order control. None decides the complete quartet assay. L997's fixed positive weight cannot be promoted to an n-dependent complex-measure obstruction.
GAP: Establish or obstruct simultaneous exact selected normalization, subexponential TV and uniform exponential competing suppression for the unchanged assay. The operator realization and quantitative costs are mathematical work, not missing source statements. Actual reconstruction, sign recovery and infinite-zero control remain independent gaps.
REASON: A materially different independently testable localization mechanism after the audited fixed-filter failure. The bounded source comparison now permits one mathematical attempt under EXPLORE; no new lemma, formula for the filtered response, mathematical script, existence result or impossibility result was produced in this literature turn.
LITERATURE_REASON: Degree-dependent signed measures and uniform suppression of a continuum of higher-beta competitors lie outside review291's fixed positive bump and two fixed inputs.
SCOPE: The unchanged finite assay below, including arbitrary finite complex Borel measures, both closed intervals, all quartet terms and K_(n+2)'s -1. Approves a constructive or dual/analytic obstruction attempt with explicit norm and uniform-error accounting; no general Fourier-model replacement or actual-zero transfer is preapproved.

## Exact finite assay preserved from the step312 nomination

Use L997's exact a_n(c;eta), original K_(n+2) including its -1,
complete quartet Q(eta), r=2, n>=2, A=7/4, B=9/4,
eta_0=3/4+i and the same z_0(c). The next review must read the
relevant canonical definitions and audited L997 proof ranges before
using its conclusions; no variable-measure claim follows from it.

Ask whether finite complex Borel measures nu_n on[A,B] exist with,
for every sufficiently large integer n,

    integral_A^B z_0(c)^n*a_n(c;eta_0) dnu_n(c)=1,
    sup_(7/4<=gamma<=9/4)
      |integral_A^B z_0(c)^n*a_n(c;7/8+i*gamma) dnu_n(c)|
                                            <=C*exp(-delta*n),

where C<infinity, delta>0 are fixed and, for every epsilon>0,

    ||nu_n||_TV<=C_epsilon*exp(epsilon*n),

with finite C_epsilon independent of n. Measures may depend on n
and these fixed assay data, never on actual unknown zeros. Complex
signed measures allow phase cancellation; conversion back to real
one-sided forcing remains an independent obligation. Retain every
quartet term, band endpoint and constant subtraction. These are
hypothetical finite inputs, not asserted actual zeta zeros.

A passing assay would identify a controlled localization resource
to examine before actual-zero reconstruction, not sign L984(H).
An exponential lower norm cost, incompatible normalization, or
unavoidable uniform competing leakage would stop this assay.
Canceling eta_1 alone, fitting finitely many ordinates, or failing
one construction is inconclusive. Preserve L997's original failure.

## Source gate and bounded decision

Check exact/stronger results under exponential type, extremal
approximation, analytic continuation and norm-constrained spectral
filtering terminology. Reuse ready Laguerre/inversion assessments.
Inspect primary hypotheses, uniform domains and essential cases;
generic approximation without norm cost is insufficient. Cite known
general theorems rather than reprove them. Approve a mathematical
assay only with a concrete test of these thresholds; otherwise park
or refine with a materially new input. Mathlib coverage is unknown.

The step312 nomination proposed a later proof_attempt/creative:
degree-dependent signed filtering addresses the audited exponential
leakage obstruction to localization, relevant to L966/L968 forcing.
The bounded decisive test is the simultaneous normalization, norm
and uniform-suppression requirement above. At step312 no creative
mathematical attempt was approved; source comparison was required.

Essential local inputs: L997's exact response and audited fixed-bump
conclusion, review291/stop293, and only needed L994/L995 contracts
through their existing assessments. No cross-notebook input.
Actual infinite-zero complements, regulator uniformity, both signed
outputs, L993 recovery, L984(H) and L030-L032/C032a remain open.

## Completed literature-only comparison — step313, 10 November 2026

This approves an attempt on the exact TARGET, not the desired conclusion.
The three simultaneous requirements and their quantifiers above are unchanged.
In particular, a fixed positive exponential TV allowance is insufficient:
the same sequence must meet every positive epsilon allowance. No finite
list of ordinate cancellations settles the uniform closed-interval test.

### Primary theorem contracts and remaining differences

**Extremal polynomial filtering.** O. Sete and J. Liesen,
[*Faber–Walsh polynomials and polynomial approximation problems on two
disjoint intervals*, arXiv:1502.07633v1, 26 February 2015](https://arxiv.org/pdf/1502.07633v1),
Definition3.1/Proposition3.2 pp5–6 and Proposition3.3 with complete proof
pp6–7. Proposition3.2 assumes a compact E without isolated points, connected
finitely connected exterior, and its Green function G with pole at infinity.
For a constraint point z_* outside E, the optimal root-rate for polynomials
of degree at most k satisfying p(z_*)=1 is exp(-G(z_*)). Proposition3.3
constructs asymptotically optimal normalized Faber–Walsh polynomials when
E is a finite union of mutually exterior simply connected nonpoint compact
sets. The proofs compare approximation of a simple pole, capacity and
Green-level curves. This is stronger than finite-point fitting. It controls
the polynomial sup norm, not coefficients or a representing slope measure's
TV. No identification of our full response with this polynomial class has
been proved. Use the theorem only after a norm-controlled realization is
justified; it does not establish either side of the assay.

**TV minimization and a continuum certificate.** E. J. Candes and
C. Fernandez-Granda, [*Towards a Mathematical Theory of Super-Resolution*,
arXiv:1203.5871v3, 14 November 2012](https://arxiv.org/pdf/1203.5871v3),
Theorem1.2 p5, Section2.1/Proposition2.1 pp14–16 and PropositionA.1 with
full proof p39. A finite atomic complex measure on the circle, with
wrap-around separation at least 2/f_c and f_c>=128, is uniquely recovered
by minimizing TV subject to its Fourier coefficients |k|<=f_c. The dual
trigonometric polynomial interpolates every prescribed unit phase at the
support and has modulus strictly below one off it. The proof separately
handles nearby and distant locations; AppendixA handles general competing
complex measures by polar decomposition. These are genuine continuum
certificates, but their measurement functions are Fourier monomials. Our
unknown is the filter measure, and its constraints involve an n-dependent
Laguerre quartet operator. Neither the separation hypothesis nor the
certificate transfers automatically. Strict off-support inequality also
does not assert our exp(-delta*n) rate. No recovery or TV bound is imported
for this operator.

**Analytic propagation without an atom-count hypothesis.** O. Kovrijkine,
[*Some results related to the Logvinenko–Sereda theorem*,
math/0012186v1, 19 December 2000](https://arxiv.org/pdf/math/0012186v1),
Lemma1 and full proof pp4–6: phi is analytic on D(0,5), I is a real
length-one interval containing zero, E is a measurable positive-measure
subset of I, |phi(0)|>=1, and M=max_(|z|<=4)|phi(z)|. Then

    sup_I |phi| <= (C/|E|)^(log(M)/log(2))*sup_E |phi|,

with absolute C. The proof uses Blaschke removal, Harnack, polynomial
Remez and Jensen; its Lp corollary is not needed here. This is available
for an exactly justified analytic response, without approximating an
arbitrary measure by finitely many atoms of controlled number. Our
selected quartet normalization is not automatically the normalization
of a scalar analytic continuation of the competing family: conjugate
and reflected entries must all be tracked. Its complex growth and the
resulting constants must also be paid. Theorem1's global Fourier-support
version requires thickness on every interval; a single finite stopband
does not supply that hypothesis. These tools leave a quantitative test,
not an automatic contradiction.

**Finite exponential sums and sampling limits.** O. Friedland and
Y. Yomdin, [*An observation on the Turan–Nazarov inequality*,
Studia Mathematica218(2013),27–39](https://www.impan.pl/shop/publication/transaction/download/product/89801),
Theorem1.1 p27, Definition1.2/Theorem1.3 pp28–29 and complete proof with
Lemma2.1 p30. For p(t)=sum_(k=0)^m c_k exp(lambda_k*t), complex coefficients
and exponents, and measurable positive-measure Omega in a real interval J,

    sup_J |p| <= exp(|J|*max_k|Re(lambda_k)|)
                 *(C*|J|/|Omega|)^m *sup_Omega |p|.

Their extension replaces |Omega| by positive metric span, which depends
on order, interval length and maximal imaginary frequency. It uses
sublevel-component counts and covering numbers; it is not unconditional
discrete sampling. Arbitrary slope measures are not a fixed-order
exponential sum, and no uniform order/approximation cost is supplied.
The original source is F. L. Nazarov, Algebra i Analiz5(4)(1993),3–66,
TheoremI p5 and Section1.4; its complex-exponent discussion is Section4.1
pp57–59. The original PDF's extracted formula symbols were damaged;
the displayed contract was read in the precise English primary paper above.
No new all-measure lower bound follows.

**Quantitative approximation and superoscillation costs — reuse.** Reuse
the inspected contracts in
[the earlier Runge/superoscillation assessment](2026-10-30-genuine-positive-class-runge-flux-test.md),
items1–4, and
[the Hardy-translate cost assessment](2026-11-01-hardy-translate-localization-cost-review.md),
its scope comparison. They cover polynomial-shape bandlimited
approximation and finite interpolation, with their stated norm and access
qualifications, not this Laguerre operator with subexponential TV.
Ruland–Salo's [author manuscript](https://users.jyu.fi/~salomi/pub/Classical_Runge_L12.pdf),
Theorems2–3 pp1–2, Section4 pp6–8, was also checked at the changed interface:
nested bounded Lipschitz domains in dimension at least two, connected
outer-minus-inner closure, an open boundary patch, symmetric uniformly
elliptic bounded coefficients (Lipschitz for dimension at least three),
bounded potential and no zero Dirichlet eigenvalue. It gives interior L2
approximation with boundary H^(1/2) cost, improved for a target extending
to an intermediate domain. Proposition5.1 and proof pp8–9 give exponential
cost for particular harmonic targets. This neither proves existence for our
operator nor a universal lower cost for all selected data. No PDE model
or change of norm is silently imported.

The standard named complex Hahn–Banach extension theorem and
Riesz–Markov–Kakutani representation theorem for C([A,B]) with its sup
norm are also available. They relate bounded functionals to finite regular
complex Borel measures and their TV norms. They do not themselves produce
a separating functional with the needed cost. Any proposed exact duality,
closure or compactness argument still needs its hypotheses verified.
No such specialization is proved in this source review.

### Search, duplicates, failures and access

Queries included `signed measures exponential polynomials filter uniform
approximation total variation superoscillations lower bound`, `quantitative
Runge approximation Laplace transform norm control spectral filtering
exponential cost`, `Bernstein Walsh theorem polynomial approximation
separated compact sets potential theory`, the exact titles above,
`Kovrijkine Some results related Logvinenko Sereda theorem lemma analytic
function disk 4 pdf`, `"Laguerre" "signed measures" "filter"`,
`"Laguerre" "spectral localization" "exponential"`, and `"Fourier Laplace"
"total variation" "approximation" filter`. No inspected result decides
the exact assay; unhelpful searches are not evidence of originality.

Local exact-term searches in drafts/literature and ATTEMPTS found the
older Runge/superoscillation, angular-propagation and signed-rectangle
assessments. Their relevant contracts were narrowly read and reused,
including [the angular assessment](2026-11-02-positive-mass-angular-propagation.md)
and [the signed-rectangle assessment](2026-10-30-signed-rectangle-absolute-cost-review.md).
Their finite-sum, Fourier-support, weight and operator qualifications remain.
They contain no approval of this changed assay. Review291's ready
Laguerre/inversion/parameter tools are reused without general reproof.

Read L997's exact hypotheses, short-interval identity, root bounds,
parameter-dependent inverses, complete-quartet regularity, endpoint-jump
proof and step294 audit; also the needed L994(6)–(7) and L995 hypotheses,
conclusions and imported-tool contracts. Stop293's audited fixed positive
bump cannot exclude signed n-dependent measures. Its endpoint-jump
noncancellation uses positivity of the fixed weight. Preserve that stop
without changing its quantifiers. Stops233/235/243/293/302/305/306/307/308
and unfinished inverse work are not reopened by generic approximation.
The direct Landau-selector import remains parked as recorded in step312.

The author-hosted super-resolution URL and Kent-hosted Nazarov URLs
failed, but arXiv and the original Russian journal PDF were accessible.
The latter's screenshot request redirected to metadata and did not expose
an image; no visual formula verification is claimed. Faber–Walsh v2's
opening was accessible but later requests timed out; theorem/proof evidence
here is explicitly the accessible v1. Search snippets and the expository
Marx summary are leads only, not theorem evidence. Earlier partially unread
superoscillation energy estimates remain unused. No essential source
blocker remains for a bounded attempt with the stated tools. Full matching
Mathlib coverage is unchecked and unknown. No cross-notebook input.

### Approved continuation and stopping test

Next is one proof_attempt/creative on the unchanged TARGET. First save
partial reasoning, then use the exact finite operator to seek a
norm-controlled construction or a dual/analytic obstruction covering
all admissible measures. Import the tools above rather than reprove them.
A polynomial or pure exponential model needs a proved realization and
error estimate for the original quartet before it can decide this assay.
Keep both Laguerre branches, all four quartet terms, both band endpoints,
the lower interval and the constant subtraction. Atomic measures are
allowed, but a construction confined to one subclass cannot prove
nonexistence for every finite complex Borel measure.

Continue only on simultaneous selected value one, one fixed positive
uniform suppression exponent and TV bounded by every positive exponential
allowance, as displayed above. Abandon this assay on a proved incompatible
normalization, unavoidable competing leakage, or positive exponential TV
cost for every putative sequence. Failure of a single design, unconstrained
polynomial approximation, finite ordinate fitting, an upper norm estimate
that misses the threshold, or a numerical preview is inconclusive. Record
such incomplete work without promoting it to an impossibility theorem.

This is literature EXPLORATION / NOVELTY_UNCHECKED, not a mathematical
advance or an informative negative theorem about the measures. No lemma,
mathematical script, new response identity, extremal constant or actual-Xi
bound was derived. A successful finite assay would justify examination of
actual spectral reconstruction; the main positivity gap and the independent
obligations listed above would still remain.
