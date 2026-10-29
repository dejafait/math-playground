# L179 — An exact joint finite-data witness at the sharp endpoint

## Hypotheses

This is the existential finite-data test approved in
`drafts/literature/2026-10-28-sharp-endpoint-joint-bracket-compatibility.md`.
Its necessary identities come from the conditional family of identical
marked K3 factors with the original common metric, triple, forms and
connection, and a hypothetical locally free product-polystable rank-two
F with integral c_1=0 and full character
2-14e_1-21e_2-tau_D+62e_1e_2. The construction below does **not** assert
that such an F, its global normal bundle, or its actual evaluations exist.
Hatted maps below are a simultaneous model for the specified necessary
finite data, not identifications with those unknown geometric maps.

Retain the prescribed complex intersection space (L,q), with
L=H^(1,1)(S) of dimension twenty, the isomorphism phi from the first
Atiyah domain to L, and the q-self-adjoint semisimple correspondence D.
Its eigenvalues on L are d,2mu,2nu,4, with multiplicities 5,7,7,1,
as in L174. Here d=2lambda, lambda is the root in (1,5/4) of
x^3+x^2-2x-1, and mu,nu are the other two roots. The labelled line
vector is L177's k, with Dk=4k and q(k,k)=-14. Eigenspaces are
q-orthogonal and nondegenerate. Set ell(u)=q(phi(u),k).

Use exactly L168–L178's trace conventions. Write

\[
 p=2\pi i,\qquad \delta=\delta_B\ne0,\qquad
 \gamma=\delta/p^2,\qquad s=781,\quad t=46,
\]
\[
 \Delta=d^2-16+14s,\qquad
 r_0=(16-d^2)/14,\qquad
 \varepsilon=r_0/s,\qquad
 \alpha^2=1-\varepsilon=\Delta/(14s).                 \tag{1}
\]

Choose either square root alpha once. Since 2<d<5/2,
39/56<r_0<6/7, so Delta and alpha are nonzero. The scalar gamma
is not L168's sheaf isomorphism also called gamma. All forms are
complex bilinear. No positivity or independent point normalization
is added.

The retained constraints are the assessment's five-part checklist:
the 781 labelled point lines and their fixed quotient form/vector;
the entire 26+26 split space at every point with both pairings, weight
action and KS/ordinary-image identities; one common 46-dimensional
section space with compatible normal evaluations and alternating
pullback; the unhalved polarized section bracket in the fixed point
coordinates; and the full twenty-dimensional Atiyah domain, normal
Gram form in dimension fifteen, point projection, full residual
equation and cyclicity. No assumption is made that a Gram radical's
image vanishes, or that arbitrary sections are integrable.

## Conclusion

There is an exact simultaneous model satisfying **all** these retained
finite-data constraints at s=781,t=46. Its section brackets are fixed
homogeneous quadratics. In particular neither independent quadrics nor
point-dependent trace rescalings are used.

For h=(x_1,y_1,...,x_23,y_23) in H=C^46, put

\[
 \mathsf X=\sum x_i^2,\qquad
 \mathsf T=\sum x_i y_i,\qquad
 \mathsf Y=\sum y_i^2.
\]

If q_j(h) is its normalized section quadric at the j-th point, then

\[
 \sum_{j=0}^{780}q_j(h)=2s\alpha\mathsf T(h),\qquad
 \sum_{j=0}^{780}q_j(h)^2=4s\mathsf T(h)^2,             \tag{2}
\]
\[
 \Delta\sum_jq_j(h)^2=14\left(\sum_jq_j(h)\right)^2.  \tag{3}
\]

Equation (3), with the exact scalar in (1), supplies both the full
k-line Atiyah equation and cyclicity through the explicitly constructed
normal bracket below. The **original** point quartic is the nonzero
polynomial (4s delta/d) mathsf T^2, so in this model it has exact
complex square length one. This is not a computation of the actual
family's quartic or its minimum square length.

The original construction is an informative NEGATIVE / POTENTIALLY_NEW
result for exclusion using just the retained identities. The separate
step 604 conceptual audit below preserves it (EXPLORATION / REPRODUCTION),
with no substantive correction or stronger conclusion. It parks that
exclusion mechanism at this endpoint. It does not improve the conditional bounds s<=781,t<=46,
exclude or construct F, or give a Hodge-conjecture candidate. The
classification records the prior bounded search, not certified
originality or a general theorem beyond the sources checked.

