# L217 — A finite signed cubic limit for the complete nonradial action response

## Hypotheses

Keep L025 and L213–L216's pinned relative SU(2) cube D=(-4,4)^4,
admitted even meshes a=8/N, straight lower-rooted direction-1 forest,
both actual L010 probes i=3,6 at tau=1/16, and bare expansion before
refinement. Use ordinary stored dimensionless coordinates. Retain all
colors, transverse planes, boundary/end rows, allowed constant modes,
upper jumps, both residual subtractions and complete external heat sums.

Use L214's full covariance Sigma, residual A and mathscr V=Sigma A Sigma.
In L211(10)–(11) write the exact local factorization as

\[
 A=C^T J_N C,\qquad
 aJ_N={1\over2}(C E U C_{\rm cl}
                  +C_{\rm cl}^T U^T E^T C^T)
                   -aW_3-aC_{\rm cl}^T S_6 C_{\rm cl}.
 \tag{1}
\]

Here C is circulation, E is the original endpoint average, C_cl is
the original ordered clover filter, and U contracts the plaquette field
with the actual smooth displacement u. The strain matrices W_3,S_6
are those of the two insertion subtractions. This is the local
definition of A, including both generator orders, not an arbitrary
matrix satisfying A=PAP.

## Conclusion

There are finite real coefficients A_i^dm and A_i^nr such that

\[
 \lim_{a\to0}a^3 T_i^{\rm dm}=A_i^{\rm dm},\qquad
 \lim_{a\to0}a^3 G_i^{\rm nr}
       =A_i^{\rm nr}=P_i+A_i^{\rm dm},\quad i=3,6.
 \tag{2}
\]

T_i^dm is exactly L216(16)'s original direct/direct plus both mixed
row contributions, and P_i is L216's plateau coefficient. No value,
sign or vanishing of these coefficients is established.

Here is a definition of the new coefficient retaining the full ordered
stencils. All infinite arrays below use positive links indexed by their
lower vertices in Z^4, so no Fourier phase convention is implicit.
Freeze only U at the physical point x, obtaining U_x, and set

\[
 J_x={1\over2}(C_\infty E_\infty U_x C_{{\rm cl},\infty}
       +C_{{\rm cl},\infty}^T U_x^T E_\infty^T C_\infty^T).
 \tag{3}
\]

Let g be the Z^4 scalar Green kernel with Fourier multiplier
(sum_(r=1)^4 4 sin^2(theta_r/2))^(-1), and let Sigma_infinity have
this kernel on each of its four diagonal link-component blocks.
Define the entries of W_x by the absolutely convergent sum

\[
 W_x(h,e)=\sum_{p,q}
    (C_\infty\Sigma_\infty)_{p,h}(J_x)_{p,q}
                         (C_\infty\Sigma_\infty)_{q,e}.
 \tag{4}
\]

The notation does not assert that Sigma_infinity is a bounded l2
operator. Only its differentiated columns occur in (4).

For each transverse plane mu<nu use the four signed traversal selectors
d_l of the plaquette anchored at the origin (axial vertex coordinate
zero), and the signed transverse endpoint dipoles eta_l in L216(4).
Thus d_3,d_4 already include their negative traversal signs. Let

\[
 w_l^{[R]}=\sum_{r=-R}^{-1} I_1(\delta_r\otimes\eta_l).
 \tag{5}
\]

These are sums of axial-link selectors at their lower-vertex levels;
the last included axial link has level -1. For local selectors extend
W_x bilinearly, and put

\[
 \begin{split}
 D_{lm}^{\mu\nu}(x)
 &=d_l^T W_xd_m
   -\lim_{R\to\infty}d_l^T W_x w_m^{[R]}
   -\lim_{R\to\infty}(w_l^{[R]})^T W_xd_m,\\
 \mathcal D_{(l,c),(m,d)}^{\mu\nu}(x)
 &=\delta_{cd}D_{lm}^{\mu\nu}(x),\\
 A_i^{\rm dm}
 &=-24\sum_{2\le\mu<\nu\le4}\int_D
       K:\mathcal U_i^{\mu\nu}(x):\mathcal D^{\mu\nu}(x)\,dx.
 \end{split}\tag{6}
\]

