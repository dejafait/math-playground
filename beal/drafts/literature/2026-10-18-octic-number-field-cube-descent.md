# Octic number-field cube descent — source comparison

TARGET: Assess a finite cube-class descent for both L095 systems over Q[X]/(H(X,1)), including exceptional prime support and the system-II scaling.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Checked L095, audited L097, ATTEMPTS/043–044 and the two prior rational-factor assessments; searched superelliptic q-descent, homogeneous binary-form power descent, nonmonic leading-coefficient support and K(S,p) exact-sequence terminology; no exact classification of these two systems was found in this bounded search.
SOURCE_EVIDENCE: Mourao, arXiv:1010.2360v5 (15 May 2012), Proposition 2.3 and Sections 2.1–2.3, printed pp.2–4, including the complete ideal-support argument; Cremona–Lingham, author manuscript egros.pdf, Section 2, printed p.3, definition and full m-Kummer exact sequence, inspected.
COMPARISON: Known nonmonic linear-factor support and finite multiplicative Selmer-group methods cover the proposed mechanism; Mourao's projective curve setup assumes q divides the degree, so the degree-eight primitive-integer-pair specialization is not a direct theorem import.
GAP: Establish the fixed-pair support specialization for degree eight, certify a sufficient exceptional-prime set and the two scaled norm constraints, and retain S-class three-torsion; no class list or integer exclusion is supplied by the sources inspected.
REASON: Source coverage supports a bounded specialization attempt, rather than another discovery turn or a claim that a projective curve theorem already solves these systems.
LITERATURE_REASON: Changed from auditing rational irreducibility to number-field cube descent, an explicitly uncovered technique requiring essential theorem-level comparison.
SCOPE: Source comparison only in this turn; a separate assessment covers the proposed fixed-pair support attempt, not a projective Selmer computation or integer emptiness.

The main gap remains integer elimination of both L095 systems, with
other algebra factors and residual signatures unresolved. The proposed
intermediate target is a finite, precisely justified necessary cube-class
reduction over the degree-eight field supplied by audited L097. This
could support a later compatibility or integer lifting test; finite
classes alone would not imply emptiness.

Essential inputs are L095's exact H, both complete systems and their
positivity and gcd conditions, and L097's audited irreducibility. Retain
the nonmonic leading coefficient 1215, n=5C and the multiplier 5^11.
At invocation no integral generator, maximal-order model, exceptional-prime set,
class group, unit group, norm identity or finite class list has been
certified for this proposed descent. Polynomial discriminants must not
replace maximal discriminants without justification. A cube norm alone
must not be treated as a certified element cube class.

The initial continuation required primary hypotheses and the essential
ideal-factor cases before any derivation. That source comparison is now
complete for the bounded support method described below. No target-specific
support theorem, discriminant calculation or new lemma was derived here.
The standalone eleven-adic and direct rational-factor stops remain intact.

## Primary methods actually inspected

M. Mourao, *Descent on superelliptic curves*,
[arXiv:1010.2360v5](https://arxiv.org/pdf/1010.2360v5), 15 May 2012:
Proposition 2.3 and Sections 2.1–2.3, printed pp.2–4. After a birational
change he assumes q divides the degree. Section 2.2 works with primitive
integral X,Z. Outside the leading coefficient, both the linear factor
and complementary factor are locally integral. A valuation not divisible
by q forces both factors to vanish modulo the prime ideal. Coprimality
then makes Z invertible and puts the prime in the complementary-factor
evaluation support. This gives a finite supported power-class group.
Section 2.3 imposes the weighted norm condition. These are necessary
conditions, not emptiness theorems. All prime cases were read; no
degree-eight specialization is claimed by citation. The active version
is v5; v4's withdrawn status does not identify v5 as withdrawn.

J. E. Cremona and M. P. Lingham, *Finding all elliptic curves with good
reduction outside a given set of primes*, Experimental Mathematics
16(3) (2007), 303–312; inspected
[author manuscript](https://johncremona.github.io/papers/egros.pdf),
Section 2, printed p.3. For a number field K and a finite set S of
maximal-ring prime ideals, K(S,e) consists of multiplicative e-power
classes whose valuations outside S are divisible by e. The displayed
unnumbered e-Kummer sequence is

    1 -> O_(K,S)^*/O_(K,S)^{*e} -> K(S,e) -> Cl(O_(K,S))[e] -> 1.

It supplies finiteness and identifies the S-unit and S-class-torsion
contributions. No class-number-one or roots-of-unity hypothesis is
imposed. Computing representatives requires certified arithmetic of
these groups; finiteness alone is not their computation. This general
Section 2 statement, not the paper's elliptic-curve algorithm, is the
input relevant here. Manuscript and published pagination are distinct.

## Applicability boundary and concrete continuation

The proposed follow-up is a necessary containment for the actual fixed
integer pairs (m,C) and (m,5C), retaining every condition of L095. It
does not identify these systems with rational points on y^3=h(x), and
does not use projective rescaling to change the pair. The degree-eight
support argument must be written separately from the source's
degree-divisible projective construction. This is the identified reason
for reproducing the local ideal argument rather than citing the whole
algorithm as directly applicable.

For that attempt, h=H(X,1), K=Q[X]/(h) and theta is its residue class.
A candidate sufficient support is all maximal-ring primes over the
rational primes dividing 5*1215*Disc(h). This is a proposed bound to
certify, not a computed discriminant, a minimal set, or a statement
about the field discriminant. The nonmonic denominator issue can be
treated by local integrality away from 1215; a global integral generator
is an optional model, not permission to assume theta integral everywhere.
The system-II multiplier must remain 5^11 and its second argument 5C.
Both scaled norm constraints are still to be established explicitly.
Primes dividing C must be handled uniformly, not added to an allegedly
fixed support. At S all valuation patterns may be retained; no fabricated
local exclusion or unproved ideal principality is needed.

Continuation test: succeed only with a nonzero field-element class for
every original admissible tuple, a certified fixed finite support,
both scale-correct norm constraints and a finite ambient group retaining
its full three-torsion contribution. Stop or narrow the claim if any
prime, denominator or scalar case escapes. Computing a representative
list and using it with C's fifth-power relation are later gaps; even a
complete finite list would not imply integer emptiness.

The ready continuation is recorded in
`drafts/literature/2026-10-18-octic-supported-cube-classes.md` for separate
next-turn gate approval. No dependent mathematics was run in this turn.

## Search, reuse and scope qualifications

Queries included “superelliptic curves descent nonmonic polynomial q
descent Bruin Stoll Mourao”, “binary form equation number field descent
discriminant cube”, “generalized Fermat binary form descent leading
coefficient”, “K(S,p) class units descent”, and exact coefficient strings
from H. Searches also surfaced general superelliptic height bounds,
two-cover methods and newer fixed-signature Kummer work. Those leads
were not read as applicability inputs and are not claimed to cover H.
Failure to locate a matching classification does not establish novelty.
The two prior local assessments expressly excluded this number-field
method. ATTEMPTS/043–044 remain specific mechanism stops, not bans on
this independently testable support target.

The [live Mauldin formulation](https://sites.math.unt.edu/~mauldin/beal.html),
checked 2026-10-18, still specifies positive integer bases and exponents,
all exponents greater than two, and a common prime divisor. It matches
GOAL.md, including unit bases and no height bound. The nominated AMS
page failed retrieval again; its current contents were not inspected.

Mathlib: full matching support-specialization coverage was not checked.
No mathematical novelty or completed Beal input is asserted by this
literature comparison. No lemmas, mathematical scripts, DAG or argument
assembly were changed.
