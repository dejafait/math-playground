# Scalar Volterra third-contact model: completed comparison892

TARGET: Assess coverage for a smooth positive scalar-Volterra model with H>0,H'<0 whose third signed derivative determinant crosses zero while the first two stay positive.
CHECKED: 2026-11-14
DECISION: EXPLORE
SEARCH_EVIDENCE: Step892 searched self-decomposable/log-concave densities, finite-order gamma PF and exact Wronskian terminology; checked the named local stops and recent gamma/geometric/third-Volterra nominations. Read primary statements and the relevant negative-power and smoothing proof cases below. No matching joint first-contact theorem was located; no novelty inference.
SOURCE_EVIDENCE: Khare author PDF, Theorems1.2/1.7/A and Corollary3.2, pp3-4/11-12; Kwasnicki arXiv:1710.11023v3 Section6.1 smoothing construction pp20 and Section6.2 pp21. Reused assessment883's Steutel--van Harn V.2.11/V.2.16 equation(2.23), and assessment888's derivative-combination comparison. Exact locators and scope below.
COMPARISON: Sources provide noninteger gamma finite-order distinctions, a smooth one-sided infinite-exponential mollifier and the scalar-law toolkit, but no simple first zero of the confluent D3 with lower signs throughout its prefix. Non-PF3 and excess derivative sign changes are insufficient. Actual low-order PF remains overlapped by Sra v3; C466c still supplies only a free jet.
GAP: For a fixed gamma-plus-geometric-exponential candidate, admissibility must be justified from the cited toolkit and strict D2, initial D3 positivity, exclusion of earlier contacts and D3'<0 remain unproved. This comparison constructs no witness and proves no obstruction to the whole model class.
REASON: Essential sources for one explicit family are now inspectable; nominate its bounded joint-contact diagnostic under EXPLORE, separately in assessment892. Do not continue generic browsing or infer the requested model from the source counterexamples.
SCOPE: Completed literature-only comparison for the saved target. One fixed generic m=3 candidate is nominated, with no order/parameter sweep, actual-density realization or retained-zero domination. Its new continuation assessment needs separate next-turn approval.
LITERATURE_REASON: First coverage of the joint law-level first-D3 geometry; prior finite-jet and bell-shape assessments explicitly excluded this target. The new gamma critical-exponent lead supplies a different model family.

## Exact proposed model

Require a probability density p in C^infinity(R), zero on
(-infinity,0], positive on (0,infinity), and H in C^1(0,infinity)
with H>0, H'<0 and integral_0^infinity H(t)dt<infinity, satisfying

    x p(x)=integral_0^x H(t)p(x-t)dt,       x>0.

Use D_j(p;x)=(-1)^(j(j-1)/2)det[p^(r+s)(x)]_(0<=r,s<j).
Seek x_*>0, eta>0 with D_1,D_2>0 on (0,x_*+eta),
D_3>0 on (0,x_*), D_3(x_*)=0 and D_3'(x_*)<0.
All endpoint regularity, integrals and signs would need proof.
These are proposed thresholds, not an example or existence claim.
An isolated negative sample or numerical plot is insufficient.

Essential local inputs are C466b's scalar-law/contact hypotheses,
C466a's boundary-role distinction and C466c's finite-jet obstruction.
L018/L024 identify the actual object only; they add no premise to
this generic model. C466c supplies no density, convolution kernel
or first-contact neighborhood. A model would obstruct universal
preservation from these scalar premises, not actual Xi's complete
kernel. A theorem excluding it could instead identify a preservation
input to compare with actual H. Neither outcome would settle arbitrary
orders, weighted forcing, simultaneous contacts, barriers, compact
propagation or L030-L032/C032a transfer.

## Bounded next review

Check exact/stronger results and PF-order counterexamples for positive
self-decomposable laws. Read primary hypotheses and the essential
model proof; failure of bell shape alone does not certify the required
first-D3 geometry. Reuse scalar-law coverage unless an essential
unread case or changed hypothesis warrants another source read.
Candidate families remain unread leads until inspected; none has
been calculated or asserted to be a witness this turn.

Approve at most one explicit model family with a discriminating
first-contact test, or import a theorem settling this class. If
coverage remains missing, retain REVIEW_REQUIRED or SOURCE_BLOCKED;
do not derive and approve a model in the same turn. If this merely
duplicates a sufficient recorded obstruction, record the overlap
and choose a materially different mechanism instead.

Preserve the
[automatic-preservation stop](../../ATTEMPTS/2026-11-14-volterra-automatic-pf-preservation-unpaid.md),
[bell-shape stop](../../ATTEMPTS/2026-11-14-contact-weight-bell-shape-source-stop-889.md)
and [finite-root stop](../../ATTEMPTS/2026-11-14-contact-kernel-real-root-inference-stop-891.md).
No historical stop is a global prohibition. No source-ready new
actual-H creative sign mechanism emerged from the finite diagnostic;
do not relabel elementary algebra or routine specialization creative.
Full matching Mathlib coverage of this model target is unchecked.

## Completed source comparison, step892

