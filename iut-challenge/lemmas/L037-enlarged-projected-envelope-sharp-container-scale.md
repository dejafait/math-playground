# L037 — Enlarged projected envelope sharp container scale

## Hypotheses

Let L=Q_3(zeta_20,pi), where zeta_20 has order 20 and pi^27=3.
Put O=O_L, J=log(O^times), V=ker(Tr_(L/Q_3)),
M=J intersect V, C=O intersect V and T=(pi J/6) intersect V.
Use the genuine complete logarithm and exactly the admitted presentation
and reciprocity-defined finite-word reference subgroup Gamma of audited
L036. In particular Gamma preserves M and V and fixes the actual
primitive y_1 pointwise. Its words use only the paired/adjacent generators
and their inverses; no larger group or extra action is admitted.

Set W=Q_3 y_1, H=V/W, q:V->H, P=q(M), N=q(C) and D=q(T).
Audited L035 supplies full rank-106 lattices P,N in the same H and
P=M/(Z_3 y_1). Audited L034 supplies the complete relative Smith
exponents of C in M, increasingly ordered:

    alpha = -1 (36 times), 0 (48), 1 (16), 2 (7).

Audited L036 supplies the embedded ordinary finite-sum identity

    S = sum_(h in Gamma) Z_3 h(D) = 3^(-4) P.

The sum uses finite words and finite sums, without taking a closure.
These three audited local results are mathematical inputs; their
certificates and analytic arguments are not recomputed here.

