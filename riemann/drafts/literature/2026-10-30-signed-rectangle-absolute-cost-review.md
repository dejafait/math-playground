# Signed rectangle detector: source comparison

TARGET: Review source coverage for signed band-limited rectangle detectors with K-weighted absolute real-axis cost O(log log T (log T)^(-c)) after removing full-strip nonnegativity.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Exact-class, complex-interpolation, signed-extremal and norm-equivalence searches completed; primary Kovrijkine v1 Theorem 1/proof, Brevig--Chirre--Ortega-Cerda--Seip v2 Theorem 3.6/proof, and ABR (1.1)/(1.2) read. Reused the existing same-kernel extremal and positive-strip assessments; bounded queries and distinctions below.
SOURCE_EVIDENCE: Kovrijkine, arXiv:math/0012186v1, Theorem 1, pp. 1--7; Brevig et al., arXiv:2210.13922v2, Theorem 3.6, pp. 12--13; Axler--Bourdon--Ramey, Harmonic Function Theory, second edition, author PDF 17 July 2020, (1.1)/(1.2), printed p. 4. Direct primary links and inspected cases below.
COMPARISON: Inspected results supply signed real-axis norm control, point-evaluation duality and a boundary identity, but no matching complex-rectangle constraint with absolute K-cost. Full-strip Harnack and the existing nonnegative real-axis extremal theorem do not settle the changed class. No novelty, feasibility or impossibility is established.
GAP: Combine rectangle positivity with quantitative control of every boundary term and the degenerating weight K; decide whether the resulting absolute-cost lower bound excludes every fixed C,c>0. This mathematical combination is not supplied by the inspected theorems and has not been attempted here.
REASON: Essential supporting sources are accessible and the quantitative difference is identified. Prepare one first-transverse-mode boundary test of this different positivity domain; its new ready assessment needs separate approval before mathematics. This literature-only step proves no detector bound.
SCOPE: Source comparison for exactly the family below. EXPLORE supports only the separately nominated bounded boundary test, not an existence theorem, a class obstruction or an arithmetic application.

## Exact proposed target

For real T tending to infinity put L=log T, delta=log L/L,
B=L/(4pi), a=delta L/pi, b=delta L/(4pi), and
K(x)=1-(sin(pi x)/(pi x))^2, with K(0)=0.
Ask whether there exist fixed R,C,c>0 and, for every sufficiently large
T, an even entire f_T real on R, represented by

    f_T(z)=integral_R phi_T(v) exp(2pi i v z) dv,
    phi_T in C_c^infinity(R), supp phi_T subset [-R,R],

such that

    Re f_T(x+iy)>=1       (|x|<=a, b<|y|<B),
    integral_R |f_T(x)| K(x) dx <= C log L L^(-c).

There is no sign requirement elsewhere, including on the real axis.
The absolute value in the cost is intentional: a small signed integral
obtained by unconstrained cancellation would not meet this target.
No derivative bound uniform in T is assumed. Existence and nonexistence
are both live possibilities; this nomination contains no derivation.

## Relevance and bounded continuation test

A feasible family could supply a signed test with controlled real-axis
cost. Controlling its negative values at actual complex zero coordinates,
uniform moving-test arithmetic errors, height/kernel transfers and all
initial Xi signs would remain independent gaps. No RH, simplicity,
spacing, external half-plane estimate or selected-amplitude moment is
assumed. L502 is a contrast, not a premise for this prospective problem;
L018 would supply coordinates only for a later arithmetic application.
Mathlib coverage of the changed class is unchecked.

The next source review should locate the strongest applicable primary
theorem and its essential proof cases, or document the precise missing
coverage. Continue toward one construction or necessary-bound test only
if an adequate assessment can be approved. A theorem excluding this
class should be imported and the class parked; persistent source blocking
requires another independent target. Do not repeat the positive-strip
construction or infer success of a signed arithmetic detector from
geometric feasibility alone.

## Completed bounded search: 2026-10-30

Queries included `entire functions exponential type positive real part
rectangle extremal L1 complex interpolation bandlimited`, `bandlimited
functions small L1 norm positive real part rectangle complex plane sign
uncertainty principle`, `"entire" "positive real part" "strip"
"exponential type"`, `"bandlimited" "complex" "L1" "extremal" point
evaluation`, `Kovrijkine Some results related Logvinenko Sereda theorem
2001 arxiv`, `Carneiro Chirre Ortega Cerda point evaluation Paley Wiener
Lp extremal complex`, `"bandlimited" "rectangle" "absolute"
"extremal"`, and `"weighted" "Paley-Wiener" "complex" "point
evaluation" L1`. Exact-term searches found no matching theorem; this
does not establish novelty. Discovery snippets were not theorem evidence.

The scoped local comparison used the prior positive-window assessment,
its Harnack test, L502's full statement/proof and the positive-strip stop
record. Their failure concerns full-strip positivity. No recorded signed
rectangle construction or obstruction was found in those specific files.
The shared overview's weighted Green covariance and amplitude routes
have different hypotheses; none is imported here.

