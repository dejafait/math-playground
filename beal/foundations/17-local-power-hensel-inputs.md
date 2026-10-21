# Local power inputs for the scalar domain

## Hypotheses

For Hensel–Newton, K is a complete nonarchimedean discretely valued field, R its valuation ring, f in R[X], and alpha in R with |f(alpha)| < |f'(alpha)|^2. For the unit decomposition below, p is a rational prime and the field is Q_p.

## Conclusion

Hensel–Newton gives a unique root beta in R satisfying |beta-alpha| < |f'(alpha)|. In particular its derivative hypothesis must be verified at the proposed approximate root.

The unit group has the direct-product decomposition Z_p^* = mu_(p-1) × (1+p Z_p), with mu_(p-1) reducing bijectively onto F_p^*. This is a statement about units, not about arbitrary integral nonunits.

## Proof

Citation only. Pete L. Clark, *Algebraic Number Theory II: Valuations, Local Fields and Adeles*, [author-hosted notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf), Theorem 1.79, printed p.58 (PDF page 58), supplies Hensel–Newton. Inspected the exact hypothesis and both conclusions; the accessible 161-page version was retrieved 2026-10-08 and has no identified revision date. Theorem 2.36, printed p.79, was also inspected but its index formula is not needed for the proposed specialization.

Gergely Zábrádi, *Notes for the course p-adic methods in arithmetic*, ELTE summer school, **29 June 2022**, [author-hosted notes](https://zabradi.web.elte.hu/Jegyzetek/p-adic-meth-arith.pdf), Corollary 2.5, printed p.4 (PDF page 4), supplies the unit decomposition. Its proof lifts the distinct residue roots of X^(p-1)-1. Lemma 2.3 and Theorem 2.4 on the same page were inspected, including repeated one-variable lifting while fixing the other coordinates. Theorem 2.4 assumes f in Z_p[x_1,...,x_m], alpha in Z_p^m, f(alpha)=0 modulo p^n, and one partial derivative of valuation k with 0 <= 2k < n; it produces an exact root congruent to alpha modulo p^(n-k).

These are imported standard inputs, with no reproof. Applying them to normalized cube, fourth-power and eleventh-power equations at p=5, and eliminating their shared coordinate, remains a separate specialization. No scalar domain, simultaneous primitive witness or image comparison is established here. Changing one variable to solve a sum equation does not automatically preserve a prescribed j-value; the forthcoming argument must retain both defining identities. It must treat nonunit coordinates by exact valuations rather than applying a unit-root criterion to them.

## Mathlib

Full common-j characterization and these supporting Hensel/unit-decomposition declarations: **not checked**. Unknown coverage is not evidence of absence.
