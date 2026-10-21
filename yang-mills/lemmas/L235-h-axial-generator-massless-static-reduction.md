# L235 — A uniform massless axial reduction for the H generator

## Hypotheses

Use exactly L095 and L098's finite response R_H,ax and actual probes
i=3,6: SU(2), relative all-face pinned cube (-4,4)^4, straight
lower-rooted direction-1 forest, sufficiently large admitted even N,
a=8/N, tau=1/16, ordinary dimensionless stored coordinates, and the
bare small-coupling coefficient taken at fixed mesh before refinement.
Retain both generator orientations, all interior levels, transverse
normal end rows, covariance sources, allowed constant indices and
the complete exterior heat sum. This is the component as normalized
in L095(9), without another generator factor 1/2 or outside factor 3.

Write n=N-1, P for the transverse gradient projection, Q=I-P,
Delta_T for the relative transverse edge Hodge Laplacian, and
K_h=(L_D tensor I+I tensor Delta_T)^(-1)(I tensor Q).
Import L095's actual A_k(s)=P Omega_k(s) Q and endpoint-filtered U_s.
Set W_k(s)=A_k(s)U_s, extend only W_k by zero at s=0,N, and put
D_c W_k(s)=[W_k(s+1)-W_k(s-1)]/2. The c_(i;kl,a) are the unchanged
real symmetric coefficients of the actual probes.

Import L098(3), (4), (7) and its heat majorant. In particular, with
a fixed mesh-independent mode polynomial p, enlarged if necessary,

    ||A_l(s)|| <= C a p(l),
    ||W_k(s)|| <= C a p(k),
    ||D_c W_k(s)|| <= C a^2 p(k),
    sum_(k,l) |c_(i;kl,a)| p(k)p(l) <= C_i.             (1)

The product W_k and its centered difference are zero outside a
fixed physical axial interior, for sufficiently large N. This uses
compact displacement support, not an extension of the forest field
through its upper pin.

## Conclusion

Define the finite, unregularized, ordered transverse expression

    T_(i,ax,N) = -a^(-1) sum_(k,l)c_(i;kl,a) sum_(s=1)^n
      Tr_T[Delta_T^(-1) Q A_l(s)^T
                         (W_k(s)/2+s D_c W_k(s))].       (2)

There is a constant independent of sufficiently large admitted N such
that, for both actual probes,

    |R_H,ax-T_(i,ax,N)| <= C_i N^2 log(eN),
    |a^3(R_H,ax-T_(i,ax,N))| <= C_i log(eN)/N.           (3)

The endpoint-deficit part alone is O_i(N^2). The kink half-weight,
the derivative of the full product A_k U, both original orientations,
all sources and every heat label remain in (2). No mass parameter is
introduced. This sharpens only L098's axial reduction, previously
estimated at fixed positive mass.

It does NOT establish the approved complete estimate
|R_H,ax-a^(-3)K_(i,ax)| <= C_i N^(5/2)log(eN)^2. The remaining
claim is that same estimate for T_(i,ax,N)-a^(-3)K_(i,ax), with exactly
L098(2)'s coefficient. L098 and (3) give its qualitative scaled
convergence, but no quantitative transverse comparison is asserted.
The normalized differentiated exterior coefficient, ordered projection
and inverse placements, finite boundary comparison and full heat-sum
rate still need justification in that comparison. No E or H-curvature
rate is transferred. Other component rates, the complete interacting
reflected error <=c_box/2, continuum axioms, infrared control and finite
positive mass remain unresolved. The separate critical audit in proof
section 5 accepts this reduction relative to imported inputs; there is
no complete-solution candidate.

## Proof

### 1. Imported scalar kernel and its full first moment

Use J. S. Dowker, *Heat-kernels on the discrete circle and interval*,
arXiv:1207.2096v2 (31 August 2012), sections 2, 7 and 10,
equations (3), (5), (29)--(31), (42)--(48), printed pp. 1--2,
10--11 and 14--16: <https://arxiv.org/pdf/1207.2096v2>.
The interval in (29)--(31) has vertices 1,...,N-1 and zero values at
0,N; its diagonal-2, off-diagonal-minus-1 operator is L_D here.
Laplace transforming its heat kernel gives R_lambda=(L_D+lambda)^(-1).
The infinite integer-line resolvent, in the same normalization, is

    r_lambda(j)=exp(-kappa |j|)/(2 sinh(kappa)),
    lambda=2 cosh(kappa)-2,  kappa>0.                  (4)

