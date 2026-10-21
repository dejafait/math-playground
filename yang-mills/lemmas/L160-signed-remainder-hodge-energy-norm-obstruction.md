# L160 — The signed remainder is not uniformly bounded in Hodge energy

## Hypotheses

Keep L156–L157's full-link, ordinary stored-coordinate conventions for
the SU(2) relative cube, a=8/N through admitted even meshes and the
straight direction-1 lower-rooted forest. This is a one-color matrix
statement; its three-color diagonal extension has the same norm.
Retain every normal end link, pinned boundary vertex, the upper axial
jump and the constant axial edge mode. The actual L010 probes and
complete residual/action tensors remain as in L156; none is replaced
by the packet used below.

Write D=D_0, L=D_1^T D_1, Delta=L+D D^T, Sigma=Delta^(-1),
R=I-D Phi, K=Phi Sigma Phi^T and

    E=R Sigma R^T-D K D^T
     =Sigma-D Phi Sigma-Sigma Phi^T D^T.

Here Phi sums axial edges below an interior vertex and is zero on all
boundary vertices. Let Delta_v=D^T D, P=Sigma L, Q=I-P and

    Z=Sigma^(-1/2) D Phi Sigma^(1/2),
    X=Q Z P : range(P) -> range(Q),
    W=Sigma^(-1/2) E Sigma^(-1/2).                       (1)

All square roots are positive finite-matrix square roots. E is signed,
not an independent Gaussian covariance. P here is the four-dimensional
co-closed projector, not L085's transverse gradient projector.

## Conclusion

On the orthogonal decomposition range(Q) plus range(P), exactly

    W=[-I  -X; -X^T  I],
    W^2=[I+X X^T  0; 0  I+X^T X],
    ||W||=sqrt(1+||X||^2).                              (2)

There are mesh-independent positive constants c,C with

    c N^(3/2) <= ||W|| <= C N^(3/2).                    (3)

More precisely, let phi be any normalized transverse scalar Dirichlet
eigenvector of eigenvalue lambda, and take the full-link unit vector
u with component 1 equal to phi/sqrt(N) on every axial edge and every
other component zero. Then P u=u and

    ||X u||^2=N/lambda+2(N-1)
                       +lambda (N-1)(2N-1)/6.           (4)

For lambda=12 sin^2(pi/(2N)), (2)–(4) give

    ||W||^2 >= 1+N^3/(3 pi^2).                          (5)

This is an obstruction to bounding L156's E,E sector by treating each
signed remainder as uniformly bounded relative to Sigma. It is not a
lower bound for that contraction or either actual probe. No cubic
bound, scaled limit, vanishing or nonvanishing of H_i^EE or the complete
-kappa(f_(i,0),r_1,S_3) follows. L158–L159's cubic-bounded mixed branches
are retained; their tensor-specific cancellations are unaffected.
The complete response, other jets, finer powers/logarithm, matching,
interacting reflected comparison and continuum/infrared requirements
remain unresolved. This specializes elementary spectral and incidence
identities, without an originality claim beyond the assessed sources.

## Proof

### 1. The actual signed Hodge blocks

The prefix telescopes on a pinned vertex field: Phi D=I. This includes
the upper normal edge because its endpoint potential is separately
zero; Phi does not sum that edge into an interior vertex. Delta_v is
positive: a vertex field with zero gradient is constant on the connected
cube and its pinned boundary value is zero. Since L D=0,

    Delta D=D Delta_v,    Sigma D=D Delta_v^(-1),
    Q=Sigma D D^T=D Delta_v^(-1) D^T.                    (6)

Thus Q is the orthogonal gradient projector. L157's P=Sigma L is its
orthogonal complement; both commute with Sigma and its square roots.
The range of Z lies in range(Q), so Q Z=Z. Since D Phi is the identity
on gradients, Z Q=Q. Consequently on range(Q) plus range(P),

    Z=[I  X; 0  0].

The exact expansion of E in the hypotheses gives W=I-Z-Z^T, proving
its first block identity. Squaring gives the second. The finite real
spectral theorem implies ||W||^2=||W^2||; the largest eigenvalues of
X X^T and X^T X coincide and equal ||X||^2. This proves (2).
It also shows Q E Q=-Sigma Q and P E P=Sigma P. Negativity on the
gradient subspace alone does not remove the off-diagonal blocks.

For later normalization put J=D Delta_v^(-1/2). It is an isometry
from pinned vertex coordinates to range(Q). From (6),

    Sigma^(-1/2) D=J Delta_v,
    ||Z v||=||Delta_v Phi Sigma^(1/2) v||.               (7)

These are full-link identities; no forest-row tensor is deleted.

### 2. An exact co-closed packet with its upper endpoint retained

