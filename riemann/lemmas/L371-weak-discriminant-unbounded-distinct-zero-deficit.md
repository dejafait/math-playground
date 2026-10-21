# Lemma 371: weak discriminant control permits an unbounded distinct-zero deficit

## Hypotheses

For real analytic functions F,G, use ordinary real derivatives and put

\[
 \mathscr L(u)=u'^2-uu'',\qquad
 B=2F'G'-FG''-F''G,\qquad
 D=B^2-4\mathscr L(F)\mathscr L(G).
\]

For a nonzero real analytic function u, let N_u([H,X]) count its
distinct real zeros in the closed interval [H,X], with each endpoint
counted once when it is a zero. The generic implication under test is
that D≤0 and \(\mathscr L(G)>0\) on an eventual ray imply
\(N_F([H,X])\ge N_G([H,X])-C\) for some finite C independent of X,
possibly after increasing H finitely. No common ODE, simplicity of F,
or actual-theta representation is assumed in this implication.

## Conclusion

The real entire pair

\[
 F(t)=1+\cos t,\qquad G(t)=\sin t                         \tag{1}
\]

satisfies D≤0 and \(\mathscr L(G)=1>0\) on the whole real axis, but
has an unbounded deficit of distinct F zeros relative to G on every
eventual ray. In fact, for every positive integer n,

\[
 N_F([\pi,2\pi n])=n,\qquad N_G([\pi,2\pi n])=2n.       \tag{2}
\]

Thus no finite C or finite increase of onset repairs the proposed
generic count implication. This is not a counterexample for the actual
F_0,G of L366–L370 and is not a disproof of RH.

## Proof

