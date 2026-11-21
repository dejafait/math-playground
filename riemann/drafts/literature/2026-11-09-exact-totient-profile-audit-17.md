# Exact totient-profile asymptotic — audit source coverage

TARGET: Independently audit L931's uniform exact totient-profile limit, including the approximate eigenvector, both full metrics and the combined endpoint errors.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step18 reused step16's exact-profile discovery, row-sum comparison and combined-operator coverage; checked the scoped step17 history/stop and L931 against L930's exact definitions and step15 audit. Followed both primary citations to their statements and essential proof cases; no repeat broad discovery or matching-result novelty claim.
SOURCE_EVIDENCE: Reinspected Tao 254A Notes1 Section2 Proposition12/Theorem13 equations20,22–24 and proofs; Moree–Saad Eddin–Sedunova–Suzuki MPIM18-66 Section2 ConditionTheta1 p4, Section3 Lemmas1–2 and complete proof pp5–6, including beta=-1 and both tail ranges. Reused L737/step261 and L930/step15 carrying L928/step8 for the unchanged finite/moment interface.
COMPARISON: The scalar imports have the required real-cutoff and harmonic-case scope; they do not state L931's finite propagation or coupled full-metric limit. Step16's stronger-source comparisons remain adequate. SPECIALIZE authorizes an independent REPRODUCTION audit of the existing applicability argument and local proof, not a source import of the final asymptotic.
GAP: L931 remains mathematically unaudited: growing-dimension errors, transpose endpoint, both complete energies and normalization need independent checking. Operator contraction, joint projection, signed realization and actual-Xi positivity remain separate gaps.
REASON: Separate source/scope approval is complete for exactly TARGET; no essential external source is missing. Perform the conceptual audit next, importing the named scalar results and checking only their specialization and the existing local argument. No mathematical audit or new derivation was performed in this literature turn.
LITERATURE_REASON: The newly nominated audit had REVIEW_REQUIRED status; this step resolves that separate scope gate using ready discovery coverage and primary hypothesis checks, without repeating the profile attempt.
SCOPE: Fixed w, phase, N=floor(T^(1/5)), T<=X<=2T, v_d=phi(d)^(-1/2), both exact H metrics and exact V only. No vector optimization, new length, L925/L929 theorem, stronger moment result or cross-notebook input.

## Invocation-start nomination (preserved; approval status superseded below)

The main gap is L030–L032/C032a. The intermediate audit concerns
whether this one profile is rigorously excluded as a saturation
witness; that would inform joint-projection work without proving
contraction of the whole operator. L931 and its scoped attempt record
contain the new evidence. The earlier termwise and parameter-norm
stops remain separate. The next turn should reuse
2026-11-09-exact-totient-profile-cross-test-15.md and
2026-11-09-logarithmic-gcd-row-sum-review.md, not reopen completed
discovery unless a specific source hypothesis is found missing.

Essential review points are the general-totient lemma at beta=-1,
sigma=1/2,kappa=0; uniformity over every row cutoff N/d>=1 in
the imported first-Mertens estimate; the bounded prime-power correction;
propagation of (A-log(N)I)v through the nonnormal finite exponential;
the transpose in W_+; the averaged kappa/Jordan error; the lower endpoint
atom in partial summation; both full energy logarithmic terms; and all
regular-zeta, weight and exact Hardy-phase errors before normalization.
The error must be uniform in X and the growing length. Check the floor
in N and the strict rational threshold; the result requires no numerical
certificate or script. Matching Mathlib coverage is unknown.

Accept the scalar exclusion only if every O(L) numerator/energy error
and the resulting O(1/L) normalized error follows with one uniform
constant. Otherwise identify and repair the precise defect or withdraw
the scalar conclusion while preserving the attempt. A pass neither
establishes an operator norm upper bound nor pays signed Xi transfer.
No fixed gap should be inferred from a single Rayleigh pairing.

This is a newly nominated target with REVIEW_REQUIRED status, not a
second mathematical attempt, completed literature review or approval.
No independent signed input presently justifies describing this unsigned
specialization as a central creative Xi mechanism; the specific new
asymptotic first needs its conceptual audit.

## Completed source and scope review — 9 November 2026, step18

The exact TARGET is now source-covered for one conceptual audit.
Reused the completed discovery in
`2026-11-09-exact-totient-profile-cross-test-15.md`, the row-sum
assessment and `2026-11-09-joint-combined-operator-coverage-11.md`.
Read L931 to identify its claimed inputs and audit obligations; compared
L930's definitions (3)–(5), bound (10) and step15 audit scope. The
step17 history and scoped saturation stop contain the existing result,
explicitly pending review. No duplicate audit was found in these records;
this is a narrow check, not an archive-wide absence assertion. Previous
Schur and parameter-norm stops remain separate. No cross-notebook input
or new zero-free region is involved.

### Primary hypothesis check

Tao, *254A, Notes 1: Elementary multiplicative number theory*,
23 November 2014, [Section2, Theorem13](https://terrytao.wordpress.com/2014/11/23/254a-notes-1-elementary-multiplicative-number-theory/),
equation (22), supplies the first-Mertens estimate for every real
x>=1. Read the theorem and its proof through (24), Proposition12's
proof and the prime-power comparison. There is no height, growing-row
parameter or RH hypothesis. This covers the scalar input L931 invokes
at its row cutoffs; its totient-denominator correction remains a local
audit obligation. Import the theorem rather than reprove Mertens.

Moree–Saad Eddin–Sedunova–Suzuki, *Jordan totient quotients*,
[MPIM18-66 (2018)](https://archive.mpim-bonn.mpg.de/3557/1/preprint_2018_66.pdf),
printed pp4–6 (PDF pages8–10 counting from one): reinspected the
squarefree-supported definition, ConditionTheta1, Lemmas1–2 and the
complete Lemma2 proof. Its harmonic branch uses sigma<1 and requires
no ConditionsTheta2/Theta3. This matches the already assessed real
parameter choice in L931 Section1. The audit must check that choice
and its constants; no moving-complex-exponent theorem is imported.
The source's stronger fixed-index statements do not supply the coupled
limit. Step16's comparisons with uniform Selberg–Delange and mollifier
profiles remain applicable; no new indispensable source was identified.

### Audit boundary and decision test

The genuinely local issues are still those in the nomination above.
Check L931's (4)–(23) against the imported real-variable estimates and
the audited finite interface, with every constant independent of N,d,X.
In particular the nonnormal exponential estimate must be the existing
operator bound, the endpoint must retain transpose, and both full H
forms must retain their logarithmic cross terms and kappa correction.
Check the lower atom in Abel summation, all exact time/phase factors,
the floor and the rational sine threshold. These are future audit
instructions, not claims that the calculations have passed.

Accept only if the numerator and each energy have the claimed O(L)
errors uniformly in X, yielding the stated O(1/L) normalized error and
a common eventual threshold. Otherwise isolate the precise failure and
repair or withdraw the affected scalar conclusion while preserving its
record. No grid, optimization, new length, new moment theorem or full
operator upper bound belongs to this audit. Its downstream use is only
to validate or reject this particular saturation-witness exclusion.

Mathlib matching coverage remains unknown; no declaration was checked.
L931 retains the canonical proof and citations. This literature-only
step modifies no lemma, mathematical script, DAG or PROOF overview.
Outcome EXPLORATION records completed scope approval, not new mathematics
or a passed proof audit. The exact Next action stays unchanged and
defaults to mathematics; no additional source turn is justified absent
a specific newly exposed missing hypothesis. No independent signed-Xi
input has been identified to justify a central creative target before
this essential audit.
