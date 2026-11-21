# C032e conceptual-audit scope — approved1269

TARGET: Review source coverage for a conceptual audit of C032e's full-theta strip continuation and compact-profile Fourier injectivity, including the exact scope of the ansatz obstruction.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused review1266's exact-statement, stronger-transform and obstruction searches; read C032e in full, its four direct local inputs, history1268 and the exact compact-transport stop1268. No new discovery search or broader ansatz is needed for this audit.
SOURCE_EVIDENCE: Reused review1266's inspected primary comparisons; directly rechecked NIST DLMF live Section 1.14(i), definition (1), continuity bound (2), convolution (5) and Uniqueness on 2026-11-17. The definition permits complex functions and uniqueness requires continuous absolutely integrable inputs and equality at every real frequency.
COMPARISON: Classical uniqueness matches the two intended final applications to k and H if their stated hypotheses are verified. It does not establish full-theta strip continuation or half-line injectivity by citation alone; C032e's explicit reduction is the object of the separate audit.
GAP: Source coverage is sufficient for the bounded conceptual audit below; correctness of the reduction and the compact-only obstruction remains unaudited. No completed-profile, approximation, parameter-uniform or actual-Xi positivity conclusion is covered.
REASON: Approve checking the existing specialization, without rederiving a uniqueness theorem or widening the target. The proof's analytic obligations are explicit and independently testable; no essential unread theorem was identified in its dependency inventory.
SCOPE: Conceptual audit of C032e as written, fixed omega=1/4 and z=i, full Psi=K(./2)/2, arbitrary complex compact smooth f; one-sigma strengthening may be audited, but no extension beyond compact exact profiles is approved.
COVERED_TARGET: Audit C032e's full-theta strip continuation, compact-profile convolution and Fourier-injectivity reduction at omega=1/4 and z=i, retaining arbitrary complex f and the compact exact scope.
LITERATURE_REASON: The target changed from solving the fixed equation to approving an audit of the newly available proof; the narrow DLMF reread checks the precise complex-input and transform-convention requirements, without repeating discovery searches.

## Completed source-scope review — step1269

This is a literature-only coverage decision. C032e was read to identify
its obligations, not critically verified in this turn. No lemma,
mathematical script, DAG row or PROOF argument is changed. The outcome
is EXPLORATION: the audit is ready, with no new mathematical result or
novelty claim. Mathlib coverage remains unknown as recorded in C032e;
the supporting L016 references are not a full formalization.

### Precise source match and retained obligations

