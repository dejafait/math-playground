# Ordered (3,5,11) — rational-factor literature comparison

TARGET: Determine whether L093's coefficient-one algebra can have a rational direct factor for a positive primitive solution.
CHECKED: 2026-10-18
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused signature coverage and histories 311, 313 and 315, with targeted searches in 308, 309 and 312; bounded rational/linear-factor, reducibility and Belyi searches inspected Putz's global cases, the author's GFE/3511.m, and Pacetti–Villagra Torcomian Theorems A–C; no matching coefficient-one rational-factor exclusion was located.
SOURCE_EVIDENCE: Putz (2024), DOI 10.5463/thesis.832, Section 5.2 p.165, Remark 5.13 p.167 and Propositions 5.24–5.27 pp.170–173; CPutz/etale-algebra-family master GFE/3511.m; Pacetti–Villagra Torcomian, On the generalized Fermat equation of signature (5,p,3), author-hosted 42-page PDF, Theorems A–C pp.4–5, all inspected on 2026-10-18.
COMPARISON: Putz's terminal exclusions have different coefficient hypotheses, and the newer modular theorems explicitly except p=11; the inspected local-algebra code supplies no global rational-root classification. L093/L094 remain necessary restrictions only. Branch-specific rational-root arithmetic is uncovered by the inspected results, without any novelty claim.
GAP: Whether a positive primitive solution's entire coefficient-one algebra has a Q factor remains undetermined; no exact denominator/gcd reduction preserving both power equations or complete rational-point computation is available.
REASON: Essential coverage for a bounded elementary rational-root attempt is adequate; use the known cover directly, without special-coefficient exclusions or full Hunter enumeration. Newly changed readiness requires separate supervisor approval before research.
LITERATURE_REASON: The prior assessment explicitly lacked rational-factor-specific comparison; this review fills that essential changed branch scope, reusing signature discovery and audited algebra inputs.
SCOPE: Exactly TARGET from L093/L094 and the original positive primitive equation; elementary reduced-fraction, rational-root, gcd and valuation methods retaining simultaneous powers; no full field enumeration, new modular machinery or other signature.

Essential inputs: L093, L094 and the original positive primitive equation
A^3+B^5=C^11. The candidate entry point is the rational-root equation
phi(t)=B^5/C^11 with t in Q. Its applicability and any resulting
Diophantine reduction are for the next assessment to check; none is
derived here. A local degree-one factor is not evidence for a global
rational factor. Retain all complementary components.

Main gap: global algebra elimination and integer power lifting. This
intermediate target isolates one reducible branch without requiring
a complete field enumeration. A rigorous exclusion would remove that
branch only; other reducible types and the irreducible case remain.

The original gate (superseded by the completed comparison below) was literature-only: search the exact rational-factor
statement and known Belyi-cover/Diophantine treatments, reuse the prior
signature assessment, and inspect relevant primary hypotheses. Continue
to mathematics only with an applicable exclusion or a precisely scoped,
independently testable reduction. If the available argument merely
assumes irreducibility or uses the nonunit-coefficient exclusions, reject
that argument and record the uncovered difference. No calculation,
new lemma or full enumeration was approved by that placeholder.

## Completed comparison — sources inspected

Reuse `2026-10-18-ordered-three-five-eleven-coverage.md` for signature
discovery, the conditional explicit-abc alternative and target conventions.
L093's full proof/application audit and L094's relevant coefficient and
maximal-algebra passages were inspected. Histories 311, 313 and 315
separate completed imports/audits from this new branch. Targeted notebook
searches located no prior solution of it. Older affine and fixed-tuple
duality stops concern different mechanisms and remain intact.

