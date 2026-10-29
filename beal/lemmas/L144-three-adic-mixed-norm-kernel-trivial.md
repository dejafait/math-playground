# L144 — The norm-restricted mixed coefficient filter at 3 is vacuous

## Hypotheses

Let k=Q_3. Use the smooth proper curves of L110 and L111, base changed
to k, with their actual equations and rational base points

    Q4(T)=7+52T−6T²−64T³−25T⁴,
    B: W²=11(T²−4)Q4(T), q_+=(2,0),
    E: R²=−33Q4(T), O_E=(2,165).

Put A_4=k[T]/(Q4), with generator theta. Use the degree-zero divisor
evaluation convention of L143, specialized to k as justified below:

    lambda_B:Jac(B)(k) → V=A_4*/(k* A_4*²),
    lambda_E:E(k) → V.

In the elliptic map identify P with [P−O_E]. All divisor representatives
are moved off the quartic branches and the T-infinity fibers before
evaluation. Closed-point evaluations use the full residue-algebra norm.
There is no assumption about either complete local image, any global
class or unit basis, rank, point completeness or integer recovery.

## Conclusion

There is a complete local algebra decomposition A_4≅k×L, where L/k
is a totally ramified cubic extension with residue field F_3. The
well-defined norm map

    N:V → k*/k*²

is an isomorphism of two-dimensional F_2-vector spaces. In particular

    ker N={1},
    lambda_B(Jac(B)(k)) ∩ ker N={1} ⊆ lambda_E(E(k)).       (1)

Thus the proposed norm-trivial mixed-image test at 3 has no additional
content. This conclusion does not compute the full image on either
curve and does not assert a global mixed-image inclusion. It supplies
no rank improvement or Beal exclusion. This is a known-theory instance
specialization accepted by the separate conceptual audit below.

## Proof

### Imported local inputs and specialization of the interface

The pre-existing SPECIALIZE assessment is
`drafts/literature/2026-10-26-three-adic-mixed-image-nonredundancy.md`.
We use its approved Hensel/factorization and complete square-class
stage, with an upper bound on the entire ambient norm kernel rather
than a partial point search. Import the standard named simple-root
Hensel lemma over Z_3, and the fundamental equality e(L/k)f(L/k)=[L:k]
for a finite extension of nonarchimedean local fields. The finite
extensions here are separable of characteristic zero. The square
criterion reused by the assessment is: in a complete discretely valued
field with finite residue field of odd characteristic, a nonzero
element is a square exactly when its normalized valuation is even
and its normalized unit has square residue. No new proof of these
standard local-field results is needed.

