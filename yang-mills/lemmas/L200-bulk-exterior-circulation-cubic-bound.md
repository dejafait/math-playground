# L200 — Cubic control of the bulk exterior by retained circulations

## Hypotheses

Use exactly L198–L199's SU(2) relative cube, sufficiently fine admitted
even N, a=8/N, straight lower-rooted direction-1 forest, full compact
displacement and both actual L010 probes i=3,6 at tau=1/16. Take the
bare expansion at fixed mesh before refinement. All matrices and norms
below use ordinary stored full-link coordinates. Retain every variable
normal end edge, physical face, constant own-direction mode and heat mode.

Write D for vertex incidence, C for link-to-plaquette circulation,
L=C^T C, Delta=L+DD^T, Sigma=Delta^(-1), P for the co-closed
projection and S=Sigma P. The three Gaussian colors z have covariance
S independently. Keep the complete residual A=PAP, both insertion
subtractions, T=2SA and M=2SAS. These are signed operators where
appropriate; no positivity of A or M is assumed.

Keep L194's b, J_y and full cubics script R_3, script S_3. Use L198's
actual exterior expansion, including all its summable polynomial weights,

    SB_i=a^2 sum_(k,l) d_(i;kl) n_k e_l^T, n_k=S e_k,
    beta_k^b=(I-Pi_n)(I-D Phi)n_k,
    sum_(k,l)|d_(i;kl)|p(k)p(l)<=C_(i,p).                (1)

Pi_n acts only on the deterministic upper normal exterior. It is not
commuted through any covariance or projection. Define B_(i,N), H_(i,N),
Q_(tr,i,N) and E_(i,N) exactly as in L198(3)–(4).

## Conclusion

For a fixed color c, with beta=beta_k^b and constants polynomial in k,

    ||d script S_3(z)[beta^(c)]||_2 <= C p(k) N^2,
    ||d script R_3(z)[beta^(c)]||_2 <= C p(k) N^3,
    ||d^2 script S_3(z)[beta^(c),Tz]||_2
                                      <= C p(k) N^3.  (2)

The second directional derivative in (2) holds beta fixed; it acts on
the two remaining rough slots. In particular L198's entire bulk trace
and the complete joint group satisfy

    |B_(i,N)|<=C_i N^3,
    |kappa_0(f_(i,1),r_1)-kappa_0(f_(i,1),r_0,S_3)|
                                               <=C_i N^3. (3)

Thus the a^3-scaled joint values are bounded. No finite scaled limit,
value, sign or compensation coefficient follows. B, H and transport can
all contribute at this scale. Independent f_(i,2),r_0, finer asymptotics,
full compensation, finite matching, interacting reflected error
<=c_box/2, continuum axioms and infrared finite positive mass remain
unresolved. This is local standard-estimate progress, not a claim of
progress beyond the checked sources.

## Proof

### 1. Differentiated relative covariance, before the quadratic count

For each scalar component of Sigma, and same-component first differences
at either argument with stencils inside its variable grid, one has

    |partial_e^j partial_f^h Sigma_(e,f)|
      <=C[(1+dist(e,f))^(-2-j-h)+N^(-2-j-h)],
             j,h in {0,1}, j+h<=2.                    (4)

The constant is uniform up to the physical boundary for such stencils;
no fixed positive physical distance from a face is required. Bounded
shifts of the anchors can be absorbed in C. Different component kernels
are zero. Circulations are finite sums of these differences on the
appropriate component grids, not differences between different kernels.

Here is the needed boundary extension of the estimates in L164 proof
section 2 and L166 proof sections 1–2. Those proofs give the exact
period-2N image formula with one even edge reflection and three odd
vertex reflections, and the infinite heat estimate

    |partial^m H_t(x)| <= C_b (1+t)^(-(4+m)/2)
                      (1+|x|/sqrt(1+t))^(-b).          (5)

Use m=0,1,2 and b>10. For m=2 the Fourier argument is the same one
used in L166(7): each of the two difference symbols has a simple zero
at frequency zero, so derivatives of their product times exp(-t lambda)
have L1 bounds C_b t^((b-4-m)/2) for t>=1. The torus complement has
exponential decay; t<=1 has bounded derivatives. Integration by parts
in a maximal coordinate gives (5). A source reflection may reverse a
difference or shift its base by one step, without changing this bound.

