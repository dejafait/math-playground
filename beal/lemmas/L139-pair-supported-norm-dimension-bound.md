# L139 — Supported ambient dimension and a coarse Jacobian rank bound

## Hypotheses

Use audited L138's smooth proper curve B over Q, its monic squarefree
quintic model Y²=G(X), and its actual factorization

    G=(X−9075)H,
    H=X⁴−67760X³+1581228000X²−15306287040000X
      +52615361700000000.

H is irreducible and L=Q[X]/G is identified in L138 with Q×K and
with maximal integer ring Z×O_K. In particular this is the same
quartic field and maximal order used in audited L135 and L137, not
merely a field with matching discriminant. Let J=Jac(B).

Put S_0={2,3,5,11}, and let S_K contain every finite prime of K above
S_0. Allow every archimedean place, with no sign condition. Use L135's
signature (r_1,r_2)=(4,0), L137's complete enumeration |S_K|=7 and its
ordinary localized class bound

    c=dim_F2 Cl(O_K[1/330])/2Cl(O_K[1/330]) <= 2.

For a field F and its indicated finite support, F(S,2) means the
classes in F*/F*² whose finite valuations outside support are even.
Use L138's corresponding product group L(S,2) and its Jacobian
Kummer-image containment in the product norm kernel. No unit
generators, complete class presentation, local-image computation, GRH
or assumption on Sha is made.

## Conclusion

The dimensions, with c as defined above, are

    dim_F2 Q(S_0,2) = 5,
    dim_F2 K(S_K,2) = 11+c <= 13,
    dim_F2 L(S,2) = 16+c <= 18,
    dim_F2 ker(N:L(S,2) -> Q*/Q*²) = 11+c <= 13.

The norm image is exactly Q(S_0,2); this is a split surjection onto
that supported group. Also dim_F2 J(Q)[2]=1, and unconditionally

    rank J(Q) <= 10+c <= 12.

The numerical upper bound twelve exceeds the needed upper bound one
for rank J(Q)<2 by eleven. Thus this dimension-only calculation does
not meet the rank-below-genus test. It supplies no rank lower bound,
exact Selmer dimension, rational-point classification, marked lift,
integer recovery or Beal exclusion. Thirteen is an upper bound on the
ambient dimension, not an assertion that c=2 or that the Kummer image
fills it. This is a fixed-instance specialization of the cited theory,
not a claim of a new general theorem or certified originality.

## Proof

