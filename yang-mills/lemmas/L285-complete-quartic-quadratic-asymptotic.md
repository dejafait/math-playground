# L285 — Distinct-line limit and the complete quartic asymptotic

## Hypotheses

Use L280's SU(2) relative box D=[-4,4]^4, even N>=2 and a=8/N.
Pin every boundary-contained link, fix gauge transformations at boundary
vertices, and retain every other link, including both normal endpoint
cases. Keep all three colors and L002's exact product bump as specified
in L282: h_+=f_*, h_-=theta f_*, supported in
[-1/4,1/4]^3 times [1,2] and [-2,-1], respectively. Source derivatives
are at zero in (|s|+|t|)||f_*||_infinity<eta<1.

Use the ambient all-link Wilson quartic tensors of L279(8)–(9) on
L280's own slice, with S_4=U[x^4]/24, U=sum_p U^p, and the source
derivatives G_pm=G K_pm G of L280(18). No nonlinear forest jet is
transported. The contraction is mathcal U(U;X,Y)=U_ijkl X_ij Y_kl.
Retain Z_0, I_1, a_*=8Z_0-3/2+4I_1 from L283, S_f>0 from L282,
and J_f from L284(2). All limits below are along even N.

L283 and L284 are mathematical inputs with their separately recorded
critical audits. Section 6 below audits the present complete assembly.

## Conclusion

Define the finite constant

\[
 b_*=-\frac23Z_0+\frac{20}{3}I_1-\frac16.                 \tag{1}
\]

The remaining distinct-line action response has the complete limit

\[
 \lim N^{-2}\left[-\frac14\mathcal U(U;G_-,G_+)\right]
             =-\frac{3b_*}{128}\mathcal J_f.               \tag{2}
\]

Consequently ALL FOUR terms in L280(20)'s quartic family satisfy

\[
 \boxed{\displaystyle
 \lim N^{-2}\mathcal K_4^H
  =\frac{10Z_0-1-16I_1}{128}\mathcal J_f
       -\frac{3a_*}{128}\mathcal S_f.}                     \tag{3}
\]

Adding L282's COMPLETE density response gives

\[
 \boxed{\displaystyle
 \lim N^{-2}\{\mathcal K_4^H+\operatorname{Tr}(DG_{-+})\}
  =\frac{10Z_0-1-16I_1}{128}\mathcal J_f
   +\frac3{32}\left(\frac14-2Z_0-2I_1\right)\mathcal S_f.} \tag{4}
\]

Each limit includes an o(N^2) error for the entire finite-box quantity,
with no discarded boundary layer or internal anchor. No sign of (3)
or (4), or cancellation with the cubic family, is asserted. The complete
coefficient kappa_a, a uniform higher remainder, physical trajectory
and composite mixing, continuum axioms/positivity, a nonzero physical
sector and finite positive mass remain unresolved. This is a local
asymptotic result, not a Yang–Mills candidate solution or a claim of
originality beyond the checked sources.

## Proof

### 1. Uniform local approximation of a differentiated covariance

Suppress color; all covariances in this section tensor with I_3.
Let C_12 be the 12 rows of the relative incidence and
L=C^*C+BB^*. L280(23) and CB=0 give GC_12^*=L^-1 C_12^*.
For h=h_- or h_+, therefore,

\[
 G_h=L^{-1}C_{12}^*\operatorname{diag}(h)C_{12}L^{-1}.
                                                               \tag{5}
\]

Use the polynomial p_m=h_m and e_m(lambda)=lambda^-1-p_m(lambda)
from L283(5), and its uniform spectral sum s_m->0 in L283(6).
Put Q=C_12 L^-1 and Q_m=C_12 p_m(L). Since C_12^*C_12<=L,

\[
 \begin{split}
 \|Q\mathbf e_e\|^2&\le(L^{-1})_{ee}\le30,\\
 \|Q_m\mathbf e_e\|^2&\le(p_m(L)Lp_m(L))_{ee}\le30,\\
 \|(Q-Q_m)\mathbf e_e\|^2
 &\le(e_m(L)L e_m(L))_{ee}\le(e_m(L))_{ee}\le16s_m.
 \end{split}                                                   \tag{6}
\]