Import **John Voight, Quaternion Algebras**, GTM 288 (2021), chapter 9,
section 9.3, **Theorem 9.3.9**
([primary chapter](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_9))
for simultaneous relative factors of full lattices over the DVR Z_3,
without a nesting hypothesis. Import **Peter Bürgisser, Avinash Kulkarni
and Antonio Lerario, Nonarchimedean integral geometry**, Selecta
Mathematica **32:10 (2026)**, version of record **5 January 2026**,
**section 2.2**, pp. 13–14, **Definition 3.1.3 and Lemmas 3.1.4/3.1.5**,
pp. 22–23, and **Propositions 4.1.1/4.1.2**, pp. 35–36
([publication](https://doi.org/10.1007/s00029-025-01120-y),
[primary PDF](https://d-nb.info/1395945926/34)). These supply quotient
lattices, Smith integrality and target-only interlacing over Q_3/Z_3.
The minimax self-reference in the interlacing proof is understood as
Proposition 4.1.1; Corollary 4.1.3 is not used. Reuse the approved
source assessment rather than reprove these general theorems.

No field coordinates of y_1, O_U-linearity, quotient field valuation,
orbit-set equality or original-IUT numerical prescription is assumed.

## Conclusion

For each admitted presentation, the least integer k satisfying

    h(q(T)) subset 3^(-k)q(C) for every finite word h in Gamma

is **k=6**. Every such image is contained in q(C)/729, and there
exist an actual finite word h in this same Gamma and an actual t in T
such that

    q(h(t)) not in q(C)/243,
    equivalently h(t) not in 3^(-5)C + W.

The threshold and existential failure at the preceding scale are uniform
over admitted presentations; the spaces, lattices, word and point may
depend on the presentation. No explicit escaping word or point is given.

This is a **REPRODUCTION** specializing the checked lattice methods,
validated by the separate critical audit below. It quantifies the auxiliary projected
container comparison; it supplies no result beyond those known methods,
field radius, fixed-line control, actual/native input/action realization
or essential IUT flaw. The original finite B>=A gap remains open.

## Proof

### The largest relative factor survives the actual quotient

Apply the cited target-only interlacing to the identity from (V,C)
to (V,M), quotienting the target only by the one-dimensional W.
L034's proof identifies the 106 nonzero factors of the resulting
surjection q:(V,C)->(H,P) with the relative factors of its image
N=q(C) in P. This follows from its rectangular Smith form, whose
remaining domain column is zero; it does not quotient both lattices
by an arbitrarily chosen integral line or select a complement of C.

Write these exponents in increasing order as beta_1,...,beta_106.
The singular values are 3^(-alpha_i) and 3^(-beta_i), respectively.
Thus the cited inequalities, after applying the decreasing function
-log_3, give

    alpha_i <= beta_i <= alpha_(i+1), 1<=i<=106.

In particular alpha_106=alpha_107=2 gives beta_106=2. Every beta_i
is at most 2. Both original terminal factors are needed: simply
projecting an unprojected extreme would not justify its survival.
This holds for every rational line W, hence for every actual admitted
line, without assuming the converse realization of arbitrary lines.

### Embedded containment and the exact integer threshold

By the cited DVR normal form there is a basis e_1,...,e_106 of P with

    N = direct-sum_(i=1)^106 3^(beta_i) Z_3 e_i.

Diagonal unit factors have been absorbed into this description; they
do not change the Z_3-submodules. For any integer r, including negative
r, coordinatewise containment therefore gives

    3^r P subset N  iff  r>=beta_i for every i  iff  r>=2.

Indeed containment in coordinate i is 3^r Z_3 subset
3^(beta_i)Z_3, which holds exactly when r>=beta_i. In particular
9P is contained in N and 3P is not. For example e_106 in this
normal form satisfies 3e_106 not in N. This is an auxiliary lattice
basis witness, not a prescribed field-coordinate input or source word.

For each integer k, 3^(-k)N is a Z_3-module. All finite-word images
h(D) lie in it if and only if their ordinary finite Z_3-sum S lies
in it: one implication uses closure under finite integral linear
combinations, and the reverse uses h(D) subset S. Audited L036 now gives

    S subset 3^(-k)N
    iff 3^(k-4)P subset N
    iff k-4>=2
    iff k>=6.

All scalar multiplications here are rational and take place inside
the same H. This proves the least-integer assertion and the enclosing
scale 3^(-6)N, without identifying the orbit set with S or giving H
a field valuation.

### Failure at the preceding scale returns to an actual input

Let s=3^(-4)e_106. L036's equality puts s in S, while
3^5 s=3e_106 not in N proves s not in 3^(-5)N. By the ordinary
finite-sum definition of S there is a finite expression

    s=sum_(j=1)^m a_j h_j(d_j),
    a_j in Z_3, h_j in Gamma, d_j in D.

If every h_j(d_j) belonged to 3^(-5)N, this finite sum would also
belong to that Z_3-module, a contradiction. Hence some h_j(d_j)
does not. Since D=q(T), choose an actual t_j in T with q(t_j)=d_j.
The word h_j acts on V and fixes W, so its quotient action satisfies
h_j(q(t_j))=q(h_j(t_j)). This supplies the promised actual T-point
and actual finite word, without any limiting action. It is the same
finite-sum containment argument used in L026, with no imported
different-field valuation bound or orbit theorem.

Finally q inverse of 3^(-5)q(C) is exactly 3^(-5)C+W: equality
q(v)=3^(-5)q(c) is equivalent to v-3^(-5)c in W. This proves
the stated lift formulation. The argument supplies existence for
each presentation, not one common word/point for all presentations.

The continuation test succeeds without hidden line coordinates.
Fixed-line control, actual/native input/action compatibility,
packet/global realization, pilot transport, essentiality and the
original finite B>=A comparison remain independent unresolved gaps.
The stops in ATTEMPTS/020,022–024 remain intact. Neither a rational
container dilation nor an auxiliary-envelope point is asserted to be
an original IUT numerical bound or actual ind3 input.

### Separate critical audit, 2026-10-10

The independent audit validates the conclusion under the unchanged
hypotheses. It reuses the approved source assessment and the audited
statements and proofs of L034–L036. No general theorem is reproved and
no error requiring mathematical repair is found. In particular the
audit imports L036's embedded ordinary finite-sum equality, not an
equality between an orbit set and a lattice. Its finite matrix and
infinite-logarithm inputs remain those already audited there; no new
certificate verification is claimed or needed for this deduction.

First fix one admitted presentation. L035 puts P and N in the same
106-dimensional rational H and identifies the action as the actual
quotient action. Apply the cited target-only interlacing theorem to
the rank-107 identity (V,C)->(V,M), followed by q. Its kernel has
dimension one, so the surjection has 106 nonzero Smith factors. In
rectangular Smith form, integral changes of the 107 domain generators
preserve their full image; the 106 nonzero columns generate N and the
remaining column is zero. Thus the projected factors describe N in P,
not P in N, and not a simultaneous deletion of one coordinate from
two independently chosen bases. No nesting hypothesis is used.

The original singular values are 3^(-alpha_i) in descending order.
The source inequality
3^(-alpha_i)>=3^(-beta_i)>=3^(-alpha_(i+1)) therefore gives
alpha_i<=beta_i<=alpha_(i+1). The multiplicities in L034 sum to
107, with indices 101 through 107 all equal to 2. In particular
alpha_106=alpha_107=2, so beta_106=2, while every beta_i<=2.
This conclusion uses a repeated terminal factor, rather than assuming
that a particular vector survives projection. It holds for every
rational W, and hence for the actual W of each presentation. It does
not assert that every rational line is source-realizable.

In a simultaneous basis of P and N, the inclusion 3^r P subset N
requires r>=beta_i in every coordinate. Both necessity and sufficiency
follow from 3^r Z_3 subset 3^(beta_i)Z_3 iff r>=beta_i, for any
integer r. Consequently 9P subset N and 3P not subset N. In the
last coordinate, 3e_106 has coefficient of valuation 1 where N
requires at least 2. This checks the reverse-containment direction
and excludes confusing the largest exponent with the smallest.

For every integer k the scaled N is a Z_3-module, so containment
of all h(D) is equivalent to containment of their ordinary finite
span S. Multiplication by 3^k, an invertible scalar on H, changes
S=P/81 subset N/3^k into 3^(k-4)P subset N. The exact condition
is k-4>=2. Thus k=6 succeeds and k=5 fails; the same criterion
also excludes every smaller integer, including negative integers.
No topological closure or extra group action enters this equivalence.

For attainment, s=e_106/81 belongs to the embedded S by L036,
whereas 3^5 s=3e_106 does not belong to N. Membership in S means
an actual finite expression sum a_j h_j(d_j) with a_j in Z_3,
h_j a finite word and d_j in D. If each h_j(d_j) lay in N/243,
module closure under these coefficients and finite addition would
put s there too. Hence at least one unscaled term escapes. This
argument does not require a coefficient to be a unit and does not
replace a finite expression by a convergent infinite sum. Each d_j
lifts to an actual t_j in T by the definition D=q(T). Since the
same h_j preserves V and W, equivariance gives
h_j(d_j)=q(h_j(t_j)). Finally the kernel of q is the rational W,
so q^(-1)(N/243)=C/243+W, as claimed. The lift belongs to the
specified auxiliary T, with no assertion of actual ind3 membership.

All choices in this check were made after fixing a presentation.
The input factors and scalar level hold for every admitted presentation;
the proof therefore establishes “for each presentation there exist h,t”.
It does not interchange these quantifiers or produce a common word,
point, complement or field-coordinate basis for all presentations.

The continuation test passes. This is verification of the existing
local specialization, not a new mathematical result beyond the sources
checked. It supplies no quotient field valuation, sharp full-space
field radius, actual/native compatibility or original finite B>=A
comparison. The independent gaps and stopped mechanisms stated above
remain unresolved. Direct inputs remain L034, L035 and L036; L026
is only the already noted methodological precedent, not an additional
theorem needed in the deduction.

## Mathlib

Full matching enlarged projected-envelope sharp-container theorem:
**not checked**. Supporting relative Smith factors, quotient-only
interlacing, quotient lattices and finite module containment:
**not checked**. Precise primary citations and the complete local
specialization are given above. Unknown coverage is not evidence of
absence; no formal verification or complete IUT resolution is claimed.
