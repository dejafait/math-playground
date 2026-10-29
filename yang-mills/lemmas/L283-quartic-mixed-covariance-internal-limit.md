# L283 — Internal-kernel limit for the quartic mixed-covariance action term

## Hypotheses

Use exactly L280's SU(2) relative box: even N>=2, a=8/N,
boundary-contained links pinned, boundary-fixed gauge transformations,
and every remaining link, including both normal end-link cases,
variable. All source derivatives are at zero in its real domain
(|s|+|t|)||f_*||_infinity<eta<1. Retain L002's exact product bump
as specified in L282. Use L279(8)–(9)'s all-link jets evaluated on
L280's own slice, without transporting higher forest jets.

Let U be the symmetric fourth tensor of S_4^H=U_ijkl x_i x_j x_k x_l/24
in L280(18)–(20), with the ambient all-link polynomial specified by
L279(8)–(9), rather than an arbitrary extension from the slice.
Indices include edges and three colors. Let G and
G_-+ be its extended transverse covariance and mixed inverse derivative.
Write lambda(q)=4 sum_mu sin(q_mu/2)^2 and use normalized Brillouin
measure dq/(2pi)^4 on [-pi,pi]^4. Define

\[
 Z_0=\int\lambda(q)^{-1}\frac{dq}{(2\pi)^4},\qquad
 I_1=\int\frac{\sin^2q_1}{\lambda(q)^2}\frac{dq}{(2\pi)^4},\qquad
 a_*=8Z_0-\frac32+4I_1.                                    \tag{1}
\]

Both integrals are finite in dimension four. The values at q=0 are
irrelevant. Let S_f>0 and d_*=-1/8-I_1 have precisely L282's meaning.

## Conclusion

For the SINGLE action response in L280(20), put

\[
 M_{4,N}=-\frac14\mathcal U(U;G_{-+},G).
\]

Then, with all colors, both source orders and the complete finite box,

\[
 \boxed{\quad N^{-2}M_{4,N}\longrightarrow
                  -\frac{3a_*}{128}\mathcal S_f.\quad}       \tag{2}
\]

In particular the error for this term is o(N^2). Combining only this
term with L282's COMPLETE density response gives

\[
 \boxed{\quad
 N^{-2}\{M_{4,N}+\operatorname{Tr}(D G_{-+})\}
 \longrightarrow\frac3{32}
       \left(\frac14-2Z_0-2I_1\right)\mathcal S_f<0.
 \quad}                                                     \tag{3}
\]

This is NOT the complete quartic asymptotic. The residual is exactly

\[
 \mathcal K_4^H-M_{4,N}
  =\frac14\mathcal U(U_-;G_+,G)
   +\frac14\mathcal U(U_+;G_-,G)
   -\frac14\mathcal U(U;G_-,G_+).                            \tag{4}
\]

No bound or limit for (4), no compensation by the complete cubic
family, and no uniform higher perturbative remainder is asserted.
All interacting, continuum, positivity, nonzero-sector and finite
positive-mass gaps remain. This is partial local work within the
approved complete-quartic EXPLORE target; originality beyond the
sources checked is not claimed. Section 5 records its separate critical audit.

## Proof

### 1. Uniform approximation of the internal local covariance

Suppress color in this section. Write L=C*C+BB*, Delta=B*B, retaining
L280's full relative domains. L280(23) gives
G=L^-1-B Delta^-2 B*. Define the polynomial and its remainder

\[
 h_m(\lambda)=\frac1{16}\sum_{j=0}^m(1-\lambda/16)^j,
 \qquad e_m(\lambda)=\lambda^{-1}(1-\lambda/16)^{m+1},
\]
\[
 G_{N,m}=h_m(L)-B h_m(\Delta)^2B^*.                          \tag{5}
\]

Every eigenvalue of L and Delta is in (0,16), with the relative tensor
modes of L003. For each one-form component, its own coordinate index
can be zero; the other three are positive. Vertex indices are all
positive. Each normalized eigenvector has squared value at most
16/N^4. For a vertex mode u_k,
|(Bu_k)_e|^2<=16 lambda_k/N^4, including the first and last normal
links: take the exact difference of the sine mode to obtain its
midpoint cosine. This is the same endpoint identity used in L282(8).

