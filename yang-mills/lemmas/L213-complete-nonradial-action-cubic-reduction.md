# L213 — Only the transverse fourth-chaos action class remains at cubic scale

## Hypotheses

Use exactly L025's complete nonradial quartic-action response

\[
 G_i^{\rm nr}(a)=-\kappa_0(f_{i,0},r_0,S_4-S_{4,\rm rad}),
 \qquad i=3,6,
 \tag{1}
\]

with L010's actual probes at tau=1/16, the pinned relative cube,
a=8/N and the straight lower-rooted direction-1 forest of L026.
The bare coefficient is taken at each fixed admitted even mesh before
refinement. Retain all three colors, all action plaquettes, normal end
edges, both residual insertion subtractions and the full heat sums.

Use L025's symmetric local tensor K and matrices C_p,U_(i,p),V_p,W_(i,p).
Let P_T be all action plaquettes in the planes 23,24,34. Define exactly
the no-internal-action-pair class on this set by

\[
 T_i^{(0)}(a)=-24\sum_{p\in P_T}
 K_{\alpha\beta\gamma\delta}
 (U_{i,p})_{\alpha\beta}(V_p)_{\gamma\delta}.
 \tag{2}
\]

The local indices in (2) include colors and signed traversal entries,
with fixed links set to zero. This is an actual subset of L025(6),
not a frozen or conditionally averaged polynomial.

## Conclusion

There is a mesh-independent C_i such that

\[
 \boxed{|G_i^{\rm nr}(a)-T_i^{(0)}(a)|\le C_i a^{-5/2}.}
 \tag{3}
\]

More precisely, the absolute plaquette sum of the non-upper axial
no-internal-pair class is O(a^-5/2), and that of its one-internal-pair
class is O(1). The entire upper axial response is O(a^-2) as a signed
sum, by the existing upper-face bounds. The absolute plaquette sum of
the transverse one-internal-pair class is O(a^-1). Fixed boundary
plaquettes and the lower axial layer contribute zero to (1).

Consequently

\[
 a^3 G_i^{\rm nr}(a)-a^3 T_i^{(0)}(a)=O(\sqrt a)\longrightarrow0.
 \tag{4}
\]

The complete response has a finite cubic-scaled limit if and only if
(2) does, with the same limit. No bound at cubic scale, convergence,
value, sign or vanishing is established here for (2). Thus (3) is a
partial reduction of the approved complete-response question. It does
not establish full perturbative compensation, any finer-scale estimate,
finite interacting matching, the reflected-error threshold c_box/2,
continuum axioms or finite positive physical mass.

## Proof

### 1. Exact exterior lifts and their signed form bounds

In this proof Delta is the physical relative one-form Hodge Laplacian,
including a^-2; write R_F for the full-link forest retraction. In
ordinary orthonormal mode coordinates set

\[
 \mathcal T=a^{-1}R_F\Delta^{-1/2},\quad
 \mathcal B_i=\Delta^{-1/2}Q_{i,a}\Delta^{-1/2},\quad
 \mathcal R=\Delta^{-1/2}N_a\Delta^{-1/2},\quad
 E=e^{-\tau\Delta}.
 \tag{5}
\]

The Q_(i,a),N_a are the physical operators of L028(2); N_a contains
both Q_3 and Q_6 subtractions. These symbols distinguish the whitened
operators from L025's forest-coordinate matrices. L018's lift and
annihilation of pinned gradients by the leading insertion and probe,
with L028(13)'s checked normalization, give the following exact
full-link matrices, before any local row selections:

\[
 \begin{split}
 C&=\mathcal T\mathcal T^T,&
 U_i&=\mathcal T E\mathcal B_i E\mathcal T^T,\\
 V&=\mathcal T\mathcal R\mathcal T^T,&
 W_i&=\mathcal T E\mathcal B_i E\mathcal R\mathcal T^T.
 \end{split}
 \tag{6}
\]

