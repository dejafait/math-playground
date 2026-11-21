# Actual Mellin saddle-domain claim: nominated independent audit

TARGET: Audit paper23 Lemma2's saddle-image claim for |s|>=6000 and Re(s)>=-|s|/(8 log|s|), including u>=3 and pi/4-|h|>=1/(4u) for F(u+ih)=s; prove the stated domain and clearance or isolate a rigorous counterexample.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step508 compared the exact actual-factor construction with KPS and paper20, checked local step507 representation stops, and sought the missing supplement by exact-title/identifier searches. No prior local audit of the displayed saddle-domain claim was found; no novelty conclusion.
SOURCE_EVIDENCE: bramble_trace, paper23 v1, 18 October 2026, Section3 Lemma2, (10)–(11) and its contour/image outline; https://rstation.ai/problems/riemann_hypothesis/papers/23. Completed comparison: drafts/literature/2026-11-05-actual-xi-levy-certificate-comparison.md. Supplement derivations42/43/65 remain unread and are not accepted premises.
COMPARISON: The source already asserts the whole selected claim. The task is an independent audit of its explicitly defined elementary complex map, not a new saddle theorem, an inversion proof, or source-certificate replay. The statement and boundary cases are available without the supplement.
GAP: The source's saddle-image proof outline has not been independently verified; no global inversion, boundary containment, unique branch or uniform clearance is accepted from finite samples. Mellin remainder, evaluator and real-zero transfer remain separate gaps.
REASON: A bounded analytic premise of the actual construction is independently testable despite unavailable certificate data. Success supports one contour prerequisite; a rigorous failure changes the certificate route. Neither outcome resolves mixed positivity.
SCOPE: Only the stated saddle branch/image/clearance claim. No Mellin asymptotic, residual bound, Levy inversion, certificate regeneration or automatic real-zero inference. New assessment: separate approval required next turn before mathematics.

## Exact claim to audit

Use paper23's displayed map

    F(z)=z(pi exp(2z)-9/4).

On D={s: |s|>=6000, Re(s)>=-|s|/(8 log|s|)}, the source
claims a holomorphic choice x(s)=u+ih with F(x(s))=s, u>=3,
|h|<pi/4, and positive real part of A(s)=2F'(x(s))/x(s).
For the upper-half case it additionally states
pi/4-h>=1/(4u), with the lower-half case treated by conjugation.
Interpret holomorphy on an open neighborhood or the interior with
boundary continuation stated explicitly; D itself is closed.
Retain all source boundary cases: the real axis, the u=3 image,
the curved left boundary, critical points/branch uniqueness and
the conjugate half. This audit must prove the image coverage as
well as a pointwise inequality on an assumed branch. It must not
silently assume the branch whose existence it is meant to check.

The comparison turn did not derive this claim. Independent verification
of a source claim is justified because it is an explicit assumption
behind the proposed continuum certificate and its detailed proof is
not accessible. A finite grid cannot verify the domain claim. A
rigorous counterexample or identified failed boundary inequality may
stop the audit; an informal numerical miss is only a diagnostic.

## Purpose and stopping test

Main gap: actual-Xi all-degree mixed positivity. Intermediate target:
the actual Mellin construction's saddle-domain prerequisite. Plausible
downstream use: a verified theta-strip contour for a later quotient
estimate, eventually permitting assessment of a root-independent
Levy representation. Ordinary membership still needs an additional
sufficient sign mechanism, and no such bridge is asserted.

Continue if the global branch, image coverage, curvature and clearance
are rigorously established, or if a precise repair with the same usable
domain is source-covered. Stop this audit if there is a rigorous failure
on D or no usable branch proof within the one attempt. Preserve partial
reasoning and report a narrowed unresolved claim honestly; do not
repeat without a new input or refined mechanism. No numerical script
is required for this analytic audit.

Essential local inputs: L019/L021 identify the actual kernel/moments;
the saddle map itself and constants are source definitions. L795/L796
are relevance/stop context, not mathematical inputs to the saddle
claim. Unresolved assumptions: all remaining paper23 analytic and
evaluator claims, finite enclosure provenance, Levy integrability and
inversion, and any mixed-positivity bridge. L778/L791 software contracts
would apply only if their separate certified data are later reused;
none is needed now. No cross-notebook input. Full Mathlib coverage
unchecked. Classification for a later audit is REPRODUCTION.
