# L041 — Certified eleven-adic algebra, scalar domain and valuation baselines

## Hypotheses

Use the field K, curve E0, normalized dual connecting map delta and complete modular map j from L033–L034. In particular

    E0: y^2+y=x^3-x^2-10x-20,
    f=(x-4)y-4x^2+30x-55,
    delta(T)=[11^-1],  T=(5,5).

Set A11=K tensor_Q Q11. For s in Q11 minus {0,1728}, let B_s be the algebra of the entire modular fiber. Consider all isomorphisms B_s -> A11, and their associated points P in E0(A11). The primitive restriction requires common nonzero a,b,c in Z11 with minimum coordinate valuation zero, a^3+b^4=c^11, and s=1728 a^3/c^11. There are no positivity or other-place restrictions here. The desired vector has coordinates ord_w(delta(P_w)) modulo five, with ord_w of a uniformizer equal to one. Good divisors define delta at exceptional points.

## Conclusion

The complete algebra is

    A11 = Q11 × Q11 × L,    L ≅ Q11[r]/(r^10+55).

Order the first two places by the unique roots of L033's defining polynomial congruent to 8 and 2 modulo 11; the third is its degree-ten block with root residue 10. Their (ramification index, residue degree) pairs are (1,1), (1,1), (10,1). Thus every possible permutation of the two rational factors must still be allowed in a whole-fiber isomorphism.

For t=s/1728 and q=1-t, primitive common scalar witnesses exist exactly when

    (v11(t),v11(q)) belongs to (3 N0) × (4 N0),
    or v11(t)=v11(q)=-11k for an integer k>=1.

The unrestricted connecting valuation image on E0(A11) is all (Z/5Z)^3. Every whole-fiber-compatible vector, with or without primitive witnesses, lies in the affine plane

    H = {(d1,d2,d3): d1+d2+d3=2 modulo 5}.

This has 25 vectors, compared with 125 unrestricted vectors. The restriction is inherited entirely from L034's norm. **The exact restricted subset of H, its nonemptiness, and any additional restriction are not determined here.** The result provides certified prerequisites for the approved complete-vector target, not an answer to that target or an integer exclusion.

## Proof

### Imported inputs and why specialization is needed

The local algebra inputs are Pete L. Clark, *Algebraic Number Theory II: Valuations, Local Fields and Adeles*, [author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf), accessible 161-page version with no identified revision date: coprime Hensel factor lifting, Theorem 1.75 and Remark 1.76, printed p.57; Hensel–Newton, Theorem 1.79, p.58; and the Eisenstein extension/integer-ring statements, Proposition 2.9 and Corollary 2.10, p.65. These were inspected in the prior assessment, with Hensel–Newton also recorded in foundation 17. In each root-lifting application below the polynomial is integral, the approximate root has positive residual valuation, and the derivative is a unit, so the strict Hensel inequality holds. General factor lifting, Eisenstein theory and Hensel lifting are imported, not reproved.

L033 supplies the normalized connecting homomorphism at every completion, including its good-divisor evaluations, by Schaefer–Stoll, *How to do a p-descent on an elliptic curve*, Trans. AMS **356** (2004), 1209–1231, [June 13, 2001 manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf), Section 5, pp.8–10, and Section 9, pp.21–24. L034 supplies the full finite flat map and determinant norm, with precise FNS and Stacks citations. None of these inputs states the decomposition or simultaneous scalar construction below. This is the local arithmetic specialization authorized by the existing SPECIALIZE assessment; no general local descent theorem is reproved and no novelty is claimed.

### All three places, including the ramified factor

Let m be L033's degree-twelve defining polynomial. Exact reduction gives

    m(X) = (X+1)^10 (X+3)(X+9) modulo 11.

The three displayed blocks are pairwise coprime. The simple roots 8 and 2 have derivative residues 6 and 5, respectively. Hensel factor lifting gives two linear factors over Z11 and one monic degree-ten factor. It does not by itself prove that the latter is irreducible.

Shift X=U-1. The ascending coefficients of m(U-1) are

    [-209,-66,792,-1958,1947,-990,-22,66,165,-154,60,-12,1].

