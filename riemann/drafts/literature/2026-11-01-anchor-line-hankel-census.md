# Anchor-line census — completed bounded source comparison

TARGET: Assess whether C645g's exact Hankel symbol at delta=1/4 and eta=1/100 has a uniform lower bound ||H_q||>=c exp(-n/32) when M<=n/3 and every pole lies on Re(a)=-5/4, retaining distinct grid-avoiding poles, positive integer residues and the prescribed anchor.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed the bounded changed-support searches listed below and reused the scoped local duplicate/failure check; inspected primary discrete-transform and segment-measure statements and relevant proof cases. No inspected theorem decides the exact uniform bound; this is not an exhaustive absence or novelty claim.
SOURCE_EVIDENCE: Reuse the full-pole, one-sided and fixed-third assessments; newly compare Belov--Mengestie--Seip arXiv:0911.0318v2 Theorems 1--2 pp.2--5 and 0912.2899v1 Theorem 1.1 pp.2--3/Section 3.1 pp.15--18, BCQ 1501.01161v2 Section 5.4/(35), Proposition 2 and Theorem 6 pp.12--18, and Baratchart--Yattselev 0804.2206 retrieved text Section 2/Theorems 2.1,2.3 pp.4--7 and proof case (3.51)--(3.53) p.22; precise scope and version qualifications below.
COMPARISON: C645k/C645i's audited circles do not decide line support; C645g retains its small census coefficient. The inspected sources require special spectral weights, sparse geometry, infinite fixed measures or arclength densities, or provide multiplicity/approximation rather than the required full-norm size. No matching specialization is justified.
GAP: Prove or refute the uniform c exp(-n/32) bound for the exact finite line-supported inverse-grid-weighted family with M<=n/3; no spacing, phase or symmetry assumption is available. Actual-Xi layer isolation, other-pole control, realization and signs remain independent gaps.
REASON: The changed-support comparison is sufficient for one bounded phase-sensitive Hardy-functional or counterfamily attempt using the already covered operator/residue tools. No essential unread source is identified for that attempt; a citation alone does not evaluate the missing uniform exponent.
LITERATURE_REASON: The nomination changed planar support to a common real part, outside the ready prior assessments. This literature-only turn supplies that essential comparison and invokes no new mathematics.
SCOPE: Exactly the fixed-parameter synthetic family below, with arbitrary close distinct poles and positive integer original simple-pole residues; no actual-Xi realization or extra positivity is covered.
COVERED_TARGET: Test the anchor-line C645g bound ||H_q||>=c exp(-n/32) at delta=1/4, eta=1/100 and M<=n/3, using a phase-sensitive Hardy functional or an admissible line-supported asymptotic counterfamily.

The nomination below is preserved as historical context. Its statements
that coverage is missing or research is unauthorized describe nomination,
not this completed assessment. This newly ready scope requires the
supervisor's separate approval before a later mathematical invocation.

## Exact proposed target

Retain C645g's symbol, normalized H2 and strictly negative exterior
space, n>=5, delta=1/4, eta=1/100, R=11/8, x=-5/4 and
t_j=j/n for 0<=j<n. The product and symbol remain exactly

    B_n(z)=product_j R(z-i*t_j)/(R^2+i*t_j*z),
    q(zeta)=sum_a [r_a*B_n(x)/(R*B_n(a))]/(zeta-a/R),
    H_q f=P_-(q*f).

Require every pole to have the form a=x+i*y_a with y_a real,
|a|<=R-eta, and require x to be present. Points remain distinct,
with no positive separation imposed. Each original simple-pole
residue r_a is a positive integer and M=sum r_a<=n/3. Do not
impose symmetry, a sign on y_a, or positivity of the complex
inverse-grid amplitudes. The constant c>0 and onset must be uniform
over the entire family at these fixed parameters. No mathematical
calculation or new lemma for this target was made during nomination.

## Relevance and discriminating test

The audited planar circle mechanism stops the proposed count-only
bridge. This target instead asks whether a common-real-part zero
layer can retain a useful detector despite many distinct ordinates.
A positive result could supply one ingredient for such a layer,
conditional on separately isolating it and controlling the contribution
of poles at other real parts. Neither the existence of a suitable
selected layer nor such control is assumed or proved. In particular
no full Xi disk census is asserted to be collinear, and line support
is not offered as an unconditional shortcut to RH. Census/clearance,
realization, a useful independent boundary upper bound and signs
remain open.