This imports the known scalar kernel rather than reproving it. The
source's mass 4 sinh^2(gamma) corresponds to kappa=2 gamma. Only
the axial scalar operator after the transverse spectral decomposition
receives these Dirichlet data; no relative transverse vector component
or Brownian prefix is assigned scalar Dirichlet conditions.

The additional moment required by this trace follows by summing (4).
For q=exp(-kappa), lambda=(1-q)^2/q and
sum_(j>=1) j q^j=q/(1-q)^2. Hence exactly

    sum_(j in Z) r_lambda(j)=1/lambda,
    sum_(j in Z) |j| r_lambda(j)=1/(lambda sinh(kappa)),
    sinh(kappa)=sqrt(lambda(1+lambda/4)).               (5)

For 0<lambda<=12, (5) bounds the sum with weight 1+|j| by
C lambda^(-3/2). Finite Dirichlet kernel entries obey
0<=R_lambda(s,t)<=r_lambda(t-s). This follows either from the
killed heat kernel or from L095's minimum principle applied to the
restriction of (4), whose endpoint values are nonnegative.
Consequently

    sum_(s,t=1)^n (1+|s-t|) R_lambda(s,t)
                           <= C n lambda^(-3/2).      (6)

The necessary specialization is the weighted sum (5)--(6) followed
by the entire transverse spectral count; a scalar kernel identity
alone would not prove the response estimate.

### 2. Complete transverse spectral count and axial replacement error

Use L095 section 4's exact relative transverse spectrum. For component
nu its own index lies in 0,...,N-1, the other two in 1,...,N-1, and

    lambda_m=4 sum_(j=2)^4 sin^2(pi m_j/(2N)).

It lies in (0,12], is at least 4 r^2/N^2 on a shell
max_j m_j=r, and there are at most C r^2 labels on that shell,
counting all three components. Q commutes with Delta_T, so restricting
a positive spectral trace to its range can only reduce the count.
All allowed constant own-direction indices and normal end rows remain.
Thus

    Tr_Q Delta_T^(-3/2)
       <= C N^3 sum_(r=1)^(N-1) 1/r
       <= C N^3 log(eN).                              (7)

Each block (K_h)_ts=R_(Delta_T)(t,s)Q is positive semidefinite, by
L095's scalar minimum principle and this common spectral decomposition.
Its trace norm is therefore its positive spectral trace, even though
Q need not have nonnegative entries. Equations (6)--(7) give

    sum_(s,t=1)^n (1+|s-t|)||(K_h)_ts||_1
                                  <= C N^4 log(eN).   (8)

L098(3),(7) give, in the original order,

    R_H,ax=a^(-1)sum_(k,l)c_(i;kl,a)
                        sum_(s,t)Tr_T[(K_h)_ts (B_kl T_1)_st],
    (B_kl T_1)_st=-A_l(s)^T[h_st W_k(s)+s D_c W_k(s)]+E_(kl;st),
    ||E_(kl;st)||<=C a^3 p(k)p(l)(1+|s-t|),            (9)

where h_st is 1 for t<s, 1/2 for t=s, and 0 for t>s. These are
finite identities and bounds independent of the positive mass used
later in L098. Their applicability uses the second axial difference
of W_k, including both exterior and displacement differences. All
levels are included; no support restriction is imposed on E or K_h.

By the trace-ideal inequality, (1), and (8), the total error from E is

    a^(-1)sum_(k,l)|c_(i;kl,a)|sum_(s,t)
                    ||(K_h)_ts||_1 ||E_(kl;st)||
       <= C_i a^2 N^4 log(eN)
       <= C'_i N^2 log(eN).                           (10)

In particular no mesh-dependent mass is inserted into a qualitative
localization result. The singular low transverse modes have already
been summed in (7).

### 3. Both finite-end deficits, including the kink half-weight

For a fixed s, extend h_st to every integer t by the same definition.
Symmetry of the infinite-line kernel and the half at t=s imply

    sum_(t in Z) h_st r_lambda(t-s)=1/(2 lambda).      (11)

