# L167 — Fourth ordered trace and complete response are cubic-bounded

## Hypotheses

Keep L161's full-link SU(2) relative cube (-4,4)^4, a=8/N through
sufficiently fine admitted even meshes, direction-1 straight lower-rooted
forest, complete compact displacement and both actual L010 probes at
tau=1/16. Take the bare expansion at fixed mesh before refinement.
Use ordinary stored-coordinate matrices D,L,Sigma,A,Phi,F=Phi Sigma,
R=I-D Phi and h=h_k t_c, ell=h_l t_c, where h_k=R v_k. Hats denote
three-color diagonal extensions. Keep both residual subtractions,
every action face and normal end link, the upper pinned jump, constant
axial mode and entire exterior heat spectrum. Form the complete cubic
tensors before forest restriction. Define precisely L161(3)'s fourth
ordered trace with its coefficient:

    X_i=-sum_(k,l,c) c_(i;kl)
                   Tr[Q_A(h) Fhat Q_L(ell) Fhat].         (1)

Let G_v=(D^T D)^(-1), on vertices pinned on all physical faces, and
split ell=ell_b+ell_top exactly as in L163. In particular ell_b has
zero component 1, while ell_top is supported on the upper normal
axial edges. This splits only the exterior column.

## Conclusion

For each actual probe, with mesh-independent constants,

    |X_i|<=C_i N^3,                                     (2)
    X_i=sum_(k,l,c) c_(i;kl)
          Tr[B_h Ghat_v Dhat^T B_(ell_b) Fhat Ahat]
                                      +O_i(N^2).        (3)

The upper exterior contribution in (3) is O_i(N log(eN)). The three
terms containing at least one smooth-column subtraction from Q_A or
Q_L are respectively O_i(N^2), O_i(N) and O_i(N^-2). These errors
vanish at cubic scale. The retained bulk trace is only cubic-bounded;
no limit, value or vanishing is established for it.

Together with the prior complete sector bounds, this proves

    |-kappa_0(f_(i,0),r_1,S_3)|<=C_i N^3,
                                                    i=3,6. (4)

Thus the complete response has bounded a^3-scaled values, but its
convergence and the requested zero limit remain open. In particular
L158/L159's two mixed branches and L165/L166's retained bulk traces
still lack scaled limits or coefficients. Other response jets,
complete compensation, finer powers/logarithm, finite matching,
interacting reflected error <=c_box/2, continuum axioms and infrared
finite positive mass remain unresolved. This is local standard-method
progress, without a claim of novelty beyond the sources checked.

## Proof

### 1. Use the actual forest column before estimating the second prefix

Fix exterior labels k,l,c; constants may contain fixed polynomials
p(k)p(l). L160's pinned telescoping identity and L165's Hodge identity
give, exactly on the finite domains,

    Phi D=I,       P=Sigma L=I-D G_v D^T,
    F L=Phi P=Phi-G_v D^T.                              (5)

Every axial link summed by Phi has level 0,...,s-1 for an interior
vertex at level s<=N-1. Thus these links have levels at most N-2.
L163 section 1 proves that the actual ell vanishes on all those
links. The potentially nonzero axial upper edge, at level N-1,
is not in any interior prefix. Since B_ell acts linkwise before the
prefix, the stronger matrix identity, not merely Phi ell=0, is

    Phihat B_ell=0,
    Fhat Lhat B_ell=-Ghat_v Dhat^T B_ell.                (6)

Both identities hold separately for ell_b and ell_top. Transverse
links are not inputs of Phi. Pinned vertex rows are zero throughout.
Equation (6) does not delete the upper jump: its contribution through
G_v D^T B_(ell_top) remains. No multiplier has been commuted with
Phi, Sigma, A or L.

Put p=Ahat h and q=Lhat ell, and for this paragraph suppress hats
on the diagonal matrices. Expanding the two Q factors in their
original order gives

    Tr[Q_A(h) F Q_L(ell) F]
      =-T(ell)-U-V+W,
    T(ell)=Tr[B_h G_v D^T B_ell F A],
    U=Tr[A B_h F B_q F],
    V=Tr[B_p F L B_ell F],
    W=Tr[B_p F B_q F].                                 (7)

For the leading term use cyclicity to write
Tr[A B_h F L B_ell F]=Tr[B_h (F L B_ell) F A], then apply
(6). This establishes its minus sign in (7); (1) reverses it again.
The remaining terms in (7) keep their full ordered products.

### 2. Two kernel estimates in the required row/column placements

