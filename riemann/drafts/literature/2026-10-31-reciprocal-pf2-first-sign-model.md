# Reciprocal-density log-concavity: fixed first-sign diagnostic

TARGET: Test the fixed degree-eight polynomial P in the reciprocal-PF2 assessment for a positive log-concave density p with bilateral Laplace transform 1/P on |Re z|<1 and P'(10)^2-P(10)P''(10)<0; certify both claims or reject this fixed model.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Exact reciprocal-polynomial, rational bilateral-transform, PF2/nonreal-zero and log-concavity/Laguerre searches in the parent discovery found no inspected matching theorem; local searches distinguish L049/L055's direct-kernel countermodels and L233's weighted autocorrelation model. Queries and source comparisons are retained in the parent assessment; no novelty inference.
SOURCE_EVIDENCE: Sra riem-xi v2, Corollary 2.5 and Proposition 3.3 with its proof, supplies the motivating reciprocal-density object, not a theorem about P; primary reading is in the parent discovery. NIST DLMF 1.14.1--4 and the uniqueness paragraph in 1.14(i), inspected 31 October 2026, cover Fourier normalization/inversion/uniqueness; Cauchy's residue theorem is an optional standard named input, not a new inversion lemma.
COMPARISON: Known reciprocal-density positivity is not a proved global first-Laguerre transfer. This fixed polynomial tests PF2/log-concavity only; it neither matches nor refutes PF256, and the direct Fourier-kernel models do not settle it. No inspected theorem establishes the proposed pair of properties.
GAP: Establish the inverse density's global positivity, integrability, C2 matching at zero, transform identity and curvature sign, together with the exact negative polynomial jet value; all are unproved for this fixed P. No actual-Xi realization is sought or assumed.
REASON: An independently testable finite calculation can assess the weakest reciprocal-density sign inference before pursuing it. Import standard inversion; the model-specific global curvature check, not the criterion's restatement, is the proposed mathematical work. No calculation or result is approved as true here.
SCOPE: Exactly the polynomial below, with a single global density/curvature and exact-jet test. No parameter search, PF256 claim, infinite-zero or actual-theta extension. This ready nomination was written during the preceding literature turn and requires the supervisor's separate continuation approval.

## Fixed object and significance

Define the proposed test polynomial, without asserting its desired signs,

    P(z)=(1-z^2)(1-z^2/4)
          (1-z^2/(10+i/4)^2)(1-z^2/(10-i/4)^2).

Seek an even, strictly positive, integrable C2 function p on R with
integral 1, satisfying

    integral_R exp(-zx)p(x) dx = 1/P(z)   (|Re z|<1),
    p'(x)^2-p(x)p''(x) >= 0             (every real x),
    P'(10)^2-P(10)P''(10) < 0.

These are the **test thresholds**, not conclusions or a derived formula.
The density condition is ordinary log-concavity, without a strict
curvature requirement. Even if certified, it would test only that
condition, evenness and the finite-product model; it would not test
Sra's order-256 hypothesis, Xi's full growth, zero counting or theta
realization. A polynomial test is not an RH counterexample.

The main bottleneck remains actual-Xi all-degree mixed positivity.
C233a and L233 identify the first-sign gap. This diagnostic could rule
out a tempting reciprocal-density transfer, or show that this fixed
model fails to test it. It supplies no positive signed mechanism for
the complete residual. Higher signs remain separate in either outcome.

## Covered starting tools and obligations

Source reading/motivation:
[completed discovery](2026-10-31-complete-first-sign-mechanism-discovery.md).
The source's actual-Xi probability proof is not automatically applicable
to a finite polynomial. No self-decomposability, unimodality, PF256,
or numerical certificate is imported into this model.

[NIST DLMF 1.14.1--4](https://dlmf.nist.gov/1.14#i) uses the unitary
Fourier normalization. Equation 1.14.3 assumes absolute integrability
and local bounded variation, giving the mean of one-sided values;
the uniqueness paragraph assumes continuous integrable functions.
The test must reconcile its Fourier signs and normalization with the
bilateral convention above. DLMF's one-sided Laplace inversion is not
being cited as a bilateral theorem. Direct integration of a proposed
finite exponential/trigonometric density is an allowed alternative.
If residues are used, justify the contour decay and its orientation;
do not silently take only real poles. Checking the resulting finite
formula is a model specialization, not a reproof of Fourier inversion.

Do not infer a global sign from a plot or finite grid. Treat x=0 and
both tails explicitly; a compact interval certificate needs a rigorous
tail bound and derivative matching. Rational coefficients, trigonometric
inequalities and certified intervals are allowed after approval.
If a script is useful, keep its complete evidence under a local
`scripts/` subfolder and print only conclusions, bounds, failures and
certificate paths. No script was written in this literature turn.

Continue the PF2-only inference only if this proposed countermodel
fails and a materially new discriminating test is justified. If both
thresholds are proved, stop that inference and preserve the qualified
countermodel. If either claim fails or remains uncertified, reject or
record this fixed test without treating it as evidence that the
inference holds. Do not automatically tune parameters or enlarge the
target during the same attempt.

Mathlib: matching result and supporting inversion/residue coverage
not checked; no absence or formal verification is claimed.