P. H. C. Putz, *Enumeration of local and global étale algebras applied to
generalized Fermat equations*, VU Amsterdam thesis (2024), version of
record, DOI [10.5463/thesis.832](https://doi.org/10.5463/thesis.832),
[primary PDF](https://research.vu.nl/ws/portalfiles/portal/367784086/Thesis_CasperPutz.pdf):
read Section 5.2 p.165, Remark 5.13 p.167 and the relevant global proof
cases pp.170–173 (PDF indices 176–179). Proposition 5.27 excludes (10,1)
only for coefficients in C: its proof uses Table 5.21's discriminants
and Table 5.17's special three-adic data. Proposition 5.26 also uses
special local tables. Neither applies at (1,1,1). Proposition 5.24 is
stated for C and permits rational-factor patterns; it is a partition
filter, not a rational-root exclusion. The exact cover remains available
in Section 5.2; the coefficient-one enumeration warning remains intact.
No coefficient-one terminal theorem was found in these inspected cases.

Read the author's [GFE/3511.m](https://github.com/CPutz/etale-algebra-family/blob/master/GFE/3511.m)
on master, retrieved 2026-10-18, also through its
[raw endpoint](https://raw.githubusercontent.com/CPutz/etale-algebra-family/master/GFE/3511.m).
Its active EtaleAlgebras3511, EtaleAlgebras3511Coeff and
EtaleAlgebras3511CoeffRamification routines compute local families or
ramification, including the reciprocal infinity chart. The inspected
file supplies no global rational-factor solver. No code was executed,
and no implementation correctness or computational theorem is imported.

A new primary lead was A. Pacetti and L. Villagra Torcomian,
*On the generalized Fermat equation of signature (5,p,3)*,
[author-hosted PDF](https://sweet.ua.pt/apacetti/papers/3rp.pdf), 42-page
version retrieved 2026-10-18; no version date is printed in its inspected
opening pages. Read pp.1–5, including all hypotheses of Theorems A–C.
They concern primitive signed triples in x^5+y^p+z^3=0. Both A and B
exclude sets containing 11 from their allowed primes. C retains A's
exception set and assumes large-image Conjecture 1 and p>C. None
supplies the required theorem at 11. No theorem is imported here, and
no modular proof or later conductor case is reproduced. The explicit
prime-hypothesis mismatch suffices for this comparison.

Putz cites S. R. Dahmen's 2008 Utrecht thesis p.24 for the map's
provenance. The [publication record](https://research-portal.uu.nl/en/publications/classical-and-modular-methods-applied-to-diophantine-equations/)
was read; its PDF links and legacy igitur endpoint failed, and the
[repository handle](https://dspace.library.uu.nl/handle/1874/29640)
returned 403. The relevant thesis page is an **unread lead**, not
theorem evidence. It is nonessential for this attempt: the exact map
is already available in Putz and justified in audited L093. Any use of
a further theorem from Dahmen requires its own assessment.

## Search scope and decision

Queries included `Putz "5, 3, 11" "rational"`,
`"generalized Fermat" "3,5,11" rational factor`,
`"generalized Fermat" "5, 3, 11" reducible`,
`"generalized Fermat" "3, 5, 11" "rational points"`,
`"Putz" "Fermat" "rational" "factor"`,
`"3t^2+t+1" "5" Fermat`, and
`"generalized Fermat" "linear factor" "11"`, plus spaced signature
and Dahmen/Belyi provenance variants. Unrelated signatures and Fermat
number-factorization hits were not evidence. This is bounded discovery,
not exhaustive coverage and not a novelty claim.

The strongest applicable inputs remain canonical L093/L094. This review
does not decide existence of a rational factor. It rejects shortcut
citations on exact hypotheses, while leaving arithmetic investigation
of the branch justified. Mathlib coverage of a matching exclusion is
**not checked**. No essential source for the scoped test is blocked.

## First mathematical test, not performed

After separate approval, make one bounded attempt at the unchanged
TARGET. Under the rational-factor hypothesis, use a reduced rational
root t=m/n with n>0 and gcd(m,n)=1, retaining the equations for both
s and 1−s. Determine actual cancellations and numerator/denominator
valuation conditions, including 3,5,11 and all coordinate-divisor cases.
Seek an explicit finite collection of power-twist cases or a rigorous
contradiction; neither a collection nor a contradiction is asserted here.
Standard rational-root and unique-factorization facts may be used by
name; the solution-specific arithmetic must be proved in research.
Reproof of the imported computational local propositions is unnecessary.

Continue only with a genuine restriction or independently testable
reduced problem retaining both original power conditions. A tautological
rational-root restatement or unbounded numerical search is insufficient.
If neither an exclusion nor a useful finite twist reduction emerges,
record the limitation and reassess under the shared exploration budget.
Any new curve-classification theorem or algorithm outside this scope
needs a separate review. Other reducible types, the irreducible case,
integer lifting and the other residual signatures remain independent
gaps. No abc, GRH, irreducibility, complete field list or height bound
is assumed. No mathematical result, lemma or script is produced here.
