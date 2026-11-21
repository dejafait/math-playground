# Nomination646: a neutral reference retaining the endpoint operator

TARGET: Assess an endpoint-preserving neutral middle reference at C999z tolerance 1/100 and a certified inverse-action bound for arbitrary complex L2 forcing.
CHECKED: 2026-11-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Separate literature-only647 reused553/555/637 and611/619 theorem-level searches; read C999k Sections1-2/audit6, C744z Section1, C744v Section3 and C999z Sections1/4-6; compared the exact600/603/635/640 stops. Reopened Teschl only for the missing bounded-perturbation and full-resolvent proof cases; no novelty inference or numerical search.
SOURCE_EVIDENCE: Teschl GSM99 author version12February2009 https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf Theorems6.4/proof p135,6.24/full proof p150,2.18/proof p77; reuse553/555 for Theorem2.13 pp71-72 and Behrndt et al.1403.5704v1 Proposition2.1 p4/Corollary3.5 p12, and642/644 for Teschl Section6.3 and the exact Li45/paper60 response identities. Detailed scope and direct links below.
COMPARISON: Standard bounded perturbation, closed-form representation and resolvent control cover a neutral reference and a posteriori full-L2 residual method. C999k's audited complete reference supplies a candidate coercivity bridge, not an automatic bound for B_trial. The local order/floor, restricted strong domain, effective singular action and converging full-forcing procedure still require a separate mathematical specialization.
GAP: No local B_trial order, positive floor, inverse comparison or complete inverse-error certificate is proved647. Future work must pay the complete residual, establish convergence in an appropriate domain, and state the certified-L2 input representation required for computation on arbitrary forcing; a finite matrix or merely qualitative convergence is insufficient.
REASON: Essential general coverage is now adequate for one bounded standard-method construction/obstruction attempt, subject to separate approval of the saved continuation. The source-scope gap is closed; the mathematical construction and its usefulness for the actual signed residual are unresolved.
LITERATURE_REASON: New hypotheses involve the neutral restriction of an unbounded logarithmic form, a positive reference floor and a complete inverse-action certificate; the ready endpoint-kernel audit covers none of these applications. Reuse existing form/inverse assessments first.

The main gap remains L030-L032/C032a actual-Xi positivity. In the current
three-cell route, C744z(4) retains the signed remote-plus-induced operator
but lacks its sign. A middle reference retaining the entire endpoint
singularity could improve control of the inverse appearing there. It
does not by itself sign that residual, control higher endpoints, pay
C744q/H2 or settle the original source/core/c_* and global gaps.

## Exact proposed target and bounded test

Fix a=log(3)/4 and delta=1/100. Let m and J be the smallest integers
given by C999z Section4's displayed tolerance rules at this delta.
Let U_par be the unitary map from the full cell to its two reflected
half-interval parity spaces, exactly as in C744v and C999z. Write
C_end for C999z's Carleman operator, to distinguish it from the
two-moment map C in C744z. Consider the candidate full-cell form

    B_trial = D + U_par^-1 diag(C_end/2+R_+;m,J,
                              C_end/2+R_-;m,J) U_par - delta I,

with form domain V, then restrict the form to V0=V intersect ker(C)
on H0=ker(C). This is a proposed construction, not a derived order or
coercivity statement. In particular its neutral inverse must not be
replaced by a projected unrestricted inverse. No values of m,J or new
matrix have been computed in646.

The source review should decide whether existing closed-form and
inverse-order results cover this exact construction and a practical
full-L2 residual certificate for its inverse on arbitrary complex
forcing in H0. Identify a covered procedure that can rigorously certify
a positive floor and control the complete inverse-action error, including
all omitted output modes and the Carleman action. An existence proof or
an uncontrolled finite inverse is insufficient. Retain any IEEE754/
Decimal and analytic qualifications if using C999k's audited lower
reference; do not silently substitute the unreplayed c_* computation.
No claim that B_trial improves or dominates C999k's R is preapproved.

Continue to one construction/obstruction attempt only if the essential
source hypotheses and full error procedure are covered. If exact
endpoint retention leaves no certifiable coercivity or no complete
inverse-error mechanism, identify that precise blocker and park this
construction. Missing source coverage permits only source work; no
new lemma, numerical tuning or mathematical script belongs in review.
This is a bounded new-reference question, not permission to resume the
unchanged598 additive repair or any old enclosure prescription.

## Reuse, contrasts and remaining assumptions

