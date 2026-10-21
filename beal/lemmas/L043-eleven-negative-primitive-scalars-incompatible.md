# L043 — No primitive compatible whole fiber at a negative eleven-adic scalar

## Hypotheses

Use L033's curve E0 and normalized connecting map, and L034's complete degree-twelve modular map j. In particular

    E0: y^2+y=x^3-x^2-10x-20,
    j=(a(x)+b(x)y)/(x-16)^11,
    F(x,s)=h(x)^3+J(x)s-(x-16)^11 s^2,   J=2a-b.

The full integral coefficient lists are those of L034, not newly chosen polynomials. Let A11 and the primitive whole-fiber requirement be exactly L041's: A11=Q11 × Q11 × L, where L=Q11[r]/(r^10+55), with normalized ramification/residue pairs (1,1),(1,1),(10,1). The scalar s is in Q11 minus {0,1728}, and common nonzero a0,b0,c0 in Z11 must satisfy minimum coordinate valuation zero,

    a0^3+b0^4=c0^11,     s=1728 a0^3/c0^11.

Consider every isomorphism of the entire fiber algebra B_s with A11, including both rational-factor permutations and every ramified embedding. Assume v11(s)<0. There is no positivity, other-place restriction, global class basis, GRH, or precision cutoff.

## Conclusion

There is **no** such whole-fiber isomorphism at any primitive negative scalar. Consequently this region contributes the empty set of connecting-class valuation vectors. In a global primitive integer solution satisfying L033's 54a1 branch, this also forces 11 not to divide the original right-hand base C: divisibility would give a primitive negative scalar by L041.

Together with L042, this leaves only integral scalars in the residue disks 0 and 1 modulo eleven to finish the approved complete-vector computation. Their contributions, and the exact full image inside L041's 25-element norm plane, are not determined here. This does not exclude the 54a1 branch, any other twist, or a Beal signature.

## Proof

### Imported results and the specialization

L034 supplies the complete map, the elimination identity, and the branch values 0,1728,infinity, from Freitas–Naskręcki–Stoll, *The generalized Fermat equation with exponents 2, 3, n*, Compositio Math. **156** (2020), 77–113, [final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf), internally June 10, 2019, Section 7.2, pp.25–27, equation (7.4). L042 supplies exact shifted coefficient bounds and the integral polynomial B(Z)=b(16+121Z)/11^20, whose reduction is (Z+1)^10. L041 supplies the exact primitive scalar domain and the complete field L. These are mathematical inputs, not statements inferred from numerical factorization.

For simple-root lifting and the Eisenstein extension use Pete L. Clark, *Algebraic Number Theory II: Valuations, Local Fields and Adeles*, [161-page author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf), no identified revision date: Theorem 1.79, printed p.58, and Proposition 2.9/Corollary 2.10, p.65. These inputs were inspected in the prior SPECIALIZE assessment and foundation 17. We import their general statements. The specialization requiring proof is the uniform twelve-root coverage and the degree-ten field mismatch at this simultaneous scalar; no inspected theorem states that calculation. No Tate-coordinate or cyclotomic-field identification is assumed or needed. This is REPRODUCTION with no novelty claim.

Write v for the extension of v11 with v(11)=1, including on algebraic roots. L041 gives

    s=11^(-11k) sigma,     k>=1,     sigma in Z11^*.

The minimum coordinate valuation is essential to this assertion. We prove incompatibility for every such k and unit sigma, without replacing them by a bounded set of scalars.

### Exactly one root near infinity

If a root x of F has u=v(x)<0, monicity and integrality of h and d=(x-16)^11 give

    v(h(x)^3)=12u,    v(d(x)s^2)=11u-22k,
    v(J(x)s)>=11u-11k.

Here deg(J)=11 and all its coefficients are integral. The J term is strictly larger than the d term. If u<-22k, the h term is uniquely lowest; if -22k<u<0, the d term is uniquely lowest. Either would contradict their sum being zero. Therefore every nonintegral root has u=-22k.

Put x=s^2 X and consider the monic integral polynomial

    Q_infty(X)=F(s^2 X,s)/s^24.

