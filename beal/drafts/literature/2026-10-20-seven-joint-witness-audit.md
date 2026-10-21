# Joint seven-adic witness — audit source comparison

TARGET: Critically audit L105's common primitive seven-adic witness and disjoint whole-factor decomposition, including the exact degree-eight complement.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused exact-polynomial, signature/local/seven and Hensel-factorization searches documented in 2026-10-20-quadratic-minus-three-seven-adic-test.md; compared the full L105 proof, its working draft, histories 357–358 and ATTEMPTS/046; inspected Stacks tag 00U3 for the precise complement criterion.
SOURCE_EVIDENCE: Reused inspected Sharifi, Algebraic Number Theory, online Chapter 5, Theorems 5.3.30 and 5.3.33 with proofs, and Clark Theorem 1.79 p.58 in foundations/17; inspected Stacks Project Lemma 10.143.4 (00U3), statement and proof, online version accessed 2026-10-20.
COMPARISON: Named lifting and polynomial Chinese remainder theorems support the claimed construction, and Stacks characterizes etale algebras over a field as finite products of finite separable extensions; none supplies the specific normalized polynomial, seed arithmetic, common tuple or exact coprimality automatically.
GAP: Independent application audit of L105 and its complete relevant certificate remains necessary; no new source coverage or full decomposition of the degree-eight complement is required.
REASON: Essential method coverage matches the exact audit hypotheses; checking this application is justified to validate the recorded local route stop, without reproof of standard theorems or a claim of novelty.
LITERATURE_REASON: The newly written witness introduced an unaudited exact-complement and normalized-root application; this separate scope comparison completes its pending coverage and adds a precise primary etaleness citation.
SCOPE: Exactly TARGET, over Q7 with v7(7)=1, the full degree-eleven fiber at the single scalar s=-342, nonzero integral primitive coordinates, and all three specified exact linear factors plus the entire degree-eight complement.

## Relevance and stopping test

The main gap remains positive primitive integer elimination in both L095
systems and global factor compatibility for ordered (3,5,11); other
signatures remain independent gaps. The intermediate target is the
independent audit of L105's claimed exact local witness. Its downstream
use is deciding whether the standalone joint-factor exclusion at seven
is conclusively parked, rather than spending further precision on an
already realizable necessary condition.

Continue with the audit if the named methods cover every existence and
product step; that source-coverage test now passes. In the separate
mathematical turn, accept the witness only after exact identities,
strict lifting hypotheses, disjointness, full complementary degree and
separability have been checked independently. A concrete failure must
be corrected in canonical L105 and its effect on ATTEMPTS/046 assessed.
An unchanged passing audit verifies the existing local result; it is
not a new mathematical discovery or an integer/global realization.

## Primary inputs and exact applicability obligations

Romyar Sharifi, *Algebraic Number Theory*,
[online Chapter 5](https://www.math.ucla.edu/~sharifi/notes/algnum-ch05.html),
Theorems 5.3.30 and 5.3.33, version inspected 2026-10-20 with no revision
date identified: reuse the prior full statement/proof inspection. The
simple-root theorem requires a complete nonarchimedean field, integral
polynomial and a simple residue root, and gives a unique root in its
residue class. Coprime-factor lifting requires a coprime residual
factorization and cannot separate internally repeated factors. L105's
proposed normalized-root route should be audited against the first
criterion; the second is supporting context, not a license to split
its repeated unnormalized residue root.

Pete L. Clark, *Algebraic Number Theory II: Valuations, Local Fields and
Adeles*, [author-hosted notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
Theorem 1.79, printed p.58, accessible 161-page version retrieved
2026-10-08, no identified revision date: reuse foundations/17's primary
inspection. For integral f and seed a in a complete discretely valued
field, the sufficient inequality is v(f(a))>2v(f'(a)); the theorem gives
an exact root with the stated closeness and uniqueness. The new audit
must check integrality after normalization and actual derivative/error
values for each asserted lift. A finite root approximation alone does
not meet the theorem or the audit target. No reproof is needed.

[Stacks Project Lemma 10.143.4, tag 00U3](https://stacks.math.columbia.edu/tag/00U3),
online version accessed 2026-10-20, statement and entire proof inspected:
for a field k, k -> S is etale exactly when S is a finite product of
finite separable extensions of k. The proof's forward construction
uses gcd(f,f')=1 for a separable minimal polynomial; the converse
reduces an etale algebra to finitely many finite separable fields.
The supporting standard polynomial Chinese remainder theorem applies
to pairwise coprime factors over k. For the proposed complement, the
application obligations are exact divisibility, nonzero leading
coefficient and degree eight, and squarefreeness/coprimality over Q7.
No irreducible factor list or integer-ring etaleness is required.
This review imports the criterion, not a verification of those obligations.

Stacks 59.32.3–4 and their previously recorded proof references remain
adequate henselian/product background. They do not replace the exact
field-level coprimality checks. Putz's integer-solution hypotheses need
not be enlarged: the proposed witness is standalone over Q7, and no
Putz terminal exclusion is an audit premise. Optional package code
and previously inaccessible source leads remain unnecessary.

## Bounded independent audit

Essential mathematical input is L105 and its exact fiber polynomial;
foundations/17 and the prior EXPLORE assessment provide source coverage.
L093 and audited L103/L104 are downstream global context only, not
hidden assumptions of the local construction. The empty L105 DAG row
is therefore to be checked against the self-contained proof, without
adding global branch assumptions. No cross-notebook input is used.

Check both factors of the quadratic completion; one common primitive
tuple and the unchanged scalar in every identity; the complete
normalized polynomial and each exact lifting condition; distinct exact
roots rather than their displayed approximations; exact factor division
and complementary degree; and every critical point in the asserted
whole-fiber separability argument. The regular-residue table is ancillary
to existence, but any claimed arithmetic replay must inspect its complete
relevant evidence rather than a preview. The exact roots specify the
complement; they need not be finite rational numbers or explicit radicals.

If replay is used, inspect complete /regular, /branch, /quadratic and
/checks values in scripts/quadratic-seven/joint-fiber-certificate.json
with the prescribed JSON inspector. Independently verify all load-bearing
identities rather than relying solely on the original script's pass count.
This source review has neither run that mathematical script nor verified
its certificate. No numerical lift is promoted to an exact root.

The existing joint test and its negative evidence are in L105 and
ATTEMPTS/046; the earlier standalone local points do not duplicate its
whole-product condition. ATTEMPTS/045's global arithmetic execution park
remains independent. No source inspected here classifies all primitive
fibers or solves either integer system. Retain the minus-eleven alternative,
larger-field compatibility, global rationality and integer lifting as
unresolved. Full matching Mathlib coverage and supporting declarations
remain not checked, with no absence claim.

This SPECIALIZE assessment approves an independent REPRODUCTION audit
of a known-method application, not new mathematics. No lemma, mathematical
script, PROOF argument or DAG edge was changed during this literature turn.
