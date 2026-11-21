# Modulated-kernel critical-minimum test — separate continuation

TARGET: Test whether phi(u)=exp(-u^2-10^(-8)u^4)(1+cos(10u)/100) is a strictly log-concave admissible kernel whose full Fourier transform F has F(t)>0 and F''(t)>0 throughout [6,7], with F'(6)<0<F'(7), thereby testing the generic critical-point sign inference.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: The exact-extrema/constrained-sign search in 2026-11-04-xi-critical-point-sign-scope.md was supplemented with modulated-Gaussian, admissible-kernel/local-minimum and stronger log-concave-counterexample queries; local checks included L022/L049/L050/L251/L560/L607 and the prior associated-kernel screens. No matching certificate for this exact constrained obstruction was located; no novelty inference follows.
SOURCE_EVIDENCE: Csordas arXiv:1309.0055v2 (21 February 2014), Definition 1.2, Theorems 3.5/3.7 and Example 3.12, pp.2/6-9; NIST DLMF v1.2.8 (15 September 2026), 1.14.1-2 and Table 1.14.1 Gaussian row, read with normalization and a>0; Schubr public edition 2 (27 October 2026), Theorems 1-2 and Theorem 2 proof, pp.2-4, as a limited overlap comparison only. Primary links and reading limits below.
COMPARISON: Existing nonreal-zero and negative-first-sign examples do not state the required nonzero stationary minimum under all the proposed shape hypotheses. The standard Gaussian transform supplies only a reference calculation; quartic damping, global shape and the full compact-interval derivative margins are the unproved difference. No actual-Xi consequence is imported.
GAP: Verify or refute all shape/decay hypotheses and the four interval/endpoint inequalities for this one fixed kernel. No critical point, Fourier identity for the damped kernel, or quantitative perturbation bound is established in this literature turn.
REASON: One bounded obstruction test can determine whether the critical-point restriction rescues a generic admissible/log-concave inference after the actual-theta source screen found no independent residual mechanism. It is distinct from repeating nonreal-zero existence or an unconstrained first-sign test.
SCOPE: Only this fixed real-even kernel and F(t)=integral_R phi(u)exp(itu)du on the stated interval; no theta modularity, arithmetic coefficients, order-one transform, zero strip, actual-Xi realization or sign transfer is claimed. Newly prepared assessment; separate next-turn approval is required before mathematics.

## Relevance and bounded decision

Main gap: unconditional actual-Xi mixed positivity. The current source
review leaves its theta-specific critical-value sign unresolved. This
test addresses only the generic implementation that would try to use
positivity, strict log-concavity, full admissibility and F'(t)=0.
An obstruction would force a later sign argument to use further actual
theta information. A successful shape check alone would not be useful
evidence for the actual-Xi sign; every stated Fourier margin is needed.

Proposed intermediate threshold: certify the fixed interval and endpoint
inequalities in TARGET, with rigorous positive lower bounds and a
negative upper bound for F'(6), together with every admissibility
condition. If any bound fails, record the failed bound; do not change
the kernel parameters or widen the family within the same attempt.
Finite floating-point sampling is not a certificate. If it succeeds,
stop this generic inference route; do not convert it into an RH claim.
If the test is inconclusive, preserve the missing margin and reassess
before repetition. Neither outcome pays the actual-theta residual,
degenerate stationary points, other real centers or higher signs.

## Known inputs and comparison

[Csordas v2](https://arxiv.org/pdf/1309.0055v2), Definition 1.2, fixes
the admissible class. Its Example 3.12 lacks the super-Gaussian decay
condition and has a favorable first sign; it does not settle this test.
Use those statements by citation; do not reprove the general
associated-kernel theorem. L050's full superexponential log-concave
example proves nonreal zeros, without the requested adverse stationary
value. L607's negative sign does not assert stationarity. L251 is
masking evidence, not a positive-kernel input. These comparisons justify
the changed discriminator; they are not mathematical dependencies of
the proposed new kernel calculation.

[NIST DLMF, Table 1.14.1](https://dlmf.nist.gov/1.14#T1), with
[1.14.1](https://dlmf.nist.gov/1.14.E1), gives the Gaussian row for a>0
under the normalized full-line convention. [1.14.2](https://dlmf.nist.gov/1.14.E2)
is its absolute-integral bound. Cite the Gaussian transform and justify
the normalization and elementary frequency shifts locally. The proposed
quartic-damped kernel is not that table entry. An explicit derivative
perturbation estimate, if used, must be proved with integrable moments;
no standard theorem for an arbitrary oscillatory remainder is assumed.
The proof need not use mathematical scripts.

Scott Schubr, [*Admissible kernel lifts with positive endpoint forms
and nonreal Fourier zeros*, edition 2](https://research.luminaryoddities.com/admissible-kernel-lifts-positive-endpoint-forms-nonreal-fourier-zeros/v/2),
public 27 October 2026, manuscript dated 24 October, Theorem 1 and
Theorem 2/proof, printed pp.2-4, were inspected in the linked PDF.
They address finite-atomic hyperbolic-cosh lifts, shape and nonreal
zeros, not the fixed interval certificate in TARGET. The remaining
proofs were not read or imported. A later PDF lookup failed following
a domain redirect; this supplementary lead is not an essential input
and does not block the independent Gaussian test. The archive labels
the manuscript unrefereed and AI-assisted. No independent validation
of its main theorem is claimed.

Additional queries actually used were `"admissible kernel" "local
minimum"`, `"Fourier" "log-concave" "local minimum" kernel`,
`"logarithmically concave" "kernel" "Laguerre" counterexample Gaussian`,
`"Fourier" "exp(-" "cos(10" log concave`, and `"log-concave"
"Fourier transform" "counterexample" critical minima`. The original
screen's queries and other primary statements are retained in
[the completed actual-Xi assessment](2026-11-04-xi-critical-point-sign-scope.md).
This is a bounded search, not an exhaustive survey.

No essential lemma ID is assumed by the proposed standalone calculation;
L018-L020 specify the actual function against which scope is compared,
and L047/L048/L050/L251/L607 are contrast evidence only. Full matching
Mathlib coverage is unchecked; no absence is claimed. No new result,
lemma or mathematical script was produced here. This is an ordinary
bounded calculation nomination, not a justified creative attack on the
central theta-specific gap.
