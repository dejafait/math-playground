# L042 — Eleven-adic generic integral vectors and whole-fiber nonemptiness

## Hypotheses

Use L033's curve and normalized dual connecting class,

    E0: y^2+y=x^3-x^2-10x-20,
    f=(x-4)y-4x^2+30x-55,

and L034's complete modular map j=(a+by)/d and necessary polynomial

    F(x,s)=h(x)^3+J(x)s-d(x)s^2,
    J=2a-b, d=(x-16)^11.

The polynomials a,b,h,J are precisely those of L034, with full integral coefficients in its audited certificate. Let A11, the ordering of its factors and the primitive whole-fiber image be exactly L041's. Thus A11 is Q11 × Q11 × L, with L=Q11[r]/(r^10+55), and its normalized ramification/residue pairs are (1,1),(1,1),(10,1). Allow every isomorphism of the entire modular fiber B_s with A11, including both rational-factor permutations and all ramified embeddings. The generic integral slice means s in Z11 with residue outside {0,1}; in particular s is not a branch value 0,1728 or infinity. No global solution, positivity, other-place condition, class basis, GRH or precision cutoff is assumed.

## Conclusion

In this slice, whole-fiber compatibility forces s=4 or 10 modulo eleven. The exact valuation-vector image of compatible primitive fibers **within this slice** is

    {(0,2,0), (2,0,0)} in (Z/5Z)^3.

Both vectors occur at the same exact scalar, arising from the rational point x=500, y=60+121v, where v is the Hensel root of v^2+v-8520 with residue 2. Its scalar j has residue 4, its entire fiber algebra is A11, and L041 gives common nonzero primitive a,b,c in Z11. This proves nonemptiness of the full restricted image as well.

The result does **not** determine the full vector set. Scalars congruent to 0 or 1 modulo eleven and negative-valuation scalars may contribute further vectors. In particular the other 23 norm candidates of L041 are not excluded from that full image. No global class intersection or integer branch exclusion follows.

## Proof

### Imported results and the identified specialization

L034 supplies the complete degree-twelve map, its necessary polynomial relation and the fact that its only branch values are 0,1728,infinity, from Freitas–Naskręcki–Stoll, *The generalized Fermat equation with exponents 2, 3, n*, Compositio Math. **156** (2020), 77–113, [final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf), June 10, 2019, Section 7.2, pp.25–27, equation (7.4). Its coefficients and reconstruction identity were independently audited in L034. L033 supplies the ordinary and good-divisor connecting evaluation by Schaefer–Stoll's cited descent theorem; no general descent theorem is reproved here.

For simple roots and Eisenstein extensions use Pete L. Clark, *Algebraic Number Theory II: Valuations, Local Fields and Adeles*, [161-page author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf), no identified revision date, Theorem 1.79, printed p.58, and Proposition 2.9/Corollary 2.10, p.65. These inputs were inspected in the unchanged SPECIALIZE assessment and foundation 17. The general Hensel and Eisenstein statements are imported. The remaining work is explicit simultaneous fiber arithmetic and the field comparison, which those theorems do not state. No Tate uniformization, tame-extension classification or general local-image theorem is needed.

### All twelve roots and a uniform rescaling

Write bars for reduction modulo eleven. Exact coefficient identities give

    hbar=(x-5)^4, Jbar=dbar=(x-5)^11, bbar=(x-5)^10,
    Fbar_s=(x-5)^11(x-5+s-s^2).

Since sbar is neither 0 nor 1, the last factor has a simple root x_sm=5-s+s^2 modulo eleven distinct from 5. Hensel gives exactly one rational root in that disk, with unit derivative. All other eleven roots reduce to 5. F is monic integral; hence all its roots in an algebraic closure are integral. The fiber is unramified at this scalar; reconstruction below will identify its twelve distinct points with these roots.

Expand F(16+W,s)=sum c_i(s) W^i. The exact coefficient evidence proves uniformly on this slice

    v11(c_0)=22, v11(c_11)=v11(c_12)=0,
    v11(c_i)>=23-2i for 1<=i<=10.

Indeed c_0=11^22(s+121), c_12=1, and c_11 has residue s(1-s). The intermediate bounds hold separately for the h^3,J,d coefficients, so cannot be weakened by cancellation in the scalar. Here and below valuation is extended to algebraic extensions with v11(11)=1; ord_L=10 v11.

