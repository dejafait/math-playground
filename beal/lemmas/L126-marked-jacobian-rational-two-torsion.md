# L126 — The marked genus-three Jacobian has trivial rational two-torsion

## Hypotheses

Work over Q with L113's actual smooth proper marked curve C and its
Jacobian J, where

    C: Y²=G(t)=11F(t),
    F(t)=275t⁸−2860t⁶+6930t⁴−3564t²+243.

Use audited L115: F is irreducible over Q and its entire root algebra
K=Q[theta] is a field of degree eight. Use audited L116's maximal-field
discriminant

    disc(K)=2⁸·3⁷·5⁴·11⁷.

No Galois group, quadratic subfield, class group, unit group, supported
square-class completeness, rank or rational-point classification is
assumed. This is L113's marked curve, with its two distinct rational
infinity points, and not a changed constant twist or L095's octic.

## Conclusion

The complete rational two-torsion group is

    J(Q)[2]={0},    #J(Q)[2]=1,    dim_F2 J(Q)[2]=0.

The only Galois-stable unordered even branch partition is
{empty set, all eight roots}. There are no nonzero generators. In fact,
K has no quadratic subfield, and F remains irreducible over every
quadratic field whose discriminant is supported on {2,3,5,11}.

This is an exact specialization of the cited branch-module theorem and
standard factorization criteria. It supplies a torsion input for a later
Jacobian descent/rank calculation, without a rank bound, complete
supported arithmetic, point determination, degree-nine recovery,
remaining-factor control or an integer exclusion. The separate critical
mathematical audit below confirms both conclusions without a mathematical
correction; this verifies an existing input, not a new general result.

## Proof

