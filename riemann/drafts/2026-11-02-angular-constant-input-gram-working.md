# Angular constant-input Gram — bounded attempt

STEP_ID in preparation: 2026-11-02-angular-constant-input-gram-01.
The unchanged ready EXPLORE assessment is
`drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md`.
This is a mathematical attempt on its exact target, not a new source review.

Main gap: actual-Xi all-degree mixed positivity at unbounded heights.
Intermediate target: the approved common-pole angular largest-norm bound
at exponent 1/32. A uniform lower bound from the constant input would
suffice for that synthetic estimate; layer isolation, other poles,
census/clearance, simultaneous Xi realization, a matching upper bound
and signs would still be independent gaps.

Retain n>=5, x=-5/4, R=11/8, U=R^2, eta=1/100, t_j=j/n,
distinct common poles Re(a)=x, |a|<=R-eta, x in Z, positive integer
original simple-pole residues, M<=n/3, and the conjugated denominator
angle. C645g supplies spaces/scaling. C645l's fixed-angle obstruction,
C645m's envelope stop and C645n's inner-input response stop are retained
as contrasts, not assumed angular lower bounds. Their relevant
hypotheses, conclusions and the saved working note have been inspected.

Proposed calculation: with u=i*exp(i*theta), set

    W_a(u)=(x/a)*product_(j=1)^(n-1)
       [(x-t_j*u)/(a-t_j*u)]*[(U*u-t_j*a)/(U*u-t_j*x)].

The common interior poles are p_j=t_j*x/U, and the individual exterior
poles are a/t_j. Cancellations at special a must be justified, and the
conjugate factor in the Gram entry introduces additional interior poles.
Since H_q 1=q, the proposed exact sufficient quantity is

    mean ||q||_2^2 = sum_(a,b) r_a*r_b*
       mean[W_a*conjugate(W_b)]/(U-a*conjugate(b)).

This identity still needs its complete interchange and residue argument.
Its positive semidefiniteness alone is not the target. First test whether
the constant-input Gram admits an entrywise positivity/noncancellation
estimate; if that fails, retain the exact failure and any refined test.
Success means a uniform positive constant/onset at exp(-n/16) for this
squared response, or a rigorous admissible full-operator countersequence.
A finite screen, unevaluated Gram matrix, or inferior lower bound is
not decisive evidence for the approved target.

Partial checkpoint saved before calculation. No new theorem is claimed.

## First calculation checkpoint

The nonrigorous screen in
`scripts/one-sided-hankel/angular-constant-gram-screen.json` finds
negative real anchor cross entries, including n=12 and a=x+i/2,
Re K(x,a) approximately -0.1408. This has no error enclosure yet.
It suggests that dropping cross terms by entrywise positivity is
invalid, not that the full positive quadratic form is small.

For an exact calculation define W_b^#(u)=conjugate(W_b(1/conjugate(u))).
The interior poles of W_a W_b^#/u are 0, p_j=t_j*x/U and
q_j=t_j/conjugate(b). The latter poles are essential. When a=x or
b=x its whole corresponding factor is identically one and must be
cancelled before listing poles. For a,b different from x, all listed
p_j and q_k are distinct because p_j is real and q_k is nonreal.
The intended formula is the residue sum at all of these points,
with the residue at zero x^2/(a*conjugate(b)). Exact verification of
the n=12 witness and complete justification of this formula remain.

## Completed calculation and bounded refinement

The proof of the exact constant-input quadratic form, the complete
residue formula and the rational negative cross-entry witness is now
canonical in
[C645o](../lemmas/C645o-angular-gram-residues-and-negative-cross-entry.md).
At n=12, a=x+i/2, Re K(x,a) is strictly between -141/1000 and
-140/1000. The full compact residue table and all 16 exact checks in
`scripts/one-sided-hankel/angular-constant-gram-certificate.json` were
inspected. C645o is unaudited. The numerical screen suggested the case
but is not proof; its small Chebyshev-family sample supplies no
asymptotic conclusion. The entrywise-positive shortcut is retired.
The threshold for the complete signed Gram remains unresolved.

A distinct bounded refinement within the unchanged ready Fourier scope
is to project q onto its nonpositive angular modes, keeping the zeroth
mode as well as the negative modes. This is proposed work, not an
established estimate. The negative modes can be computed from the
common p_j principal parts of W_a; the nonconstant positive modes from
the exterior poles are orthogonal to the proposed projection. C645o's
R_j(a) and mu_a=I(a,x) provide concrete input data for that calculation.
Retaining the zeroth mode is essential: for Z={x} all negative angular
modes vanish although q is nonzero.

The test is whether this projection alone has L2 norm over the two
circle variables at least c*exp(-n/32), uniformly over the original
integer-residue families. The computation must retain signed sums of
residues; positive semidefiniteness of a projected Gram matrix is still
insufficient. A proof at that rate suffices for the saved angular
target. A slower lower bound or a small projected response does not
refute the full operator bound; stop that projection mechanism if its
complete response is rigorously inadequate, and preserve the failure.

Essential continuation inputs are C645g's normalization and C645o's
product-specific residues (independent audit pending), together with
the inspected scalar Fourier/residue sources in the unchanged
assessment. C645l, C645m and C645n remain distinct historical contrasts.
No separation, symmetry, real-amplitude sign, angular disk holomorphy
or Xi realization is introduced. The target and every original family
hypothesis remain exactly those of the assessment. No new assessment
or uncovered theorem is approved here.
