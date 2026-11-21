# Suzuki parameter descent — completed bounded source comparison

TARGET: Assess the exact composition and compression relations for Suzuki's complete operators K_theta[t], testing whether a signed defect can transfer contractivity from 2theta to theta for theta>=2, without assuming RH or a fixed-parameter all-window bound.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Exact Suzuki/title/composition and semigroup searches; continuous Wiener-Hopf/Hankel product-formula search; semigroup-contraction and delay searches. Scoped searches of L618, its assessments, construction/screw stops and parameter-descent records found no existing signed doubling defect. No adequate descent theorem was located; this is bounded coverage, not an absence or novelty claim.
SOURCE_EVIDENCE: Suzuki 1907.07302v2 (6 March 2020), printed pp.1-3,5-8: (1.1),(1.10)-(1.13), Theorem 1.2, Propositions 3.1-3.2 and relevant proofs, (3.8)-(3.10),(3.13),(3.15) with its full domain/Fubini argument; Basor-Ehrhardt, NYJM 11 (2005),171-203, section 3.1 p.178 (30)-(34); Ehrhardt, Factorization theory for Toeplitz plus Hankel operators and singular integral operators with flip (2003), section 2.3 p.23 Proposition 2.2 and proof, p.24 adjoint formula (2.49).
COMPARISON: The sourced product laws retain a reflected symbol and Wiener-Hopf factors, while Suzuki (3.15) is a weighted formula for the untruncated output, which need not be L2. Neither source supplies a same-window square identity or a signed defect yielding descent. L618's compact-window parameter limit remains valid but cannot be promoted by these citations to fixed-parameter all-window control.
GAP: No independently controlled favourable defect for the actual complete operators has been found. An exact Suzuki same-window compressed composition and any descent implication remain unproved. One later, separately gated small-window test of the simple Loewner square defect is specified below; it is not an established obstruction or transfer theorem.
REASON: This review identifies a concrete domain/reflection mismatch in the direct semigroup implementation and parks that implementation. The primary small-x formulas permit a limited actual-kernel diagnostic without assuming RH, innerness or global contraction; no signed estimate is derived here.
SCOPE: Source comparison for complete Suzuki kernels, real theta>=2, finite t>=0 and doubling; no new operator identity, kernel construction, arithmetic truncation, zero-free result or determinant/RH equivalence is imported. EXPLORE does not approve unrestricted attempts at the broad descent claim.
LITERATURE_REASON: Essential composition and compression hypotheses are outside L618's ready norm-estimate coverage; a separate literature-only step is required before any parameter-descent attempt.

## Original nomination and discriminator (retained)

The main gap remains an unconditional actual-Xi sign mechanism. The
intermediate source target is to decide whether the complete-kernel
parameter can be decreased while preserving contractivity. A valid
transfer might make the available compact-window bounds relevant at a
fixed parameter; further links to determinant control, actual-Xi signs
and all windows would still require their exact hypotheses and proofs.
No such downstream implication is assumed.

L618 is the prospective local input. Its canonical conclusion is
sup_(0<=t<=T)||K_theta[t]|| <= 16T exp(31T)(28/41)^theta for fixed T.
The defining completion is inherited from L018; L001/L005 enter L618's
existing proof. These are prospective inputs, not a new dependency
graph. The norm estimate is already independently audited in L618;
do not audit or reproduce it again. Source coverage for its derivation
is reusable, but does not approve the new target.

Start with Suzuki's exact operator and transform definitions at
https://arxiv.org/pdf/1907.07302v2, then inspect only the primary
composition/compression results needed for the comparison. Reuse
`2026-11-01-suzuki-large-parameter-compact-norm.md` for the scope of
the norm estimate. Compare the construction and screw-function stops
in `ATTEMPTS/2026-10-31-theta-de-branges-construction-source-stop.md`
and `ATTEMPTS/2026-11-01-screw-criterion-signed-remainder-source-limit.md`.
Their missing positive actual-pair data and signed remainders cannot
be assumed through operator notation. Do not retry the blocked report.

The bounded discriminator is an exact primary-source relation with a
specified defect whose independently established sign or bound could
support a contractivity implication. Retain every cutoff, projection,
reflection, domain and weighted-Fourier condition. Check the strongest
known statement and elementary generic obstructions at source level;
do not silently substitute an uncompressed convolution or Toeplitz
operator for the Hankel compression. A scalar multiplier identity alone
does not meet the discriminator. If the necessary defect control merely
rephrases the missing fixed-parameter contraction, or known obstructions
already defeat the proposed implication, record that result and park
this implementation without a new calculation.

