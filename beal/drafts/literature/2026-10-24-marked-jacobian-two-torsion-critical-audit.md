# Marked Jacobian two-torsion critical audit — source scope approved

TARGET: Critically audit L126's rational two-torsion computation, including the complete quadratic-field covering and split-prime quartic-absence certificates.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared the prior approved exact-instance assessment, complete L126 text, L115 finite-field citations, history/456–457 and ATTEMPTS/052,055; the audit is a verification of the same instance, not a new torsion determination or renewed class-backend search.
SOURCE_EVIDENCE: Reused the inspected Muller–Reitsma Section 4.5/equation (4.8)/Lemma 4.8, Poonen–Schaefer Proposition 6.2 and Milne ramification/finite-field inputs; additionally read Milne ANT v3.08 Theorem 2.1/Proposition 2.3 pp.25–26, Proposition 2.9 and proof p.28, and Proposition 7.31 with full proof p.120 for the split-prime method.
COMPARISON: The known even-branch module covers complement-exchanged quartics; standard local lifting and integral-factor reduction cover the replacement of optional Trager factorization by complete modular degree obstructions. The sources do not verify this instance's six factor lists, 31 assignments or arithmetic records.
GAP: Independently audit all essential implications and full relevant certificate records; the present review approves source scope only and does not certify L126's conclusion.
REASON: The unchanged exact torsion instance has reusable primary coverage; the critical audit requires instance verification, not a new theorem or general factorization algorithm.
LITERATURE_REASON: The saved audit continuation was REVIEW_REQUIRED; its changed implementation uses split-prime absence certificates, whose lifting and integral-reduction coverage needed explicit comparison.
SCOPE: Exactly TARGET for L113's actual marked smooth curve, with audited L115/L116 inputs and L126's complete producer/replay evidence; excludes rank, supported-group completeness, rational-point determination and integer exclusion.

## Sources reused and additional source check

The source search and theorem comparison in
`drafts/literature/2026-10-24-marked-jacobian-rational-two-torsion.md`
remain applicable to the unchanged polynomial and hypotheses. In particular,
reuse J. Steffen Müller and Berno Reitsma, *Computing torsion subgroups
of Jacobians of hyperelliptic curves of genus 3*, Research in Number
Theory 9 (2023), article 23,
[Section 4.5, equation (4.8), both cases preceding Lemma 4.8 and Lemma 4.8, PDF pp.18–19](https://doi.org/10.1007/s40993-023-00429-x).
Reuse Poonen–Schaefer, *Explicit descent for Jacobians of cyclic covers
of the projective line*, J. Reine Angew. Math. 488 (1997), 141–188,
[10 February 1997 author manuscript, Sections 4 and 6, Proposition 6.2 and proof](https://math.mit.edu/~poonen/papers/descent.pdf).
Do not reread them merely for scheduling balance. The invariant
unordered-partition case is essential; invariant subsets alone do not
cover the target. No claim that a prior arithmetic replay is an audit
is accepted.

For the implementation difference, additionally inspected J.S. Milne,
[Algebraic Number Theory, v3.08, 19 July 2020](https://www.jmilne.org/math/CourseNotes/ANT.pdf):
Theorem 2.1 and Proposition 2.3 with the first proof, printed pp.25–26,
assert closure of integral elements under ring operations; Proposition
2.9 and its proof, p.28, gives integral closedness for a PID.
Proposition 7.31 and its complete constructive proof, p.120, lifts a
simple residue root over a complete DVR uniquely in its residue class.
Its hypotheses require a polynomial over that DVR and a nonzero
residue derivative. These are the standard inputs for checking the
split-field embeddings and monic integral factors in L126; no new
local theorem is proposed. The current source remains v3.08.

Reuse the prior Milne ANT Theorem 3.35, quadratic-discriminant examples
and tower input for the covering, with L116's maximal-field
discriminant. Reuse the exact finite-field test recorded in audited
L115: Milne, *Fields and Galois Theory*, v5.10 (September 2022),
Propositions 1.13–1.14 p.12, Remark 1.18 p.14, Proposition 4.20 and
Corollaries 4.21–4.22 pp.53–54, Exercise 4-8 p.60.
The optional SymPy/Trager implementation is unnecessary to this audit;
its unread original paper is not an essential source blocker. No
stronger full-torsion algorithm or sampled Galois-group claim is needed.

## Bounded audit obligations and stopping test

The main gap remains primitive positive integer nonexistence; in this
branch supported arithmetic and rational/integer point control are
missing. The intermediate target is a critically checked rational
two-torsion input for a possible later Jacobian descent/rank argument.
It cannot supply a rank bound by itself.

In one separate research turn check L126's complete argument against
the imported hypotheses, including actual twist/infinities, even
partitions modulo complement, the quadratic coefficient-field and
root-field relationship, and every candidate in the discriminant
covering. Check simple-root lifting conditions, monic integral
specialization, preservation of degree, every full modular product,
all required Frobenius and Bezout identities, subset degrees and all
31 assigned witnesses. Inspect complete load-bearing certificate
fields, not previews; independent arithmetic replay remains evidence
requiring mathematical interpretation. Check both the zero-group
conclusion and L126's stronger quadratic-irreducibility conclusion.

Continue only if all essential cases close; any failed case reopens
the precise claim, with a correction or unresolved obligation recorded.
Do not substitute irreducibility over Q for the exchanged case or infer
rank, full Kummer image or points from the rational torsion value.
The known rational infinity points persist. Full units/S-class
two-torsion, descent/rank, cover points, degree-nine recovery, remaining
factors, both L095 systems and minus-eleven remain unresolved.

ATTEMPTS/052's backend blocker and ATTEMPTS/055's exhausted bounded
family remain preserved and are independent of this finite audit.
There is no duplicate completed critical audit of L126 in the inspected
current records. This step changes source readiness only; it produces
no new lemma, calculation, certificate or beyond-source result.
Mathematical exploration usage stays zero. Mathlib coverage of the
full branch-module theorem and exact-instance result remains not
checked; unknown availability is not absence.
