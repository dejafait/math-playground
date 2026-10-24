# L266 — Complete joint cubic probe-jet quantitative assembly

## Hypotheses

Use the identical setting of L181--L186, L193, L211, L264 and L265:
SU(2) in the relative cube (-4,4)^4, sufficiently fine admitted even
N, a=8/N, tau=1/16, the straight lower-rooted direction-1 forest,
the complete fixed compact displacement, and both actual probes i=3,6.
Take the bare small-coupling expansion at each fixed mesh before
refinement. Use ordinary dimensionless stored full-variable-link
coordinates and adjoints. Fixed boundary links have zero coordinates;
all variable normal end edges, source rows, physical faces, allowed
constant own-direction modes and complete probe heat sums remain.
Every vertex potential has its actual boundary pins, including the
upper pinned jump of the forest retraction.

Keep the definitions in L182--L184 and L193:

    D=D_0, L=D_1^T D_1, Delta=L+DD^T,
    P=1-D(D^T D)^(-1)D^T, S=P Delta^(-1)P,
    R=1-D Phi, x=pi_F Rz, z~N(0,S) in three independent colors,
    A=PAP=A^T, B_i=PB_iP=B_i^T, t(z)=2SAz,
    b(z)=[z,q Phi z]/2-[D Phi z,q Phi z]/4,
    J_i(z)=2<B_i z,b(z)>, W(z)=P db(z)[t(z)],
    rho_H=script R_3-d script S_3[t(z)],
    rho_F(z)=rho(pi_F Rz)=rho_H(z)-<Lz,W(z)>.

Here (q phi)_e=phi_tail+phi_head and [v,w]=-v cross w.
The complete residual includes both insertion subtractions. Within a
color, both prefixes and the direct fields are correlated. Neither A
nor the tilted covariance M=2SAS is assumed positive or commuted with
another factor. Write F_i(z)=F_(i,3)(z) for L193(1)'s complete cubic
flowed numerator on the co-closed input; it includes its observable
jet and its entire quadratic-flow integral on [0,tau]. This is not
F_(i,3)(Rz).

Let Q_(1,i,N), Q_(2,i,N), Q_(3,i,N) be exactly the three signed
placements in L184(5), with their existing color normalization.
Import the complete quantitative bounds L265(3), L264(7), L186(2),
L185(2) and L211(3), with every stated analytic and pending upstream
audit qualification. Their proofs are not independently audited here.

## Conclusion

For the original normalized joint cumulant group,

    G_(i,a)=kappa_0(f_(i,1),r_1)
                         -kappa_0(f_(i,1),r_0,S_3),

there exist C_i<infinity and a common admitted-mesh threshold N_0
such that, for i=3,6 and all admitted even N>=N_0,

    |G_(i,a)|<=C_i N^(5/2)log(eN)^2.                    (1)

In particular |a^3 G_(i,a)|<=512 C_i N^(-1/2)log(eN)^2,
which tends to zero. This quantitatively strengthens the already
established zero cubic limit for this selected group. It is local
REPRODUCTION by finite assembly of imported estimates, without a
claim of progress beyond the standard methods in the checked sources.
The separate critical audit below accepts this assembly relative to
its imported premises. It supplies no
independent H/Q_tr limits, transverse-H rate, complete quantitative
L011 estimate, interacting reflected-error bound, continuum theory
or infrared mass gap. All upstream qualifications remain in force.

## Proof

### 1. Identify the original response before taking absolute values

L181(3)--(5) gives the exact normalized-cumulant identity

    G_(i,a)=E_0[f_(i,1)rho],
    rho=r_1-dS_3(x)[2 Sigma_F A_F x].                  (2)

This imports the single-action cumulant subtraction, including its
connected normalization, in its original covariance order. In this
convention there is no extra factor 3 or 1/2. L182(6), with its
Gaussian representation x=pi_F Rz, then gives exactly

    G_(i,a)=E_S[F_i(z)rho_F(z)]
                         +E_S[J_i(z)rho_F(z)].        (3)

The identification F_i=F_(i,3) on the co-closed input is L193(1).
Thus the first term in (3) is exactly the object in L265(3), including
the final observable, the complete rho_H Duhamel pairing, and all
three W derivative placements through both flow endpoints. In
particular it is not only E[F_i rho_H]. None of its intermediate
errors or final-observable allowances is another summand of (3).

For the second term alone, L183(6) states

    E_S[J_i rho_F]=E_S[J_i rho_H]-E_S[dJ_i(z)[W(z)]].   (4)

Its quartic is precisely the whole expression

    E_S[dJ_i[W]]
      =2E_S{<B_i W,b>+<B_i z,db(z)[W]>}
      =Q_(1,i,N)+Q_(2,i,N)+Q_(3,i,N),                (5)

where the last equality is L184(4)--(5). In particular the derivative
acts on J_i, not on W; both differentiated prefixes and the composed
prefix in this quartic are already present. Combining (3)--(5) yields
the finite signed partition

    G_(i,a)=E_S[F_i rho_F]+E_S[J_i rho_H]
                -Q_(1,i,N)-Q_(2,i,N)-Q_(3,i,N).       (6)

