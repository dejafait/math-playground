# Positive-z opposite-coefficient trace obstruction — coverage comparison

TARGET: Test whether L159's two-trace obstruction forces m_{-1}m_1=0 for 0<=z<=119 while retaining the ordinary twisted top sheaf W.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 525 compared L147's ordinary images, L157's signed degree-one comparison and audit, L158's four-edge proof, L159's raw restriction/strictness proof and ATTEMPTS/069,/089,/090; targeted non-IT hyperholomorphic/direct-image searches found no inspected theorem stating the desired multiplicity restriction.
SOURCE_EVIDENCE: Reuse step-521/523 Verbitsky/Demailly operator and Stacks cup/trace primary reads; freshly read Stacks 20.13.4 (01F2), 36.30.1 (0A1H), 36.31.3 (0BDK) and 48.15.7 (0BRT), statements and displayed proofs, https://stacks.math.columbia.edu/tag/01F2 and corresponding tag URLs below, accessed 2026-10-24.
COMPARISON: General Leray, derived base change, duality and raw-form trace tools allow a bounded test with W retained; neither these sources nor L159 give positive forward concentration or positive-z strictness. L157 already covers the negative forward degree-one edge at arbitrary allowed z and both opposite transforms.
GAP: Determine the positive forward edge and possible kernel supported at Z without replacing its full derived image by M^vee[-1]; justify nonzero restrictions and both strict trace components, or identify the exact failure before using the quartic identity.
REASON: Essential general source coverage is adequate for one separate specialization attempt, including a failed-edge verdict. The missing positive-z comparisons are explicit mathematical obligations, not an inaccessible source or an imported theorem; no multiplicity restriction is established by this review.
LITERATURE_REASON: The changed hypothesis permits the twisted point sheaf W and does not supply L158's concentrated positive forward coefficient; reuse ready operator sources while reviewing this specific new edge/trace scope.

This target entered step 525 as REVIEW_REQUIRED. The completed comparison
below approves one subsequent bounded mathematical attempt under
SPECIALIZE, subject to the supervisor's separate approval of this changed
assessment. It proves no new result. The exact TARGET text is preserved.

The main gap remains universal primitive rational Hodge realization.
The intermediate target is the stated conditional line-multiplicity
restriction. Its plausible downstream use is to narrow the actual line
spectrum of M outside the two extremal z=0 branches, which the additive
tests and L158's weaker multiplicative relaxation leave compatible.
It need not settle F existence, other stable summands, a lower split
count or transport. Those independent gaps remain open.

Retain identical marked K3 factors and common g,h; the hypothetical
locally free Omega-polystable rank-two F with integral c_1=0 and
ch(F)=2-14e_1-21e_2-tau_D+62P; preferred dual HE lines of class
k=(-4,-2,1,2), k.h=0, k^2=-14 eta and integral eta of degree one.
Now allow 0<=z<=119, including positive z; keep L147's actual M and
W, L153's polystability and L156's endpoint vanishings. The meaning
of m_t is L157's full line multiplicity. L071's actual connection,
L157's signed powers/degree-one comparison, audited L158's cups and
audited L159's operator/sign argument are the exact proposed inputs;
L093 supplies the retained untwisted concentration. No cross-notebook
input is proposed. No full matching Mathlib result is asserted.

The continuation test is source adequacy for the actual coefficient
comparisons with W retained. Approve a separate bounded proof attempt
only if those comparisons and the harmonic hypotheses are covered;
otherwise identify the precise missing coverage. Do not assume the
positive forward complex is M^vee[-1] at positive z, infer a
multiplicative derived splitting, or import a zero-z trace sign solely
from perfection. ATTEMPTS/069,/089,/090 and the completed z=0 argument
remain preserved.

## Completed source comparison — step 525

This is LITERATURE / EXPLORATION / REPRODUCTION, actual task type
literature_comparison. No lemma, mathematical script, DAG or argument
overview is changed. Mathematical exploration usage remains one after
step 522's informative negative; this source review spends none.

