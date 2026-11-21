# Proposed independent audit of the fixed boundary certificate

TARGET: Critically audit C919b's 2048-box normalized boundary certificate, including complete arithmetic enclosures, Polymath hypotheses, the zero-time limit and conjugation, without changing the fixed test.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step2150 exact-boundary searches, duplicate/failure comparison and implementation coverage; directly reopened primary Polymath v2 theorem, definitions and relevant error-proof cases, Decimal contracts and DLMF identities on 2026-11-21. Completed audit-specific source comparison below; no new numerical audit.
SOURCE_EVIDENCE: Inspected https://arxiv.org/html/1904.12438v2 Theorem1.3/Corollary1.4, (5)-(19),(23)-(25), Section6.3 (69)-(74), Proposition6.6(iv)-(vi) and proof from (77) through its conclusion; https://docs.python.org/3.15/library/decimal.html exp/ln, contexts, next_minus/next_plus and power caveat; DLMF4.2.2-5/4.6.1/4.14.3,8-9/4.19.1-2. Versions and obligations below.
COMPARISON: Sources adequately cover the unchanged audit method and analytic inputs; none certifies this implementation or its 2048 boxes. Audit the existing specialization, importing the source error theorem rather than reproving heat asymptotics; integrity checks alone do not establish inclusion.
GAP: Source gate is complete; independent scrutiny of implementation inclusion, all saved boxes/guards, constant cutoff, normalizer, uniform margin and endpoint inference remains pending. No changed mesh, precision, formula, census or head positivity is covered.
REASON: Approve one unchanged conceptual audit with accessible primary coverage; a successful local certificate still needs independent verification before downstream use. Reuse adequate literature thereafter.

The calculation is canonical in
`lemmas/C919b-fixed-normalized-vertical-boundary-certificate.md`.
Its complete evidence is `scripts/heat/fixed-boundary-2152.json`, with
script `scripts/heat/fixed_boundary_2152.py`. The 6150 saved-evidence
integrity checks in `scripts/heat/fixed-boundary-integrity-2152.json`
include all 116736 guard thresholds, but do not constitute an independent
audit. The original fixed budget passed with minimum normalized margin
>18367/100000. Preserve its bytes, including the hashes in the integrity
report, unless a discovered defect requires a separately documented repair.

Essential mathematical inputs are L019,L037,L058,L919. L037's real
arithmetic proof is not already a complex implementation certificate.
Review the full source formulas (including both complete error bounds),
the principal-log rotations and complete series tails, exact endpoint
coverage, constant N=3 and the nonzero normalizer. Pay the t=0 argument
by continuity of the normalized function; do not apply the source's
t>0 theorem at zero. Conjugation must cover the negative local height.
No RH, simplicity, continuous zero enumeration or all-real-zero premise
is permitted. Full matching Mathlib coverage remains unchecked.

Accept C919b only if the proof and complete relevant saved evidence
support the stated common bound under the documented Decimal contracts;
otherwise identify the exact failing operation or implication and quarantine
the affected boundary claim. An audit may reject an inference without
claiming an actual zero. Initial census, the rest of a region boundary,
radial-head accounting, real-head continuation, eigenvalue margin and
all-degree/global positivity remain independent gaps on either outcome.

At nomination this continuation was **not approved**. A separate
source/gate approval is required next turn before the conceptual audit.
The pending essential audit blocks nominating a new central creative
mechanism in this bounded step; known-method implementation is not
relabeled creative. Existing moment-box, Rayleigh and source stops remain.


## Step2153 separate source approval (21 November 2026)

LITERATURE_REASON: The audit nomination was REVIEW_REQUIRED; its
source-to-implementation scope needed separate approval. This review
closes that gate without repeating the calculation or its integrity run.
SCOPE: The exact TARGET only, with the original fixed budget and evidence
preserved. The next turn may audit existing proofs, code and complete
certificate evidence and document a verdict. It may not change the fixed
test or infer a census, head positivity or a global conclusion.

### Inspected primary inputs and scope