All identities precede mesh limits and absolute values. L194(4)--(5)
is an alternative regrouping of the same prefix sextic minus quartic,
not an additional response term; it is mentioned only for contrast.
Its rough-action common trace and Q_3 must not be added to (6) again.

### 2. Match complete allowances and choose one threshold

Put ell_N=log(eN). The complete bounds on the five terms in (6) are

    |E_S[F_i rho_F]|
       <=c_(F,i)[N^2 ell_N^(5/4)+N^(5/2)ell_N],
    |E_S[J_i rho_H]|<=c_(J,i)N^(5/2)ell_N^(1/2),
    |Q_(1,i,N)|<=c_(1,i)N^(5/2),
    |Q_(2,i,N)|<=c_(2,i)N^(3/2),
    |Q_(3,i,N)|<=c_(3,i)N^(5/2).                      (7)

These are respectively L265(3), L264(7), L186(2), L185(2) and
L211(3). Their domains coincide with the hypotheses above. In
particular L264 bounds the complete sextic, including the smooth-tilt
action placement; no separate L194 allowance is added. L186 bounds
all four signed minors in Q_1. L185 applies to the original Q_2 with
M adjacent to B_i, without assigning its smoothness to another slot.
L211 bounds the complete original-covariance Q_3, including its axial
diagonal and projection correction; its intermediate mixed trace is
not a sixth summand. The correlated prefixes, upper jump, both Q
forms, all normal end rows and complete heat sums remain within
these imported complete estimates.

For each probe and each of the five imported inequalities, choose
its asserted finite admitted-mesh threshold. Let N_0 be the maximum
of these ten thresholds and 8, enlarged if necessary so that their
common sufficiently fine geometric hypotheses hold. The same fixed
box, displacement, tau and two probe forms are used in every input,
so this finite maximum is valid. Choose the finite constants in
(7) for N>=N_0; they are independent of N.

Now take absolute values in (6). Since N>=1 and ell_N>=1, each of
N^2 ell_N^(5/4), N^(5/2)ell_N, N^(5/2)ell_N^(1/2), N^(5/2)
and N^(3/2) is at most N^(5/2)ell_N^2. Thus (7) proves (1) with

    C_i=2c_(F,i)+c_(J,i)+c_(1,i)+c_(2,i)+c_(3,i).

No sign or positivity of a response is needed. Multiplication by
a^3=512/N^3 gives the stated normalized rate, and the elementary
limit N^(-1/2)log(eN)^2->0 completes the conclusion.

### 3. Scope and known traps checked

This is a finite signed assembly followed by a finite-sum inequality.
It uses no full-forest residual norm, termwise forest-to-Hodge
transfer, independence of within-color prefixes, rough-prefix
smoothness, covariance commutation or qualitative-limit rate
inference. ATTEMPTS/043's absolute full-residual norm failure is a
different estimate and remains preserved. No varying cutoff, mass
or short-time limit is introduced. Color factors, the normalized
cumulant subtraction, the negative quartic sign and all five slots
are inherited once from the exact identities. The component audits
of L211, L264 and L265 accept their respective conclusions relative
to imports; this assembly does not extend those verdicts upstream.
No L220 cancellation or numerical heat enclosure is used to obtain
(1). No mathematical script or numerical diagnostic is needed for
this finite assembly. Its separate critical audit is recorded below.

### Separate critical audit, 2026-10-23

The prior SPECIALIZE assessment
`drafts/literature/2026-10-23-joint-cubic-probe-assembly-critical-audit.md`
authorizes this finite assembly audit. The audit accepts (1) relative
to the stated imported analytic and upstream audit premises. No new
kernel estimate, component rate, direct mathematical input or stronger
conclusion is needed. The following reconstruction checks the argument
at the interface between its exact identities and complete estimates.

**Normalized original response.** At fixed mesh let f=f_(i,1),
s=S_3 and r=r_0. The color-alternating cubics f and s have zero
means, also under the normalized quadratic tilt by exp(u r).
Thus their third cumulant is

    kappa_0(f,r,s)=E_0[frs]-E_0[r]E_0[fs]
                 =d/du E_u[fs] at u=0.

L181(7)--(9) uses Sigma_F'(0)=2 Sigma_F A_F Sigma_F.
In each surviving cubic cross-pairing, placing
T_F=2 Sigma_F A_F on its action endpoint inserts
Sigma_F T_F^T=2 Sigma_F A_F Sigma_F, exactly that derivative.
The three differentiated cross lines are already the three slots of
ds[T_F x]. The two cubic tensor normalizations, six cross matchings
and color sum give 6*6/36=1. Consequently the original subtraction
is E_0[f(r_1-ds[T_F x])], with no extra 3 or 1/2. The calculation
uses the named Isserlis theorem cited below, not an unnormalized
Gaussian moment in place of the connected cumulant.