Each color has the same block, with no cross-color entries. These are
linear lifts of the exact forest contractions; the nonlinear action
still uses its original signed-edge tensor K. In particular (6) does
not transfer that action to an unmodified Hodge field. The factor
a^-1 in (5) is the dimensionless link normalization of L028(11).

L020(11) gives ||mathcal R||<=C/a, and L028 gives
||mathcal B_i||<=C_i. For any real full-link row selectors b,c, (6)
therefore implies the signed bound

\[
 |V_{bc}|\le (C/a)\sqrt{C_{bb}C_{cc}}.
 \tag{7}
\]

This follows from Cauchy--Schwarz on the two vectors
mathcal T^T b^T, mathcal T^T c^T and the operator norm of mathcal R.
It uses positivity only of C, not of V or W_i.

If d_p selects a signed plaquette circulation, then
d_p R_F=d_p. Its row in mathcal T is exactly the corresponding row
of d Delta^-1/2, because the circulation incidence is a d. Thus

\[
 C_{d_pd_p}\le1,\qquad
 V_{d_pd_p}=\beta_p,\qquad |\beta_p|\le C.
 \tag{8}
\]

The first assertion is the exact-form projection bound of L027(12).
The second identifies the diagonal with L023(3)'s normalization;
the last is L024(1), including all boundary plaquettes. The improved
diagonal bound (8), rather than ||mathcal R|| alone, is essential below.

### 2. Transverse end edges and smooth exterior columns

For every transverse link at an interior axial level 1<=j<N,
including normal links meeting a transverse face, the local covariance
obeys

\[
 C_{ee}\le j+8\le C/a.
 \tag{9}
\]

Here is the necessary extension of L026's upper bound. The direct
Hodge-link variance is at most 8 by its full relative spectral sum,
which applies to every variable link. The prefix part is the signed
sum of j component-1 transverse differences. If an endpoint lies on a
transverse face, its component-1 entries and pinned prefix are zero.
It is still exactly T_mu^T b, where b selects the j relative
(1,mu) plaquettes above that edge. L026(14)--(15)'s energy inequality
T_mu Sigma_1 T_mu^T<=I therefore bounds its variance by j, also at
these normal end edges. Direct and prefix parts have different Hodge
components and zero cross covariance. This proves (9); no interior
lower bound is being extended. Fixed links have zero rows. Positivity
then bounds every local transverse C entry by C/a.

We also require the end-edge extension of L028's exterior estimates.
Let e_k=a^2 f_(k,a) be an ordinary-coordinate normalized relative mode,
and put v_k=mathcal T e_k, z_k=mathcal T mathcal R e_k. The relative
eigenvalues obey lambda_k>=c|k|^2 with a uniform positive gap. L028(8)
gives smooth pre-retraction fields with C^1 norms at most p(k) and
a^2 p(k), respectively, for a fixed polynomial p. In particular they
are finite relative sine/cosine extensions and retain their tangential
zeros on each physical face.

For a smooth such field b the transverse retraction at interior axial
level j is the exact expression

\[
 (R_F b)_\mu(j,v)=b_\mu(j,v)
 -\sum_{\ell=0}^{j-1}
       [b_1(\ell,v+\widehat\mu)-b_1(\ell,v)].
 \tag{10}
\]

If either endpoint is on a transverse face, b_1 there vanishes:
component 1 is tangential to that face. Its path sum is consequently
zero and agrees with the prescribed pinned potential. Thus (10)
is still exact, rather than a continuation of a nonzero boundary
potential. Each bracket is O(a||b||_C1), with j a<=8. Subtracting
(10) at levels j+1 and j costs O(a||b||_C1), for j<=N-2.
These estimates only need C^1 regularity of b before retraction.
They never compare level N-1 to the pinned upper transverse link.

Including the exterior factor a in v_k and z_k as in L028(11),
(10) proves, uniformly on every interior-level transverse link,

\[
 |(v_k)_e|\le a p(k),\qquad |(z_k)_e|\le a^3 p(k).
 \tag{11}
\]

