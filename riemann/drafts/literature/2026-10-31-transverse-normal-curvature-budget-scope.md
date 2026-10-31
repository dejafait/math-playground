# Transverse normal curvature — completed source comparison

TARGET: Assess whether a transverse normal-curvature formula for |xi(1/2+a+it)|^2, using boundary jets at a=3/2 and retaining the full signed forcing, yields a zero-safe remainder test for L233 that escapes L501's harmonic cancellation and the fixed-x Lorentz obstruction.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched xi modulus-square convexity, horizontal monotonicity, normal/transverse curvature, Poisson forcing and boundary Taylor/Laguerre remainder terminology; inspected the primary sources below and narrowly compared L018/L233, the complete L501 proof, weighted-Green and signed-rectangle failures, and the completed square-variable transport assessment. No matching signed boundary-to-line budget was located; this is not a novelty claim.
SOURCE_EVIDENCE: Csordas arXiv:1309.0055v2 (21 February 2014), (2.11)--(2.13), printed pp.4--5; Sondow--Dumitrescu arXiv:1005.1104v1 (6 May 2010), Theorem 1/Corollary 1 and their proofs, pp.2--4; DLMF 25.2.1, 5.15.1 and 1.10(i); Planat Preprints.org 202606.1957 v1 (26 June 2026), Definitions 1--3, Proposition 2, Theorem 3/Proposition 9, Sections 9.2--10.4 and Appendix C.1--C.3. Precise links and applicability limits follow.
COMPARISON: Ordinary modulus-square curvature is zero-safe and differs from L501's log-modulus Laplacian pairing. The known identity does not bound inward transport of curvature. Boundary series and horizontal modulus monotonicity do not supply the missing signed remainder. The newly inspected paired-tail source uses a spatial theta variable and leaves global positivity conditional; it is no Re(s)=2 boundary-budget theorem.
GAP: No independent signed forcing/remainder inequality uniform at unbounded t reaches L233. Higher signs remain independent. A generic Taylor remainder with an uncontrolled interior derivative is not a new mechanism.
REASON: New theorem-level scope evidence parks the proposed boundary-jet implementation, without a global ban on normal curvature. A distinct, finite-block source cancellation claim is nominated for a separate approval and audit; no mathematical derivation, manuscript endorsement or new lemma is made here.
SCOPE: Completed literature review only. The Re(s)=2 boundary-jet route is parked unless a specified independent signed remainder estimate is supplied; EXPLORE does not approve an unspecified transport calculation.
LITERATURE_REASON: The invocation-start target changed the derivative and boundary interface; essential coverage and complete local overlap comparison were missing.

## Main gap and discriminating target

The main gap is actual-Xi all-degree positivity. The intermediate target
was a signed normal-curvature remainder sufficient for L233's first sign
at every sufficiently large real |t|. Its downstream use would be one
initial sign, with higher signs and the all-degree passage still open.
Continue only with an independently bounded signed remainder; park a
boundary-only argument with uncontrolled interior curvature, division at
zeros, RH-equivalent positivity, or a repeated majorant/count estimate.
The source comparison meets that park test, not a mathematical no-go test.

## Known identity and boundary scope