Let s_m be the supremum of N^-4 sum_k e_m(lambda_k), over N>=2
and over the vertex mode set and each of the four one-form mode sets.
There is no zero eigenvalue in any of these sets. If max k=r>=1,
there are at most 15r^3 indices and lambda_k>=4|k|^2/N^2.
Consequently N^-4 sum lambda_k^-1<=15/8. If lambda_k<=delta,
then r<=N sqrt(delta)/2, and summing (15/4)N^-2 r gives
N^-4 sum_{lambda<=delta}lambda^-1<=15delta/16. This remains
valid if the sum is empty. Thus, for 0<delta<16,

\[
 s_m\le\frac{15\delta}{16}
       +\frac{15}{8}(1-\delta/16)^{m+1}\longrightarrow0,     \tag{6}
\]

where first choose delta small and then m large.

The positive matrix E_1=L^-1-h_m(L) has every diagonal <=16s_m.
The matrix E_2=B(Delta^-2-h_m(Delta)^2)B* is also positive, since
0<=h_m(lambda)<=lambda^-1. Put r=(1-lambda/16)^{m+1}; then

\[
 \lambda(\lambda^{-2}-h_m(\lambda)^2)
       =(2r-r^2)/\lambda\le2e_m(\lambda).
\]

The vertex difference bound gives every diagonal of E_2 <=32s_m.
For a positive matrix |E_ef|<=sqrt(E_ee E_ff), including off-diagonal
component blocks. Since G-G_{N,m}=E_1-E_2,

\[
 \sup_{N,e,f}|G_{ef}-(G_{N,m})_{ef}|\le48s_m\longrightarrow0.\tag{7}
\]

This is an entry bound, not an operator-norm approximation to G.
It controls diagonal and nearby internal pairs uniformly at all
boundaries, with all normal links retained. L280(22)–(23) also gives
|G_ef|<=30. These statements tensor with the color identity.

### 2. The contracted local operator and its boundary control

Define symmetric matrices, now with colors,

\[
 (A_N)_{ij}=\sum_{kl}U_{ijkl}G_{kl},\qquad
 (A_{N,m})_{ij}=\sum_{kl}U_{ijkl}(G_{N,m})_{kl}.              \tag{8}
\]

Here G_kl includes delta of the two internal colors, so the internal
sum retains all three colors. Global color rotations make each A
a scalar in external color. Each nonzero U entry has its four edge
indices in one plaquette. Each edge belongs to at most six plaquettes,
each with at most four variable slots and three colors per slot.
Formula L279(8) is a fixed finite polynomial with fixed coefficients.
It follows directly that the finite constant

\[
 C_U=\sup_{N,i}\sum_{jkl}|U_{ijkl}|<\infty                 \tag{9}
\]

is independent of N. Pinned slots only delete terms. In particular,
row sums, symmetry, (7), and |G_kl|<=30 imply

\[
 \|A_N\|\le30C_U,\qquad
 \sup_N\|A_N-A_{N,m}\|\le48C_U s_m\longrightarrow0.         \tag{10}
\]

Both A operators couple only edges of a common plaquette, even though
their coefficients contain a covariance. For fixed m, every entry of
G_{N,m} is a polynomial path sum in the relative nearest-neighbor
matrices. If a plaquette is more than R_m=4m+8 lattice units from
the boundary, all coefficients in its contracted A_{N,m} are exactly
those on the infinite lattice. The same holds for the complete row
after increasing the layer by two units, already covered by R_m.
All other rows form a layer with O_m(N^3) edges; face intersections
and normal end links are included in that count.

The infinite-lattice operator A_m has a finite-range translation
invariant kernel. Its row-sum matrix is a_m times the direction and
color identity. To see this, the quartic Wilson action and covariance
are invariant under translations, lattice coordinate permutations and
reflections, with oriented edge fields changing sign when orientation
reverses, and under global color rotations. These symmetries also hold
for (5) and its contraction. On a constant field, reflection in one
coordinate kills a direction off-diagonal row sum; permutations make
the direction diagonals equal; color rotations give the color identity.

For a smooth vector field v sampled on all relative edge grids,
the bounded row sums and finite range therefore give
A_{N,m}S_a v-a_m S_a v=O_{m,v}(a) on interior rows. On the boundary
layer the difference is uniformly bounded by (10) and boundedness of
v. Its squared physical norm, using a^4 sum_e, is O_{m,v}(a^4N^3),
which tends to zero. Thus

\[
 \|A_{N,m}S_a v-a_m S_a v\|_a\longrightarrow0
                                      \quad(m\text{ fixed}).\tag{11}
\]

### 3. Exact bulk coefficient from the Wilson jet

