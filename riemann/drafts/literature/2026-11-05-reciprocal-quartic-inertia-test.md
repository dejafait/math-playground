# A single reciprocal-factor quartic inertia diagnostic

TARGET: Test the reciprocity-only inertia premise for G_0(z)=(z+4/5)(z+9/10)(1+4z^2/5) at r=3,R=1 by exact local-factor admissibility, projection weighting and J-Q inertia checks.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step448's linked-factor-hermitian-realization-review.md: reciprocal Toeplitz/Hankel, indefinite Schur/completion and polynomial root/minor searches and local duplicate comparisons are recorded there. No inspected theorem settles this specified model; no originality is claimed.
SOURCE_EVIDENCE: Böttcher-Widom math/0604009v1 (1)-(2), Theorem1.1 and Section3 pp.2-3,5 https://arxiv.org/pdf/math/0604009v1; de Boor Example2/(10), Proposition25/(26)/proof pp.49,53-54 https://pages.cs.wisc.edu/~deboor/sat/papers/2/2.pdf; Duits DPP2 Lemmas66/69 pp.51-52 https://people.kth.se/~duits/static/media/DPP2.44e051d148b79af222fa.pdf; Berkolaiko-Kuchment DOI10.4171/JST/395 Lemma2.3 and Theorem2.7/proof pp.87-91 https://ems.press/content/serial-article-files/33861. Prior complete proof-case coverage reused; direct sources and selected interfaces rechecked in step449 below.
COMPARISON: General determinant, divided-difference and inertia interfaces are known. Their specialization to this rational model is unpaid; L782 proves its weighting only for the actual (3,2048) pair and cannot be cited as a generalization. All-minor real-root criteria do not by themselves identify this prescribed signed matrix or minor.
GAP: Verify exact model admissibility and residues, calculate the complete rational Laurent tail with convergence, justify its projected pairing and diagonal similarity, then determine full inertia including nullity. No model sign or obstruction is asserted here.
REASON: A local-factor countermodel could reject sufficiency of reciprocity plus selected local real-zero data even for a genus-zero polynomial with nonnegative coefficients; it would isolate a needed extra Xi premise instead of replaying an actual-pair sign or stopped class test.
SCOPE: Exactly the displayed quartic, r=3,R=1,k=2 and proposed sigma=21/20 to be checked; one exact rational/algebraic calculation. No parameter sweep, Taylor-index test, actual-Xi conclusion, global class hypothesis or new general theorem. Separate literature approval completed in step449; model conditions and inertia remain uncomputed.

## Purpose and proposed data

The main gap is actual-Xi all-degree mixed positivity. This diagnostic
tests sufficiency of the local reciprocal factors for the coupled index
bound. It can remove an unsupported generic shortcut; a useful Xi
mechanism would still need an additional structural input.

Use G_0 above, P(z)=(z+4/5)(z+9/10), F_0=G_0/P,
p=z^-2 P, b=p/F_0, c=F_0/p. These are definitions, not verified
hypotheses or an asserted negative minor. Verify G_0(0)>0, G_0(1)>0,
real nonnegative coefficients, exactly two simple negative nonzero zeros
inside the unit disk, contour nonvanishing and zero-freeness of F_0
on a neighborhood of the closed sigma disk. Retain all exterior roots
in the check. Also check the polynomial genus-zero representation and
order-at-most-one-half growth upper bound if using them in the conclusion.
Do not claim actual-Xi theta realization, strip geometry, strictly
positive infinitely many coefficients or asymptotic zero counts.

Essential methodological inputs: L777's one-based factor/projection
conventions; L782's fixed-pair normalization as a comparison only; L780's
constraint against positive-block arguments. L779 numerical data/software
contracts are unnecessary for this exact model. L017/L018/L021/L776
explain the actual-Xi motivation, not mathematical assumptions about G_0.
No cross-notebook input is needed.

## Covered specialization and thresholds

After checking the roots alpha_i, use complete residues
d_i=alpha_i^2 F_0(alpha_i)/P'(alpha_i), C=diag(d_i), and
V_(l,i)=alpha_i^(l-1). Put U=Q_3 H(b)V, Y=Q_3 V and S=Y*U.
Determine residue signs and ordering rather than assuming the actual
pair's signs. Calculate all needed positive-index Laurent coefficients
beta_n of the complete rational b on its correct annulus. Exact partial
fractions, geometric series and the standard residue theorem are available
methods; a finite Taylor truncation is insufficient.

