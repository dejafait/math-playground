# Marked Jacobian rational two-torsion — source comparison approved

TARGET: Determine the rational two-torsion of L113's Jacobian by classifying Galois-stable even branch partitions, including partitions exchanged with their complements.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared L113–L116, the marked-model/support/factorization and earlier pair-rank assessments, ATTEMPTS/050,052,055 and history/455; searched even-degree rational two-torsion, complement-stable partitions, Stoll descent, exact octic coefficients and Muller–Reitsma Lemma 4.8/errata; found a complete primary method, but no inspected determination for this exact octic.
SOURCE_EVIDENCE: Read Muller–Reitsma (2023), Section 4 setup and Section 4.5 pp.18–19, equation (4.8), both Galois cases, Lemma 4.8, Example 4.9 and Remark 4.10; Poonen–Schaefer author manuscript dated 10 February 1997, Section 4 pp.6–7 and Section 6 pp.10–11 including Proposition 6.2 and its proof; Milne ANT v3.08, Theorem 3.35/proof pp.60–62, Example 2.41 p.39, Example 3.44 p.63 and Exercise 4-2 p.83; official SymPy 1.14.0 polynomial factorization and Trager-method documentation.
COMPARISON: Known Galois-module and quadratic-factor counting results cover the whole rational two-torsion problem, including exchanged quartics; L115 irreducibility alone and the odd-degree pair-rank formula do not. No checked source supplies this instance's complete factor certificates or generators.
GAP: In a separate research turn certify the complete invariant-partition list for the unchanged octic, using all required quadratic fields and exact factorization/complement checks, then give generators and prove completeness; no torsion group has been computed here.
REASON: Primary coverage now approves a bounded specialization of known methods independent of the parked class/unit backend; import the general results rather than reprove them, and compute only the exact instance next turn.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED; prior curve-point fake-map and odd-degree Jacobian assessments did not cover exchanged complements for an even-degree genus-three Jacobian.
SCOPE: Exactly TARGET for L113's unchanged smooth curve and Jacobian; use L114/L115 and audited L116's field discriminant for a finite quadratic-field covering, exact polynomial factorizations and invariant-partition generators; excludes rank, complete supported arithmetic, rational-point completeness and integer exclusion.

The main gap remains primitive positive integer nonexistence, with full
supported arithmetic and point control missing in this branch. The
intermediate target is an exact rational two-torsion group, potentially
fixing the torsion contribution in a later Jacobian descent/rank bound.
It does not itself supply units, S-class two-torsion, rank or rational
points. The fake curve-point quotient must not be equated with the
Jacobian's full Kummer image without an appropriate theorem.

Essential local inputs are L113 (actual smooth marked curve), L114
(unchanged model/support convention), L115 (entire degree-eight field)
and, for the finite-field covering below, L116's audited field
discriminant. Only the relevant model/factorization proofs and L116's
statement were loaded; L116's audit is reused, not independently repeated.
L111/L112 are unnecessary for this method and were not loaded. Accept
only a complete classification with explicit generators or a proved
trivial group; partial Galois data or ordinary irreducibility alone must
not be reported as completeness. A failed finite certificate must be
recorded precisely rather than replaced by a speculative group value.

This proposal does not reopen ATTEMPTS/055's quadratic family,
ATTEMPTS/054's fixed mask, or ATTEMPTS/052's backend probes. Full
units/S-class two-torsion, cover points, degree-nine recovery, remaining
factors, both L095 systems and minus-eleven remain unresolved. No new
lemma, torsion value or mathematical script was produced in this
literature turn. The approval concerns source/method readiness only.

## Imported results and qualifications

