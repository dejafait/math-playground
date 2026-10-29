# L284 — Separated limits of both quartic insertion responses

## Hypotheses

Use exactly L280's SU(2) relative box and L283's hypotheses: even
N>=2, a=8/N, boundary-contained links pinned, boundary-fixed gauges,
every other link including both normal end-link cases variable,
three colors, and L002's exact real product bump f. Sources have
(|s|+|t|)||f||_infinity<eta<1, and derivatives are at zero. Put
h_+=f and h_-=theta f, supported respectively in
[-1/4,1/4]^3 times [1,2] and [-2,-1].

Use L279(8)–(9)'s ambient all-link fourth Wilson tensors evaluated
on L280's own slice. Let U^p be the symmetric tensor of the single
plaquette polynomial 4p_4, with the convention 4p_4=U^p[x^4]/24.
Thus U=sum_p U^p and U_h=sum_{p parallel12} h(z_p)U^p. Pinned
slots are zero. G and G_pm are exactly L280(18)'s extended transverse
covariance and single inverse derivatives; mathcal U is L279(24)'s
contraction. Retain L283's constants Z_0, I_1 and

\[
 a_*=8Z_0-\frac32+4I_1,\qquad \beta_*=a_*/3.                 \tag{1}
\]

L283 is used with the hypotheses above. Its separate audit and the
separate audit in section 5 below accept these partial inputs.

## Conclusion

Let R_mu(x,y) be the off-diagonal, one-color kernel of
mathscr L^-1 d_12^* from relative 12-forms to one-forms on
D=[-4,4]^4, with measure dy. Here mathscr L has exactly L003's
relative tensor sine/cosine modes, as in L282. Only the opposite
source supports are used, so this notation makes no assertion of
an integrable coincident-point square. Define

\[
 \mathcal J_f=\int_D\!\int_D h_-(x)h_+(y)
                  \sum_{\mu=1}^2 R_\mu(x,y)^2\,dy\,dx.
                                                               \tag{2}
\]

This is finite and nonnegative. With all three colors included,

\[
 \boxed{\quad
 \lim N^{-2}\frac14\mathcal U(U_-;G_+,G)
 =\lim N^{-2}\frac14\mathcal U(U_+;G_-,G)
 =\frac{a_*}{256}\mathcal J_f .\quad}                       \tag{3}
\]

Limits are through even N. Each assertion includes an o(N^2)
error for its complete finite-box term. Consequently the sum I_{4,N}
of these two insertion responses has limit

\[
 N^{-2}I_{4,N}\longrightarrow\frac{a_*}{128}\mathcal J_f.
                                                               \tag{4}
\]

Together with L283 and L282 this controls three of the four quartic
terms and the complete density, with partial combined coefficient

\[
 N^{-2}\{I_{4,N}+M_{4,N}+\operatorname{Tr}(DG_{-+})\}
 \longrightarrow
 \frac{a_*}{128}\mathcal J_f+
 \frac3{32}\left(\frac14-2Z_0-2I_1\right)\mathcal S_f.       \tag{5}
\]

No sign of (5) is asserted. The remaining quartic term is EXACTLY

\[
 \mathcal K_4^H-I_{4,N}-M_{4,N}
             =-\frac14\mathcal U(U;G_-,G_+).                \tag{6}
\]

No bound or limit for (6), complete quartic coefficient, cubic
compensation or uniform higher remainder is established. The
interacting comparison, physical trajectory/composite mixing,
continuum axioms, positive sector and finite positive mass remain
unresolved. This is partial local progress under the approved
EXPLORE target, without certified originality beyond checked sources.

## Proof

### 1. The exact separated edge-to-plaquette kernel

Suppress color. Let C_12 consist of the 12 rows of the unscaled
relative plaquette incidence. Put

\[
 R_{N,ep}=(GC_{12}^*)_{ep},\qquad
 R_{a,\mu}(x_e,z_p)=a^{-3}R_{N,ep}\quad(e\parallel\mu).
                                                               \tag{7}
\]

The identity GC^*=L^-1 C^*, with L=C^*C+BB^*, follows from
L280(23) and B^*C^*=0. Its relative component Laplacians are block
diagonal by L003 section 2. Since C_12^* has components only in
1 and 2, R_{a,3}=R_{a,4}=0 exactly, including on normal end links.

