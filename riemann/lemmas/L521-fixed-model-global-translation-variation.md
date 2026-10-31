# L521 — Fixed-model global translation variation by renewal and localization

## Hypotheses

Retain exactly L520's fixed conditional model. Thus 0<a<A<infinity,
ell=2a, I=(0,ell), and G_I is the smooth-core part operator for

    Psi(xi)=(1/2)log(1+xi^2), n(x)=exp(-|x|)/(2|x|), x!=0.

Use zero extension E and Fourier transform
hat f(xi)=integral_R f(x)exp(-i xi x)dx. The complete finite real
even signed measure and operator are

    c=log(2pi), d_n=log(n), w_n=Lambda(n)/sqrt(n),
    mu=nu_rho+sum_(n>=2,d_n<=2A)w_n(delta_(d_n)+delta_(-d_n))
                         -2cosh(x/2)1_(|x|<=2A)dx,
    rho(x)=exp(-x/2)/(1-exp(-2x))-exp(-x)/(2x), x>0,
    A_I=G_I-cI-R_I K_mu E, Dom(A_I)=Dom(G_I),

where nu_rho has even density rho. Every cutoff-equality atom and
the signed pole remain present. Assume real u in Dom(A_I), A_Iu=0,
and ||u||_2=1. As in L520, assume ell>log(2), nonzero left renewal
trace and absence of a direct reflected-endpoint image at log(2):
log(2)!=ell-d_n whenever w_n>0 and d_n<=2A. These additional
hypotheses are retained even though the estimate below does not use
the nonzero trace or the image separation.

L515 supplies the bounded continuous zero extension f=Eu and the
bounded function G_Iu. L513 supplies its two half-line renewal
representations with the normalized V and positive continuous
decreasing v=V', V(0)=0. L516's full-Weil identification and its
source-manuscript qualification remain unchanged; no actual-Xi
realization or existence of this nullvector is proved here.

This attempt uses the pre-existing EXPLORE gate
`drafts/literature/2026-10-30-weil-global-translation-variation-test.md`.
The known difference-quotient criterion is imported below. The new
local work is closure of its estimate for the complete fixed model;
POTENTIALLY_NEW does not certify originality. The separate conceptual
audit below passes this fixed-model closure; it does not audit the
imported source proofs or enlarge the hypotheses or conclusion.

## Conclusion

There are h_0>0 and C<infinity, depending on the fixed model and u,
such that

    Q_h(f):=||f(.+h)-f||_1/h <= C,             0<h<h_0.       (1)

Consequently f belongs to BV(R). The proof gives a closed estimate
Q_h(f)<=theta Q_h(f)+C_* with theta<=1/2 and C_* independent of h.
It does not differentiate the renewal-trace error or suppose any
translated image is smooth. No uniform bound as a,A or u vary, no
individual prime-correlation formula or sign, and no saving
proportional to an eigenvalue follow. L516's signed cancellation,
trace vanishing, branch/collar arguments and Xi transfer remain open.

## Proof

### Known criterion and finite data

Import Bruno Galerne, *Random fields of bounded variation and
computation of their variation intensity*, Adv. Appl. Probab. 48
(2016), 947–971, Section 2, Lemma 1 and Theorem 1, pp.951–953
([primary publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/83627D38EAB49283AE917366027E8BE7/S0001867816000604a.pdf/random_fields_of_bounded_variation_and_computation_of_their_variation_intensity.pdf)).
For an L1 function on an open domain, finite directional variation
is equivalent to a finite liminf of its L1 translation-quotient
norms on the eroded domain. Here the domain is R and the direction
is 1, so there is no erosion and directional variation is total
variation. L515 supplies f in L1, because it is bounded and supported
in [0,ell]. We prove the stronger uniform estimate (1), rather than
assume the criterion's missing premise. No reproof of this theorem
or of its derivative-measure conclusions is needed.

Put

    B=||f||_infinity, F=||f||_1, M=||mu||_TV,
    b_0=|c|+M, b_1=|c+1|+M,
    H_0=c f+mu*f, H=(c+1)f+mu*f, J=b_0 B.

