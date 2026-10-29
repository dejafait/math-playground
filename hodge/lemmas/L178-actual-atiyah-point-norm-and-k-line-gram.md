# L178 — The prescribed Atiyah point norm and the surviving k-line

## Hypotheses

Retain the full conditional family and fixed choices of L168, L169 and
L174–L177. Thus X=S_1 x B is the product of the identical marked
projective K3 surfaces, with the original common metric, ordered triple,
fixed identical holomorphic forms sigma_1,sigma_B and actual connection.
The hypothetical locally free rank-two product-polystable F has integral
c_1(F)=0 and full character

\[
 \operatorname{ch}(F)=2-14e_1-21e_2-\tau_D+62e_1e_2.
\]

Use the actual truncation inclusion j, retraction r, top map a and
their cohomological maps i,R,A. Put V=End_0(F), E=H^2(X,V),
W=R^2p_*V, U=H^0(B,W). The split set Z is finite and reduced,
W has length one at each point, and s=|Z| may be zero. Retain
L176's actual orthogonal lift T and forms Q,Q_U,S_N, and the actual
normal residual map g_N=Rf, where f is L174's residual Atiyah map.
The bilinear forms are complex symmetric, not Hermitian.

Use L174's relative normalization, namely L108's fibre trace
(2 pi i)^(-2) integral sigma_1 wedge Tr, and its base-trace scalar
gamma defined by Tr_B(z)=gamma integral_B sigma_B wedge z.
This gamma is a nonzero scalar, distinct from L168's sheaf map
also named gamma. Retain L169's scalar delta_B and its specified
Verdier convention. Its optional relative scalar kappa is therefore
1 in the present fixed normalization.

Write q for the factor intersection form, phi(u)=delta_u sigma_1,
d=2 lambda, where lambda is the root in (1,5/4) of
lambda^3+lambda^2-2lambda-1=0. Retain the full self-adjoint,
semisimple correspondence D of L174 and L177's specific Dk=4k,
q(k,k)=-14. The two other cubic roots are in (-2,-3/2) and
(-1/2,0). Use L175's common labelling h_z=diag(1,-1), its actual
top base-change map theta_z and integral-normalized chi_sigma.
For nonempty Z let w_k(z)=theta_z^(-1)(h_z chi_sigma), as in L175.
There is no independently adjustable point scalar.

No existence of F, section integrability, actual section quadric,
radical-image value or minimum square length is assumed. In particular
the norm below is computed, not assumed from nondegeneracy.

## Conclusion

The trace conventions give

\[
       \gamma=\delta_B(2\pi i)^{-2}.                    \tag{1}
\]

For nonempty Z the prescribed vector has norm

\[
 \boxed{Q_U(w_k,w_k)=\frac{\gamma s}{d(2\pi i)^2}},
 \qquad
 c:=(-2\pi i)^2Q_U(w_k,w_k)=\frac{\gamma s}{d}.         \tag{2}
\]

On the k-line in L174's domain, L176's normal pullback form is

\[
 \left.g_N^*S_N\right|_{\phi^{-1}(\mathbb C k)}
   =\frac{\gamma}{d}(d^2-16+14s)\,\left.\phi^*q\right|_{\phi^{-1}(\mathbb C k)}.
                                                               \tag{3}
\]

Its coefficient cannot vanish for any integer 1<=s<=782 (in fact
for any positive integer). The only real zero as a function of s is

\[
          \frac{16-d^2}{14}\ \in\ (39/56,6/7).         \tag{4}
\]

Consequently rank(g_N^*S_N)=15, rank(g_N)>=15 and

\[
        704-s+2t\ge15,\qquad s\le689+2t\le781.        \tag{5}
\]

For empty Z, U=0 and L176 already gives rank(g_N^*S_N)=15;
no w_k or nonzero point norm is asserted. The uniform inequality
(5) includes that case, retaining t<=46 from L176.

This is a conditional local ADVANCE / REPRODUCTION by specialization
of the assessed trace theorems and actual-coordinate formulas. The
separate step 600 conceptual audit below preserves these formulas
(EXPLORATION / REPRODUCTION), without a substantive correction or
stronger result. It excludes the remaining formal
cardinality 782 under these hypotheses; it neither excludes F nor
constructs it. It computes no actual section bracket or radical image,
and supplies no lower square length, transport or uniform primitive
Hodge realization. No new general trace theorem or claim beyond the
checked source tools is made.

## Proof