First check primary theorems and relevant proof cases for weighted
discrete Cauchy transforms supported on a line, rational Hankel
operators and simple partial fractions. Reuse the existing operator
normalization and residue coverage. BCQ's already inspected segment
hypotheses require an arclength density on a hyperbolic geodesic;
they cannot be silently substituted for arbitrary discrete atoms on
this Euclidean vertical segment. Likewise, original positive residues
do not make the exact grid-weighted residues positive. These are
source-scope cautions, not proofs that a useful specialization fails.

Approve a later bounded mathematical test only after finding a valid
import/specialization or documenting the remaining quantitative gap
with no essential unread input. A later decisive positive result is
the stated uniform lower bound; a decisive negative is an admissible
line-supported sequence with exp(n/32)*||H_q|| tending to zero.
Scalar cancellation, least singular values or a finite numerical
screen do not settle it. No such test is authorized by this nomination.
If the reviewed source already covers the target or a matching stop,
import that result rather than reproving it. Otherwise keep missing
coverage visible; this assessment is not ready yet.

Full matching Mathlib coverage is not checked. No new source passage,
novelty conclusion, actual-Xi assertion or RH candidate is claimed.

## Completed source comparison — 1 November 2026

### Search scope, duplicates and preserved stops

Queries actually issued in this review:

- `Hankel operator Cauchy transform discrete measure segment complex weight lower bound norm`
- `rational function poles on line positive residues weighted Blaschke norm lower bound`
- `Cauchy transforms discrete measures real line rational approximation bounded variation argument Hankel lower bound`
- `"discrete Cauchy" "Hankel" norm`
- `"Hankel" "Cauchy transform" "finite" "positive measure" norm`
- `"multipoint Padé" "complex Cauchy transforms" theorem measure bounded variation`
- `discrete Hilbert transforms sparse sequences Belov Mengestie Seip boundedness theorem`
- `"Cauchy" "discrete" "line" "Hankel operators" weights norm lower`

Read C645g's exact hypotheses, spaces, scaling and (3)--(6), and its
denominator-cost mechanism through (14). Reused the
[full-pole comparison](2026-11-01-full-pole-hankel-boundary-mechanism.md),
[one-sided comparison](2026-11-01-one-sided-pole-hankel-census.md) and
[fixed-third comparison](2026-11-01-fixed-third-census-hankel.md).
Read the specific C645i/C645k stop records and C645k audit history;
searched only the associated Hankel assessments/histories for line
support, collinearity and common real part. No exact duplicate was
identified in that scope. Their circle counterfamilies remain stops
for their own hypotheses, without settling this stricter family.
C645g's established small-census result is not a bound at M<=n/3.
No unchanged certificate or lemma audit was repeated.

### Primary theorem comparisons