Write its Hensel factorization as G(U) H(U), with monic degrees ten and two, G congruent to U^10, and H congruent to (U+2)(U+8). Every nonleading coefficient of G is divisible by 11. Since H(0) is a unit, m(-1)=-209=-19·11 gives v11(G(0))=1. Hence G is Eisenstein. It defines a totally ramified degree-ten field L with residue field F11; if pi is its root, ord_L(pi)=1 and ord_L(11)=10. Together with the two rational factors, these account for all twelve dimensions and all places. No assertion about maximality of the original power order is used.

There is also an exact convenient model for L. Modulo 11,

    H(0)=5,    G(0)/11=(-19)/5=5.

Divide G(pi)=0 by 11 and reduce modulo pi. Each term G_i pi^i/11 for 1<=i<10 has positive valuation, so

    pi^10/11 = -5 = 6 modulo pi.

The unit (-55)/pi^10 is therefore 1 modulo pi. Hensel applied to Z^10-(-55)/pi^10 at Z=1, whose derivative 10 is a unit, gives z in 1+pi O_L with z^10=(-55)/pi^10. Put r=pi z. Then r^10=-55 and ord_L(r)=1. The polynomial X^10+55 is Eisenstein over Q11, so Q11(r) has degree ten and equals L. This proves the displayed model, not merely agreement to a finite precision.

### Exact scalar witnesses without an eleventh-root claim

Necessity retains all coordinate valuations. Write alpha=v11(a), beta=v11(b), gamma=v11(c). The identities give

    v11(t)=3alpha-11gamma,    v11(q)=4beta-11gamma.

If gamma=0, the first alternative follows. If gamma>0, primitivity makes at least one of a,b a unit, and subtracting its power from c^11 makes the other a unit. Thus alpha=beta=0, giving the second alternative. These exhaust the primitive cases.

Conversely, let r0=v11(t) and s0=v11(q) meet an alternative. In the nonnegative case set gamma=0. In the negative case set gamma=-r0/11; here s0=r0 because q=1-t and r0<0. In both cases set

    alpha=(r0+11gamma)/3,    beta=(s0+11gamma)/4,
    t0=11^(-r0)t,    q0=11^(-s0)q.

The first two are nonnegative integers with min(alpha,beta,gamma)=0, and t0,q0 are units. Choose any integer unit u with residue q0^(-1) modulo 11. Since u^11 has residue u, q0 u^11 has residue one. Hensel applied to Z^4-q0 u^11 at Z=1 has derivative 4 and yields a unit z with z^4=q0 u^11. Every unit has a cube root in Z11: the cube map permutes F11^* because gcd(3,10)=1 (its inverse exponent is 7), and the lifting derivative 3w^2 is a unit. Obtain w with w^3=t0 u^11. Now put

    a=11^alpha w,    b=11^beta z,    c=11^gamma u.

These are common nonzero integral primitive witnesses and satisfy a^3=t c^11 and b^4=q c^11 exactly. Adding gives the required equation at the original scalar s. No eleventh root has been taken: u was chosen freely and only cube and fourth roots were lifted. This checks the residue-characteristic-eleven issue rather than importing L036's five-adic unit-root argument.

### The full unrestricted valuation baseline

For either rational factor, delta(T)=[11^-1] has valuation -1 modulo five. Since delta is a group homomorphism, its multiples give all five residues.

For L use the exact uniformizer r above and construct a point near the singular residue point explicitly, without a Tate-coordinate normalization assumption. Put x=5+r and y=5+r w. The curve equation becomes

    w^2+(11/r)w-r-14-55/r=0.

All coefficients are integral: ord_L(11/r)=ord_L(55/r)=9. Its reduction is w^2-3, which has the root w=6 modulo r, with derivative 12=1 in F11. Hensel gives an exact integral root w of that residue. Substituting in L033's polynomial function gives

    f(x,y)=r[(1+r)w-5-4r].

The bracket has residue 6-5=1, so ord_L(f)=1. This point has x=5+r different from 5 and is affine, hence is neither T nor O; its ordinary f-evaluation gives delta. Multiples of this point give every valuation residue. Choosing points independently in all three factors proves that the unrestricted vector image is the full product of three copies of Z/5Z. This is a statement about unrestricted points only, not compatible modular fibers.

