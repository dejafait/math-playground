# L272 — Massless axial reduction of the exterior-circulation remainder

## Hypotheses

Use exactly L123(2)--(5): SU(2), both actual probes i=3,6, the relative
all-face pinned cube (-4,4)^4, the straight lower-rooted direction-1
forest, sufficiently large admitted even N, a=8/N, tau=1/16 and ordinary
stored coordinates. Take the bare small-coupling coefficient at fixed
mesh before refinement. Retain both mixed orientations, every axial
level and transverse source/end row, the original pinned covariance
and projections, all allowed constant mode indices and the complete
finite-mesh exterior heat coefficients c_(i;kl,a).

Write n=N-1. On the transverse relative edge space let Delta_T be the
Hodge Laplacian, P the gradient projection and Q=I-P. Import L123's
exact normalized operators

    beta_k(s)=A_k^f(s)/a^2,
    alpha_k(s)=A_k^D(s)/a,
    g(s)=a G_tr(s),
    H_(kl;st)=[beta_l(s)^T alpha_k(t)
                           +alpha_l(s)^T beta_k(t)]g(t).       (1)

These symbols denote finite matrices, with their actual coefficient
samples, path filters and component selectors; they are not the frozen
torus symbols of L123(1). L123(6),(11) give a fixed polynomial p with

    ||beta_k(s)||+||alpha_k(s)|| <= C p(k),
    ||beta_k(s+1)-beta_k(s)||
      +||alpha_k(s+1)-alpha_k(s)|| <= C a p(k),
    ||g(s)|| <= C,   ||g(s+1)-g(s)|| <= C a,
    sum_(k,l)|c_(i;kl,a)|p(k)p(l) <= C_i.                       (2)

Neighbor differences concern existing interior levels only. By L123
section 3, g(s) is zero outside a fixed physical axial interior:
there is b>0 independent of N,k,l such that g(s) can be nonzero only
if bN<=s<=N-bN. This does not extend a forest potential through its
pinned upper level.

## Conclusion

Define the finite, massless, ordered static trace

    T_(i,f,N)=a^2 sum_(k,l)c_(i;kl,a) sum_(s=1)^n s
      Tr_T[Delta_T^(-1) Q
        {beta_l(s)^T alpha_k(s)+alpha_l(s)^T beta_k(s)}g(s)]. (3)

Then, for both actual probes with constants independent of N,

    |E_(i,N)^f-T_(i,f,N)| <= C_i N^2 log(eN),
    |a^3(E_(i,N)^f-T_(i,f,N))| <= C_i log(eN)/N.              (4)

The complete f,f term and the axial endpoint-deficit contribution are
each O_i(N^2). All finite transverse projections, inverses, raw
coefficients and heat labels remain in (3), in their original order.
In particular this is not a finite-to-infinite transverse comparison.

L123 and (4) imply a^3 T_(i,f,N) -> K_(i,f), with exactly L123(2)'s
coefficient. They do not prove the required rate

    |T_(i,f,N)-a^(-3)K_(i,f)| <= C_i N^(5/2)log(eN)^2.         (5)

Since the error in (4) is below that budget, the approved complete
E^f remainder bound is equivalent to (5), up to changing its constant.
This is a partial quantitative reduction, not completion of that bound.
The remaining ordered transverse boundary/projection/freezing and
raw-coefficient/full-heat comparisons, independent upstream audits,
quantitative L011 assembly and all interacting/continuum/infrared
construction requirements remain unresolved. The separate critical audit
in proof section 4 accepts this specialization relative to imported inputs.

## Proof

### 1. Reuse the matching scalar and full-spectrum estimates

L235(8) applies to precisely the covariance appearing in L123(5):

    (K_h)_ts=[(L_D+Delta_T)^(-1)]_ts Q,
    sum_(s,t=1)^n (1+|s-t|)||(K_h)_ts||_1
                                      <= C N^4 log(eN).       (6)

Its proof uses the entire relative transverse edge spectrum, including
the constant own-direction indices and normal end edges. The restriction
to Q commutes with Delta_T. Each axial block is positive semidefinite
in that common spectral decomposition; no entrywise positivity of Q
is assumed. This is the same space, normalization and axial interval
as here, independent of the alternating matrices multiplying it.
Consequently this covariance estimate is reusable even though L235's
response, generator and final static expression are different.

The scalar input underlying L235 is J. S. Dowker, *Heat-kernels on the
discrete circle and interval*, arXiv:1207.2096v2, 31 August 2012,
sections 2, 7 and 10, equations (3), (5), (29)--(31), (42)--(48),
printed pp. 1--2, 10--11, 14--16,
<https://arxiv.org/pdf/1207.2096v2>. The axial scalar operator is the
diagonal-2/off-diagonal-minus-1 Dirichlet L_D on 1,...,N-1; the source's
mass parameter satisfies kappa=2 gamma. L235(5)--(8) already performs
the first-moment and full transverse spectral specialization. Neither
the scalar kernel nor that specialization is reproved here, and scalar
Dirichlet conditions are not assigned to transverse vector components.

