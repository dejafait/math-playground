# Entire marked octic algebra — factorization source approval

TARGET: Determine and certify the complete Q-irreducible factorization of L114's octic G, retaining every factor for supported-class arithmetic.
CHECKED: 2026-10-22
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Targeted local searches of L113–L114, marked-model/support assessments, history/395–399 and ATTEMPTS/050–051 found no complete factor certificate; exact coefficient-string web searches found no matching instance result. Reused the elementary-method assessment for the different L095 octic; no novelty inference is made.
SOURCE_EVIDENCE: Milne, Fields and Galois Theory v5.10 (September 2022), 1.8, Propositions 1.13–1.14, Remarks 1.17–1.18, Proposition 4.20/Corollaries 4.21–4.22 and Exercise 4-8; Lenstra–Lenstra–Lovasz, CWI IW 195/82 (1982), algorithm (3.5) and Theorem (3.6), printed pp.25–28, read with relevant cases.
COMPARISON: Exact rational factorization and irreducibility certification are covered by standard algorithms and criteria; these sources do not supply this octic's factorization. Bruin–Stoll's already assessed support containment needs all simple factors and supplies no field assumption or class/unit computation.
GAP: Execute and verify the input-specific exact product, scalar/content, multiplicities and irreducibility evidence for every retained rational factor; no arithmetic was executed in this source turn.
REASON: Essential certification coverage is now available for the unchanged target; a later mathematical turn may specialize it without reproving general algorithms or claiming a new factorization method.
LITERATURE_REASON: Startup REVIEW_REQUIRED concerns the new entire-octic factorization scope, beyond the ready support audit; this completes its essential method comparison and does not repeat support browsing.
SCOPE: Exactly TARGET for audited L113–L114's unchanged squarefree G over Q, using exact rational/integer polynomial arithmetic, Gauss, finite-field certificates, modular degree constraints or the cited complete rational-factorization algorithms; excludes class/unit groups, maximal-order certification, local images and rational-point completeness.

## Gap, inputs and downstream use

The main target remains Beal nonexistence for every residual signature.
On this route the immediate gap is rational-point control on the marked
curve, followed independently by degree-nine distinguished-root recovery,
remaining-factor compatibility and the L095 integer power conditions.
The intermediate target is the complete rational simple-factor description
of A=Q[t]/(G), where L114 fixes

    G=3025t^8−31460t^6+76230t^4−39204t^2+2673.

Its downstream use is to identify precisely the fields whose maximal-ring
supported square-class arithmetic is needed. Essential inputs are audited
L113's actual marked model and L114's squarefreeness, unchanged polynomial,
support {2,3,5,11}, real place and two distinct rational infinity points.
Retain L109 marking and L110–L111 transport when interpreting later points.
No cross-notebook input, field assumption or maximal-order assumption is used.

## Inspected methods and limits