Here K is L025's original tensor and mathcal U_i is L216(8)'s full
heat-weighted exterior matrix. Both limits in (6) converge absolutely.
All integrals and heat sums in (2),(6) converge absolutely, although
the integrands and the resulting coefficients are signed. Full
perturbative compensation, finer scales, finite matching, interacting
reflected error <=c_box/2, continuum axioms and infrared finite mass
remain unresolved. This is local reproduction/specialization of the
existing kernel and cumulative-stencil machinery, not a novelty claim.

## Proof

### 1. Establish the fixed-offset differentiated Green limit

Import L200(4)–(5)'s relative component heat/image estimates, with their
one even own-direction reflection, three odd vertex reflections and
full constant-mode spectrum. For a plaquette p and link e in a fixed
bounded cluster whose physical distance from every face is >=delta>0,
they imply

\[
 (C\Sigma)_{p,e}
       -(C_\infty\Sigma_\infty)_{p',e'}\longrightarrow0
 \tag{7}
\]

uniformly over translations of that cluster. Primes denote its
translation to Z^4; the orientations and staggered offsets are unchanged.
We give the convergence justification rather than infer it from a
uniform bound. In the exact component heat image formula the direct
image is the infinite heat kernel. A circulation entry is a bounded
sum of first differences of the matching scalar components. Every
nondirect nearest image for this cluster is at distance >=c_delta N
for large N. Integrating L200(5), with m=1 and b>10, gives

\[
 \int_0^\infty C_b(1+t)^{-5/2}
       (1+L/\sqrt{1+t})^{-b}\,dt\le C_b'(1+L)^{-3}.
 \tag{8}
\]

Indeed split at 1+t=(1+L)^2; below that point use the power b,
and above use the integrable t^(-5/2) tail. Thus the finitely many
nearest nondirect images contribute O_delta(N^-3) on 0<=t<=N^2.
The further images, grouped by their period-2N translates as in
L200's proof, contribute O(N^-3): rescaling t=N^2 s bounds their
integrals by N^-3 times a convergent sum with decay exponent b>10.
For t>=N^2 the full finite differentiated product spectrum has bound
C N^-5 exp(-ct/N^2), so its integral is O(N^-3). The infinite
differentiated heat tail on the same interval is O(N^-3) by (8)'s
zero-distance heat bound. This proves (7), in fact with error
O_delta(N^-3) for the fixed cluster. Both normal end conditions and
the own-direction zero index were included in the finite spectrum;
none was suppressed to obtain convergence.

The same infinite heat estimate gives

\[
 |(C_\infty\Sigma_\infty)_{p,e}|
          \le C(1+\operatorname{dist}(p,e))^{-3}.
 \tag{9}
\]

The Green kernel itself is well defined because its Fourier
singularity |theta|^-2 is integrable in dimension four. Its
differentiated columns have square-summable tails by (9). This is
all that is required of the infinite covariance.

### 2. Control the spatial tail before freezing coefficients

The finite-range matrices aJ_N have uniformly bounded coefficients,
overlap and range by L211(11). For any fixed cluster of p,q about a
physical point x in a compact interior, smoothness of u and the fixed
endpoint/clover stencils imply

\[
 (aJ_N)_{p,q}-(J_x)_{p',q'}\longrightarrow0
 \tag{10}
\]

uniformly over cluster translations. Both occurrences of u in the
adjoint order are evaluated at their original shifted samples before
this limit. Each differs from u(x) by O(a) on the fixed cluster.
The two subtraction matrices in (1) are uniformly bounded, so their
contribution to (10) is O(a); they have not been deleted from the
finite expression. There is no derivative approximation to a rough
field or covariance in (10).

Fix link selectors e,f at a bounded offset from each other. From
L211(12), the exact factorization and bounded stencil overlap, the
part of a mathscr V_(e,f) with internal plaquette anchor outside a
lattice ball of radius L about e is bounded by

\[
 C_B L^{-2}+C N^{-2},\qquad L\ge2B+2r_*+2.
 \tag{11}
\]

Here B bounds the e,f offset and r_* the stencil range. To check
the tail, both decaying differentiated kernels there are bounded by
C_B(1+r)^-3; four-dimensional shells give sum_(r>L) C_B r^3 r^-6
<=C_B L^-2. Each finite-size cross term is at most
N^-3 sum_p C(1+dist(p,e))^-3<=C N^-2, and the constant product
is O(N^4 N^-6)=O(N^-2). These estimates also apply to q shifted
within r_*. The infinite sum (4) has tail C_B L^-2 by (9).

