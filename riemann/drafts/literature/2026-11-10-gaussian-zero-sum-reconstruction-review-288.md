# Gaussian zero-height reconstruction: completed source comparison

TARGET: Test a Gaussian-height-regularized zero-sum reconstruction of L994's initial germs, with a compact-uniform regulator limit and all pole, archimedean and J_r-C_r terms retained.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step289 searched canonical logarithmic derivatives, Gaussian/Abel zero sums, Guinand-Weil test classes and Laguerre/Perron regulators; exact queries and duplicate/stop comparisons are below. No inspected theorem gives the full saved two-limit statement. This is no novelty claim.
SOURCE_EVIDENCE: Newly inspected Montgomery-Vaughan MNT I (2007), Lemma10.11/Theorems10.12-10.13/Corollary10.14, pp346-350, equations10.24-10.30; Theorems12.5/12.13 and Lemma12.14, pp400-401,410-416, including endpoint, bounded-variation and conditional gamma-integral proof cases; AppendixA TheoremsA.1-A.4, pp486-490. Read DLMF25.4.4/25.10(i); CCM1309.1526v1 Lemma5 explicitly assumes RH. Precise URLs and qualifications below.
COMPARISON: Canonical normalization, multiplicity accounting, symmetric explicit formulas and Stieltjes partial summation are known inputs to import. Their general proofs need no reproduction. The identified difference is uniformity for L994's coupled contours, infinite degree sum and literal exp(-epsilon*Im(omega)^2) weight, including conditional archimedean terms. A pointwise product formula or an RH-only ordinate formula does not establish that difference.
GAP: Prove or obstruct compact-uniform removal of the literal height regulator through the complete symmetric Perron limit on |z|<(1/4)exp(-2), retaining both shifts, canonical constants, real pole, gamma term and J_r-C_r. No such uniform bound or limit interchange is established in step289.
REASON: Essential source statements and convergence cases are now accessible and inspected; the remaining issue is a concrete mathematical uniformity test, not an unread essential source. Approve only a future specialization attempt after the supervisor's separate approval of this newly completed assessment. No new lemma, estimate or mathematical script was produced here.
LITERATURE_REASON: Review288 was REVIEW_REQUIRED for a new infinite zero-height regulator; finite-quartet reviews do not cover its canonical normalization or joint limits. This step fills that source gap once, without repeating the ready finite audit.
SCOPE: L994's rho=1/4, Re(s)=1, r=1,2, n>=2, both shifted branches and |z|<rho*exp(-2). Proposed zero weight exp(-epsilon*(Im(rho_zero))^2), epsilon>0, with every nontrivial zero counted with multiplicity and conjugation/functional-equation symmetries respected. Include critical-line pairs without treating a collapsed quartet as four distinct zeros. No RH, simplicity, rightmost zero, nonresonance or continuation beyond this disk is assumed.

## Completed comparison — step289, 10 November 2026

This is source coverage, not a proof of the reconstruction. Local inputs
were read before external comparison: L994's definitions, (3)-(7),
finite-height control and audit scope; L995's hypotheses, conclusions
and finite-input convergence proof; L018's completion normalization.
L985's finite K identity is used only transitively through L994.

### Canonical input to import