Let d_lambda(s)=lambda^(-1)-sum_(t=1)^n R_lambda(s,t).
The finite row-sum equation shows that this deficit solves the
homogeneous massive recurrence in the interior, with endpoint values
lambda^(-1). Uniqueness (or the interval image formula) gives

    d_lambda(s)=cosh(kappa(s-N/2))/(lambda cosh(kappa N/2))
       <= [exp(-kappa s)+exp(-kappa(N-s))]/lambda.     (12)

For clarity the recurrence uses the endpoint extension of the deficit,
not an extension of a forest field. Nonnegativity and R_lambda<=r_lambda
also give, without assuming symmetry of a finite row about s,

    0 <= 1/(2 lambda)-sum_(t=1)^n h_st R_lambda(t,s)
       <= d_lambda(s).                               (13)

Indeed the difference is a weighted sum of nonnegative kernel deficits
inside the interval plus the omitted infinite tails; 0<=h_st<=1
bounds it by their unweighted sum d_lambda(s). The unweighted row
deficit is exactly (12). Symmetry R_lambda(s,t)=R_lambda(t,s) is
matrix symmetry, not reflection about the row's center.

By (1)'s support condition there exists b>0, independent of k,l,N,
such that W_k(s) or D_c W_k(s) can be nonzero only for
bN<=s<=N-bN, for sufficiently large N. Since 0<lambda<=12,
kappa>=c sqrt(lambda) with a uniform c>0. Apply the same complete
shell count as in (7) to (12). For these supported levels,

    Tr_Q d_(Delta_T)(s)
       <= C sum_(r=1)^(N-1) r^2 (N^2/r^2) exp(-c' r)
       <= C N^2.                                     (14)

The trace includes the lowest allowed modes, for which the exponential
need not be small in N. They are controlled by their multiplicity and
inverse weight rather than discarded.

Set H_s=sum_t h_st (K_h)_ts and J_s=sum_t (K_h)_ts. Spectral
decomposition and (12)--(14) imply, on the same supported levels,

    ||(1/2)Delta_T^(-1)Q-H_s||_1 <= C N^2,
    ||Delta_T^(-1)Q-J_s||_1 <= C N^2.                 (15)

Both differences are positive spectral operators. In the main term
of (9), sum t before multiplying any transverse factor: its two terms
are exactly Tr[H_s A_l(s)^T W_k(s)] and
Tr[J_s A_l(s)^T s D_c W_k(s)]. No multiplier is commuted through a
projection or inverse. Also (1) and aN=8 give

    ||A_l(s)^T W_k(s)|| + ||A_l(s)^T s D_c W_k(s)||
                                    <= C a^2 p(k)p(l). (16)

Replacing H_s,J_s by their infinite-row sums in these exact placements
costs, by (1), (15), (16), at most

    C_i a^(-1) n a^2 N^2 <= C'_i N^2.                (17)

The resulting expression is exactly (2). Combining (10) and (17)
proves (3), with a^3=512/N^3 giving its normalized form.

### 4. Scope, heat sum and continuation

Every bound before the exterior sum has the same polynomial factor
p(k)p(l). L098's Gaussian heat majorant sums that polynomial uniformly
over all retained mesh labels. No continuum coefficient replaces a
finite coefficient in this proof, and no cutoff or omitted continuum
tail enters (2)--(3). Both i=3 and i=6 therefore follow from their
actual coefficients without altering their path stencils or signs.

The normalized remaining expression can be written exactly as

    a^3 T_(i,ax,N)=-a^4 sum_(k,l)c_(i;kl,a)sum_s
      Tr_T[Delta_T^(-1)Q alpha_(l,a)(s)^T
        (omega_(k,a)(s)/2+as dot_omega_(k,a)(s))],       (18)

where alpha=A/a, omega=W/a and dot_omega=D_c W/a^2. This notation
does not replace dot_omega by a continuum derivative. Proving a rate
between (18) and L098(2) still requires that separate derivative
comparison and an ordered transverse trace estimate. Equation (3)
is below the proposed N^(5/2)log(eN)^2 threshold, but the missing
estimate cannot follow from (3), coefficient-value convergence or
L098's successive fixed-parameter limits.

This is a RESEARCH / REPRODUCTION specialization under the unchanged
EXPLORE assessment
`drafts/literature/2026-10-18-h-axial-generator-quantitative-remainder.md`.
Its local advance is a uniform full-spectrum axial reduction using
imported scalar kernels and existing finite contractions, not a claim
of a new general resolvent theorem or a result beyond the sources
checked. No numerical evidence or mathematical script is needed.

### 5. Separate critical audit, 2026-10-19

**Verdict: accept (3), including the O(N^2) end-deficit estimate,
relative to L095 and L098.** The prior EXPLORE assessment is
`drafts/literature/2026-10-18-h-axial-complete-rate-critical-audit.md`.
This checks their finite contraction's massless specialization, without
recursively verifying the inputs or proving the static-to-continuum rate.

**Order and error.** L098(3) gives B_st=min(s,t)A_l(s)^T W_k(t) and
(B T_1)_st=(B_(s,t-1)-B_(s,t+1))/2. Thus (9)'s minus sign and
h_st=1,1/2,0 are correct. With m_t=min(s,t), the exact identity is
D_c(mW)_t=(D_c m)_t bar W_t+bar m_t D_c W_t. Here
D_c m=h_st, |bar m_t-m_t|<=1/2 and |m_t-s|<=|t-s|.
Replacing bar W_t by W_s costs Ca^2 p(k)(1+|t-s|).
Replacing D_c W_t by D_c W_s costs Ca^3 p(k)|t-s| by L098(4),
with multiplier at most N. Multiplication by ||A_l(s)||<=Ca p(l),
using Na=8, gives exactly Ca^3 p(k)p(l)(1+|t-s|).
The endpoint cases use the actual zero W_0,W_N. No forest exterior
is continued through the upper pin. L095(9)'s symmetric heat sum
already includes both orientations and consumes the insertion half.

**Entire moment and spectrum.** Both geometric tails give
sum r=1/lambda and sum |j|r=1/(lambda sinh kappa).
Since sinh kappa=sqrt(lambda(1+lambda/4)), the weighted row sum
is O(lambda^(-3/2)) for 0<lambda<=12. Killing decreases the scalar
kernel. On the complete transverse shell r, lambda>=4r^2/N^2
and multiplicity is O(r^2), including all components and permitted
zero own-direction indices. Thus Tr_Q Delta_T^(-3/2) is at most
CN^3 sum_(r<N)r^(-1); the n axial rows give CN^4 log(eN).
Each transverse covariance block is positive by its scalar spectral
values, without entrywise positivity of Q. Its trace norm is therefore
this spectral trace. The response error is a^(-1)a^3 times the full
sum, giving O(N^2 log(eN)). No lowest mode has been omitted.

**Both finite ends.** The deficit lambda^(-1)-sum_t R_lambda(s,t)
has homogeneous massive recurrence and endpoint values lambda^(-1).
Its unique solution is (12)'s cosh expression. Extend the finite
kernel by zero outside and subtract it from the full kernel. Every
entry of the difference is nonnegative. Weighting by 0<=h<=1 bounds
the weighted deficit by the same unweighted deficit, proving (13)
without finite-row reflection symmetry. On supported s, both kappa s
and kappa(N-s) are at least c r on shell r. The complete deficit
trace is at most CN^2 sum_(r>=1)exp(-c r)=O(N^2), retaining low
modes. The ordered response estimate is a^(-1) times N levels times
O(a^2) coefficient norm times O(N^2) deficit, hence O(N^2).
This applies to both H_s and J_s in their actual positions.

**Normalization and full heat sum.** A=a alpha, W=a omega and
D_c W=a^2 dot omega give exactly (18), including a^4(as) in the
derivative term. All errors have a fixed polynomial p(k)p(l), summed
by the unchanged full actual-probe heat majorant. Both probes, every
source and all constant indices remain. The accepted reduction still
requires L236's separate ordered-column and derivative comparison.
No numerical premise or script is needed. This validates a local
standard-method specialization, without a claim beyond checked sources.

## Mathlib

Full matching ordered-response estimate: **not checked**. Supporting
finite spectral decomposition, geometric first-moment sums, discrete
minimum principle, trace-ideal inequalities and harmonic shell bounds:
**not checked**. Unknown availability is not evidence of absence.
