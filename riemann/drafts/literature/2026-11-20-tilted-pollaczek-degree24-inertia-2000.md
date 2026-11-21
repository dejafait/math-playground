# Tilted-Pollaczek degree24 diagnostic nomination

TARGET: Certify the Hermite-matrix inertia of Kuznetsov's Jensen-weighted tilted-Xi Pollaczek truncation at degree 24, testing whether its negative index is at most one.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused discovery2000/notes1601 and scoped Pollaczek stops; searched Hermite trace rank/signature/Coste, Kuznetsov Jensen-weighted degree24 zeros and certified Arb inertia. No exact degree24 certificate found; no novelty inference. drafts/literature/2026-11-20-tilted-pollaczek-inertia-source-review-2001.md
SOURCE_EVIDENCE: Kuznetsov2008 https://doi.org/10.4153/CMB-2008-055-0 definition p562/(2)-(4)p563/(13)-(14)p566/weights pp568-569; Coste2002 Section1.4.1 pp17-18 Theorem1.14/full proof and Section1.4.2 p19 Jacobi theorem; Plaumann2023 Theorem1.1/full multiplicity proof slides3-4; Arb2.23 and python-flint0.9 determinant/enclosure contracts inspected. Exact URLs/ranges in source-review2001; Nathanson1601 reused.
COMPARISON: Standard source formulas and Hermite/Jacobi theorems cover the finite algorithm, not degree24 signs. Negative index counts distinct conjugate pairs; nullity retains repeated-root information. Generic preservation stops do not settle this actual-family diagnostic; no uniform bound or novelty claim.
GAP: Evaluate actual degree24 coefficient and all leading Hermite-determinant enclosures. Prove degree/nonzero minors before applying Jacobi; otherwise report unresolved. Runtime availability, uniform index bound, weighted compact convergence and multiplicity/actual-Xi transfer remain unpaid.
REASON: Essential source coverage is complete for one finite reproduction by the specified determinant method; the changed ready assessment receives separate supervisor approval before calculation. No new mathematics or program was produced in review2001.
SCOPE: Only degree24, with source p_k(t)=P_k^(3/4)(t/2;pi/2), source coefficients denoted beta_k to avoid collision with C028b, and weights m_(24,k)=24!/((24-k)!24^k). Form T_24(t)=sum_(k=0)^24 m_(24,k)*beta_k*p_k(t). Retain all terms and all singular cases; assume no root reality or simplicity.

Require a full certificate of the inertia, degree and coefficient
enclosures. A floating root plot or unverified LDL output is insufficient.
If the chosen precision cannot separate a pivot, record an unresolved
enclosure rather than manufacture simplicity; a different certified
inertia method may be used after its source coverage is checked.

Continue the one-pair mechanism only if the certified negative index is
at most one. An index at least two stops that particular proposed bound.
Passing the finite test establishes no uniform result or RH. Even a
future uniform index bound would need independently justified compact
convergence, singular-root accounting and actual-Xi symmetry transfer.
C028b and C028f remain branch context, not premises identifying T_24
with the ordinary reciprocal Jensen family. No height estimate is
inferred from a distinct-root census. Full Mathlib coverage is unchecked.

## Source approval2001

See [complete primary-source comparison and certificate protocol](2026-11-20-tilted-pollaczek-inertia-source-review-2001.md).
The original REVIEW_REQUIRED nomination is resolved at the source level.
Scope and target are unchanged. Use source (13) through u_26 and (4),
all beta_0,...,beta_24 and all Jensen weights; no term may be dropped.
Use source recurrence (2) for the basis. The degree and simplicity are
outputs to certify, not hypotheses. No finite coefficient was evaluated.

The approved method encloses each leading Hermite determinant with
Arb and applies Coste p19's Jacobi theorem only after every determinant
has a certified nonzero sign. Full inertia/nullity and distinct-root
interpretation use Coste Theorem1.14 and Plaumann Theorem1.1, including
their repeated-root cases. A zero-containing enclosure remains unresolved;
no singular-case algorithm or unverified indefinite LDL routine is
approved. Default python3 lacks the required numerical packages; locate
or provision an authorized runtime before evaluation. This is an
operational qualification, not missing mathematical source coverage.

After separate approval, the finite evaluation is REPRODUCTION under
SPECIALIZE. Its purpose is a branch discriminator; no uniform mechanism
has yet justified a creative central proof attempt. No theorem is added
to the canonical lemma collection by this literature-only approval.