Here lambda e_m(lambda)^2<=e_m(lambda) and
lambda p_m(lambda)^2<=lambda^-1 on (0,16). These are quadratic-form
inequalities, so no commutation of C_12^*C_12 with L is required.
The last entry bound is L283's relative-mode bound, including normal
end links. Define G_{h,m}=Q_m^* diag(h) Q_m. Cauchy–Schwarz applied
to the two terms obtained by subtracting the products in (5) yields

\[
 \sup_{N,e,f}|(G_h-G_{h,m})_{ef}|
       \le 8\|h\|_\infty\sqrt{30s_m}=:\epsilon_m\to0,
 \qquad |(G_h)_{ef}|,|(G_{h,m})_{ef}|\le30\|h\|_\infty.
                                                               \tag{7}
\]

The constants are independent of the source position, anchors and mesh.
This estimates local entries; it does not approximate the inverse in
operator norm.

For fixed m, Q_m has finite path range m+1 (a larger fixed range also
suffices). For two edges e,f of a plaquette p, let x_p be its center.
Every source plaquette z contributing to (G_{h,m})_ef lies within
c_m a of x_p. Replacing h(z) by h(x_p) has error at most
30 c_m a ||grad h||_infinity, by the column norm bound in (6).
If the paths remain in the interior, their coefficients equal exactly
the full-lattice coefficients of Q_{infinity,m}. If paths encounter a
boundary, their anchors are within c'_m a of a face. The source support
has a fixed positive distance from every face, so, for sufficiently
large N at fixed m, all such paths have h(z)=h(x_p)=0. Their weighted
entries vanish exactly. This includes normal end links and corners;
no boundary estimate for an unweighted bulk inverse is assumed.

Write H_{infinity,m}=Q_{infinity,m}^*Q_{infinity,m}. It converges at
every fixed edge offset to

\[
 H_{12,\infty}=L_\infty^{-1}C_{12,\infty}^*C_{12,\infty}
                                      L_\infty^{-1}.        \tag{8}
\]

Precisely, its Fourier multiplier is p_m(lambda)^2 C_12(q)^*C_12(q).
Its matrix norm is bounded by 1/lambda, integrable in dimension four,
and it converges almost everywhere to the multiplier with p_m=1/lambda.
Dominated convergence proves convergence of every required offset.
Only finitely many component/offset pairs occur within a plaquette.
Consequently, taking N->infinity first and then m->infinity in (7),

\[
 \delta_N:=\max_{h\in\{h_-,h_+\}}\quad
 \sup_{p,\ e,f\in p}
 \left|(G_h)_{ef}-h(x_p)(H_{12,\infty})_{ef}\right|
                         \longrightarrow0.                \tag{9}
\]

The infinite-lattice entry is translated to the actual relative edge
offsets. Pinned slots are assigned zero in G_h; for large N every
plaquette containing such a slot has h(x_p)=0, so (9) extends to these
slots too. More explicitly the limsup error is bounded by epsilon_m
plus ||h||_infinity times the maximum of finitely many Fourier-entry
errors. This establishes the claimed order of limits without a rate.

### 2. The separated covariance on either time half

Partition all plaquettes, of all six orientations, by x_{p,4}<=0 or
x_{p,4}>0. On the first half every edge of p is at time <=a/2, whereas
h_+ is supported at time >=1. For a<=1 the separation is at least
1/2. Reverse the roles on the second half. The choice of where to put
centers at zero is immaterial but is fixed by this partition.

Use L284(7)–(8)'s exact kernel
R_{N,ez}=(GC_12^*)_{ez}=a^3 R_{a,mu_e}(x_e,z), which vanishes
identically for edge directions 3 and 4. The extension of its
separated uniform estimates to all spatial anchors and all times on
the indicated half needs justification: the same spatial sine/cosine
factors and their first derivatives are bounded on the whole closed
box. In the hyperbolic time formula of L003, with t<=s and s-t>=1/2,

\[
 |G_{a,\Omega}(t,s)|
 \le\frac{e^{-\Omega(s-t)/2}}{\Omega(1-e^{-2})}.
                                                               \tag{10}
\]