Here is a full formula for the nonzero components and their limit.
Use v_k,e_k,omega_{k,a},Omega_{k,a},phi_k from L003 section 2.
For spatial k with k_1>=0,k_2>=1,k_3>=1 put
chi_{1,k}(x)=e_{k_1}(x_1)v_{k_2}(x_2)v_{k_3}(x_3).
For k_1>=1,k_2>=0,k_3>=1 put
chi_{2,k}(x)=v_{k_1}(x_1)e_{k_2}(x_2)v_{k_3}(x_3).
Use k_j<=N-1 in both finite sums. With x=(x_sp,t), y=(y_sp,s),

\[
 \begin{split}
 R_{a,1}(x,y)&=-\sum_k\omega_{k_2,a}\chi_{1,k}(x_{sp})
                       \phi_k(y_{sp})G_{a,\Omega_{k,a}}(t,s),\\
 R_{a,2}(x,y)&=\phantom{-}\sum_k\omega_{k_1,a}\chi_{2,k}(x_{sp})
                       \phi_k(y_{sp})G_{a,\Omega_{k,a}}(t,s).
 \end{split}                                                   \tag{8}
\]

These are identities at their respective edge and plaquette grids.
Indeed d_12 A=D_1 A_2-D_2 A_1, and the exact sine/cosine
identities in L003 give respectively +omega_{k_1,a} and
-omega_{k_2,a} for its adjoint. The time coordinate is a vertex
coordinate for both edge components and the source 12-plaquette.
The common denominator and Green kernel are those of L003
sections 2–3. To check normalization without
an implicit counting-measure change, the physical operator is
(L/a^2)^-1(C_12^*/a)=aGC_12^*. Its matrix relative to the measure
a^4 sum has point kernel a^-3 GC_12^*, precisely (7).

Extend the right sides of (8) to continuous spatial arguments by
the displayed trigonometric functions, and to separated time
arguments by L003's hyperbolic formula. Take fixed compact
neighborhoods

\[
 E_-=[-1/2,1/2]^3\times[-9/4,-3/4],\qquad
 E_+=[-1/2,1/2]^3\times[3/4,9/4].                            \tag{9}
\]

For x in E_- and y in E_+, their time difference is at least 3/2.
The same estimates apply in the reverse order by the symmetry of
the scalar time Green function. L003 section 4 gives
|k|/4<=Omega_{k,a}<=pi|k|/8 and
Omega_{k,a}/2<=gamma_{k,a}<=Omega_{k,a}. From its exact formula,
for t<s with s-t>=1,

\[
 |G_{a,\Omega}(t,s)|
 \le\frac{e^{-\Omega(s-t)/2}}{\Omega(1-e^{-2})}.             \tag{10}
\]

For clarity, bound each numerator sinh by half its positive
exponential, use a/sinh(a gamma)<=1/gamma, and
sinh(8 gamma)=e^{8 gamma}(1-e^{-16 gamma})/2.
Since gamma>=|k|/8>=1/8, the last factor is at least 1-e^-2.
This proves (10), using 2 gamma>=Omega. All spatial basis factors
are bounded by 1/2 in each coordinate. Since omega_{k_j,a}<=Omega,
each summand of (8) is bounded by

\[
 C e^{-|k|/8},                                               \tag{11}
\]

with C independent of N,k,x,y. One derivative in a continuous
spatial argument introduces at most pi|k|/8. One time derivative
replaces a numerator sinh by gamma cosh and has the same bound
with an additional factor at most 2 Omega. Thus all first derivatives
of each summand are bounded by C'(1+|k|)e^-|k|/8 on (9).
These majorants are summable over the three indices, including
zero cosine indices. They control the complete mode tails uniformly.

For fixed k, omega_{k_j,a}->pi k_j/8 and the exact time kernel
converges to

\[
 G_{\Omega_k}(t,s)
 =\frac{\sinh(\Omega_k(\min(t,s)+4))
         \sinh(\Omega_k(4-\max(t,s)))}
        {\Omega_k\sinh(8\Omega_k)} .                        \tag{12}
\]

This follows directly from L003's formula and gamma->Omega;
it also holds for the first derivatives on (9). Fixed modes are
present for all sufficiently large N. Finite-mode convergence and
(11) therefore give uniform convergence R_{a,mu}->R_mu on both
E_- times E_+ and E_+ times E_-, and a uniform first-derivative
bound there. The limiting series is (8) with omega replaced by
pi k_j/8, all allowed indices retained and (12) substituted.
Its mode coefficients identify it with mathscr L^-1 d_12^*.
This proves the stated meaning of R without using a full-space
scalar kernel or omitting any relative mode. In particular (2)
is finite by boundedness on separated compact supports.

