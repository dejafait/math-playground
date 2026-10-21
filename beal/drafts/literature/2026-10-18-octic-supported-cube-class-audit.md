# L098 support and norm specialization — audit coverage approved

TARGET: Critically audit L098's finite cube-class containment, fixed support {3,5,11} and both norm scales for the full L095 domains.
CHECKED: 2026-10-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the bounded exact-system and standard-terminology search in drafts/literature/2026-10-18-octic-number-field-cube-descent.md and the ready support assessment; compared the full L098 proof with that scope, L095 domains, audited L097 and ATTEMPTS/043–044; no changed mathematical target requires renewed discovery.
SOURCE_EVIDENCE: Reopened Mourao, arXiv:1010.2360v5 (15 May 2012), https://arxiv.org/pdf/1010.2360v5, Proposition 2.3 and Sections 2.1–2.3, printed pp.2–4, including every support-proof case; reopened Cremona–Lingham, https://johncremona.github.io/papers/egros.pdf, Section 2, printed p.3, definition, unnumbered m-Kummer exact sequence and finiteness paragraph.
COMPARISON: These sources cover the ideal-support method, norm-class framework and finite supported Kummer group; they do not directly prove the degree-eight fixed-pair specialization or its numerical scales. The audit must independently check those written differences, without importing projective degree-divisibility assumptions.
GAP: Coverage is adequate for the exact audit; correctness of L098's discriminant, local cases and both norms remains unverified until the separate mathematical audit. Representative enumeration and integer elimination remain outside this scope.
REASON: Approve a bounded independent audit using already assessed methods; no new theorem or dependent calculation is derived in this literature turn.
LITERATURE_REASON: The supervisor requires separate approval of the new critical-audit scope; reuse the existing comparison and inspect only the primary passages needed to check that scope.
SCOPE: Exactly TARGET, including complete relevant certificate inspection and independent exact arithmetic if useful; excludes new descent mechanisms, class enumeration, survival tests, integer elimination and other algebra factors.

## Primary coverage and its boundary

M. Mourao, *Descent on superelliptic curves*, v5 cited above:
Proposition 2.3 and the standing assumption on printed p.2 put the
projective construction in degree divisible by the odd prime exponent.
Section 2.2, printed pp.3–4, treats integral coprime coordinates:
outside the leading coefficient the linear and complementary factors
are locally integral; an unsuitable valuation forces simultaneous
vanishing; coprimality makes the second coordinate invertible and
confines the prime to fixed complementary-factor support. Section 2.3
places these classes in a norm coset. This covers the method to audit,
not a direct projective theorem for degree eight. L098 explicitly
writes its own fixed-pair argument, so the audit needs no birational
replacement or new projective applicability theorem.

J. E. Cremona and M. P. Lingham, *Finding all elliptic curves with good
reduction outside a given set of primes*, Experimental Mathematics
16(3) (2007), 303–312; author manuscript Section 2, printed p.3:
K is any number field, S a finite set of maximal-ring finite primes,
and m>1. The unnumbered sequence retains S-units modulo mth powers
and S-class m-torsion; its following paragraph gives finiteness for
prime exponent. Taking m=3 requires no class-number-one or
roots-of-unity assumption. The elliptic-curve algorithm is not an
input. This provides the finiteness citation, not computed classes.

## Exact audit boundary and discriminating test

Main gap: integer elimination of both L095 systems, alongside other
unresolved factors and signatures. Intermediate target: independently
validate the necessary ambient cube-class reduction in L098. A valid
reduction could support later representative and fifth-power
compatibility work; it does not by itself exclude a solution.

Essential inputs: the full two L095 systems and domains; audited L097;
L098's complete proof; and the complete relevant evidence in
`scripts/rational-factor/octic-cube-support-certificate.json` and its
producer `scripts/rational-factor/check_octic_cube_support.py`.
The certificate was not replayed or verified in this literature turn.

The next mathematical audit must check the polynomial transcription,
resultant/discriminant leading-coefficient scales, both gcd(m,n)
arguments for n=C and n=5C, nonvanishing, local integrality outside
the leading coefficient, all unit and nonunit cases at primes outside
S (including primes dividing C), normalized maximal-ring valuations,
the Kummer input and both exact norm identities. Treat S above
{3,5,11} and classes [75], [15] as claims to check, not new source
conclusions established here. Retain S-class three-torsion.

Continue if every full-domain case and exact scale survives independent
checking; otherwise correct or narrow the canonical claim and exhibit
the escaping case. Unresolved assumptions remain the correctness of
this specialization, arithmetic of S-units and S-class three-torsion,
representatives, norm-fiber survival, simultaneous fifth-power
compatibility, integer lifting and coverage of other algebra factors.

Duplicate/failure comparison: L098 is the existing local result, not
a proposed additional lemma. ATTEMPTS/043 stops standalone eleven-adic
nonexistence and ATTEMPTS/044 stops rational polynomial factor descent;
neither supplies or forbids this number-field support audit. The
previous complete search found no matching classification of the two
systems; this is not a novelty claim. No unread lead is used as input.
Mathlib matching coverage remains not checked.

Coverage approval is not a critical-audit verdict. No lemma,
mathematical script, DAG or PROOF assembly changed in this turn.