### Imported statements and specialization

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-24-marked-jacobian-rational-two-torsion.md`.
Import J. Steffen Müller and Berno Reitsma, *Computing torsion subgroups
of Jacobians of hyperelliptic curves of genus 3*, Research in Number
Theory **9** (2023), article 23,
[published text](https://doi.org/10.1007/s40993-023-00429-x),
**Section 4.5, equation (4.8), the argument preceding Lemma 4.8, and
Lemma 4.8, PDF pp.18–19**. For a squarefree octic over Q the geometric
two-torsion is the Galois module of even root subsets modulo complement.
If Omega is the branch set, the class of an even subset U is

    P_U=[sum_(a in U)(a,0)−(|U|/2)D_infinity],
    D_infinity=infinity_+ + infinity_−,   P_U=P_(Omega\U).

This gives every geometric two-torsion class, with just that complement
identification; addition is symmetric difference modulo complement.
Rationality requires the unordered partition, rather than either half,
to be Galois-stable. The complement-exchanged cases are quartic halves
defined over a quadratic field k that embeds in Q[t]/(F). Equivalently
they come from monic quartic divisors h over k with conjugate product
F/275 and relatively prime conjugate halves. The theorem counts these
cases as well as Q-defined even divisors; irreducibility over Q alone
would not suffice.

The general branch-module input is also Proposition 6.2 and its proof
in Bjorn Poonen and Edward F. Schaefer, *Explicit descent for Jacobians
of cyclic covers of the projective line*, J. Reine Angew. Math.
**488** (1997), 141–188,
[author manuscript dated 10 February 1997](https://math.mit.edu/~poonen/papers/descent.pdf),
**Sections 4 and 6, pp.6–7 and 10–11**. Its characteristic and root-of-
unity conditions hold with p=2 over Q, and degree eight is divisible
by two. L113 proves squarefreeness, smoothness, genus three and
unramified infinity. Thus the imported description applies to G=11F;
the scalar 11 does not change its branch set. We keep the actual
curve and both actual infinity points in the displayed divisor formula.
No curve-point fake quotient is identified with J(Q)/2J(Q).

For ramification and quadratic-field discriminants import J.S. Milne,
*Algebraic Number Theory*, **v3.08, 19 July 2020**,
[author text](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
**Theorem 3.35 and proof pp.60–62, Example 2.41 p.39, Example 3.44
p.63, and Exercise 4-2 p.83**, as inspected in the prior assessment.
The discriminant detects ramification, ramification indices multiply
in a tower, and for squarefree d the quadratic discriminant is d if
d=1 mod 4 and 4d otherwise. In particular a quadratic subfield of K
can ramify only at {2,3,5,11}, by the actual maximal-field discriminant
in L116, and must be among

    k_d=Q(sqrt(d)),  d in {±a : a divides 330}, d!=1.       (1)

These are exactly 31 distinct quadratic fields. This is a covering
list, not an assertion that any candidate embeds in K.

For exact finite-field irreducibility reuse the imported Milne,
*Fields and Galois Theory*, **v5.10, September 2022**,
[author text](https://www.jmilne.org/math/CourseNotes/FT.pdf),
**Propositions 1.13–1.14, Remark 1.18, Proposition 4.20, Corollaries
4.21–4.22 and Exercise 4-8**, with the precise page references and
criterion in audited L115. For a monic h of degree n over F_p the
criterion is

    x^(p^n)=x mod h,
    gcd(h,x^(p^(n/q))−x)=1 for every prime q dividing n.   (2)

These general theorems are cited, not reproved. The difference from
the sources is the exact instance covering and absence calculation
below. The approved scope permits exact factorization/absence
certificates. No Trager norm factorization is used: complete modular
factorizations rule out quartic divisors at a split prime for each
candidate field. This proves the required absence directly and does
not infer a whole Galois action from sampled cycle types.

For the split-prime passage, also import Milne, *Algebraic Number
Theory*, v3.08, **Theorem 2.1 and Proposition 2.3, pp.25–26;
Proposition 2.9 and proof, p.28; Proposition 7.31 and full proof,
p.120**, as checked in the separately approved audit assessment.
Integral elements are closed under ring operations, a PID is integrally
closed, and a simple residue root over a complete DVR lifts to an
actual root. Here the DVR is Z_p, the lifted polynomial is X²−d,
and the residue derivative is 2r!=0. These citations justify the
lifting and integral-factor steps below; neither step assumes that
theta is globally integral.

### Complete modular factorizations

For each of the six primes below, 275 is a unit and the displayed
product is exactly the monic reduction f_p=275^(-1)F modulo p.
Every factor has multiplicity one and is irreducible over F_p.

| p | Complete factorization of f_p | Factor degrees |
| --- | --- | --- |
| 7 | (x²−3)(x³+2x²−x+3)(x³−2x²−x−3) | 2,3,3 |
| 13 | (x²−5)(x³+2x²−2x+6)(x³−2x²−2x−6) | 2,3,3 |
| 19 | x⁸+x⁶+10x⁴+3x²+8 | 8 |
| 29 | (x²+14)(x⁶−7x⁴+13x²−14) | 2,6 |
| 31 | (x²+5)(x⁶−3x⁴+3x²+8) | 2,6 |
| 43 | (x+10)(x−10)(x⁶−5x⁴−19x²+10) | 1,1,6 |

Here is complete compact irreducibility evidence for (2). Number the
factors h_(p,j) from left to right in the preceding table. For every
factor of degree n, the iterated Frobenius R_0=x mod h,
R_(i+1)=R_i^p mod h has R_n=R_0. The full intermediate residues are
stored in the certificate specified below and independently replayed.
For the linear factors this is immediate. For every required proper
index m=n/q, the table gives g=R_m−x mod h and polynomials A,B with
Ah+Bg=1 in F_p[x]. All bracketed lists are complete ascending
coefficient lists; an omitted trailing coefficient is zero.

| (p,j), m | g | A | B |
| --- | --- | --- | --- |
| (7,1),1 | [0,5] | [2] | [0,1] |
| (7,2),1 | [3,1] | [2] | [3,2,5] |
| (7,3),1 | [4,1] | [5] | [4,2,2] |
| (13,1),1 | [0,11] | [5] | [0,9] |
| (13,2),1 | [8,7,2] | [0,9] | [5,10,2] |
| (13,3),1 | [5,7,11] | [0,9] | [8,10,11] |
| (19,1),4 | [0,17] | [12] | [0,18,0,3,0,6,0,6] |
| (29,1),1 | [0,27] | [27] | [0,28] |
| (29,2),3 | [0,27] | [2] | [0,13,0,22,0,1] |
| (29,2),2 | [0,2,0,1,0,26] | [2,0,6,0,25] | [0,0,0,27,0,18] |
| (31,1),1 | [0,29] | [25] | [0,28] |
| (31,2),3 | [0,29] | [4] | [0,6,0,25,0,2] |
| (31,2),2 | [0,14,0,24,0,14] | [4,0,22,0,19] | [0,22,0,14,0,23] |
| (43,3),3 | [0,41] | [13] | [0,27,0,32,0,28] |
| (43,3),2 | [0,2,0,34,0,21] | [13,0,10,0,31] | [0,9,0,13,0,19] |

For clarity the necessary R_n=R_0 congruences are full polynomial
congruences, not evaluation at selected roots. They follow by powering
and division in the finite polynomial quotient; every multiplication
and quotient/remainder identity is retained and checked. The listed
gcd indices exhaust the prime divisors of n (only 2 for n=2,8,
only 3 for n=3, and 2,3 for n=6). Thus (2) proves irreducibility of
all displayed factors. The complete product equalities and
gcd(f_p,f_p')=1 are also checked by exact Bezout identities.

The possible divisor degrees are respectively

    {0,2,3,5,6,8}, {0,2,3,5,6,8}, {0,8},
    {0,2,6,8}, {0,2,6,8}, {0,1,2,6,7,8}.

In every case four is absent. These sets are obtained by exhausting
all subsets of the complete irreducible factor list, including both
distinct cubics at 7,13 and both distinct linear factors at 43.

### Every candidate quadratic field has a certified split obstruction

The following table covers (1) exactly once. Each entry d:r means
r²=d modulo the indicated p, with 0<r<p. Thus 2r is nonzero modulo
p. The simple-root Hensel lemma gives an actual square root of d
in Q_p and hence an embedding k_d -> Q_p, not merely a finite
precision approximation.

| p | Complete assigned list d:r |
| --- | --- |
| 7 | −110:3, −66:2, −55:1, −33:3, −10:2, −6:1, −5:3, −3:2, 2:3, 11:2, 15:1, 22:1, 30:3, 165:2, 330:1 |
| 13 | −165:2, −30:3, −22:2, −1:5, 3:4, 10:6, 55:4, 66:1 |
| 19 | −15:2, −2:6, 5:9, 6:5 |
| 29 | 33:2, 110:9 |
| 31 | −11:12 |
| 43 | −330:10 |

Fix any row d and its assigned p. Suppose F had a monic quartic
divisor h over k_d. Embed its coefficients into Q_p. The monic
polynomial F/275 has coefficients in Z_p. Every root of it is
integral over Z_p; the coefficients of both h and its monic cofactor
are elementary symmetric functions of such roots, hence are integral.
Since they lie in Q_p, they belong to Z_p. Reducing the factorization
therefore gives a monic degree-four divisor of f_p. Neither factor
loses degree because both are monic. This contradicts the complete
divisor-degree sets above. Thus there is no monic quartic divisor
over any of the 31 fields. This is an exact absence certificate for
each field, without any probabilistic inference.

It also proves the stated complete quadratic factorization degrees
[8]. Indeed, if k_d embedded into K, the minimal polynomial of theta
over k_d would be a monic degree-four divisor of F/275, since
[K:k_d]=4. No such divisor exists. Hence k_d is not a subfield of K;
the quadratic polynomial defining k_d remains irreducible over K,
so [Kk_d:K]=2 and [Kk_d:k_d]=8. Thus F is irreducible over k_d.
Every quadratic subfield of K was in the covering (1), so there are
none. The finite-field covering is sufficient; no algebraic
factorization package or uncertified irreducibility return value is
used as evidence.

### Exhaustion of partitions and generators

By L115's irreducibility, a root subset fixed as a set by G_Q is
empty or all of Omega. Both give the same zero class. For a
Galois-stable unordered partition that is not fixed half by half,
some element exchanges its halves. They must have equal cardinality,
so both have four roots. The imported theorem places the corresponding
monic quartic h over a quadratic subfield k of K. The preceding
complete absence proof excludes every such k and every such h.
It retains all complement-exchanged possibilities rather than taking
invariants before quotienting by complement.

Consequently the full partition list consists of {empty,Omega}, and
the branch-module isomorphism identifies it with {0} in J(Q)[2].
The empty list of nonzero generators generates exactly this entire
list; its order is one and its F_2-dimension is zero. The geometric
two-torsion still has order 2^6; its rational invariants are the
computed subgroup. No inference about higher torsion, Mordell–Weil
rank or rational-point completeness is made.

### Complete evidence, verification and limits

Run from the active notebook:

    python3 scripts/pair-genus-two/marked_jacobian_two_torsion.py
    python3 scripts/pair-genus-two/replay_marked_jacobian_two_torsion.py

The full producer evidence is
`scripts/pair-genus-two/marked-jacobian-two-torsion-certificate.json`;
all 122 producer checks pass. It retains the unchanged polynomial,
the actual field discriminant, all six complete modular products,
squarefreeness identities, all factor Frobenius residues, complete
division traces and Bezout identities, all factor-subset degrees,
and all 31 exact square-root/derivative witnesses.

The separate replay imports neither the producer nor its helper and
writes
`scripts/pair-genus-two/marked-jacobian-two-torsion-replay.json`.
All 1,520 checks pass without failures. It uses p successive
multiplications for Frobenius rather than binary powering, replays
every saved division and Euclidean identity, independently enumerates
the squarefree signed divisors, and checks every entire factor list,
degree obstruction, scalar and field-cover row. The full relevant
modular witnesses and full quadratic covering were inspected through
the bounded JSON inspector with --full for those selected fields.
This arithmetic replay is not the later critical mathematical audit.

The initial active Python lacked SymPy; an existing Python 2.7/
SymPy 0.7.4.1 interpreter supplied exploratory factor suggestions.
Neither that old package nor its claims are mathematical inputs.
The final producer and independent replay use only Python's standard
library and the producer's explicitly recorded L115 polynomial
arithmetic helper. No package was installed, no class backend was
retried, and no external source refresh was required. The exact
modular absence certificate replaces the optional Trager implementation
while staying inside the approved complete-factorization target.

This fixes one torsion term for a possible later descent. The full
S-unit and S-class two-torsion data, full descent/Kummer comparison,
rank, points on surviving covers, degree-nine distinguished-root
recovery, compatible remaining factors, both L095 integer systems and
minus-eleven remain unresolved. Known rational infinity points still
survive the curve-point descent. Trivial rational J[2] supplies no
rank or point bound and no exclusion of a Beal signature.

### Separate critical mathematical audit, 2026-10-24

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-24-marked-jacobian-two-torsion-critical-audit.md`.
The audit confirms the entire claim, including quadratic irreducibility,
with no mathematical correction and no new general theorem. Its work
record is `drafts/2026-10-24-marked-jacobian-two-torsion-audit.md`.
The full proof and both arithmetic implementations were reviewed;
audited L115/L116 are reused as inputs rather than re-certified here.
The following checks explain why the complete arithmetic evidence
proves the stated mathematical conclusion.