As a supporting finite check, run
`python3 scripts/quartic-response/insertion-kernel-check.py`.
It independently applies the raw relative component Laplacian to
selected columns from (8) and compares with the oriented C_12^*
columns. On N=4,6 it checks 5148 rows, including 1824 normal endpoint
rows, with maximum residual 1.023e-15 against the required 2e-11
floating-point tolerance and no failures. The full residuals and
qualifications are saved in
`scripts/quartic-response/insertion-kernel-certificate.json`.
This checks finite signs, relative endpoint stencils and mesh factors;
the analytic mode identities and uniform estimates above, rather
than numerical tolerances, justify the theorem.

### 2. Weighted local contraction and its complete row sum

On all edge/color indices define

\[
 (A_{h,N})_{ij}=\sum_{p\parallel12}h(z_p)
                                  \sum_{kl}U^p_{ijkl}G_{kl}.
                                                               \tag{13}
\]

The internal covariance includes its three-color Kronecker delta.
Global color rotations imply A_{h,N}=\widetilde A_{h,N} tensor I_3;
henceforth A denotes its scalar color block. It is symmetric and
couples only edges of a common 12-plaquette. Its rows in directions
3 and 4 are identically zero.

Use L283(5)–(7)'s polynomial approximation G_{N,m}, tensor I_3,
and write A_{h,N,m} for (13) with this internal covariance. Set

\[
 C_{\mathrm{loc}}=\sup_{N,i}
           \sum_{p\parallel12}\sum_{jkl}|U^p_{ijkl}|<\infty.
\]

This finiteness follows from L279(8): each edge lies in at most
two 12-plaquettes, with four edge slots and three colors per slot,
and fixed quartic coefficients; pinned slots only delete terms.
Taking one fixed external color block cannot increase this bound.
L283's estimates, including every normal link, imply

\[
 \sup_N\|A_{h,N}\|\le30\|h\|_\infty C_{\mathrm{loc}},\qquad
 \sup_N\|A_{h,N}-A_{h,N,m}\|
       \le48\|h\|_\infty C_{\mathrm{loc}}s_m,\quad s_m\to0.
                                                               \tag{14}
\]

The same last bound holds for every absolute row sum, directly
from the entry error before the symmetric Schur estimate. Thus it
also bounds the sup-norm error on any bounded edge field. This is
a uniform local covariance estimate, rather than operator-norm
approximation of G itself.

For fixed m the polynomial has finite path range R_m as in L283
section 2. The compact support of h stays a fixed distance from
all boundary faces. For sufficiently large N every plaquette
contributing to (13), and every path needed for its G_{N,m}
entries, therefore lies in the interior. Its coefficients equal
the infinite-lattice coefficients exactly. No boundary row is
replaced or deleted; the weighted operator is zero outside the
one-plaquette neighborhood of this support.

Let beta_m be the row-sum coefficient for the infinite-lattice
operator formed with h=1 and only 12-plaquettes. Reflections in
coordinates 1 and 2 kill its off-direction row sums; interchange
of 1 and 2 makes those two diagonal sums equal. All other direction
rows vanish. The color block is scalar. Hence its row-sum matrix
is beta_m Pi_12, with Pi_12 the projection on directions 1 and 2.
The complete action row-sum coefficient a_m in L283 is the sum
of the equal contributions of the three orientations containing
any fixed direction. Consequently

\[
 \beta_m=a_m/3\longrightarrow a_*/3=\beta_*.                 \tag{15}
\]

Equivalently, L283(12)–(13)'s single-plaquette constant-field
contraction is c(g_m), giving beta_m=4c(g_m), whereas its full
a_m=12c(g_m). Thus (15) retains the exact Wilson tensor, the
internal three-color sum and the factorial convention; it is not
an isotropy assumption about the source-weighted action.

Let V_a(x,y) be the vector field whose components are R_{a,mu}(x,y),
with zeros in directions 3 and 4, and y on the opposite source
support. Its values and first derivatives on (9) are uniformly
bounded by section 1. For any nonzero row i of A_{h,N,m}, all
edge arguments j in that row and its plaquette centers are within
O(a) of x_i. Replacing h(z_p) by h(x_i) and V_{a,nu}(x_j,y)
by V_{a,nu}(x_i,y) therefore has error O_m(a), uniformly in i,y.
The finite absolute row sums and the smoothness of h justify
this replacement even at the edge of its support. Use (15) on
the resulting constant vector field. Rows outside this support
neighborhood and h(x_i) both vanish. Thus (14) gives

