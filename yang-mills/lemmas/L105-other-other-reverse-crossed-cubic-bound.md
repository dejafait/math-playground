# L105 — Cubic control of the co-closed-base reverse trace

## Hypotheses

Keep L093's SU(2) forest Gaussian and its actual reverse trace R_R:
both L010 probes i=3,6, the straight lower-rooted direction-1 forest,
relative all-face fixed-link box (-4,4)^4, sufficiently fine admitted
even N, a=8/N and tau=1/16. Take the bare small-coupling coefficient
at fixed mesh before refinement. All coordinates, transposes and norms
are ordinary stored ones. Retain every interior axial level, transverse
end row, ordered plaquette pair including coincidences, and exterior
heat mode. This R_R is different from L102--L104's gradient-base G_R.

On one transverse layer use L085's incidence T, circulation D,
Delta_0=T^T T, G=Delta_0^-1, Delta_T=TT^T+D^T D,
P=T G T^T and Q=I-P. Put n=N-1 and

    K_ts=[(L_D tensor I+I tensor Delta_T)^-1]_ts Q
         =R_ts(Delta_T) Q,
    A_k(s)=P Omega_k(s) Q, H_k(s)=Q Omega_k(s) Q.       (1)

Here the first expression uses tensor functional calculus. Omega_k(s) and the real symmetric
coefficients c_(i;kl,a) are exactly L088's full exterior expansion.
The letter H_k in (1) denotes the projected alternating matrix, not
L091's residual block H. Import L103's exact generator stencil

    G_T1=a^-1 W C_1,
    (W_t phi)_mu=-C_mu^T M_(u_(a,1)(t)) T_mu phi,
    T_mu=C_mu D_mu,                 mu=2,3,4.           (2)

D_mu is the forward vertex difference used in that stencil, whereas
T has the tail-minus-head incidence orientation. C_mu and C_1 are
the actual relative endpoint averages. Equation (2) retains both
transverse filters; W_t is not assumed to have gradient image.

## Conclusion

The actual co-closed-base reverse trace has the exact layer formula

    R_R=a^-1 sum_(k,l)c_(i;kl,a) sum_(s,t=1)^n S_st
      Tr_T[K_ts A_k(s)^T T G W_t^T H_l(t)],
    S_st=1_(t<s)+delta_st/2.                            (3)

Every coefficient stays at its displayed axial level and in its
original transverse order. In particular the diagonal half-weight
and both pinned axial ends are retained. Uniformly for both probes,

    |R_R|<=C_i N^3,
    |R_hx|<=C_i N^3,   R_hx=R_L+R_R-R_Q.              (4)

The second assertion uses L093's already proved bounds for R_L and
R_Q. It completes cubic boundedness of the co-closed-base crossed
pair, without proving a scaled limit or its value.

There is also a subleading simplification. Set, exactly as in L103,

    F_k=Bb^T M_(f_k) Bq-Bq^T M_(f_k) Bb,
    Zeta_k=M_(b_k) Bq-M_(q_k) Bb,
    Omega_k^0=Zeta_k^T D-D^T Zeta_k,
    Omega_k=F_k+Omega_k^0.                              (5)

Define R_R^0 by replacing both Omega occurrences in (3) by Omega^0,
with all projections, W_t, G, S_st and K_ts unchanged. Then

    |R_R-R_R^0|<=C_i N^2.                             (6)

Thus the actual exterior-circulation terms have zero a^3-scaled
contribution here. The retained trace R_R^0 still has no proved limit
or sign. No cancellation with -4 gamma D_i before the outside factor
3 is asserted. Transverse H still lacks cubic control; its limit,
evaluation of the existing E/H/G functionals, all finer scales and
the independent interacting continuum and mass requirements remain
unresolved. No Yang--Mills candidate follows.

## Proof

### 1. Expand the actual reverse order before estimating it

Import L093(3), without changing either generator orientation:

    R_R=sum_(k,l)c_(i;kl,a)
      Tr[K_h Omega_(gh,k)^T C G_T1^T Qcal Omega_(hh,l)]. (7)

L093 gives C=Tcal G_v B. L103(8) supplies the exact stencil (2),
and L093(5) gives B C_1^T=S with the entries in (3). Since the
transverse constant maps act separately on each axial layer,

    (C G_T1^T)_st=a^-1 S_st T G W_t^T.                (8)

No coefficient has passed through G: W_t remains on its right.
The formula for S was proved on all n interior rows and all N axial
edges, including the pinned endpoints. It uses the prefix exactly,
not a replacement by a local or infinite-interval profile.

Both alternating matrices in (7) are level diagonal, with respective
blocks A_k(s) and H_l(t). Consequently the (s,t) block of the product
following K_h is

    a^-1 S_st A_k(s)^T T G W_t^T Q H_l(t)
      =a^-1 S_st A_k(s)^T T G W_t^T H_l(t).           (9)

Only the adjacent Q H_l=H_l was removed. Taking the trace of K_h
times this block matrix sums Tr_T[K_ts times (9)] over all s,t.
L085 identifies these K_ts as precisely (1), proving (3). This is
a specialization of L093's finite contracted identity, not a reproof
of L048 or a change of its connected classes or outside factors.