1. **Actual curve and invariant quotient.** L113's infinity chart has
   Z²=3025 at q=0, hence two smooth rational points Z=±55 and no
   branch point at infinity. Its eight finite branch points are simple.
   Thus the imported even-subset module applies to this genus-three
   curve, with its actual D_infinity. Multiplying F by 11 changes no
   branch root; no curve or Jacobian isomorphism to a different twist
   is asserted. Taking invariants of the quotient is essential:
   the invariant class is an unordered partition, not necessarily an
   invariant subset. Geometric two-torsion has dimension six, while
   the invariant subgroup is what is computed.

2. **Exchanged halves and the root field.** In the transitive action
   on the eight roots, a setwise invariant subset is empty or full.
   Otherwise an invariant unordered partition defines a nontrivial
   action on its two halves. Its kernel has index two. An element
   exchanging the halves cannot fix any root, because the halves are
   disjoint. Therefore the stabilizer of a chosen root lies in that
   kernel, so its quadratic fixed field embeds in that root's field
   K. The quartic product over the half containing that root has
   coefficients in this quadratic field; its conjugate is the other
   half. This checks the precise specialization of the cited
   exchanged-partition theorem, without a sampled Galois-group claim.
   It also covers every possible nonzero invariant class: an exchange
   forces equal sizes, hence size four, not two or six.