On an axial plaquette below the upper layer let m be the mean of
its positive transverse links, and d their upper-minus-lower difference.
The same calculation proves

\[
 \begin{array}{c|cc}
 &m&d\\\hline
 |v_k|&a p(k)&a^2p(k)\\
 |z_k|&a^3p(k)&a^4p(k).
 \end{array}
 \tag{12}
\]

L028(14)'s exact double heat sum for W_i and the corresponding sum
with v_k v_l^T for U_i retain every mode. Since
|(mathcal B_i)_(kl)|<=C_i and a polynomial times
exp[-tau(lambda_k+lambda_l)] is uniformly summable, (11)--(12) imply

\[
 \begin{split}
 |(U_i)_{mm}|&\le C_i a^2,& |(U_i)_{md}|&\le C_i a^3,
 & |(U_i)_{dd}|&\le C_i a^4,\\
 |(W_i)_{mm}|&\le C_i a^4,&
 |(W_i)_{md}|+|(W_i)_{dm}|&\le C_i a^5,
 & |(W_i)_{dd}|&\le C_i a^6.
 \end{split}
 \tag{13}
\]

Every W_i entry between transverse links at interior axial levels
is at most C_i a^4, including end edges and the last interior level.
Nothing in this argument damps an internal covariance pair or makes
a rough residual column smooth.

### 3. The missing non-upper axial fourth-chaos class is subcubic

Fix an axial plaquette with lower axial level 1<=j<=N-2. If it lies
in another boundary face, all its links are fixed. Otherwise both its
axial traversal entries are zero: an interior endpoint uses a forest
link, and a transverse boundary endpoint uses a fixed link. Thus its
ordered polynomial is the two-edge polynomial of L027, even when a
transverse endpoint is on the boundary:

\[
 q=-\frac1{24}|[m,d]|^2.
 \tag{14}
\]

The possible sign change of [m,d] from traversal orientation is
irrelevant in its square. For a three-color centered Gaussian with
one-color covariance c on (m,d), Isserlis' formula gives

\[
 E q=-\tfrac14(c_{mm}c_{dd}-c_{md}^2).
 \tag{15}
\]

For a symmetric quartic tensor K, E q=3 K:c:c. Differentiating
in two covariance directions u,v gives 6 K:u:v. Hence the
no-internal-pair term -24 K:U_i:V is -4 times the mixed derivative
of (15), namely exactly

\[
 G^{(0)}_{i,p}=(U_i)_{mm}V_{dd}
              +(U_i)_{dd}V_{mm}-2(U_i)_{md}V_{md}.
 \tag{16}
\]

This includes the three colors and the original negative cumulant
sign once. The differentiation is a polynomial identity in symmetric
matrices; it does not require positivity or invertibility of U_i,V
or the selected actual covariance. For example it can first be
performed at a positive definite auxiliary c and then extended
algebraically. It retains all 24 pairings in L025.

By (9), C_mm<=C/a; by (8), C_dd<=1 and |V_dd|<=C. Equations
(7)--(8) then give

\[
 |V_{mm}|\le C a^{-2},\qquad |V_{md}|\le C a^{-3/2}.
 \tag{17}
\]

Use (13), (17) and the stronger diagonal (8) in (16):

\[
 |G^{(0)}_{i,p}|
 \le C_i(a^2+a^4a^{-2}+a^3a^{-3/2})
 \le C'_i a^{3/2}.
 \tag{18}
\]

There are O(a^-4) such plaquettes, including all normal transverse
end edges. Their absolute sum is O(a^-5/2). The generic diagonal
bound |V_dd|<=C/a would give only cubic control here; L024 is what
improves it to a zero cubic coefficient.

For completeness the quadratic Wick coefficient of (14) is

\[
 -\frac1{12}\left(C_{dd}|m|^2+C_{mm}|d|^2
                         -2C_{md}\,m\cdot d\right).
 \tag{19}
\]

This is L027(5) in the (m,d) covariance notation; it also follows
by applying one half of the covariance-contracted Hessian to (14).
L025's 48-pair term, including colors, is consequently

