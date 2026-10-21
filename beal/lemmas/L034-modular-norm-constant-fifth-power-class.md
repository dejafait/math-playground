# L034 — The modular norm has constant fifth-power class

## Hypotheses

Let E0, T=(5,5), O and f=(x-4)y-4x^2+30x-55 be as in L033, on the smooth projective curve y^2+y=x^3-x^2-10x-20 over Q. Let j:E0 -> P1 be **the modular map**, of degree twelve, in Freitas–Naskręcki–Stoll (FNS), *The generalized Fermat equation with exponents 2, 3, n*, Compositio Math. 156 (2020), 77–113, [June 10, 2019 final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf), Section 7.2, printed pp.25–27, modular formula and equation (7.4). Write its formula as j=(a(x)+b(x)y)/d(x), where d=(x-16)^11 and a,b are the exact source polynomials. Their complete coefficients, including both factors of b, are transcribed in scripts/five-isogeny-modular-norm/check_norm.py and its certificate.

For the arithmetic specialization assume all L033 hypotheses: positive primitive A^3+B^4=C^11, the 54a1 branch, its specified degree-twelve field K, and the transported point P0 with j0=1728 A^3/C^11 and (1728-j0)C^11/1728=B^4. No certified unit/class basis, GRH, rank or Sha condition is assumed.

## Conclusion

The function-field norm is exactly

    N_{Q(E0)/Q(j)}(f)=11^22 (j+24729001)^5.

Consequently its class in Q(j)^*/Q(j)^{*5} is the constant [11^2]. On the transported solution fiber,

    N_{K/Q}(f(P0))=11^22 (1728 A^3/C^11+24729001)^5,

so its class in Q^*/Q^{*5} is also [11^2], independent of A,B,C. This is a necessary norm identity, not an exclusion. It fails the approved requirement of nonconstant fifth-power-class information. It does not compute the original K(S,5) classes or show their local intersections are empty.

## Proof

### The complete map and its exceptional coordinates

Put g=x^3-x^2-10x-20 and

    h=x^4-52820x^3+1333262x^2+4971236x+9789217,
    J=2a-b,
    F(x,j)=h^3+Jj-dj^2.

Exact polynomial multiplication verifies both the complete source coefficient list for J in (7.4) and

    a^2-ab-b^2g=-d h^3.

Indeed eliminating y=(jd-a)/b from y^2+y=g gives

    (jd-a)^2+b(jd-a)-b^2g=-d F(x,j).

The polynomial F is monic of degree twelve in x. In the generic function field b is nonzero, so this reconstruction gives Q(E0)=Q(j)(x), with y determined uniquely. The source degree-twelve theorem therefore makes F the minimal polynomial, rather than a degree-twenty-four model that also counts the x-involution. No assertion of a coordinate presentation at every exceptional specialized j is needed.

There is no hidden deletion at x=16. L033 gives the two points 2T=(16,-61) and 3T=(16,60), where x-16 is a local parameter because 2y+1=±121. At 3T the numerator a+by equals 81402749386839761113321, which is nonzero, so j has a pole of order eleven. At 2T the numerator vanishes. The involution sends these points to one another, and the polynomial identity gives

    (a+by)(a+b(-y-1))=-d h^3.

Since h(16) and the second factor at 2T are nonzero, the first factor has order exactly eleven. Its denominator cancels completely; the resulting value is j(2T)=-121. This includes the point rather than removing it from the map.

At O use L033's parameter t=-x/y: x~t^-2 and y~-t^-3. The degrees and leading coefficients of a,b,d are respectively (11,743), (10,1), (11,1). Thus j~-t^-1 and has a simple pole. The displayed expression has no other possible poles. Its pole divisor is therefore (O)+11(3T), consistent with degree twelve. At T the exact value is j(T)=-24729001; at 4T it is -32768. L033's polynomial f is regular at x=16, with f(2T)=-1331 and f(3T)=121.

### Divisor of the norm

