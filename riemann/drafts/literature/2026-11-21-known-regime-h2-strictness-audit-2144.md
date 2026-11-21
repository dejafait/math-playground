# Known-regime H2 strictness — ready scope for a separate audit

TARGET: Audit the known-result specialization that L874's H2(1/16) is strictly positive definite, using the published real-zero cutoff and complete reciprocal-zero support.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step2144's Poisson-contact review discovered overlap with the already-assessed unconditional real-zero regime; reused the low-time H2 comparison and reopened the primary cutoff, normalization, deformed product and Hankel statements/proofs. This changed target is outside the Poisson-square mechanism; no strictness derivation was performed.
SOURCE_EVIDENCE: Platt-Trudgian, Bull.London Math.Soc.53(2021),792-797, arXiv:2004.09765v1 Section3.4 Corollary2 and supporting paragraph; Polymath, Res.Math.Sci.6(2019),31, arXiv:1904.12438v2 (3)-(4), transition paragraph and Theorem1.1; Choi arXiv:2611.04359v1 (5)-(10), Lemma3.4 with proof, Theorem4.1 with real-zero/product/Gram/distinct-support branches, (19) and following Hankel formulas; local L488(11), L019/L058/L874 and L024's named Hadamard input.
COMPARISON: The published real-zero regime covers the chosen slice in L488's normalization; the checked source product and Hankel formulas provide known mathematical coverage. Exact local coefficient indexing and strictness of H2 at coalesced Taylor nodes require an applicability audit. Distinct-node Loewner strictness cannot simply be passed through a limit.
GAP: Check the exact normalized deformed product and infinite distinct support, match L874's S_k and H2, and decide strict positivity with all convergence/multiplicity qualifications. No result below the known cutoff, numerical lower eigenvalue bound or contact-flux sign is supplied.
REASON: Resolve whether the recent fixed-slice contact target is empty by an independently checkable known-result application. The missing work is specialization/critical checking, not a creative mechanism or a new real-rootedness theorem.
SCOPE: Exactly the TARGET at lambda=1/16 for the actual L019/L058 family; strict H2 contact exclusion only. No parameter extension below1/20, new point-process formula, auxiliary atomic-law identification or RH inference.
LITERATURE_REASON: The completed review exposed a known-regime overlap; exact strict-contact applicability differs from the failed Poisson square and the previous low-time interval calculation.

## Inspected coverage and qualifications

The completed source comparison is
`2026-11-21-poisson-contact-covariance-nomination-2143.md`, step2144.
It records the primary ranges and queries. This ready scope was written
in a literature-only turn and receives separate supervisor approval
before research. No proof is claimed in this assessment.

[Platt-Trudgian](https://arxiv.org/html/2004.09765v1), Section3.4
Corollary2, supplies Lambda<=0.2. Its supporting paragraph uses the
proved finite-height verification and Polymath's conditional table;
cite the published result rather than replay its computation.
[Polymath](https://arxiv.org/html/1904.12438v2), (3)-(4) and the
following transition paragraph, fixes H_t and the all-real-zero
criterion. L488(11) already justifies F(lambda,z)=8H_(4lambda)(2z).
The fixed slice lies inside that assessed regime; no new zero-free
estimate or analytic envelope is proposed.

[Choi v1](https://arxiv.org/html/2611.04359v1) is an unreviewed
preprint, not independent validation. Its (5)-(10) have
K_source=K_local/4 and a=lambda; normalization removes the factor.
Lemma3.4's entire-growth argument, genus-zero product in the squared
coordinate, reciprocal-square summability, infinite-distinct-zero
argument using Riemann-Lebesgue and local derivative convergence were
read in full. Theorem4.1's last paragraph explicitly removes RH in
the known regime. Equation(19) and the two subsequent Hankel forms
identify the relevant logarithmic coefficients. Read convergence
and multiplicity qualifications. Strictness for distinct-node divided
differences is supporting context, not the strict Taylor-Hankel claim.

The later audit must check the classical Hadamard factorization and
Riemann-Lebesgue applications against L058's family and the published
real-zero input. L024 supplies the canonical undeformed Hadamard
discussion; it is not automatically a deformed-family theorem.
Reproducing the necessary applicability and strictness difference is
justified to avoid importing an unreviewed preprint wholesale. Do not
reprove the published cutoff, Hadamard theorem or general moment theory.

## Bounded discriminator and downstream use

Essential local inputs: L019,L058,L488,L874; L024 for the named
factorization reference/method only. The claim is strict positivity
of exactly H2=(S_(i+j+2))_(0<=i,j<=2) in L874's normalization.
No H3 premise, actual contact, zero simplicity or identification of
C874b's auxiliary atoms with the full zero measure is assumed.

Require exact strict positivity for every nonzero real c, not a
numerical eigenvalue preview or just H2>=0. Check the distinct support
needed for strictness, convergence of coefficient sums and exclusion
of hidden exponential factors. If an essential claim fails, save the
precise reason and do not report exclusion. Success would retire the
fixed-slice contact premise as a research target, with no advance
beyond known mathematics or extension below the cutoff.

Prior score, node-mass and Poisson-square stops remain in scope. The
low-time H2 calculation covered a lower band and is not being rerun.
Initialization, arbitrary lower positive lambda, all-degree mixed
positivity and lambda=0 remain unresolved. Full matching/supporting
Mathlib coverage is unchecked. A creative lower-time mechanism still
needs its own concrete idea and literature comparison.