\[
 G^{(1)}_{i,p}=2\left(C_{dd}(W_i)_{mm}
                   +C_{mm}(W_i)_{dd}
                   -C_{md}[(W_i)_{md}+(W_i)_{dm}]\right).
 \tag{20}
\]

Since |C_md|<=sqrt(C_mm C_dd)<=C a^-1/2, (13), (8) and (9)
bound its absolute plaquette sum by
C_i a^-4(a^4+a^5+a^(9/2))=O(1). This explicitly includes the
previously excluded normal transverse end edges; no estimate has
been extended through the upper axial pin.

### 4. Upper and lower axial layers, transverse loops and assembly

At axial level zero the lower transverse link is fixed and both
axial entries are forest or fixed. Only one link can remain in the
ordered product. A one-exponential plaquette has w_2=w_3=0, so its
nonradial q is zero. This is an identity on the forest slice and
removes both connected classes, rather than just their expectations.

At axial level N-1 retain the three-edge polynomial of L029. Its
complete one-internal-pair sum is O(a^-2) by L029(4)--(8). Its
complete no-internal-pair sum is O(a^-2) by L043(1). Both results
include normal transverse end edges and all transverse boundary
strips. These signed bounds suffice; neither a sign nor any numerical
enclosure from L047 is used. Thus no IEEE heat-arithmetic premise
is needed for this reduction beyond the imported analytic bounds.

On a purely transverse plaquette not contained in a fixed boundary
face, its axial level is 1,...,N-1. Every active row is a transverse
link row covered by (9),(11). The universal K entries are bounded
independently of a. With the fixed local dimension and (6),

\[
 |G^{(1)}_{i,p}|=|48 K:W_i:C|\le C_i a^4 a^{-1}=C_i a^3.
 \tag{21}
\]

Its absolute sum over O(a^-4) plaquettes is O(a^-1). Plaquettes in
any physical boundary face have all traversal links fixed and q=0;
this also accounts for the transverse plaquettes at axial levels 0,N.
The no-internal-pair transverse class has not been estimated: it is
precisely (2), with every remaining plaquette retained.

The partition exhausts the six plaquette orientations and every
axial level. Add the two connected classes once on each set in
L025(6). The errors just proved are O(a^-5/2), O(1), O(a^-2)
and O(a^-1), respectively. This proves (3), and multiplication by
a^3 proves (4) and the finite-limit equivalence. There is no
inference from this equivalence to existence or vanishing of either
limit, nor from a selected response to forest invariance.

### 5. Scope, checks and source reuse

The approved EXPLORE/COVERED_TARGET in
`drafts/literature/2026-10-16-complete-residual-coefficient-cubic-assembly.md`
is unchanged. That comparison found no adequate primary theorem for
this complete bare forest response. Known Wick pairing counts and
all cited analytic estimates are reused; the new work is the specific
signed diagonal specialization (16)--(18) and the exhaustive boundary
partition, needed because the earlier selected axial estimate omitted
the fourth-chaos class and normal transverse end edges. No general
flow-renormalization theorem is reproved or assigned stronger scope.

The mathematical checks are analytic: (15)--(16) check the color,
sign and 24-pair normalization independently through the covariance
polynomial; (19)--(20) retain the 48-pair normalization; (10)
checks pinned end-edge values before applying smooth estimates; and
the final partition counts both connected classes on every nonzero
plaquette. No finite numerical diagnostic is substituted for these
all-mesh estimates. No new mathematical program or numerical
certificate is needed. Upstream lemmas are imported, not recursively
audited. This is local progress within the checked-source scope,
with no certified originality or complete-solution claim.

## Mathlib

Full coverage of this forest-specific cubic reduction: **not checked**.
Supporting covariance-direction differentiation, Isserlis' formula,
spectral-order and heat-sum facts: **not checked**. Unknown coverage
does not mean absence. The specialization and boundary accounting are
proved explicitly above; no matching Mathlib theorem is asserted.