L026(6)–(7) gives a constant axial edge mode and the scalar transverse
Dirichlet spectrum. The stated u has norm one. At each interior vertex
its two axial edge values agree, so D^T u=0; hence P u=u. The axial
edge Laplacian kills its constant axial factor, and Delta u=lambda u.
Thus Sigma^(1/2)u=lambda^(-1/2)u. For s=1,...,n=N-1,

    (Phi Sigma^(1/2)u)(s,y)=s phi(y)/sqrt(N lambda).      (8)

On this transverse mode Delta_v is L_D+lambda I, where L_D is the
axial Dirichlet vertex matrix with diagonal 2 and off-diagonal -1.
For m=(1,2,...,n)^T the lower boundary value is m_0=0, while the
actual upper pinned value is m_N=0. Directly,

    L_D m=N e_n.                                        (9)

In particular one must not extend the linear prefix to value N at the
upper face. Since u belongs to range(P), X u=Z u. Apply (7)–(9):

    ||X u||^2=||N e_n+lambda m||^2/(N lambda)
             =N/lambda+2n+(lambda/N) sum_(s=1)^n s^2.

The exact sum n(n+1)(2n+1)/6 proves (4). For the lowest transverse
mode lambda=12 sin^2(pi/(2N))<=3 pi^2/N^2. Equations (2) and (4)
give (5), establishing the lower bound in (3). If (9)'s upper
endpoint term were omitted, the remaining squared expression would
be only lambda n(2n+1)/6, bounded at this lowest frequency. That
omission changes the order and the boundary condition.

### 3. A full-spectrum upper bound

Phi uses only component-1 link inputs. On a transverse scalar mode
of eigenvalue lambda, its axial part is the n-by-N prefix matrix H,
H_(s,r)=1 for 0<=r<s and zero otherwise, with s=1,...,n. The
component-1 Hodge covariance is (L_E+lambda I)^(-1), with
L_E=B^T B and (B v)_s=v_s-v_(s-1). Directly on every entry,

    L_D H=-B+e_n 1^T,     ||H||<=N.                    (10)

The norm bound is the row/column sum bound. The vector 1 on all N
axial edges is a zero mode of L_E, and
||B(L_E+lambda I)^(-1/2)||<=1 by L_E=B^T B. Therefore the norm
of this transverse block of Delta_v Phi Sigma^(1/2) is at most

    1+sqrt(N/lambda)+N sqrt(lambda).                    (11)

Here the second term is exactly the norm of
e_n 1^T (L_E+lambda I)^(-1/2); the last bounds
lambda H (L_E+lambda I)^(-1/2). The transverse mode blocks are
orthogonal both in input and output. Their eigenvalues obey

    12/N^2 <= lambda <= 12,

using the sine inequality sin(t)>=2t/pi on [0,pi/2] and the three
positive transverse vertex indices. Thus (11) is uniformly at most
1+N^(3/2)/sqrt(12)+sqrt(12)N<=C N^(3/2). Component inputs other
than 1 contribute zero to Phi. Equations (7), ||X||<=||Z|| and
(2) prove the upper bound in (3), with every axial and transverse
mode and all boundary rows retained.

### 4. Relevance to the approved response and exact checks

L156's E,E term retains two E lines in the -36 full combined-color
tensor contraction, one exterior U_i line and both cubic Taylor
tensors. Equations (2)–(5) concern a possible matrix estimate of those
two lines, not the value of that tensor contraction. The packet is
not the residual, an exterior heat column, or either actual probe.
In particular the residual's compact support and the action's gauge
identities can remove the very endpoint effect producing this global
norm. They must be applied in the actual contraction order before an
improved estimate is claimed. There is no signed-cumulant lower bound
and no assertion of a power divergence from this test.

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_signed_remainder_energy.py`.
Its full certificate is
`scripts/combined-ward-response/signed-remainder-energy-certificate.json`.
It checks the unwhitened block identities on a pinned graph by exact
rational arithmetic, and verifies (9)–(10) and (4)'s complete squared
packet expression for specified finite N and positive rational lambda.
The rational lambda cases check the identity, not the actual sine
eigenvalues. The lower and upper bounds for the actual cube are the
analytic arguments in sections 2–3; finite checks alone establish no
cutoff asymptotic or actual-probe response.

## Mathlib

Full matching result: **not checked**. Supporting finite spectral
theorem, orthogonal projector identities and incidence spectra:
**not checked**. Unknown availability is not absence. The unchanged
[assessment](../drafts/literature/2026-10-12-cubic-residual-action-cubic-scale.md)
is reused; no new external theorem is imported or reproved. The
elementary linear algebra is specialized explicitly because the
relative normalization, signed off-diagonal blocks and separately
pinned upper prefix determine the proposed E,E estimate's validity.