On the remaining fixed finite ball, (7),(10) give convergence of
every term, uniformly on compact physical interiors. Taking N to
infinity before L gives

\[
 a\mathscr V_{e,f}\longrightarrow W_x(e',f').
 \tag{12}
\]

In particular neither the spatial tail nor distant displacement
coefficients are frozen without a uniform error estimate. The full
coefficient levels may differ far away, but (11) removes their
contribution to this normalized local limit.

L211(13)'s convolution argument applied to (9) also gives

\[
 |W_x(h,e)|\le C(1+\operatorname{dist}(h,e))^{-2}
 \tag{13}
\]

uniformly in x. The coefficients of J_x are real and linear in u(x).
Thus (4) is real, symmetric under transposing its link arguments,
and continuous in x, with the same uniform bound.

### 3. Sum the two actual lower half-fibers

Expand the lifted residual rows exactly as in L214(5),(9). For a
signed traversal edge l of a transverse plaquette at axial level j,
the row is d_l-w_l, where w_l is its signed endpoint dipole summed
over axial levels 0,...,j-1. Translating its anchor level j to zero
gives levels -j,...,-1, exactly (5) truncated at R=j. Therefore
the one-color direct/mixed block is

\[
 (V_p^{\rm dm})_{lm}
   =d_l^T\mathscr V d_m-d_l^T\mathscr V w_m
                                 -w_l^T\mathscr V d_m.
 \tag{14}
\]

There is no extra factor 2: both mixed orientations are displayed
separately. The plus two-prefix term is the part treated by L215–L216.
Traversal signs reside in both d_l and w_l; colors remain diagonal.

For either mixed sum remove only source levels of axial distance
greater than R from the local direct edge. L211(5) yields, after
multiplication by a and using aN=8, the uniform tail bound

\[
 a\sum_{\substack{0\le r<j\\j-r>R}}
       |\mathscr V_{d,(r,v)}|
      \le C\sum_{n>R}(1+n)^{-2}+C/N
      \le C'/R+C/N.
 \tag{15}
\]

There are at most two endpoint fibers per prefix; bounded traversal
offsets change only C. Pinned endpoints remove a fiber. This bound
retains even the bottom sources and the upper-adjacent plaquettes.
The infinite half-fiber tail is C/R by (13). On every compact
physical interior j tends to infinity uniformly. For fixed R the
remaining fiber consists of finitely many fixed offsets, so (12)
applies to each. First let a tend to zero, then R to infinity.
Equations (12),(14),(15) prove

\[
 a V_p^{\rm dm}\longrightarrow\mathcal D^{\mu\nu}(x)
 \tag{16}
\]

uniformly on compact physical interiors. This also proves absolute
convergence, boundedness and continuity of the half-fiber expressions
in (6). Neither prefix was approximated by a bounded operator or a
smooth function. No two-prefix fiber estimate has been used, and no
scalar estimate has been transferred to a mixed component of A.

### 4. Sum every plaquette and restore the complete response

L214's direct and mixed estimates give |a V_p^dm|<=C on all variable
transverse plaquettes, including normal end edges. L216(14) and its
full heat majorant give a^-2 U_(i,p) -> mathcal U_i^(mu nu) uniformly
on compact interiors, with |a^-2 U_(i,p)|<=C_i everywhere. The
corresponding limiting matrices have the same uniform bounds. Thus

\[
 a^3 T_i^{\rm dm}
       =-24a^4\sum_{p\in P_T}
                     K:(a^{-2}U_{i,p}):(a V_p^{\rm dm}).
 \tag{17}
\]

On the region of physical distance >=delta from all four pairs of
faces, (16) and the exterior heat limit give the Riemann integral
in (6). The omitted full boundary collar has at most
C(delta a^-4+a^-3) plaquettes, so its absolute contribution to
(17) is <=C_i(delta+a). The limiting integral over that collar is
<=C_i delta. Taking a to zero before delta proves the first limit
in (2), with every plane and end row counted. The argument does not
extend fields through the fixed upper transverse link. In particular
the infinite half-fiber description is used only after restricting
to compact interiors; the actual upper and lower collars were
estimated with their original finite rows.