At most three source chains: the exact Suzuki construction; primary
Hankel/compression composition results; known semigroup-contraction
transfer or counterexamples. Nominate at most one concrete later
inequality after comparison. No new lemma, mathematical script or
operator identity is derived in this nomination. Mathlib coverage for
the new question is unchecked. No originality or absence claim follows.

This is source discovery, not an approved proof_attempt/creative. Its
blocker is the missing exact signed defect and its source scope. A later
creative nomination must specify that defect, the main-gap relevance
and a bounded mathematical test; the present audit cannot approve it.

## Completed review, step 266

The three bounded source chains were: Suzuki's definitions and weighted
operator formula; primary continuous/discrete compression algebra; and
searches for semigroup contraction transfer or delay obstructions.
Representative queries were `Suzuki "Integral operators arising"
composition convolution theta`, `Wiener Hopf Hankel operators W(ab)
H(ab) continuous real line product formulas`, and `"semigroup"
"Hankel" "contraction" powers`. Delay and gamma-subordinator search
results were leads only: no generic counterexample is imported from
them, and no new model was constructed. Scalar multiplication of
Suzuki's exponential symbols is not an operator-composition theorem.

In [Suzuki v2](https://arxiv.org/pdf/1907.07302v2), (3.15) retains
`(Ff)(-z)` for `Im z>1/2`. Its proof treats the untruncated output
supported in `[-t,infinity)`, explicitly without an L2 conclusion.
Equation (1.1) instead has both the input cutoff and output cutoff at
`t`. Thus this primary formula does not authorize a second application
as a bounded unweighted full-line operator, or deleting the cutoff
between applications. No same-window doubling identity is stated in
the inspected passages. Theorem 1.2 supplies local determinant
nonvanishing, not the requested descent estimate.

For a precise comparison, [Basor and Ehrhardt, section 3.1,
p.178](https://nyjm.albany.edu/j/2005/11-10p.pdf) assume bounded symbols
`a,b` on the real line and act on `L2(R_+)`. Their convention uses the
Fourier kernel `exp(-i xi x)/(2pi)`, reflection `Jf(x)=f(-x)` and the
positive-half-line projection. Equations (32)-(33) state

    W(ab) = W(a)W(b) + H(a)H(tilde b),
    H(ab) = W(a)H(b) + H(a)W(tilde b),  tilde b(u)=b(-u).

Equation (34) defines the additional finite-section projections `P_R`
on both sides. These are full half-line identities, not identities
obtained by replacing every factor by its finite section. Their terms
are not supplied with a favourable sign for the present question.
The paper's determinant asymptotics concern different specified
symbols and are not an actual-Xi contraction input. Its `L1` condition
is needed for the literal integral-kernel representation, whereas the
bounded-symbol operator definitions already act on L2. We do not
identify Suzuki's shifted contour, reflected cutoff and unweighted
norm with this model without an applicability proof.

[Ehrhardt's 2003 habilitation](https://d-nb.info/972573305/34), section
2.3, Proposition 2.2, printed p.23 (PDF p.25), supplies the corresponding
circle formulas for bounded matrix symbols on `(H^p(T))^N`, `1<p<infinity`.
The complete short proof inserts the complementary Riesz projections,
uses `JM(b)J=M(tilde b)` and then compresses. Formula (2.49), p.24,
retains the reflected symbol in the Hankel adjoint. This confirms why
a product correction is not automatically a positive adjoint-square.
No circle-to-Suzuki specialization is claimed.

Direct shell retrieval of the Suzuki PDF failed DNS; primary text was
read successfully through the web PDF extraction. Web screenshots
returned no usable image content. The Virtanen repository PDF timed
out, so it remains an unread supplementary lead, not a blocker or an
input: the inspected Basor-Ehrhardt and Ehrhardt statements suffice
for the comparison. Suzuki's older Hamiltonian paper is also only a
reference lead here; no theorem from it is assumed.

The source mismatch is informative against direct semigroup descent,
not a counterexample to descent for actual Suzuki operators. No
unconditional reflection/compression defect with the needed sign was
found. Park direct descent from L618. A generic support-delay
counterexample has not been verified, and no statement excluding all
parameter methods follows.

The single proposed later inequality is the sign of
`<f_t,(K_4[t]^2-K_2[t]^2)f_t>` with
`f_t=1_[-t,t]/sqrt(2t)` as `t` decreases to zero. A negative value
would exclude the sufficient order `K_2[t]^2 <= K_4[t]^2`; it would
not refute a bare contractivity implication. Small windows may have
both operators contractive. The separate assessment
`2026-11-04-suzuki-small-window-square-defect.md` records the exact
source scope and the still-unperformed specialization. No sign,
leading coefficient or operator asymptotic has been calculated here.

Mathlib: full operator/product/signed-defect coverage was not checked;
availability is unknown. No formalization or originality claim is made.