Y. Belov, T. Y. Mengestie and K. Seip, *Unitary discrete Hilbert
transforms*, inspected [arXiv:0911.0318v2](https://arxiv.org/pdf/0911.0318v2),
13 January 2010, Theorems 1--2, pp.2--5, definitions (1)--(5).
Finite or infinite disjoint point sequences and positive sequence
weights are allowed. Theorem 1 makes circle/line support necessary
for unitarity; its proof uses orthonormality and real cross-ratios.
Theorem 2 requires an admissible real sequence with
sum v_j/(1+|gamma_j|^2)<infinity. The target sequence is a level set
phi(lambda)=alpha of its Herglotz function; target weights are inverse
sums of v_j/(lambda-gamma_j)^2. Unitarity holds exactly when
(alpha-phi)^(-1) is purely atomic Herglotz. Read the relevant proof
cases using both isometries and the atomic representation. Collinear
poles alone do not supply these weights or level sets. This is a
sequence-to-sequence transform, not our prescribed circle Hankel
operator. No unitary realization or norm identity for q is imported.

The same authors, *Discrete Hilbert transforms on sparse sequences*,
Proc. London Math. Soc. **103** (2011), 73--105,
[DOI](https://doi.org/10.1112/plms/pdq053); inspected
[arXiv:0912.2899v1](https://arxiv.org/pdf/0912.2899v1), 15 December 2009,
Theorem 1.1/(1.2)--(1.5), pp.2--3, and selected necessity/sufficiency
cases in Section 3.1, pp.15--18. The theorem characterizes boundedness
from l2_v to L2(mu) for positive admissible weights, a nonnegative
measure with mu(Gamma)=0, and inf |gamma_(j+1)|/|gamma_j|>1, through
the stated local and two tail tests. Basis-vector testing and the
three-part sum estimate are the relevant proof cases. Our family
has no such sparsity hypothesis. Boundedness of this different map
also does not evaluate a lower bound for our prescribed weighted
symbol. No transformation making the hypotheses applicable is claimed.

L. Baratchart, S. Chevillard and T. Qian, *Minimax principle and lower
bounds in H2-rational approximation*, J. Approx. Theory **206** (2016),
17--47, [DOI](https://doi.org/10.1016/j.jat.2015.03.004).
Inspected [1501.01161v2](https://arxiv.org/pdf/1501.01161v2), 24 March
2015, Section 5.4/(35), H1--H2, Proposition 2 and Theorem 6/(51),
pp.12--18. Theorem 6 compares uniform rational, uniform meromorphic
and L2 rational approximation errors, with positive constants depending
on a fixed f. Its Cauchy integral requires a hyperbolic geodesic and
an arclength-integrable density with continuous argument except finitely
many pi jumps. The inspected proof mechanism uses phase correction
(44), geodesic conjugation from Lemma 2 and normality of outer factors;
the two inequalities retain approximation distances. Our finite atoms
do not meet the density hypothesis, and no uniform constants for the
varying q_n or evaluated exp(-n/32) bound follow by citation. Existing
rational-symbol/AAK coverage is reused without reproof.

L. Baratchart and M. Yattselev, *Multipoint Padé approximants to complex
Cauchy transforms with polar singularities*, J. Approx. Theory **156**
(2009), 187--211, [DOI](https://doi.org/10.1016/j.jat.2008.04.013).
Inspected [0804.2206](https://arxiv.org/pdf/0804.2206), Section 2,
pp.4--7, Theorems 2.1/2.3, and proof case (3.51)--(3.53), p.22.
The retrieved 30-page PDF prints 11 November 2021; the explicit v1
endpoint returned the same dated text, so no historical-version identity
is inferred. Theorems concern a fixed complex measure with infinite
compact real support, bounded-variation argument, regular support and
|lambda|([u-h,u+h])>=c h^L. Interpolation must stay away from the
support's convex hull and rational poles, have a finite-energy limiting
counting distribution and uniformly bounded phase derivatives. They
give pole-distribution and approximation-error convergence in capacity.
The inspected lower-estimate case uses a positive-capacity subset and
local mass. These are not estimates uniform over our varying finite
atomic family or for its circle operator norm. No limiting-measure
argument supplying the missing hypotheses is assumed.

Reuse Yattselev's 2009 Theorem 2.1 from the one-sided assessment;
the primary journal statement was checked again only for the changed
support comparison. It bounds singular-value multiplicities for an
infinite-support measure, rather than singular-value sizes. The prior
SPF/Gorin and Komarov comparisons remain adequate: the unweighted
positive-residue setting is different from the exact inverse-grid
amplitudes. No repeated general survey is needed. Search hits on
general SVD algorithms, prescribed-pole derivative inequalities,
analytic-arc interpolation and Cauchy-transform books were discovery
leads only; no theorem from them is imported or identified as an
essential dependency of the bounded test.

### Decision and one bounded continuation

DECISION is EXPLORE. This records adequate bounded comparison for an
attempt, not a new bound, novelty certification, or proof that no
matching theorem exists. No essential source is currently blocked.
The joint requirements still missing from an evaluated theorem are:
the exact complex B_n weights; all large n; all distinct line-supported
pole sets without separation; positive integer original residues of
total at most n/3; and a constant/onset uniform over all those choices.
Neither an affine line parametrization nor an unspecified disk map
is asserted to preserve the prescribed norm and weights.

For a later separately approved invocation, the COVERED_TARGET permits
one phase-sensitive Hardy-functional or line-supported counterfamily
attempt at exactly these parameters. This tests the extra common-real-part
geometry rather than repeating C645g's absolute denominator cost or the
stopped planar circle construction. It does not assume a positive
complex measure, ordinate symmetry, a spacing bound or a favorable
least singular value. This is a proposed mechanism, not a dual formula
or estimate established during review. General Hardy/residue inputs
are ready in the reused assessments; no reproof of their general
theorems is called for.

Continue on a proof of the uniform c>0/onset at exp(-n/32), or stop
the asserted bound on an admissible sequence with
exp(n/32)||H_q|| tending to zero, controlling the largest operator
norm. A failed functional, scalar cancellation, finite screen or small
singular value alone is inconclusive; preserve partial reasoning and
require a refined mechanism before repeating an unsuccessful attempt.
Essential mathematical input is C645g's exact symbol and spaces;
C645k's audited stop must be respected. C645h/C645j supply relevance
context, not extra hypotheses. Actual-Xi common-real-part layer
isolation, contributions from other poles, census/clearance,
realization, an independent useful upper bound and signs stay open.
No cross-notebook input, new lemma, mathematical script, full matching
Mathlib coverage or RH candidate was produced. This newly ready
assessment receives separate supervisor approval before research.
