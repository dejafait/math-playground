# Fixed prescribed-Stein model: completed source comparison

TARGET: Test the monotone-Stein first-Laguerre implication using the fixed prescription tau(u)=1/(1+u^2), reconstructing its centered density and seeking a rigorous negative Fourier Laguerre value.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the generic criterion review; searched the exact reciprocal-quadratic ratio, prescribed-kernel reconstruction, quartic Fourier real-zero classes and stronger Pólya/Newman results. Inspected primary statements and relevant sufficiency proofs below; no exact fixed-model answer was located. Failed searches establish no novelty.
SOURCE_EVIDENCE: Saumard arXiv:1804.03926v3 Section 2 (5)-(6), pp. 3-4, Proposition 5 (18)-(19) and its proof, pp. 7-8; Newman, Proc. AMS 61 (1976), 245-251, (1.5), Theorem 2 and its sufficiency proof, pp. 246-248; Csordas arXiv:1309.0055v2 Definition 1.1 and (2.1), pp. 2-3. Direct URLs and restricted source scope below.
COMPARISON: Reconstruction and a stronger real-zero class now have usable primary coverage. Compare the fixed reconstructed density with Newman's finite-product class before searching for a negative sign. C233b's mixture failure and L604's unsigned integrated remainder persist; no model application or new sign has been proved in this source turn.
GAP: The remaining work is the elementary fixed-density reconstruction, realization/decay checks, exact class matching, damping/Fourier coordinate checks and Laguerre applicability. If matching succeeds, import the global nonnegative sign and stop the negative-witness search; this does not decide the generic implication or any Xi sign.
REASON: Essential source coverage for the saved target is complete. The literature supplies a bounded theorem-specialization test with a possible decisive stop, replacing an unguided numerical witness search; it does not yet supply a verified local specialization.
SCOPE: Only tau(u)=1/(1+u^2), with the original positivity, evenness, smoothness, centering, all-derivative rapid decay and exact-ratio requirements. Permit either a rigorous negative first sign or a cited global nonnegative-sign obstruction after checking applicability. No parameter sweep, generic transfer proof or actual-Xi sign calculation is covered.
LITERATURE_REASON: Startup coverage was REVIEW_REQUIRED: the prescribed-ratio inverse problem and essential stronger Fourier-class sources were unread. This turn supplies those passages without deriving the model.

## Original nomination and retained scope

The L605 audit nominated this target without approving its mathematics.
The generic criterion's previous search did not establish absence,
novelty, or coverage of this different model. The separate source turn
recorded below now completes its coverage; no reconstruction or Fourier
calculation was performed during either the nomination or this review.

Compare the exact reconstruction with standard Stein-kernel examples
and known real-zero/Fourier results before selecting a mathematical
test. Import a matching result by precise citation. A ready later
attempt must verify every density/decay/centering hypothesis rather
than treating the prescribed ratio as an established realization.
If no applicable source or bounded certified sign test emerges, park
this fixed model; do not vary parameters or repeat the L604 pointwise
argument under a new name. A proof of global nonnegative first sign
would reject this model as a counterexample, not prove the generic
criterion. A numerical preview alone would decide neither outcome.

Essential continuation context: L605 (audited actual-theta premise),
C233b (fixed-mixture failure), L604 (uncontrolled integrated remainder),
and Saumard (5)-(6). These are context and prospective applicability
inputs, not a second dependency graph. No cross-notebook input.
Full-result Mathlib coverage remains not checked.

## Primary inputs actually inspected

