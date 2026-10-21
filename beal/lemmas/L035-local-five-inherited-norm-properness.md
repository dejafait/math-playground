# L035 — The local-five comparison is already strict before imposing powers

## Hypotheses

Let K, E0, theta:E1 -> E0, T, f and the modular map j be exactly those of L033–L034. Put A=K tensor_Q Q5, the entire twelve-dimensional étale Q5-algebra. Thus A is the product of all K_v for v above 5, without selecting a factor. Write delta for the product of L033's local connecting maps and N for the determinant norm A^* -> Q5^*. It induces a homomorphism on fifth-power classes, since N(w^5)=N(w)^5.

For a finite scalar s in Q5 minus {0,1728}, let B_s be the coordinate algebra of the **whole scheme-theoretic modular fiber** j^-1(s). The complete-map facts in L034 imply that B_s is étale of dimension twelve. Every Q5-algebra isomorphism B_s -> A gives a point P in E0(A). All such isomorphisms are permitted. Define three sets in A^*/A^{*5}:

- I_all = delta(E0(A)), the unrestricted local image.
- I_fiber consists of delta(P) from every such s and every whole-fiber isomorphism B_s -> A.
- I_pow uses the same data, additionally requiring common a,b,c in Z5, all nonzero, with at least one of a,b,c a unit, a^3+b^4=c^11 and s=1728 a^3/c^11. Consequently (1728-s)c^11/1728=b^4. These are scalar witnesses shared across all factors of A; no positivity or conditions at 2 or 3 are imposed.

The last set is exactly the restricted set in the approved assessment drafts/literature/2026-10-08-five-isogeny-local-five-image.md. Nonzero a,b,c exclude s=0,1728,infinity. None of the sets is assumed nonempty except I_all; neither restricted set is assumed to be a subgroup.

## Conclusion

Every class alpha in I_fiber satisfies

    N(alpha)=[11^2] in Q5^*/Q5^{*5}.

This includes the exceptional fiber s=j(T)=-24729001, where f itself vanishes at T and the descent value must instead use a good divisor. The identity class belongs to I_all and belongs to neither I_fiber nor I_pow, because [11^2] is nontrivial over Q5. In particular

    I_pow subset I_fiber proper-subset I_all,
    I_pow proper-subset I_all.

Thus the literal approved proper-subset comparison has a certified excluded unrestricted class. The exclusion is entirely inherited from L034's fixed norm, independently of the primitive power conditions. **No assertion that I_pow is a proper subset of I_fiber is proved.** No nonempty restricted image, computed local group, new primitive-power filter, global intersection or integer exclusion is obtained.

## Proof

### Imported map, descent and norm inputs

L033 identifies theta's connecting map by the function f away from T and O and by good divisors at every point, over every completion. Its source is Schaefer–Stoll, *How to do a p-descent on an elliptic curve*, Trans. AMS 356 (2004), 1209–1231, [June 13, 2001 long author manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf), Section 5, pp.8–10, and Section 9, pp.21–24; the direction and normalization are proved in L033. We reuse this input without a descent reproof.

L034 proves, for the complete modular map,

    N_{Q(E0)/Q(j)}(f)=11^22(j+24729001)^5.

Its finite locally free determinant base-change argument specializes this equality to the entire fiber whenever s is finite and s is not j(T). The same base change applies over Q5 and then through any B_s -> A isomorphism; it is not limited to fibers arising from global positive solutions. Its map facts, from Freitas–Naskręcki–Stoll, *The generalized Fermat equation with exponents 2, 3, n*, Compositio Math. 156 (2020), 77–113, [final author manuscript, June 10, 2019](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf), Section 7.2, pp.25–27, give branch values only 0,1728,infinity and pole divisor (O)+11(3T). The finite-flat and determinant statements and their precise Stacks citations are recorded in L034. We reuse the norm, not recompute it.

If s is not j(T), no point of the finite fiber is T or O, so delta(P)=[f(P)] factorwise. The displayed determinant is nonzero and gives N(delta(P))=[11^22]=[11^2]. This covers the removable coordinate value s=j(2T)=-121 as well: L034 proves the map value at 2T and the determinant base change concerns the whole fiber, without imposing x-16 invertible.

It remains to justify the connecting-class norm at s=j(T), rather than assigning a class to the zero determinant of f there.

### Local constancy of the connecting class, with every exceptional point retained

Fix a finite extension F/Q5 and a point Q in E0(F). By L033, one can select R from {2T,3T,4T} so that both R and Q+R avoid T and O: at most two of the three choices are forbidden. The rational function

    h_R(Q')=f(Q'+R)/f(R)

is regular and nonzero on a neighborhood of Q and represents delta(Q') there. This statement includes Q=T and Q=O. In the F-adic topology it is continuous, and h_R(Q')/h_R(Q) tends to one as Q' tends to Q.