The inequality follows by bounding each sinh by half its positive
exponential, using a/sinh(a gamma)<=1/gamma,
gamma>=Omega/2, and 1-e^-16gamma>=1-e^-2. It holds up to the time
endpoints. Differentiating a numerator replaces sinh by gamma cosh;
bounding cosh by its positive exponential gives the same estimate
with a factor at most 2 Omega. Spatial differentiation introduces
at most pi|k|/8. Thus the R_a summands and all their first derivatives
are bounded by C(1+|k|)exp(-|k|/16), uniformly on the full separated
sets, because Omega>=|k|/4. This is summable. Fixed-mode convergence
as in L284 proves uniform convergence to the same continuum R and
uniform first-derivative bounds on those sets. At pinned tangential
slots the exact sine factors vanish; assigning those entries zero
is consistent with the formula.

For e,f belonging to a negative-half plaquette, (5) now gives

\[
 a^{-2}(G_+)_{ef}
   =a^4\sum_{z\parallel12}h_+(z)
                   R_{a,\mu_e}(x_e,z)R_{a,\mu_f}(x_f,z).
                                                               \tag{11}
\]

Uniform bounds and convergence, followed by uniform Riemann-sum
convergence on the compact source support, imply

\[
 (G_+)_{ef}=a^2 T^+_{\mu_e\mu_f}(x_p)+a^2o(1),\qquad
 T^+_{\mu\nu}(x)=\int_D h_+(y)R_\mu(x,y)R_\nu(x,y)dy.
                                                               \tag{12}
\]

The o(1) is uniform over ALL negative-half plaquettes and their slots.
Indeed coalescing x_e,x_f to x_p costs O(a) by the derivative bound;
the Riemann-sum error is uniform by the same bound in the y variables.
In particular |(G_+)_{ef}|<=C a^2. Components of T^+ involving 3 or
4 vanish. The corresponding assertions for G_- and T^- hold over
all positive-half plaquettes, by time reflection. No coincident-source
square is integrated in (11)–(12).

### 3. All-anchor error control and reduction to a bulk tensor

On negative-half plaquettes insert (9) for G_- and (12) for G_+ in
the contraction with U^p. Its error per plaquette is
a^2 O(delta_N+rho_N), with rho_N->0 the uniform error in (12).
This follows from (7), the bound C a^2 for the remote covariance,
bounded h and H_{12,infinity}, and the fixed finite sum of absolute
coefficients of U^p. The latter includes all edge/color slots and is
bounded uniformly in N by the explicit Wilson polynomial L279(8).
There are O(N^4) plaquettes. After division by N^2 the COMPLETE error
is bounded by C a^2 N^2(delta_N+rho_N)=64 C(delta_N+rho_N)->0.
The positive half has the same estimate. This is why (9) needs only
an o(1) local error: the other covariance supplies a uniform a^2.

The surviving negative-half expression is therefore the Riemann sum
of U^p contracted with h_-(x_p)H_{12,infinity} and T^+(x_p), with
each color covariance proportional to the identity. Since h_- has
interior support, every surviving plaquette has its full four slots
for sufficiently fine meshes. Every orientation grid has density a^-4.
The conversion factor is

\[
 \frac{a^2}{N^2}\sum_p=\frac1{64}\,a^4\sum_p.              \tag{13}
\]

To specify the finite bulk tensor exactly, contract U with H_{12,infinity}
on one pair of slots and take its row sum on constant external edge
fields. Denote this direction/color matrix by B_*. Global color
rotations make it scalar in color. Each coordinate reflection preserves
the action and C_12^*C_12 (the sign of C_12 itself is squared); on
constant fields it reverses just that direction. Hence off-direction
entries vanish. Interchanging coordinates 1 and 2 preserves the same
objects, so the first two direction diagonals agree; call their value
b_*. The other two diagonals are not needed, since T^+ has only 1,2
components. This row sum is equivalently the sum, per unit lattice cell,
of the six single-plaquette contractions on constant external fields.
There is no boundary identification in this definition.

It follows from (13), with three external colors, that

\[
 \lim N^{-2}\!\sum_{p:x_{p,4}\le0}
                  \mathcal U(U^p;G_-,G_+)
 =\frac{3b_*}{64}\int_D h_-(x)
                      \{T^+_{11}(x)+T^+_{22}(x)\}dx
 =\frac{3b_*}{64}\mathcal J_f.                             \tag{14}
\]

