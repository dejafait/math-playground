# L047 — A primitive three-adic realization of the entire canonical fiber

## Hypotheses

Work over Q3, with valuation ring Z3 and v3(3)=1. Let j:E0 -> P1 be L034's degree-twelve **modular** map on the smooth projective model

    E0: y^2+y=x^3-x^2-10x-20.

Let K be L033's degree-twelve field for 54a1, defined over Q by

    k^12-6k^10+6k^9-6k^8-126k^7+104k^6+468k^5
      +258k^4-456k^3-1062k^2-774k-380.

For s in Q3 write B_s for the coordinate algebra of the **entire scheme-theoretic fiber** j^-1(s). This includes every factor and multiplicity, not a selected point. L032's relevant three-adic conditions are a=1 modulo 3, b^2=1 or 4 modulo 9, and c a unit. No positivity, parity or two-adic condition is imposed on a three-adic witness.

Imported inputs:

- Freitas, Naskręcki and Stoll (FNS), *The generalized Fermat equation with exponents 2, 3, n*, **Compositio Mathematica 156 (2020), 77–113**, [DOI](https://doi.org/10.1112/S0010437X19007693), [final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf), internally June 10, 2019. Section 5, printed pp.17–18, supplies the local pair (X,Y,E)=(13,7,54a1) and its covariant verification criterion. Section 7.2, printed p.25, identifies the canonical entire fiber through all twelve cyclic order-eleven subgroups and states irreducibility and degree twelve; Table 5, printed p.27, supplies K's polynomial. This field identification precedes the GRH-dependent Selmer calculation; neither that calculation nor the conditional complete classification is used.
- Pete L. Clark, *Algebraic Number Theory II: Valuations, Local Fields and Adeles*, [author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf), accessible 161-page version inspected 2026-10-10, revision date unidentified, Theorem 1.79, printed p.58. For a complete nonarchimedean field, an integral polynomial f and integral approximation r, |f(r)|<|f'(r)|^2 gives an integral root beta with |beta-r|<|f'(r)|. This is the previously assessed Hensel–Newton input.

No primitive integer solution, class-group evaluation, rank, Sha condition, GRH or equality of Selmer and point classes is assumed.

## Conclusion

There exist a,b,c in Z3^* with

    a=7, b^2=13, c^11=512, a^3+b^4=c^11,
    a=1 modulo 3, b^2=4 modulo 9, c=-1 modulo 3.

They form one common primitive witness triple: min(v3(a),v3(b),v3(c))=0. For this same triple,

    s=1728 a^3/c^11=9261/8=j(54a1),
    s=-27+243*(39/8) in -3^3+3^5 Z3,
    1728-s=1728 b^4/c^11,
    B_s isomorphic to K tensor_Q Q3.

Thus the approved primitive three-adic whole-fiber existence test has a realization. Local nonexistence at three cannot exclude 54a1 under these conditions. This does not determine a connecting-image subset, a global class intersection or an integer solution.

## Proof

### Exact common primitive witnesses

Set a=7. Apply the cited Hensel–Newton theorem in the complete field Q3 to F(U)=U^2-13 at r=1. The polynomial and approximation are integral, and

    F(1)=-12, v3(F(1))=1,
    F'(1)=2, v3(F'(1))=0,
    |F(1)|3=1/3<1=|F'(1)|3^2.

There is therefore an exact b in Z3 with b^2=13 and |b-1|3<1. Hence b=1 modulo 3 and b is a unit; its square is 4 modulo 9.

For G(V)=V^11-512 use r=-1. Again coefficients and approximation are integral, and

    G(-1)=-513=-27*19, v3(G(-1))=3,
    G'(-1)=11, v3(G'(-1))=0,
    |G(-1)|3=1/27<1=|G'(-1)|3^2.