## Primary results actually inspected

O. Kovrijkine, *Some results related to the Logvinenko--Sereda theorem*,
[arXiv:math/0012186v1](https://arxiv.org/pdf/math/0012186v1), 19 December
2000, pp. 1--7, Theorem 1: for 1<=p<=infinity, Fourier support in an
interval of length beta and a measurable E with |E intersect I|>=gamma alpha
for every interval I of length alpha,

    ||f||_{Lp(E)} >= (gamma/C)^(C(alpha beta+1)) ||f||_p.

Inspected finite-p normalization, Bernstein estimates, good/bad intervals,
analytic Lemma 1 (Blaschke removal, Harnack and Remez), its Lp corollary,
summation and the infinity endpoint. There is no sign assumption on f.
This is norm equivalence, not a positive lower normalization from a
complex rectangle. Applying it to the present K-cost still requires an
explicit thick set, Fourier convention and weight comparison. Those
specializations are future work, not established here. Constants are not
numerically imported.

O. F. Brevig, A. Chirre, J. Ortega-Cerda and K. Seip, *Point evaluation
in Paley--Wiener spaces*, [arXiv:2210.13922v2](https://arxiv.org/pdf/2210.13922v2),
1 November 2022, Theorem 3.6, printed pp. 12--13. For 1<=p<infinity,
the origin-normalized unweighted PW^p extremizer is characterized by
f(0)=integral f(x)Phi(x)dx for all f in PW^p, where
Phi=|phi|^(p-2)phi/||phi||_p^p. Read both proof directions, the real
variation and complex linearity, and the alternative Hahn--Banach/Riesz
argument, including its p=1 qualification. This supports a dual viewpoint;
it does not solve weighted absolute-cost minimization under continuum
complex inequalities. In particular, |f| on the real axis is not thereby
an admissible entire replacement for f. No extremizer, dual measure or
complex-point bound is imported into the detector problem.

S. Axler, P. Bourdon and W. Ramey, *Harmonic Function Theory*, second
edition, [author PDF dated 17 July 2020](https://axler.net/HFT.pdf#page=12),
printed p. 4, (1.1)/(1.2): for bounded smooth-boundary Omega and u,v C^2
near its closure, Green's identity equates integral (u Delta v-v Delta u)
to the outward-normal boundary integral u D_n v-v D_n u. Read its
divergence-theorem proof. It allows signed harmonic u. Rectangle corners
require direct iterated integration by parts or a justified smooth-domain
limit. It gives no sign or bound for the resulting boundary terms. The
previously inspected disk Harnack result may only be used inside a domain
where positivity is known; it cannot propagate through the gap to y=0.

The unchanged [same-kernel assessment](2026-10-30-positive-analytic-window-majorant-feasibility.md)
already inspected Carneiro--Chandee--Littmann--Milinovich v1 Corollary 14
and its proof, and Theorem 5's real majorization constraints. Those
nonnegative-real-axis hypotheses remain insufficient here. Reusing that
comparison avoids another extremal-theory audit.

## Unread leads and access qualification

Yuditskii's *On the L1 extremal problem for entire functions*, the
Gorbachev--Ivanov--Tikhonov eventually-constant-sign uncertainty paper,
general interpolation surveys, and the 2026 point-evaluation survey
surfaced as leads. No theorem from them is claimed inspected or imported.
Their surfaced formulations do not supply the exact rectangle constraint;
they are not essential dependencies of the nominated elementary boundary
test. Search failure is not evidence that stronger matching results do
not exist. Primary PDFs were accessible through the web tool. A shell
download failed at DNS resolution; no inaccessible source is being used
as a premise. No source certificate or mathematical script was generated.

## One proposed continuation; no mathematical result

The nominated mechanism is Green's identity projected against the first
positive transverse mode on [-a,a]. Keep the two horizontal faces and
both vertical faces. Combine signed Fourier norm control with positivity
only on the stated rectangle; do not insert positivity below b or outside
[-a,a]. Seek a nonvanishing lower bound for the absolute K-cost for each
fixed R, or isolate the precise uncontrolled boundary quantity and its
best justified scale. A lower bound merely of order L^(-A_R) does not
exclude the requested family for arbitrary c>0. Neither this projection,
its signs, weight conversion nor any lower bound has been derived here.

The new ready target is saved in
`drafts/literature/2026-10-30-signed-rectangle-transverse-boundary-test.md`
for separate approval next turn. It is a bounded potential mechanism,
not routine reproduction of Harnack and not an assertion of novelty.
There are no local lemma premises. L502 remains a contrast and L018
only a possible later coordinate interpretation. Full Mathlib coverage
of this signed weighted problem and its ingredients is unchecked.
No lemma, mathematical script, DAG edge or PROOF assembly changed.