All are finite. Signed convolution against mu gives, for every h>0,

    ||H_0||_infinity<=J, ||H||_1<=b_1 F,
    Q_h(H_0)<=b_0 Q_h(f), Q_h(H)<=b_1 Q_h(f).              (2)

These are inequalities, not replacements of the model by |mu|.
In particular every actual translation remains inside H_0 and H.
Each Q_h(f) is finite before any estimate, since it is at most 2F/h.
For any bounded Lipschitz multiplier alpha and z in L1,

    Q_h(alpha z)<=||alpha||_infinity Q_h(z)
                         +||alpha'||_infinity ||z||_1.     (3)

This follows by adding and subtracting alpha(x+h)z(x) under the
integral. For the indicator of a finite interval J_0 the same
calculation, using the symmetric difference of its two translates,
gives for bounded z

    Q_h(1_(J_0) z)<=Q_h(z)+2||z||_infinity.               (4)

### Renewal representation in a left collar

Choose for now 0<delta<ell/4. Let g be L513's signed half-line
forcing for the extension of u by zero to (ell,infinity):

    g(y)=H_0(y), 0<y<ell,
    g_e(y)=-integral_0^ell n(y-z)u(z)dz, y>ell.

By L513 (8)–(9), G_e:=||g_e||_(L1(ell,infinity))<=B/2.
Write g_i=1_I H_0, extended by zero to R. Equations (2) and (4)
give

    Q_h(g_i)<=b_0 Q_h(f)+2J.                              (5)

For 0<z<delta define

    b_i(z)=integral_0^ell v(t)g_i(z+t)dt,
    b_e(z)=integral_ell^infinity v(y-z)g_e(y)dy,
    b(z)=b_i(z)+b_e(z).

The first formula defines b_i on all of R as convolution with an
L1 kernel of norm V(ell). Thus

    ||b_i||_infinity<=V(ell)J,
    Q_h(b_i)<=V(ell)[b_0 Q_h(f)+2J].                       (6)

For 0<z<delta, monotonicity of v bounds |b_e(z)| by
v(ell-delta)G_e. L513's kernel factorization gives, almost
everywhere for 0<x<delta,

    f(x)=integral_0^x v(x-z)b(z)dz.                        (7)

Here is the requisite absolute interchange. In L513 (4), first
integrate over 0<z<min(x,y); reversing the y,z integration produces
integral_z^infinity v(y-z)g(y)dy. Its interior absolute part is
at most J V(ell), and its exterior absolute part is at most
v(ell-delta)G_e. The resulting integral is at most
V(x)[J V(ell)+v(ell-delta)G_e]. Tonelli for absolute values,
followed by Fubini, therefore justifies (7) with signed g. The
almost-everywhere potential identity near zero is exactly the one
proved in L513; it suffices for all L1 statements here.

To control the exterior part after cutoff, fix y>ell and define
beta_y(z)=v(y-z) on (0,delta), and zero elsewhere. It is increasing
inside its support. If 0<h<delta, its only negative difference
beta_y(z+h)-beta_y(z) is on (delta-h,delta); the total integral
of the difference is zero. Hence

    ||beta_y(.+h)-beta_y||_1
       =2 integral_(delta-h)^delta v(y-z)dz
       <=2h v(ell-delta).

If h>=delta, use disjoint supports and
2||beta_y||_1<=2delta v(ell-delta)<=2h v(ell-delta).
Integrating against |g_e(y)| proves

    Q_h(1_(0,delta)b_e)<=2v(ell-delta)G_e.                 (8)

No variation or derivative of u, g_e or the trace remainder is used.
For b_delta=1_(0,delta)b, (4), (6) and (8) now give

    Q_h(b_delta)<=V(ell)b_0 Q_h(f)+C_b,
    C_b=4V(ell)J+2v(ell-delta)G_e,
    ||b_delta||_1<=delta D_b,
    D_b=V(ell)J+v(ell-delta)G_e.                           (9)

