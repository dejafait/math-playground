# Full-kernel Stein monotonicity: completed source comparison

TARGET: Review whether a nonincreasing Stein kernel for a positive even rapidly decaying density implies F'^2-FF''>=0, and whether the criterion is applicable to the full theta kernel.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed exact/stronger searches for decreasing/nonincreasing Stein kernels, characteristic functions, Fourier signs, real zeros and Laguerre inequalities; primary passages and queries are recorded below. Read L019/L233/L049/L055 and C055a's statement narrowly; reused the complete-first-sign discovery and the two named route stops. No matching implication or counterexample with verified Stein monotonicity was found; this is not an absence or novelty theorem.
SOURCE_EVIDENCE: Saumard arXiv:1804.03926v3 Section 2 (5)-(6), printed pp. 3-4, and Theorem 6/full proof, pp. 9-10; Bobkov--Duggal author PDF Section 16 (16.4)-(16.8), pp. 34-35; Csordas arXiv:1309.0055v2 Theorems 4.1/4.2/4.5/4.6 and Open Problem 4.7, pp. 10-12; Bagnoli--Bergstrom 4 March 2004 manuscript Theorem 3/Corollary 2 and Appendix 8.2 Lemma 4, pp. 4,25. URLs and qualifications below.
COMPARISON: The inspected Stein results provide identities and variance bounds, and the shape results provide spatial concavity or hazard monotonicity; none states the requested Fourier Laguerre implication. L055's nonreal zeros alone do not refute a first-sign criterion. L233 already supplies a fixed negative-first-sign model satisfying positivity/evenness/smooth rapid decay; only its Stein monotonicity remains to test.
GAP: Neither generic sign transfer nor the full theta Stein hypothesis has been established here. The fixed L233 model permits a bounded diagnostic of the former without assuming the latter; all higher Xi signs remain independent.
REASON: The required source comparison is complete with an actionable fixed-model test, not a new sign theorem. Park citation-only theta application; nominate the separate diagnostic assessment for next-turn approval before mathematics.
SCOPE: Completed literature-only review of the exact criterion below. No new identity, derivative evaluation, theorem specialization, counterexample construction, lemma or mathematical script was performed.
LITERATURE_REASON: The startup assessment was REVIEW_REQUIRED for an uninspected sign-transfer criterion; probability variance and spatial shape results could not be substituted for essential Fourier-sign coverage.

## Exact proposed criterion and usefulness

Let k be strictly positive, even and smooth on R, with every derivative
decaying faster than every exponential. Define

\[
 F(x)=\int_{\mathbb R} k(u)e^{ixu}\,du,\qquad
 \tau(u)=\frac{\int_u^\infty v k(v)\,dv}{k(u)}.
\]

The candidate sufficient hypothesis is that tau is nonincreasing on
the positive half-line. The question to assess is whether that
hypothesis implies F'(x)^2-F(x)F''(x)>=0 for every real x. No such
implication, monotonicity of the actual-theta tau, or new differential
identity is claimed here. Normalizing k to a density does not change
the proposed ratio's definition; the source must state its own
integrability and boundary assumptions precisely.

For the full L019 theta kernel, L233 identifies this expression as
four times the first Xi sign. An independent sufficient theorem plus
an independently established theta hypothesis would address that
first-sign gap. Higher-degree signs would still be unresolved. Merely
renaming the spectral inequality as a Stein condition is not useful.

Essential local inputs for a later application are L019 and L233;
L356 and L603 are comparisons that explain why the full kernel and
all cross terms must be retained. There is no cross-notebook input.

## Bounded comparison and continuation test

Three possible continuations were compared at nomination, without
performing mathematics beyond the approved L603 audit:

1. Separate primitive-family positivity is stopped by audited L603.
   Its exact regrouping remains valid. No repeat test is proposed.
2. Boundary matching between reflected blocks is not a new sign
   mechanism by itself: L356 already has cancellation and no total
   sign. No independently specified remainder threshold is available
   here, so another tail-cancellation calculation is not selected.
3. A monotone-Stein criterion uses the complete smooth density and
   a weighted integration-by-parts structure. Its fixed sufficient
   hypothesis can be checked against theorem statements or a model,
   independently of RH. Select its source comparison, with no claim
   that the criterion is true or holds for theta.

Retrieve primary Stein-kernel Fourier identities and any associated
Laguerre/real-zero theorem, first their hypotheses and relevant proof
cases. Check exact statements and stronger conditions; distinguish
log-concavity of a density, Poincare inequalities, positivity of its
characteristic function and the requested Laguerre inequality. The
earlier complete-first-sign assessment notes direct-kernel comparison
models in L049/L055; read their exact hypotheses narrowly if they
provide a counterexample lead, without assuming they satisfy the
new tau condition. No ready prior assessment covers this comparison.

Continue toward mathematics only if the review supplies a precise
applicable theorem and an independently testable theta hypothesis,
or a fixed covered model that can discriminate the proposed generic
criterion. Import a known counterexample if it matches. Abandon this
criterion if a known counterexample satisfies all its hypotheses;
if no theorem or fixed diagnostic can be specified, record the
inconclusive search and park it rather than repeating retrieval or
silently adding hypotheses. A counterexample to this sufficient
criterion would say nothing about the actual theta sign.

At nomination, the missing sign-transfer theorem was the blocker to a justified
creative proof attempt. This nomination prepares source coverage;
it does not label routine identities or model specializations as
creative. Any future creative attempt needs its own exact obstruction,
bounded test and approval. Full-result Mathlib coverage is not checked.

## Completed review: 31 October 2026

