# Corollary 644a: the full vertical Pick norm has no uniform fixed reserve

## Hypotheses

Use precisely the actual-Xi grid and full Gram of L641 and the
simultaneous conclusion of audited L644. Thus, for sufficiently large
real T, with natural logarithms,

    N=floor(log T), T<=X<=2T, ell_X=log(X/(2pi)),
    s_j=2+i(X+j/N), C_jk=1/(3+i(j-k)/N), 0<=j,k<N,
    F=xi'/xi, K_jk=(F(s_j)+conjugate(F(s_k))) C_jk,
    B_(T,X)=C^(-1/2) K C^(-1/2)/ell_X,
    R_(T,X)=B_(T,X)-I_N.

Square roots are the positive Hermitian square roots. L641's checked
norm identity and distinct-pole independence make C strictly positive
definite; K and B are Hermitian. Norms of matrices are induced Euclidean
operator norms. L640 supplies only these definitions; its arithmetic
reduction and separate estimates are not premises.

Use L642's absolutely convergent complete mixed zero trace tau_X on
the actual interpolation subspace U_X, and its conditional
average-Rayleigh construction. Write r_X=dim U_X and use the positive
constants c_*, delta_* and fixed C_tail from L644. For every sufficiently
large T that result supplies a measurable S_T inside [T,2T] with

    |S_T| >= (delta_*/2)T, r_X>=c_*N for X in S_T,
    |tau_X|/(ell_X r_X) <= d_N,
    d_N=(2/c_*)[N^(-1/160)+C_tail N^(-1/2)] -> 0.

Every zero order, both ordinate directions and both horizontal
displacements are retained. Value constraints include repeated rows;
they impose no derivative or simplicity assumption. The local boundary
|Re(zeta)-(X+1/2)|=1 is annihilated; the distant boundary sqrt(N) belongs
to the complete tail. The imported analytic manuscripts retain L644's
source-audit qualifications. No RH, positive paired measure, invariant
U_X or effective onset is assumed.

The finite complex-Hermitian tools are imported, not reproved:
MIT 18.701, [*The Spectral Theorem for Hermitian Matrices*,
15 November 2010, p.1, theorem and real-eigenvalue corollary](https://ocw.mit.edu/courses/18-701-algebra-i-fall-2010/2622987fba1e172b289fc78934b8404d_MIT18_701F10_spthm.pdf);
Mark W. Meckes, [*Lecture notes on matrix analysis*,
27 April 2019](https://ncatlab.org/nlab/files/MeckesMatrixAnalysis.pdf),
Lemma 1.5/Definition 1.7 p.5 (basis-independent trace), Theorem 3.1
p.20 (Hermitian Rayleigh quotients), and Section 4.4 p.38 (induced
norm). The ready source comparison is
`drafts/literature/2026-11-01-l644-fixed-reserve-consequence.md`.

## Conclusion

For every sufficiently large T and every X in its selected S_T, there
is a Euclidean unit vector x in C^N with

    x* B_(T,X) x = tau_X/(ell_X r_X),
    ||R_(T,X)|| >= |1-tau_X/(ell_X r_X)| >= 1-d_N.            (1)

Consequently, for every fixed epsilon>0, there exists T_epsilon such
that for every real T>=T_epsilon and every X in S_T,

    ||C^(-1/2) K C^(-1/2)/ell_X-I_N|| > 1-epsilon.           (2)

In particular there do not exist epsilon>0 and T_0 for which this norm
is <=1-epsilon for every T>=T_0 and every X in [T,2T]. The violation
occurs on a set of measure at least (delta_*/2)T for every sufficiently
large T, not merely on one finite sample.

This is a standard finite-dimensional specialization (REPRODUCTION)
and a negative result for that sufficient norm budget. It proves no
negative eigenvalue, eigenvalue close to zero in absolute value,
finite-height norm >=1, failure of K positivity, or RH disproof.
The consequence is locally proved here; a separate critical audit of
this corollary has not been performed.

## Proof

Fix a sufficiently large T and X in S_T. Then ell_X>0 and r_X>0.
L642 identifies tau_X as the trace of the Hermitian zero-pair form
compressed to U_X, in its inherited boundary inner product. Its
absolute convergence and finite trace interchange retain the entire
zero sum. Apply the conditional average-Rayleigh construction already
given there: the normalized compressed form has a unit h in U_X with
quadratic value

    q_X=tau_X/(ell_X r_X).

For clarity, this is the scalar average of the real eigenvalues:
in an orthonormal eigenbasis take coefficients of squared modulus
1/r_X. This uses the cited finite Hermitian spectral and trace
theorems. It does not claim that q_X is itself an eigenvalue, or that
the ambient operator preserves U_X. L644 gives |q_X|<=d_N uniformly
on S_T, including either sign of q_X.

Transfer only this scalar value through L641. Its map v -> h_v from
C^N onto H_N is an antilinear bijection with

    ||h_v||^2=v* C v,
    v* K v=sum_zeta h_v(zeta-c_X)
                         conjugate(h_v(conjugate(zeta)-c_X)).

Choose v with h_v=h. Since h has unit norm, x=C^(1/2)v has Euclidean
norm one. Local terms vanish on U_X, so the displayed complete sum
is exactly the compressed form evaluated on h. Therefore

    x* B_(T,X) x=(v* K v)/ell_X=q_X.

No complex-linear unitary identification or matrix similarity is
asserted for the antilinear map. The full C, rather than its diagonal,
is essential to this norm and value calculation.

By Cauchy--Schwarz and the definition of the induced norm,

    |q_X-1|=|x*R_(T,X)x|<=||x|| ||R_(T,X)x||<=||R_(T,X)||.

The reverse triangle inequality gives |1-q_X|>=1-|q_X|>=1-d_N,
proving (1). This deduction uses neither positivity nor a spectral
sign; cancellation among eigenvalues is allowed.

For a fixed epsilon>0, d_N tends to zero because N=floor(log T)
tends to infinity and C_tail,c_* are fixed. Enlarge the existential
onset in L644 until d_N<epsilon for every later T. The bound is
independent of X in S_T, proving the strict inequality (2). If an
eventual all-height reserve with this epsilon existed, take T beyond
both onsets. The set S_T is nonempty, indeed has the stated positive
measure, and any of its X contradicts that reserve. Only selected
heights are used in this contradiction; no estimate is extended to
every height. All zero and endpoint conventions are unchanged from
the imported complete-trace identity. This proves the conclusion.

## Mathlib

Supporting finite-dimensional spectral coverage was inspected in the
ready assessment: [Mathlib.Analysis.InnerProductSpace.Spectrum](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/Spectrum.html),
`LinearMap.IsSymmetric.eigenvectorBasis`,
`LinearMap.IsSymmetric.apply_eigenvectorBasis`, and
`LinearMap.IsSymmetric.eigenvectorBasis_apply_self_apply`.
These support real/complex Hermitian diagonalization, including
repeated eigenvalues. Full matching coverage for the actual-Xi,
antilinear full-Gram specialization is not checked. No Lean verification
or absence claim is made.
