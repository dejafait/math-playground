# Approved audit coverage: the coefficient-1 integer-density obstruction

TARGET: Audit L736's incompatibility proof at b=3/4, checking the Axiom-A specialization including theta=0, formal multiplicities and endpoints, analytic error transform, common meromorphic continuation and integer zero order.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the step-254 coefficient/zero-multiplicity comparison and step-255 approved scope in 2026-11-04-beurling-integer-density-specialization.md; no changed coefficient, exponent, system or new discovery search.
SOURCE_EVIDENCE: https://arxiv.org/pdf/2110.11463v1 Definition 1.1, (1.2)–(1.5), endpoint footnote p. 2, Lemma 2.1 (2.2),(2.4) and proof pp. 4–5 (served PDF has v2 footer); https://arxiv.org/pdf/2202.01837v3 Section 1 (1)–(7) pp. 1–3 and Section 7 (52)–(54) pp. 17–18; https://dlmf.nist.gov/1.10 (i),(ii),(iv), especially https://dlmf.nist.gov/1.10.E9. These already assessed passages were consulted during the step-256 application.
COMPARISON: L736 combines the previously inspected standard continuation, Mellin and integer-order inputs for exactly the approved coefficient-1 target; the separate audit checks that specialization rather than a stronger theorem or a construction reproof.
GAP: L736 has a written incompatibility proof but no separate audit; endpoint normalization, compact analytic domination and identity of the continued functions require critical verification. Actual-prime upper-prefix norms and Xi signs remain open.
REASON: Reuse the established source scope for one bounded verification of the newly written proof; no source theorem or novelty claim beyond that comparison is proposed.
SCOPE: Only fixed b=3/4, error O(sqrt(x)log x), one locally finite free-semigroup system from audited L735, and hypothetical fixed kappa>0, 0<=theta<3/4; retain unit and all formal multiplicities. Separate literature-only coverage approval completed in step 257; the mathematical proof audit remains deferred. Neither approval nor proof audit was performed in step 256.

Essential local inputs are audited L735 and the written L736. The
integer-count estimate is assumed only for contradiction. The imported
continuation uses the source exponent eta=(theta+3/4)/2>0 and its
N-kappa(x-1) convention. Retain the requested-v1/v2-footer qualification
when citing the inspected source. No prime-discretization theorem is
an additional input to this audit beyond L735.

The discriminating checks are that the remainder transform is
holomorphic near b, both formulas belong to the same Euler-product
zeta, the meromorphic identity holds on their connected common domain,
and the residues computed by the transform and by Taylor order cannot
agree. In particular a step-function error need not have an absolutely
convergent Stieltjes derivative transform on that whole domain; check
the ordinary integral and its compact domination actually used.
Keep the unit contribution in the N transform, zero lower endpoint
in the psi transform, and every atom at equality. Check the m=0 case
as well as positive zero multiplicities.

Pass only if all these analytic and normalization checks hold for
every fixed pair kappa>0, 0<=theta<3/4. Repair a local mistake if
possible; otherwise preserve its precise effect and withdraw the
unsupported incompatibility. Do not test other coefficients or extend
the exponent boundary. No numerical certificate is called for.

The downstream use is limited: this verdict separates integer-count
regularity from L735's coarse same-system diagnostic. It cannot
exclude arbitrary off-line zeros or pay a prefix or sign bound.
L734/L639 and the coarse-kernel stop retain their scopes. No justified
new central sign mechanism has been identified, so the essential
analytic audit takes priority over a creative nomination here.
Matching Mathlib coverage remains unchecked.

Recommended mathematical routing after separate coverage approval:
proof_audit/conceptual_audit, deep_research/xhigh. The common-domain
and logarithmic-derivative inference warrants analytic scrutiny;
this is not a candidate audit of a complete RH argument.

## Separate source-scope approval — step 257

LITERATURE_REASON: The supervisor requires separate approval of the newly prepared L736 audit assessment; inspect its essential source cases and reuse the established discovery comparison, without executing the audit.

Reopened the direct primary URLs in SOURCE_EVIDENCE on 2026-11-04.
For 2110.11463, inspected Definition 1.1, the endpoint footnote,
and Lemma 2.1's statement and complete proof (printed pp. 4–5),
including its continuation argument and remainder integration by parts.
The requested-v1 URL again serves the 29-page text with a v2 footer.
The positive source exponent and N-kappa(x-1) convention are retained;
the source does not itself approve L736's theta=0 application.

For 2202.01837v3, inspected Section 1's formal-semigroup conventions,
Axiom A, Euler product and continuation, and Section 7's Mellin
paragraph through (52)–(54), printed pp. 17–18. The rational product
there belongs to that construction, not to L735. For DLMF 1.10,
checked Taylor order, analytic-continuation uniqueness and (1.10.9)'s
contour and multiplicity hypotheses. The meromorphic identity step
and holomorphic parameter integral still require checking in L736;
these references are supporting inputs, not a full matching theorem.

The duplicate/failure comparison reuses the step-254 coefficient-scope
assessment and step-255 specialization approval, together with L735's
statement, L736's written proof and
`ATTEMPTS/2026-11-04-self-generated-coarse-kernel-discrimination-stop.md`.
That coarse stop does not decide the added N hypothesis. No new
search, source theorem, stronger scope or novelty conclusion is claimed.
No essential unread source remains for this bounded audit. Matching
Mathlib coverage remains unchecked.

Coverage is approved as SPECIALIZE for the unchanged TARGET. This is
STALLED as mathematics: it approves verification, not the proof's
compatibility verdict. No lemma, mathematical script, DAG or argument
overview is changed. Retain all endpoint, compact-domination,
common-zeta and integer-order checks above; a later audit must accept,
repair or identify the precise failure. No other coefficient, exponent
boundary, ordinary-prime transfer or Xi conclusion is authorized.