**Stein inputs.** Adrien Saumard, *Weighted Poincare inequalities,
concentration inequalities and tail bounds related to Stein kernels in
dimension one*, [arXiv:1804.03926v3, 23 November 2018](https://arxiv.org/pdf/1804.03926v3),
Section 2 (5)-(6), printed pp. 3-4, states the identity for a density
with connected support and finite absolute first moment. Test functions
must make both sides integrable and satisfy the endpoint condition
`[tau p phi]_a^b=0`. Theorem 6 and its complete Cauchy--Schwarz/Jensen
proof, pp. 9-10, give `Var(f)<=E[tau f'^2]` for absolutely continuous
`f` in L2. Neither statement asserts the proposed Fourier sign.

Sergey G. Bobkov and Devraj Duggal, *Spherical covariance representations*,
[author-hosted PDF](https://www-users.cse.umn.edu/~bobko001/preprints/BD_Spherical.covariance.identities.pdf),
Section 16, printed pp. 34-35, (16.4)-(16.8), gives the Hoeffding-marginal
Fourier identity `hat h(t)=-f'(t)/t` for centered laws, `t!=0`, and the
Stein ratio `h/p`. Read those passages, including Proposition 16.4's
Gaussian characterization. No version/date was displayed in the inspected
passages; this identifies the retrieved author copy, not a verified edition.
For later use require finite second moment, which all candidate densities
here have. Do not use Proposition 16.3's first-moment wording as a warrant
for finiteness of the entire marginal measure. No Fourier Laguerre sign
transfer appears in the inspected passage. Positive definiteness of a
Fourier transform and pointwise nonnegativity of its values are distinct.

**Theta and shape comparison.** George Csordas, *Fourier transforms of
positive definite kernels and the Riemann xi-function*,
[arXiv:1309.0055v2, 21 February 2014](https://arxiv.org/pdf/1309.0055v2),
Theorems 4.1-4.2, pp. 10-11, supplies theta decay/evenness and strict
log-concavity of both `Phi(sqrt(t))` and its integrated tail. Read the
displayed normalization (4.2), the statements, and Theorem 4.5's short
proof, followed by Theorem 4.6/Open Problem 4.7, pp. 11-12. These give
spatial properties and the associated-kernel criterion, not a Stein
transfer. They identify a possible source for checking theta's proposed
hypothesis later; no coordinate specialization is performed here.
The source's Example 3.12, pp. 8-9, explicitly separates first-sign
positivity from all-real Fourier zeros. Thus L055's nonreal zeros alone
are insufficient negative evidence for this exact target.

Mark Bagnoli and Theodore C. Bergstrom, *Log-Concave Probability and Its
Applications*, [4 March 2004 author manuscript](https://escholarship.org/content/qt0xt8k6sd/qt0xt8k6sd_noSplash_d3b995fc634e40551bbd3dc90a1b0e43.pdf),
Theorem 3/Corollary 2, p. 4, concerns a continuously differentiable
log-concave probability density on an interval: its survival function is
log-concave and its hazard is nondecreasing. Appendix 8.2 Lemma 4's
right-integral argument, p. 25, was read. This is a shape comparison lead,
not the requested Fourier theorem or a completed Stein specialization.
No claim depends on the manuscript's apparent intermediate sign typo.

**Local overlap.** L049's Gaussian mixture proves a different cumulant
failure. L055 and C055a concern square-root-coordinate shape and nonreal
zeros; none of those read statements certifies a negative first Fourier
sign under the new hypothesis. L233, read in full, already certifies
the exact negative sign and every non-Stein hypothesis for its fixed
three-Gaussian mixture. Testing that existing object does not repeat
L603's stopped primitive decomposition or the citation-only determinant
transfer stopped in
`ATTEMPTS/2026-10-31-actual-theta-fourier-determinant-transfer-stop.md`.
The primitive-family stop and its audit history were also read narrowly.
No other notebook or uninspected theorem is a mathematical input.

Representative queries actually used:

- `"Stein kernel" "decreasing" characteristic function zeros`
- `"Stein kernel" "nonincreasing"`
- `"Stein kernel" "monotone" Fourier`
- `"Stein kernel" "Laguerre inequality"`
- `"Stein kernel" "real zeros"`
- `Stein kernel symmetric density decreasing x density sqrt log concave hazard rate`
- `Bagnoli Bergstrom log concave probability applications Theorem 3 reliability function pdf`
- `"decreasing Stein kernel" characteristic function`

Search results about kernel Stein discrepancy, gamma/Laguerre generators
and decreasing discrepancy along a central limit theorem concern other
objects. Their snippets are not sign-transfer theorems. The Courtade--Fathi--
Pananjady spectral-gap and Ledoux--Nourdin--Peccati papers are unread leads
beyond the cited secondary descriptions, not imported results. Failed
searches do not establish novelty or falsity of the candidate criterion.

**Decision and bounded continuation.** No matching affirmative theorem
or already-verified counterexample was located. Choose the existing
L233 mixture as the fixed diagnostic, covered separately in
[the model assessment](2026-10-31-l233-stein-monotonicity-diagnostic.md).
Only a proof of global nonincrease would combine with its existing
negative sign to reject the generic criterion. A single rigorously
positive Stein derivative would instead reject this model as a
counterexample; it would leave the criterion undecided. Park that model
after such a failure, rather than varying parameters without review.
No actual-theta derivative or new Fourier bound was calculated.

Outcome EXPLORATION, completed literature comparison with an actionable
diagnostic. No progress beyond the checked sources is claimed. Full-result
Mathlib coverage remains not checked. The new continuation receives a
separate approval next turn; it is not invoked here. No justified creative
actual-Xi proof mechanism is ready: its missing sign-transfer theorem is
still the precise blocker. The diagnostic is an ordinary calculation.