Finally L216(16) states

\[
 a^3 G_i^{\rm nr}=P_i+a^3T_i^{\rm dm}+o(1).
 \tag{18}
\]

Its error already includes L213's complete discarded pairing/plaquette
classes and L215's scalar plateau comparison. Substitution proves
the second limit in (2). Absolute convergence in (6) follows from
(13), the one-dimensional fiber series, the bounded domain and
L216's complete exterior heat majorant. No value or sign is inferred
from the existence of these limits. In particular no finite matching
coefficient or full residual cancellation follows.

### 5. Coverage, duplication and verification scope

Reuse the unchanged EXPLORE assessment
`drafts/literature/2026-10-16-complete-residual-coefficient-cubic-assembly.md`.
Its covered target is the complete L025 response and permits partial
signed estimates on that target. The primary flow/Ward comparisons
there do not supply this bare forest result; no additional literature
or known general renormalization theorem is being reproved here.
L211 provides the exact local residual, differentiated-kernel bound
and convolution; L200 provides the primary local heat/image estimates
with their boundary hypotheses; L216 provides the complete exterior
heat limit and the other row block. The additional applicability work
is (7)–(16), followed by the bounded collar/Riemann assembly. The
earlier raw-loop, ordered-Wick and upper-pin failures remain intact;
none excludes this normalized, differentiated covariance mechanism.

The checks are analytic: the single factor a in (1),(12), the
four-dimensional product tail, the actual prefix levels ending at -1,
both minus signs in (14), both generator orders and subtractions,
the finite-size C/N fiber tail, and the a^4 Riemann weight in (17).
No mathematical script, preview, finite-mesh numerical sign or IEEE
arithmetic premise is used. Earlier results are imported within their
stated domains, not recursively certified by this proof. A separate
critical audit of this new limit argument remains appropriate.

### 6. Separate critical audit, 2026-10-17

This audit accepts (2) relative to the stated imported inputs. It
checks the new local-limit and summation argument, not every upstream
plateau, flow or residual theorem. No load-bearing error was found.
The following details make the uniform summed error and limit order
explicit; no new coefficient value is inferred.

**Normalization and the exact finite contraction.** L211(10)–(11)
uses the unscaled circulation C and exactly one factor 1/a in K_a.
Multiplication of its J by a gives (1); neither covariance carries
an additional cell weight in these stored coordinates. This agrees
with the physical-to-stored conversion checked in L211's audit.
The two insertion matrices in aJ are O(a) in each fixed stencil,
whereas both displacement-generator orders survive. Their bounded
range/overlap also makes their normalized spatial tails obey the
same estimates as the generator. They are not discarded on the
basis of entrywise convergence alone.

L214(4) identifies the selected forest matrix as R Sigma A Sigma R^T,
with no tilt factor 2. Its row d_l-w_l gives the three terms in
(14) and the plus two-prefix term, exactly once each. L216(4)'s
eta_3 and eta_4 already reverse their endpoint differences, just as
d_3 and d_4 reverse their link selectors. On translating an axial
anchor j to zero, its included link levels 0,...,j-1 become
-j,...,-1. Thus both infinite prefixes in (6) end at -1, not at
zero, including in the transposed mixed placement. No symmetry
argument changes either endpoint or combines the two minus signs
into an additional outside factor.