Use raw edge coordinates on a mu,nu plaquette with edges
0=(0,mu), 1=(mu,nu), 2=(nu,mu), 3=(0,nu), and signs
epsilon=(1,1,-1,-1). Let g_ij be a one-color covariance of these raw
edge values. Set the external field to r times a fixed unit color on
all mu edges and zero on other directions. In the degree-two term
of E[S_4(Z+r y)], (8) and symmetry give r^2 y*A y/4.

For completeness the finite contraction on ONE plaquette is explicit.
For each n_0+...+n_3=4, form the ordered word w of n_0 zeros,
n_1 ones, n_2 twos, n_3 threes. For each choice J of two of its four
positions with w_j in {0,2}, put the unit external color there and
put a common internal color c in the other two positions. Sum c=1,2,3.
The contribution to the raw covariance g_{w_l,w_h}, for the complementary
positions {l,h}, is

\[
 -\frac{2\prod_{j=1}^4\epsilon_{w_j}}{\prod_{i=0}^3 n_i!}
 \sum_{c=1}^3\operatorname{Tr}(t^{a_1}t^{a_2}t^{a_3}t^{a_4}).\tag{12}
\]

The factor -2 is exactly 4p_4 in L279(8), without a factorial change.
The trace is
(delta_ab delta_cd-delta_ac delta_bd+delta_ad delta_bc)/8.
Its internal-color sum is 3/8 when the external positions are adjacent
cyclically and -1/8 when they alternate. Summing the 35 ordered
monomials in (12), combining symmetric raw pairs, gives the following
complete coefficient of r^2 in E[4p_4]:

\[
 c(g)=-\frac{g_{00}+g_{22}}{12}+\frac{g_{02}}6+g_{13}
       +\frac{-g_{01}+g_{03}+g_{12}-g_{23}}3.                 \tag{13}
\]

There are no g_11 or g_33 terms and no other pairs. Formula (12)
specifies each term of this finite enumeration, including repeated-edge
monomials. The exact-rational script
`scripts/quartic-response/constant-field-contraction.py` checks all
35 monomials and records the eight coefficients and two independent
degeneracies in its certificate. A constant Gaussian only in direction
mu gives zero; one only in direction nu gives coefficient one, as
also follows directly from the constant-field plaquette commutator.
The script verifies finite algebra only, not the analytic limits here.

The infinite-lattice limit of (5) has symbol, in tail-indexed edges,

\[
 g_{\mu\nu}(q)=\frac{\delta_{\mu\nu}}{\lambda(q)}
       -\frac{b_\mu(q)\overline{b_\nu(q)}}{\lambda(q)^2},
 \qquad b_\mu(q)=1-e^{iq_\mu}.                              \tag{14}
\]

Indeed (5)'s symbol is h_m(lambda)I-h_m(lambda)^2 b b*. Its entries
are dominated by 2/lambda, an integrable function in four dimensions,
and tend pointwise almost everywhere to (14). Every fixed-offset
entry therefore converges, so a_m tends to the row sum computed from
(13) with (14). This uses a finite number of integrals, not a
finite-domain bulk replacement without error control.

Here is its evaluation with all offsets retained. Set
J=integral (1-cos q_mu)(1-cos q_nu)/lambda^2 for mu!=nu. Symmetry
and the exact edge offsets give

\[
 g_{00}=g_{22}=g_0=3Z_0/4,\quad
 g_{02}=g_{13}=H=g_0-1/8+2J,\quad
 g_{01}=g_{23}=J,\quad g_{03}=g_{12}=-J.                    \tag{15}
\]

For example g_01 has the additional phase exp(-iq_mu) multiplying
g_mu,nu(q); the real integral is +J. The zero-displacement cross entry
g_03 has integral -J. Also integral cos(q_nu)/lambda=Z_0-1/8 and
integral cos(q_nu)|b_mu|^2/lambda^2=Z_0/4-2J, proving H.
Substituting into (13) gives c(g)=g_0-7/48+J.
There are three plaquette orientations containing a given direction.
Because the quadratic expectation is y*A y/4, the bulk row sum is

\[
 a_*=12c(g)=9Z_0-7/4+12J.                                  \tag{16}
\]

To reduce this to (1), put u_mu=2(1-cos q_mu), lambda=sum u_mu,
A=integral u_1^2/lambda^2. Permutation symmetry yields
4A+12 integral u_1 u_2/lambda^2=1, hence 12J=1/4-A.
The identity u_1^2=4u_1-4 sin(q_1)^2 and symmetry
integral u_1/lambda^2=Z_0/4 give A=Z_0-4I_1. These finite integrals
prove (1) and a_m->a_*. No continuum scalar inverse-square theorem
has been imported at its excluded borderline dimension.