For precise extension and degree references use J.S. Milne,
[*Algebraic Number Theory*, v3.08 (19 July 2020)](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
Proposition 7.31/proof p.120 (simple-root lifting), Theorem 7.38/proof
p.123 (unique extension and completeness), and Corollary 7.42/proof
with Remark 7.43 p.124 (degree formula and value group (1/e)Z).
The printed page numbers and hypotheses were checked in the prior
audit assessment. These results do not require tame ramification;
the cubic below is allowed to be wildly ramified at three.

For a precise source for the valuation/unit and Hensel square inputs
reuse Pete L. Clark, *Algebraic Number Theory II: Valuations, Local
Fields and Adeles*, 161-page author-hosted version accessed 2026-10-26,
[Proposition 2.20 p.72 and Theorem 2.24/proof p.73](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf).
Exercise 2.11 in those notes is not treated as a separately proved
theorem. The source assessment already covers Hensel/Newton
factorization for this exact algebra. Below a direct valuation check
establishes the cubic degree, so no numerical factorization or
approximate Newton slope is being assumed exact.

For the coefficient interface import Bruin–Poonen–Stoll,
*Generalized explicit descent and its application to curves of genus 3*,
Forum Math. Sigma 4 (2016), e6, DOI 10.1017/fms.2016.1,
[74-page author manuscript](https://math.mit.edu/~poonen/papers/genus3.pdf),
Remark 6.5/Definition 6.7 p.16 and Section 6.3/Proposition 6.10
pp.17–20, with the all-class cycle check of L143. These statements
allow a base field k, n invertible in k and a finite nonempty étale
branch scheme. Here n=2, k=Q_3 and Q4 is separable by L110, so those
hypotheses hold. The divisor identities and equivariant finite pairing
checked in L143 persist under base change. Both base points remain
k-rational and Q4(2)=−825≠0. The rational-point case of Schaefer,
*Computing a Selmer group of a Jacobian using functions on the curve*,
Math. Ann. 310 (1998), 447–471,
[corrected arXiv:1507.08325v1, Proposition 2.7/proof pp.9–10](https://arxiv.org/pdf/1507.08325v1),
includes completions. Every k-rational Jacobian class therefore has
a k-rational degree-zero divisor representative; the moving result
avoids the finite bad supports. The comparison and the diagonal
coefficient exact sequence give well-defined evaluation maps to V,
just as in L143. No assertion about all of H¹(k,ker G) is needed.

If using L138's odd model, its identity

    X−eta=−c(T−theta)/((T−2)(theta−2)),
    c=−36300, eta=c/(theta−2),

holds over k without changing constants. Move the divisor also off
T=±2 when evaluating the full odd-model tuple. On a degree-zero
divisor the constant evaluates to one and the T−2 denominator to
a k-scalar. Thus the projected quartic evaluation agrees in V;
the odd-model rational component is not erased in its own full map.
This checks the coordinate convention but is not needed to enumerate
the local images in the argument below.

### Exact local factorization

Set alpha=25theta. Direct coefficient comparison gives

    g(U)=U⁴+64U³+150U²−32500U−109375,
    g(25T)=−25³Q4(T).

Since 25 is invertible in k, these changes give inverse algebra
isomorphisms. Put s=alpha−1. The complete shifted polynomial is

    p(s)=g(1+s)=s⁴+68s³+348s²−32004s−141660.            (2)

Its coefficient valuations in increasing degree are (2,2,1,0,0).
Its reduction is s³(s−1). At s=1 one has p(1)≡0 mod 3 and
p'(1)≡1 mod 3. Hensel's lemma gives an exact r∈1+3Z_3 with
p(r)=0. Synthetic division over Z_3 gives

    p(s)=(s−r)h(s),
    h=s³+(68+r)s²+(348+68r+r²)s
                     +(−32004+348r+68r²+r³).            (3)

Reducing (3) gives h≡s³ mod 3, and h(r)≡1 mod 3. In particular
the two factors are coprime. The certificate's twelve lifted digits
and approximate factorizations check (2) and this construction; it is
Hensel's lemma, not the finite precision data, that gives exact r.

For every root beta of h in an algebraic closure, write t=v_3(beta).
Since h is monic integral its roots are integral: a negative valuation
would make its leading term uniquely least. Its reduction s³ then
excludes t=0, so t>0. The valuations of the five terms of p(beta),
in increasing degree, are

    2, 2+t, 1+2t, 3t, 4t.

If 0<t<2/3, the cubic term has uniquely least valuation: subtracting
3t gives (2−3t,2−2t,1−t,0,t), with every other entry positive.
If t>2/3, the constant term is uniquely least: subtracting 2 gives
(0,t,2t−1,3t−2,4t−2), with every other entry positive. Either
case contradicts p(beta)=0 in a nonarchimedean field. Hence t=2/3.

No beta can belong to k, whose nonzero valuations are integers.
A reducible cubic over a field has a root there, so h is irreducible.
Let L=k(beta). Its degree is three, and its ramification index is
divisible by three because its value group contains 2/3. The local
fundamental equality gives e=3 and f=1, with residue field F_3.
For example pi=beta²/3 has normalized L-valuation one. The exact
coprime factorization (3) and the Chinese remainder theorem now give

    A_4≅k[s]/p≅k×L.

This proves the complete factorization, rather than just a mod-3
factor pattern; no claim about a monogenic maximal order is used.

### Complete square classes and the scalar quotient

The odd-residue square criterion gives |k*/k*²|=|L*/L*²|=4.
In k the classes [3],[-1] form a basis. In L the element 3 has
normalized valuation three, hence odd, and −1 has nonsquare residue
2 in F_3. Their classes are likewise a basis of L*/L*². Thus
restriction k*/k*²→L*/L*² is an isomorphism, with precisely those
actual rational representatives; neither valuation nor unit bits
have been discarded. Cubic norm sends a rational d to d³, so on
these bases it is the inverse isomorphism.

It follows that every class in A_4*/A_4*² has a representative
(a,b) with a,b∈k*. The full diagonal scalar image consists of
(d,d), and has dimension two. Dividing by (a,a) gives the unique
normalized form (1,b/a) at the level of square classes. The quotient
V consequently has dimension two, with all four classes represented
by (1,1), (1,3), (1,−1), (1,−3).

Algebra norm is well-defined on V: multiplying by a scalar d
multiplies its norm by d⁴, a square. Moreover

    N_(A_4/k)(a,b)=a N_(L/k)(b)=a b³,
    [a b³]=[b/a] in k*/k*².                             (4)

Hence norm is exactly the above normalized-coordinate isomorphism,
not merely a rank estimate or a necessary local condition. Its kernel
is the identity. The complete sixteen-row raw square-class table
also records all diagonal orbits and verifies (4).

### Image comparison and stopping decision

Every norm-trivial lambda_B class lies in the just-computed entire
ambient kernel, so it must be 1. Conversely lambda_B(0)=1. The
elliptic identity has good support and lambda_E(O_E)=1, by evaluating
the zero divisor. Thus (1) follows. The actual point equation is
165²=−33Q4(2)=27225, so this is an available representative on
the actual elliptic twist, with the actual origin.

No upper bound for E's full point image or enumeration of B's full
Jacobian image is needed: the ambient norm kernel supplies a stronger
upper bound on the particular B slice being compared. This is why
zero elliptic recursion cells and zero B-witness searches suffice;
it is not an inference of containment from deficient samples. This
shortcut is entirely within the approved full factorization, diagonal
square-class and norm-comparison stage. It stops the proposed extra
local filter at 3, rather than enlarging the workload or changing target.

The same-T redundancy in ATTEMPTS/062 is a different argument; here
the two local divisor-class images are separate. Neither the saturated
real/11-adic filters nor L139–L141 enter the proof. No class is removed
from their supported global group. Full descent, mixed global conditions,
Abel-image membership, point control, integer recovery and the residual
Beal signatures remain independent unresolved obligations.

### Exact certificates and verification limits

Run `python3 scripts/pair-genus-two/three_adic_mixed_image.py` and
`python3 scripts/pair-genus-two/verify_three_adic_mixed_image.py`.
Full evidence is in
`scripts/pair-genus-two/three-adic-mixed-image-certificate.json` and
`scripts/pair-genus-two/three-adic-mixed-image-verification.json`.
The producer passes 59 checks and the independent replay 74, with
empty failure lists. The replay imports no producer code. It reconstructs
the polynomial shift by a different expansion, checks every saved
lift/factor coefficient, and computes every norm/scalar orbit using
rational representatives rather than the producer's bitwise table.

Actual/required raw classes are 16/16, quotient classes 4/4 and
norm-trivial classes 1/1. Required/certified elliptic representatives
for this restricted comparison are 1/1. The elliptic workload caps
4096 cells and depth 24 are unused, with no unfinished frontier.
These finite checks do not replace the Hensel, irreducibility,
ramification, square-class completeness or base-change arguments
written above. Arithmetic replay alone does not establish the separate
conceptual audit recorded next.

### Separate conceptual critical audit — 2026-10-27

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-26-three-adic-mixed-norm-kernel-audit.md`.
Its TARGET exactly matches this turn's initial Next action. The audit
accepts the stated decomposition, complete norm isomorphism and (1),
without changing the hypotheses or conclusion. This is REPRODUCTION:
verification of a local instance of the cited theory, with no new
general theorem or progress beyond the checked methods.

**Exact field, rather than finite precision.** Direct expansion checks
both polynomial changes, and p(1)=−173247, p'(1)=−31100 give the
simple mod-3 root. Milne's Proposition 7.31 supplies the exact compatible
root r; twelve digits alone would not suffice. Since r is integral,
the synthetic cubic has integral coefficients, reduction s³ and
h(r)≡1, so the two exact factors are coprime. For an h-root beta,
monic integrality excludes negative valuation; reduction s³ excludes
valuation zero, even in an enlarged residue field. For 0<t<2/3 the
four differences from the cubic term are 2−3t, 2−2t, 1−t, t, all
strictly positive. For t>2/3 the differences from the constant term
are t, 2t−1, 3t−2, 4t−2, again strictly positive. Thus t=2/3 is
necessary for every h-root. In particular no root is in Q_3, and a
cubic without a base-field root is irreducible. Its extension is
separable in characteristic zero. Milne's Theorem 7.38 and degree
formula now apply: 2/3 in (1/e)Z forces 3|e, and ef=3 forces e=3,
f=1. With normalized valuation w=3v_3, w(beta²/3)=4−3=1.
The extension is complete with residue F_3, exactly as required by
the odd-residue square criterion. No unproved maximal-order claim,
tameness assumption or inference of irreducibility from reduction
alone is hidden in this step.

**All scalar and square classes.** Over L the classes of 3 and −1
are independent: an odd power of 3 has odd w-valuation, whereas
−1 is a unit with nonsquare residue. If the valuation exponent is
even, its rational power of 3 is already a square, leaving exactly
that unit test. The complete square criterion gives four classes,
so these two independent classes exhaust them. The same argument
over k gives the same basis. Hence every L square class has an
actual rational representative, not merely two formal bit labels.
The diagonal scalar subgroup in the product has exactly four
elements, and every orbit has the unique first-coordinate-one
representative (1,d). All four possible d occur. Norm of (1,d)
has class [d³]=[d], and a diagonal scalar has norm d⁴, so the
induced norm is well-defined and bijective. The sixteen-row table
tests every raw pair and all four scalar orbits. It corroborates
the complete mathematical argument; it does not establish the
local-field square criterion by enumeration.

**Every local class and the actual origin.** L143's accepted finite
pairing and divisor identities hold over an algebraic closure and
are Galois-equivariant; base changing to k preserves those identities
and the actual maps. The finite branch algebra is étale and 2 is
invertible. Schaefer's Proposition 2.7, rational-point case including
completions, applies to q_+ and O_E over k. Every Jacobian class has
a k-rational degree-zero divisor; the moving result in Bruin–Poonen–
Stoll Remark 6.5 moves it off the prescribed finite supports. A closed
point contributes the full norm of its residue algebra after tensoring
with A_4. Thus the coefficient comparison and injection of Proposition
6.10 apply to all local classes, not only point differences. One must
not transport L143's absence of rational quartic branches over Q to
Q_3: the linear factor here does give a Q_3-rational branch. Movement
handles that class as well, so this observation causes no exception.
The zero divisor is already good and gives both lambda_B(0)=1 and
lambda_E(O_E)=1. The equation at O_E is checked on the actual twist;
there is no replacement of the infinity fiber by 2O_E. The optional
L138 coordinate conversion is not required by this containment proof.

Consequently the entire norm-trivial B slice is the singleton {1}
and the actual elliptic origin supplies it. Bounding that slice by
the *entire ambient* kernel is sufficient, independently of either
full local image. The unused recursion caps do not conceal a missing
frontier or turn a sample into exhaustion. This establishes the local
stop in ATTEMPTS/063, with no global pruning, Abel-image sufficiency,
point control or integer recovery. The rank bound remains at most
7+c<=9, eight above the sufficient threshold one.

**Evidence replay.** Reran both displayed commands and inspected both
script implementations, all twelve complete lift records, all symbolic
valuation differences, every raw square-class row, every independently
replayed scalar orbit, both result objects and every check flag. Actual/
required counts are 16/16 raw classes, 4/4 quotient classes, 1/1 kernel
classes and 1/1 required elliptic representatives. The producer passes
59 checks and the replay 74, with no failures. The replay imports no
producer code; its independent arithmetic and binding checks pass.
The full producer certificate SHA-256 is
`e91e357f31f4e136e032ac59602c3ad243e62c0c9164b09e1c6ace705df21101`;
the full verification SHA-256 is
`c285c434f4a03ea58ff15c250009dd269904f8add836de3a49b60273f512c70e`.
The conceptual claims above were checked separately from those finite
certificates. No DAG inputs change: L139–L141 and the stopped same-T
construction are comparisons, not mathematical premises of (1).

## Mathlib

Full matching coverage of this local product-algebra norm-kernel and
mixed evaluation comparison has not been checked. Supporting Hensel,
local ramification and square-class theorem names were not searched.
Unknown availability is not evidence of absence; no Lean verification
or new general descent theorem is claimed.