### 2. Use the actual transverse energy bound inside each block

Import L103(13), whose proof uses only the exact filtered map (2),
the bounded displacement and sum_mu D_mu^T D_mu=Delta_0:

    ||W_t G^(1/2)||<=C,   ||T G^(1/2)||=1.             (10)

These bounds apply uniformly at every interior level on the same
pinned transverse vertex space used in (8). Therefore

    ||T G W_t^T||
      =||(T G^(1/2))(W_t G^(1/2))^T||<=C.             (11)

This does not bound the full prefix S, commute any multiplier or
claim that Q W_t=0. In particular (11) is compatible with L094's
quadratic lower bound on the full reverse-prefix operator.

L088(3),(5) gives, by bounded multiplicity of the complete path and
circulation selectors, a fixed mode polynomial p such that

    ||Omega_k(s)||<=C a p(k),
    sum_(k,l)|c_(i;kl,a)|p(k)p(l)<=C_i.                (12)

Indeed the two F terms have size O(a^2 p(k)) and the other four
terms have size O(a p(k)); all selector norms are uniformly bounded.
The projected factors in (1) obey the same bound. For the exact
operator between K_ts and the end of (3), (11)--(12) imply

    ||A_k(s)^T T G W_t^T H_l(t)||
                              <=C a^2 p(k)p(l).       (13)

This estimate uses all cross-component outputs in W_t and all six
terms of Omega. It invokes no scalar polarization of the residual.

### 3. Apply the existing positive-block trace sum

Import L095(13)--(14) on exactly L085's same relative covariance:

    K_ts is positive semidefinite for every s,t,
    sum_(s,t)||K_ts||_1
      <=n Tr_(ker P)(Delta_T^-1)<=C N^4.              (14)

The applicability is exact: L095 uses the same pinned Dirichlet
axial L_D, transverse Delta_T and commuting projection Q. Its
positivity is proved for each scalar axial inverse entry R_ts(lambda)
by the finite minimum principle, hence for each transverse spectral
block K_ts; it is not inferred from positivity of the full covariance
alone. Its row sum is at most 1/lambda, with both ends retained.
Its three-dimensional spectral shell bound includes every relative
edge component, including its zero own-direction index, and proves
Tr Delta_T^-1=O(N^3) without dropping low transverse modes. Thus
there is no missing boundary or singular-frequency qualification in
applying (14). This input is already established and is not reproved.

Since 0<=S_st<=1, trace duality and (13)--(14) give, for each k,l,

    a^-1 |sum_(s,t) S_st
      Tr_T[K_ts A_k(s)^T T G W_t^T H_l(t)]|
      <=C a p(k)p(l) sum_(s,t)||K_ts||_1
      <=C a N^4 p(k)p(l)<=C' N^3 p(k)p(l).           (15)

The trace and the exterior coefficients need not be positive. Only
the known covariance-block trace norm enters this absolute estimate.
The full exterior heat sum in (12) now proves the first inequality
in (4) for both actual probes, retaining every axial pair. L093's
|R_L|<=C_i N^3 and |R_Q|<=C_i N^(5/2) prove the second by its exact
split. No transpose cancellation or improved free operator bound is
used.

### 4. Remove only terms with actual exterior circulation

From (5), L088's coefficient bounds imply, uniformly in s,

    ||F_k(s)||<=C a^2 p(k),
    ||Omega_k^0(s)||<=C a p(k).                        (16)

Expand the difference of the two products in (3) and R_R^0. Each
of its three terms contains at least one F, and has unchanged middle
factor T G W_t^T. By (11),(16), their sum of operator norms is at
most C(a^3+a^4)p(k)p(l)<=C' a^3 p(k)p(l) for small a. Apply (14)
and the same nonnegative S weights. After the a^-1 factor and the
full heat sum the error is at most C_i a^2 N^4=O_i(N^2), proving
(6). This estimate removes neither the remaining signed path terms
nor any pinned row. It proves no N^2 limit or logarithmic statement.

### 5. Scope of the advance

This is a RESEARCH / REPRODUCTION attempt under the unchanged ready
assessment `drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
L093's finite trace, L103's generator stencil and energy bound, and
L095's positive-block trace sum are imported. The additional argument
is their applicability in the actual reverse order (8)--(15), which
was not supplied by the operator obstruction or the gradient-base
cumulative formula. This is local progress by established finite
matrix methods, with no originality claim beyond sources checked.

The proof is an analytic full-spectrum estimate; no numerical script,
finite-mesh extrapolation or IEEE arithmetic assumption is required.
L082's saved-table/IEEE qualifications still attach to any eventual
numerical comparison with D_i. Bounded a^3-scaled values alone do not
give convergence, a coefficient or compensation. In particular this
argument has not proved a uniform inverse-regularization error or
justified coefficient freezing. Those remain concrete obligations for
a limit argument based on (3) or (6).

## Mathlib

Full matching reverse-trace bound: **not checked**. Supporting finite
block trace, operator/trace norm duality and spectral matrix coverage:
**not checked**. Unknown availability is not evidence of absence.
All mathematical inputs are the stated local finite Gaussian,
stencil, covariance and spectral results; no external Ward, flow
finiteness or continuum construction theorem is imported.
