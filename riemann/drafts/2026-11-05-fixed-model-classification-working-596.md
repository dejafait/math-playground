# Fixed-model application — step596 working record

Approved target: the exact TARGET in
`literature/2026-11-05-fixed-model-classification-application.md`.
Reuse its IMPORT coverage; no new classification or degree sweep.

L791 fixes positive A,B,C in its radius10^(-15) rational box and
3.73557374335529<D<3.73557374335530. Its full box lies in
35.630<A<35.632, 11.539<B<11.541, 4.054<C<4.055,
3.735<D<3.736. Thus 24<A-B<25, 0<C-D<1,
31<A-D<32, and -8<C-B<-7. Neither permutation pairs numerator
parameters to denominator parameters by nonnegative integer differences.

Put c=D/(AC)>0 and alpha_j=c^j(A)_j(C)_j/[(B)_j(D)_j].
The correct exponential generating function is
Phi(z)=sum alpha_j z^j/j! = 2F2(A,C;B,D;c z),
not the ordinary coefficient series. Its binomial symbols are
q_d(x)=p_d(-x). Every coefficient of q_d is positive and its constant
and leading coefficients are nonzero. If every p_d were real-rooted,
each q_d would therefore have only negative real roots. Infinite
Pólya–Schur then places Phi in LP+; its reflected product alternative
is excluded by Phi(0)=1 and Phi'(0)=alpha_1>0. Positive scaling
identifies this with LP+ membership of unscaled 2F2. Sokal Theorem5
at p=q=2 forbids it by the two integer-pairing exclusions.

Consequently some finite degree has a nonreal model root; no first
failure degree is identified. This does not challenge L791's degree5
brackets, L792's actual degree5 transfer, or actual-Xi hyperbolicity.
Inherited analytic/data/software contracts remain assumptions.
Canonical statement/proof and documentation update follow.