For completeness, the required openness of fifth powers follows from the strong form of **Hensel's lemma**: for a polynomial H over the valuation ring of a complete discretely valued field, v(H(t))>2v(H'(t)) implies a root near t. Normalize the extension valuation by v(5)=1. If u belongs to 1+125 O_F, then H(X)=X^5-u at t=1 has v(H(1))>=3>2v(H'(1))=2 (and u=1 is immediate). Hence u is a fifth power in F. This applies regardless of the ramification of F/Q5. It follows that [h_R(Q')] is constant on a sufficiently small neighborhood of Q. Thus delta is locally constant, and so is its product over all factors of A. No finite sampling cutoff or unrestricted-image size formula is used.

### Deforming a complete exceptional fiber

Suppose B_s -> A is one of the permitted isomorphisms at s=j(T), with point P=(P_v)_v. Since s is not 0,1728,infinity, the map j is unramified at every geometric point of its fiber. For each v, the local inverse form of Hensel's lemma therefore supplies, for all scalars s' sufficiently close to s, a point P_v(s') in E0(K_v) with j(P_v(s'))=s' and P_v(s') tending to P_v. To see the hypothesis explicitly, choose a local parameter at the smooth point P_v; the expansion of j-s has a nonzero linear coefficient because the map is unramified. Rescaling the parameter and shrinking the neighborhood gives the usual simple-root Hensel equation. This produces the local inverse over K_v. There are finitely many v, so one Q5-neighborhood of s works for every factor simultaneously.

These points still give a **whole-fiber isomorphism**, not just unrelated homomorphisms to some factors. Here is a dimension check that avoids that shortcut. Every finite fiber is a closed subscheme of the affine curve E0 minus O, because O is a pole of j. Thus its coordinate algebra is generated by its affine x,y. At s the assumed isomorphism shows that x(P),y(P) generate all of A as a Q5-algebra. Choose twelve monomials in these two elements whose coordinate columns, in the fixed basis 1,k,...,k^11 of A, have nonzero determinant. Such a choice exists precisely because they span A. The coordinates x(P_v(s')),y(P_v(s')) vary continuously; all points stay affine after shrinking the neighborhoods. Hence this determinant stays nonzero for sufficiently close s'. Evaluation at P(s') is a Q5-algebra map B_s' -> A whose image contains these twelve independent elements. Both algebras have dimension twelve, so the map is an isomorphism. Shrink once more to avoid branch values. This proves completeness across the product and includes every initially chosen isomorphism.

Choose such an s' distinct from s; the Q5-neighborhood contains infinitely many choices. By local constancy, shrink also until delta(P(s'))=delta(P). The nonexceptional case already proved gives

    N(delta(P))=N(delta(P(s')))=[11^2].

The auxiliary s' need not admit primitive power witnesses: the nonexceptional norm statement was proved for every complete fiber isomorphism. No power witness is altered or asserted to persist. At no point is f(T)=0 replaced by a nonzero ordinary evaluation; all connecting classes near the exceptional point are defined through good divisors. This proves the norm assertion for every I_fiber class.

### Exact excluded class and meaning of the comparison

The tuple of origins (O)_v lies in E0(A), and its connecting class is the identity. Its norm class is also the identity. On the other hand, 121 is not a fifth power in Q5. A hypothetical z with z^5=121 would have v5(z)=0. For a unit z with residue r in {1,2,3,4} modulo 5, the binomial expansion gives z^5=r^5 modulo 25. The four residues are respectively 1,7,18,24, whereas 121=21 modulo 25. This is an exact exhaustive unit-residue obstruction, not a precision assertion about the local image.

It follows that the identity cannot be in I_fiber, including its exceptional fibers and all algebra isomorphisms, and a fortiori cannot be in I_pow. The subset inclusions follow from their definitions. This proves strictness without asserting existence of any allowed power tuple.

The achieved threshold is one certified unrestricted class excluded by **all** allowed restricted tuples. The independent question whether simultaneous primitive powers remove anything from I_fiber remains unresolved. The exclusion above already holds after dropping all the power conditions. Its role is therefore to diagnose the baseline of the approved test, not to revive ATTEMPTS/009's failed nonconstant-norm mechanism. The global arithmetic blockers in ATTEMPTS/008, the other four twists, and infinitely many Beal signatures remain unaffected.

## Mathlib

The full product-algebra local comparison, exceptional-fiber continuation and connecting-class norm specialization: **not checked**. Supporting Hensel, finite étale fiber, determinant norm and continuity declarations: **not checked**. Unknown availability is not evidence of absence. This is a local reproduction/application of the already assessed descent and norm inputs, with the exceptional specialization justified above; no novelty beyond the checked literature is claimed.
