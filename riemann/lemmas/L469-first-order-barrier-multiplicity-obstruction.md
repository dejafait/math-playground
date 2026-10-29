# Lemma 469: local multiplicity obstruction to a regular first-order barrier

## Hypotheses

Let F be a nonzero real analytic function near a real point a_0, with a zero of finite multiplicity m>=1 there. Write x=a-a_0 and F(a)=x^m g(a), where g is real analytic and g(a_0)!=0. Let w be positive and C^1, and C be real and continuous, on an open interval containing a_0. Define

D(a)=D_1(F;a)=F'(a)^2-F(a)F''(a),    U(a)=w(a)D(a).

In particular F may be the actual Xi function of L018. No assertion that Xi has a multiple zero is a hypothesis or conclusion of this lemma.

## Conclusion

For every such w and C, if m>=2, there is delta>0 such that

U'(a)+C(a)U(a)<0 for a_0-delta<a<a_0,

U'(a)+C(a)U(a)>0 for a_0<a<a_0+delta,

and the defect is zero at a_0. Thus U'+CU>=0 cannot hold on a two-sided neighborhood of a_0 for this multiplicity. The same pair w,C is not being required to work across different zeros: failure already holds for every local choice at any one multiple zero.

If m=1, then for every prescribed positive C^1 weight w there exists a continuous C (indeed a constant on a sufficiently small neighborhood) for which U'+CU>0 throughout that neighborhood. This is local compatibility only, not an independently derived Xi coefficient or a global inequality. At a simple zero, for a prescribed C the exact central defect is

w'(a_0)g(a_0)^2+2w(a_0)g(a_0)g'(a_0)+C(a_0)w(a_0)g(a_0)^2.

A negative central value precludes the inequality; a positive value ensures it on a smaller neighborhood. A zero central value alone gives no verdict.

## Proof

Local analytic factorization at a finite-order zero gives the stated g. L018 supplies real entirety and nontriviality for actual Xi, so any of its real zeros has precisely such a factorization. No zero-location or simplicity theorem is used.

Direct product differentiation gives the exact identity

D(a)=x^(2m-2) H(a),

H(a)=m g(a)^2+x^2(g'(a)^2-g(a)g''(a)).

The two mixed terms 2m x^(2m-1)gg' cancel. This identity also holds at x=0, by continuity (or as a power-series identity), including m=1. Put q=2m-2 and A=wH. The function H is analytic, so A is C^1 with A'=w'H+wH'; no second derivative of w is needed. Also A(a_0)=m w(a_0)g(a_0)^2>0. Shrink the interval so that A>0. For x!=0 and q>=1, ordinary differentiation, without differentiating a big-O remainder, gives

U'+CU=x^(q-1) [q A+x(A'+CA)].

When m>=2, q is a positive even integer. Continuity of A,A',C makes the bracket tend to q A(a_0)>0 as a tends to a_0. Choose delta so that the bracket is strictly positive throughout the punctured neighborhood. The exponent q-1 is odd, proving the two strict signs. Since q>=2, both U and U' vanish at a_0; the central defect is therefore zero. In particular the achieved left defect is strictly negative, whereas the proposed barrier requires it to be nonnegative. Bounded continuous C cannot offset the lower-order derivative term. No derivative of w beyond its first derivative has been assumed.

For m=1, q=0 and U=A>0 on the smaller interval. Choose a closed interval J around a_0 within it. A'/A is continuous on J, so let M=max_J |A'/A| and take C=M+1. Then U'+CU=A(A'/A+C)>=A>0 on J. The displayed central formula follows from H(a_0)=g(a_0)^2 and H'(a_0)=2g(a_0)g'(a_0); the x^2 term contributes no derivative there. Continuity proves the stated consequences of strict central signs. To see why zero central defect alone gives no general verdict, take F(a)=a-a_0 and w=1: C=0 gives an identically zero defect, whereas C(a)=a-a_0 gives a defect negative to the left. Both have zero central defect. These are local examples, not claims about actual Xi. Choosing C via A'/A establishes existence locally only; it does not furnish an actual-Xi estimate independent of D.

For completeness, at every point the unnormalized defect also has the exact zero-safe expression

U'+CU=w(F'F''-FF''')+(w'+Cw)(F'^2-FF'').

This follows from D'=F'F''-FF'''; it is not a sign estimate for actual Xi.

The obstruction has the standard integrating-factor interpretation. On any compact subinterval define I(a)=exp(integral from a_0 to a of C(s) ds)>0. If U'+CU>=0 held, then (IU)'=I(U'+CU)>=0, so IU would be nondecreasing. For m>=2, U(a_0)=0 while U>0 immediately to its left, contradicting that monotonicity. This is an independent check of impossibility, not a replacement for the strict defect calculation above.

The comparison tool is the usual scalar differential-inequality theorem: Grace D'Agostino and Hermann J. Eberl, *Uncertainty Analysis of a Simple River Quality Model Using Differential Inequalities*, SIAM Review 67(2) (2025), 375–398, Section 2.3, Theorem 1 and proof, pp. 381–382, [primary PDF](https://epubs.siam.org/doi/epdf/10.1137/23M1616406). Its finite-interval hypotheses include differentiability, a locally Lipschitz right side, initial ordering and defect ordering. For f(a,u)=-C(a)u, continuity of C provides a bounded Lipschitz coefficient on each compact interval. No source theorem is invoked to supply Xi's defect or initial data. The factorization/product calculation is written out because the exact multiplicity and the minimal w regularity are the approved specialization, not a stated conclusion of that comparison theorem. The elementary integrating-factor check does not reprove the full comparison theorem.

Qualification: this known-tool specialization rejects multiplicity-uniform use of this particular two-sided first-order class. It proves neither an actual multiple Xi zero nor a missing Xi sign, simplicity, an off-line zero, or RH. A one-sided interval, singular C, a weight vanishing at a_0, and other operators are outside its hypotheses; no conclusion about them is asserted. Global source control and usable all-height boundary data remain missing even in the simple-zero case.

Separate critical audit, 2026-10-26: the product identity, exact derivative, both punctured-side signs for every integer m>=2, central values, m=1 existence and prescribed-coefficient cases, and integrating-factor quantifiers were replayed. The statement survives unchanged. Continuity supplies only local boundedness of C, which is all the proof uses. L018 is the sole direct notebook input; L466, L468 and the external half-plane premise are not used. This verifies the local specialization, not the cited comparison manuscript as a whole or any global Xi defect estimate.

## Mathlib

Full matching theorem and supporting local-factorization/comparison declarations not checked. No absence claim is made. [Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