Adrien Saumard, *Weighted Poincare inequalities, concentration inequalities
and tail bounds related to Stein kernels in dimension one*,
[arXiv:1804.03926v3, 23 November 2018](https://arxiv.org/pdf/1804.03926v3),
Section 2, Proposition 5 (19), printed p. 7, gives

\[
 p(x)=\frac{E|X-\mu|}{2\tau(x)}
 \exp\left(-\int_\mu^x\frac{y-\mu}{\tau(y)}\,dy\right).
\]

Its hypotheses are an existing density with connected support and finite
first moment; the general version (18) assumes an integrable centered h
and a positive inverse Stein image. Read (5)-(6), the full Proposition 5
statement and its proof on pp. 7-8. Formula (19) is a representation,
not an existence theorem for arbitrary prescriptions. A later application
must normalize and verify the tail-ratio identity independently. The Stein
identity (5) requires integrable terms and a vanishing endpoint expression.

Charles M. Newman, *Fourier Transforms with Only Real Zeros*,
Proc. Amer. Math. Soc. **61** (1976), 245-251,
[primary article scan](https://sites.math.northwestern.edu/~auffing/papers/Newman.pdf),
(1.5) and Theorem 2, pp. 246-247, with the complete sufficiency argument,
pp. 247-248. The finite-product subclass needed for comparison is

\[
 d\rho(t)=K t^{2m}e^{-a t^4-\beta t^2}
 \prod_{j=1}^{N}(1+t^2/a_j^2)\,dt,
 \quad K>0,\ m\in\mathbb N_0,\ a>0,\ \beta\in\mathbb R,\ a_j>0.
\]

These even finite nonnegative measures have real-zero Fourier transforms
after multiplication by exp(-b t^2), for every b>0; Theorem 2 uses the
equivalent imaginary-zero Laplace convention. Its proof treats polynomial
times Gaussian measures and quartic approximation. Use this subclass only;
the general infinite compensated product is unnecessary. The target's
undamped transform must be identified as a damped member or treated by a
justified limit. Neither matching nor removal of damping is performed here.

George Csordas, *Fourier transforms of positive definite kernels and the
Riemann xi-function*,
[arXiv:1309.0055v2, 21 February 2014](https://arxiv.org/pdf/1309.0055v2),
Definition 1.1 and (2.1), printed pp. 2-3, give the Laguerre--Pólya product
class and its first-sign inequality. Read the intervening logarithmic
derivative justification and polynomial-limit characterization. Real zeros
alone do not license this step: verify order strictly below two and apply
the standard named Hadamard factorization theorem to obtain membership,
or justify the relevant real-rooted polynomial limit. Do not use Definition
1.2's admissible-kernel assertion without its additional decreasing-kernel
hypothesis. The inequality holds also at real zeros by continuity. No
theta-shape theorem is being substituted for Fourier positivity.

David A. Cardon, *Fourier transforms having only real zeros*, Proc. AMS
**133** (2005), 1349-1356,
[author PDF](https://mathdept.byu.edu/cardon/papers/FourierRealZeros_Proc_AMS.pdf),
Proposition 1, pp. 1349-1350, was inspected as a comparison. It requires
an even integrable superquadratically decaying base whose transform already
has only real zeros, and a Laguerre--Pólya universal factor. It supplies no
Stein-to-sign theorem and is unnecessary if Newman's direct class matches.
The original Pólya 1927 PDF link redirected to a discontinued archive;
that original is not claimed read or essential to the selected primary
Newman proof. A shell download failed DNS; web article text remained
accessible. Screenshot calls supplied no inspectable page images, so no
visual verification is claimed. The finite subclass and sufficiency case
above were readable in the primary text; no ambiguous infinite-product
formula is imported.

## Search, duplication and bounded mathematical continuation

Queries actually used include:

- `Stein kernel prescribed density reconstruction tau density exp integral Saumard 1804.03926`
- `"Stein kernel" "1/(1+x^2)"`
- `"Stein" "(1+x^2)" "x^4" density`
- `"decreasing Stein kernel" Fourier Laguerre`
- `Polya Fourier exp quartic quadratic all real zeros exp -at4 -bt2 theorem`
- `"exp" "quartic" "Lee-Yang" "zeros" theorem Newman`
- `"Fourier" "at4" "bt2" zeros`
- `"Über trigonometrische Integrale mit nur reellen Nullstellen" pdf`

The Dimitrov--Rusev 2011 survey's quartic/universal-factor discussion was
used only to locate primary sources. Its initial PDF fetch timed out but
later text access worked. Its statements and other search snippets are
not mathematical inputs. No exact model theorem was found; this does not
establish originality. Narrow local searches of the Stein assessments,
working notes and stop records found no prior application of this Newman
class to the saved prescription. C233b and the generic transfer review
were read; L604/L605 were searched only for their relevant scope. No
sibling notebook was read. No prior proof is displaced.

The saved TARGET is unchanged. Next mathematics may perform the fixed
reconstruction and verify every original density hypothesis, including
both infinite tails and all derivatives. Then test exact membership in the
covered finite class and handle the positive damping parameter explicitly.
If it matches, check the entire-function growth/product hypotheses and
import the first Laguerre inequality instead of scanning for a negative
value. This is a routine specialization of known mathematics, not a
creative Xi mechanism and not a reason to reprove Newman's theorem.

If a negative value remains possible after that comparison, require a
complete analytic or interval certificate, with differentiated-integral
and tail bounds. A sample is insufficient. If the known-class match fails
and no bounded certified sign test emerges, park this fixed diagnostic;
do not vary its parameters. A changed model or a generic implication needs
REVIEW_REQUIRED coverage. The original 1988 theta-shape proof remains
unread and is unnecessary for this independent model test.

Outcome: EXPLORATION, completed literature comparison with ready scope
for the same target. No new mathematical result, reconstructed density,
sign witness or established class membership is claimed. The plausible
downstream use is to eliminate a misleading generic counterexample or,
if a rigorously valid negative sign emerges, reject the generic criterion.
Actual-Xi first-sign transfer and all higher signs remain open. A justified
creative actual-Xi mechanism is still blocked by missing sign transfer;
this known-class specialization is not relabeled creative to fill a quota.
