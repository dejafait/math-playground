# Fixed finite seven-primary Sha — proposed integral leading-term comparison

TARGET: Assess whether an integral ordinary main-conjecture leading-term theorem, applied to L033 and L034 on the conductor-389 curve at seven, certifies Sha(E/Q)[7^infinity]=0 under independently checkable hypotheses.
CHECKED: 2026-10-18
DECISION: IMPORT
SEARCH_EVIDENCE: Targeted local comparison of foundations/04--05, L004/L030/L033/L034, the first-index/full-descent assessments and ATTEMPTS/031/034 found no prior import of Stein--Wuthrich Theorem 12.3; exact ordinary-leading-term/regulator and Skinner--Urban searches led to the published fixed-case theorem in the already cited Stein--Wuthrich paper. Exact theorem/errata searches produced no inspected correction to it; this is not a certified exhaustive errata search.
SOURCE_EVIDENCE: Stein--Wuthrich, Math. Comp. 82 (2013), 1757--1792, published author offprint https://wstein.org/papers/mcom2649-iwasawa-alg.pdf , Theorem 12.3 and proof/Remark 12.4 p.1788; Section 12.4 pp.1787--1788; Algorithm 11.1 and its full ordinary proof pp.1783--1784; Theorem 6.1 p.1776 and Proposition 7.2/Theorems 7.3--7.4 p.1778 inspected. Exact model naming reuses L034's inspected Cremona sources.
COMPARISON: Theorem 12.3 already covers the fixed curve and prime and is stronger than the proposed new applicability calculation; its published computational proof can be imported. Reproducing a regulator or proving a reverse main-conjecture divisibility is unnecessary for this target. L033/L034 alone still do not supply the integral conclusion.
GAP: No essential theorem coverage remains missing for a cited fixed-case import; a separate application must match the exact model and prime, retain computational-source qualifications and justify the passage from seven-torsion to the seven-primary group. No original regulator transcript or independent replay is supplied.
REASON: A documented exact known result changes the route from new integral arithmetic production to a short known-theorem import. No new lemma, mathematical script or Sha theorem application is made in this literature-only turn.
SCOPE: Exact curve [0,1,1,-2,0] at p=7; direct import of the published fixed-case result only. No general integral upgrade of L004, L026 premise package, other curve, full Sha finiteness or arbitrary-curve rank conclusion is covered.

## Gap, intermediate target and decision test

The arbitrary-curve rank/order gap remains open. The intermediate target
is a source-level verdict on removing the fixed seven-primary defect
without completing the degree-48 unit/class calculation. Its downstream
use is an independent fixed arithmetic input; it cannot supply arbitrary
rational directions or the refined formula for all curves. The startup
test was an exact theorem with a finite, noncircular applicability task,
or a concrete unavailable hypothesis requiring this mechanism to stop.
The exact published fixed-case theorem passes the source-coverage test.

## Primary theorem and relevant proof cases

[Stein--Wuthrich, published offprint](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=32),
Theorem 12.3 (p.1788), states Sha(E/Q)[p]=0 for the rank-two
conductor-389 curve at all good ordinary p<48859 except 16231,
and also at two. Its proof is a computation using Section 12.4's
method. The complete ordinary proof of Algorithm 11.1 (pp.1783--1784)
uses a certified nonzero regulator, full Mordell--Weil group, local
factors, Theorem 6.1's algebraic leading term and integral Kato
divisibility to bound Sha. Main-conjecture equality is not required.
Remark 12.4 explains the exceptional prime through extra regulator
valuation. Section 12.4 distinguishes its proved upper bound from
additional numerical BSD consistency checks.

Theorem 7.3 requires surjective p-adic representation and semistability
at p; Proposition 7.2 transfers residual surjectivity for p>=5.
Theorem 7.4 otherwise allows a power of p. Theorem 6.1 retains finite
p-primary Sha and nondegenerate height in its leading-term formula.
These distinctions matter for a new calculation; Theorem 12.3 already
packages the fixed computation.

## Local comparison and applicability obligations

L030 establishes the minimal conductor-389 non-CM model, L034 identifies
it with the published 389A1/389a1 model [0,1,1,-2,0], and L033 certifies
good ordinary reduction at seven with #E(F_7)=13. These are independent
local inputs for matching the source statement. Seven lies below the
stated cutoff and is not the exceptional prime. The source identifies
its curve immediately before Theorem 12.3 as 389a; this is a curve-label
match through L034's Cremona input, not an assertion that any curve with
the same rank and conductor may be substituted.

The published fixed-case theorem has no additional caller-supplied
residual, regulator, Manin or period assumption. Its proof's computation
is part of the imported theorem. The original regulator transcript and
residual-surjectivity calculation have not been replayed here. Retain
this computational-source qualification explicitly in the canonical
import; do not relabel the present literature review as independent
certificate validation. The future passage from its p-torsion conclusion
to the target p-primary group needs the elementary torsion-group argument,
to be written in the subsequent application, not derived in this review.

L033 gives the unit coefficient and L034 finiteness/nondegeneracy, but
neither canonically records residual surjectivity or a regulator valuation.
Thus the existing rationalized L004 cannot itself supply an integral
order bound. L081's local nondivisibility is useful local information,
not a replacement for either obligation. A new leading-term computation
would need the missing integral data; importing an exact result already
proved for this curve avoids that redundant reproof. Do not infer the
full L026 package or an actual descent representative from this import.

## Searches, duplicates and disposition

Search queries included “elliptic curve p-adic regulator integral leading
coefficient characteristic series Sha good ordinary Schneider Perrin
Riou theorem”, “Skinner Urban Iwasawa main conjecture elliptic curves
theorem 3 residual ramified multiplicative prime”, and exact
“Stein Wuthrich 12.3 errata” / “389a1 surjective 7 Stein Wuthrich”.
Only primary theorem statements support the decision; snippets and
unrelated claimed BSD proofs were not used. The Skinner--Urban author
PDF https://www.math.columbia.edu/~urban/eurp/MC.pdf was inspected narrowly
at Theorem 3.6.4 and the adjacent proof: its residual irreducibility,
distinguishedness and ramified multiplicative-prime conditions would
still need matching. It is unnecessary for the stronger exact overlap;
no application or full proof inspection of that theorem is claimed.

Reused foundations/04--05 and L004's existing known-source coverage;
searched the relevant first-index/full-descent assessments and read
ATTEMPTS/031 and /034. Those stops concern missing generic localization
or descent arithmetic and do not ban this fixed theorem import. L035's
completed complex-order comparison is not repeated. No enlarged point,
auxiliary-prime or order-correction calculation is proposed.

The next concrete target and the same coverage are recorded in
[the import assessment](2026-10-18-fixed-seven-published-sha-import.md).
Its newly ready continuation requires the supervisor's separate approval
before application. Mathlib matching/supporting coverage is **not checked**;
the published theorem is the mathematical input, not a library claim.