For any root reducing to 5, W=x-16 has positive valuation h0. If 0<h0<2, c_11 W^11 is the unique term of lowest valuation: its valuation is 11h0, while c_0 has valuation 22, the intermediate terms have valuation at least 23-2i+i h0>11h0, and W^12 has valuation 12h0>11h0. If h0>2, c_0 is uniquely lowest instead. Neither is possible in a zero sum. Thus every cluster root has v11(W)=2.

Put Z=W/121. The polynomial

    R_s(Z)=F(16+121Z,s)/11^22

has integral coefficients, and

    Rbar_s=s((1-s)Z^11+1).

Every cluster root has integral Z with the unique residue

    z0=1/(sbar-1).

This residue is nonzero and is not -1. The unique-minimum argument treats arbitrary algebraic roots, not just a finite precision sample.

### Reconstruction and every connecting valuation in the slice

Let B(Z)=b(16+121Z)/11^20 and N(Z)=(a(16+121Z)+60b(16+121Z))/11^22. Both have integral coefficients, with complete reductions

    Bbar=(Z+1)^10,
    Nbar=1+5Z+6Z^2+5Z^3+6Z^4+5Z^5+6Z^6
           +5Z^7+6Z^8+5Z^9+6Z^10+6Z^11.

For a cluster root, B is a unit because z0 is not -1. In particular b is nonzero, and the unique reconstructed ordinate is

    y=(sd-a)/b=60+121V,
    V=(s Z^11-N(Z))/B(Z).

On each of the nine possible nonzero residues z0 different from -1, Nbar(z0)=1+6z0 and Bbar(z0)=1. Since sbar z0=z0+1, this gives Vbar=6z0. These nine cases are exhaustively recorded in the certificate; this is an identity on the finite residue field, not a claim that residue samples determine the whole fiber.

Direct substitution gives

    f/121=1-38Z+12V+121(ZV-4Z^2).

Its residue is 1+z0, which is nonzero. Thus every cluster point has v11(f)=2, through every embedding. At the smooth point x_sm, b and x_sm-5 are units. Reconstruction supplies an integral ordinate. The identity f(P)f(-P)=-(x(P)-5)^5 from L033 then forces f(P) to be a unit: both factors are integral and their product is a unit. Consequently its connecting valuation is zero.

This also justifies the complete fiber presentation. Every root has b nonzero (a unit at the smooth root, valuation twenty at cluster roots), and no root is x=16 since F(16,s)=11^22(s+121) is nonzero. L034's elimination identity reconstructs a point with modular scalar s at every root. Conversely every finite-fiber point is affine, satisfies F=0, and is accounted for by this reconstruction. A separable degree-twelve fiber has length twelve; therefore B_s=Q11[x]/(F(x,s)), with all twelve points retained.

If B_s is isomorphic to A11, its rational factors supply the smooth point and one cluster point. Its degree-ten factor supplies a cluster point. Their normalized f-valuations are respectively 0,2,20; modulo five the last is zero. The rational-factor permutations give precisely the two possible vectors in the conclusion. This argument retains every ramified embedding; valuations are invariant under local field isomorphisms. The points are away from T,O and x=16 in this slice, so ordinary nonzero f evaluations suffice. The excluded exceptional scalar j(T) has residue 0 and is left for the remaining disks, rather than assigned an ordinary zero Kummer value here.

### The ramified field test is simultaneous, not an independent-point test

Remove the smooth root and rescale its monic degree-eleven factor:

    M_s(Z)=121^-11 [F(x,s)/(x-x_sm)] at x=16+121Z.

Every root of M_s is integral by the preceding valuation proof. Thus its elementary symmetric coefficients are in Z11, and Mbar_s=(Z-z0)^11. Exactly,

    R_s(Z)=U_s(Z) M_s(Z),
    U_s(Z)=121Z+16-x_sm,    Ubar_s=sbar(1-sbar)=lambda.

Suppose a rational cluster root z_R exists, as it must under whole-fiber compatibility. Set G(W)=M_s(z_R+W)/W. This is monic integral of degree ten, with Gbar=W^10 and G(0)=M_s'(z_R)=R_s'(z_R)/U_s(z_R).

The coefficients of R_s' are divisible by eleven. Reduction of R_s'/11 depends only on sbar and z0; all nine cases are as follows:

| sbar | z0 | (R_s'/11)(z0) | lambda | C=G(0)/11 |
| --- | --- | --- | --- | --- |
| 2 | 1 | 4 | 9 | 9 |
| 3 | 6 | 9 | 5 | 4 |
| 4 | 4 | 6 | 10 | 5 |
| 5 | 3 | 8 | 2 | 4 |
| 6 | 9 | 3 | 3 | 1 |
| 7 | 2 | 6 | 2 | 3 |
| 8 | 8 | 2 | 10 | 9 |
| 9 | 7 | 4 | 5 | 3 |
| 10 | 5 | 1 | 9 | 5 |

All entries are in F11. In particular G(0) has valuation exactly one, so G is Eisenstein and its root w is a uniformizer in a totally ramified degree-ten field. Dividing G(w)=0 by eleven and reducing modulo w yields w^10/11=-C: every intermediate term has positive valuation after this division.

If this field is L, compare w with L041's uniformizer r satisfying r^10=-55. The unit w/r has residue in F11^*, whose tenth power is one. Therefore w^10/11 has residue -5, and C must be 5. The table forces sbar in {4,10}. This necessary condition uses the actual degree-ten whole-fiber factor, not a point chosen independently over L.

Conversely, if C=5, (-55)/w^10 has residue one. Hensel on Z^10-(-55)/w^10 at 1, with unit derivative 10, supplies a unit u such that (wu)^10=-55. The polynomial X^10+55 is Eisenstein over Q11; hence Q11(wu) has degree ten and is the whole field Q11(w). It is isomorphic to L. This proves the field comparison without assuming a finite-precision factorization is exact.

### An exact common scalar realizes both vectors

Take Z=4, x=16+121Z=500. The curve equation with y=60+121V becomes

    V^2+V=6Z+47Z^2+121Z^3=8520.

At V=2 modulo eleven this equation has residual value zero and derivative 2V+1=5, a unit. Hensel gives an exact V in Z11. Put P_R=(500,60+121V) and s=j(P_R). At x=500 the exact coefficient calculations give v11(b)=20, v11(a+60b)=22 and v11(d)=22. The residues of (a+60b)/11^22, 121b/11^22 and d/11^22 are respectively 3,1,4. Thus sbar=(3+2)/4=4. In particular s and s-1728 are units and s is in the generic slice. Also f(P_R)/121 has residue 5.

This is a rational cluster point at the original shared scalar s. The smooth root is rational by the first Hensel argument. Removing these two roots gives exactly the degree-ten Eisenstein factor above, with C=5, so its field is L. Reconstruction consequently identifies the entire B_s with Q11 × Q11 × L=A11. This supplies generation of the entire fiber algebra, not only selected component points. The two isomorphic rational factors can be sent to L041's ordered rational completions in either order, and every embedding of the remaining factor has the same valuation. Both listed vectors are therefore realized.

Since v11(s/1728)=v11(1-s/1728)=0, L041's exact scalar-domain theorem supplies common nonzero integral primitive a,b,c with a^3+b^4=c^11 and this very scalar s. It does not require an eleventh-root argument. These witnesses leave P_R, s and the whole-fiber isomorphism unchanged. They are local witnesses only.

### Evidence, threshold and qualifications

Run `python3 scripts/primitive-eleven-vectors/check_generic_fibers.py`. The full [certificate](../scripts/primitive-eleven-vectors/generic-fiber-certificate.json) records the shifted components, exact integral scalings, derivative polynomials, all nine residue cases and the exact point's Hensel data. All 20 checks pass; the complete relevant valuation arrays, residue tables, polynomial reductions and point data were inspected. The proof above establishes the uniform valuation and lifting statements beyond those finite arithmetic checks.

Actual proved generic slice: two vectors, with necessary scalar residues {4,10} and complete whole-fiber realizations. Required full target: all primitive compatible scalars; L041 still leaves 25 norm candidates globally. The branch disks s=0,1 modulo eleven and v11(s)<0 remain unresolved, including good-divisor evaluation at j(T). Neither the table nor nonemptiness decides whether these disks contribute further vectors or whether the full vector set improves the inherited norm plane. All independent global gaps remain.

## Mathlib

Full matching generic-slice theorem, simultaneous fiber construction and valuation vectors: **not checked**. Supporting Hensel, Eisenstein, polynomial reconstruction and local norm declarations: **not checked**. This is REPRODUCTION under the preexisting SPECIALIZE assessment; it establishes local arithmetic progress without claiming novelty beyond the assessed source methods or completion of the exact vector target.
