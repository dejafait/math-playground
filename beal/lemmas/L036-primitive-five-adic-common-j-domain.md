# L036 — Exact primitive five-adic common-j domain

## Hypotheses

Let v=v5 on Q5, normalized by v(5)=1, and let N0={0,1,2,...}. Fix j in Q5 minus {0,1728}, and set

    t=j/1728,  q=1-t=(1728-j)/1728.

Both t and q are nonzero. A primitive scalar witness means a,b,c in Z5 minus {0} with min(v(a),v(b),v(c))=0, satisfying

    a^3+b^4=c^11,  j=1728 a^3/c^11.

There is no positivity requirement, condition at another prime, or modular-fiber hypothesis. This is precisely the scalar-witness requirement appearing in L035; its full-fiber and descent conditions are additional conditions, not hypotheses here.

## Conclusion

A primitive scalar witness exists if and only if one of the following holds:

1. v(t) is in 3 N0 and v(q) is in 4 N0.
2. v(t)=-11 k for some integer k>=1; in this case v(q)=v(t) automatically.

Equivalently, the exact set D of such j is the following disjoint union, where Z5^* denotes the units:

    D = (1+5 Z5) union (2+5 Z5) union (4+5 Z5)
        union [union over m>=1 of 5^(3m) Z5^*]
        union [union over n>=1 of (1728+5^(4n) Z5^*)]
        union [union over k>=1 of 5^(-11k) Z5^*].

Every admitted j has a construction with b=5^beta, using the same c in both identities. This characterizes scalar witnesses only. It does not establish an image restriction relative to I_fiber, a local-image list, a global intersection, or any integer exclusion.

## Proof

### Imported local input and its precise specialization

Use Hensel–Newton as cited in [foundation 17](../foundations/17-local-power-hensel-inputs.md): Pete L. Clark, *Algebraic Number Theory II: Valuations, Local Fields and Adeles*, [author-hosted notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf), Theorem 1.79, printed p.58, in the 161-page version retrieved 2026-10-08 with no identified revision date. For a complete discretely valued field with valuation ring R, its hypothesis is f in R[X], r in R, and |f(r)|<|f'(r)|^2; it supplies a unique root within |beta-r|<|f'(r)|. We import this theorem, rather than reprove lifting. The unit decomposition also cited in foundation 17 is not needed for the construction below.

For n=3 or n=11, every U in Z5^* has a unique n-th root in Z5^*. Indeed, gcd(n,4)=1, so raising to the n-th power permutes F5^*. More explicitly n is 3 modulo 4 and its inverse modulo 4 is 3; the required root residue is Ubar^3. Choose its integer representative r in {1,2,3,4}. For f(X)=X^n-U, f(r) is divisible by 5 and f'(r)=n r^(n-1) is a unit. Hence |f(r)|<=1/5<1=|f'(r)|^2. The cited theorem supplies a root with the required nonzero residue. Every root in Z5^* has that same residue, and the uniqueness clause therefore gives uniqueness on the entire unit group. This verifies all lifting hypotheses; n is never divisible by 5. Only this unit specialization is needed, since nonunits will be handled by their exact valuations.

### Necessity: all primitive valuation cases

Suppose a,b,c is a witness and put alpha=v(a), beta=v(b), gamma=v(c). These are nonnegative integers with minimum zero. The two identities, both using the given c, are

    t c^11=a^3,  q c^11=b^4.

They imply

    v(t)=3 alpha-11 gamma,  v(q)=4 beta-11 gamma.

If gamma=0, these are exactly the nonnegative divisibility conditions in case 1. This includes both the all-unit case and the cases where just a or just b is a nonunit. Both a and b cannot be nonunits when c is a unit, since their powers would sum to a nonunit.

If gamma>0, primitivity ensures that at least one of a,b is a unit. If a is a unit then b^4=c^11-a^3 is a unit, because a unit minus an element divisible by 5 is a unit. Thus b is a unit. If b is a unit the symmetric subtraction a^3=c^11-b^4 makes a a unit. Consequently alpha=beta=0, and

    v(t)=v(q)=-11 gamma.

This is case 2, with k=gamma. These alternatives exhaust primitive witnesses; in particular a pattern with two nonunit coordinates has not been retained as an extra possibility.

### Sufficiency: explicit common-c construction at fixed j

Assume one of the stated cases and write r=v(t), s=v(q). In case 1 choose gamma=0. In case 2 choose gamma=-r/11, a positive integer. In case 2, since r<0, the nonarchimedean unequal-valuation rule applied to q=1-t gives s=r. Thus in both cases

    alpha=(r+11 gamma)/3,  beta=(s+11 gamma)/4

are nonnegative integers. In case 1 gamma=0; in case 2 alpha=beta=0. Hence min(alpha,beta,gamma)=0.

Normalize the units

    t0=5^(-r)t,  q0=5^(-s)q.

By the unit-root specialization above, choose u,w in Z5^* with

    u^11=q0^(-1),  w^3=t0 u^11.

Define

    a=5^alpha w,  b=5^beta,  c=5^gamma u.

These are nonzero integral 5-adic numbers with exactly the three specified coordinate valuations, so they are primitive. Direct computation gives

    a^3=5^(3 alpha)t0 u^11
       =5^(r+11 gamma)t0 u^11=t c^11,

    q c^11=5^(s+11 gamma)q0 u^11
          =5^(4 beta)=b^4.

Adding gives a^3+b^4=(t+q)c^11=c^11. The first identity gives j=1728 a^3/c^11 exactly. Thus the construction preserves the originally specified j, with one c shared by both identities; it is not a deformation of j or a pair of separate power witnesses. There is no further unit-residue compatibility obstruction: it has been absorbed by the chosen eleventh root u, while the fourth power is the explicit b^4.

### Translation to the displayed j-domain

Since 1728 is a 5-adic unit, v(t)=v(j) and v(q)=v(1728-j). In case 1, if both valuations are zero, j modulo 5 is neither 0 nor 1728 modulo 5=3, leaving exactly residues 1,2,4. If v(j)>0, then v(1728-j)=0 and v(j)=3m with m>=1. If v(1728-j)>0, then v(j)=0 and v(1728-j)=4n with n>=1. These exhaust integral j because j and 1728-j cannot both be divisible by 5. The corresponding sets are exactly the first five terms in the displayed union; the sign of j-1728 has no effect on its valuation or on its being a unit times 5^(4n).

In case 2, v(j)=-11k, giving precisely the last family of shells. They are nonintegral and cannot meet the other terms. Inside the integral terms, distinct positive valuations and distinct unit residues make all listed pieces disjoint. Neither 0 nor 1728 occurs in any listed piece. Conversely each piece has the prescribed pair of valuations, completing the translation and the equivalence.

The result meets the exact scalar-characterization threshold, not the zero-integer-solution threshold. In particular, scalar admissibility supplies no assertion that the whole modular fiber is isomorphic to L035's algebra A. Even removing some fiber scalars would not by itself show that their descent classes fail to occur at other admissible scalars. The image comparison and all global gaps therefore remain separate.

## Mathlib

Full matching primitive five-adic common-j characterization: **not checked**. Supporting Hensel, unit-root and valuation declarations: **not checked**. Unknown coverage is not evidence of absence. This is a signature-specific REPRODUCTION specialization of the cited standard local input under the saved SPECIALIZE assessment; no originality beyond the sources checked is claimed.
