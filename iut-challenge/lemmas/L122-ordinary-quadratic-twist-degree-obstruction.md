# L122 — Ordinary quadratic twists cannot generate the retained normal closure

## Hypotheses

Fix the single original elliptic curve E/Q supplied by L118, and fix
one ordering o. Retain L090's fixed algebraic closure, literal Legendre
curve E_o and fields

    G_o=Q(t_o)(iota,E_o[15]), iota^2=-1,
    M=Q(E[60]), C_o=G_o^nor over Q.

L118 retains a survivor in the sense of L090: the original E has full
level-120 image and j(E) is neither 0 nor 1728. Use L090's actual
joint image Gal(M/Q)=GL_2(Z/4) x GL_2(Z/15), and L092's audited
degree [C_o:Q]=1105920. Normal closures are in the fixed closure.
Every division field here adjoins both coordinates of every geometric
torsion point. Let E'/Q be any pointed quadratic twist of this E,
including the trivial twist. No factorization of its quadratic
character through Gal(M/Q) is assumed.

## Conclusion

For every such E',

    [Q(iota,E'[30]):Q] <= 552960 < 1105920 = [C_o:Q].

In particular C_o cannot equal Q(iota,E'[30]) as an embedded field
for any of these twists. The upper bound is sufficient, not asserted
sharp. This rules out this ordinary rational-descent explanation of
the retained normal closure. It supplies no verdict on other enlarged
fields, complete initial data, native pilot identification, the original
finite B>=A, or an essential IUT flaw. The separate step507 critical
audit below validates this specialization without strengthening it.

## Proof

### Approved scope and known inputs

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-26-ordinary-descent-division-field-test.md`.
The approved test first seeks a uniform strict degree obstruction;
only an inconclusive comparison would require fixing-kernel analysis.
L091's different nonnormality obstruction concerns G_o, not C_o.
The scoped duplicate check found no existing local twist/core verdict.
ATTEMPTS/031,035–036 remain preserved and are not reopened.

Import these previously inspected results in precisely this scope:

- Sutherland, MIT 18.786, [Lecture 21, 6 May 2024](https://math.mit.edu/classes/18.786/2024/LectureNotes21.pdf),
  section 21.2, p.2: over a perfect field, pointed twists of an
  elliptic curve with j different from 0,1728 are classified by
  quadratic characters; over Q they have representatives with nonzero
  rational quadratic twisting parameter, including the trivial class.
  Characteristic is zero here.
- Gonzalez-Jimenez, Lozano-Robledo and York,
  [arXiv:2408.04159v1, 8 August 2024](https://arxiv.org/pdf/2408.04159v1),
  Lemma 3.4(1), pp.12–13 and its coordinate-map proof: for a number
  field, a nonsingular short equation, nonzero twisting parameter d
  and N>2, the full division field of its quadratic twist is contained
  in the original full N-division field with sqrt(d) adjoined.
  Only this containment is used, not part (2)'s stronger equality.
- Sutherland, [Lecture 20, 1 May 2024](https://math.mit.edu/classes/18.786/2024/LectureNotes20.pdf),
  section 20.1, pp.1–2, and Yvon,
  [arXiv:2407.14370v1, 19 July 2024](https://arxiv.org/pdf/2407.14370v1),
  Introduction p.2: the full N-division field is fixed by the kernel
  of the full torsion representation. Finite Galois degrees are image
  orders, as also in Milne, *Fields and Galois Theory*,
  [v5.10, September 2022](https://www.jmilne.org/math/CourseNotes/FT.pdf),
  Theorem 3.17, pp.39–40.

The calculation below specializes these known inputs and the audited
ambient/core degree to this same witness. No general twist theorem
is reproved and no originality beyond these sources is claimed.

### The original full level-30 degree

Put N=Q(E[30]). The restriction of L090's actual full level-60
representation is its reduction modulo 30. By the Chinese remainder
theorem this is

    GL_2(Z/4) x GL_2(F_3) x GL_2(F_5)
      -> GL_2(F_2) x GL_2(F_3) x GL_2(F_5).

It is onto: any entrywise lift modulo four of an invertible matrix
modulo two has odd determinant and is invertible modulo four; the
other factors are unchanged. Thus the actual level-30 image is the
whole GL_2(Z/30), not a product inferred merely from marginal images.
By the full-coordinate kernel convention and Galois correspondence,

    [N:Q]=|GL_2(F_2)| |GL_2(F_3)| |GL_2(F_5)|
         =6*48*480=138240.

Here the factor orders are L092's independent-column counts
(p^2-1)(p^2-p); no additional arithmetic image assumption is used.

### Arbitrary twist and iota

The original monic equation in L090 has a nonsingular short equation
over Q: substituting x=X-c/3, where c is its quadratic coefficient,
removes the quadratic term. This is a pointed Q-isomorphism with
inverse over Q. It preserves the embedded full torsion coordinate
field, since both maps are defined over Q and carry the entire torsion
sets bijectively. Thus the cited short-equation containment applies
to this original E without replacing its division fields or assuming
E_o is Q-isomorphic to E.

By the nonexceptional-j classification, for E' choose a representative
quadratic parameter d in Q^*. A Q-isomorphism to that representative
likewise preserves its full torsion coordinate field. Lemma 3.4(1),
with base Q and torsion level 30>2, therefore gives in the fixed closure

    Q(E'[30]) subset N(sqrt(d)).

Consequently, writing J=N(sqrt(d),iota),

    Q(iota,E'[30]) subset J,
    [J:N]=[J:N(sqrt(d))]*[N(sqrt(d)):N] <= 2*2=4.

Each inequality follows from the polynomial X^2+1 or X^2-d over the
field in question. No independence of the quadratic extensions,
membership of sqrt(d) in M, or character factorization is required.
Tower degrees give

    [Q(iota,E'[30]):Q] <= [J:Q] <=4*138240=552960.

L118 retains the same survivor and literal fields to which L092
applies, so [C_o:Q]=1105920=2*552960. This is strictly larger than
the bound for every E'. Equality of embedded finite fields would
force equal absolute degrees, proving the conclusion. The degree
test succeeds, so actual fixing-kernel comparison is unnecessary.
There is no inference of equality from equal degrees or abstract
groups, and no assumption of normality of G_o. The numeric gap is
for this ordinary-twist proposal, not the original IUT comparison.

### Separate critical audit — 2026-10-26, step507

**Scope and verdict.** The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-26-ordinary-twist-degree-critical-audit.md`.
The exact uniform obstruction passes without correction. This is an
audit of a known-method specialization, not new general mathematics.
Use the cited classification, containment and finite Galois inputs;
Lemma 3.4(2)'s stronger equality is neither needed nor imported.

**The retained witness.** L118 selects a good member of L117's fixed
lattice once, before ordering and prime selection. Its good-pair
condition retains L089's original full level-120 and level-seven
images. L090 applies to every such survivor, not just an earlier
existential example. Its calculation gives 0<j(E)<1728 and the full
joint level-60 image on this same original Q-curve. L118's literal
definitions of G_o and C_o are exactly L090/L092's; no subsequent
place section, cover, stable model or theta assembly is used here.
L092's separately audited absolute degree is 1105920 for each of the
six orderings. Its relative degree or the source constants are not
substituted for that absolute degree.

**Restriction and degree.** In characteristic zero, multiplication by
two maps E[60] onto E[30]. For a compatible basis its Galois action is
the reduction modulo 30 of the level-60 matrices. Thus the restriction
of the actual joint image, rather than separate marginal images,
computes Gal(Q(E[30])/Q). CRT reduces the mod-four factor to mod-two
and leaves the mod-three and mod-five factors unchanged. Any lift of
an invertible mod-two matrix has odd determinant, hence is invertible
modulo four. The restriction is therefore onto the displayed product.
The independent-column orders are (4-1)(4-2)=6,
(9-1)(9-3)=48 and (25-1)(25-5)=480, giving
6*48*480=138240. Full coordinates are essential to the kernel/field
correspondence used in this calculation.

**Models and all twists.** The original equation is
y^2=x^3+c x^2+d x+e, with rational coefficients. The change
x=X-c/3, leaving y unchanged, and its inverse are Q-defined pointed
isomorphisms to a nonsingular short equation. On finite torsion
points the coordinate formulas in both directions are rational over
Q, so the embedded fields generated by all coordinates coincide;
the origin is rational and adds no coordinates. More generally, a
pointed Q-isomorphism of elliptic curves maps the entire N-torsion
bijectively and preserves its field of definition, equivalently the
kernel of its Galois action. The cited perfect-field classification
applies since Q has characteristic zero and j(E) is nonexceptional.
Every pointed quadratic twist under consideration has a representative
with a nonzero d in Q; rational isomorphisms to that representative
preserve the full torsion field. The letter d in this sentence is
the twisting parameter, independent of the original cubic coefficient.
The trivial class is included by a square parameter.

For this representative, the number-field, nonsingularity and N>2
hypotheses of Lemma 3.4(1) hold with base Q and N=30. Its containment
places the full twist field inside N(sqrt(d)) in the fixed closure.
This argument does not place sqrt(d) in M: it works equally for any
quadratic character outside the level-60 quotient. Adjoining sqrt(d)
has degree at most two over N, and adjoining iota thereafter has
degree at most two, by their respective quadratic polynomials.
They can be dependent or already present. The intermediate field
Q(iota,E'[30]) lies inside J=N(sqrt(d),iota), so the tower law gives
its absolute degree at most 4*138240=552960. Comparing with the
unchanged absolute degree 1105920=2*552960 proves strict inequality
uniformly in the twist and ordering. No embedded-field inclusion
between this twist field and C_o is required for the inequality to
exclude equality.

**Limits of the verdict.** The audit does not classify non-Q descents,
other enlarged fields or alternate repairs. In particular it supplies
no mandatory-hypothesis or essentiality argument connecting this
ordinary-twist exclusion to a flaw in IUT. Full initial data,
directed (*), native action/factorization/pilot and finite B>=A
remain open. No direct mathematical input or DAG edge changes.

## Mathlib

Coverage for this full specialization has not been checked. No claim
of a matching theorem, absence from Mathlib, or formal verification is
made. The cited full-torsion, twisting and Galois inputs above are the
mathematical references used here.