D. H. J. Polymath, *Effective approximation of heat flow evolution of
the Riemann xi function, and a new upper bound for the de Bruijn-Newman
constant*, Research in the Mathematical Sciences 6 (2019), article31,
[arXiv:1904.12438v2, 4 August2019](https://arxiv.org/html/1904.12438v2).
Reopened (5)-(19),(23)-(25), Section6.3 (69)-(74),
Proposition6.6(iv)-(vi), the relevant proof from (77) to its conclusion,
and the paragraph converting (vi) to (24). The theorem's region is
0<t<=1/2, 0<=Y<=1, x>=200; time zero is excluded. Formula (23)
bounds e_A+e_B; (24) bounds e_C,0, including its constant contribution.
Use actual gamma, s_* and kappa; the discrepancy already recorded
between (21) and Proposition6.6(ii) is outside the selected method.
The source's normalizer uses a specified holomorphic log M_0 on its
slit domain, not an arbitrary principal log of M_0. Its published
large-height numerical constants are not inputs here.

The [Python3.15.2 Decimal documentation](https://docs.python.org/3.15/library/decimal.html)
was directly reopened at exp, ln, next_minus, next_plus, Context,
rounding/signals and power. It specifies nearest half-even exp/ln and
adjacent representable neighbors; general C-module power is only almost
always correctly rounded. These contracts support review of endpoint
widening, not a verified implementation kernel. The saved run's actual
runtime/context, exact rational conversions, sign operations, integer
powers, exceptions and every outward operation remain audit obligations.
No undocumented complex Decimal contract may be assumed.

NIST DLMF version1.2.8, release15 September2026, inspected21 November:
[4.2.2-5](https://dlmf.nist.gov/4.2) for the principal branch/cut,
[4.6.1](https://dlmf.nist.gov/4.6.E1) for the complex log series,
[4.14.3,8-9](https://dlmf.nist.gov/4.14) for exponential/trigonometric
identities and periodicity, and
[4.19.1-2](https://dlmf.nist.gov/4.19) for sine/cosine series.
These are exact identities. They do not certify C919b's rotations,
series remainder estimates or implementation recurrences; those already
written claims are objects of the next audit, not new results here.

### Local comparison and bounded acceptance test

Read C919b's statement and existing inclusion/endpoint argument, L037's
complete real-arithmetic contract, L058's domination/entirety/conjugation
proof, and L919's normalization paragraph. L019's kernel identity remains
an essential exact input to trace during the audit. Only function names
and the implementation expression locations were inspected in the script;
no code-inclusion verdict or certificate verification was performed.
The saved 18367/100000 margin remains the calculation's unaudited claim.

Reuse the exact searches and duplicate/failure comparison in
`2026-11-21-h2-fixed-boundary-nonvanishing-review-2149.md` and the approved
calculation scope in `2026-11-21-h2-fixed-boundary-polymath-certificate-2150.md`.
The specific step2152 history confirms no independent audit was already
completed. Earlier moment-box, Rayleigh and expansion-only source stops
remain evidence against rerunning those observables; they do not block
checking this distinct successful vertical-boundary certificate. No
novelty claim follows from these searches. No unread external lead is
essential to this audit, and no essential source remains inaccessible.

The unchanged intermediate target can pay one finite-region boundary
input. It leaves initial census, the remaining boundary, rectangular to
radial-head accounting, real continuation, eigenvalue margin and the main
L030-L032/C032a all-degree actual-Xi positivity gap unresolved.
A new central creative mechanism is still unspecified; its discovery
priority does not justify skipping this essential audit or calling this
specialization creative.

Accept only after checking source expressions against code, every
arithmetic/series inclusion, all complete saved box/guard evidence,
cutoff constancy, a nonzero continuous normalizer, and the common positive
margin through time zero and conjugation. In particular a hard-coded
successful guard is no substitute for its analytic justification, and
integrity checks do not replace these checks. If any load-bearing
inclusion or implication fails, identify and quarantine the affected
claim; do not infer an actual zero or improve the grid/precision/cutoff.
No new estimate or proof is established in this literature-only step.

The SPECIALIZE assessment is now ready for the exact unchanged TARGET.
The next audit is REPRODUCTION of a known-method specialization, with
proof_audit/conceptual_audit routing. A source citation alone cannot
replace checking a newly written computer-assisted certificate. Full
matching Mathlib coverage remains unchecked; no absence claim is made.