**Reusable harmonic scope.** The primary read register in
[step 521](2026-10-24-dual-coefficient-quaternionic-trace-sign.md), checked
against [step 523](2026-10-24-dual-coefficient-trace-sign-critical-audit.md),
already covers Verbitsky, *Hyperholomorphic bundles over a hyperkähler
manifold*, alg-geom/9307008v1 (29 July 1993), Section 4, Theorem 4.1 and
Corollary 4.3 pp. 15–16 and the doubled-dual proof of Theorem 4.2.A p. 17
([primary preprint](https://arxiv.org/pdf/alg-geom/9307008v1)). Those
harmonic inputs concern the actual hyperholomorphic coefficient and its
dual on the compact product; their hypotheses do not include IT of a
projection. This source-scope observation does not extend L159's
conclusion: its extracted operator, determinant normalization and raw
restriction comparisons must be retained and checked against the changed
data. Neither an independently rotating factor nor a real structure on
an individual twist is imported.

Demailly, *L2 vanishing theorems for positive line bundles and adjunction
theory*, alg-geom/9410022v3 (28 February 1995), Sections 1.A pp. 4–5 and
4.A (4.3)–(4.4') pp. 27–28
([primary preprint](https://arxiv.org/pdf/alg-geom/9410022v3)), remains the
recorded source for locally free coefficient Dolbeault products and
normalized Serre integrals. Smooth locally free Q_s on X and its fibres
retain those hypotheses. This does not imply strictness of a particular
restriction. The counit/trace primary reads and qualifications in steps
516/519/523 also cover general derived coefficients, not only IT objects:
Stacks 0FP3, 0FP6, 0H99, 0AAB, 0B6J and 0BRT. In particular the proof
of 0H99 remains recorded as omitted, not newly inspected.

**Changed edge scope: fresh primary checks.**

- [Stacks Lemma 20.13.4, 01F2](https://stacks.math.columbia.edu/tag/01F2)
  gives Leray for a morphism of ringed spaces and a bounded below
  coefficient complex. Its displayed proof reduces to the Grothendieck
  spectral sequence. Q_s fits this scope with either projection. The
  theorem supplies the spectral sequence; vanishing terms, surviving
  edges and any injectivity are specialization obligations.
- [Stacks Lemma 36.30.1, 0A1H](https://stacks.math.columbia.edu/tag/0A1H)
  assumes finite presentation, a perfect E, and a bounded finitely
  presented base-flat complex with proper support. It gives perfect
  pushforward and arbitrary derived base change. Here take E=O_X and
  the locally free coefficient Q_s; the projective smooth projections
  meet these hypotheses. Read the proof's base-change reduction,
  Noetherian case and approximation case; the invoked supporting lemmas
  were not newly followed. Derived base change does not itself identify
  ordinary R^1 at a jumping fibre with fibre H^1.
- [Stacks Lemma 36.31.3, 0BDK](https://stacks.math.columbia.edu/tag/0BDK)
  characterizes the open locus where a perfect object is a rank-r bundle
  in one degree by the corresponding pullback property. Its proof uses
  fibre Betti functions and finite locally free representatives. It
  permits checking concentration on an appropriate open locus, not
  erasing W on the whole base.
- [Stacks Lemma 48.15.7, 0BRT](https://stacks.math.columbia.edu/tag/0BRT)
  identifies the right adjoint's value on O with omega_f[d] for a smooth
  proper relative-d-dimensional morphism over a Noetherian scheme. Read
  the diagonal/Koszul proof again. Here d=2 and a chosen K3 form
  trivializes omega_f. The theorem is a derived duality input; it does
  not replace a two-cohomology-sheaf complex by its middle bundle.

These are the only fresh theorem reads. The general duality and
base-change hypotheses survive positive z. BBHR's IT preservation
theorem is reused only for L157's separately proved opposite H_1 and
H_-1; it is not newly applied to the positive forward coefficient.
No general theorem warrants reproof.

**Exact local distinction.** L157's proof of (5), and its audit of that
passage, expressly retain W and establish the negative forward
total-degree-one comparison for both d signs. Its independently
concentrated opposite transforms also remain available. By contrast,
L158's proof of P_+=M^vee[-1] explicitly begins with W=0. L159's
strictness uses all four concentrated forward/opposite rows, so its
quoted conclusion cannot simply be relabeled for arbitrary z. These
are comparisons of existing proofs, not new positive-z edge statements.
The local question is whether duality/truncation and actual generic
restriction supply the needed replacement, including any contributions
supported at Z. It is left entirely to the next mathematical attempt.

**Discovery and duplicates.** New queries were `hyperholomorphic bundles
opposite coefficient cohomology restriction trace positivity non IT
Fourier transform` and `hyperholomorphic bundle higher direct images
torsion K3 Fourier transform base change`. Together with step 521's
recorded operator searches they locate general tools but no inspected
matching multiplicity theorem. Teleman's *On the torsion of the first
direct image of a locally free sheaf*, AIF 65 (2015), 101–136, and
Verbitsky's *Stability of Fourier-Mukai transform* appeared as leads;
their theorem/proof contents were not read and are not inputs or evidence
of this restriction. No novelty inference follows. ATTEMPTS/069's
unknown actual entry and /089,/090's compatible formal relaxations
remain valid; neither further additive filtering nor chosen cup matrices
answer this changed actual-connection question.

**Approved bounded test and stopping rule.** Keep the exact TARGET.
First check the positive forward degree-one edge with the full derived
image retained, and determine whether nonzero classes are detected on
some smooth fibre in each direction. If that comparison is justified,
test L159's actual harmonic/raw-trace argument for both opposite pairs
and then the four-input identity. The desired threshold is precisely
m_-1*m_1=0 throughout 0<=z<=119, not an improved upper bound for z.
Continue only with a justified edge/strictness bridge or an informative
failure locating a kernel or uncontrolled term. If that bridge fails,
record the obstruction and park this extension; do not silently assume
positive concentration or infer strictness from perfect duality.

All essential inputs and numerical hypotheses in the preceding proposal
remain mandatory: L071, L093, L147, L153, L156, L157, audited L158 and
audited L159, used only within their proved scopes. F existence, other
stable summands, independent lower control, transport and universal
primitive realization remain unresolved. Full matching Mathlib coverage
is **not checked**, with no absence claim. No cross-notebook input is used.