Choose a fixed compact interior enlargement S containing both
index supports of A and all neighboring endpoints. It has O(N^4)
links. On S, |h_e|<=C a p(k), by the actual-column bound used in
L159 and L166. For e in S and every vertex w=(s,w_T), L166(5)
implies

    |(F A)_(w,e)|<=C a^-1 (1+|w_T-e_T|)^-3.             (8)

Here is the prefix summation explicitly. Symmetry of A and Sigma
gives (Sigma A)_(z,e)=(A Sigma)_(e,z). Thus F A sums, with no
change of order, L166's bound
C a^-1[(1+dist(e,z))^-4+N^-4] over the component-1 links z
below w. For m=|w_T-e_T|,

    sum_(n in Z)(1+sqrt(n^2+m^2))^-4<=C(1+m)^-3.

Comparison with the integral of ((1+m)^2+t^2)^-2 proves this
inequality, including m=0 after adding one bounded term. The constant
part of the Green bound sums to at most C N^-3. Since m<=C N,
it is absorbed in C(1+m)^-3. This proves (8), uniformly in s,
including s=N-1 and every low frequency and constant axial mode.
The estimate uses compactness of e, not compactness of the prefix.
If e is outside the support of A, the column is zero.

For a vertex v in S and any variable link f, the second estimate is

    |(G_v D^T)_(v,f)|
       <=C[(1+dist(v,f))^-3+N^-3].                     (9)

It includes normal end edges. To justify its precise boundary case,
write G_v as the integral of the scalar heat kernel with Dirichlet
conditions in all four vertex coordinates. The entry in (9) is the
difference of this kernel between the head and tail of f, with a
boundary vertex value set to zero. The one-difference infinite heat
bound in L164(6) integrates to C(1+dist(v,f))^-3. The exact odd
period-2N image formula in all four coordinates is the vertex
counterpart used in L165 section 2. As v is compactly interior,
all nonidentity image distances are at least c N(1+|b|), after a
fixed finite grouping. Through time N^2, sum the one-difference
heat estimate with decay exponent greater than 8 and integrate;
the contribution is O(N^-3). For times at least N^2 the normalized
fourfold sine expansion, with one source difference, is bounded by
C N^-5 exp(-ct/N^2); its time integral is again O(N^-3).
The infinite heat tail obeys the same bound. The image identity
holds at boundary vertices, where the odd reflections cancel, so
the head-minus-tail formula still retains the normal end edge.
This proves (9) for every source link without removing a boundary
collar or treating a pinned value as a smooth nonzero extension.

We also use L166(12)'s global prefix-row bound, for v in S or
elsewhere and every link f:

    |F_(v,f)|<=C(1+|v_T-f_T|)^-1.                      (10)

It is zero for nonaxial f. Bounds (8)--(10) concern cross matrices,
not positive covariances. Both residual insertion subtractions and
both generator orders are retained in the imported A Sigma bound.

### 3. Sum the bulk kernel product and retain the upper exterior

The exact entry expansion of T is

    T(ell)=sum_(e,v,f,w) (B_h)_(e,v)
                  (Ghat_v Dhat^T)_(v,f)
                  (B_ell)_(f,w) (Fhat Ahat)_(w,e).      (11)

Only e in S contributes. The endpoint incidences restrict v to an
endpoint of e and w to an endpoint of f. These choices and all color
multiplicities are bounded independently of N. Put m=|e_T-f_T|
and r=1+dist(e,f), absorbing fixed midpoint shifts into constants.
For each e the product of the spatial bounds in (8),(9) is summable:

    sum_f [r^-3+N^-3] * (1+m)^-3<=C.                   (12)

Indeed a transverse shell at distance m has at most C(1+m)^2 sites,
and summing r^-3 over all integer axial offsets gives C(1+m)^-2.
The decaying part of (12) is bounded by C sum_(m>=0)(1+m)^-3.
The constant part is at most
C N^-3 N sum_(m<=CN)(1+m)^-1<=C N^-2 log(eN).
These counts include all source components and end edges; restricting
to actual variable links only decreases the upper bound.

L163/L164 give |ell_b|<=C a p(l) globally on variable links.
Consequently (8),(11),(12) yield

    |T(ell_b)|<=C p(k)p(l) N^4 a a a^-1
                <=C p(k)p(l) N^3.                     (13)

No cancellation, limiting passage or coefficient freezing is used in
this inequality. All bulk action faces are counted.

For ell_top, the f links are in the last axial layer and satisfy
|ell_top|<=C p(l). Since v is compactly interior, (9) is at most
C N^-3 there. On this layer
sum_f(1+|e_T-f_T|)^-3<=C log(eN), retaining every transverse
position. The same expansion therefore gives

    |T(ell_top)|<=C p(k)p(l) N^4 a a^-1 N^-3 log(eN)
                    <=C p(k)p(l) N log(eN).             (14)