J. S. Milne, *Fields and Galois Theory*, v5.10, September 2022,
[author PDF](https://www.jmilne.org/math/CourseNotes/FT.pdf):
1.8 pp.10–11 supplies Euclidean/Bezout certificates; 1.13–1.14 p.12
supply integral factors and monic-factor integrality. Remark 1.17 p.13
normalizes to monic integral input and bounds all candidate factor
coefficients for finite exact search. Remark 1.18 p.14 requires a prime
avoiding the leading coefficient for reduction to preserve factor degrees;
it also explains why absence of irreducible reductions proves nothing.
Statements and relevant proofs were read. Proposition 4.20 and Corollaries
4.21–4.22 pp.53–54 give finite-field Frobenius and factor facts.
Exercise 4-8 p.60 states the Rabin test: for monic degree n input over F_p,
require X^(p^n)=X modulo it and gcd with X^(p^(n/r))−X equal to one for
every prime divisor r of n. This is an exercise statement, with supporting
finite-field proofs inspected, not a read proof in Rabin's original paper.
These are imported criteria; no general reproof is needed.

A. K. Lenstra, H. W. Lenstra Jr. and L. Lovasz, *Factoring polynomials
with rational coefficients*, CWI IW 195/82 (1982),
[institutional primary preprint](https://ir.cwi.nl/pub/9304/9304D.pdf),
algorithm (3.5), printed pp.25–26, Theorem (3.6) and proof pp.26–28
(PDF indices 28–31). The theorem factors any positive-degree primitive
integer polynomial completely. The inspected cases use a prime avoiding
the resultant, retain every residue factor, recover rational factors and
iterate until a constant remains; the repeated-factor case uses gcd with
the derivative. This is a complete fallback to single-prime criteria,
not a claim that an arbitrary software output implements a verified trace.
The published article is Math. Ann. 261 (1982), 515–534,
[DOI](https://doi.org/10.1007/BF01457454); the cited numbering/pages here
refer specifically to the inspected CWI preprint.

Rabin, *Probabilistic Algorithms in Finite Fields*, SIAM J. Comput.
9 (1980), 273–280, [publisher](https://doi.org/10.1137/0209024),
was located bibliographically, but its full theorem/proof was not read.
No conclusion depends on access to that original: the explicit test above
is cited through Milne. The inaccessible Leiden LLL URL and a Waterloo
course PDF whose later fetch returned 404 are nonessential leads;
neither is used to bridge a missing hypothesis.

## Duplicates, failures and bounded discovery

The local search was confined to the active notebook. Relevant queries
included `Rabin|Kronecker|Lenstra|275t|2860|marked.octic.*factor`,
and the exact marked coefficient strings. External queries included
`"275" "2860" "6930" "3564" polynomial`,
`"275t" "2860" octic`, Rabin's finite-field criterion and LLL rational
factorization. The bounded searches located general methods, not this
instance's complete answer. No novelty is inferred from a failed search.

Reuse `drafts/literature/2026-10-18-rational-octic-factor-descent.md`
for its inspected elementary methods only. Its L095 polynomial and
cube-descent objective are different: L097's Eisenstein conclusion is
not evidence about G. Reuse the marked support and critical-audit
assessments for Bruin–Stoll's role, without another source review.
ATTEMPTS/050's bounded rank-detector failure and ATTEMPTS/051's positive
elliptic rank stop do not obstruct factorization. Preserve unfinished
L108 and L113's recorded failures. No larger rank search is authorized.
The exact target/source conventions remain those in
`foundations/01-target-and-scope.md`; no change to Beal's statement is used.

## Certificate contract and decision test

In the next mathematical invocation, candidate factors may be discovered
by exact software. The proof must separately record their rational
scalar/content and coefficient arrays, recover all of G by exact
multiplication, and certify irreducibility of every nonconstant factor.
Linear factors require no extra irreducibility calculation. For a modular
certificate, prove the prime and leading-coefficient conditions, normalize
the reduction, retain full modular powers and Euclidean/Bezout evidence.
If modular degree constraints from several primes are used, justify their
application to every possible rational factor degree, with all residue
factors and multiplicities retained. A reducible reduction is not itself
a rational factorization, and irreducibility of a polynomial in t^2 is
not irreducibility after substituting t^2.

Bound an initial single-prime certificate search to primes at most 101;
this is a work cap, not a mathematical completeness bound. If it fails,
use the already covered modular-degree constraints or an explicitly
certified complete rational algorithm; do not silently enlarge the cap.
If no full certificate is feasible within one coherent attempt, save
partial factors and identify each unresolved irreducibility claim.
Continue to supported-class arithmetic only after the exact product and
all irreducibility claims are certified. Otherwise abandon only the failed
certificate method, preserving its evidence. Factorization alone is not
a point bound, an empty fake Selmer set or an integer exclusion. The known
infinity points already prevent an empty rational-point image.

## Mathlib and remaining scope

Full matching Mathlib coverage of this instance and of a complete
factorization certificate was not checked. No absence claim is made.
The generic source results are cited rather than reproved. The future
instance verification is REPRODUCTION under SPECIALIZE, not a claim of
source-level novelty. Maximal orders, class/unit data, full local images,
surviving-cover points, root recovery, remaining factors, both L095
systems and the minus-eleven alternative remain unresolved.