## Proof

**Sources, applicability and the verification being supplied.** The
invocation-start assessment has DECISION EXPLORE for this exact test.
Reuse L164's actual polarized split cup formula and L168/L169/L178's
fixed point coordinates and residue/trace comparison. Their general
moment-map comparison is Arbarello–Sacca, *Singularities of moduli
spaces of sheaves on K3 surfaces and Nakajima quiver varieties*,
Adv. Math. 329 (2018), 649–703, Proposition 6.1 and proof, pp.680–681,
with (5.5), pp.674–675
([primary PDF](https://www.math.columbia.edu/~giulia/Quiver.pdf#page=32)).
No algebraic-polarization chart is imported at the fixed real class,
and no simultaneous-realization theorem is attributed to that result.

L173 and L177 already specialize the commutator-annihilation theorem
of Buchweitz–Flenner, *A Semiregularity Map for Modules and Applications
to Deformations*, Compositio Math. 137 (2003), 135–210,
math/9912245v1, Definition 4.1, Proposition 3.12 and Corollary 4.8,
printed pp.28,24,32
([primary PDF](https://arxiv.org/pdf/math/9912245v1#page=32)).
Local freeness makes F perfect in that conditional application.
Their resulting identities, not a new semiregularity assertion, are
the equations tested here. Orthogonal decomposition for a nondegenerate
restriction is covered by Elman–Karpenko–Merkurjev, *The Algebraic and
Geometric Theory of Quadratic Forms*, AMS Colloquium Publications 56
(2008), I.1.A, Proposition 1.6 and Corollary 1.9, pp.14–15
([primary text](https://www.math.ucla.edu/~rse/book/Kniga.pdf#page=24)).
All spaces here are finite-dimensional over C; each restriction used
as nondegenerate is checked below or is the retained L178 certificate.

These results do not furnish the joint witness. The work below is an
explicit construction and verification. The short geometric-series
calculation is included to certify its exact exponent range; it is not
a reproof of a moment-map classification or a generic SOS theorem.
No numerical fit, closure membership or genericity argument is used.

**The common alternating section pairing is nondegenerate.** This is
not an extra rank hypothesis. Under the conditional geometric inputs,
L116 gives N=O_B^46 direct sum A with H^0(A)=0, and L108 gives
the perfect alternating form b_N:N -> N^vee. Consequently
h^0(N^vee)=h^0(N)=46. Applying H^0 to the dual direct sum gives
h^0(A^vee)=0 as well. The component O_B^46 -> A^vee of b_N is
therefore zero; alternation makes its transpose component zero.
Since b_N is invertible, its restriction to O_B^46 is invertible.
Its entries are constants because H^0(B,O_B)=C. The induced form
on H is thus one nondegenerate alternating form of rank 46, common
to every point evaluation. L108's tangent/normal orthogonality and
L171's actual tangent comparison identify the corresponding fibre
forms. Choosing symplectic coordinates on this abstract H is permitted;
it does not prescribe any actual evaluation matrix.

**What the endpoint equations require, including the radical.** Let
g denote the actual normal residual map for this paragraph only.
L116 gives dim K_N=704-781+92=15, and L178 gives rank(g^*S_N)=15.
Thus g is surjective. If x is in the radical of its pulled-back form,
then S_N(gx,gu)=0 for every u, so surjectivity and nondegeneracy give
gx=0. Conversely a kernel vector is radical. L174/L178 identify this
radical with phi^(-1)(L_d). Thus its five directions have zero normal
image at this endpoint as a consequence, not a presumption. L175's
point projection also kills them since ell is zero there.

Put g_k=g(phi^(-1)k). L177's fourteen-dimensional nondegenerate
image J and L178's nondegenerate k-line exhaust K_N orthogonally.
The full Gram identity gives, for every domain u,

\[
 S_N(g_k,g(u))=\frac{\gamma\Delta}{d}\ell(u),\qquad
 S_N(g_k,g_k)=-\frac{14\gamma\Delta}{d}.               \tag{4}
\]

Indeed the first term in L176's Gram form at (k,phi(u)) is
gamma(d-16/d)ell(u), and its subtracted point term is
-(gamma s/d)(-14)ell(u). Their sum is (4).

Write n_j=ell_j^(-1)(1) in the fixed point line. By L168/L169/L178,

\[
 Q_U(n_j,n_l)=\frac{\delta}{d}\delta_{jl},\qquad
 w_k=p^{-2}\sum_j n_j.                               \tag{5}
\]

For beta(h)=sum q_j(h)n_j and C(h)=sum q_j(h), equations (5) imply
Q_U(beta,w_k)=gamma C/d and Q_U(w_k,w_k)=gamma s/(dp^2).
L177's full equation, tested against J and g_k, therefore determines

\[
 v(h)=\frac{pC(h)}{\Delta}g_k.                        \tag{6}
\]

Conversely (4) shows (6) satisfies that equation for **every** domain
vector, including the k-line and the five radical directions. Its norm is

\[
 S_N(v(h),v(h))=-\frac{14\delta}{d\Delta}C(h)^2.
\]

Hence L173's cyclicity is precisely (3). No point polynomial has
been subtracted or replaced. This reduction motivates the construction;
the full model, including all Gram blocks, is specified below.

**Compatible evaluations producing the quadrics.** Fix a primitive
781st root zeta, label points j=0,...,780, and write z_j=zeta^j.
Define constants

\[
 a_j=\alpha+z_j+\frac{\varepsilon}{2}z_j^{-1},\qquad
 b_j=z_j^4,\qquad c_j=(1-a_j^2)z_j^{-4}.
                                                               \tag{7}
\]

Thus b_j is never zero and a_j^2+b_jc_j=1. On each coordinate
pair of H use the fixed linear evaluation matrix

\[
 T_j=\begin{pmatrix}(a_j+1)/b_j&1\\
                    (a_j-1)/2&b_j/2\end{pmatrix}.
                                                               \tag{8}
\]

For Omega_0=[[0,1],[-1,0]] and B_0=[[0,1],[1,0]], direct multiplication
gives

\[
 \det T_j=1,\qquad T_j^t\Omega_0T_j=\Omega_0,\qquad
 T_j^tB_0T_j=\begin{pmatrix}-c_j&a_j\\a_j&b_j\end{pmatrix}.
                                                               \tag{9}
\]

The last matrix has determinant -1. Apply (8) to all 23 pairs and
include the result into 24 split pairs of a normal 48-space, with zero
coordinates on the last pair. This defines injective evaluations of
the **same** H, with common alternating pullback Omega_H=sum Omega_0
of rank 46. Their symmetric restrictions have rank 46, and their
diagonal quadrics are

\[
                  q_j=-c_j\mathsf X+2a_j\mathsf T+b_j\mathsf Y.
                                                               \tag{10}
\]

The quadrics are obtained from the evaluations and pairings, rather
than being freely specified and asserted to be realizable afterwards.
The factor 2 in (10) is retained from L164's unhalved commutator.

**Exact root sums and all quartic coefficients.** Consider the Laurent
polynomials a(z),b(z),c(z) defined by (7), using epsilon=1-alpha^2.
For any integer m with 0<|m|<781,

\[
 \sum_{j=0}^{780}z_j^m=0.
\]

Indeed zeta^m is not 1, and multiplying this sum by 1-zeta^m gives
1-zeta^(781m)=0. For m=0 the sum is s. All exponents in
a,b,c,a^2,b^2,c^2,ab,ac,bc lie in [-12,8], so only their constant
coefficients contribute. Those coefficients are

\[
 [a]_0=\alpha,\quad [b]_0=[c]_0=0,\quad [a^2]_0=1,
 \quad [b^2]_0=[c^2]_0=[ab]_0=[ac]_0=[bc]_0=0.          \tag{11}
\]

For completeness, [a^2]_0=alpha^2+epsilon=1.
The support of c=(1-a^2)z^(-4) is contained in {-6,-5,-3,-2};
that of ac is strictly negative, those of b^2 and ab are strictly
positive, and that of c^2 is strictly negative. Finally bc=1-a^2
has zero constant coefficient. This proves every value in (11).

The coefficient vector of (10) in (mathsf X,mathsf T,mathsf Y) is
(-c_j,2a_j,b_j). Equations (11) give its total first moment
(0,2s alpha,0) and its total symmetric second-moment matrix
diag(0,4s,0), with all six independent entries specified. Thus
(2) holds as a polynomial identity in all 46 section variables,
and Delta=14s alpha^2 proves (3). In fact the coefficient-tensor
identity is stronger than the required diagonal quartic identity,
so its full polarization also holds. No sampled section values enter.

**The full split fibres, KS plane and ordinary image.** At each point
take E_j=C^26_+ direct sum C^26_-, with basis e_i^+,e_i^-, perfect
cross-pairing P(x,y)=sum x_i y_i and

\[
 \Omega((x,y),(x',y'))=P(x,y')-P(x',y),\qquad
 B((x,y),(x',y'))=P(x,y')+P(x',y).
\]

Let A_j act by +2 and -2 on the labelled summands, so
Omega(A_j xi,eta)=2B(xi,eta). Let N_j be the first 24 pairs,
and use (8) on its first 23 pairs for rho_j. On the last two pairs
of E_j set

\[
 k_1=e_{25}^++e_{26}^-,\qquad
 k_2=\frac d2(e_{25}^--e_{26}^+),\qquad K_j=\langle k_1,k_2\rangle.
                                                               \tag{12}
\]

Choose tangent coordinates with sigma_B(u_1,u_2)=1 and define
the model KS map by u_i -> k_i. Then

\[
 B|_{K_j}=0,\quad \Omega(k_1,k_2)=d,\quad
 \Omega(K_j,A_jK_j)=0,\quad
 \Omega(A_jk_1,A_jk_2)=-4d.                            \tag{13}
\]

In the ordered four-coordinate basis (e_25^+,e_26^+,e_25^-,e_26^-),
the determinant of (k_1,k_2,A_jk_1,A_jk_2) is +4d^2, hence nonzero.
It follows that

\[
 E_j=N_j\mathbin{\perp_\Omega}(K_j\oplus A_jK_j),\quad
 Q_j=(A_jK_j)^{\perp_\Omega}=N_j\oplus K_j=K_j^{\perp_B}.
                                                               \tag{14}
\]

Since B is nondegenerate on N_j and zero on K_j, its radical on
Q_j is exactly K_j, and its rank there is 48. The ordinary fibre
is the full 50-space Q_j with tangent/normal splitting K_j direct
sum N_j. Its extended alternating form has tangent restriction
d sigma_B, nondegenerate normal restriction, and zero cross term.
The evaluation image lies in N_j and avoids K_j. Equations (12)–(14)
give precisely the L108/L111/L170/L171/L172 finite-fibre identities.
Neither extra derived middle direction is removed from E_j.

One can also retain the actual-type minimal local-complex data, rather
than just the dimensions. Over R=C[[u,v]], put V_0=-u A_jk_1-v A_jk_2
and take the three-term complex in degrees 0,1,2

\[
 R\xrightarrow{\ 1\mapsto V_0\ }R^{52}
   \xrightarrow{\ w\mapsto-\Omega(V_0,w)/2\ }R.       \tag{15}
\]

The composition is zero by alternation. Pair the endpoint generators
by 2 and the middle term by Omega; this satisfies L111's pairing
chain equation. The incoming plane has pairing -4d, so its summand
is a two-parameter Koszul complex, while Q_j tensor R is the free
middle summand. Its ordinary middle fibre is Q_j, its ordinary top
is R/(u,v), and its derived middle fibre is all E_j. Its linear
incoming coefficients are exactly -A_jk_i. This is a formal local
complex only, not a claimed realization as Rp_*End_0(F).

**Fixed top coordinates and residue weights.** For each point let n_j
generate W(j), let H^2(V_j) have generator h_j chi_sigma with
integral sigma_1 chi_sigma=1 and h_j=diag(1,-1), and set

\[
 \widehat\theta_j(n_j)=p^2h_j\chi_\sigma,\qquad
 \widehat\ell_j(n_j)=1,
 \qquad \widehat w_k=p^{-2}\sum_jn_j.                 \tag{16}
\]

This is exactly L168's coordinate: the expression
p^(-2) Tr(h_j theta_j(n_j))/2 integrates to 1, since Tr(h_j^2)=2.
The split cup pairing with normalized cross form P gives the unhalved
bracket p^2 B(xi,eta)h_j chi_sigma. Thus defining
beta_hat(u,v)=sum B(rho_j u,rho_j v)n_j gives L164 (3),(5), with
beta_hat(h,h)=sum q_j(h)n_j. No scalar was inserted separately at
any point.

For (15), its endpoint scalar is 2, its incoming pairing is -4d,
and the fixed relative normalization has kappa=1. L168 (10) and
L169 (10) give, in parameters with sigma_B=du wedge dv at the point,

\[
 \mu_j=\frac{4}{-4d}(-\delta)=\delta/d.                \tag{17}
\]

This retains the oriented local duality functional and supplies (5)
with the same delta at every point. With another tangent frame its
nonzero sigma_B coefficient cancels exactly as in L169. L178's global
bridge gamma=delta/p^2 is retained, so (16) also gives its prescribed
norm gamma s/(dp^2), and p^2 Q_U(w_k,w_k)=gamma s/d. The sheaf-duality
map is determined by this local pairing; it is not identified with
the scalar gamma. No unrelated diagonal quotient form is chosen.

**The entire global finite-data model.** Keep the given q,D,phi,k,
and put

\[
 V_{15}=L_{2\mu}\oplus L_{2\nu}\oplus\mathbb C k,
 \qquad \widehat K_N=V_{15},
\]
\[
 \widehat S_N(x,y)=\gamma q((d-D^2/d)x,y)
                   -\frac{\gamma s}{d}q(x,k)q(y,k),\qquad
 \widehat g(u)=\operatorname{pr}_{V_{15}}\phi(u).       \tag{18}
\]

The other summand is L_d, of dimension five. On the two seven-spaces
the coefficients are gamma(d-(2mu)^2/d) and gamma(d-(2nu)^2/d),
both nonzero by the retained root intervals in L174. On the k-line
the form is (gamma Delta/d)q, nonzero by (1). Thus (18) is
nondegenerate, of dimension fifteen, and reproduces L176 (3) with
L178's evaluated coefficient. The five domain directions are explicitly
retained and mapped to zero; the endpoint argument preceding (4) shows
why this is consistent with, and forced by, these necessary identities.

Set K_T=L, give it form gamma d q, and define

\[
 \widehat E=K_T\mathbin{\perp}\widehat K_N\mathbin{\perp}U,
 \qquad \widehat Q=\gamma d q\mathbin{\perp}\widehat S_N
                                  \mathbin{\perp}Q_U.             \tag{19}
\]

Its dimension is 20+15+781=816=724+2t. Define the inclusion i_hat
of K_T direct sum K_N, its retraction R_hat, the projection A_hat
to U and its orthogonal lift T_hat by these direct summands. Hence
R_hat i_hat=1, ker A_hat=im i_hat and T_hat=(A_hat|ker R_hat)^(-1).
These are the cohomological identities of L116/L176, not a claimed
global derived splitting of a constructed sheaf. On the whole
twenty-dimensional first-factor domain define

\[
 \widehat{\mathfrak a}_2(u)=(\phi(u),0,0),\qquad
 \widehat f(u)=(0,\widehat g(u),-p\ell(u)\widehat w_k),
\]
\[
 \widehat{\mathfrak a}_1(u)=\widehat f(u)
                          -\widehat{\mathfrak a}_2
                             (\phi^{-1}(D\phi(u)/d)).              \tag{20}
\]

The point block of f has Gram (gamma s/d)ell tensor ell by (5).
Adding this to (18) gives exactly
gamma q((d-D^2/d)phi(u),phi(v)). Adding the tangent correction in
(20) yields gamma d q for the first diagonal block, while the
cross block is -gamma q(Dphi(u),phi(v)); the second diagonal block
is gamma d q. Thus all four ordered blocks of L174 (3), its
orthogonal residual map and L175's point projection hold, with the
specified phi and k. Nondegeneracy of all ambient restrictions is
explicit; no rank of a pulled-back form is confused with a map rank.

Let C(h)=sum q_j(h) and define

\[
 \widehat v(h)=\frac{pC(h)}{\Delta}\widehat g(\phi^{-1}k),\qquad
 \widehat b(h,h)=(0,\widehat v(h),\widehat\beta(h,h)).   \tag{21}
\]

Polarize both components to define b_hat(u,v), using the symmetric
bilinear form in (16) and the same linear expression for v_hat(u,v).
In particular this is the unhalved bracket convention, not a later
halving of its diagonal values. Equation (4), now verified directly
from (18), gives for every u and h

\[
 \widehat S_N(\widehat v(h),\widehat g(u))
   =\frac{p\gamma}{d}C(h)\ell(u)
   =p\ell(u)Q_U(\widehat\beta(h,h),\widehat w_k).       \tag{22}
\]

Together with (20) this proves orthogonality of b_hat to both full
Atiyah maps, for diagonal and polarized brackets. The normal bracket
has no tangent component. Finally (3) and (6) prove

\[
 \widehat Q(\widehat b(h,h),\widehat b(h,h))
 =\frac{\delta}{d}\sum_jq_j(h)^2
   -\frac{14\delta}{d\Delta}C(h)^2=0.                 \tag{23}
\]

This is L173's cyclicity for the same bracket, with no sign or point
norm omitted. Equations (11) in fact make the whole coefficient
pairing of the total bracket zero, so all polarizations of (23)
hold. The map is nevertheless nonzero: mathsf T is a nonzero
polynomial and the original point quartic in (2) is nonzero.

**Verification certificate, qualification and stopping decision.** The
exact standard-library calculation is
`scripts/joint_endpoint/check_witness.py`; reproduce it from this
notebook with `python3 scripts/joint_endpoint/check_witness.py`.
Its full output certificate is
`scripts/joint_endpoint/L179-exact-certificate.json`. All 21 checks
pass: the two pairing pullbacks and determinants, all first/second
Laurent moments, absence of nonzero multiples of 781 in the complete
support [-12,8], the complete three-by-three quartic coefficient
tensor, and all KS pairings. The full relevant test entries and
moment matrices were inspected, not just a preview or PASS label.
The normal Gram ranks, all-domain equations and nonzero constants
are justified analytically above; the script does not certify geometry.

The first run's expected sign for the ordered KS determinant was wrong.
Its complete failure certificate remains at
`scripts/joint_endpoint/L179-first-run-certificate.json`. Direct
inspection gives +4d^2, not -4d^2; the nondegeneracy conclusion is
unchanged. The expected sign was corrected and the exact checks rerun.
SymPy was unavailable, so the certificate uses rational sparse Laurent
arithmetic without installing dependencies or approximating roots.

This model retains every item of the approved finite checklist,
including the common symplectic section form, local minimal-complex
directions, fixed point-coordinate functional, full domain and original
quartic. Omitted, exactly as allowed by that test, are a global N or F
realizing these data, holomorphic variation and actual connection or
curvature compatibility beyond the imported identities, the full global
derived multiplication and higher deformation operations, compatibility
of the metric with the Leray maps, and section integrability. A model
for the local complex does not fill any of those omissions.

Therefore these retained finite identities alone cannot exclude the
endpoint. Reopening an exclusion requires a materially additional
geometric identity, rather than another unrestricted scalar lift or a
generic square count. The separate critical audit below checks this
precise construction and its stated boundary. There is no claim that
the actual section quadric equals (10), or that any actual F realizes
its rank-one quartic. Uniform primitive cycle realization remains open.

**Separate conceptual audit (2026-10-28, step 604).** Use the unchanged,
invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-28-joint-endpoint-witness-critical-audit.md`.
This is a RESEARCH / proof_audit / REPRODUCTION check of the existing
construction, not a new construction or a source-readiness decision.
The five retained conditions are those of the original joint-feasibility
assessment. The comparison below uses L108/L111/L116, L164, L168–L178
with their actual hypotheses, rather than inferring fidelity from a
certificate's PASS count. The imported general results and applicability
are as cited above; the ready audit assessment additionally covers the
local free-complex, Koszul and oriented residue comparisons already
specialized in L111/L168/L169. No additional theorem is assumed here.

1. **One section space and both fibre forms.** The proof of full rank
   of the alternating section form is valid. In N=O_B^46 direct sum A,
   h^0(A)=0, self-duality of N gives h^0(N^vee)=46, and dualizing the
   direct sum gives h^0(A^vee)=0. Thus the matrix of b_N has zero
   off-diagonal blocks; its O_B^46 block is a constant invertible
   alternating matrix. This does not require the chosen trivial
   summand to be assumed orthogonal in advance. Each T_j in (8) has
   determinant ((a_j+1)-(a_j-1))/2=1. Its symmetric pullback has
   first diagonal entry (a_j^2-1)/b_j=-c_j, off-diagonal entry a_j,
   and last diagonal entry b_j. Twenty-three copies therefore give
   injective rank-46 maps with exactly the same alternating pullback,
   not merely the same rank. The remaining normal pair is retained.
   The two 26-dimensional weight spaces, A=diag(2,-2), and
   Omega(A xi,eta)=2B(xi,eta) have the precise L164/L170 conventions.

2. **KS plane, ordinary image and local complex.** In the last four
   coordinates, direct computation gives B(k_i,k_l)=0,
   Omega(k_1,k_2)=d, Omega(K,AK)=0, and
   Omega(Ak_1,Ak_2)=-4d. The displayed ordered determinant is
   +4d^2, so K and AK really are complementary nondegenerate
   alternating planes. Consequently Q=(AK)^perp_Omega=N direct
   sum K=K^perp_B; B|Q has radical exactly K and rank 48.
   Its Omega-normal to K is the specified 48-space N, containing
   all section images. Thus the tangent inclusion and section-image
   intersection are those modeled from L171/L172, with neither
   extra derived direction removed.

   For the local complex, set a_0=-Ak_1, b_0=-Ak_2. Its incoming
   vector is u a_0+v b_0, its endpoint scalar is s_0=2, and
   c_0=Omega(a_0,b_0)=-4d. In the ordered basis a_0,b_0 the
   outgoing row is (-2dv,2du), that is (c_0/2)(v,-u).
   The chain-pairing equation is exactly
   Omega(u a_0+v b_0,w)+2d^1(w)=0. It holds also with the
   factors reversed by graded symmetry. Since u,v are regular
   parameters in C[[u,v]], the kernel of this row is R(u,v),
   equal to the incoming image; the cokernel is R/(u,v).
   The orthogonal free 50-summand has zero differentials. This
   verifies the ordinary module and top term, while reduction of
   the entire minimal complex has zero differentials and middle
   dimension 52. Inclusion of that free 50-summand is a representative
   of truncation and reduces to the stipulated ordinary-to-derived
   injection. This is only a formal local complex, as stated.

3. **Fixed coordinates and the scalar bridge.** The degree-zero
   generator is h=diag(1,-1), and the degree-two generator n has
   theta(n)=p^2 h chi_sigma. Their normalized endpoint trace is
   p^(-2) integral sigma_1 Tr(h p^2 h chi_sigma)=2, agreeing
   with the preceding local complex. The fixed functional ell(n)
   is 1. For the split cross pairing, the graded unhalved bracket
   has top value p^2 B(xi,eta)h chi_sigma, so its coefficient in
   n is B(xi,eta); there is no extra half in the diagonal quadric.

   The local orientation is load-bearing: L168's specified Ext
   generator has trace -delta in these parameters, by L169. Hence
   (4/c_0)(-delta)=delta/d. This verifies (17) using the same
   complex and generator, rather than assigning a diagonal form
   independently. The reference relative normalization has kappa=1
   by L178. Keeping gamma=delta/p^2 and w_k=p^(-2) sum n_j gives
   Q_U(beta,w_k)=gamma C/d and
   Q_U(w_k,w_k)=gamma s/(d p^2). In particular the point part of
   f=-p ell w_k has Gram +(gamma s/d) ell tensor ell: the two
   minus signs multiply, and p^2 has not been replaced by |p|^2.
   This matches L175/L176/L178 with one global trace scalar.

4. **All twenty domain directions and all Gram blocks.** At the
   endpoint dim K_N=15 and rank(g^*S_N)=15, so rank(g)=15 and
   g is onto K_N. If x is in the radical of g^*S_N, then gx
   pairs to zero with every vector of K_N and is zero. This
   proves, rather than assumes, that the five-dimensional L_d
   block is killed. Its point component is zero since k is
   q-orthogonal to L_d. For each of the two seven-spaces the
   coefficient gamma(d-(2mu)^2/d) or gamma(d-(2nu)^2/d) is
   nonzero by the retained disjoint root intervals. On the
   k-line the coefficient is gamma Delta/d, also nonzero.
   Thus (18) is nondegenerate on exactly the proposed 15-space.

   For x=phi(u), y=phi(v), adding the point Gram block to
   S_N(g(u),g(v)) cancels its subtracted rank-one term and gives
   gamma q((d-D^2/d)x,y). The tangent correction in a_1 has
   norm gamma q(D^2 x,y)/d, using q-self-adjointness of D.
   Their sum is gamma d q(x,y). Its pairing with a_2 is
   -gamma q(Dx,y), while the second diagonal block is gamma d q.
   These calculations hold on the entire domain and verify the
   four ordered blocks, the residual map and the projection in
   (20). The direct-sum inclusion/retraction are adjoint for the
   stated form, and ker R is exactly the nondegenerate point
   summand. Dimensions are 20+15+781=816=724+2t, as required.

   Finally S_N(g_k,g(u))=(gamma Delta/d)ell(u) and
   S_N(g_k,g_k)=-14 gamma Delta/d. Thus v=(pC/Delta)g_k
   satisfies the full residual equation for every u, including
   the fourteen point-free and five radical directions. Its norm
   is -14 delta C^2/(d Delta). The signs and factors agree with
   (22) and with cyclicity (23); no separate restriction to the
   k-line or to selected section values is being substituted.

5. **Exact coefficients, polarization and scope of the certificate.**
   The sparse arithmetic script was read and rerun; all 21 tests
   pass. Complete selected JSON values were inspected using the
   scoped inspector: all Laurent polynomials, the evaluation and
   restricted matrices, both moments, the KS matrix/determinant,
   and all test residuals. The actual support is contained in
   [-12,8], strictly inside the required |m|<781 bound away from
   zero. The first moment is (0,1562 alpha,0), and the second
   moment is diag(0,3124,0); all nine residual tensor entries
   vanish. These are exact polynomials, not numerical root samples.
   The relation Delta=14s alpha^2 and nonzero root/trace constants
   are analytical inputs, not extra checks silently attributed
   to the script. The complete first-run failed test has residual
   8d^2 when testing the old expected determinant -4d^2; the
   retained actual determinant +4d^2 explains that failure fully.

   To check the stronger polarization assertion, let
   r=(mathsf X,mathsf T,mathsf Y), let l_j=(-c_j,2a_j,b_j), and
   let m=sum l_j. The total bracket is linear in r. The Gram
   matrix of its three coefficient vectors is exactly

       (delta/d) [sum_j l_j l_j^t - (14/Delta) m m^t] = 0.

   This follows from the checked entire second-moment matrix and
   m=(0,2s alpha,0), not just a diagonal quartic identity.
   Polarization of X,T,Y therefore gives
   Q(b(h_1,h_2),b(h_3,h_4))=0 for every four section inputs
   in this particular model. The polarized residual equations
   follow from their linear coefficient identities as well.
   This stronger property is a property of the constructed witness;
   it is not asserted for every actual bracket satisfying cyclicity.
   The original point quartic is (3124 delta/d)mathsf T^2,
   nonzero since d,delta are nonzero and mathsf T is nonzero.
   Over C its exact square length is one, as claimed.

No failed identity or omitted member of the approved five-part finite
checklist was found. This verification is EXPLORATION, not another
ADVANCE or informative NEGATIVE: it preserves the original stopping
evidence without improving its mathematical conclusion. It does not
check existence of global N or F, global variation/connection or
curvature identities beyond the checklist, full derived multiplication
and higher operations, metric/Leray compatibility, or section
integrability. In particular the last displayed coefficient-isotropy
identity cannot be promoted from the model to unknown geometric data.
Exclusion by the retained checklist alone remains parked. No new node
or mathematical dependency is introduced by this audit.

## Mathlib

Full matching coverage for this joint construction was not checked.
No Mathlib absence claim or Lean verification is made. General finite
dimensional linear algebra and finite geometric sums would be supporting
inputs only; they would not by themselves verify the evaluation maps,
trace bridge, whole-domain equations or the boundary of this formal
model's geometric conclusions.