The original target and thresholds above are preserved. The main gap is
L030-L032/C032a's actual-Xi all-degree positivity. A generic law-level
countermodel would only identify limitations of scalar-law propagation;
an impossibility theorem would instead offer a preservation input to
compare with actual H. Neither would directly close the main gap.

### Primary statements and essential proof cases

Apoorva Khare, *Multiply positive functions, critical exponent phenomena,
and the Jain--Karlin--Schoenberg kernel*,
[author PDF](https://math.iisc.ac.in/~khare/papers/TN-crit.pdf),
retrieved 2026-11-14, 32 pages: for integer r>=2 and a>=0,
Theorem1.2 p3 states that Omega(x)^a,
Omega=x exp(-x)1_(x>0), is TN_r when
a is a nonnegative integer or a>=r-2. Theorem1.7 p4 gives failure
for noninteger 0<a<r-2. Read TheoremA's proof pp11-12 and
Corollary3.2: negative minors are obtained through positive diagonal
factors and a nonsingularity/homotopy argument. At a=1/2, the gamma
shape-3/2 density differs from Omega^(1/2) by a positive constant
and exp(-x/2); this changes each translation matrix by positive row
and column factors. Thus the cited finite-order comparison applies.
It does not concern a first confluent determinant crossing. The gamma
density itself also lacks the required smooth flat zero extension.
The separately opened arXiv:2008.05121v2 has 31 pages; the locators
just given refer to the inspected author PDF, not an asserted identical
pagination or full independent verification of its cited antecedents.

Mateusz Kwasnicki, *A new class of bell-shaped functions*,
[arXiv:1710.11023v3](https://arxiv.org/pdf/1710.11023v3),
Section6.1 p20 constructs g_m with transform
product_(n>=1)(1+s/(m 2^n))^(-1), as an infinite convolution of
positive exponential laws. The proof establishes smoothness using
arbitrarily long finite convolution heads, one-sided support, the
scaling g_m(x)=m g_1(mx), and its Levy density
sum_(n>=1) exp(-m 2^n x)/x. Read the complete smoothing paragraph
and Section6.2 p21's decreasing-kernel check for its original example.
That example certifies excess sign changes of f'', not this target's
D3. Its differentiated approximate-identity argument uses its own
C2 base density; it is not imported unchanged for a fractional gamma
base. The source supplies a smoothing component, not a theorem that
convolving any counterexample preserves a simple first contact.

Reuse, without a new book read, assessment883's precisely cited
Steutel--van Harn scalar-law coverage: a positive self-decomposable
law with left endpoint zero and canonical kernel k satisfies xp=k*p,
including the singular-kernel case. A new model must identify its own
k and verify the hypotheses. Assessment888's Nahmias--Proschan
Theorem2.2 has a global PF premise; it cannot supply first-contact
geometry from the desired lower determinants. No source theorem is
being reproved, and no new lemma or mathematical script was written.

### Search and comparison limits

Queries used: `self decomposable density log concave Polya frequency
finite order gamma convolution`; `"self-decomposable" "Wronskian"`;
`"gamma" "density" "total positivity" "non-integer"`;
`gamma density Polya frequency order alpha integer Karlin Schoenberg`;
`"gamma" "PF" "Simon" "total positivity"`;
`"self-decomposable" "log-concave" "gamma" density`.
Search snippets, secondary reviews and a generalised-Planck lead were
discovery material only. The 1961 Karlin--Proschan--Barlow paper's
opening/definitions were inspected, but no applicable joint-contact
theorem was extracted; it is not an input. No essential access blocker
remains for the bounded diagnostic; failure to find a match is not
evidence of originality or of nonexistence.

Narrow local checks covered C466a's hypotheses/conclusion, C466b's
scalar/contact hypotheses and audited obstruction, C466c's finite
counterexample, assessments883/888, and the named preservation and
bell-shape stops. A search of November14 literature/attempt notes for
the shape-3/2/geometric-smoothing proposal found no earlier matching
target. This is a scoped duplicate screen, not an exhaustive novelty
claim. L874/L611/U12 and the retained-zero stop are retained.

### Decision and continuation boundary

Nominate only the fixed candidate p=g_(3/2,1)*g_1, where the first
factor is the gamma density of shape3/2 and rate1 and g_1 is the
source's geometric-exponential smoothing density. The proposed kernel
to verify later is H(t)=(3/2)exp(-t)+sum_(n>=1)exp(-2^n t).
This is a proposed model specification, not a newly proved scalar
identity or contact example. All convergence, normalization,
endpoint, strict-sign and first-contact claims remain for research.
No parameter sweep or replacement family is approved in this review.

The discriminating test remains exactly the stated joint conditions:
D1,D2>0 through a simple first downward D3 zero, with D3 positive
on the whole preceding open interval. An isolated negative value,
failure of PF3 or a multiple zero is insufficient. A certified earlier
lower-sign failure or an obstruction to these conditions stops this
fixed candidate; an unresolved calculation stays unfinished and is
not reported as a model. The separate
[continuation assessment](2026-11-14-gamma-geometric-third-contact-test-892.md)
records this exact bounded target for later approval. Full matching
Mathlib coverage remains unchecked; no absence claim is made.