Hensel–Newton supplies an exact c in Z3 with c^11=512 and |c+1|3<1, so c=-1 modulo 3 and c is a unit. Also a is a unit and a=1 modulo 3. Since b^4=169 and 7^3=343, their sum is 512=c^11. These **same** b and c give the required equation. All coordinates are nonzero units, proving primitivity and the three-adic residues. No cube equation is lifted at three: a is fixed. No fourth-root surjectivity is assumed: the square equation constructs b.

### The scalar is exactly the canonical invariant

The common witness gives

    s=1728*343/512=9261/8,
    1728-s=(13824-9261)/8=4563/8=1728*169/512.

Moreover s+27=9477/8=243*(39/8); 39/8 lies in Z3. Thus s is in the source Table 2 disk for X=4 modulo 9 and Y=1 modulo 3. It is neither 0 nor 1728 nor infinity.

Disk membership alone would not identify the entire fiber. Import FNS's explicit pair (X,Y,E)=(13,7,54a1) and its accompanying covariant verification: there is nonzero d in Q3 with X=c6(E)d^3 and Y=-c4(E)d^2. The standard elliptic invariant identities 1728 Delta=c4^3-c6^2 and j(E)=c4^3/Delta give

    j(E)=1728 c4(E)^3/(c4(E)^3-c6(E)^2)
        =1728 Y^3/(Y^3+X^2)
        =1728*343/512=s.

The common factor d^-6 cancels, and X^2+Y^3=512 is nonzero. No global isomorphism of the local Frey curve with E is needed; quadratic twists also have the same j-invariant. Both j(E) and s are rational numbers, so equality in Q3 implies equality in Q. The invariant identities and Frey j formula also underlie FNS equation (2.2), already used in L032. Here j(E) is the constant invariant of E=54a1; B_s uses the nonconstant modular map on E0.

### Entire-fiber base change

Let Z=j^-1(s) be the fiber over Q and D_s=Gamma(Z,O_Z). L034's complete-map interface supplies a finite locally free degree-twelve morphism whose branch values are 0,1728,infinity. Since s avoids them, Z is finite etale of degree twelve over Q. This is characteristic-zero etaleness; no good reduction at three is asserted.

The equality s=j(E) makes Z exactly the canonical fiber in FNS Section 7.2. The source identifies its **whole** geometric Galois set with all twelve cyclic order-eleven subgroups of E[11], states that this canonical fiber is irreducible of degree twelve, and identifies its residue field K_E by Table 5. Its displayed polynomial is exactly L033's polynomial for K. A finite etale irreducible Q-scheme has a field as coordinate algebra. Hence the cited whole-fiber and field identification yields D_s isomorphic to K. This uses the Galois action and actual field identification, rather than matching dimensions or selecting a K-valued point of possibly smaller degree.

Formation of a scheme-theoretic fiber commutes with base change. Z is affine and finite, so its base change to Q3 has coordinate algebra D_s tensor_Q Q3. It is exactly the fiber defining B_s, and therefore

    B_s=D_s tensor_Q Q3 isomorphic to K tensor_Q Q3.

Every local factor and its degree is retained. There are no nonreduced multiplicities in this fiber because etaleness survives base change. No fresh local factorization is required. This argument uses the projective modular map itself, not an elimination polynomial or y-reconstruction denominator, so no point at x=16 or at a zero of a coordinate denominator is deleted. L034's exceptional-chart verification is part of the map interface. Also s differs from j(2T)=-121, j(T)=-24729001 and j(4T)=-32768; O and 3T lie over infinity. No exceptional descent evaluation is needed.

One fixed a,b,c and s apply on every factor; the construction never chooses separate right-hand witnesses on different factors. This proves the conclusion.

### Scope and stopping decision

This is REPRODUCTION under the saved SPECIALIZE assessment. FNS supplies the local pair and canonical fiber; the square-coordinate/common-c applicability is the bounded specialization proved above. General Hensel lifting and the modular field computation are imported, not reproved. No progress beyond the sources checked is claimed.

