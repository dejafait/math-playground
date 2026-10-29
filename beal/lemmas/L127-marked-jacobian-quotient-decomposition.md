# L127 — Marked Jacobian decomposition over Q

## Hypotheses

Work over Q with the audited smooth proper curves of L110, L111 and
L113. Write

    Q4(T)=7+52T−6T²−64T³−25T⁴,
    a(T)=−3(T²−4), b(T)=−33Q4(T),
    B: W²=a(T)b(T)/9=11(T²−4)Q4(T),
    D: h²=a(T), R²=b(T),
    E: R²=b(T), O_E=(2,165).

E has its elliptic group law with origin O_E. Let C be L113's smooth
proper genus-three curve Y²=11(275t⁸−2860t⁶+6930t⁴−3564t²+243).
The Q-isomorphism alpha:C→D is the proper extension of

    T=2(t²−3)/(t²+3), h=−12t/(t²+3), R=3Y/(t²+3)².

No upper rank, rational-point completeness, descent arithmetic or
primitive integer solution is assumed.

## Conclusion

Let p_B:D→B and p_E:D→E be the proper projections

    p_B(T,h,R)=(T,hR/3), p_E(T,h,R)=(T,R).

Using E≅Jac(E) via P↦[P−O_E], the Q-homomorphism

    F: Jac(B) × E → Jac(C),
    F(x,e)=alpha^*(p_B^*x+p_E^*e)

is an isogeny. The exact ordinary Mordell–Weil rank relation is

    rank Jac(C)(Q)=rank Jac(B)(Q)+rank E(Q).

This gives neither a numerical upper rank nor an isomorphism of the
integral groups of rational points. It excludes no Beal solution.

## Proof

### The actual connected unramified cover

L110 proves that the sextic for B is squarefree and B has genus two.
L111 proves that a,b have simple disjoint geometric root sets, that
Qbar(T,h,R) has degree four over Qbar(T), and that its finite and
infinity charts give the smooth proper geometrically integral D.
Thus Q(T,hR/3)=Q(B) has index two in Q(D). The covering involution is

    iota:(T,h,R)↦(T,−h,−R).

It differs from the involution of p_E, which changes h alone. On the
finite chart a fixed geometric point of iota would have h=R=0,
impossible because a,b have disjoint roots. The entire infinity fiber
is in L111's chart x=1/T, H=h/T, S=R/T², where at x=0 one has
H²=−3 and S²=825. Both are nonzero and iota negates both, so there
is again no fixed point. These charts cover D. For this separable
quotient in characteristic zero, geometric ramification is exactly
nontrivial inertia, hence a fixed point of the involution. Therefore
p_B is unramified everywhere. Geometric integrality supplies geometric
connectedness. Both projections are the proper morphisms of L111;
no affine denominator deletes a fiber.

### Imported Prym comparison and its specialization