G. Csordas, *Fourier transforms of positive definite kernels and the
Riemann xi-Function*, [arXiv:1309.0055v2](https://arxiv.org/pdf/1309.0055v2#page=4),
(2.11)--(2.13), printed pp.4--5, gives, for a nonzero real entire f,

    (1/2) partial_y^2 |f(x+iy)|^2
       = |f'(x+iy)|^2 - Re(conj(f(x+iy)) f''(x+iy)).

This has no quotient or zero exclusion. For f=Xi, L018 gives
xi(1/2+a+it)=Xi(t-ia); conjugation permits y=a in the modulus.
At a=0 the right side is precisely L233's Xi'^2-Xi Xi''.
This is applicability of a cited identity, not a new curvature lemma.
The source's global complex inequality is a Laguerre--Polya criterion,
not an available positivity input. Its real-axis first sign alone is
weaker. No sign follows merely from naming normal curvature.
The v1 passage was located first; the v2 statement was then checked.

J. Sondow and C. Dumitrescu, *A monotonicity property of Riemann's xi
function and a reformulation of the Riemann Hypothesis*,
[arXiv:1005.1104v1](https://arxiv.org/pdf/1005.1104v1), Theorem 1 and
Corollary 1, pp.2--4: horizontal modulus monotonicity holds in a zero-free
open right half-plane; extension to every sigma>1/2 is equivalent to RH.
The complete proof uses the zero-free location and the Hadamard
exponential normalization. At sigma=2 its hypothesis is unconditional;
it gives monotonicity there, not a normal-curvature budget across the
critical strip. No zero-free interior half-plane is inferred.
The guessed v2 URL returned 404; v1 was accessible. This is not a blocker.

[NIST DLMF 25.2.1](https://dlmf.nist.gov/25.2.E1) states the Dirichlet
series only for Re(s)>1; [5.15.1](https://dlmf.nist.gov/5.15.E1)
states the trigamma series away from its nonpositive-integer poles.
Together with L018's completion these identify ordinary boundary-jet
inputs at s=2+it. Differentiated Dirichlet series would require local
uniform convergence, and Gamma derivatives their corresponding product
rules; neither is a signed inward remainder theorem.
[DLMF 1.10(i)](https://dlmf.nist.gov/1.10.i) gives analytic Taylor
expansion on a disk, not a favorable signed truncation error.
No finite jet bound, specialized derivative estimate or new transport
identity has been derived in this literature turn.

## Local duplication and failure comparison

Read the complete L501 proof. Its test is a compactly supported
Laplacian pairing of log|xi|; both curvatures cancel every harmonic
completion/prime-log main term. Its surviving covariance bound loses
L^(31/32+c) against a requested fixed saving L^(-c), c>0. This is
contrast, not a modulus-square premise or a universal obstruction.
The exact identities and estimate remain canonical in L501; its audit
qualification remains unchanged. See also
`ATTEMPTS/2026-10-30-weighted-green-harmonic-replacement-stop.md`.

The signed-rectangle first-mode stop leaves side-gap flux uncontrolled;
see `ATTEMPTS/2026-10-30-signed-rectangle-first-mode-norm-closure.md`.
It is a Fourier-detector boundary problem, not actual-xi boundary data.
The earlier endpoint boundary-curvature test concerns saddle sectors
and is not this target. The completed
`2026-10-31-square-variable-transport-residual-scope.md` covers fixed
x=a^2-b^2 forcing, not normal variation. Its conclusions are reused;
no unchanged characteristic integration is repeated. L233's positive
comparison kernel is not actual theta. L018/L233 fix the actual target;
L501 and these failures supply comparisons, not signs.

## New lead and bounded continuation

M. Planat, *Curvature Transition Layers and Paired-Tail Positivity for
the Riemann Xi-Function*,
[Preprints.org 202606.1957 v1](https://www.preprints.org/manuscript/202606.1957),
26 June 2026. Read Definitions 1--3, Proposition 2, Theorem 3 and its
full proof/Proposition 9, Sections 9.2--10.4, and Appendix C.1--C.3.
Its transverse variable b belongs to M(a,b)=Phi(a+b)Phi(a-b).
Theorem 9 retains finite certification, pre-crest positivity and crest
uniqueness assumptions. Appendix C restricts its derivative bounds to
a fixed compact strip and invokes Proposition 9 at each integration.
Thus no all-height normal budget or y-to-zero uniformity is imported.
The first two cancellation steps provide a distinct audit target, not
an established actual-Xi input. Later appendices/certificates and the
parent-paper growth bridge remain unaudited and are not required for
that finite-block test.

The separate nomination is
`2026-10-31-paired-tail-endpoint-cancellation-audit.md`.
It must receive approval before mathematics. A creative actual-Xi test
is not justified until its load-bearing cancellation is audited and a
signed remainder with the required uniformity is specified. This is an
essential audit blocker, not a reason to repeat source searches or
completed L473/L528 audits. Mathlib coverage of the full proposed normal
budget is unchecked; no source theorem has been installed in lemmas/,
and no DAG or PROOF.md change is warranted.