3. **Complete quadratic covering.** For a subfield k of K, each prime
   of k has a prime of K above it and ramification indices multiply.
   Thus a ramified rational prime of k must ramify in K. L116's
   maximal-field discriminant permits only 2,3,5,11. The quadratic
   discriminant formula then forces the squarefree radicand to be
   one of the signed divisors of 330, with 1 omitted. Conversely each
   such radicand has discriminant supported there. Unique squarefree
   radicands give 31 distinct fields, including both signs and −1;
   no reality assumption is used to shrink the list. The complete
   certificate list agrees with an independent divisor enumeration.

4. **Every arithmetic obstruction is complete.** Fresh execution of
   `python3 scripts/pair-genus-two/replay_marked_jacobian_two_torsion.py`
   passes all 1,520 comparisons with no failures. The six normalized
   products and all fourteen factors are retained. The full 48
   successive Frobenius residues, fifteen proper-index Bezout tests,
   six squarefreeness identities and every factor-subset degree were
   inspected and checked by the reviewed replay. For degrees 2,3,8
   the only required prime divisors of the degree are respectively
   2,3,2; for degree 6 both 2 and 3 are tested. Linear factors need
   no proper-index test. All products have degree eight, so no factor
   or multiplicity is omitted. The resulting degree sets, including
   duplicate degree positions, omit four in all six cases.

   The replay computes each Frobenius step by successive modular
   multiplications independently of the producer's binary-power
   traces. It checks the Bezout polynomial equality directly, so the
   mathematical gcd conclusion does not depend on interpreting a
   saved Euclidean trace as a linked algorithm execution. The traces'
   division identities are checked as additional evidence. Reading
   a saved final `order=1` or `factor_degrees=[8]` is not a proof of
   either value; those values follow from the implications here.

