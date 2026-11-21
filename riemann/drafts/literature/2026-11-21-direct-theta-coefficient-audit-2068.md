# Four-coefficient certificate — source approval2069

TARGET: Critically audit C530a's certified c0,c2,c4,c6 bounds and replay certificate2068, checking both tails, the global fourth-derivative estimate and outward Decimal arithmetic.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed direct-coefficient review2066 and source recovery2067, with their exact-statement, duplicate and failure checks; this nomination concerns verification of that same four-integral specialization, not a changed coefficient family or novelty search.
SOURCE_EVIDENCE: Romik arXiv:1902.06330v3 (1.7)/(3.3), https://arxiv.org/html/1902.06330v3 ; DLMF (3.5.6)-(3.5.8), https://dlmf.nist.gov/3.5.ii ; (8.2.2)/(8.4.8)/(8.4.11), https://dlmf.nist.gov/8.2.E2 , https://dlmf.nist.gov/8.4.E8 , https://dlmf.nist.gov/8.4.E11 ; Decimal exp/context/neighbor contracts, https://docs.python.org/3/library/decimal.html . Actual prior primary reads and applicability are retained in 2026-11-21-direct-theta-coefficient-calculation-2066.md and its completed review.
COMPARISON: The imported coefficient, Simpson and gamma identities cover the analytic inputs. The new local certificate must be checked for correct specialization and implementation; no source supplies its numerical endpoints, tail constants or runtime verification.
GAP: C530a and its 2068 script/certificate have internal checks but no independent audit; exact positive tails, complete derivative estimates, arithmetic endpoints and trust assumptions must survive replay before downstream use.
REASON: Separate source approval2069 permits the unchanged finite audit next turn, using completed primary coverage2066/2067; it neither verifies C530a nor adds mathematical evidence.
LITERATURE_REASON: The supervisor requires separate approval of the newly saved audit nomination2068; reuse completed primary coverage2066/2067 without further browsing or execution of the audit.
SCOPE: Audit only j=0,1,2,3 with X=16,N=4,m=2^18,60 digits and the saved exact formulas. No discriminant, root count, higher-degree sweep or new coefficient calculation method is covered.

Essential local input: C530a, including its full proof and qualifications;
`scripts/pollaczek/direct_theta_coefficients_2068.py` and complete relevant
fields of `scripts/pollaczek/direct-theta-coefficients-2068.json`.
L530 is downstream motivation only and need not be loaded for this audit.
No cross-notebook result. Matching Mathlib coverage remains unchecked.

Check theta-tail positivity and both sum/integral majorants, Leibniz
coefficients and full-interval C4 bounds, exact Simpson normalization,
Machin endpoints and constant comparisons, all Decimal contexts and
flags, exact node construction, transcendental enclosure rules and
signed final errors. Replay with the same work caps, retaining complete
failure evidence if any check fails. Accept only four positive finite
intervals of width <=2^-40 with explicit backend trust; agreement with
uncertified floating-point values is insufficient.

Remaining independent gaps: initial hyperbolicity, collisions and
multiplicities, all-degree signs and Xi transfer. A successful audit
does not close them or establish novelty beyond the checked sources.
No actual-theta invariant has yet been identified that justifies a
creative all-degree attempt. The finite input may make the separately
unapproved degree-six discriminator concrete after audit.

## Separate source-gate review2069 — 2026-11-21

Read the completed comparison2066 and direct-source recovery2067,
then C530a in full to compare its stated inputs with that coverage.
Reused their exact-statement searches and duplicate checks for L768/L821;
read stop2065's centered-series obstruction. No new external search or
primary-source reread was necessary: the target, normalization, finite
method and arithmetic assumptions have not changed. Unread Petras and
Gaussian-quadrature leads remain unnecessary for this Simpson audit.

The imported inputs match the audit scope as follows:

| Primary input already inspected | Applicability to be verified in the audit |
| --- | --- |
| Romik v3 (1.7), (3.3) | Exactly the actual omega and c_(2j), j=0,1,2,3, with 4sqrt(2) normalization; no atomic/tilted substitution. |
| DLMF (3.5.6)-(3.5.8) | Finite real C^4 integrand, even positive panel count, full-interval derivative bound and exact normalization. |
| DLMF 8.2.2, 8.4.8, 8.4.11 | Positive real lower endpoints and integer polynomial-exponential majorant integrals; identities alone do not prove tail comparisons. |
| Decimal exp, contexts, neighbors, signals | Correctly rounded half-even exp plus outward neighbors, directed basic operations, exact sqrt endpoint comparisons, actual runtime and flags. |

C530a's positivity, two explicit tail bounds, Leibniz constants, Machin
argument, interval implementation and numerical widths are local proof
obligations. This source approval does not check those claims or the
saved JSON. Their verification is precisely the unchanged next target;
no new source-dependent method is needed and no source imports the
certificate's endpoints. Correct CPython/libmpdec remains trusted even
after replay. Mathlib matching remains unchecked, not asserted absent.

Decision remains SPECIALIZE, now separately approved for a later
REPRODUCTION audit. Record this mandatory gate completion as STALLED:
it repeats adequate coverage and contributes no new mathematical or
literature finding. No lemma/script was changed or executed. Keep the
saved acceptance test and all independent gaps above. On audit failure,
preserve the specific failure and withhold downstream use; source
approval is not mathematical acceptance. No creative mechanism is
justified merely by four finite coefficients.