Combining (10), (11) and a_m->a_* proves

\[
 \|A_NS_a v-a_*S_a v\|_a\longrightarrow0.                  \tag{17}
\]

The order is first fixed m and N->infinity, then m->infinity. Uniform
boundedness in (10) extends (17), by finite-mode approximation and
Cauchy–Schwarz, to inner products of strongly convergent discrete
fields in exactly the physical-norm sense of L282(19).

### 4. External source sums, both orders and comparison with density

The contraction definition and symmetry give the exact identity
mathcal U(U;G_-+,G)=Tr(A_N G_-+). No nonlinear observable is being
replaced by its curvature law: only the quadratic covariance and its
source derivatives enter this trace.

Use L281's exact separated factorization and L282's fields
X_{pm,k,a}=aGC* sigma_{pm,k,a}. Their strong convergence, proved in
L282(20)–(21), and (17) give for each fixed k

\[
 \langle X_{+,k,a},A_N X_{-,k,a}\rangle_a
       \longrightarrow a_*\langle X_{+,k},X_{-,k}\rangle.
\]

Exactly as in L282(22), finite-dimensional trace cyclicity gives

\[
 N^{-2}\operatorname{Tr}(A_N G_{-+})
   =\frac6{64}\sum_{k\in\mathcal K_N}b_{k,a}
       \langle X_{+,k,a},A_N X_{-,k,a}\rangle_a.              \tag{18}
\]

There are three equal color blocks and two equal source orders:
the latter follows by transposing the trace, since A_N and G are
symmetric. The normalization is a^2N^2=64, as in L282. In particular
the internal-color contraction already in A_N introduces no further
color factor beyond these three external color blocks.

For any uniformly bounded symmetric one-color edge matrix E_N with
norm <=M, L281's factorization, ||U_pm||<=sqrt(F/12)N and trace-norm
tail yield

\[
 \left|N^{-2}\operatorname{Tr}(E_NG_{-+})\big|_{|k|>R}\right|
       \le\frac{MF}{2}\,m_a(>R)
       \le\frac{M}{2}\,8^4 F^2 C_{\rm sep}(>R)\to0.         \tag{19}
\]

The same estimate bounds the sum of absolute mode contributions:
apply ||U_pm v_k||<=sqrt(F/12)N||v_k|| to each positive rank-one
term of L281's expansion before summing. Thus it does not require
positivity of E_N. Take M=30C_U in (19). This controls every external
tail in (18) uniformly, while all internal anchors remain included.
Taking finite-mode limits first and then R->infinity proves
N^-2 Tr(A_N G_-+)->(3a_*/32)S_f. Multiplication by -1/4 proves (2).

L282(5), (1) and d_*=-1/8-I_1 give (3). Its strict sign requires no
numerical integral: Cauchy–Schwarz and integral lambda=8 imply
Z_0>=1/8, while I_1>0. Hence 1/4-2Z_0-2I_1<0; L282 gives S_f>0.
The other three terms remain exactly (4). In particular (19) does
not apply to their distinct internal source derivatives just by
calling them a covariance. No complete-quartic or full-coefficient
cancellation follows from this partial comparison.

### 5. Separate critical audit (2026-10-26)

**Verdict.** Equations (2)–(3) pass under the hypotheses above, using
L281/L282 with their separately audited exact hypotheses. This accepts
an existing partial result; it does not add a new asymptotic or establish
the complete interacting coefficient. The audit used the unchanged
complete-quartic critical-audit EXPLORE assessment.

**Uniform local input.** The counting-normalized component modes are
products of factors bounded by sqrt(2/N), including the zero cosine
factor N^-1/2. A vertex-mode difference on either normal endpoint
is exactly a midpoint cosine times 2 sin(pi k_mu/(2N)); extending
the boundary vertex value by zero gives the same identity there.
Thus the squared point bounds 16/N^4 and 16 lambda_k/N^4 hold on
every required row. Each mode family is a subset of nonnegative
four-tuples with maximum r, whose number is at most 15r^3; its
eigenvalues satisfy lambda_k>=4r^2/N^2. For the low-frequency sum
put M=floor(N sqrt(delta)/2). If M=0 it is empty; otherwise
sum_{r<=M}r<=M^2 gives 15 delta/16, while the unrestricted sum
is at most 15/8. Splitting at delta proves (6) by choosing delta
first and m second, uniformly in N, also for the one-form zero-index
sectors. There is no inverse operator-norm approximation here.