Reuse [ready642/comparison643](2026-11-12-response-endpoint-carleman-review-642.md)
and [audit approval644/645](2026-11-12-response-endpoint-critical-audit-review-644.md)
for the response input. For the changed form/inverse issues, first inspect
the relevant source evidence in the existing
[fixed-reference review553](2026-11-12-fixed-block-metric-test-553.md),
[its audit review555](2026-11-12-fixed-block-metric-audit-555.md), and
[neutral-shortening review637](2026-11-12-neutral-reference-shortening-review-637.md).
These are leads for comparison, not an asserted approval of the new
target. Retrieve primary proof cases only if the saved evidence omits
an essential hypothesis or effective-error step. Further browsing needs
a specific missing-source reason, not another general compactness search.

C999z Section6 and C744v Section3/audit534 are essential inputs for the
response and unitary normalization; C744z Sections1-3 supplies the
intended neutral domain and actual residual, with its original unresolved
core/c_* qualifications; C999k Sections1-2 supplies only its qualified
form-order precedent and lower reference. No cross-notebook input.
C999y Section4's fixed598 rank-two stop and C744z Sections8-9's fixed32
stop are contrasts: the proposal retains a noncompact operator instead
of a finite response prefix or an additive moment correction. The600/
603/635 failed sufficient allowances remain preserved. None is an
actual negative three-cell form or a global ban on changing references.

This is a REVIEW_REQUIRED nomination, not an assessment completed during
the audit. It grants no mathematical approval. The next turn is
literature_comparison/standard/high. A protected creative sign attempt
is not yet justified: there is still no concrete covered test paying
the actual remote-plus-induced coupling. The proposed form/inversion
bridge may be a standard specialization; classify it honestly after
source comparison instead of labeling it creative to satisfy routing.
Full matching Mathlib coverage remains unchecked.

## Completed source comparison647 — 12 November 2026

The nomination above is preserved as the question reviewed, not as an
already proved construction. This turn performs source comparison only.
No lemma, mathematical program, local floor, inverse identity or numerical
value of m,J is produced. The standard-method coverage is adequate;
the separate construction must establish every local application below.

### Imported results and precise scope

New narrow retrieval from [Teschl, GSM99, author version12February2009](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf):
read Theorem6.4/full proof p135 and its bounded-perturbation case;
Theorem6.24/full proof p150, including norm equivalence;
Theorem2.18/proof p77. These give selfadjointness on the old operator
domain for a symmetric bounded perturbation, closedness on the old form
domain for a bounded Hermitian perturbation, and inverse norm control
below a strict positive lower spectral bound. They provide no numerical
floor or computable residual norm automatically. Import these theorems;
reprove only the local applicability and effective scalar estimates.

Reuse553/555's inspected Theorem2.13/dense-domain convention/proof
pp71-72. Apply representation on H0 after checking density of V0 there,
not on the full L2 space with an unjustified dense-domain assertion.
Reuse611's complex projection and spectral-calculus coverage for domain
and convergence questions; a form core alone is not a strong operator
core. These are source-covered tools, not a proof of the new core claim.