The internal color sum is already in B_*; the displayed factor three
counts the external color trace only. Symmetry of U permits exchange
of its covariance pairs. Reflection in time carries the positive-half
limit to (14), since R_1 and R_2 are even under simultaneous reflection
of their arguments and h_+ reflects to h_-. Although the partition
assigns the zero-time layer to one half, the limiting expressions are
supported at times at least one away from zero, so no extra interface
term occurs. Equivalently (9) and the all-anchor error estimate already
control that layer. The full contraction has limit 3b_* J_f/32.

### 4. Exact Wilson value of the bulk tensor

Use normalized Brillouin measure and put b_mu(q)=1-exp(iq_mu),
u_mu=|b_mu|^2, lambda=sum_mu u_mu. In tail-indexed edge coordinates,
the incidence row is C_12(q)=(b_2,-b_1,0,0). Thus (8)'s only
nonzero symbol entries are

\[
 H_{11}=u_2/\lambda^2,\quad H_{22}=u_1/\lambda^2,\quad
 H_{12}=-b_1\overline{b_2}/\lambda^2,\quad H_{21}=\overline{H_{12}}.
                                                               \tag{15}
\]

This fixes also the phases needed at distinct raw edge offsets.
Let

\[
 A=\int u_1^2/\lambda^2=Z_0-4I_1,\qquad
 J=\int (1-\cos q_1)(1-\cos q_2)/\lambda^2
       =\frac1{48}-\frac A{12}.                             \tag{16}
\]

These are L283(15)–(16)'s elementary integral identities: permutation
symmetry gives integral u_1/lambda^2=Z_0/4 and
4A+48J=1; u_1^2=4u_1-4sin^2 q_1 gives the first equality.
All integrals converge, since their numerators have at least quadratic
vanishing where required in dimension four.

For a constant external field in direction 1 and one unit color,
L283(12)–(13)'s exact Wilson trace contraction on a 1,nu plaquette is

\[
 c(g)=-\frac{g_{00}+g_{22}}{12}+\frac{g_{02}}6+g_{13}
             +\frac{-g_{01}+g_{03}+g_{12}-g_{23}}3.          \tag{17}
\]

Raw edges are 0=(0,1), 1=(e_1,nu), 2=(e_nu,1), 3=(0,nu).
Its normalization is E[4p_4(Z+r y)]_{r^2}=c(g), so the contracted
operator on the constant field contributes 4c(g). This retains the
internal three-color sum. We reuse that finite contraction, not an
isotropic substitution for H_{12,infinity}.

For nu=2, substituting (15) with these actual offsets gives

\[
 g_{00}=g_{22}=Z_0/4,\quad g_{02}=g_{13}=Z_0/4-A/2,\quad
 g_{01}=g_{23}=J,\quad g_{03}=g_{12}=-J.
                                                               \tag{18}
\]

For example g_02 is integral cos(q_2)u_2/lambda^2, while g_01
has the phase exp(-iq_1) multiplying H_12. Its real numerator
integrates to +(1-cos q_1)(1-cos q_2); the zero-offset cross entry
integrates to its negative. Odd sine terms vanish separately by
coordinate reflection. For nu=3 or 4 the direction-nu covariance and
all cross entries vanish, and

\[
 g_{00}=g_{22}=Z_0/4,\qquad g_{02}=Z_0/4-2J.                \tag{19}
\]

Indeed integral cos(q_nu)u_2/lambda^2 differs from Z_0/4 by
one half of integral u_nu u_2/lambda^2=4J. Equations (17)–(19) give

\[
 c_{12}=Z_0/4-7A/12-4J/3,\qquad c_{13}=c_{14}=-J/3,
\]
\[
 b_*=4(c_{12}+c_{13}+c_{14})
     =Z_0-7A/3-8J=Z_0-5A/3-1/6
     =-2Z_0/3+20I_1/3-1/6.                                \tag{20}
\]

The other plaquette orientations contain no direction-1 slot and
therefore contribute zero to this constant-field coefficient.
Coordinate interchange gives the same value in direction 2.
This proves (1). A supporting exact-rational check independently
enumerates the 35 ordered SU(2) monomials and substitutes the three
covariance tables in (18)–(19):
`python3 scripts/quartic-response/distinct-line-contraction.py`.
Its full certificate is
`scripts/quartic-response/distinct-line-contraction-certificate.json`.
This verifies finite algebra and the coefficient reduction, not the
analytic estimates or any continuum construction.