\[
 \limsup_{N\to\infty}\sup_{i,y}
 \left|(A_{h,N}V_a(\cdot,y))_i
       -\beta_*h(x_i)(\Pi_{12}V_a(x_i,y))_{\mu_i}\right|
 \le C_h s_m+C_h'|\beta_m-\beta_*|.                         \tag{16}
\]

The supremum need only include rows in a fixed compact neighborhood
of supp h; all other contributing rows are zero, and for large N
that neighborhood is within (9). The constants on the right can
be chosen independent of m, from the uniform bound on V_a. Sending
m to infinity proves that the supremum error tends to zero. This
order of limits controls every internal anchor before the external
Riemann sums. The proof uses no unsupported bulk replacement and
no scalar boundary condition for the one-form covariance.

### 3. Exact trace normalization and both insertion limits

Since U_h is fully symmetric, its contraction satisfies exactly
mathcal U(U_h;G_barh,G)=Tr(A_{h,N}G_barh). From L280(18),
G_barh=GC_12^* diag(barh) C_12G=R_N diag(barh)R_N^*.
For the scalar color block and with all three external colors,
finite-dimensional trace cyclicity and (7) give

\[
 \begin{split}
 N^{-2}\operatorname{Tr}(A_{h,N}G_{\bar h})
 &=\frac{3a^6}{N^2}\sum_{i,p}\bar h(z_p)
       R_{a,\mu_i}(x_i,z_p)
       (A_{h,N}V_a(\cdot,z_p))_i\\
 &=\frac3{64}a^8\sum_{i,p}\bar h(z_p)
       R_{a,\mu_i}(x_i,z_p)
       (A_{h,N}V_a(\cdot,z_p))_i .                          \tag{17}
 \end{split}
\]

Here a^2N^2=64. The internal color sum is already in A_{h,N};
the factor three in (17) counts only its external color trace.
All i are relative edges and all p are retained 12-plaquettes.
The untruncated trace includes every normal endpoint, even though
the insertion rows active in this limit lie in the interior.

For h=h_- and barh=h_+, section 1 uniformly bounds the kernel
on all active rows and opposite plaquettes. The physical volumes
a^4 times the counts of these rows and plaquettes are bounded.
The uniform error in (16) therefore tends to zero after multiplying
by the other factors and summing in (17). Uniform kernel convergence
then permits replacement of R_a by R. Product Riemann sums on the
shifted edge and plaquette grids converge to the continuum integrals;
all supports lie strictly inside D and all limiting factors there
are smooth. Thus

\[
 \lim N^{-2}\operatorname{Tr}(A_{-,N}G_+)
      =\frac{3\beta_*}{64}\mathcal J_f.                    \tag{18}
\]

For the other insertion reverse the two supports. Time reflection
preserves spatial edge directions 1,2 and 12 orientation. The
scalar time Green function obeys G_Omega(-t,-s)=G_Omega(t,s);
(8) hence gives R_mu(theta x,theta y)=R_mu(x,y).
Changing both variables by reflection identifies the corresponding
integral with exactly mathcal J_f. Alternatively the finite trace
is carried to the other by the relative-grid reflection permutation.
Both orders are retained, with no additional multiplicity within
either trace. Multiplying (18) by 1/4 and using beta_*=a_*/3 gives
a_* mathcal J_f/256 for EACH insertion. This proves (3)–(4).
The uniform-tail and uniform-row estimates prove convergence of
the complete normalized terms, hence their claimed o(N^2) errors.

### 4. Comparison and the unresolved quartic action response

Adding (4) to L283(3) proves (5), with exactly L282's S_f and
complete density normalization. Subtracting these evaluated terms
from L280(20) leaves (6) as an exact finite-mesh identity. In
particular G_- and G_+ there are internally source-differentiated
covariances; neither is the bare G approximated in (14). Section 1
only controls kernels between separated source neighborhoods, and
does not by itself control all plaquette anchors in (6). No error
bound for (6), quartic-only cancellation, complete coefficient
estimate or Yang–Mills solution follows from this insertion result.

### 5. Separate critical audit (2026-10-26)

**Verdict.** The two complete insertion limits (3)–(4) pass, with their
o(N^2) errors and exact source/color normalizations. The audit uses
the unchanged complete-quartic EXPLORE audit assessment and L283's
section 5 audit. This verifies an existing partial result, rather than
adding a new estimate or asserting interacting reflection positivity.