With r=(1-lambda/16)^(m+1), the two positive error multipliers are
r/lambda and (2r-r^2)/lambda^2. The vertex differences supply the
extra lambda in the second diagonal estimate. Positivity therefore
bounds every entry of E_1 and E_2 by 16s_m and 32s_m respectively.
Only after contracting with U does the finite plaquette row allowance
C_U convert (7) into the symmetric row-sum operator estimate (10).
This order avoids an invalid norm bound for G itself.

For fixed m, h_m(L) and B h_m(Delta)^2 B^* are finite path sums.
Their bulk entries agree with the full-lattice entries whenever the
entire path neighborhood avoids every boundary face. The remaining
O_m(N^3) rows include face intersections and normal end links. Their
bounded values have squared physical contribution O_m(a^4 N^3).
Interior shifts of a smooth sampled field cost O_m(a). Reflection
and coordinate permutations of the oriented Wilson polynomial give
the scalar row sum a_m; global color rotations give its color
identity. These facts verify (11), including its boundary passage.
The Fourier majorant 2/lambda is integrable in four dimensions, so
fixed-offset convergence gives a_m->a_*. Taking N first, then m,
proves (17). The uniform operator bound extends the resulting inner
products to the strongly convergent L282 fields by finite-mode
approximation; pointwise convergence of those fields is not assumed.

**Wilson trace and Fourier phases.** Directly from t^c=i sigma^c/2,
Tr(t^a t^b t^c t^d)=(delta_ab delta_cd-delta_ac delta_bd+
delta_ad delta_bc)/8. Its internal-color sums are 3/8 and -1/8
in the two cyclic position cases. Expanding the four exponentials
with their individual factorials gives exactly (12), with -2=4(-1/2).
The 35 weak compositions and their six possible external-position
choices give the eight coefficients in (13), retaining the repeated
raw edges. The existing exact-rational script was rerun: all eight
coefficients agree exactly, with constant-field degeneracies 0 and 1.
This is a finite-algebra check only.

Independently, use inverse Fourier kernel exp(iq(x-y)). With
b_mu=1-exp(iq_mu), the cross multiplier is -b_mu conjugate(b_nu).
The raw pair 01 has displacement -e_mu, so its multiplier includes
exp(-iq_mu). Its integrated real numerator is
+(1-cos q_mu)(1-cos q_nu); pair 03 has zero displacement and the
negative numerator. Pair 12, with displacement e_mu-e_nu, gives
-J; pair 23 gives +J. The same-direction variance is 3Z_0/4;
the offset-one entry is 3Z_0/4-1/8+2J. This verifies the whole
table (15), not just its diagonal. Consequently
12c=9Z_0-7/4+12J. The exact identities
4A+48J=1 and A=Z_0-4I_1 reduce it to (1).

**All source modes and normalization.** In one color the two traces
with the opposite orders of K_- and K_+ are equal by transpose and
cyclicity, because A_N is symmetric. The other factor three is the
external color trace; the internal color sum already belongs to A_N.
Inserting L281's a^4 b_{k,a} mode expansion and
GC^*sigma=a^-1 X gives 6/(a^2 N^2)=6/64 after passing to the
physical inner product. This proves (18)'s normalization independently.
The tail estimate is valid for every bounded symmetric E_N:
||U_+^* E_N U_-||<=MF N^2/12, and the two orders and three colors
give MF/2 times the separated trace-norm tail. Applied rank by rank
it also bounds the absolute mode tail. Taking E_N=A_N therefore
justifies summing the fixed-mode limits without deleting any internal
anchor. Multiplication by -1/4 gives (2). With d_*=-1/8-I_1,
d_*-a_*/4=1/4-2Z_0-2I_1, verifying (3). Finally Z_0>=1/8 by
Cauchy–Schwarz, I_1>0 and L282's S_f>0 prove the stated strict sign.
The three other quartic terms remain outside this lemma's conclusion.

## Mathlib

Coverage of the full partial asymptotic, its relative-domain internal
kernel comparison, and the exact Wilson contraction: **not checked**.
No matching Mathlib theorem or supporting name/link is claimed.
The proof uses the recorded finite relative spectral decomposition,
finite SU(2) matrix traces and Gaussian pairings, polynomial path
identities, elementary dominated convergence and Cauchy–Schwarz.
The broader literature assessment is
`drafts/literature/2026-10-26-quartic-response-quadratic-asymptotic.md`;
no inspected source there supplies this complete subfamily evaluation.
This is a local partial advance, without a certified novelty claim.