### 5. Assembly and qualifications

Multiplying the full limit after (14) by -1/4 proves (2).
L284 gives the sum of insertion limits a_* J_f/128, while L283 gives
the mixed-covariance action limit -3a_* S_f/128. Their sum with (2)
is (3), since a_*-3b_*=10Z_0-1-16I_1. L282 gives density coefficient
3d_* S_f/32 with d_*=-1/8-I_1; combining it with the S_f term in
(3) gives (4). These finite additions introduce no limit interchange.

The uniform local error (9), separated all-anchor bound (12), and the
explicit error sum preceding (13) prove o(N^2) for the whole residual;
the input lemmas provide the other three o(N^2) errors. No coincident
continuum kernel square or replacement of G_h by the bare G was used.
This completes the approved quartic target only. Section 6 records the
separate critical audit; no full kappa_a estimate,
quartic-only cancellation or sign conclusion follows merely from (4).

### 6. Separate critical audit (2026-10-26)

**Verdict.** Equations (1)–(4) pass under the exact hypotheses above,
including the complete o(N^2) errors. L283 section 5 and L284
section 5 audit the three upstream subfamilies in this same independent
audit step. Their L281/L282 source-field and tail inputs are used with
the previously audited exact bump and relative-domain hypotheses.
This accepts an existing partial asymptotic, not a new mathematical
discovery, a cubic cancellation, or a Yang–Mills candidate solution.
The pre-invocation complete-quartic critical-audit assessment approves
exactly these checks under EXPLORE. No new theorem or DAG input enters.

**Noncommuting energy estimate and every boundary path.** For any
edge vector v,
||C_12 e_m(L)v||^2<=<e_m(L)v,L e_m(L)v> follows directly from
C_12^*C_12<=L. Only e_m(L) is commuted with L, by the spectral
theorem. Applying this to a basis vector, and using
lambda e_m(lambda)^2<=e_m(lambda), proves the third line of (6).
The analogous inequalities with L^-1 and p_m(L) prove its first
two lines. Thus both columns have norm at most sqrt(30), and
the difference has norm at most 4sqrt(s_m). Subtracting
Q^*hQ-Q_m^*hQ_m in two products gives the entry error
8||h||_infinity sqrt(30s_m), uniformly in both columns and N.
This does not commute the source diagonal or C_12^*C_12 with L.

For fixed m, a contributing source cell is within a fixed number
of lattice steps of each anchor. Its physical distance from the
plaquette center is at most c_m a. Cauchy–Schwarz with the same
column norms bounds the source-weight replacement by
30 c_m a ||grad h||_infinity. If a path encounters any face,
the center and every source cell on it are within c'_m a of that
face. For fine mesh both weights are zero, since supp h has a
fixed positive distance from the entire boundary. This includes
corners and pinned slots; no unweighted boundary covariance is
replaced by a full-lattice value. In the bulk the path coefficients
are exactly the infinite ones. The infinite multiplier has norm
at most 1/lambda, since ||C_12(q)||^2=u_1+u_2<=lambda and
p_m(lambda)<=1/lambda. This integrable majorant proves every
fixed-offset limit in (8). The finitely many slot offsets, followed
by N->infinity and then m->infinity, give (9) uniformly over all
anchors, including those outside the source support. No rate for
delta_N is required or claimed.

**Both entire time halves and the full error sum.** For a<=1,
edges on a negative-center plaquette have time at most a/2; the
positive source has time at least 1. The opposite assignment works
on the other half. L284's hyperbolic estimate therefore applies
with separation at least 1/2. More precisely one may use the fixed
closed sets t<=1/2,s>=1 and t>=-1/2,s<=-1. All spatial sine/cosine
functions and their first derivatives are bounded on the full box,
including the faces. The time bound extends to both endpoints;
its derivatives are controlled by replacing numerator sinh by cosh.
The summands and every first derivative in either argument have
the summable majorant C(1+|k|)exp(-|k|/16). Fixed-mode convergence
is uniform there. Pinned tangential values vanish by their sine
factors, while normal links retain their actual cosine grids.

It follows that (11) is a uniformly convergent source Riemann sum,
also as the two edge arguments coalesce to the plaquette center.
The first-derivative bound controls this O(a) shift and the Riemann
error in every source variable. Hence (12) holds on each whole
assigned half with one common rho_N->0, and its remote covariance
is uniformly O(a^2). Source directions 3 and 4 vanish exactly.