Set J_s=sum_(t=1)^n (K_h)_ts. The second inequality of L235(15), with
its proof (12)--(14), gives

    ||Delta_T^(-1)Q-J_s||_1 <= C_b N^2,
                                bN<=s<=N-bN.                 (7)

In particular both physical axial ends and the lowest transverse modes
are included in (7). Its support hypothesis is only a restriction on
the level s of the multiplying insertion. It imposes no restriction
on the covariance source t or any transverse source. L123's g(s)
satisfies exactly that level restriction. The O(N^2) deficit is kept;
there is no assertion that the massless deficit is exponentially small
in N.

### 2. Keep both mixed terms while making their axial levels equal

Import the exact expansion L123(5), including its existing orientation
normalization, and its complete O_i(N^2) f,f bound. Call that f,f term
F_(i,N). Substitution of (1) in the two remaining terms gives exactly

    E_(i,N)^f=F_(i,N)+a^2 sum_(k,l,s,t)c_(i;kl,a) min(s,t)
                                     Tr_T[(K_h)_ts H_(kl;st)],
    |F_(i,N)| <= C_i N^2.                                   (8)

No generator orientation is deleted: both ordered products in (1)
remain, and the later other/other factor 3 is not inserted.

Telescoping (2) along existing axial levels gives

    ||H_(kl;st)|| <= C p(k)p(l),
    ||H_(kl;st)-H_(kl;ss)|| <= C a p(k)p(l)|t-s|.             (9)

For the second inequality, beta_l(s),alpha_l(s) stay fixed; the
differences act on alpha_k(t),beta_k(t) and g(t). Thus (9) uses only
their actual neighbor estimates. It holds also when one level is in
an axial coefficient collar and the other is not. It requires no
extension to levels 0 or N.

Using |min(s,t)-s|<=|t-s| and as<=8,

    ||a^2 min(s,t)H_(kl;st)-a^2 s H_(kl;ss)||
       <= C a^2 p(k)p(l)|t-s|.                              (10)

Apply |Tr(XY)|<=||X||_1||Y||, then (6), and finally the complete heat
majorant (2). The difference between the mixed part of (8) and

    U_(i,N)=a^2 sum_(k,l,s)c_(i;kl,a)s
                                  Tr_T[J_s H_(kl;ss)]        (11)

is at most

    C_i a^2 N^4 log(eN) <= C'_i N^2 log(eN).                 (12)

All s,t were summed before this estimate. In particular no source
localization, projection commutation or symmetry of a finite kernel
row around its center was needed. J_s occurs on its original left
side of the complete ordered product.

### 3. Bound both endpoint deficits and retain the finite static trace

H_(kl;ss) vanishes unless g(s) is nonzero, so (7) applies wherever
the summand of (11) survives. It gives, with (9),

    |U_(i,N)-T_(i,f,N)|
      <= C_i a^2 N^2 sum_(s=1)^n s
      <= C'_i a^2 N^4 <= C''_i N^2.                         (13)

Only the level support of the insertion is used. Every transverse row
is still present in the trace norms, and no raw exterior field is
declared compact or made smooth through the upper pin. The trace
in (3) therefore has the actual finite Delta_T, P, Q and selectors.
Equations (8), (12), (13) prove (4).

For normalization, (3) gives exactly

    a^3 T_(i,f,N)=a^4 sum_(k,l,s)c_(i;kl,a)(as)
                              Tr_T[Delta_T^(-1)Q H_(kl;ss)]. (14)

This is L123(13)'s finite static expression with zero covariance mass,
now obtained by uniform finite inequalities rather than by substituting
zero into a fixed-mass limit. The identity is a^3 a^2 s=a^4(as).
There is no additional half, color factor, factor 8 or outside 3.
L123's independently established limit and (4) identify the qualitative
coefficient. They give no quantitative modulus for the remaining
transverse comparison (5).

The heat sums in this proof are the original finite-mesh sums throughout.
Every bound is modewise with the same fixed polynomial p(k)p(l), which
(2) sums for each actual probe. No continuum heat coefficients have
been substituted and no omitted continuum labels need to be estimated
to prove (4). Those matching obligations remain part of (5).

This is RESEARCH / REPRODUCTION under the unchanged EXPLORE assessment
`drafts/literature/2026-10-24-exterior-circulation-quantitative-remainder.md`.
The contribution is a new local applicability argument for already
proved scalar, spectral and coefficient estimates, not a claimed new
general theorem beyond the checked sources. ATTEMPTS/030's varying-mass
shortcut and ATTEMPTS/032's separate absolute-moment shortcut are unused.