This is an estimate of the actual discontinuous exterior column,
not an O(a) assignment or smooth extension of it.

### 4. The three smooth-column subtraction terms

L156's exact gauge annihilation and smooth-column consistency give

    ||p||_infinity<=C a^5 p(k),
    ||q||_infinity<=C a^3 p(l).                         (15)

The p column is compactly supported because A is; q includes all
normal end rows. These are estimates on A h=A v_k and L ell=L v_l,
not on A B_h or L B_ell. The endpoint map always satisfies
||B_z||<=C||z||_infinity by its bounded row and column degrees.

For U, keep its order and write its trace as

    U=sum_(e,v,f,w) (B_h)_(e,v) Fhat_(v,f)
                              (B_q)_(f,w) (Fhat Ahat)_(w,e).

Again e is in S and v,w are endpoints of e,f. Combining (8),(10),+(15), the compact h bound and the complete axial count gives

    sum_f (1+|e_T-f_T|)^-4
          <=C N sum_(m>=0)(1+m)^-2<=C N,
    |U|<=C p(k)p(l) N^4 a a^3 a^-1 N
                         <=C p(k)p(l) N^2.             (16)

For V and W it suffices to use finite Hilbert--Schmidt inequalities.
L161 proves ||Fhat||_HS<=C N^3. Also (5) gives

    ||F L||_HS=||Phi P||_HS
       <=||Phi|| ||P||_HS<=C N^3.                     (17)

The same bound holds for the color extensions, with their fixed
multiplicity. Indeed ||Phi||<=N by its prefix
row/column sums, while an orthogonal projector on O(N^4) link/color
coordinates has HS norm at most C N^2. The global actual bound is
||B_ell||<=C p(l), retaining its jump. Therefore

    |V|<=||B_p|| ||Fhat Lhat||_HS ||B_ell|| ||Fhat||_HS
          <=C p(k)p(l) a^5 N^6<=C p(k)p(l) N,
    |W|<=||B_p|| ||B_q|| ||Fhat||_HS^2
          <=C p(k)p(l) a^8 N^6<=C p(k)p(l) N^-2.       (18)

These are trace Cauchy--Schwarz inequalities for compatible rectangular
matrices. Neither symmetry nor positivity of B_p,B_q or F is assumed.
All original signs in (7) remain available even though these error
bounds use absolute values.

### 5. Full heat sum and complete-response assembly

L156(8) provides mesh-uniform summability of
sum_(k,l)|c_(i;kl)|p(k)p(l) for both actual probes. Restore hats,
sum the three exterior colors, and keep the coefficient -1 in (1)
once. Equations (7),(13),(14),(16),(18) prove (2)--(3). Since
N log(eN)<=C N^2, all the displayed errors fit the remainder in (3).
The retained trace is O(N^3); that fact gives neither convergence
nor vanishing of its a^3-scaled sequence.

To check (4), use L159(3)'s exact assembly
H_i=T_i+V_i+H_i^EE+O_i(N). Both mixed branches are O_i(N^3)
by L158 and L159. In L161(3)'s E,E identity, the first trace is
O_i(N^2 log(eN)) by L164, the second and third are O_i(N^3)
by L166 and L165, the fourth is (2), and the fifth and sixth are
O_i(N) and O_i(N^(5/2)) by L161 and L162. Every contribution is
at most O_i(N^3), so their finite sum is too. This restores all
sectors and outside coefficients without treating signed E as noise,
discarding any action face or adding any other response jet.

The meaningful verification is analytic: the entrywise forest zero
in (6), the ordered expansion and signs in (7), the complete prefix
sum (8), the normal-end Dirichlet difference in (9), both shell
counts (12),(16), and the separate top count (14). No numerical
extrapolation or mathematical script is needed for these estimates.

## Mathlib

Full matching result and supporting lattice-kernel coverage:
**not checked**. Unknown is not absence. Reuse the unchanged
[target assessment](../drafts/literature/2026-10-12-cubic-residual-action-cubic-scale.md).
No new external theorem is imported or reproved. The all-Dirichlet
one-source-difference case is justified explicitly because its normal
end edges and compact observation row are essential to this order.
L156 supplies exterior/heat estimates, L157/L160 the Hodge and prefix
identities, L161 the exact traces and HS bound, L163/L164 the exact
forest exterior split and heat estimates, and L165/L166 the required
kernel placements. L158/L159/L162 and L164--L166 supply the other
complete sector bounds when assembling (4).