On the negative half, write G_-=h_-H+E with |E|<=delta_N,
and G_+=a^2(T^++F) with |F|<=rho_N. All entries of H, T^+ and
G_- are bounded. After contracting with a fixed U^p, the error is
at most C a^2(delta_N+rho_N), absorbing the bounded product error.
There are at most six times O(N^4) plaquettes. The complete error
after division by N^2 is therefore at most
C a^2 N^2(delta_N+rho_N)=64C(delta_N+rho_N)->0.
The positive half has the identical estimate. It also covers the
zero-time layer, endpoint rows and intersecting boundary faces;
none is discarded. In the limiting term h_- or h_+ restricts the
anchors to the interior, permitting ordinary shifted-grid Riemann
sums. Thus this is full finite-box error control, rather than a
bulk coefficient with an unestimated remainder.

**Anisotropic Fourier table and Wilson normalization.** With raw
tail-indexed edges, C_12(q)=(b_2,-b_1,0,0), so C_12^*C_12 has
off-diagonal -conjugate(b_2)b_1=-b_1 conjugate(b_2).
This verifies (15) independently and distinguishes it from the
isotropic transverse covariance. For a 12-plaquette the raw pair
02 has multiplier cos(q_2)u_2/lambda^2, giving Z_0/4-A/2;
pair 13 gives the same value with 1 and 2 exchanged. The raw cross
offsets are exactly those checked in L283's audit: the phase
exp(-iq_1) in pair 01 turns the real cross numerator into +J;
zero-offset pair 03 gives -J. Pairs 12 and 23 give -J and +J.
The variance is Z_0/4. For the 13 and 14 plaquettes only direction
1 remains, and the offset covariance is Z_0/4-2J. These facts prove
the whole anisotropic tables (18)–(19) before their substitution.

Using L283's audited ordered trace formula gives
c_12=Z_0/4-7A/12-4J/3 and c_13=c_14=-J/3. Since the
r^2 coefficient of E[S_4(Z+r y)] is y^*B_*y/4,
b_*=4(c_12+c_13+c_14)=Z_0-7A/3-8J.
The identities A=Z_0-4I_1 and 4A+48J=1 give (1).
The existing exact-rational enumeration was rerun: 35 words in
each of three orientations, exact residual 0 against required 0,
zero failures. Its selected complete coefficients agree; the
Fourier and analytic checks above do not rely on that certificate.

The contraction's one-color row sum already includes its internal
three-color sum. The external trace adds precisely three. The
conversion a^2 N^-2 sum_p=(1/64)a^4 sum_p gives 3b_* J_f/64
on the negative half. Time reflection preserves both spatial edge
directions and the source orientation; symmetry of U exchanges
its covariance pairs, so the positive half has the same limit.
This is a partition of the anchors, not an extra source derivative.
The full limit is 3b_* J_f/32, and its action prefactor -1/4
gives (2). L280(20) supplies exactly two insertion prefactors +1/4
and the mixed-inverse prefactor -1/4, as obtained by differentiating
-U(s,t)[G(s,t),G(s,t)]/8. The audited L283/L284 limits therefore
assemble to (3), with a_*-3b_*=10Z_0-1-16I_1. Adding the full
density uses d_*-a_*/4=1/4-2Z_0-2I_1, giving (4).
No sign of the combined coefficient or interchange with the coupling
limit has entered. Cubic compensation, a uniform higher remainder
and the continuum/infrared construction remain independent gaps.

## Mathlib

Full matching coverage of the differentiated local covariance limit,
the all-anchor quartic asymptotic and its Wilson coefficient: **not
checked**. No matching theorem name or link is asserted. The argument
uses the canonical relative-mode identities in L003/L280, L279's
ambient Wilson tensors, L283's spectral approximation and exact finite
trace formula, L284's separated kernel, and L282's density result.
It extends their estimates to the differentiated internal covariance
and both time halves rather than importing a bulk theorem outside its
hypotheses. The reused assessment is
`drafts/literature/2026-10-26-quartic-response-quadratic-asymptotic.md`;
no inspected external theorem there gives this finite-box asymptotic.
Originality is not certified; section 6 accepts this local proof only.