J. Steffen Müller and Berno Reitsma, *Computing torsion subgroups of
Jacobians of hyperelliptic curves of genus 3*, Research in Number Theory
**9** (2023), article 23, published 19 March 2023,
[DOI and published text](https://doi.org/10.1007/s40993-023-00429-x),
[published PDF](https://link.springer.com/content/pdf/10.1007/s40993-023-00429-x.pdf).
Read the Section 4 setup (PDF p.13) and all of **Section 4.5, PDF
pp.18–19**, including the argument preceding **Lemma 4.8**.
For squarefree degree-eight f over Q, equation **(4.8)** identifies
geometric two-torsion with unordered even partitions of its roots:

    P_U = [sum_(a in U) (a,0) − (|U|/2) D_infinity],
    P_U = P_(Omega\U).

This identification is Galois equivariant. Rational classes include
partitions whose two quartic halves are exchanged over a quadratic
field k. These correspond to monic h with
`f=lc(f) h h^sigma` and `gcd(h,h^sigma)=1`; k embeds in Q[x]/(f).
Writing t_Q for half the number of monic even-degree Q-divisors and
t_k for half the number of these h, Lemma 4.8 gives
`#J(Q)[2]=t_Q+sum_k t_k` over quadratic subfields. Example 4.9
explicitly exhibits irreducible f with nonzero rational two-torsion.
No monicity or geometric-simplicity hypothesis is needed for this
counting method. A swapped class need not have a Q-defined
Mumford representative of the special form (A,0,C).

Bjorn Poonen and Edward F. Schaefer, *Explicit descent for Jacobians of
cyclic covers of the projective line*, J. Reine Angew. Math. **488**
(1997), 141–188, DOI 10.1515/crll.1997.488.141;
[author manuscript](https://math.mit.edu/~poonen/papers/descent.pdf),
dated **10 February 1997**, **Section 4 pp.6–7, Section 6 pp.10–11,
Proposition 6.2 and its full proof**, and the concluding norm-module
identification. The hypotheses are characteristic different from p,
primitive pth roots of unity in the base, an actual cyclic map to P1,
and a model unramified over infinity with p dividing its degree.
For p=2 the branch multiplicities are one and phi is multiplication
by two. The theorem describes J[2] as the even branch module modulo
the diagonal class, with its Galois action. The proof identifies the
sole diagonal relation, rather than taking invariants before quotienting.
The actual leading coefficient is retained; a rational branch point is
not required. This supports the even-partition import, without
identifying the curve-point fake image with J(Q)/2J(Q).

J.S. Milne, *Algebraic Number Theory*, **v3.08, 19 July 2020**,
[author PDF](https://www.jmilne.org/math/CourseNotes/ANT.pdf):
**Theorem 3.35, printed pp.60–62**, with the reduced-residue-algebra
proof; **Example 2.41 p.39**, including both mod-four discriminant
cases; **Example 3.44 p.63**; **Exercise 4-2 p.83** (tower
multiplicativity). These standard results imply that a quadratic
subfield of a number field unramified outside a prime set S containing
2 is among Q(sqrt(d)) for signed squarefree products d of primes in S.
Use the actual maximal-ring discriminant, not a nonmonic polynomial
discriminant. Here audited L116 supplies the field input with support
{2,3,5,11}; the research proof must spell out that applicability.
Testing this finite superset does not assert that all its fields embed.

## Exact execution and certificate requirements

L113 supplies squarefreeness, genus three and two rational infinities;
L115 supplies the whole root field and the nonmonic scalar. Thus the
primary methods apply to **G=11F**, without replacing the marked curve
by Y²=F. Its branch set may be computed from the monic normalization,
while divisor classes and both infinities remain on L113's curve.
The odd-degree m−1 rule in the earlier pair-rank assessment is outside
its hypotheses here; ATTEMPTS/050's torsion allowance belongs to a
different Jacobian.

In the separate calculation, enumerate Q's even divisors and cover
every possible exchanged partition by factoring over the signed
squarefree-divisor fields of 330 (omit the square d=1). Retain the
entire factors and every multiplicity. Enumerate every monic quartic
divisor there, check the conjugate product and gcd exactly, and identify
h with h^sigma. Do not count quadratic embeddings as separate classes.
Give the full list of rational partitions before choosing generators;
the branch-module addition is symmetric difference modulo complement.
The resulting exhaustive list must agree with the group generated.
An exchanged partition itself, with its coefficient field and exact
conjugation, specifies a generator through (4.8); do not fabricate a
Q-rational branch divisor to represent it.

An executable route is exact algebraic polynomial factorization, rather
than maximal-order unit/class arithmetic. Inspected official
[SymPy 1.14.0 factor_list/factor documentation](https://docs.sympy.org/latest/modules/polys/reference.html#sympy.polys.polytools.factor_list),
[algebraic domains](https://docs.sympy.org/latest/modules/polys/domainsref.html),
and [dup_ext_factor's Trager explanation](https://docs.sympy.org/latest/modules/polys/internals.html#sympy.polys.factortools.dup_ext_factor).
The documented method shifts a polynomial to obtain squarefree rational
norm, factors that norm over Q, takes exact gcds over the extension and
undoes the shift. Save those exact norm, squarefreeness, complete rational
factorization and gcd witnesses if this route is used. Full product
equality alone does not certify irreducibility or exhaustive absence.
The original Trager (1976) paper is a referenced, unread lead; approval
uses the inspected official implementation explanation, not a claimed
reading of that paper. No general factorization algorithm is reproved.

Continue only with complete factorization/absence evidence for every
candidate field and an exhaustive partition/generator certificate.
If an irreducibility or completeness obligation cannot be certified
within this one finite family, preserve the exact unresolved case and
park that dependent calculation. Do not enlarge a point-search box,
retry the class backend, or substitute Frobenius samples for the whole
Galois action. The bound concerns one finite structural computation;
no torsion value, factor over a quadratic field or rank is predicted.

## Search record, balance and Mathlib

Queries included `hyperelliptic Jacobian rational 2 torsion even degree
partitions complement Galois invariant`, `Stoll implementing 2 descent
Jacobians hyperelliptic curves rational 2 torsion factorization even
degree`, `"275" "2860" "Jacobian" torsion`,
`"275" "2860" "6930" hyperelliptic torsion`, and
`"Müller" "Reitsma" "4.8" erratum`. No matching exact-instance
answer or applicable correction was identified; neither absence nor
novelty is inferred. Schaefer's 1995 odd-degree paper and Stoll's
2001 odd-degree formulas are insufficient alone. Müller–Reitsma's
stronger full-torsion algorithm is unnecessary for this target.
Its code repository is a lead, not an executed calculation.

The shell PDF download failed DNS resolution, but the primary PDFs and
relevant theorem/proof text were accessible through the web tool; this
is not an essential source blocker. No backend availability probes or
mathematical calculations ran. This literature step spends no
mathematical exploration turn. Ready coverage now defaults to research.
Mathlib coverage for the full branch-module theorem and exact-instance
torsion computation is **not checked**; no absence claim is made.