For t<=N^2, retain the finitely many nearest reflected images separately.
In each coordinate their distances are the direct distance or the
distances reflected about the two endpoints. Since both points lie in
the same interval, these are at least the direct coordinate distance,
up to the bounded shifts of a difference stencil. Their integrated
bounds from (5) are C(1+dist(e,f))^(-2-m). All further images are at
distance >=cN(1+|b'|) after a fixed finite grouping, b' in Z^4.
Summing (5) and integrating to N^2 gives C N^(-2-m). This argument
does not presume that the nearest reflected images are far away.

For t>=N^2, use the full relative product spectrum of L026(6)–(7).
Mode products have amplitude at most C N^-4, and each difference
contributes at most C |q|/N. The shell sum, with all allowed indices,
is at most C N^(-4-m) exp(-c t/N^2); its integral is C N^(-2-m).
There are at least three positive indices per link component. The
own-direction index zero remains included and has zero derivative in
that direction. These estimates prove (4) for mixed differences as well
as undifferenced entries. No boundary law has been changed.

### 2. Two local quadratic estimates with their volume dependence

Consider a two-color quadratic q with bounded-radius stencils, at most
M placements, bounded placement multiplicity and absolute coefficient
sum <=B per placement. L194(7)'s proof, with the placement count left
explicit, gives

    ||q||_(L2(S)) <= C B sqrt(M log(eN)).               (6)

Indeed S<=Sigma and
Sigma tensor Sigma-S tensor S=(Sigma-S) tensor Sigma
                              +S tensor (Sigma-S)>=0.
Thus compare the norm of the complete signed coefficient tensor with
its norm under Sigma, then expand that latter norm. Each cross-placement
product is bounded by C B^2[(1+r)^-4+N^-4]. Its sum over the second
placement is at most C B^2 log(eN), by the four-dimensional shell
count. This is uniform for a subset of placements, in particular a
boundary collar. There are no same-color internal pairs: differentiating
a fixed color of an alternating cubic leaves the other two colors.

If every summand has a first difference on at least one of its two
rough fields, and those difference stencils are inside the variable
grids, a stronger estimate is

    ||q||_(L2(S)) <= C B sqrt(M).                      (7)

To verify it without comparing entries of S and Sigma, first make the
same positive tensor comparison. Split q into the fixed finite number
of component, color-order and difference-direction types. Within each
type the differentiated color is fixed. Its second moment under Sigma
has a differentiated covariance in that color and an undifferenced
covariance in the other color. By (4) their product is bounded by

    C B^2[(1+r)^-4+N^-4][(1+r)^-2+N^-2].              (8)

The shell sum of (8) is uniformly bounded: the r^-6 term is summable;
N^-2 sum_(r<=CN) (1+r)^-4 is O(N^-2 log(eN));
N^-4 sum_(r<=CN) (1+r)^-2 is O(N^-2); and the constant N^-6
term sums to O(N^-2). Multiplication by M and a square root prove
(7) for this type. The triangle inequality over the bounded number of
types proves it for q. One can instead keep crossed derivative types;
their two first-derivative covariances have the same summable estimate.
Variable coefficients are held in the local coefficient bound and are
never moved through a covariance. No mesh-dependent number of types is
introduced. These arguments retain the original signed polynomial norm.

### 3. Smoothness of the actual bulk exterior where it is used

L187(14) and its at-most-four-dimensional mode projection give, for
unscaled same-component differences of orders j=0,1,2,

    |partial^j n_k|<=C a^j p(k)                       (9)

on the smooth sine/cosine extension. The second-difference assertion
follows by applying the same product-mode calculation twice; projections
remain inside the same frequency block, and all frequency factors are
absorbed in a fixed polynomial p. The positive physical spectral gap
controls the inverse in n_k.

Away from the exceptional upper normal row, the first component of
beta=(I-Pi_n)Rn_k is zero. A transverse component is n_k minus a
transverse difference of the complete lower axial sum of n_(k,1).
A transverse difference of that component is bounded by
C[a+N a^2]p(k)<=C a p(k), by (9). An axial difference of that
prefix difference is one transverse difference of n_(k,1), again
O(a p(k)). This telescoping identity retains the lower endpoint and
the constant axial mode. L187(15) gives the global amplitude bound
|beta|<=C p(k), including near all faces.

It follows that, on any fixed-radius stencil entirely away from the
physical boundary layers,

    |beta|<=C p(k), |partial beta|<=C a p(k),
                         |C beta|<=C a p(k).           (10)

The last estimate uses the paired opposite edges of a plaquette.
We do not use (10) on a stencil touching a fixed face or the selected
upper row. No smooth extension of beta across the upper pin is claimed.
All residual stencils are in a fixed compact interior enlargement by
L155 and L166. For the action, retain separately a collar of a fixed
number of lattice layers wide enough to contain every stencil touching
a physical face. It has O(N^3) plaquettes. Outside that collar, (10)
applies; on the collar only the global amplitude bound is used.

### 4. Every required interior cubic retains a linear difference

For the action use exactly L189(5)–(6):

    script S_3(z)=sum_p <(Cz)_p,w_(2,p)(z)>,
    d script S_3(z)[beta^(c)]
      =sum_p <(C beta^(c))_p,w_(2,p)(z)>
        +sum_p <(Cz)_p,dw_(2,p)(z)[beta^(c)]>.          (11)

w_2 is a bounded-coefficient quadratic of the four signed links.
On interior plaquettes the first term has coefficient bound C a p(k)
and no required rough derivative; (6) bounds it by
C p(k) a N^2 sqrt(log(eN)). The second retains a rough circulation
and coefficient bound C p(k); (7) bounds it by C p(k) N^2.
On the entire collar (11) remains an exact identity with fixed-link
zeros. Use the undifferentiated bound (6) for its complete polynomial,
with B=C p(k), M=O(N^3). Its norm is at most
C p(k) N^(3/2) sqrt(log(eN)). Both additional allowances are
O(p(k)N^2). This proves the first estimate of (2) without deleting
any action face or assuming a derivative estimate on its exterior jump.

For completeness check the residual from its exact full words rather
than transfer an action-only cancellation. L155(2) gives its force/vector
part before forest restriction as

    sum_e {<G_(e,1),X_(e,2)>+<G_(e,2),X_(e,1)>}.       (12)

L149(4)–(6) gives G_1=Lz and X_1=(1/a) times the endpoint-weighted
linear clover circulation. Thus G_1 is a finite sum of first
same-component differences of z with bounded coefficients (it actually
has two differences), and X_1 has the same property with coefficients
O(1/a). G_2 is a bounded local quadratic; X_2 is a local quadratic
with coefficient sum O(1/a). Endpoint transport terms in X_2 are
retained in this latter bound. Their coefficients include the full
sampled displacement, which is uniformly bounded.

Differentiate the first product in (12). The term G_1(z)dX_2(z)[beta]
retains a rough difference with coefficient bound C p(k)/a. The term
G_1(beta)X_2(z) has coefficient bound C p(k), since (10) gives
G_1(beta)=O(a p(k)); no stronger second-difference gain is needed.
For the second product, dG_2(z)[beta]X_1(z) retains a rough difference
with coefficient bound C p(k)/a, while G_2(z)X_1(beta) has bound
C p(k). This uses both force/vector terms. L155 proof section 1
identifies their sum with the coordinate-correct Ds_2 v_2+Ds_3 v_1;
no left-frame term is substituted for the coordinate jet.

The triplet subtraction is a weighted copy of the action cubic in
(11): 4 Tr W_(p,3) is -2 times its action coefficient, by L048(4) and
the identity 4P_p=4-2 Tr U_p. The fixed numerical factor is immaterial
for this norm bound. Its differentiated pieces have respectively an
exterior difference with coefficient O(a p(k)) or a rough difference
with coefficient O(p(k)). The shear subtraction consists of the two
orders C_1 C_2 and C_2 C_1 in L155(2). C_1 is a linear clover
circulation and C_2 a bounded local quadratic, so its differentiated
pieces have exactly those same two bounds. Both insertion weights are
bounded, and all their stencils are compact interior ones.

Consequently the whole derivative d script R_3[beta^(c)] is a fixed
finite sum of types with a rough difference and coefficient bound
C p(k)/a, plus types without that difference and bound C p(k).
There are O(N^4) placements. Equations (6)–(7) give

    ||d script R_3[beta^(c)]||_2
      <=C p(k)[a^-1 N^2+N^2 sqrt(log(eN))]
      <=C p(k) N^3.                                  (13)

This proves the second estimate in (2). It does not use residual
consistency on a rough column or discard a derivative of a coefficient.

### 5. Keep both rough tilt slots and close the original trace

Whiten S on im P as in L190 and L194: z=Z xi, ZZ^T=S, and
Tz=Z E xi with E=2Z^T A Z real symmetric and ||E||<=C N.
For the entire quadratic q=d script S_3[beta^(c)] the two remaining
colors give ||q||_2 equal to the Hilbert–Schmidt norm of its whitened
coefficient matrix. Acting with Tz on these two slots applies E in
each tensor factor, so

    ||d^2 script S_3[beta^(c),Tz]||_2
       <=2||E|| ||d script S_3[beta^(c)]||_2
       <=C p(k) N^3.                                 (14)

Apply this only after bounding the full quadratic in section 4; it
does not assert that a circulation of Tz has the covariance of a
circulation of z. The complete A, with both generator orders and both
subtractions, is present in E. Beta is held fixed, so no T beta term
belongs in (14). L198(10) already retains the distinct smooth-tilt term
in its subcubic error.

L198(13) is the exact contraction for the braces defining B_(i,N):

    -6 Tr(J_(e_l) S r_beta S)+12 Tr(J_(e_l) M s_beta S)
      =2 sum_c E[<e_l,b^c>
          {d script R_3[beta^(c)]
                    -d^2 script S_3[beta^(c),Tz]}].    (15)

L194(9),(11) gives ||<e_l,b^c>||_2<=C N^2 for every full mode.
Cauchy–Schwarz and (13)–(14) bound (15) by C p(k) N^5.
Multiplication by a^2 and the complete summable coefficients (1)
prove |B_(i,N)|<=C_i N^3. No prefix, selector or covariance was
reordered in this estimate, and both rough action placements remain.

Finally L198 gives G=B+H-Q_tr+E. L199 bounds H by C_i N^3;
L196 bounds Q_tr by C_i N^3; and L198 proves E=o(N^3).
This proves (3) for both actual probes. The three cubic-bounded terms
are retained with their original signs, without asserting separate
convergence or cancellation.

### 6. Verification and scope

The analytic checks are the mixed-difference image/spectral estimate
(4), the summable complete shell products (8), the actual-prefix
telescoping in (10), every product in (11)–(12) and both insertion
subtractions, and the full two-slot whitened tilt in (14). The collar
uses its actual placement count in (6), including corners and fixed-link
zeros. The full heat sum is taken only after polynomial mode bounds.
No numerical fixture or mathematical script is used as proof evidence.

The discriminating cubic-bound test succeeds. Bounded scaled values
need not converge: neither a subsequential choice nor the common upper
bound supplies the mesh-uniform approximation needed for a limit. The
next unresolved step is a signed limit of the retained B+H-Q_tr sum.
L197's factorwise covariance-commutator obstruction and ATTEMPTS/039–044
are unaffected; this proof instead improves the complete local quadratic
norm before applying the signed tilt.

## Mathlib

Full matching bulk bound and joint scaled limit: **not checked**.
Supporting relative-kernel, Gaussian tensor and finite-matrix coverage:
**not checked**; unknown coverage is not an absence claim. The named
Isserlis Gaussian pairing theorem, positive tensor comparison and
Cauchy–Schwarz are used in the explicit forms above. The exact word
jets, relative product spectra and image formula are imported from
L149, L155, L026, L164 and L166. Their boundary-uniform mixed-difference
specialization is justified because L194's generic local quadratic
bound alone retains the logarithm. No general flow-renormalization
theorem is reproved. Reuse the unchanged
[approved assessment](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md)
for the same selected bare joint group.
