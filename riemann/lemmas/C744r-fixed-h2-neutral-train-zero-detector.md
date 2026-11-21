# C744r: A strict fixed H2 budget retains off-line-zero detectors

## Hypotheses

Put ell=log(3)/2 and let N consist of the complex functions f in
C_c^infinity(0,ell) satisfying both local moments

    integral exp(x/2) f(x) dx = integral exp(-x/2) f(x) dx = 0.

All extensions are by zero, all L2 norms are unweighted, and

    ||f||_H2^2 = ||f||_2^2 + ||f'||_2^2 + ||f''||_2^2.

Fix a prescribed finite M0 for which there exists f0 in N with

    ||f0||_2=1, b=||f0||_H2<M0.                            (1)

This strict slack is essential to the proof. No assertion is made for
an empty family or a budget equal to its least admissible norm.
Write A_L for the original complete causal generator and
E_L(u)=-Re<A_L u,u>, with inner product linear in the first slot.
Use the unconditional smooth identity L742(8)-(12), its smooth-domain
argument, and L744(1),(6),(8). No RH-conditional conclusion of L742
is an input to the forward detector implication.

The imported zero formula is Suzuki, *Aspects of the screw function
corresponding to the Riemann zeta-function*,
[arXiv:2206.03682v4](https://arxiv.org/pdf/2206.03682v4), internal date
31 May 2023, Section2.2, printed p.7, and Sections3.1-3.5,
printed pp.9-11, especially (3.3), (3.5), Proposition3.1 and its
distributional interpretation. These give the compact-smooth Weil
formula and the order-one zero summability. The conjugate-ordinate
convention also appears explicitly in Suzuki, *Weil's quadratic form
via the screw function*,
[arXiv:2606.09096v3](https://arxiv.org/html/2606.09096v3),
23 September 2026, Section3.1, (3.1). These source statements were
assessed in steps279/283/512 and are reused, not reproved here.

Let Z be the distinct complex zeros z of Xi(z)=xi(1/2+iz), with
multiplicities r_z. Thus |Im z|<1/2, Z is discrete, conjugation and
negation preserve multiplicity, and

    sum_(z in Z) r_z/(1+|z|^2) < infinity.                 (2)

These are the usual nontrivial-zero strip, functional symmetries and
the cited order-one Hadamard summability. They do not assume RH, a
rightmost zero, a finite off-line set, or isolation of a lattice phase.

## Conclusion

If an off-line nontrivial zero exists, there are a single nonzero
f in N, an integer K0>=2 and a nonzero finite complex vector c such that

    ||f||_H2/||f||_2 < M0,
    U(x)=sum_(j=0)^(K0-1) c_j f(x-j ell),
    u=U/||U||_2,       E_(K0 ell)(u)<0.                   (3)

The train is in L744's exact smooth family, with both local and global
moments zero and with the actual generator domain verified below.
The proof needs only trains with at most two occupied cells. Neither
the profile nor its budget changes when this witness is extended by
zero to any K>=K0; its normalized energy remains the same negative
number. Hence it also gives a negative witness on every eventual
K_R=floor(log log R/ell) scale.

Under (1), nonnegativity for every admitted fixed-profile finite train
is therefore equivalent to RH. The reverse implication is just the
imported real-zero square formula. This is a constrained criterion,
not a proof of either its positivity or RH. In particular a uniform
eventual low-energy margin for every locally neutral member of
L744's budget-M0 family would imply RH. C744q's sufficient margin
32 C^2 log(R)/R^4 for a given low vector is not established here,
and RH is not asserted to imply that strict uniform margin.

This is one research derivation under the prior EXPLORE assessment
`drafts/literature/2026-11-11-fixed-h2-cell-train-complete-pairing-512.md`,
11 November 2026, step513. Classification POTENTIALLY_NEW refers only
to the constrained combination not covered by that bounded comparison;
it is not a claim of originality. The separate conceptual audit in
Section 6 (11 November 2026, step515) accepts the argument under exactly
(1), without a mathematical repair. No actual off-line
zero, effective detector length, positive low floor or RH candidate
is supplied.

## Proof

### 1. Exact admission, Fourier convention and all-zero convergence

For any nonzero f in N and any nonzero finite coefficient vector,
disjoint cell supports, including those of every derivative, give

    ||U^(a)||_2^2 = ||f^(a)||_2^2 sum_j |c_j|^2,
                    a=0,1,2.                             (4)

Thus ||U||_2>0 and ||u||_H2=||f||_H2/||f||_2 exactly.
Each cell moment is zero. The global moment with sign sigma is
the sum of these local moments multiplied by c_j exp(sigma j ell/2),
and is therefore also zero. Smooth compact support inside every cell
makes U a member of C_c^infinity(0,K ell), with no boundary jumps.
As in L742, Phi_U(x)=integral_0^x log(x-y)U(y)dy has derivative
integral_0^x log(x-y)U'(y)dy. Local integrability of log and boundedness
of U' give an absolutely continuous Phi_U with L2 derivative on the
finite interval. This is the actual generator-domain criterion;
no guessed closed-form domain or extension of a positivity theorem
is being used.

For any compact smooth v on the line put

    F_v(z)=integral v(x) exp(-izx) dx,
    tilde(v)(x)=conj(v(-x)),  tau_a v(x)=v(x-a),
    H(v,w)=W(v*tilde(w)).

The source uses the plus Fourier transform. Direct finite-support
Fubini gives Fplus_(v*tilde(w))(z)=F_v(-z)conj(F_w(-conj(z))).
Reindex its zero formula by z to -z, retaining multiplicity. With
L742(12) and polarization this yields

    H(v,w)=sum_(z in Z) r_z F_v(z)conj(F_w(conj(z))).      (5)

For v,w supported in a common positive window, H is exactly the
Hermitian polarization of the original E_L. It is independent of the
chosen encompassing window. Formula (5) also defines its extension to
arbitrary compact smooth supports and shows common real-translation
invariance. In particular H(tau_a v,tau_b w)=H(v,tau_(b-a) w).
Hermitian symmetry follows either by polarization on a translated
positive window or by conjugating (5) and reindexing conjugate zeros.

Here all zero sums converge absolutely before any grouping. For each
fixed compact smooth v, integration by parts N times gives
|F_v(z)|<=C_(v,N)(1+|z|)^(-N) uniformly on |Im z|<=1/2.
The support bound controls exp(Im(z)x), and the bound near z=0 is
included by increasing the constant. Taking N=2 and using (2)
proves absolute summability in (5). For the single-profile train,
P(w)=sum c_j w^j gives the exact factorization

    F_U(z)=F_f(z)P(exp(-i ell z)),
    E_(K ell)(u) = [||f||_2^2 sum_j |c_j|^2]^(-1)
      sum_z r_z F_f(z)conj(F_f(conj(z)))
        P(exp(-i ell z))conj(P(exp(-i ell conj(z)))).      (6)

For each fixed P this series is absolute, since its arguments lie
in a fixed compact annulus. Formula (6) includes all aliases, all
multiplicities and the entire zero complement. At a nonreal z its
summand is not a modulus square. No bound uniform in deg(P) is
inferred from this fixed-train convergence.

### 2. Consequences of nonnegativity on the strict-slack family

Suppose, for contradiction, that every normalized finite train from a
nonzero g in N with ||g||_H2/||g||_2<M0 has nonnegative energy.
It suffices to suppose this for the subfamily with at most two occupied
cells. Denote d(v)=H(v,v) on one cell and
define, for m>=0,

    B_m(v,w)=H(v,tau_(m ell) w),   q_m(v)=B_m(v,v).

All these forms are complex-linear in the first slot and conjugate-
linear in the second. For an admitted profile g, the one-cell test
padded into two cells gives d(g)>=0. For m>=1, both diagonal entries
of its two-cell section are d(g), by translation invariance. Its
energy before normalization is

    (|a|^2+|c|^2)d(g)+2 Re(a conj(c) q_m(g)).

Nonnegativity for arbitrary a,c implies |q_m(g)|<=d(g): if
q_m(g)!=0, take a=1 and c=-q_m(g)/|q_m(g)|. Thus, also for m=0,

    |q_m(g)|<=d(g),  m>=0, for every admitted g.           (7)

We next extend boundedness, not positivity, to arbitrary bounded sets
of neutral profiles. L742(9) and L744(8) give a fixed-cell bound.
Since exp(ell)=sqrt(3)<2 there are no arithmetic delays on this cell;
neutrality kills the pole product. With

    A=2+8sqrt(2)/3+log(4pi),  D=A+2,

the inequality |m(xi)|<=A+log(2+|xi|)<=A+2+xi^2 and Plancherel give

    |d(v)|<=D ||v||_H2^2,       v in N.                   (8)

The elementary second inequality follows, for t>=0, from
log(2+t)<=log(2)+t/2<=2+t^2. This uses the full local energy,
not its arithmetic part or a source positivity certificate.

Fix B>0 and let v in N have ||v||_H2<=B. Write Delta=M0-b>0 and
choose the same positive number for every such v,

    epsilon=min{1/(2B), Delta/[2(1+M0)B]}.

Then g_+=f0+epsilon v and g_-=f0-epsilon v are nonzero, neutral,
and have strict normalized H2 budget below M0: their L2 norms are
at least 1-epsilon B>=1/2, while their H2 norms are at most
b+epsilon B, and

    M0(1-epsilon B)-(b+epsilon B)>=Delta/2>0.             (9)

The exact quadratic second difference, valid also for the generally
non-Hermitian B_m, is

    q_m(g_+)+q_m(g_-)-2q_m(f0)=2 epsilon^2 q_m(v).

Apply (7),(8), noting that b+epsilon B<=b+1/2. It follows that

    |q_m(v)| <= C_B,
    C_B=D[(b+1/2)^2+b^2]/epsilon^2,  every m>=0.          (10)

This constant is finite, depends on the fixed set bound B, and is
independent of m. The direction v itself need not satisfy the budget;
only the small perturbations actually tested in (7) do. No large
carrier frequency is substituted into the admitted family.

For independent v,w in N, complex polarization of the sesquilinear
B_m gives, without a Hermitian assumption on B_m,

    4 B_m(v,w)=q_m(v+w)-q_m(v-w)
                    +i q_m(v+iw)-i q_m(v-iw).             (11)

Consequently |B_m(v,w)|<=C_B whenever
||v||_H2+||w||_H2<=B, uniformly for all m>=0. This deduction uses
only single-profile two-cell tests; it does not assume positivity
for trains whose cells have independently chosen profiles.

### 3. Recover continuous separations without separating lattice aliases

Choose any 0<w<ell/2 and any nonzero phi in N supported in (0,w).
Let D0=ell-w>ell/2. Every tau_a phi with 0<=a<=D0 is still compactly
supported inside (0,ell), is neutral (its two moments acquire nonzero
exponential factors), and has the same H2 norm as phi.

Given t>=0, choose a nearest nonnegative integer m to t/ell.
Then delta=t-m ell lies in [-ell/2,ell/2]. Choose a,b0 in [0,D0]
with b0-a=delta; for example (a,b0)=(0,delta) for delta>=0,
and (-delta,0) otherwise. Translation invariance and (11) give

    h(t):=H(phi,tau_t phi)
        =B_m(tau_a phi,tau_b0 phi),
    |h(t)|<=C_(2||phi||_H2),       all t>=0.               (12)

The same estimate includes m=0. All auxiliary supports have a
uniform positive distance from their cell boundaries because phi
has compact support strictly inside (0,w). This step neither assumes
distinct lattice phases nor deletes their collisions. It obtains
continuous separations from perturbations and polarization before
attempting to distinguish any zero.

### 4. A nonzero off-line residue and the complete meromorphic tail

If RH fails, conjugation gives z0 in Z with Im(z0)<0. Choose phi as
above so that both F_phi(z0) and F_phi(conj(z0)) are nonzero. Here is
an explicit existence argument, with no density/interpolation import.
Fix x_* in (0,w) and choose a nonnegative smooth bump eta of integral
one in a sufficiently small neighborhood of x_*. For each z in the
finite set {z0,conj(z0)}, require throughout its support

    |exp(-iz(x-x_*))-1|<1/2.

Continuity permits this choice and implies
|exp(iz x_*)F_eta(z)-1|<1/2, hence F_eta(z)!=0. Set
phi=eta''-eta/4. Twice integrating by parts proves both moments zero,
and

    F_phi(z)=(-z^2-1/4)F_eta(z).

Neither z0 nor its conjugate is +i/2 or -i/2, since those are outside
the open nontrivial-zero strip. Thus both values are nonzero and
phi is nonzero. Its H2 norm may be large but is fixed and finite;
(9) pays that norm by a smaller epsilon without changing M0.

For this one phi put

    a_z=r_z F_phi(z)conj(F_phi(conj(z))).

The proof of (5) gives sum_z |a_z|<infinity, with a_(z0)!=0.
Its complete, absolutely convergent translated correlation is

    h(t)=sum_z a_z exp(i t z).                            (13)

Convergence is uniform on bounded real t intervals, since each
exponential has modulus at most exp(|t|/2). Under the contradiction
assumption, (12) instead bounds this whole function for all t>=0.
Therefore

    J(s)=integral_0^infinity h(t) exp(-s t) dt

is holomorphic in Re(s)>0: on every closed sub-half-plane Re(s)>=sigma>0,
boundedness dominates the integrand and each s derivative by a
constant times t^n exp(-sigma t), an integrable function.
For Re(s)>1/2, Tonelli's absolute bound

    sum_z integral_0^infinity |a_z exp((iz-s)t)|dt
       <= (sum_z |a_z|)/(Re(s)-1/2)

justifies interchange and yields

    J(s)=G(s):=sum_z a_z/(s-i z),        Re(s)>1/2.        (14)

The right side is meromorphic on the whole plane with a simple pole
at i z whenever a_z!=0. To check the complete tail, take any compact
set in |s|<=R avoiding all points i z. There are finitely many zeros
with |z|<=max(2R,1). For all other zeros, |s-i z|>=|z|/2, so their
series is uniformly absolutely convergent, bounded termwise by
2|a_z|/|z|<=2|a_z|. The uniform-limit theorem for holomorphic functions
applies. The same argument on a small disk about any one pole, with
that term omitted, shows that the rest is holomorphic there. Thus the
residue at i z0 is exactly a_(z0), not a truncated or assumed remainder.
Multiplicities are already in a_z; distinct zeros give distinct i z.

The half-plane Re(s)>0 minus the discrete set {i z} is connected:
any compact polygonal path can be detoured around its finitely many
intersections with that discrete set. By the identity theorem, (14)
therefore holds on this punctured half-plane. But p=i z0 lies strictly
inside it, because Re(p)=-Im(z0)>0. J is holomorphic at p while G has
residue a_(z0)!=0 there. Multiplying the equality on a punctured disk
by s-p and letting s tend to p gives 0=a_(z0), a contradiction.

This proves existence of (3). No extremal displacement, lattice-atom
isolation, sign of a deleted-zero remainder, or growing-degree uniform
truncation was used. The complex-analytic identity theorem and the
uniform-limit theorem are standard named inputs; the bounds needed
for their use and for the Laplace integral are supplied explicitly.

### 5. Fixed-profile transfer and the exact limitation

Once a negative witness f,K0,c exists, fix all of them. Padding c by
zeros to length K>=K0 leaves U, (4), and its normalized H2 norm
unchanged. By (5), E_(K ell)(u)=E_(K0 ell)(u)=e<0, independently of
the ambient window. For R>=exp(exp(K0 ell)), K_R>=K0, so this same
unit vector is an admitted negative low vector on every such scale.
This supplies the eventual transfer; it does not estimate K0 or e.

If RH holds, every z in (5) is real and E_L(u)=sum_z r_z|F_u(z)|^2
is nonnegative. This proves the converse criterion, using the imported
formula. It provides no uniform strictly positive margin. The main
actual-Xi sign, non-neutral coverage and all-window assembly remain
open. In particular the conditional detector is not a disproof: its
off-line-zero hypothesis has not been exhibited or established.

### 6. Separate conceptual audit — 11 November 2026, step515

This audit uses the prior EXPLORE assessment
drafts/literature/2026-11-11-fixed-h2-train-detector-audit-513.md,
separately approved in step514. The complete proof above was checked
against L742(8)-(12) and its existing normalization/polarization audit,
and L744(1),(6),(8). The cited Suzuki formulas and their version
qualifications are reused from the ready assessments; no new source
theorem or stronger positivity input is imported. The result is an
audit of the constrained combination, not a reproof of the explicit
formula or a new mathematical discovery beyond the derivation above.

1. **Admission and the complete pairing, (4)-(6).** Smooth zero
   extensions have disjoint derivative supports in distinct cells.
   Thus (4) holds also for zero coefficients and for arbitrarily
   separated occupied cells. For a nonzero coefficient vector its
   a=0 case gives a strictly positive denominator. Each global moment
   is the corresponding local moment times a finite exponential
   factor, summed over the cells, so both vanish exactly. For each
   finite window the domain bound is

       |Phi_U'(x)| <= ||U'||_infinity integral_0^L |log v| dv < infinity.

   Together with U(0)=0 and the convolution identity this gives the
   actual absolute-continuity and L2 derivative conditions.
   It requires no uniform bound as L grows.

   The Fourier transform of tilde(w) at z is
   conj(F_w(conj(z))), not conj(F_w(z)). With the source's plus
   convention, negation of the entire zero set gives exactly (5).
   Conjugation of (5), followed by z -> conj(z), gives Hermitian
   symmetry. The transform factors for tau_a v and tau_b w multiply
   to exp(i(b-a)z), giving common-translation invariance. Integration
   by parts twice in the closed strip bounds the absolute summand
   by a constant times r_z(1+|z|)^(-4); (2) sums this majorant.
   For each finite polynomial P the annulus bound in (6) is finite.
   Nothing here supplies a bound uniform in its degree.

2. **Uniform strict-slack extension, (7)-(11).** The two-cell
   Hermitian section has equal real diagonals d(g). For q_m(g)!=0,
   the displayed choice a=1, c=-q_m(g)/|q_m(g)| has energy
   2(d(g)-|q_m(g)|). The padded one-cell test gives d(g)>=0;
   hence (7), including m=0. Nonnegativity is used only for these
   same-profile tests.

   On the single cell no log(n) delay occurs since exp(ell)<2,
   and neutrality kills the complete pole product. L744(8) and
   Plancherel therefore give

       |d(v)| <= (A+2)||v||_2^2+||v'||_2^2
              <= D||v||_H2^2.

   For every direction with H2 norm at most B, the same epsilon
   in (9) satisfies epsilon B<=1/2 and
   (1+M0)epsilon B<=Delta/2. Thus both perturbations have L2
   norm at least 1/2 and normalized H2 norm strictly below M0,
   independently of m and of the chosen direction. The quadratic
   second difference has no Hermitian prerequisite. Its triangle
   bound is

       2 epsilon^2 |q_m(v)|
         <= 2D(b+1/2)^2+2Db^2,

   exactly the constant in (10).

   For an arbitrary first-slot-linear sesquilinear B_m, expansion
   gives q_m(v+w)-q_m(v-w)=2B_m(v,w)+2B_m(w,v), whereas
   q_m(v+iw)-q_m(v-iw)=-2iB_m(v,w)+2iB_m(w,v).
   This verifies the sign and the non-Hermitian validity of (11).
   Each of the four directions has H2 norm at most B when
   ||v||_H2+||w||_H2<=B, giving the same C_B uniformly in m.
   Positivity of mixed-profile trains is never inferred.

3. **All real separations, (12).** If supp(phi) is contained in
   [alpha,beta] inside (0,w), its translates with 0<=a<=ell-w
   stay at least min(alpha,w-beta)>0 from the cell boundary.
   Their H2 norms are identical and both moments remain zero.
   The relative-shift interval [-(ell-w),ell-w] contains
   [-ell/2,ell/2]. A nearest nonnegative lattice index consequently
   realizes every t>=0, including t near zero, by
   t=m ell+b0-a. Applying (11) with B=2||phi||_H2 proves (12)
   with one finite constant for all t. There is no passage from
   lattice bounds to continuous bounds by an unproved sampling
   theorem; the shifts are actual admissible directions in (9).

4. **Nonzero residue and full complement, (13)-(14).** The small
   real nonnegative bump can satisfy the two strict exponential
   bounds simultaneously, since there are only two evaluation
   points. Its unit integral gives the stated distance from 1
   at each point. Integration by parts makes eta''-eta/4 neutral,
   and its multiplier -z^2-1/4 is nonzero at the selected zeros.
   The resulting a_(z0) is nonzero, with its multiplicity included.
   A large but finite profile norm causes no loss of the prescribed
   M0: it changes epsilon and C_B, not the tested budget.

   The absolute sum of |a_z| is finite by item 1. For real t in
   a compact interval, exp(it z) is bounded by exp(|t|/2);
   hence (13) defines a continuous function and termwise translation
   is legitimate. Under the contradiction assumption (12) bounds
   this entire correlation on t>=0. The Laplace integral and all
   its complex derivatives then converge locally uniformly on
   Re(s)>0. The absolute integral bound before (14) separately
   justifies the zero-sum interchange only on Re(s)>1/2.

   On a compact set |s|<=R, the terms with |z|>max(2R,1) have
   absolute size at most 2|a_z|/|z|<=2|a_z|. Local finiteness
   of Z handles all remaining terms. After removing the selected
   term the same bound applies on a small disk about p=i z0;
   there are no other zero poles in that disk. Thus the entire
   complementary sum is holomorphic there and the residue is
   exactly a_(z0). This controls all other zeros, not a finite
   truncation or a signed remainder assumed favorable.

   The punctured right half-plane is connected: paths with compact
   image meet only finitely many points of the discrete pole set,
   each of which admits a small detour inside the half-plane.
   The identity theorem extends J=G from Re(s)>1/2 to that domain.
   Since Re(p)=-Im(z0)>0, J is holomorphic at p; multiplying the
   equality by s-p in the punctured disk contradicts the nonzero
   residue. This argument needs neither a rightmost zero nor
   distinct phases exp(i ell z).

5. **Quantifiers and eventual transfer.** The contradiction assumed
   nonnegativity for every profile strictly inside the prescribed
   budget and every section with at most two occupied cells.
   Its failure therefore gives one such finite negative section,
   rather than a merely negative limit or a profile outside the
   budget. Its K0 can be taken at least two by padding. Once chosen,
   f, c, U and ||U||_2 remain fixed under every further padding.
   Formula (5) makes the full normalized energy independent of
   the encompassing finite window. The inequality
   R>=exp(exp(K0 ell)) implies floor(log log R/ell)>=K0, including
   equality, as needed. Under RH the same absolute series becomes
   a real-zero sum of nonnegative squares, proving only the stated
   converse. C744q's margin is a comparison, not an input or
   a consequence of this converse.

No failure or changed-scope repair was found. The audit accepts the
conditional detector and its exact fixed-budget transfer. It does not
verify an actual off-line zero, quantify K0 or the negative energy,
or establish the universal low sign. The strict-slack hypothesis
cannot be dropped on the basis of this proof. The remaining positive
margin, non-neutral tests and all-window assembly are unresolved;
this is neither a complete RH candidate nor a disproof.

## Mathlib

Full matching coverage of this fixed-budget train criterion has not
been checked. No absence claim is made. The standard complex-analytic
identity and uniform-limit theorems and Fourier identities are supporting
ingredients, not an asserted formalization of this result. The imported
Weil formula and source-specific generator identification retain the
precise citations and scope given above.