For the coefficients coming from h^3,J,d the exponents of s are respectively 2i-24, 2i-23, 2i-22. They are nonpositive throughout their respective degree ranges. The only exponent-zero terms are X^12 from h^3 and -X^11 from -d s^2. Since v(s)<0, all other terms reduce to zero. Thus

    Q_infty_bar=X^11(X-1).

The root 1 has derivative 1. Hensel gives a rational root X_O with residue 1 and the corresponding root x_O=s^2 X_O of F, with v(x_O)=-22k. Division by its linear factor leaves a monic integral polynomial reducing to X^11, so no other root has nonzero X residue. Every nonintegral root of F must have that residue by the valuation calculation and the displayed reduction. Hence x_O is the **unique** nonintegral root, including among algebraic roots; the other eleven roots of F are integral, counted initially with multiplicity.

### The other eleven roots have one exact cusp scale

Expand F(16+W,s)=sum c_i(s) W^i. L042's component bounds, also checked directly in the certificate below, give

    c_0=11^22(s+121),     v(c_0)=22-11k,
    v(c_11)=-22k,         c_12=1,
    v(c_i)>=23-2i-11k    for 1<=i<=10.

For c_11 the -s^2 term is strictly lower than the J coefficient times s and the h^3 coefficient, so its valuation is exact. At an integral root, W cannot be a unit: the term -s^2 W^11 would then have valuation -22k, strictly below h^3 and Js. Nor can W=0, because c_0 is nonzero. Write e=v(W)>0.

If 0<e<k+2, c_11 W^11 is uniquely lowest. Compared with it, the constant has valuation difference 22+11k-11e>0. The intermediate term of index i has difference at least

    23-2i+11k-(11-i)e > 1+ik >0,

where evaluation at e=k+2 gives 1+ik. The leading term has difference e+22k>0. If e>k+2, instead the constant is uniquely lowest: an intermediate term has difference at least 1+i(e-2)>0, the index-eleven term has difference 11(e-k-2)>0, and the leading term has difference 12e-22+11k>0. Both cases are impossible. Thus all eleven remaining roots satisfy exactly

    v(x-16)=k+2.

Set rho=11^(k+2), Z=(x-16)/rho and

    R(Z)=F(16+rho Z,s)/11^(22-11k).