One exact realization meets the continuation test and retires local nonexistence at three under these conditions. It does not establish equality of primitive and unrestricted three-adic connecting images; that would be another target requiring separate assessment. No descent class is evaluated. L045's quotient classes remain unevaluated; the unconditional global 54a1 intersection, the other four twists and infinitely many signatures remain open. Since 13 is strictly between 3^2 and 4^2, b is not an integer, so this local witness is not a Beal counterexample. STATUS remains IN_PROGRESS; the independent application audit below confirms this local conclusion only.

### Critical application audit, 2026-10-10

The independent audit finds no mathematical correction. It reuses L032's
residue interface, L033's exact field definition and L034's complete
projective map; their global-solution hypotheses are not assumed for
this existence construction. Only their unconditional map and field
data are used. The audited tests are exact, not finite-precision root
approximations.

For Clark Theorem 1.79 the field Q3 is complete and both polynomials
are in Z3[U], with integral initial points. Recomputing the evaluations
gives F(1)=-12 and F'(1)=2, and G(-1)=-513=-3^3*19 and
G'(-1)=11. Thus the required strict valuation inequalities are 1>0
and 3>0, respectively. The root-distance conclusion puts b in 1+3Z3
and c in -1+3Z3. The cube coordinate 7 is fixed, so no derivative
divisible by three enters either application. The identities
7^3=343, 13^2=169 and 343+169=512 verify the equation with these
same roots. Each coordinate has valuation zero; b^2=4 modulo nine,
a=1 modulo three and c is a unit, exactly as required by L032's
54a1 three-adic row. Conditions at two are outside this local claim.

Recomputing the scalar gives 1728/512=27/8 and hence s=9261/8.
The complementary numerator is 13824-9261=4563=27*169, and
9261+216=9477=243*39. This checks both common-c identities and
the specified disk. Both numerators are nonzero, so no branch value
0,1728 or infinity occurs.

The FNS Section 5 pair and scaling criterion (printed pp.17–18)
were checked directly. Substituting X=c6*d^3 and Y=-c4*d^2 gives
Y^3=-c4^3*d^6 and X^2+Y^3=(c6^2-c4^3)*d^6. Both minus signs
cancel in 1728Y^3/(X^2+Y^3). Here d is nonzero and the denominator
is 512, so cancellation is legitimate. Equality of rational invariants
can be read through the injective map Q -> Q3.

FNS Section 7.2, printed p.25, identifies the canonical fiber's
twelve-subgroup Galois set and irreducible degree-twelve field.
Every coefficient of its Table 5 polynomial, p.27, agrees with the
K in the hypotheses. The GRH assumption follows at the separate
Selmer computation; no Selmer dimension is used. This imports the
source field computation without claiming an independent rerun.

L034's finite locally free map and branch locus make the rational
fiber Z finite etale. The canonical identification therefore concerns
its whole coordinate field D_s, not a smaller residue subfield.
Apply [Stacks Lemma 26.17.2, tag 01JQ](https://stacks.math.columbia.edu/tag/01JQ)
to X=Spec(D_s), Y=Spec(Q3), S=Spec(Q). Its tensor-product proof
gives Spec(D_s tensor_Q Q3). Associativity of this same fiber product
identifies it with the fiber of the base-changed j-map at s. Thus all
factors of K tensor_Q Q3 occur, with total dimension twelve and no
nilpotents. Etaleness here is over characteristic-zero fields and
does not presume unramified reduction at three. The projective map
requires no affine-coordinate division; the separately listed
exceptional torsion scalars also differ from s. No new factorization
or choice of a distinct c for different factors is needed.

This is REPRODUCTION verification of the existing application. It
confirms the local-nonexistence stop, without a new restriction,
connecting-image determination, global intersection or integer solution.

## Mathlib

Full matching three-adic whole-fiber realization and FNS field identification: **not checked**. Supporting Hensel–Newton, elliptic-invariant, finite-etale algebra and fiber/base-change declarations: **not checked**. Unknown coverage is not evidence of absence. The named primary sources supply the imported inputs.