### 4. Separate critical audit, 2026-10-24

**Verdict: accept (3)--(4), including the complete O(N^2) f,f and
two-end deficit allowances, relative to L123 and L235.** The unchanged
invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-24-exterior-circulation-axial-reduction-critical-audit.md`.
This is a RESEARCH / REPRODUCTION audit of the ordered application, not
a recursive certification of L123, L235 or their upstream premises.

**Exact response and both orders.** In L123(5), substituting
A^f=a^2 beta, A^D=a alpha and G_tr=a^(-1)g gives a^2 times
beta_l(s)^T alpha_k(t)g(t) and a^2 times
alpha_l(s)^T beta_k(t)g(t). They are precisely the two summands of
(1); neither is transposed into the other or deleted. The adjacent
gradient projection was already absorbed in L123(5). Its orientation
normalization is imported, so there is no further factor 1/2 or 3.
For the third product, L123(6) gives norm at most
C N a^3 p(k)p(l), including min(s,t) and the generator. Its complete
covariance sum is O(N^4), giving O(a^3 N^5)=O(N^2) for f,f.
That term is removed exactly once in (8).

**All-level replacement.** Write
B_st=beta_l(s)^T alpha_k(t)+alpha_l(s)^T beta_k(t), so H_st=B_st g(t).
Then H_st-H_ss=(B_st-B_ss)g(t)+B_ss(g(t)-g(s)). Every factor has
L123(11)'s bound on the same finite transverse space, and telescoping
from s to t stays entirely in 1,...,N-1. Thus (9) follows without
commuting a coefficient or projection. In particular it covers a pair
with s in a zero-generator collar and t outside that collar. The exact
identity

    min(s,t)H_st-sH_ss
       =(min(s,t)-s)H_st+s(H_st-H_ss)

and as<=8 prove (10), with coefficient Ca^2 p(k)p(l)|t-s|.
The complete sum in L235(8) therefore gives
Ca^2 N^4 log(eN)=O(N^2 log(eN)); it already includes both axial
indices and every transverse spectral multiplicity. No additional
row factor is due. Block positivity is spectral positivity of
R_st(Delta_T)Q, not entrywise positivity of Q. L095's relative spectrum
and L235's audited moment use exactly this K_h and its normal end rows,
including the allowed zero own-direction indices. No scalar Dirichlet
condition is imposed on transverse vector components.

**Both ends in the correct placement.** After this replacement, summing
t gives J_s on the left of H_ss, exactly as in (11). The rightmost
g(s) makes H_ss zero outside a fixed physical axial interior, even
though beta and alpha need not vanish there. L235(15)'s second,
unweighted inequality applies at every surviving s. Its scalar deficit
is bounded by lambda^(-1)[exp(-kappa s)+exp(-kappa(N-s))]; both
physical ends and the lowest modes are present in its O(N^2) trace.
There is no kink-weighted H_s in this application and no additional
half-weight. The response cost is

    C_i a^2 N^2 sum_(s=1)^(N-1) s
       = C_i a^2 N^2 N(N-1)/2 = O(N^2).

This uses only generator-level support. Every covariance source t and
transverse input/output row remains in the imported norms. In particular
no assertion of exponentially small massless deficits, finite-row
reflection symmetry or smooth upper extension is needed.

**Heat count, normalization and scope.** All three allowances have
the same fixed polynomial p(k)p(l), enlarged once if needed, so the
original finite-mesh heat majorant bounds them for each actual probe.
No continuum labels replace these sums. Their sum proves (4), and
a^3=512/N^3 gives its normalized error. Directly,
a^3 a^2 s=a^4(as), proving (14) with the physical lower distance and
without another color, orientation or box-length factor. Combining
only this vanishing scaled error with L123(3) identifies the same
qualitative coefficient. It gives no rate for the remaining transverse
comparison. ATTEMPTS/030 and ATTEMPTS/032 are not invoked: no varying
mass limit or separate absolute spatial kernel moment enters the proof.
No unsupported identity or budget was found within this audit's scope.
The result clears a local premise of the conditional L273--L275 chain;
it supplies no new source-level theorem, complete quantitative L011
assembly or interacting/continuum/infrared construction.

## Mathlib

Full matching pinned exterior-circulation remainder or this axial
specialization: **not checked**. Supporting finite spectral calculus,
Schatten trace inequalities, telescoping sums and relative-cochain
coverage: **not checked**. Unknown availability is not absence. No
formal verification or general Ward/flow-finiteness result supplies
the remaining transverse estimate or an interacting construction.