This is integral even when the denominator exponent is negative. The coefficient bounds imply

    R_bar=sigma_bar-sigma_bar^2 Z^11,
    (R'/11)_bar=-sigma_bar^2 Z^10.

For clarity, the derivative division is coefficientwise exact. Apart from the constant J contribution sigma, each J term of index 1<=i<=10 has coefficient valuation at least 1+ik>=2 in R. Its index-eleven coefficient has valuation at least 11k. Each h^3 term has valuation at least two in R, including the constant, index-eleven and leading terms. These remain divisible by eleven after differentiation and division by eleven. The only surviving derivative contribution is from -sigma^2 Z^11. The full affine valuation bounds in k, with nonnegative slopes and their minima at k=1, are in the certificate. Thus the two reductions hold for **all** k>=1 and unit sigma.

All cusp roots Z are integral units. Their residue is uniquely

    z0=sigma_bar^(-1) in F11^*,

because Z^11=sigma_bar^(-1) has only that root in an algebraic closure of the residue field. Internal repeated residue roots have not been called irreducible or lifted by a simple-root argument.

### The polynomial accounts for the entire modular fiber

At x_O, the monic degree-ten polynomial b has valuation 10v(x_O), so b is nonzero. At a cusp root, write x=16+121(11^k Z). L042 gives

    b(x)=11^20 B(11^k Z),     B_bar(0)=1.

Thus b has valuation twenty and is nonzero at every cusp root. Also none of these roots, nor x_O, equals 16. At any root reconstruct

    y=(s d(x)-a(x))/b(x).

L034's exact elimination identity gives the curve equation and modular scalar s. Conversely every point in this finite modular fiber is affine: O and 3T lie above infinity. A point with x=16 would be 2T or 3T, whose scalars are -121 or infinity, so cannot occur at our negative s. Every fiber point therefore satisfies F=0 and, since b is nonzero at every root, has precisely the reconstructed y.

The scalar is not 0,1728,infinity. L034's complete finite degree-twelve map consequently has twelve distinct geometric points here. Reconstruction makes x injective on these points, so F has twelve distinct roots and its quotient algebra is exactly B_s. This verifies the whole fiber, including the chart guards, before using factor degrees. In particular T has integral scalar j(T)=-24729001 and does not occur here; no ordinary zero f-evaluation or omitted good-divisor case is involved.

### Any second rational factor forces the wrong degree-ten field

Remove the unique root x_O, obtaining the monic degree-eleven polynomial Q_cusp(x)=F(x,s)/(x-x_O). Define

    M(Z)=rho^(-11) Q_cusp(16+rho Z),
    U(Z)=11^(22k)(16+rho Z-x_O).

Then R=UM exactly. All roots of M are integral by the proved valuation scale. As M is monic with rational coefficients, its elementary symmetric coefficients are integral. Its reduction is

    M_bar=(Z-z0)^11,     U_bar=-sigma_bar^2.

The latter follows from x_O=s^2 X_O with X_O_bar=1; the other terms of U have positive valuation.

Suppose B_s were A11. Its two rational field factors would give two distinct rational roots of F. Exactly one can be x_O, so at least one cusp root z_R is rational. Its residue is z0. Translate and divide:

    G(W)=M(z_R+W)/W.

This is monic integral of degree ten with G_bar=W^10. Because M(z_R)=0 and R=UM,

    G(0)=M'(z_R)=R'(z_R)/U(z_R),
    (G(0)/11)_bar=z0^10=1.

The last equality holds for every z0 in F11^*. Hence G is Eisenstein, not merely a candidate factor with repeated reduction. Its root w is a uniformizer of a totally ramified degree-ten field L'. Dividing G(w)=0 by eleven and reducing at w gives

    (w^10/11)_bar=-1.

All intermediate terms vanish after this division: their coefficients are divisible by eleven and their positive powers of w have positive valuation. The factorization of the **entire** fiber is now Q11 × Q11 × L'. Therefore compatibility with A11 requires L' isomorphic to L; fields of degrees one and ten cannot be interchanged.

Under such an isomorphism w is a uniformizer of L. L041's r satisfies r^10=-55. The unit w/r has residue in F11^*, whose tenth power is one, forcing

    (w^10/11)_bar=(r^10/11)_bar=-5.

This contradicts -1. The contradiction covers every rational-factor permutation and every isomorphism or embedding of the ramified factor. If there is no rational cusp root, the two rational factors already fail, so that case is covered as well. No compatible fiber exists, and there are no vectors to realize in this scalar region.

For the global consequence, a primitive integer solution gives primitive Z11 coordinates. If 11 divides C, reducing the equation shows A and B are both units; hence v11(s)=-11v11(C)<0. L033's transported full fiber would give the prohibited isomorphism after base change. Thus 11 cannot divide C within this branch. This is a necessary condition only, not branch emptiness.

### Evidence, threshold and remaining cases

Run `python3 scripts/primitive-eleven-vectors/check_negative_scalars.py`. The full [certificate](../scripts/primitive-eleven-vectors/negative-scalar-certificate.json) records the exact shifted coefficients, all affine coefficient bounds for k>=1, complete derivative bounds, every infinity-scaling term and all ten unit residue cases. All 13 checks pass. The complete load-bearing bound tables, infinity terms and unit cases were inspected. Actual degree-ten constant/11 residue is 1; required for L is 5. The uniform proof above supplies root counts, factor irreducibility and whole-fiber coverage beyond those finite arithmetic checks.

Actual proved negative-slice vector count: zero. Required full target: a complete set with necessity and realization for all primitive compatible scalars. The two integral branch disks remain unresolved, including exceptional evaluation at j(T); no claim is made that L042's two vectors exhaust the full image. Global unit/class data, class intersections, the other twists and infinitely many signatures remain independent gaps. This is local progress under assessed methods, not a result beyond the checked literature or a Beal resolution.

## Mathlib

Full matching negative-scalar exclusion, simultaneous fiber factorization and degree-ten field comparison: **not checked**. Supporting Hensel, Eisenstein, complete-field valuation, polynomial reconstruction and finite-map declarations: **not checked**. Unknown coverage is not evidence of absence.