5. **Lifting, integrality and preservation of degree.** All 31 complete
   assigned rows have r²=d mod p and 2r nonzero mod p, for their
   certified odd primes. Hensel yields a Q-embedding k_d -> Q_p.
   Both 275 and the polynomial's leading monic coefficient are units
   there. Roots of F/275 are integral over Z_p, so the elementary
   symmetric coefficients of a monic quartic divisor and its monic
   cofactor are integral. Those coefficients lie in Q_p, and integral
   closedness puts them in Z_p. Their leading coefficients remain
   one after reduction. Thus a quartic divisor over k_d would produce
   an actual degree-four divisor of the complete reduction, contrary
   to step 4. This uses one split place for each entire quadratic
   coefficient field; it does not confuse residue splitting with a
   global factorization. Every field, including d=33 at 29 and d=−330
   at 43, has its own checked witness.

6. **Both final conclusions.** If a candidate k embeds in K, the
   minimal polynomial of theta over k has degree four by the tower
   formula and divides F/275. Step 5 excludes this. If k does not
   embed in K, its defining quadratic remains irreducible over K;
   hence [Kk:K]=2, [Kk:Q]=16 and [Kk:k]=8. Since k(theta)=Kk,
   F/275 is irreducible over k. This justifies the stronger [8] claim
   without inferring it merely from the absence of quartic divisors
   for an arbitrary reducible polynomial. No quadratic subfield of K
   exists, so step 2 excludes every exchanged class. Only empty/full
   remains, giving J(Q)[2]={0} with the stated empty generator list.

The full arithmetic evidence remains in the producer and replay paths
above; no sampled subset or bounded preview is the certificate.
The direct mathematical inputs remain unchanged; the additional Milne
inputs are precise standard citations, not new local nodes. This audit adds
neither a rank bound nor an identified full Kummer image. In particular
known rational infinity points survive, and all supported-class,
point-control and integer gaps listed above remain open. Mathlib
coverage remains not checked.

## Mathlib

Coverage of the full even-degree branch-module theorem and this exact
instance determination is **not checked**. No claim of absence is made.
The existing L115 finite-field references support the arithmetic
criterion, but no formalization or Lean verification is claimed.