### Known inputs and why this specialization is needed

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-26-pair-supported-norm-dimension.md`.
It supplies primary coverage and the duplicate/failure comparison for
exactly this calculation. The sources give the general dimension and
rank tools; the missing local work is to bind the actual signature,
finite-prime count, ordinary class bound, product norm and torsion
subtraction. No general descent or unit theorem is reproved here.

Import J. E. Cremona and M. P. Lingham, *Finding all elliptic curves
with good reduction outside a given set of primes*, Experimental
Mathematics 16(3) (2007), 303–312,
[author manuscript, Section 2, p.3](https://johncremona.github.io/papers/egros.pdf),
the definition of K(S,m) and its unnumbered m-Kummer exact sequence.
For m=2 it is

    1 -> O_(K,S_K)^*/O_(K,S_K)^{*2}
      -> K(S_K,2) -> Cl(O_(K,S_K))[2] -> 1.             (1)

It uses the full integer ring and arbitrary finite prime support; it
does not assume odd class number. No elliptic-curve-specific algorithm
from that paper is used.

Import J. S. Milne, *Algebraic Number Theory*, v3.08 (19 July 2020),
[Theorem 5.11 and proof, printed p.90](https://www.jmilne.org/math/CourseNotes/ANTc.pdf):
the S-unit group is the roots of unity times a free abelian group of
rank r_1+r_2+|S_K|−1. Here the localized ring in (1) is exactly
O_K[1/330]: these are all finite primes above the rational primes
dividing 330. L137 proves there is one such prime over 2, two over 3,
three over 5 and one over 11. Ramification multiplicities do not change
the number seven. L135 proves K totally real using four disjoint
real root intervals. Thus the free S-unit rank is 4+0+7−1=10.

Since K embeds into R, its roots of unity are precisely {1,−1}.
Their quotient by squares has dimension one. The S-unit square-class
dimension is therefore 10+1=11. Archimedean places have already been
counted by the signature; they are not additional finite primes and
impose no positivity restriction here.

The ordinary S-class group is finite, being a quotient of the finite
ordinary number-field class group. By the standard invariant-factor
structure theorem for finite abelian groups, a finite abelian group
C satisfies dim_F2 C[2]=dim_F2 C/2C: each even cyclic invariant factor
contributes one to each side, and each odd factor contributes zero.
Consequently the final group in (1) has dimension c, bounded by two
by L137. This comparison is within one finite group; it uses no
surjectivity on two-torsion under localization. Taking dimensions in
(1) gives exactly dim K(S_K,2)=11+c, not necessarily thirteen.

For Q, factorization of a nonzero rational number shows that every
supported square class is represented uniquely by

    (−1)^e0 2^e1 3^e2 5^e3 11^e4,  e_i in {0,1}.

Valuations at the four primes recover e1,...,e4, and the real sign
recovers e0. This proves dimension five, with no assumption about
quartic norms or units. The maximal-ring product and support in L138
then give L(S,2)=Q(S_0,2)×K(S_K,2), of dimension 16+c.

### The supported product norm and its section

Import Milne, same version,
[Corollary 8.4 and determinant proof, printed p.136](https://www.jmilne.org/math/CourseNotes/ANTc.pdf),
the field norm as the determinant of multiplication. On Q×K the
multiplication operator is block diagonal, so its determinant is

    N(q,b)=q N_(K/Q)(b).

This applies to the actual product algebra of L138. Norms of squares
are squares, so the formula descends to square classes. For p outside
S_0, the standard norm valuation formula is

    v_p(N_(K/Q)b)=sum_(P|p) f(P/p) v_P(b).

Every v_P(b) on the right is even for supported b. Thus the norm of
a supported pair lies in Q(S_0,2), including its unrestricted sign.
Equivalently, this formula follows by taking norms in the principal
ideal factorization, using N(P)=p^{f(P/p)}. Hence the codomain can be
restricted to the full supported rational group, not just a sign row.

The map [q] -> ([q],[1]) is a well-defined supported section: rational
valuations outside S_0 are even in its first component and zero in
the second, and its product norm is [q]. The norm image is therefore
exactly Q(S_0,2), of dimension five. Its kernel in the unrestricted
rational square-class codomain is the same kernel as in this supported
codomain. Rank-nullity gives

    dim ker N=(16+c)−5=11+c <= 13.                      (2)

More explicitly, [b] -> ([N_(K/Q)b]^{−1},[b]) identifies
K(S_K,2) with that kernel; inverse projection recovers [b]. Support
of the first component was just checked. This is not a claim that
the quartic norm itself is onto. No scalar quotient is taken in this
odd-degree Jacobian descent.

### Rational two-torsion and the rank consequence

Import Michael Stoll, *Implementing 2-descent for Jacobians of
hyperelliptic curves*, Acta Arith. 98 (2001), 245–277, DOI
10.4064/aa98-3-4,
[Lemma 4.3(3), p.250](https://www.impan.pl/shop/en/publication/transaction/download/product/83397).
For its monic squarefree odd-degree model, the rational two-torsion
dimension is m_Q−1, where m_Q is the number of distinct irreducible
factors. L138 proves all those model hypotheses and the actual
factorization above. There are exactly two factors, the rational
linear factor and irreducible quartic, so dim J(Q)[2]=2−1=1.

By the named Mordell–Weil theorem, J(Q) is finitely generated. Its
free part contributes rank J(Q) to J(Q)/2J(Q), and its finite torsion
part contributes dim J(Q)[2]=1, by the same finite-abelian comparison.
Stoll's Lemma 4.1 and Proposition 4.2, p.250, give the injective
odd-degree Kummer map from this quotient. L138 specializes the norm
and support containment for that actual map, so (2) implies

    rank J(Q)+1=dim_F2 J(Q)/2J(Q) <= 11+c.

This proves rank J(Q)<=10+c<=12 directly. It is also compatible with
Stoll's equation (1.1), p.245, bounding rank by the two-Selmer dimension
minus rational two-torsion dimension; no Selmer equality, local-image
enumeration or finiteness of Sha has been used.

### Threshold, scope and remaining obligations

The test fixed before calculation was rank J(Q)<2. Since rank is an
integer, a sufficient numerical upper bound must be at most one.
The obtained bound twelve fails by eleven. In the corresponding
Kummer dimensions the worst allowed ambient upper bound is thirteen,
whereas a bound at most two would suffice after subtracting rational
two-torsion. This measures the shortfall of these bounds only: it
does not prove that eleven independent local conditions exist, that
the ambient dimension is thirteen, or that the actual rank is large.
Even c=0 would leave this method with upper bound ten, so improving
the class bound alone cannot make this particular ambient estimate
meet the test. The dimension-only shortcut ends here.

All arithmetic is the displayed integer dimension calculation applied
to already audited inputs; no mathematical script or upstream
certificate was rerun or modified. General theorems are cited rather
than reproved. Complete filtered descent and point control, the
marked lift, degree-nine/integer recovery, both L095 systems and all
other residual exponent signatures remain independent gaps. Existing
backend, relation-box, localization and point-search stops, including
ATTEMPTS/059–060 and unfinished L108, remain in force for their stated
routes. The separate critical audit below accepts this specialization.

### Separate critical proof audit — 2026-10-26

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-26-pair-supported-norm-dimension-audit.md`.
The audit reads the entire specialization and checks its essential
inputs in audited L135, L137 and L138. It accepts the stated dimensions
and unconditional rank upper bound without a mathematical correction.
This is validation of a known-theorem specialization, not a new general
theorem or a complete Beal candidate. The approved primary coverage is
reused; no general theorem is reproved or source scope enlarged.