**Imported trace comparison and its convention.** The invocation-start
SPECIALIZE assessment is
`drafts/literature/2026-10-28-actual-atiyah-point-norm.md`.
Import David A. Cox, *Toric Residues*,
[arXiv:alg-geom/9410017v1, Appendix A, Proposition A.1 and proof,
printed pp.19–20](https://arxiv.org/pdf/alg-geom/9410017v1#page=19).
For a compact orbifold of complex dimension n it identifies the
standard algebraic trace with (-1/(2 pi i))^n times the integral of
the corresponding Dolbeault (n,n)-form. Its Appendix has no toric
hypothesis. B is a smooth projective surface, so n=2 applies.
The integral computation in that theorem is imported, not reproved.

Use S. Nayak and P. Sastry, *Grothendieck Duality and Transitivity II*,
[arXiv:1903.01783v2, Section 5.2, Proposition 5.2.3(i) and proof,
printed pp.24–26](https://arxiv.org/pdf/1903.01783v2#page=24),
with (4.1.2),(4.1.5), pp.21–22. These fix the Verdier trace by the
standard projective trace and identify supported and proper traces.
For its actual functorial evaluation/composition use
[Stacks Lemma 48.27.1(5),(7), Remarks 48.27.2–3, 0FVU](https://stacks.math.columbia.edu/tag/0FVU).
The structural map of B is smooth proper over C, and the coherent
inputs are bounded; these are the same normalized counits used in
L168/L169. No point sheaf is assumed locally free or flat over B.

Here is the necessary comparison of the two source conventions.
On the standard ordered cover of P^2, Cox's normalizing class is
represented by Omega/(T_0 T_1 T_2). On T_0!=0, with t_i=T_i/T_0,
it is dt_1 wedge dt_2/(t_1 t_2). This is exactly the ordered Cech
generator given trace 1 in Nayak–Sastry Section 5.2. Thus their
Verdier trace has the standard algebraic normalization in Cox's
theorem, using the functorial trace normalization in its proof;
there is no independent scalar or sign to choose for B.

Cox's Dolbeault comparison is the composition of connecting maps in
the usual bar-partial resolution (Proposition 6.1, printed pp.14–15).
Multiplication by sigma_B identifies the Dolbeault resolutions of
O_B and omega_B by z -> sigma_B wedge z. It is a chain map without
a sign because sigma_B has total degree two. Moving it past a
(0,2)-form also has sign +1. The shift [2] in L169's defining
dualizing isomorphisms is even and introduces no differential sign.
We are therefore using the actual class m_sigma_B(z), represented
by sigma_B wedge z, rather than a differently signed comparison.
L169 has already incorporated the internal-Hom/Koszul sign in its
weight; it must not be attached a second time here.

Let tr_B^Verd be the proper trace using nu_B of L169. The imported
dimension-two formula now reads

\[
 \operatorname{tr}_B^{\rm Verd}(m_{\sigma_B}(z))
       =(2\pi i)^{-2}\int_B\sigma_B\wedge z.           \tag{6}
\]

L169 defines chi_B=delta_B nu_B composed with m_sigma_B. Applying
the counit is linear in this isomorphism, so Tr_B(z) is delta_B
times (6), not delta_B^(-1) times it. The integral is a nonzero
functional on H^2(O_B), by Serre duality and sigma_B!=0. Comparing
with L174's definition of gamma proves (1). This is a comparison
of the specified trace conventions, not an identification of scalars
solely because both were called traces.

**Coordinates of the prescribed vector.** L168 fixes

\[
 \ell_z(w)=\frac{(2\pi i)^{-2}}2
       \int_{S_1}\sigma_1\wedge
                \operatorname{Tr}(h_z\theta_z(w)).
\]

For L175's particular w_k(z), theta_z(w_k(z))=h_z chi_sigma,
Tr(h_z^2)=2 and integral sigma_1 wedge chi_sigma=1. Thus

\[
                \ell_z(w_k(z))=(2\pi i)^{-2}.          \tag{7}
\]

This uses the same actual top map, including derived base change;
neither the residue line nor the bracket coordinate has been rescaled.
L168 gives orthogonality across distinct points, and L169 gives the
common weight delta_B kappa/d. L108's relative integral form, retained
in L174, is exactly the reference integral defining kappa, so kappa=1.
Substitution of (7) at all s points yields, before using (1),

\[
 Q_U(w_k,w_k)=\frac{s\delta_B}{d(2\pi i)^4}.
\]

Equation (1) gives (2). In particular the norm is nonzero for s>0
because gamma and d are nonzero. This conclusion uses equal actual
coordinates and the evaluated weights, not positivity or the false
implication that every nonzero vector in a nondegenerate complex
bilinear space has nonzero norm. The square (-2 pi i)^2 in c is an
ordinary scalar square, not an absolute square.

**Exact k-line test.** L176's actual orthogonal decomposition gives

\[
 (g_N^*S_N)(u,v)
    =\gamma q((d-D^2/d)\phi(u),\phi(v))
                   -\frac{\gamma s}{d}\ell(u)\ell(v),
 \qquad \ell(u)=q(\phi(u),k).                         \tag{8}
\]

By the audited marking in L177, Dk=4k and q(k,k)=-14. For
x=a k, y=b k we have q(x,k)q(y,k)=-14 q(x,y).
Putting these in (8) proves (3); explicitly its value at
u=v=phi^(-1)(k) is -14 gamma(d^2-16+14s)/d.

The exact root data give 2<d<5/2, hence 4<d^2<25/4.
Solving the affine coefficient equation gives (4), since
(16-25/4)/14=39/56 and (16-4)/14=6/7. This interval contains no
positive integer. Equivalently, for s>=1,
d^2-16+14s>=d^2-2>2. These are exact inequalities from the
specified root interval, not floating-point evidence. No division
by an unknown norm occurs.

**Rank consequence and qualifications.** L174 decomposes H^(1,1)
into the q-orthogonal eigenspaces with multiplicities 5,7,7,1 for
d,2 mu,2 nu,4. L177 identifies the last line as C k. Thus ell
vanishes on the other three eigenspaces, by self-adjointness and
their eigenvalues being different from 4. The rank-one term in (8)
changes only the k-line block. The d block stays zero, the two
other cubic blocks stay nondegenerate by L174's exact absolute-root
separation, and (3) makes the last block nondegenerate. The pulled-back
normal Gram form therefore has rank 7+7+1=15 exactly.

The composition/range rank inequality already imported and specialized
in L176 gives rank(g_N^*S_N)<=rank(g_N)<=dim K_N. With
dim K_N=704-s+2t and t<=46 from L176 this proves (5).
When Z is empty, (8) is replaced by g_N^*S_N=f^*Q, which already
has rank fifteen; there is no use of a point vector in that case.
No assertion is made that rank(g_N)=15, since the five domain radical
directions may have nonzero isotropic images invisible to the pullback.

This meets the bounded continuation test: the normalization bridge
and integer test determine a surviving fifteenth Gram direction.
The improvement from s<=782 to s<=781 is conditional on the complete
retained family and actual arrows; its separate audit is below.
It supplies no value of a section quadric or geometric lower square
length. In particular the new k-line normal direction has a nonzero
point component when Z is nonempty; no fifteenth point-free direction
or improvement of L177's original-quartic square capacity is claimed.
The existence, transport and general primitive-realization gaps remain.

**Separate conceptual audit (2026-10-28, step 600).** The unchanged
invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-28-actual-point-norm-critical-audit.md`.
This audits the specialization (1)–(8), conditional on the retained
actual-family results L108, L168, L169 and L174–L177. It does not
reaudit their entire ancestry or assert existence of F. The primary
passages re-inspected are Cox A.1 and its complete proof, printed
pp.19–20, the connecting-map comparison in Proposition 6.1,
pp.14–15, and Nayak–Sastry II Section 5.2, Proposition 5.2.3(i)
and (4.1.5), in the versions cited above. This is verification of
the approved proof's application, not new source discovery.

The global scope of the imported theorem matters. Cox A.1 compares
the normalized algebraic trace on every compact orbifold with its
Dolbeault integral. Its proof uses the formal properties of that
trace system to obtain one normalization constant; it does not infer
equality of two arbitrary functionals on B from an equality on P^2.
The proper counit, composed with Verdier's isomorphism, is the
algebraic trace system here: Nayak–Sastry (4.1.5) identifies its
proper trace with its supported residue trace. Proposition 5.2.3(i)
identifies its projective normalization with the standard algebraic
one. On the ordered cover (T_0,T_1,T_2), both sources use
dt_1 wedge dt_2/(t_1 t_2), without a reversed parameter order or a
negative generator. It therefore has trace 1 in both conventions.
Apply Cox's global theorem to this normalized system on B, which
is smooth projective of dimension two. No new uniqueness theorem
for traces, toric hypothesis on B, or chosen identification of
H^2(omega_B) with H^2(omega_{P^2}) is being assumed.

The Dolbeault comparison in Cox is specified by the successive
connecting maps of the bar-partial resolution. For every degree q,
m_sigma_B on that resolution is z -> sigma_B wedge z, and
bar-partial(sigma_B wedge z)=sigma_B wedge bar-partial z.
It agrees in degree zero with multiplication on the holomorphic
sheaves. Naturality of those same connecting maps consequently
identifies its map on H^2 with multiplication by sigma_B. The
factor from interchanging a (2,0)-form and a (0,2)-form is +1.
The even shift [2] changes neither this chain-map equation nor the
degree-two trace evaluation. Thus the integral in L174's definition
of gamma is the integral to which Cox A.1 applies, with factor
(-1/(2 pi i))^2=(2 pi i)^(-2).

L169 fixes chi_B=delta_B nu_B m_sigma_B as an equality of global
dualizing isomorphisms. The proper counit is linear in this map;
therefore Tr_B is delta_B times the Verdier trace, not its inverse.
Since sigma_B gives a nonzero Serre functional on H^2(O_B),
comparison of these functionals proves (1). This retains the
internal-Hom/Koszul minus sign already present in L169's local
formula; the global comparison introduces no second such sign.
The scalar gamma here never denotes L168's sheaf isomorphism.

Next compare the relative normalization without appealing to (1).
L108 (4) explicitly specifies the fibre pairing as
(2 pi i)^(-2) integral sigma_1 wedge Tr, and L174 retains exactly
that pairing. This is the reference used to define kappa in L168
and L169, so kappa=1, not (2 pi i)^(-2). The fixed coordinate ell_z
itself already contains (2 pi i)^(-2)/2. For L175's prescribed
vector, the actual theta_z gives h_z chi_sigma; hence Tr(h_z^2)=2
and integral sigma_1 wedge chi_sigma=1 give ell_z(w_k(z))=(2 pi i)^(-2).
There is no replacement of a derived middle fibre by the ordinary
one: only the previously established actual top isomorphism is used.

L168's point form is bilinear and orthogonal between distinct
support points. Put a=(2 pi i)^(-2). L169 gives its weight
delta_B/d in each ell_z coordinate. Thus both arguments contribute
a, and the norm is s delta_B a^2/d. By (1), gamma=delta_B a,
so this equals gamma s/[d(2 pi i)^2]. Multiplication by
(-2 pi i)^2=(2 pi i)^2 then gives c=gamma s/d. In particular the
negative real value of (2 pi i)^2 is present on both sides of this
cancellation; replacing either square by an absolute square would
give the wrong sign. Uniform nonzero coordinates and the evaluated
common weight establish nonzero norm for s>0. Nondegeneracy alone
would not establish it.

The audited L176 decomposition is G=g_N^*S_N+c ell tensor ell.
Subtracting its point term gives (8). To check the sign directly,
take x=y=k. The G-value is -14 gamma(d^2-16)/d, and the
subtracted point value is 196 gamma s/d. Their difference is
-14 gamma(d^2-16+14s)/d, exactly (3). In particular the negative
intersection square k^2=-14 changes the coefficient by +14s,
not -14s. This uses L177's checked eigenline Dk=4k.

The root interval 1<lambda<5/4 gives 4<d^2<25/4, so the unique
real zero (16-d^2)/14 is strictly between 39/56 and 6/7. For an
integer s>=1 the stronger direct estimate d^2-16+14s>2 suffices.
L174's other two cubic-root intervals give |2mu|>3>d and
|2nu|<1<d; their coefficients d-(2mu)^2/d and d-(2nu)^2/d
are nonzero. By semisimplicity and self-adjointness their
seven-dimensional eigenspaces and the five-dimensional d-eigenspace
are nondegenerate and orthogonal to the k-line. Thus ell vanishes
on them, the d block stays zero, and the other blocks have ranks
7,7,1. This proves rank(g_N^*S_N)=15, not merely a nonzero
k-line value or a claim of rank fifteen for g_N itself.

As a map to the dual domain the Gram form is
g_N^vee b_N g_N, where b_N is the map associated with S_N.
Its rank is at most rank(g_N), which is at most dim K_N.
The actual dimension 704-s+2t and retained t<=46 give
s<=704+2t-15<=781. At s=782, even t=46 would give dimension
14, contradicting the verified Gram rank. If Z is empty then U=0,
g_N^*S_N=G has rank fifteen by L174/L176, and 704+2t>=15 is
automatic; no w_k, point norm or nonempty-support claim is used.

All substantive formulas and bounds survive. The five-dimensional
domain radical may still have nonzero isotropic image. The extra
normal k-line has a point part when Z is nonempty, so the audit
does not subtract fifteen from the original-quartic capacity.
Actual section quadrics, their minimum square length, F existence,
transport and primitive realization remain open. The direct inputs
already listed for L178 in the DAG are sufficient and unchanged.
This is EXPLORATION / REPRODUCTION: verification of the existing
conditional specialization, not a second advance or a new general
trace theorem. No mathematical script or new lemma is needed.

## Mathlib

Full matching coverage of this geometric trace-convention bridge and
prescribed-vector norm has **not been checked**; no absence claim or
Lean verification is made. The sum/composition/target-dimension rank
inequalities and their exact Mathlib declarations and revisions remain
as cited in L176. The general trace comparisons here are imported by
precise primary citations; the coordinate substitution, root-interval
test and actual normal Gram specialization are the informal proof above,
with its separate conceptual audit. This is not a Lean verification.