**Kernel, grids and endpoints.** On one component, the physical
operator is (L/a^2)^-1(C_12^*/a)=aGC_12^*. Relative to a^4 counting
measure its point kernel is therefore a^-3 GC_12^*, as in (7).
The target edge component 1 has cosine/vertex-sine/vertex-sine
spatial modes, while its source 12-component has cosine/cosine/sine
modes. In coordinate 2 the adjoint difference of the cosine mode
is +omega times the vertex sine; the minus sign in the A_1 term
of C_12 gives the first line of (8). The A_2 line similarly has
the positive coordinate-1 difference. These are precisely the
adjoints of C_12 A=D_1 A_2-D_2 A_1 on their actual shifted grids.
Zero indices in the cosine coordinate are retained. The difference
identities include the first and last normal midpoint, by the
zero boundary vertex extension. Components 3 and 4 are identically
zero since L is block diagonal and C_12^* has no such rows.

The scalar time recurrence has source 1/a, not 1, giving exactly
L003's kernel with prefactor a/sinh(a gamma). Here
|k|/4<=Omega<=pi|k|/8, Omega/2<=gamma<=Omega and gamma>=1/8.
Bounding the two numerator sinh factors gives
exp[-gamma(s-t)]/[2 gamma(1-exp(-16gamma))], which implies (10).
A time derivative changes one sinh to gamma cosh, giving a bound
at most 2Omega times this exponential majorant. A spatial derivative
costs at most pi|k|/8. Thus the complete first-derivative tails are
summable on both separated neighborhoods (9). This includes source
derivatives, as needed for Riemann sums, and gives uniform fixed-mode
convergence to the stated continuum adjoint kernel. No coincident
square or scalar Dirichlet replacement of a normal component is used.

The existing finite recurrence check was rerun: all 5148 selected
rows, including 1824 normal endpoint rows, pass. Maximum residual
1.0229447497400734e-15 is below 2e-11, with zero failures. Its
summary is in the existing kernel certificate. The analytic mode
identities above, rather than this finite tolerance, justify (7)–(12).

**Weighted operator and limits.** L283's entry bound contracts against
the finite single-plaquette absolute allowance to give (14) both in
operator norm and absolute row sum. For fixed m, every path from a
weighted plaquette is interior for fine mesh, because supp h stays
away from every face. Rows can be nonzero only within one plaquette
of that support. Replacing the weight and a kernel value by their
values at the row position costs O_m(a), including rows at the edge
of supp h, since h is globally smooth and zero outside its support.
Coordinate reflections kill off-direction row sums; interchange of
1 and 2 equates their diagonals. The full a_m is the sum of the
three equal orientation contributions, so beta_m=a_m/3, retaining
the internal three-color contraction. The error limsup in (16)
then tends to zero by sending m to infinity after N. Constants
multiplying s_m and |beta_m-beta_*| use the uniform kernel bound
and are independent of m. No uniform estimate for the fixed-degree
O_m(a) constant is needed in this order of limits.

Finally R_N=a^3 R_a gives 3a^6/N^2=3a^8/64 in the complete
trace (17). All active rows lie in a compact source neighborhood;
their physical counts and the opposite source's physical counts
are bounded. Uniform row and kernel errors therefore vanish in
the double sum. The shifted grids give ordinary product Riemann
integration, with no extra orientation density. The scalar row sum
beta_* gives 3beta_* J_f/64. Multiplying by 1/4 gives
a_* J_f/256 per insertion. The second insertion is its time
reflection: directions 1,2 and the 12-plaquette have positive
reflection signs. There is one trace per insertion and no additional
factor two inside either trace. Adding the two gives (4), and the
finite addition with L283/L282 gives (5). Equation (6) is the exact
remaining quartic term; its all-anchor estimate is not inferred here.

## Mathlib

Full coverage of these relative-box insertion limits, the weighted
Wilson contraction and the separated matrix-kernel approximation:
**not checked**. No matching theorem or Mathlib name/link is claimed.
The inputs are the canonical finite relative-mode identities in
L003, L279's Wilson jets, L280's exact source formula and L283's
internal approximation and finite contraction. The new specialization
keeps the source weights and proves the separated uniform tail and
normalization needed for these two terms; no known full-space
propagator theorem is reproved or used outside its hypotheses.
The reused source assessment is
`drafts/literature/2026-10-26-quartic-response-quadratic-asymptotic.md`.
It does not supply this insertion limit as a quoted known theorem.
Originality beyond that search is not certified. Section 5 records
the separate critical audit, including the audited L283 input.