The displayed H agrees coefficient for coefficient with L138. Its
verified inverse field maps identify its quartic factor with L135's
totally real field and transport the maximal order and localization.
L138's monic squarefree degree-five model and two irreducible factors
are therefore the actual curve and algebra required by Stoll. Its
support containment uses all maximal-ring primes, so no singular power
order or smaller finite support enters this calculation.

L137's complete support argument counts 1+2+3+1=7 distinct primes
above 2,3,5,11. Its exceptional enumeration includes higher-residue-degree
possibilities, and the repeated factor at 11 represents one ramified
prime. Thus the S-unit theorem gives free rank 4+0+7-1=10. The real
embedding excludes every root of unity other than ±1. In the unit-group
decomposition the torsion quotient contributes one square class, hence
unit square-class dimension eleven. There is no positivity restriction.

The exact sequence (1) uses precisely C=Cl(O_K[1/330]). Localization
makes C a quotient of the finite ordinary class group. The comparison
of C[2] with C/2C is within this same finite group: each cyclic factor
of even order contributes one to both, and each odd-order factor zero.
L137 bounds the latter by two. It neither establishes c=2 nor asserts
surjectivity from the original class two-torsion. Exactness consequently
gives 11+c for the supported quartic group, including classes without
S-unit representatives. Omitting those classes would be invalid.

The five rational square classes retain the negative sign and all four
prime valuations independently. The product norm's outside-support
valuation is the integer sum of residue degrees times even valuations,
so its image lies in that five-dimensional group. The section (q,1)
is supported and has norm q. In particular this is not the diagonal
embedding of Q into both factors and assumes nothing about surjectivity
of the quartic norm. The explicit inverse-norm graph in the proof
independently identifies the kernel with K(S_K,2), confirming 11+c.
The kernel is unchanged on passing to the unrestricted rational
square-class codomain. No scalar quotient or sign row is omitted.

Stoll's odd-degree formula now gives 2-1=1 for rational two-torsion.
Mordell–Weil and the finite-abelian comparison give rank+1 for the
dimension of J(Q)/2J(Q). L138's supported Kummer injection therefore
gives rank+1<=11+c, hence rank<=10+c<=12. This deduction uses only
containment, not Selmer equality or finite Sha. The gap to the sufficient
rank upper bound one is eleven; even c=0 leaves the bound ten. None
of these inequalities is a rank lower bound. Point control and the
remaining lifting and signature obligations are unchanged.

The direct inputs remain exactly L135, L137 and L138; no DAG edge is
added. The audit checks the displayed dimension arithmetic and logical
specializations directly. No script is needed for these integer sums,
and no upstream certificate, search or backend is rerun. This audit
does not replace the separate arithmetic audits of those inputs.

## Mathlib

Full matching coverage of this instance and its supporting S-Kummer,
S-unit, norm and Jacobian results has not been checked in Mathlib.
No absence claim or Lean verification is made.
