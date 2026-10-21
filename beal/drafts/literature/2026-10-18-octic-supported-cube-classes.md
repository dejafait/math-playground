# Fixed primitive-pair octic cube-class support — proposed specialization

TARGET: Prove a finite necessary cube-class containment for both L095 systems, certifying fixed exceptional prime support and both scaled norm constraints over Q[X]/(H(X,1)).
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed number-field source comparison in drafts/literature/2026-10-18-octic-number-field-cube-descent.md; the exact two systems, nonmonic coefficient and fixed-pair scope are unchanged.
SOURCE_EVIDENCE: Mourao, https://arxiv.org/pdf/1010.2360v5 (15 May 2012), Proposition 2.3 and Sections 2.1–2.3, printed pp.2–4, complete support proof previously inspected; Cremona–Lingham, https://johncremona.github.io/papers/egros.pdf, Section 2, printed p.3, full multiplicative Kummer sequence previously inspected; both direct URLs reopened successfully on 2026-10-18.
COMPARISON: Reproduce the known local ideal-support method for fixed primitive integer pairs; import finite K(S,3) structure by citation, retaining S-units and S-class three-torsion; do not import the projective Selmer construction with its degree-divisibility assumption.
GAP: Certify nonmonic local integrality, a fixed support independent of C, every prime-divisor case and both exact norm scales; the target-specific containment is unproved.
REASON: The inspected primary proof supplies the method, while degree eight and system-II scaling require a written specialization; no new descent principle or integer-emptiness theorem is sought.
SCOPE: Exactly TARGET, using audited L095 and L097, the cited ideal-support and Kummer-group methods, exact polynomial/resultant arithmetic if needed, and basic maximal-ring valuation theory; excludes enumerating a class group, claiming a Selmer list, projective-curve equivalence, integer elimination or other algebra factors.

The main gap is global integer elimination of both L095 systems, with
other algebra factors and residual signatures independent and unresolved.
The intermediate target is a finite ambient set of necessary field
cube classes, including their actual norm cosets. This could support a
later local/global class compatibility test while retaining C's
fifth-power relation. Neither finite containment nor its norm condition
is an integer exclusion.

Use L095's exact H and domains and audited L097's irreducibility. Set
h=H(X,1), K=Q[X]/(h), and let theta be the residue of X. The field
elements to examine are m-theta*C in I and m-theta*(5C) in II; verify
nonvanishing rather than admitting a zero multiplicative class. A
candidate fixed support is the maximal-ring primes over divisors of
5*1215*Disc(h), to be certified in the attempt. No numerical
discriminant, minimal support or maximal-order basis is supplied here.
Treat the polynomial discriminant as a sufficient support device only,
without equating it to a field discriminant. Handle theta's denominators
locally outside the leading coefficient; any proposed integral model
must be justified before use.

The printed proof in the first cited source uses a curve of degree
divisible by q. This attempt must separately check its local factor
argument on fixed primitive integer pairs of degree eight, without
claiming the paper's projective descent theorem applies unchanged.
Retain n=C or 5C, the right-hand factors 1 and 5^11, positivity,
gcd(m,u)=1, gcd(m,55)=1 and gcd(C,15)=1. Primes dividing C, including
eleven, must not be omitted or used to make the support depend on a
solution. At exceptional primes retain unrestricted class components
unless a separate restriction is proved. Use the maximal integer ring
for ideals; a power order is not presumed maximal.

Continue if every admissible original tuple gives a nonzero class in
one certified finite K(S,3) with the correct respective norm constraint.
The cited exact sequence, including Cl(O_(K,S))[3], supplies the
abstract finiteness input; do not assume an ideal cube is principal or
that its generator is a unit times an element cube. Stop or explicitly
narrow the result if any support or scaling case escapes. A complete
representative list, class/unit arithmetic, class survival and integer
lifting remain independent later tasks.

This ready continuation retains its original mathematical scope. Direct
primary-source URLs were added in the 2026-10-18 recovery review; it
awaits the supervisor's separate next-turn gate approval. No specialized proof was derived in
the literature turn that prepared it. Mathlib matching coverage is not
checked; any later canonical lemma must state that qualification.

## Direct-source recovery review (2026-10-18)

The direct [Mourao v5 PDF](https://arxiv.org/pdf/1010.2360v5)
was reopened: Proposition 2.3 and the standing assumption immediately
after it explicitly impose q dividing n. Sections 2.2–2.3 identify
finite supported power classes and a weighted norm coset. These remain
method coverage only for the fixed-pair octic target, as explained above.
The previously inspected complete support proof is reused rather than
claimed as a new theorem comparison.

The direct [Cremona–Lingham author PDF](https://johncremona.github.io/papers/egros.pdf)
was reopened at Section 2, printed p.3. Its unnumbered m-Kummer exact
sequence retains both S-units modulo powers and S-class m-torsion; the
following paragraph explicitly states finiteness for prime m. No
principality or class-number assumption has been added. Full source
identification and earlier search/overlap evidence remain in
`drafts/literature/2026-10-18-octic-number-field-cube-descent.md`.

LITERATURE_REASON: Supervisor recovery requires direct source URLs in
the ready assessment; this repair verifies the existing primary links
and does not expand the research target or repeat mathematical discovery.
No specialized containment, norm scaling, new lemma or calculation was
performed. ATTEMPTS/043–044 remain stops for their original mechanisms,
not for the distinct fixed-pair number-field support test.
