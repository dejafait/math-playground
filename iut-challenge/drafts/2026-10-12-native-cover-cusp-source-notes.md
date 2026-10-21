# Native cover/cusp source comparison — 2026-10-12

This literature-only review imports definitions and known isogeny inputs.
It constructs no quotient, marking or lemma for E_0. The main gap remains
original finite B>=A and actual input/action/pilot/essentiality compatibility.

## Primary sources and inspected cases

[Mochizuki, IUT I](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf),
May 2020, 186-page author PDF: Definition 3.1(d)–(f), printed pp.62–63,
and Remarks 3.1.2(iii),3.1.3,3.1.6, pp.64–66. The author endpoint now
yielded readable complete relevant passages. This confirms their wording,
not byte identity with the reproduction or the separate journal version.

Clause (d) distinguishes the basic level covering from C_K and the
further theta covering. Clause (e) requires the basic local cover at every
selected bad place to have EtTh's graph-quotient type. Clause (f) selects
a nonzero global cusp with local graph-generator label up to sign.
Remark 3.1.3 does not remove the need to verify selected data.
Remark 3.1.6 corrects the even-level construction: use odd level and do
not import the deleted EtTh Remark 2.2.1.

[Mochizuki, EtTh](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Etale%20Theta%20Function%20and%20its%20Frobenioid-theoretic%20Manifestations.pdf),
December 2008 author PDF, 112 pages; journal reference PRIMS 45 (2009),
227–349. Inspected section 2 opening/Definition 2.1, pp.32–33;
Proposition 2.2, entire proof, and Definition 2.3, pp.34–35;
Definition 2.5(i), p.36; section 1 opening, pp.10–12, and double-dot
base-field definition, p.16. Also read Theorem 1.10's hypotheses,
parts (i)–(iii) and proof, pp.27–28; cusp-label discussion/Corollary 2.9
and its entire proof, pp.39–40. No later environment theorem is imported.

For characteristic-zero non-arithmetic once-punctured elliptic X, the
basic construction uses a rank-one Z/lZ quotient of its elliptic
fundamental-group quotient: geometric restriction surjects and the
original cusp decomposition group maps trivially. Cusps are rational;
choosing an origin gives the inversion quotient and cartesian square.
Local graph type requires factorization through the profinite completion
of the tempered graph quotient, odd l, odd residue characteristic and
K=K-double-dot=K_2=K(zeta_2,q_X^(1/2)). The separate theta cover requires
a compatible splitting. Theorem 1.10(iii)'s standard-type and
square-root-of-minus-one hypotheses must be retained if invoked.
Labels come from the infinite graph cover, modulo l and sign; arbitrary
nonzero torsion is not asserted to have label ±1.

[Sutherland, MIT 18.783 Lecture 5](https://math.mit.edu/classes/18.783/2023/LectureNotes5.pdf),
26 September 2023: Corollary 5.2, p.2; Theorem 5.8, pp.3–4;
Theorem 5.11 with full proof sketch and field-of-definition qualification,
pp.5–6; Theorem 5.25 with proof, p.14. Finite subgroup quotients are
separable isogenies defined over the subgroup's field of definition;
the translation quotient is unramified. Multiplication by n has degree
n^2, separable when n is prime to field characteristic. The quotient
proof is explicitly a sketch; no independent reproof is claimed.

[Milne, Elliptic Curves, second edition, 2021](https://www.jmilne.org/math/Books/EC2.pdf):
II.1.7, p.49, kernel inclusion gives isogeny factorization, with
inseparable group-scheme qualification; II.6.3, p.70, prime-to-characteristic
torsion has rank two; III.3, pp.102–103, Tate uniformization discussion
and (23)–(26). These passages were inspected. Reuse the assessed Tate
theorem and finite-extension/Galois qualification in
`drafts/literature/2026-10-10-split-tate-compatible-local-packet.md` and
`drafts/literature/2026-10-11-approximating-curve-geometric-tate-parameter.md`.
Silverman III.4.12 faculty-host retrieval timed out: unread lead, unneeded
once Sutherland's matching quotient theorem is available.

## Verdict and separate continuation

The literal full multiplication cover carries rank-two torsion, whereas
EtTh specifies a rank-one quotient. Literal identification is unsupported.
This is an imported-object comparison, not a newly derived degree theorem,
a counterexample to initial data or a proof of native nonexistence.
A specified intermediate quotient of the same map is a separate test.

Retain L045,L048 and K=D=F(E_0[7]); L052 only for quotient coricity,
L051 only for reduction. The intermediate test must check K-definition,
punctures, inversion square, trivial original cusp decomposition image,
graph factorization and chosen cusp label. Point-group agreement alone
is insufficient for graph-cover identification. A complete place section
and theta-root splitting are not supplied by this review.

Duplicate/failure checks used the two native assessments and history/176;
ATTEMPTS/022,025,026 exclude other packet roles, /027 only the exact old
curve, /028 a different model quantifier, /029 redundant core approval.
None decides the intermediate quotient. No cross-notebook input was read.
Queries included `Mochizuki Definition 3.1 cusps covering`, `Mochizuki
EtTh l-covering`, the exact EtTh title and `elliptic curve finite subgroup
quotient isogeny theorem 4.12 Silverman`. Secondary IUT material and
search snippets were leads only. Full matching Mathlib coverage is unchecked.