**Retraction and the signed five-term partition.** L182(8) gives
R S R^T=I_F Sigma_F I_F^T and I_F x=Rz. It therefore preserves
the forest law for the entire polynomial, without transferring
either nonlinear jet separately. Its exact gauge-jet identity gives
F_(i,3)(Rz)=F_i(z)+J_i(z), since
2<B_i z,b>=J_(i,1)-J_(i,2)/2. L193(1) confirms that F_i is
the complete co-closed cubic, including the whole flow integral.

For the residual, L183(7) lifts the original direction as
I_F T_F x=R(2SAz), using AR=A and R^T A=A in that order.
Differentiation of the retracted action produces
<Lt,b>+<Lz,db[t]>. Since Lt=2Az, its first term cancels
the residual's +2<Az,b> exactly. The remaining identity is
rho_F=rho_H-<Lz,W>, with W=P db[t]. On im P the Gaussian
inverse is L and div W=0: its diagonal color derivatives vanish
by antisymmetry, even with the nonlocal prefixes. L183(13) thus
gives E[J_i<Lz,W>]=E[dJ_i[W]]. This fixes the negative quartic
sign. There is no derivative of W left over. The other pairing
E[F_i rho_F] is kept whole, including its own W response.

L184(4)--(5) contracts precisely this dJ_i[W]. Its two crossing
fourth-moment pairings have color sums +6 and -6; skewness changes
the latter sign back to plus. Together with the two factors 1/2,
this gives 3; the two differentiated b inputs then give 6.
Expanding h's three probe-leg placements gives the three factors
12 in L184(5), already built into Q_1,Q_2,Q_3. The Q_1 wedge
expansion has coefficient 12/4=3 and all four signed minors, exactly
L186(1). The other two contractions contain MB and SB, respectively,
exactly L185(1) and L211's original-covariance Q_3. This checks
that neither a color factor nor a placement is missing from (6).

**Complete bounds, without counting intermediate errors twice.**
L265(3) is a bound for E[F_i rho_F], not E[F_i rho_H] alone.
Its proof section 4 includes the entire rho_H integral, the
external W placement, the combined two short-output placements,
and the final observable with its W derivative. Those latter
allowances are internal to the first slot in (6).
L264(19)--(20) bounds exactly E[J_i rho_H]. Its derivative
contains d script R_3, both rough action-slot derivatives and
the derivative of Tz; both bracket orders and both residual
subtractions are already included. No separate smooth-tilt term
from L194 is added. L185(2) and L186(2) bound the complete
second and first placements; their return-to-response counts
retain the actual a^2-weighted heat matrices. L211(3) bounds
the original complete Q_3. Its proof section 5 has already
combined the axial O(N^(5/2)), projection O(N^2 sqrt(log(eN)))
and mixed O(N^2) allowances. None is a sixth slot. In particular
L211's separate qualitative statement about G is not used as a
quantitative estimate for G. This independently matches every
entry of (7) to a complete statement.

**Shared domain and final inequality.** Each statement uses the
same relative cube, a=8/N, admitted even meshes, tau=1/16,
lower-rooted direction-1 forest and stored dimensionless adjoints.
They concern the same fixed displacement and actual triplet/shear
forms, retaining correlated prefixes, the upper pin, both residual
Q forms, every source/end row, constant modes and full heat sums.
The finitely many sufficiently-fine hypotheses therefore admit
the maximum threshold in section 2. Constants depend on the fixed
data and probe, never N. For N>=N_0>=8, division of the five
types of allowance by N^(5/2)ell_N^2 yields respectively
N^(-1/2)ell_N^(-3/4), ell_N^(-1), ell_N^(-3/2),
ell_N^(-2) and N^(-1)ell_N^(-2); each is at most one.
The first component has two allowances, so its constant is counted
twice in C_i, as stated. Multiplication by a^3=512/N^3 then
gives the claimed vanishing rate. No cancellation, positivity or
interchange of mesh and time limits is needed in this last step.

The audit validates the existing local assembly, not progress beyond
the checked source methods. L264/L265's and L211's component verdicts
remain relative to imports; L185/L186 and all other analytic premises
are not recursively audited here. ATTEMPTS/043's full-residual
absolute-norm failure remains intact and is unused. No new script
or numerical evidence is needed. The transverse-H rate, complete
quantitative L011 assembly, interacting comparison and continuum/
infrared construction remain unresolved. The original DAG is unchanged.

## Mathlib

Full matching joint-probe theorem: **not checked**. Supporting finite
Gaussian, cumulant and elementary finite-sum/logarithm coverage:
**not checked**; unknown availability is not absence. The Gaussian
pairing used in the imported exact identities is Isserlis' theorem,
precisely H. Z. Munthe-Kaas, O. Verdier and G. Vilmart, *A short proof
of Isserlis' theorem*, author PDF dated 7 March 2025, Theorem 1,
p. 1, and Theorem 4, p. 3
([primary PDF](https://www.unige.ch/~vilmart/paper_isserlis.pdf)).
The singular-covariance specialization and color factors are already
justified in the imported lemmas; no pairing theorem or kernel rate
is reproved. The only additional argument is the explicit finite
partition, scope matching and common-threshold inequality required
by the unchanged approved assembly assessment. General renormalized
gradient-flow results are not substituted for this selected bare
group, and no originality claim is made.