### Norm plane for every whole fiber, including exceptional evaluation

For s different from j(T)=-24729001, L034's finite locally free determinant base change applies over Q11 to the complete fiber, and after any isomorphism B_s -> A11 gives

    N_A11/Q11(delta(P))=[11^22]=[11^2].

Both O and 3T lie above infinity and are absent from this finite fiber; T is absent for this nonexceptional s. The removable x=16 chart is included by the complete map. The field norm valuation formula is v11(N z)=sum_w f_w ord_w(z); it follows directly by norming principal ideals in the local DVRs. All three residue degrees f_w equal one. Thus the vector sum is 2 modulo five. The coefficient of the third coordinate is one, **not** its ramification index ten.

At s=j(T) use good divisors and a complete-fiber deformation. Details at this prime are as follows. For each factor F and point Q, choose R among {2T,3T,4T} with R and Q+R away from T,O, as justified in L033. Then f(Q'+R)/f(R) is continuous and nonzero near Q and represents delta(Q'). Every unit in 1+m_F is a fifth power, by Hensel on Z^5-u at 1 with derivative 5 a unit. Consequently delta is locally constant at Q, including Q=T.

The scalar j(T) is not a branch value 0,1728,infinity, so j is unramified at every point of this fiber. In a smooth local parameter its nonzero linear term gives a local inverse by Hensel after shrinking and rescaling the parameter. Starting from any whole-fiber isomorphism, deform its three component points simultaneously to P_w(s') for rational scalars s' sufficiently close to s. This still gives a whole-fiber isomorphism: since the original affine x(P),y(P) generate A11, choose twelve monomials in them with nonzero coordinate determinant. They remain independent by continuity. The evaluation map from the new fiber algebra to A11 is then surjective between twelve-dimensional Q11 algebras and hence is an isomorphism. This also prevents any silent omission of an isomorphic factor or embedding. Shrink again so that all connecting classes stay constant, and choose s' distinct from s and from the branch values. The nonexceptional case gives the norm class at P(s'), which equals that at P. The auxiliary scalar need not retain power witnesses, because the norm claim was proved for every whole fiber.

This establishes the plane constraint even where f(T)=0; a zero ordinary norm has never been assigned a Kummer class. For each choice of the first two coordinates there is exactly one third coordinate with sum two, so H has 25 elements. Nothing here proves that any or all elements of H occur in a whole fiber.

### Evidence, achieved threshold and remaining blocker

Run `python3 scripts/primitive-eleven-vectors/check_vectors.py`. The [full certificate](../scripts/primitive-eleven-vectors/vector-prerequisites-certificate.json) records the exact shifted polynomial, all pairwise Bezout identities, simple-root derivatives, Eisenstein and Kummer residues, local-point Hensel data and complete scalar residue constructions. All 14 arithmetic checks pass. Actual total dimension is twelve, required twelve; actual constant valuation is one, required one; the local-point coefficient valuation is nine, required positive. The exact shifted coefficients, valuations, simple-root data, Bezout witnesses and unit tables were inspected in full. The lifting and whole-fiber arguments above supply the proofs that finite residues alone cannot supply.

The achieved comparison is 125 unrestricted vectors versus 25 necessary norm candidates. The required threshold for the approved target is a proved exact restricted set, including a realization argument for each retained vector. That threshold is not reached. The remaining concrete blocker is simultaneous modular compatibility: determine which points on E0(Q11)×E0(Q11)×E0(L) with one scalar in the proved domain generate the entire fiber algebra, and prove their valuation coverage in both directions. Independent realizations in each factor do not meet that condition. No finite-precision cutoff, class/unit basis, global lifting, GRH, Tate hypothesis or branch emptiness is assumed. The other four twists and infinitely many signatures remain independent gaps.

## Mathlib

Full matching local-algebra model, scalar-witness domain, and complete-vector prerequisites: **not checked**. Supporting Hensel, Eisenstein, local norm, connecting-map and finite-flat declarations: **not checked**. Unknown coverage is not absence. This is local REPRODUCTION progress under the prior assessment, with no claim of progress beyond the checked general source results or of completion of the exact vector target.