Import Nils Bruin, *The arithmetic of Prym varieties in genus 3*,
Compositio Math. 144 (2008), 317–338, DOI
[10.1112/S0010437X07003314](https://doi.org/10.1112/S0010437X07003314),
[arXiv:math/0408069v2](https://arxiv.org/pdf/math/0408069v2),
Section 2.2, Proposition 2.2 and proof, manuscript pp.4–5.
For the split unramified cover of y²=f1 f2 with squarefree even-degree
factors, the factor-curve Jacobians identify by their pullbacks with
Prym(D/B). Here take exactly

    f1=a, f2=b/9, y1=h, y2=R/3, y=y1*y2=W.

The factor degrees are two and four, and their product is exactly
L110's sextic. The quadratic factor curve h²=a is smooth proper of
genus zero with rational point (2,0), so its Jacobian is zero. The
quartic factor curve (R/3)²=b/9 is Q-isomorphic to E by the indicated
rational rescaling. Hence the proposition identifies E≅Jac(E) with

    P=Prym(D/B)=ker(p_B,*:Jac(D)→Jac(B))^0

by j=p_E^*. The chosen origin gives the stated E≅Jac(E) identification.
No rational point of B is required, and no square root of −3 is
adjoined. This is the actual marked twist over Q. Only the
abelian-variety identification is imported, not a polarization formula.

Import Jordan Docking, *2-infinity-Selmer rank parities via the Prym
construction*, J. Number Theory 265 (2024), 208–225, DOI
[10.1016/j.jnt.2024.06.009](https://doi.org/10.1016/j.jnt.2024.06.009),
[arXiv:2108.09564v2](https://arxiv.org/pdf/2108.09564v2), Section 2,
manuscript p.4 (Table 1, Case II), and Lemma 5.3 and proof, p.8.
For a connected unramified double cover with genus-two base its
Q-homomorphisms are

    phi:Jac(B)×P→Jac(D), (x,y)↦p_B^*x+y,
    psi:Jac(D)→Jac(B)×P, z↦(p_B,*z,z−iota_*z),
    psi phi=[2], phi psi=[2].

All cover hypotheses were checked above. The extra rational-point
hypothesis in the genus-three-base case is irrelevant because our
base B has genus two. Compose phi with id×j and transport by alpha^*
to obtain exactly F. With

    G=(id×j^(-1)) psi (alpha^*)^(-1)

one has GF=[2] and FG=[2]. Thus ker F is contained in the finite
multiplication-by-two kernel, and F is surjective since FG=[2] is
surjective. This proves an isogeny over Q, not just over an extension.
For the finite-kernel criterion and multiplication isogenies see
J.S. Milne, *Abelian Varieties*, v2.00, 16 March 2008,
[author notes](https://www.jmilne.org/math/CourseNotes/AV.pdf),
Chapter I Proposition 7.1 and Theorem 7.2, printed pp.32–34.
No degree or enumeration of rational kernel points is asserted.

### Ordinary rank and limitations

Milne, same version, Chapter I Theorem 16.7, printed p.69, gives
Mordell–Weil finite generation over number fields. F and G are defined
over Q, so both composites on rational points remain multiplication by
two. After tensoring with Q, F is an isomorphism with inverse G/2.
Dimensions of these finite-dimensional Q-vector spaces give precisely
the rank sum. Integrally, finite kernels and cokernels can remain;
a group isomorphism does not follow.

This is the known-result application approved by
`drafts/literature/2026-10-24-marked-jacobian-quotient-decomposition.md`
(IMPORT), not a new decomposition theorem or a reproof. No numerical
calculation is needed. Quotient upper ranks, supported unit/S-class
arithmetic, descent and point control remain unresolved, followed by
degree-nine recovery, remaining factors, both L095 systems, minus-eleven
and other residual signatures. Neither torsion nor dimension supplies
those missing bounds. The relation is a potential reduction of rank
work, not a complete route to the Beal target.

### Independent critical instance audit, 2026-10-25

The prior IMPORT assessment is
`drafts/literature/2026-10-24-marked-decomposition-critical-audit.md`.
The audit confirms the stated F and ordinary-rank identity without
changing either conclusion. This is verification of a known-result
application, not a new decomposition theorem. It uses L110's audited
squarefreeness, L111's audited fields and smooth proper charts, and
L113's audited proper Q-isomorphism; it does not claim a new execution
or audit of all their arithmetic certificates.

**Cover and twist.** Multiplying the actual factors gives
ab/9=11(T²−4)Q4, exactly B's polynomial. Over Qbar(T), L111's
disjoint simple root sets make a, b and ab nonsquares. Thus the
compositum has basis 1,h,R,hR, and the fixed field of simultaneous
negation is exactly Qbar(T,hR); the same basis argument holds over Q.
It follows that p_B is the connected degree-two quotient to the
specified B, rather than merely a map to a curve with the same genus.
On the finite chart, h=0 forces R nonzero and R=0 forces h nonzero;
in either case the other coordinate is changed by iota. Where both
are nonzero neither is fixed. On the infinity chart all four geometric
points have H²=−3 and S²=825. They are exchanged in pairs by
(H,S)↦(−H,−S), not fixed. The B-coordinate at infinity is
U=W/T³=HS/3, with U²=−275, so the map agrees with L110's full
infinity chart as well. These smooth charts exhaust D. In
characteristic zero the quotient therefore has no ramification.
In particular the ramification of p_E at h=0 has not been incorrectly
attributed to p_B. The already audited genera are g(B)=2 and g(D)=3.

**Actual Prym inclusion.** Bruin's Proposition 2.2 applies to the
squarefree degree-six product with even factor degrees two and four.
The first factor curve h²=a has genus zero; its point (2,0) is smooth
since a'(2)=−12, and its Jacobian is zero. For the second factor
write E2: y2²=b/9. The Q-isomorphism

    r:E2→E, (T,y2)↦(T,3y2)

has inverse (T,R)↦(T,R/3) and sends (2,55) to O_E=(2,165).
If q2:D→E2 is (T,h,R)↦(T,R/3), then p_E=r q2, whence
p_E^*=q2^* r^*. Bruin identifies q2^*:Jac(E2)→P with an
isomorphism, because the other Jacobian factor is zero. Thus the
actual p_E^* identifies Jac(E), and hence (E,O_E), with P over Q.
This verifies the specific j in F; it does not replace j by an
unspecified isogeny. The inverse j^(-1) used below is the inverse
of this abelian-variety isomorphism over Q. Neither an inverse to
multiplication by two on integral points nor a choice of sqrt(−3)
is involved. No polarization claim is needed.

**Both composites and transport.** Write u=p_B^*, n=p_B,* and
i=iota_* on Jac(D). The norm/pullback identities in the imported
comparison are

    n u=[2], u n=1+i, i u=u.

On P=ker(n)^0, inclusion gives n|P=0; the second identity gives
i|P=−1. The connected image of 1−i lies in P, since
n(1−i)=0, so the second component of psi really has target P.
For x in Jac(B) and y in P the identities therefore give

    psi phi(x,y)=(n(ux+y),(1−i)(ux+y))=(2x,2y),
    phi psi(z)=u n z+(1−i)z=(1+i)z+(1−i)z=2z.

These are identities of homomorphisms, not just equalities tested on
rational points. They check the specialization of Docking's Section 2
and Lemma 5.3 in both directions. The genus-two case has no extra
rational-point requirement on B.

For alpha:C→D, pullback A=alpha^* has source Jac(D) and target
Jac(C). L113 gives its proper inverse over Q, hence A^(-1) is
also an abelian-variety isomorphism over Q. Put k=id×j. The maps
in the conclusion are precisely F=A phi k and G=k^(-1) psi A^(-1).
The displayed composites give GF=[2] on Jac(B)×E and FG=[2]
on Jac(C). Milne I.7.2 makes these multiplication maps finite and
surjective; consequently ker(F) is a subgroup scheme of ker([2])
and F is surjective. Milne I.7.1 therefore applies over Q.

Finally Milne I.16.7 applies to all these abelian varieties over Q.
On their finitely generated rational-point groups, F and G retain
both composite identities. Tensoring with Q makes G/2 the inverse
of F, and the rank of the product is the sum of the two ranks.
This verifies the exact ordinary-rank assertion, without a Selmer
parity substitution, a Sha hypothesis, or an integral group
isomorphism. The continuation test passes for this structural input
only. Numerical upper ranks, point control and all the independent
Beal recovery obligations listed above remain unresolved.

## Mathlib

Full matching Prym/decomposition coverage and supporting Jacobian
isogeny APIs were not checked. No absence or Lean-verification claim
is made. This is an informal cited-theorem application.