Let v_delta=1_(0,delta)v, an L1 kernel of norm V(delta), and
F_L=v_delta*b_delta on R. On (0,delta) it equals f by (7),
and both functions vanish on the negative half-line. Choose a smooth
nonincreasing alpha_L with 0<=alpha_L<=1, equal to 1 on
(-infinity,delta/2] and 0 on [delta,infinity). Then alpha_L f
equals alpha_L F_L almost everywhere on R. Young's inequality and
(3),(9) yield

    Q_h(alpha_L f)<=V(delta)V(ell)b_0 Q_h(f)+C_L,
    C_L=V(delta)[C_b+||alpha_L'||_infinity delta D_b].       (10)

All constants are finite and independent of h. The factor V(delta)
multiplies the only unknown quotient norm; it is not obtained by
differentiating a pointwise asymptotic.

### Right collar and a fixed interior cutoff

Apply the same argument to f(ell-x). The even measure mu and the
part operator commute with this reflection, and L515/L513 supply
the reflected half-line split and renewal representation. The
same B,F,J,b_0 and V apply; the exterior L1 norm is again at most
B/2. Set alpha_R(x)=alpha_L(ell-x). The result is

    Q_h(alpha_R f)<=V(delta)V(ell)b_0 Q_h(f)+C_R.           (11)

Reflection preserves the quotient norm (positive and negative
translation lengths have equal L1 norm). A common finite upper
bound for C_L,C_R is obtained in (9)–(10) by replacing G_e by B/2.

Now set chi=1-alpha_L-alpha_R. Since delta<ell/4, these collar
cutoffs have disjoint transitions, 0<=chi<=1, and
chi belongs to C_c^infinity(I). Globally,

    f=alpha_L f+chi f+alpha_R f.                           (12)

Choose and fix delta sufficiently small that

    theta_E=2V(delta)V(ell)b_0<=1/4.                      (13)

This is possible by V(delta)->0, with ell and b_0 fixed. The
derivatives of chi can now be large but finite; the remaining
frequency choice will be made after this spatial choice.

### A small L1 high-frequency inverse

Use L520 (4)–(8): P=(1+G)^(-1) has a nonnegative kernel p in L1(R)
with integral p=1. Its explicit resolvent computation and all
Fourier conventions are those of L520; no zero-energy Green
potential is substituted. Choose the smooth cutoff eta of L520,
and set, for N>=1,

    eta_N(xi)=eta(xi/N), e=F^(-1)eta, e_N(x)=N e(Nx),
    K_N=p-e_N*p, k_N=||K_N||_1.

The Schwartz kernel e has integral eta(0)=1. Consequently

    k_N<=integral_R |e(z)| ||p(.)-p(.-z/N)||_1 dz ->0.     (14)

For fixed z, L1 translation continuity of p gives convergence;
2||p||_1 |e(z)| is an integrable dominator. One can use L520's
explicit kernel-translation bound for that continuity. This proves
smallness in the operator norm needed here; decay of the multiplier
alone would not justify (14). Also ||e_N'||_1=N||e'||_1<infinity.

### The commutator's relative quotient estimate

For this fixed chi, L520's exact localization commutator is

    C_chi f(x)=integral_R [chi(x)-chi(x-r)]n(r)f(x-r)dr.

Define the finite constants

    A_chi=integral_R min(||chi'||_infinity |r|,
                         2||chi||_infinity)n(r)dr,
    B_chi=integral_R min(||chi''||_infinity |r|,
                         2||chi'||_infinity)n(r)dr.        (15)

Finiteness follows from n(r)~1/(2|r|) at zero and its exponential
tail. The commutator is in L1 with norm at most A_chi F. To take
its difference, write a(x,r)=chi(x)-chi(x-r) and use the identity

    a(x+h,r)f(x+h-r)-a(x,r)f(x-r)
      =a(x+h,r)[f(x+h-r)-f(x-r)]
                         +[a(x+h,r)-a(x,r)]f(x-r).

The first coefficient is bounded by the integrand defining A_chi,
before multiplication by n. The second is bounded by h times the
corresponding coefficient defining B_chi, by the mean value theorem
applied to chi'. Integrating absolute values in x,r proves

    Q_h(C_chi f)<=A_chi Q_h(f)+B_chi F.                    (16)

All Fubini uses are justified by these finite majorants for each
fixed h. This bound retains the rough f in the commutator. An
absolute O(h log(1/h)) modulus alone would not close the argument.

### Interior closure and absorption

The weak equation on I is (1+G)f=H. L520's form-localization and
L2 inversion, with chi in C_c^infinity(I), give

    (1+G)(chi f)=chi H+C_chi f,
    chi f=K_N*(chi H+C_chi f)+e_N*(chi f).                 (17)

This is the same identity for any eta_N. Its use requires no
global operator-domain assertion for the unlocalized f. All terms
on the right are also in L1: chi H is in L1, the commutator was
bounded above, and K_N,e_N are in L1. Thus the L2 identity is
legitimately used in L1 translation estimates. By (2),(3),(16),
Young's inequality and the integrable derivative of e_N,

    Q_h(chi f)<=k_N(b_1+A_chi)Q_h(f)+C_M,
    C_M=k_N[||chi'||_infinity b_1+B_chi]F
                              +||e_N'||_1 F.              (18)

The low-frequency bound follows from
||e_N(.+h)-e_N||_1<=h||e_N'||_1; ||chi f||_1<=F.
With delta already fixed, use (14) to choose one finite N such that

    theta_M=k_N(b_1+A_chi)<=1/4.                          (19)

There is no requirement that the cutoff derivatives stay bounded
as delta tends to zero; delta no longer varies when N is chosen.
Combining (10)–(13),(18)–(19) gives, for every 0<h<delta/2,

    Q_h(f)<=theta Q_h(f)+C_*,
    theta=theta_E+theta_M<=1/2,
    C_*=C_L+C_R+C_M<infinity.                            (20)

Because Q_h(f)<infinity for each h, subtracting theta Q_h(f) is
valid without already knowing a uniform bound. Hence
Q_h(f)<=2C_*; take h_0=delta/2 and C=2C_* in (1).
The cited deterministic theorem of Galerne now implies f in BV(R).

Every prime-power atom, possible coincident image and signed density
was retained in mu throughout (2), (5), (17) and (18). No partition
avoiding those images is used. Only the spatial endpoints require
the renewal representation, and their collars were handled with
signed forcing and its full exterior contribution. The result is
conditional finite variation of one fixed nullvector, not the
eigenvalue-relative arithmetic inequality or a complete RH candidate.

### Independent conceptual audit, 2026-10-30

The pre-existing EXPLORE assessment is
`drafts/literature/2026-10-30-weil-global-variation-closure-audit-coverage.md`.
This audit checks (2)–(20), including their applications of the
previously audited local inputs. They pass without a change to the
estimates or dependencies. The resulting coefficient is theta<=1/2,
against the required strict absorption threshold theta<1. This is
verification of L521's conditional result, not a strengthened theorem,
an independent source-manuscript audit, or certified originality.

**Finite data and signed renewal inversion.** The model measure is
finite: its atomic sum is finite, the pole is cut off on a bounded
interval, and the even density rho is bounded at zero and decays
exponentially at infinity, as checked in L520. L515 supplies bounded
u and G_Iu and both half-line operator-domain splits. L513 therefore
applies to this actual signed forcing. Its normalized v includes its
nonzero constant at infinity; no decay of v is used here. The
estimate G_e<=B/2 is precisely L513's absolute cross integral.

The kernel defining b_i on R is v(-s)1_(-ell,0)(s), whose L1 norm
is V(ell). On 0<z<delta its integral to ell equals the interior
part of integral_z^infinity v(y-z)g(y)dy: g_i vanishes once
z+t>=ell. The interior absolute integral is bounded by J V(ell).
For the exterior, y-z>=ell-delta, so decreasing v and g_e in L1
give v(ell-delta)G_e. Integrating these bounds against v(x-z)
on 0<z<x gives a finite multiple of V(x). This verifies the
absolute Fubini step even though the original potential kernel can
have an infinite diagonal. The potential equals f almost everywhere
on (0,ell/4) by L513; delta<ell/4 keeps all of (7) in that range.

**Sharp cutoffs and both collars.** For h<delta, beta_y(x+h)-beta_y(x)
is nonnegative on (-h,0) and (0,delta-h), nonpositive on
(delta-h,delta), and zero elsewhere. Its integral is zero since
beta_y is integrable. Thus its absolute integral is exactly twice
the integral lost at the right cutoff. When h>=delta the supports
are disjoint up to null endpoints. Both cases give (8); the left
jump is included, not suppressed. Integrating this estimate against
|g_e| is legitimate by Tonelli. The other sharp cutoff contributes
2||b_i||_infinity, in addition to the 2J already present in (5).
This gives exactly C_b=4V(ell)J+2v(ell-delta)G_e in (9).

The equality alpha_L f=alpha_L(v_delta*b_delta) holds globally:
on (0,delta) it is the potential identity, both sides vanish for
x<0, and alpha_L vanishes for x>=delta. The L1 norm of the
convolution is at most V(delta)delta D_b. Hence the multiplier
error in (10) is finite without differentiating f or a trace
remainder. Reflection preserves both the equation and quotient
norm; the reflected exterior estimate is again B/2. With
delta<ell/4 the two transitions do not overlap and
chi=1-alpha_L-alpha_R is smooth and supported strictly inside I.
The decomposition (12) therefore holds on all of R. As V(delta)
tends to zero, (13) fixes one positive delta and finite cutoff
derivatives before any frequency choice.

**L1 inverse, commutator and domains.** L520 supplies p in L1 with
mass one. Under the stated Fourier convention integral e=eta(0)=1
and hat(e_N*p)=eta_N/(1+Psi). Consequently K_N=p-e_N*p is exactly
the kernel of (1-eta_N(D))(1+G)^(-1), with no extra Fourier factor.
The integral bound (14), dominated by 2||p||_1|e|, proves
k_N->0 in L1; no positivity of e or multiplier-to-L1 inference
is needed. The singularity of p at zero is allowed by its L1 norm.

For the commutator, |a(x,r)| has the first bound in (15), and
|partial_x a(x,r)|=|chi'(x)-chi'(x-r)| has the second. Integration
of the latter over a segment of length h bounds the second
difference term in (16). Both majorants are O(|r|) at zero and
bounded at infinity before multiplication by n(r). Thus they are
integrable. Translating the first difference of f under the x
integral gives exactly A_chi Q_h(f); the other gives B_chi F.
This keeps the unknown quotient on the right and assumes no BV.

The distributional localization from L520 is applicable because
f is in the whole-line form domain and chi has compact support in
I. Multiplication by chi preserves that domain. The commutator
also belongs to L2, since |C_chi f| is bounded by the convolution
of |f| with the integrable first majorant in (15); chi H is in L2.
Therefore (1+G)(chi f)=chi H+C_chi f has an L2 right side and
places chi f in the full multiplier operator domain. L2 inversion
and its decomposition by eta_N give (17). All terms are also in
L1 by the estimates above, so the same almost-everywhere identity
supports the L1 quotient calculation. No global operator-domain
claim for the unlocalized f is required.

**Absorption and scope.** Applying (3) to chi H gives the error
||chi'||_infinity b_1 F; (16) gives B_chi F. The low-frequency
term costs ||e_N'||_1 F. These are exactly the finite errors in
(18). For the already fixed delta, A_chi is finite and (14)
permits one finite N satisfying (19). Hence theta_E<=1/4 and
theta_M<=1/4 hold simultaneously. Every Q_h(f)<=2F/h is finite
before subtraction, so (20) yields Q_h(f)<=2C_* uniformly for
0<h<delta/2. Galerne's quoted one-dimensional criterion now
applies to the integrable zero extension on R; the positive-shift
convention is harmless because the two translation norms agree.

Every cutoff-equality atom and both signed densities occur in the
same H_0 and H throughout. The constants depend on the fixed data;
this audit proves no uniform family bound, individual prime limit,
sign or O(lambda) saving. The nonzero-trace and image-separation
assumptions remain as stated, although these estimates do not use
them. Nullvector existence, full-Weil identification and Xi transfer
are still separate unresolved assumptions. Mathlib matching and the
imported manuscript proofs retain their earlier qualifications.

## Mathlib

Full matching coverage of this signed translated-model BV closure
has not been checked. No absence claim is made. Galerne's specific
criterion is the imported BV input; L513/L515/L516/L520 retain
their source and Mathlib qualifications. Supporting facts used with
their hypotheses above are Young's inequality, Tonelli/Fubini,
dominated convergence, and the smooth approximate-identity argument.
No Mathlib formalization or independent source-manuscript audit is
claimed.