H. L. Montgomery and R. C. Vaughan, *Multiplicative Number Theory I:
Classical Theory*, Cambridge, 2007,
[section10.2, pp346-350](https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/14.0_pp_326_357_Analytic_properties_of_the_zeta_function_and_L-functions.pdf#page=21).
Lemma10.11 gives compact-uniform genus-one products under the entire
growth bound max_(|u|<=R)|f(u)|<=exp(R^theta) for all sufficiently
large R and some 1<theta<2, with the zero at0 separated. Theorem10.12
applies it to xi; Theorem10.13
gives N(T+1)-N(T)=O(log(T+2)), with the stated half-weight convention
at a height endpoint. Corollary10.14, (10.28)-(10.30), gives the
following identities away from their poles, and meromorphically:

    xi'(u)/xi(u)=B+sum_omega [1/(u-omega)+1/omega],
    zeta'(u)/zeta(u)=B+(log pi)/2-1/(u-1)
                     -(1/2)psi(u/2+1)
                     +sum_omega [1/(u-omega)+1/omega],
    B=-(Euler constant)/2-1+(log(4*pi))/2.

All nontrivial zeros occur with multiplicity. The proof's compact
product convergence and constant evaluation were inspected, including
the distinction between compensated sums and separately convergent
real-part sums. These are unconditional identities, not RH premises.

The normalization matches L018 and
[DLMF25.4.4](https://dlmf.nist.gov/25.4.E4), including xi(0)=1/2.
[DLMF25.10(i)](https://dlmf.nist.gov/25.10#i) supplies the open-strip
location and both symmetries. Use the negative of the displayed zeta
identity for L994's F. In particular the real-pole contribution has
positive residue, while a zero has negative multiplicity residue.
The psi(u/2+1) convention absorbs the rational 1/u term; do not add
that term a second time. This is notation/sign matching to a cited
identity, not a new partial-fraction proof.

The precise prospective regulated input is fixed for the next attempt:

    A(u)=-B-(log pi)/2+1/(u-1)+(1/2)psi(u/2+1),
    F_epsilon(u)=A(u)-sum_omega exp(-epsilon*Im(omega)^2)
                                      *[1/(u-omega)+1/omega].

This defines the proposed test, without asserting its joint-limit
properties. Keep B fixed, the full compensated bracket and the gamma
term. An undetermined additive constant or an epsilon-dependent
renormalization is outside this assessment. Apply the same F_epsilon
in both shifted occurrences. Full conjugate pairs and all distinct
functional-equation partners are counted once with their actual
multiplicities; a critical-line pair is not a quartet of distinct points.

### Available summation tools and their limits

Montgomery-Vaughan,
[section12.1-12.2, pp400-416](https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/16.0_pp_397_418_Explicit_formulae.pdf#page=4):
Theorem12.5 gives the midpoint psi explicit formula with symmetric
height cutoff, nearest-other-prime-power error and separate trivial
zero/pole terms. Its proof treats near endpoints and horizontal edges;
uniform convergence fails across prime-power jumps. Theorem12.13
requires a measurable test F and a fixed delta_0>0 with

    integral_R exp((1/2+delta_0)*2*pi*|x|)*|F(x)| dx < infinity,
    integral_R exp((1/2+delta_0)*2*pi*|x|)*|dF(x)| < infinity,
    F(x)=(F(x-)+F(x+))/2,
    F(x)+F(-x)=2*F(0)+O(|x|) near zero.

Its spectral test is Phi(s)=integral_R F(x)*exp(-(s-1/2)*2*pi*x)dx,
on -delta_0<Re(s)<1+delta_0. It sums Phi(omega) in symmetric height
order, not a function merely of the ordinates. The theorem permits
the primitive principal character of modulus1, giving the zeta case
(q=1, kappa=0, E_0=1). Its right side then retains Phi(0)+Phi(1),
the term [psi(1/4)-log(pi)]*F(0)/(2*pi), the prime-power sum
-(1/(2*pi))*sum_(n>=1) Lambda(n)/sqrt(n)
*[F(-log(n)/(2*pi))+F(log(n)/(2*pi))], and
integral_0^infinity exp(-pi*x)/(1-exp(-4*pi*x))
*[2*F(0)-F(x)-F(-x)]dx. This is a cited source statement; its F
is a test function, distinct from L994's negative zeta derivative.
Its proof uses bounded-variation Fourier inversion, retains pole and
gamma terms, and has constants depending on the test. Lemma12.14
handles the conditional gamma integral with fixed a,b>0 for L1,
bounded-variation J with J(x)=J(0)+O(|x|) near0; the zero and nonzero
J(0) cases were inspected.
Exercise12.1.9 is a Gaussian lead with a holomorphic rho-squared
weight and an additional contour; it is not an imported proved
height-regulator theorem.

Thus the source supports a possible fixed-degree endpoint/variation
method, but uniformity as degree, Perron height and regulator vary
must still be proved. Its test-dependent constants cannot be called
uniform constants for L994. The full logarithmic interval kernels,
after any change of variables and midpoint convention, must be checked
against those hypotheses; this turn performs no such specialization.

Montgomery-Vaughan,
[AppendixA, pp486-490](https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/20.1_pp_486_494_The_RiemannStieltjes_integral.pdf#page=3),
TheoremsA.1-A.4 and (A.4)-(A.7), give Stieltjes existence, integration
by parts and variation bounds. Read the finite-interval hypotheses,
endpoint conventions and proof of A.2. They permit partial summation
of a zero-height counting step function against a continuous Gaussian
at finite cutoff. They do not by themselves give a uniform infinite
cutoff or regulator limit. Import these named tools rather than
reprove them; any application must supply its own tail bounds.

E. Carneiro, V. Chandee and M. B. Milinovich,
[*Bounding S(t) and S1(t) on the Riemann hypothesis*, arXiv1309.1526v1,
6 September2013](https://arxiv.org/pdf/1309.1526v1), Lemma5, pp6-7,
assumes RH, analytic h on |Im s|<=1/2+epsilon, decay faster than
|s|^(-1), and real values on the real axis. Its h(gamma) formula
therefore cannot be imported here. In the unconditional Weil theorem
the spectral argument is the full complex zero. A holomorphic
Gaussian in (omega-1/2)/i must not silently replace the literal weight
exp(-epsilon*Im(omega)^2). No claim that the latter is impossible is
made; the source comparison only rules out that direct substitution.

### Exact bounded mathematical test, still unproved

Define I_(r,H)^epsilon by L994(4) with the proposed F_epsilon above,
and require, on every |z|<=R<R_0, existence and equality of

    lim_(epsilon down to0) lim_(H->infinity) I_(r,H)^epsilon(z)
      =lim_(H->infinity) lim_(epsilon down to0) I_(r,H)^epsilon(z)
      =G_r(z)-J_r(z)+C_r(z),  r=1,2.

Every indicated limit must be uniform on that compact disk. This is
the target contract, not an identity proved or assumed in this review.
A sufficient discriminating route would establish compact convergence
at fixed H and a Perron-tail modulus uniform for 0<epsilon<=epsilon_0;
otherwise a weaker, explicitly justified iterated-limit argument may
be tested. Do not infer a limit along arbitrary coupled paths without
proving it. When using the source's sharp zero cutoff T, distinguish T
from the integration height H and justify each order of limits.

The proposed attempt must start with finite degree, finite spectral
cutoff and finite H; retain all boundary terms through each passage.
Either provide a summable degree majorant uniform in the relevant
parameters and a finite-head limit, or identify the exact failure of
that method. L994's Perron bounds are for the original Dirichlet
series; they are not automatically bounds for F_epsilon. L995's
absolute height majorant depends on its finite input. Neither can be
summed over all zeros without a separate argument. The canonical
constants must remain explicit even if a later calculation shows
that this particular transform annihilates one of them. Retain J_r-C_r
unchanged rather than use smoothing to erase midpoint corrections.

Continue after the separate approval only for this initial-disk
uniformity problem, using the cited canonical identity and summation
tools. If the attempt yields only fixed-H convergence, record that
partial scope and the missing tail estimate. Park the tested mechanism
if its chosen majorant fails with no refined, independently testable
input; preserve the evidence instead of reopening direct actual-cluster
import. Reconstruction alone gives no continuation to z_*, noncancellation
there, signed output, L993 recovery or L984(H), and is no RH candidate.

### Search, duplicates, unread leads and classification

Queries actually issued included:

- `Riemann zeta logarithmic derivative Hadamard product sum zeros 1/(s-rho) 1/rho`
- `Guinand Weil explicit formula test function hypotheses Gaussian zeros`
- `site.personal.science.psu.edu/rcv4 Hadamard zeta zeros logarithmic derivative pdf`
- `Guinand Weil explicit formula holomorphic strip h decay 1 delta theorem Carneiro Chandee Milinovich pdf`
- `zeta Gaussian regularized sum zeros imaginary parts explicit formula heat kernel non Riemann hypothesis`
- `"zeta" "Gaussian" "Abel" "explicit formula" zeros`
- `"Laguerre" "Gaussian" "zeros" "Perron"`
- `"zeta" "e^{-epsilon" "zeros" logarithmic derivative`

The author-hosted MNT chapter PDFs were reached through its book index
after an optional publications-index URL failed. The PDF edition is
the 2007 book, with Cambridge online copyright2010 in the files.
Kowalski's 2021 notes were located but their theorem passages were not
read or relied on. Connes2402.13082 and Perisic's Zenodo Gaussian
staircase record22056422 are unread optional leads, not assessed
theorems or coverage for this target. No result is imported from
search snippets, community answers or computational pages. DLMF text
was read live on the checked date; a separate release number was not
verified. Full matching Mathlib coverage remains unchecked and unknown.

Scoped local exact-term searches in drafts/literature, ATTEMPTS and
foundations found only this nomination for the literal target; that
is not evidence of novelty. Reused review284/source-working285 and
read stops214/244/279/285 narrowly. Stop214 preserves residue-sign and
horizontal-comparison failures; stop279 preserves the unpaid signed
interval estimate; stop244 concerns centered arithmetic correlations;
stop285 leaves the actual complement unproved. This initial-disk
reconstruction neither contradicts nor resolves those stops. The
unfinished finite inverse work271 was inspected only for scope and
left unchanged; no certificate was rerun. No cross-notebook input.

Completed kind: LITERATURE; classification NOVELTY_UNCHECKED. The
useful outcome is newly checked known-source coverage and an explicit
remaining estimate, not a newly proved result or verified originality.
Future specialization is REPRODUCTION unless a separately reviewed
target changes that scope. The newly completed SPECIALIZE assessment
requires the supervisor's separate approval before research; no
mathematical invocation is made in step289.

## Original nomination context — step288, historical

The following nomination predates the completed source comparison
above. It established no identity, interchange, estimate or new lemma.
The completed step288 work was the L995 audit. Existing finite-target
assessments remain unchanged and reusable within their scopes.

The main gap is still L030-L032/C032a positivity and L966/L968 signed
forcing. The prospective intermediate output is an exact initial-germ
reconstruction with an independently justified regulator removal.
Its plausible downstream use is to distinguish a controllable
infinite spectral remainder from an assumed holomorphic complement.
Even success would not imply continuation to L995's singular point,
noncancellation there, actual signed estimates, L993 recovery or L984(H).

The source review must first retrieve the exact canonical
logarithmic-derivative or explicit-formula statement, including
summation order, additive normalization, real poles and gamma-factor
terms. L018 is the prospective local notation input; its relevant
statement must be read narrowly before use. Identify whether the
source supplies Gaussian regularization, an equivalent Abelian
limit, or a summability theorem with hypotheses actually met here.
Read those hypotheses and the essential convergence cases before
larger source extracts. An unregulated pointwise meromorphic identity
alone would not pay the joint integral limit.

The bounded test, after adequate prior approval, would ask whether
the epsilon-to-zero limit and symmetric H-to-infinity limit can be
matched locally uniformly in z on the stated initial disk, with
both contour branches and every nonzero-sum term retained. Accept
only a precise source specialization or a separately approved proof
of its missing estimate. If the source requires an unpaid uniform
bound, record that exact requirement and decide whether it yields
an independently testable estimate or parks this reconstruction.
Do not infer a natural boundary, cancellation, impossibility, or
actual complementary holomorphy from an inconclusive comparison.

Required local inputs are L994 and audited L995; L985's finite K
identity is transitive through L994. The exact completed-zeta identity
and regulated convergence are unresolved prospective inputs, not
established dependencies. Preserve stops214/244/279/284/285 and
unfinished inverse work271. No cross-notebook input is proposed.
The previous finite-response source comparisons, including
[DLMF1.10(viii)](https://dlmf.nist.gov/1.10#viii), give the analytic
obligation, not this reconstruction. Full matching Mathlib coverage
is unchecked and unknown. Next routing: literature_comparison,
standard/high, to compare the two-limit hypotheses before research.