Reuse553/555's [Behrndt–Hassi–de Snoo–Wietsma,
arXiv1403.5704v1](https://arxiv.org/pdf/1403.5704v1),
Sections2.1-2.3, Proposition2.1 p4, Theorem3.4's nonnegative sufficient
proof p11 and Corollary3.5 p12. The relation setting allows a non-dense
lifted form domain and reverses nonnegative form order under inversion.
Its hypotheses still require the right form-domain inclusion and actual
lower bound. It neither identifies a restricted inverse with a projected
unrestricted inverse nor validates any finite inverse.

Reuse642/644 and C999z audit646 for the exact response input and kernel
error. Teschl Section6.3's Hilbert-Schmidt estimate applies to the compact
remainder error only. It cannot be applied to the Carleman kernel.
C744v Section3 supplies the full bounded response and weighted Schur
bound already checked with both parities. No new response-source search
is needed while these identities and assumptions remain unchanged.

### Applicability comparison and covered procedure

C999z supplies a two-sided raw-L2 error for both selfadjoint parity
approximants. C744v supplies the unitary normalization, D and V.
C744z Section1 supplies the existing qualified neutral-domain setup.
Consequently bounded perturbation and restriction are the correct source
framework. The future proof must distinguish the full-cell operator from
the operator represented by its restriction to V0. It must check the
order direction on V0 and lift the restricted relation only when needed.

For a positive floor, use C999k Sections1-2 and audit6 as a specific
candidate bridge: its complete reference R has head floor .239999 and
complement floor greater than3.07, and its form comparison to D+S holds
on V0 because the moment penalty vanishes there. Compare those existing
certified allowances with the actual two-sided C999z approximation loss
at delta=1/100. This is an instruction for a future applicability proof;
no new inequality or floor for B_trial is asserted here. The fixed546
endpoint vector and .023083550 correction are not inputs to this general
floor comparison. Keep every analytic/arithmetic qualification attached
to R; do not substitute the unreplayed c_* computation or claim that the
new reference dominates R.

The covered inverse-error method is a posteriori certification on H0.
After proving a positive floor beta, choose an exact-neutral strong-domain
trial q and bound the COMPLETE residual f-B0 q in L2, where B0 is the
restricted represented operator. Theorem2.18 then supplies the standard
resolvent estimate to specialize to the inverse-action error. The later
proof must establish the error formula and all domain identifications;
the source theorem supplies neither the residual nor a finite solve.
It must also give a converging trial/residual procedure, for example by
proving the required strong-core property for exact-neutral cosine trials.
The recorded V0 form core alone does not establish that property.

A concrete full-output procedure to test is scalar integration of the
retained singular action with certified L2 error: approximate each smooth
trial by piecewise constants, use the existing Carleman Schur bound for
the input approximation error, and enclose the resulting logarithmic
primitive expressions on the entire half interval. The near-zero
logarithmic contribution needs an explicit integrable error bound; a
quadrature grid omitting that interval is not a certificate. Compute or
bound the finite-rank remainder action and D action as well, including
all output and arithmetic errors before taking the residual norm.
The scalar primitive, endpoint estimate, projection and convergence
checks are elementary specialization obligations for the next proof,
not estimates derived or approved as correct in this source review.
No Hilbert-Schmidt approximation of the singular operator is permitted.

For arbitrary complex L2 forcing the analytic estimate must hold without
smoothness or parity restrictions. An effective numerical instance needs
forcing data with certified L2 approximation errors (or an equivalent
certified residual-norm oracle). Include that input error in the full
residual allowance. No inspected theorem supplies a computable tail for
an unspecified abstract L2 element, a universal finite cutoff or a rate
independent of its supplied data. This is an essential effectivity
qualification, not permission to silently replace arbitrary forcing by
a fixed finite input family. If the desired claim excludes such input
data, record that obstruction rather than claiming an algorithm for it.

### Search reuse, stops and decision

The exact terminology and stronger-result searches for closed-form
inverse order, constrained inverse/shorting and full Galerkin residuals
are recorded in553/555/637 and611/619. Their primary statements were
read there; those searches are reused, not claimed as new retrieval.
The additional retrieval here was limited to Teschl's named theorem
locations needed for bounded perturbation and a whole-space residual.
No result in the inspected sources certifies this particular B_trial.
No novelty follows from that difference.

Compared the complete600/603/635/640 failure records. They respectively
stop an entrywise radius allowance, a preset head-action allowance, an
extra recentering comparison, and a rank-two repair of unchanged598.
They do not test a reference retaining the endpoint operator. Conversely
this reference cannot retroactively pay their missing estimates. The
fixed32 stop remains a finite-prefix contrast, not a negative actual
three-cell form. All these stops and unfinished work remain preserved.

DECISION SPECIALIZE: known tools cover one construction attempt. Pass
requires proved neutral form order, a certified positive floor and a
complete inverse-action error procedure for represented arbitrary complex
L2 forcing that can reach any prescribed positive error tolerance.
Park this construction if the floor cannot be certified under retained
contracts or the singular/full-output/convergence obligation remains
unpaid. Do not enlarge m,J, change delta or resume an old enclosure to
evade the fixed test. No S3 gain or superiority to R is required or claimed.

The main goal still lacks the sign of the remote-plus-induced coupling,
reference usefulness in that comparison, higher endpoints, C744q/H2,
source/core/c_* validation and global assembly. This is standard-method
REPRODUCTION scope. A central creative sign attempt still lacks a
specific covered mechanism that pays that coupling; no creative label is
justified merely by a changed reference. Full matching Mathlib coverage
for this construction and effective procedure is unchecked. General
theorems remain in the cited sources; any later local proof belongs in
a canonical lemma, not in this assessment.