**Local Green convergence and its boundary domain.** The relevant
input is the m=1 case of L200's relative heat/image proof. For a
fixed cluster at physical distance delta from the faces, all nearest
nondirect images are at lattice distance at least c_delta N. Their
integrated first-difference bounds are O_delta(N^-3). For the further
images it is essential to stop the image integral at t=N^2. With
image distance at least cN(1+|b'|), (5) of L200 bounds each such
integral by

    C_b N^(-b)(1+|b'|)^(-b)
        integral_0^(N^2) (1+t)^((b-5)/2) dt
      <= C_b' N^-3 (1+|b'|)^(-b).

The sum over b' in Z^4 converges for the chosen b>10. Integrating
each image to infinity and then summing its distance^-3 bound
would not be a valid substitute. For t>=N^2 the full finite spectrum
instead gives N^-5 exp(-ct/N^2); integration gives O(N^-3), as does
the infinite heat tail. This verifies (7) uniformly on each fixed
interior cluster, including the allowed own-direction constant mode.
The at-least-three positive transverse mode indices supply the
finite spectral gap; no constant mode has been removed by hand.

For the spatial tail, L211(12) is needed only on the compact internal
plaquette support of J, but is uniform over every covariance source.
It therefore applies to all finite terms of (4)'s comparison, even
when a fiber source approaches a face. For sources at separation at
most B, and L>=2B+2r_*+2, both large-distance factors are O_B(r^-3).
The shell sum is sum_(r>L) O_B(r^-3)=O_B(L^-2), since the dimension
is four. Each finite-size cross term is N^-3 times O(N), and the
constant product is O(N^4 N^-6), hence both are O(N^-2).
This validates (11) and excludes a hidden logarithmic or volume loss.
Finite-stencil convergence may now be used on the remaining ball.
The same argument on Z^4 defines (4) without a bounded infinite
inverse; only differentiated columns are paired.

**Fiber tails and the ordered uniform error.** After the normalization
aN=8, summing L211(5) on a single omitted fiber gives
O(sum_(n>R)(1+n)^-2)+O(N*N^-2)=O(R^-1)+O(N^-1).
There are only two endpoint fibers for each traversal row, not a
three-dimensional source sum. This proves (15) for both orientations;
the finite-size term vanishes even though the prefix length grows.
For fixed R, every retained source has bounded offset B<=R+O(1).
The spatial-tail constant may consequently depend on R. One must
remove the spatial cutoff before the fiber cutoff.

More explicitly, fix a physical collar width delta>0, a fiber cut
R>=1 and a spatial cut L>=2R+O(1). On the interior, apply the
finite-ball convergence to the finitely many retained offsets, then
use the spatial and fiber estimates for both the finite expression
and its limiting expression. L216(14) gives uniform convergence of
the *complete* exterior matrix and a mesh-independent bound for it.
The exact a^4 weight in (17) converts a uniform normalized entry
error into an equally small scaled response error. Taking the mesh
limsup yields, for constants independent of N,L,delta,

    limsup_(N->infinity) |a^3 T_i^dm-A_i^dm|
       <= C_i delta + C_i/R + C_(i,R)/L^2.

Here all finite-size terms and finite-ball convergence errors have
already vanished at fixed delta,R,L. The collar count is
O(delta a^-4+a^-3) with bounded normalized entries, so its finite
contribution is O(delta+a) and its limiting contribution O(delta).
Constants in finite-ball convergence may depend on delta; no rate
uniform as delta tends to zero is required. Send L to infinity,
then R to infinity, then delta to zero. This proves precisely the
required uniformly summed o(N^3) error. Choosing growing cutoffs
inside a fixed-cutoff convergence theorem is unnecessary.

**Complete heat sum, colors and assembly.** L216's full two-mode
polynomial-times-Gaussian majorant applies to the original transverse
exterior rows, including normal end edges. It controls heat tails
uniformly before any local limit; smooth upper continuation is never
used. Its U/a^2 normalization, together with aV, gives
a^4*(a^-2)*(a)=a^3 in (17), so there is no missing 8 or cell factor.
Each of the three positive transverse planes is counted once, the
color-diagonal matrices retain all three colors, and the -24 comes
from L025's original no-internal-pair class. Its 48-pair class was
removed only by L213's complete comparison, not by this local limit.

L215 changes only the plus two-prefix term with O(a^-5/2) total
error; L213's excluded plaquette/pairing classes have the same total
error bound. Both errors become O(sqrt(a)). L216's signed plateau
limit then gives (18) with its stated o(1), and the audited direct/
mixed limit proves (2). The plateau theorem and its upstream scalar
energy inputs remain imported, not recursively audited here. This
audit establishes the complete action limit as a usable local input
for later assembly. It does not evaluate P_i or A_i^dm, certify
compensation, provide a finer remainder rate, or improve the
interacting reflected bound. No numerical or IEEE premise was needed;
the Mathlib qualifications below are unchanged.

## Mathlib

Full matching specialized forest response limit: **not checked**.
Supporting lattice heat/image estimates, finite-stencil convergence,
convolution and dominated/Riemann limit coverage: **not checked**.
Unknown coverage does not imply absence. The needed boundary and
summability specializations are written above; no matching Mathlib
theorem or certified originality is asserted.