[NIST DLMF, Section 1.14(i)](https://dlmf.nist.gov/1.14.i), live text
checked 17 November 2026: definition (1) explicitly includes complex
functions. The Uniqueness paragraph states equality everywhere for
continuous, absolutely integrable inputs whose transforms agree at
all real frequencies. No nonnegative-input, transform-integrability
or derivative hypothesis is added there; the adjacent inversion
paragraph has different hypotheses and is not the theorem imported.
Definition (1) uses the positive exponential and a normalization
factor. The audit must account for C032e's negative exponent and
unnormalized convention by frequency reversal and the nonzero scalar
factor; these are convention checks, not a new uniqueness theorem.
The subsection's convolution statement under (5) assumes two L1
inputs and uses its own normalized convolution. C032e instead writes
its unnormalized convolution identity explicitly, so its absolute
double-integral estimate and Fubini justification must be audited.

The standard named identity theorem for holomorphic functions is the
other decisive import: its domain must be connected and open, and
the zero set must accumulate inside it. C032e uses it for evenness
on S, zero continuation on T, and the compact transform on C. The
proof also uses the standard Weierstrass locally uniform convergence
theorem, dominated differentiation, and Tonelli/Fubini. Their domain,
domination and absolute-integrability hypotheses are explicit proof
obligations below, not facts inferred from Fourier uniqueness.
No reproof of any of these standard theorems is called for.

The source-to-proof inventory is:

| Passage in C032e | Input and exact audit obligation |
| --- | --- |
| (5)-(7) | L016 supplies real positive-x modularity; inspect compact strip majorants, termwise differentiation and the modular cancellation before holomorphic evenness. L016 does not itself assert a complex strip theorem. |
| (8)-(9) | L019 supplies the positive-side kernel bound; check rescaling and two-sided decay after the proposed extension. L020 supplies Xi's cosine normalization; (9) is a consistency passage, not the injectivity mechanism. |
| (1)-(2), (10) | L018 supplies exterior-strip nonvanishing for the denominator in c; L019 supplies the positive denominator for compact division. Check finite c and nonzero k without assuming signs of c or f. |
| (11)-(12) | Check support inside a fixed bounded interval, real translations remaining in T, compact parameter domination and the exact branch-difference convention. No holomorphy of f is available or needed by the claimed argument. |
| (13)-(15) | Check continuous L1 inputs, the full absolute double integral, nonzero kernel transform, an open frequency interval and compact-transform entireness before applying DLMF uniqueness and the identity theorem. |

This inventory approves an audit, not any of the checks themselves.
Review1266's Liehr sampled-Laplace and Ransford lower-support results
are comparisons only; neither is used by C032e, so neither needs a new
source read. The prior source C.1 feature comparison supplies motivation
for the fixed equation, not a theorem that completed evaluation
profiles are compact. No claim against the whole source construction
is approved. Existing duplicate/failure evidence from review1266 and
the precise stop1268 is retained; the new audit is not a retry of the
stopped construction or another discovery search.

### Discriminator and routing

Accept the scoped obstruction only if every listed analytic step
survives the independent audit. Otherwise name the first concrete
failed hypothesis or inference and repair or downgrade C032e. A proof
failure does not construct a nonzero profile. If accepted, retain the
compact exact route stop; this gives no quantitative defect bound and
no statement about noncompact completion or approximation.

Essential continuation inputs are C032e, L016,L018-L020 and the cited
DLMF uniqueness statement, with the original review1266 available for
source-convention context. The main gap remains actual-Xi all-degree
positivity L030-L032/C032a; signing, realization and initialization
are unresolved. The audit's plausible use is a trustworthy decision
about this restricted route before investing in a different bridge.
It cannot supply a central positivity mechanism. Independent positive
representation/bridge data are absent, so no justified creative target
is nominated to meet scheduling preferences. Next is exactly the
COVERED_TARGET above, proof_audit/conceptual_audit, deep_research/xhigh.

## Original nomination1268 — retained limitations

The main gap remains L030-L032/C032a actual-Xi all-degree positivity.
The completed1268 result is an informative negative for one restricted
ansatz, not a new central sign mechanism. Its proof and citations are
in `lemmas/C032e-compact-exact-branch-compatibility-obstruction.md`.
Do not turn this nomination into an approval of broader completed
profile classes or a claim about the source's entire construction.

Essential local inputs are L016,L018,L019,L020 and the new C032e proof.
C032d and the Green-mass source-limit1266 are contrasts only. The
original review1266 is unchanged and remains the assessment for the
completed step. No new theorem is imported by this nomination.

The planned conceptual audit must check local normal convergence on
|Im v|<pi/4, the modular cancellation at v=0, the scale Psi=K(./2)/2,
two-sided real L1 tails after exponential/affine weighting, compact
division by Psi, holomorphic parameter integration, Fubini, nonzero
kernel transform, and entireness of the compact transform. It must
retain arbitrary complex f and distinguish the full theta density
from corrected finite-mode kernels. The continuation test is acceptance
or a concrete correction/failed hypothesis at one of these steps.

The downstream use is to decide whether the compact exact route stop
is reliable before routing elsewhere. Completion, quantitative
approximation, source-core identification, norm matching, other
evaluation points, uniform parameters, actual-Xi signs, graph
realization and initialization remain open. A failed proof must be
repaired or downgraded; it is not evidence of a nonzero solution.

Following the separate scope approval above, the intended audit is
proof_audit/conceptual_audit, deep_research/xhigh. No justified creative
positivity mechanism follows from this injectivity argument; independent
positive representation and bridge data are still missing. Full
Mathlib coverage remains unchecked. No cross-notebook input is proposed.