This is a **POTENTIALLY_NEW** local obstruction in the process sense:
the prior EXPLORE assessment found no covering theorem for the exact
weak analytic-pair statement. The elementary example and computation
are not claimed to be historically novel. The previously inspected
Sturm separation theorem (MIT 18.034 Spring 2009, Lecture 9,
[Theorem 9.1, printed pp. 1–2](https://ocw.mit.edu/courses/18-034-honors-differential-equations-spring-2009/0cdeb657491010f0f8c60aa49f2d5248_MIT18_034s09_lec09.pdf))
requires independent solutions of one regular second-order equation.
That premise is absent here. It is a comparison, not an imported
mathematical input. Direct verification is necessary because that
theorem does not decide the tested implication with common zeros.

Write c=cos t and s=sin t. The functions in (1) are entire, real on
the real axis, and not identically zero. Their jets are

\[
 F=1+c,\quad F'=-s,\quad F''=-c,\qquad
 G=s,\quad G'=c,\quad G''=-s.
\]

Using s²+c²=1 gives

\[
 \mathscr L(F)=s^2+(1+c)c=1+c,\qquad
 \mathscr L(G)=c^2+s^2=1,
\]
\[
 B=-2sc+(1+c)s+cs=s.
\]

Consequently

\[
 D=s^2-4(1+c)=-(1+c)(3+c)\le0,                         \tag{3}
\]

because 1+c≥0 and 3+c≥2 for real t. Equality holds exactly at odd
multiples of π. These are ordinary physical jets; no common envelope
is discarded. In L370's normalization the discriminant is
\(\Delta=D/(A^4T^4L^4)\), with A>0, T=1+|t| and
L=log(2+|t|)>0. Thus its sign is exactly the sign in (3), regardless
of the chosen positive envelope. No quantitative actual-family
envelope bound is needed or asserted for this abstract pair.

There is no concealed Wronskian nonvanishing. Directly,

\[
 W=FG'-F'G=(1+c)c+s^2=1+c,\qquad W'=-s,
\]
\[
 K=F'G''-F''G'=s^2+c^2=1.
\]

Thus W vanishes at each common zero, and W'²−4WK equals (3),
also at those points. In particular no quotient argument may pass
through these points by assuming W stays nonzero. As a further check,
for every real constant a the whole differential pencil obeys

\[
 \mathscr L(F+aG)=a^2+as+1+c
  =(a+s/2)^2+\frac{(1+c)(3+c)}4\ge0.                  \tag{4}
\]

The parameter a is constant during differentiation. Equation (4)
does not assert that all complex zeros of the pencil are real.

The real zeros of G are exactly kπ for integers k. They are simple
since G'(kπ)=(-1)^k. The identity F(t)=2cos²(t/2) shows that its
real zeros are exactly (2k+1)π. At such a point t_0, F(t_0)=F'(t_0)=0
and F''(t_0)=1, so the multiplicity is exactly two. Every F zero is
a common zero, whereas every even multiple of π is a G zero with
F=2. This verifies all degeneracies rather than excluding them.

The closed interval in (2) contains the G zeros kπ, 1≤k≤2n,
and the F zeros (2j+1)π, 0≤j≤n−1. The lower endpoint is a
common zero counted once by each count; the upper endpoint is only
a G zero. This proves (2) with the stated convention. For any fixed
H≥π and all sufficiently large n, partitioning [π,2πn] into
[π,H) and [H,2πn] gives exactly

\[
 N_G([H,2\pi n])-N_F([H,2\pi n])
 =n-N_G([\pi,H))+N_F([\pi,H)).                         \tag{5}
\]

The last two terms are finite constants independent of n. For fixed
H<π, partition [H,2πn] at π instead, adding the fixed finite
counts on [H,π). Thus in every case the deficit tends to infinity
along X=2πn. Given any finite C, (5) exceeds C for sufficiently
large n. This rules out the desired bound for every fixed onset.

The distinction between multiplicities and distinct zeros is essential:
in (2), counting the double F zeros with multiplicity would give 2n.
The approved statement requires distinct zeros and explicitly allows
multiple F zeros. Proving a version with extra simplicity or disjointness
hypotheses would not repair this counterexample to that statement. ∎

**Scope and verification.** All formulas above are exact identities;
the sign uses only −1≤cos t≤1. The count lists every real zero and
handles arbitrary endpoints by exact finite subtraction. No numerical
experiment, mathematical script or zero-density extrapolation is used.
This stops the generic distinct-count consequence, not the hypothesis
Δ≤0 for the actual family. Actual-family restrictions might give a
different implication, but their sufficiency is unproved here. L368's
actual positive response, L370's signed arithmetic residual, higher
Laguerre signs and the endpoint arithmetic margin remain independent.

**Critical audit, 2026-10-06.** The original hypotheses and conclusion
survive without correction. This audit is a REPRODUCTION of the saved
example, not a new obstruction or a claim of originality. Independently
substituting the six ordinary jets gives B=s and
D=s²−4(1+c)=−(1+c)(3+c). The factor 3+c is strictly positive;
the only equality points are c=−1. At each such point the six jets are
(F,F′,F″,G,G′,G″)=(0,0,1,0,−1,0). Hence the F zero has exactly
multiplicity two, the G zero is simple, and W=W′=0, K=1. There is
no missing strictness condition at the common zeros: the tested
discriminant inequality is weak and the response inequality remains
strict there. Completing the constant-parameter pencil square in (4)
gives precisely the same nonnegative residual −D/4.

For the physical scaling, substitution into the coefficient definitions
of L367 (1)–(3) gives
\(\mathcal B=B/(A^2T^2L^2)\),
\(\ell_F=\mathscr L(F)/(A^2L^2)\), and
\(\mathcal C=\mathscr L(G)/(A^2T^4L^2)\).
Both terms of their discriminant therefore have the identical divisor
A⁴T⁴L⁴, as in L370 (1)–(2). It is strictly positive on every
eventual ray where A>0; T≥1 and L≥log 2. This is a pointwise
scaling of physical jets, not the discriminant of F/A and G/A.
In particular the curvature correction for differentiated quotients
has not been omitted. The actual envelope may be used on t≥40,
but no actual-family identity or quantitative bound for this example
is inferred from that choice. These coefficient definitions are used
only to check conventions; the counterexample proof is self-contained.

As an independent check of the endpoint subtraction, fix any real H
and put h=H/π. For all sufficiently large positive integers n the
complete zero lists give the closed-endpoint formulas

\[
 N_G([H,2\pi n])=2n-\lceil h\rceil+1,\qquad
 N_F([H,2\pi n])=n-\left\lceil\frac{h-1}{2}\right\rceil.
\]

Indeed the G indices run from ceil(h) to 2n, and the F indices in
(2j+1)π run from ceil((h−1)/2) to n−1. These include a zero at H
exactly once, also when H is an odd or even multiple of π. Thus

\[
 N_G([H,2\pi n])-N_F([H,2\pi n])
 =n+1-\lceil h\rceil+\left\lceil\frac{h-1}{2}\right\rceil
 \longrightarrow+\infty.
\]

This agrees with (5) and also checks H<π directly. Counting F zeros
with multiplicity instead would double its count, so the audited
obstruction remains specifically about distinct zeros. The generic
route stop is retained. No actual-theta common-zero restriction,
comparison of actual zero counts, or total signed margin has been
established by the audit; the mathematical argument and DAG are unchanged.

## Mathlib

Full matching weak-discriminant obstruction: **not checked**. The proof
uses elementary sine/cosine differentiation and exact zero sets; no
Mathlib theorem is imported. Unknown availability is not evidence of
absence. The cited Sturm result has stronger hypotheses and is not a
matching theorem for the implication refuted here.