Define the proposed mechanism's objects by

    h_3(z)=sum_(n>=0) beta_(4+n) z^(n+1),
    K_ij=(h_3(alpha_i)-h_3(alpha_j))/(alpha_i-alpha_j),
    K_ii=h_3'(alpha_i), E_ii=sqrt(|d_i||alpha_i|^3),
    J=diag(sign(d_i)), Q=-E K E.

Check this model's projected pairing, complete-series diagonal limit,
invertible diagonal similarity and determinant orientation by specializing
the cited interfaces. No model identity is asserted here; this check is
needed because L782's statement is restricted to its actual pair. Do not
reprove the general source theorems. Distinguish operator projection Q_3
from finite matrix Q. Retain the complete c, including its analytic part
when identifying its negative Laurent coefficients.

The discriminating threshold is failure of

    n_0(J-Q)=0 and n_-(J-Q)=n_-(J).

Determine full exact inertia, not determinant parity alone. Exact
congruence/LDL or symmetric 2-by-2 trace/determinant classification must
cover zero cases and every denominator. Algebraic square roots may be
removed by an explicitly justified positive diagonal congruence. An
optional orientation check may compare the exact 3-by-3 coefficient
Toeplitz determinant using the cited Fredholm identity and checked
nonzero prefactors; that comparison cannot replace full inertia.

If an adverse inertia and all listed local conditions are certified,
stop the reciprocity-only sufficiency claim and state precisely which
stronger Xi properties the model does not test. If the prescribed
inertia holds, record a nondiscriminating result and close this diagnostic.
If a local condition fails, reject the chosen model without tuning it.
No automatic degree, parameter or precision sweep is authorized. Passing
one model proves no universal bound or Xi sign.

This is REPRODUCTION by known rational-function and matrix methods,
not a creative Xi mechanism or certified novelty. No values, lemma,
counterexample or script were produced while preparing the assessment.
If later scripting helps, save complete exact evidence under local
scripts/ and print actual/required indices, failures and paths only.
Full matching Mathlib coverage remains unchecked.

## Direct-source repair and approval — step449, 2026-11-05

This is a source-reference repair and separate approval of the unchanged
target, not a mathematical attempt. Reuse the inspected theorem/proof cases
in `2026-11-04-exact-projection-similarity-review.md`,
`2026-11-04-signed-rank-two-fredholm-diagnostic.md` and
`2026-11-05-linked-factor-hermitian-realization-review.md`.
Their local comparisons and the step448 stop record cover the relevant
duplicate and failure checks. No new discovery search is needed for this
unchanged finite rational specialization, and no novelty is inferred.

All four direct primary PDFs above were accessible on 2026-11-05.
Böttcher-Widom v1 pp.2,5 were rechecked: nonvanishing zero-winding
C^beta symbols (noninteger beta>1/2), normalized factors and the full
inverse-product/Jacobi proof. This is a determinant interface; optional
Toeplitz comparison must verify its symbol and factor hypotheses.
It supplies no compressed Hermitian inertia bound.

De Boor's published author version (21 December2004; volume1,2005)
pp.53-54 was rechecked through the Newton-basis proof and repeated-node
continuity step in Proposition25. Reuse Example2/(10)'s quotient/derivative
convention. Do not use the previously flagged ambiguous extraction of
display(27). Polynomial identities do not pay the infinite-series limit;
the quartic calculation must establish convergence separately.

Duits's undated filename-identified author version, printed pp.51-52,
remains the finite-rank reference. Lemma66 and its block-matrix proof,
and the finite-dimensional restriction definition, were rechecked.
Reuse the previously read complete Lemma69 proof and its linear-first
inner-product qualification. Only finite-dimensional algebra after
restriction is approved; no unexamined counting-measure extension,
selfadjointness or norm-smallness premise is imported.

Berkolaiko-Kuchment's 2022 publisher version pp.88-89 was rechecked
for Theorem2.7's domain-preserving orthogonal decomposition,
selfadjoint blocks, essential-spectrum and cross-block bounds, finite
indices and explicit nullity formula. Its complete proof remains covered
by step448. For the proposed finite symmetric diagnostic this is a
congruence/index interface, never an automatic residual-index estimate.
No proposed model has been shown to satisfy any of these premises here.

DECISION remains SPECIALIZE; the saved target is approved for one
REPRODUCTION calculation. No new theorem, coefficient, residue, inertia,
counterexample or mathematical script was produced. The discriminating
threshold and stop rules above remain unchanged. This repair provides
no new mathematical evidence and does not reset exploration usage.