Import [Stacks Project, Lemma 42.18.1, tag 02RT](https://stacks.math.columbia.edu/tag/02RT). For a dominant proper morphism between integral curves it identifies the divisor of a rational-function norm with the pushforward divisor. Here both curves are smooth projective integral over Q, j is nonconstant and proper, and f is a nonzero rational function. L033 gives div(f)=5(T)-5(O). Both T and O, and their images, have residue field Q; the pushforward weights are residue-field degrees one, **not** the ramification indices of j. Hence

    div(N(f))=5(-24729001)-5(infinity).

On P1 the rational function j+24729001 has divisor (-24729001)-(infinity). The quotient N(f)/(j+24729001)^5 has no zeros or poles, so it is a nonzero rational constant c. This determines the shape, not the scalar.

### Exact scalar from a complete regular fiber

Choose j=1. Let F1=h^3+J-d and define

    A_f=-4x^2+30x-55,   B_f=x-4,
    G1=A_f b+B_f(d-a).

Exact determinants give F1(16)=9931135425194450855825162, Res(F1,b) nonzero, and Res(F1,F1') nonzero. The full integers are stored in the certificate's fiber_at_1 object. Thus F1 is monic, degree twelve, squarefree, and none of its roots is 16 or a zero of b. For each of its twelve geometric roots, y=(d-a)/b satisfies the curve equation by the elimination identity and has modular j=1. Conversely every point of that fiber is finite, has x different from 16, and arises this way. These twelve points exhaust the degree-twelve fiber. In particular its finite algebra is Q[x]/(F1), not a selected field factor or half of a fiber.

On this algebra f=G1/b. For monic squarefree F1 the determinant norms equal the products over its twelve roots, hence their ratio is Res(F1,G1)/Res(F1,b). Using full exact integer Sylvester determinants, with checked exact divisions in fraction-free elimination, gives

    N(f)|_{j=1}=752786846314989488999297147841293520385534848541942436346272
              =121^11 * 24729002^5.

It follows that c=121^11=11^22. This is a complete regular-fiber evaluation, not a numerical preview. The generic norm agrees with this specialized determinant by the base-change theorem explained next. As a consistency check, the O branch has f/j^5 tending to one, while the eleven branches meeting 3T have f tending to 121; their product has leading coefficient 121^11. This check is not needed as a separate premise for the scalar computation.

### Specialization, including branch fibers

Import [Stacks Lemma 53.2.4, tag 0CCL](https://stacks.math.columbia.edu/tag/0CCL) for finiteness of the nonconstant proper curve map, [Lemma 53.2.3, tag 0CCK](https://stacks.math.columbia.edu/tag/0CCK) for flatness over the normal target curve, and [Section 29.49, tag 02K9, Lemma 29.49.2](https://stacks.math.columbia.edu/tag/02K9) for finite local freeness on this locally Noetherian target. The degree is twelve. Import [Lemma 31.18.6, tag 0BD2](https://stacks.math.columbia.edu/tag/0BD2): the determinant norm is compatible with arbitrary base change.

On U=P1 minus {-24729001,infinity}, f is regular and invertible on j^-1(U), because its only zero and pole are T and O. Thus the theorem specializes the rational norm to the determinant norm on the **whole** fiber algebra for every value in U. In particular it justifies the preceding j=1 computation. It also includes j=0 and j=1728 even though their fibers are ramified and possibly nonreduced: multiplication by f is invertible and its determinant is the displayed nonzero value. No simple-root or product-of-distinct-points assertion is used for those branch fibers.

At j=-24729001 the rational norm has a zero of exact order five. The actual modular fiber is unramified, since FNS's only branch values are 0,1728,infinity; at T, f is regular but zero. Its determinant norm on that fiber is zero, so there is no fifth-power class there. At infinity f has a pole at O, and the rational norm has a pole of exact order five, even though the other cusp 3T has ramification eleven and unit f-value 121. No finite field-norm evaluation or Kummer class for f is asserted at infinity. L033's good-divisor evaluations remain the appropriate descent values at T and O; they are not substituted into this rational-function norm.

For an original solution 0<j0<1728, so j0 belongs to U and is not a branch value. L033 imports FNS's complete fiber transport: P0 has residue field K of degree twelve. Evaluation at P0 is a surjection from the rational fiber algebra, of dimension twelve, to K, also of dimension twelve. It is therefore an isomorphism. The specialized determinant is exactly N_{K/Q}(f(P0)), over all twelve embeddings, not the norm of one local factor. This proves the claimed field-norm identity while retaining the full fourth-power condition, positivity, primitivity and 54a1 restrictions.

Finally 11^22=11^2(11^4)^5. Consequently the class is constant [11^2] both generically and on every permitted rational specialization. This constant is nontrivial over Q: its 11-adic valuation is two, not a multiple of five. It is also nontrivial over Q(j), since a rational function whose fifth power is constant must be constant, and Q is the constant field. Nontriviality of a constant class is not nonconstant information about j. It may express a fixed norm constraint on descent representatives, but the approved variation test is not met. No original solution, empty Selmer intersection, height bound or signature exclusion follows.

### Verification and qualification

Run `python3 scripts/five-isogeny-modular-norm/check_norm.py`. The full certificate is [scripts/five-isogeny-modular-norm/norm-certificate.json](../scripts/five-isogeny-modular-norm/norm-certificate.json). All fourteen checks pass, including the two elimination identities, degree-twelve regular-fiber model, complete scalar determinant and constant-class factorization. The actual nonconstant-class flag is false, against the required true. The full residuals, torsion evaluations, fiber determinants and norm were inspected, not merely their previews.

The general norm/divisor and base-change results are imported; only this explicit specialization is calculated. Its existing assessment did not locate a matching normalized formula, which does not certify novelty. This result supplies a negative decision for compression, while the original isogeny descent, four other twists and infinitely many signatures remain unresolved. The separate critical review below confirms this calculation without strengthening its arithmetic conclusion.

### Critical audit, 2026-10-08

The audit found no mathematical correction. Every coefficient of a, both factors of b, h and J was compared with FNS Section 7.2, printed pp.26–27, including equation (7.4). The field-transport paragraph on p.25, Table 5 on p.27 and the y-reconstruction qualification in Lemma 7.6's proof on p.28 were rechecked. The exact Stacks statements and proofs cited above were also rechecked; 02K9 is the section containing Lemma 29.49.2. No conditional Selmer result is imported.

Run `python3 scripts/five-isogeny-modular-norm/audit_norm.py`. This imports no construction code. It uses the certificate's coefficient lists as candidates, whose source coefficients were checked as just described. For x=0,...,24 it verifies the identities defining b, g, d, J, F1 and G1, and the elimination and descent x-norm identities. The respective degree bounds are 10,3,11,11,12,12,23,5: for the largest bound, b^2g and d h^3 have degree at most 23 and a^2 has degree 22. Each residual has 25 distinct exact zeros, more than its degree, so it is identically zero. This is polynomial identity verification, not sampled evidence. All original residuals and full polynomial lists were inspected.

For each q=b,G1,F1', the independent code constructs the twelve columns obtained by reducing q x^k modulo monic F1, for k=0,...,11. These are the multiplication matrices in the basis 1,x,...,x^11. Reduction subtracts the leading term times a shifted F1, so it preserves the quotient class and terminates in degree less than twelve. Ordinary Gaussian elimination over rational numbers computes their determinants: row replacement preserves the determinant, row exchange changes its sign, and the product of the final diagonal entries gives the result. This uses neither the original Sylvester matrices nor their fraction-free elimination. For monic F1, after extension to its splitting field the multiplication determinant equals the product q over all roots, hence exactly Res(F1,q) in the convention used above. No leading-coefficient or sign correction is missing; dividing the G1 determinant by the b determinant gives the norm of G1/b. The full three integers match the original resultants, including the nonzero derivative determinant, and the norm is exactly 752786846314989488999297147841293520385534848541942436346272. Division by 24729002^5 gives 81402749386839761113321=11^22. The complete [audit certificate](../scripts/five-isogeny-modular-norm/audit-certificate.json) retains all matrices, evaluations and determinants; all 20 checks pass. Full determinant, fiber, torsion and identity values were inspected.

The exceptional-coordinate argument also passes. At x=16, the curve derivative in y is ±121, so x-16 is a uniformizer at both points. The independently checked h(16)=214358881 is nonzero; the conjugate numerator at 2T is 81402749386839761113321. The product identity therefore forces exact order eleven of the vanishing numerator at 2T and gives the removable value -121. At 3T there is no cancellation. At O, the unique order-23 numerator term is the leading term of b y, with coefficient -1 in t=-x/y; the denominator has order -22 and coefficient one. Thus j has leading term -t^-1 and f has leading term -t^-5. These checks give the full pole divisor O+11(3T), independently verifying the degree used for the generic minimal polynomial. The four full torsion evaluations agree. No point is deleted by the coordinate denominator.

For j=1, the nonzero b determinant makes b invertible on Q[x]/(F1); F1(16) is nonzero and the derivative determinant proves twelve distinct geometric roots. Reconstruction yields twelve distinct points of the modular fiber, all with the displayed j-value. A finite locally free map of degree twelve has fiber length twelve, so these points account for its entire algebra, with no remaining point or multiplicity. For general specialization the smooth projective source is integral, the target is separated and normal, and the nonconstant map satisfies the finiteness and flatness hypotheses. Its connected locally Noetherian target makes the locally free rank equal to the generic degree twelve everywhere. On the complement of infinity f is regular, and on U it is invertible. Determinant base change thus includes the nonreduced fibers at 0 and 1728, gives zero at j(T), and does not assert a regular value at infinity. The divisor pushforward uses residue degrees one at T and O; ramification eleven at the other cusp does not multiply the pole order of the norm.

Finally, in the solution domain 0<j0<1728, FNS's irreducible twelve-subgroup Galois set supplies a closed point of residue field K, not merely a K-valued point with smaller residue field. The evaluation map from the twelve-dimensional whole fiber algebra onto K is surjective and therefore an isomorphism. This is why the determinant is the full field norm. Both original power identities remain premises. The class computation 11^22=11^2(11^4)^5 is exact; valuation two at 11 proves its nontriviality, but not variation with j. The required nonconstant-class flag is true and the actual flag is false. The audit therefore confirms the compression stop without excluding any branch or computing any global descent intersection. It is verification of the existing specialization, not a new mathematical restriction or a novelty claim.

## Mathlib

Full matching modular norm, scalar computation and transported-fiber specialization: **not checked**. Supporting norm/divisor, finite-flat base-change, determinant and resultant results: **not checked**. Unknown coverage is not evidence of absence; the precise primary inputs above suffice for this informal specialization.
