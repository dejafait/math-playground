# L188 — A skew commutator split does not remove the prefix transport

## Hypotheses

For the actual third placement use exactly L187's hypotheses and
notation: SU(2), relative box (-4,4)^4, admitted even N, a=8/N,
straight direction-1 lower-rooted forest, both complete L010 probes
at tau=1/16, and bare expansion before refinement. Full variable-link
coordinates retain every normal end edge, and all vertex potentials
are pinned on every physical face. Keep S, P, the complete signed
residual A=PAP with both insertion subtractions, M=2SAS, V=q Phi,
H=1-D Phi/2, R=1-D Phi and mathcal J_y as in L187.

For a rank-one summand SB=n y^T, put

\[
 J=P\mathcal J_yP,\quad \alpha=Vn,\quad \beta=Rn,
 \quad Z=P\operatorname{diag}(\alpha)P,
 \quad C=P\operatorname{diag}(\beta)VP.                 \tag{1}
\]

In particular J is skew, Z and M are symmetric, and C need not be
symmetric. The commutator convention is [M,Z]=MZ-ZM.

The separate fixture below tests only identities following from
pinned incidence, prefix, projection, covariance support and symmetry.
Its S, A and B are synthetic; they are not the actual residual,
Hodge covariance or either L010 probe. It is not an admitted-mesh
asymptotic example.

## Conclusion

L187's entire rank-one third placement has the exact split

\[
 \boxed{\mathcal Q_3(n,y)
 =-3\operatorname{Tr}(J[M,Z])
  +3\operatorname{Tr}\bigl(J(MC^T-CM)\bigr).}           \tag{2}
\]

If alpha is constant over the full link index set, the first term
vanishes. This does not remove the second term: the explicit all-end-row
pinned-incidence fixture below has a symmetric supported B, constant
alpha for each of its two rank-one summands, and total Q_3=-3/8.
Thus skewness, covariance symmetry and cyclicity alone cannot give
universal cancellation of the complete placement, even with the pinned
product identity retained. An actual residual-specific cancellation is
not excluded.

No stronger all-mesh estimate follows. The actual-probe bound remains
L187's O(N^(7/2)), above the required O(N^3). This fixture supplies no
actual-probe growth, sign or failure of convergence. The finite scaled
joint response, sextic partner, co-closed flow down to zero time,
independent f_(i,2),r_0 contribution, finer asymptotics, finite matching,
interacting reflected error <=c_box/2 and continuum/infrared construction
remain unresolved. This is standard finite linear algebra specialized
to an assessed tensor, not a claim of discovery beyond checked sources.

## Proof

### 1. Preserve the exact signed order before using skewness

L187(3),(6) imply

\[
 P U_n P=Z-C,\qquad
 \mathcal Q_3(n,y)=-6\operatorname{Tr}(J M(Z-C)^T).
                                                               \tag{3}
\]

Indeed M=PMP and cyclicity allow a P on the final output and both
sides of mathcal J_y. Multiplying L187's exact projected product
identity on the right by P gives the first equality. This uses the
full pinned incidence; no upper row is deleted. Since Z=Z^T,
(3) equals -6 Tr(JMZ)+6 Tr(JMC^T).

For real finite matrices, taking a transpose inside a trace and
then cycling gives

\[
 \operatorname{Tr}(JMZ)=-\operatorname{Tr}(JZM),\qquad
 \operatorname{Tr}(JMC^T)=-\operatorname{Tr}(JCM).
\]

Here only J^T=-J and M^T=M, Z^T=Z are used. Averaging each pair
proves (2), with all signs and the factor 3 retained. If alpha=c is
constant, Z=cP and M=PMP imply [M,Z]=0. The second bracket in (2)
is also skew; a trace of two skew matrices need not vanish.

### 2. A complete symmetric-probe fixture with nonzero transport

Take eight normal edges around one interior vertex, ordered lower,
upper in directions 1 through 4. Write e_j for the eight standard
unit vectors, indexed 0 through 7. Put

\[
 d=(1,-1,1,-1,1,-1,1,-1)^T,\quad D=d,
 \quad q=\mathbf1,\quad \Phi=e_0^T,
 \quad P=I-dd^T/8.                                      \tag{4}
\]

All boundary vertex values are zero. The upper and lower normal
edges are both present, so PD=0. These are the one-interior-vertex
relative incidence and the lower-rooted direction-1 prefix. Define

\[
 n=e_0+e_1,\quad y=e_2+e_3,\quad t=Pe_2,
 \quad S=P,\quad M=tt^T,\quad A=M/2,
 \quad B=ny^T+yn^T.                                    \tag{5}
\]

Then n,y,t are co-closed, S is a positive supported covariance,
2SAS=M, and B=PBP=B^T. In particular SB=B has both rank-one
summands in (5). This checks the full symmetric B, rather than one
unmatched rank-one term. The actual covariance/residual/probe
restrictions have deliberately not been imposed on (5).

Here V=mathbf1 e_0^T and H=I-de_0^T/2. For any co-closed yy,
yy^T d=0 gives

\[
 \mathcal J_{yy}=-\tfrac12(yy e_0^T-e_0 yy^T),\qquad
 P\mathcal J_{yy}P=-\tfrac12(yy(Pe_0)^T-(Pe_0)yy^T).
                                                               \tag{6}
\]

For the first summand (n,y), alpha=mathbf1 and beta=n-d.
Thus Z=P and the multiplication commutator is zero. Since
t_0=-1/8, y^T t=1 and (Pe_0)^T t=-1/8, equation (6) gives

\[
 Jt=y/16+Pe_0/2,\qquad
 PU_n t=P(t-(n-d)t_0)=t+n/8.                            \tag{7}
\]

As J is skew, t^T Jt=0. Also n^T y=0 and n^T Pe_0=1. Hence

\[
 \mathcal Q_3(n,y)
 =-6(PU_n t)^T Jt=-6/16=-3/8.                          \tag{8}
\]

For the second summand (y,n), alpha=0 and beta=y, so Z=0.
Equation (6), now with yy=n, gives Jt=n/16, since n^T t=0.
The projected product identity gives PU_y t=y/8. As n^T y=0,
this summand contributes zero. Both multiplication commutators vanish,
and the complete symmetric B third placement is therefore -3/8,
entirely in the retained prefix-transport branch.

### 3. Verification, qualifications and the remaining estimate

Run from the notebook:

    python3 scripts/combined-ward-response/check_probe_quartic_skew_split.py

The exact Fraction certificate is
`scripts/combined-ward-response/probe-quartic-skew-split-certificate.json`.
Both original traces agree exactly with (2), and P U_n P=Z-C is
checked in each summand. The full fixture and both checks were
inspected in full. The analytic rational calculation (4)--(8) supplies
the proof independently of those finite checks.

For actual heat-mode columns, constant alpha is only a hypothetical
test. L187(15) retains an O(N) upper pinned jump in beta, and its
prefix alpha is not a constant full-link field. Neither [M,Z] nor
MC^T-CM has a smaller norm or a controlled scaled limit here.
Moving M past a variable multiplier without a commutator estimate
would replace the question by an unproved hypothesis. The old absolute
count in ATTEMPTS/040 remains stopped; this new test stops only
universal cyclic removal, not actual-probe tensor cancellation.

### 4. A later paired test is inconclusive, including with compatible cubic jets

The one-vertex example above cannot refute cancellation of the *whole*
quartic or L183's paired expression. In that example q phi has the
same color vector phi on every edge, and D phi=d phi. Thus
[D phi,q phi]=0 and b_e=[z_e,phi]/2. For symmetric B,

    J=2<Bz,b>=sum_(e,g) B_eg <z_g,[z_e,phi]>=0.

Exchanging e,g changes the scalar triple product's sign and leaves
B_eg fixed. This is a polynomial identity, so dJ[W]=0 as well.
L184's full three-placement sum is consequently zero; its Q_1+Q_2
equals +3/8, compensating the Q_3=-3/8 above. This does not contradict
L185–L186: the fixture is not an actual-probe mesh family, and their
subcubic estimates do not apply to it.

A bounded follow-up tests a two-vertex pinned graph, with the same
boundary endpoint rule but synthetic covariance and cubic jets. It
also fails to separate the full pairing. Here are complete definitions
and the reason its zero co-closed cubic jets are gauge-compatible
through the degree tested; no Wilson-action or actual-probe identity
is asserted for these jets.

Let D have fifteen rows: (1,0), (-1,1), six rows ((-1)^j,0) for
j=0,...,5, then (0,-1), then six rows (0,(-1)^j) for j=0,...,5.
The second row is the interior edge; every other row ends at a pinned
boundary vertex. Put q=|D| entrywise,

    chi=(D^T D)^(-1)D^T,   P=I-D chi,
    Phi_1=e_0^T,          Phi_2=e_0^T+e_1^T.

Indices e_j start at zero. D^T D has diagonal 8 and off-diagonal -1;
its inverse has diagonal 8/63 and off-diagonal 1/63. Both chi D and
Phi D are I_2. For any y, set theta=chi y, u=Py and define

    b_chi(y)=[y,q theta]/2-[D theta,q theta]/4,
    C_K(y)=-2<Ku,b_chi(y)>,                    K=PKP=K^T.

These are three-color polynomials. In particular C_K is zero on im P.
For a fixed pinned vertex color field eta, u is unchanged under
y -> y+s D eta and theta changes to theta+s eta. Therefore

    d C_K(y)[D eta]
      =-<Ku,[u,q eta]>
       -<Ku,([D eta,q theta]+[D theta,q eta])/2>
      =-<Ky,[y,q eta]>.

The second equality uses the edge identity
[D eta,q theta]-[D theta,q eta]=2D[eta,theta], killed in the
pairing by K D=0. This identity includes all normal end rows since
both vertex fields are zero at their boundary endpoints. The displayed
derivative is exactly the cubic gauge-jet identity for a quadratic
jet <y,Ky>. Thus choosing C_(L/2), C_A and C_B gives compatible
action, residual and probe cubic jets through this order. This does
not supply their higher jets, an actual Wilson flow or a local
four-dimensional action.

Put t_0=Pe_2. In the anisotropic cases let u_0=Pe_1 and set

    S=P+u_0 u_0^T,
    L=P-u_0 u_0^T/(1+||u_0||^2),
    A=t_0 t_0^T/2,   T=2SA,   M=2SAS.

The isotropic case instead has u_0=0. S and L are positive inverse
matrices on im P, with LS=SL=P; both vanish on im D. Thus L183's
finite Gaussian integration by parts applies. Each C_K vanishes
identically on im P, as does its derivative in the co-closed direction
Tz. Consequently rho_H=C_A-d C_(L/2)[Tz]=0 there. Retain the original
Phi in b, J and W, not chi: the retraction identity of L183 then
gives the paired gradient response -E[dJ[W]]. No sextic term is
silently dropped; its E[J rho_H] is zero by this particular choice
of synthetic jets.

For symmetric B=Pe_i e_j^T P+Pe_j e_i^T P the exact tested values are:

| S | (i,j) | (Q_1,Q_2,Q_3) | Q_1+Q_2+Q_3 |
| --- | --- | --- | --- |
| P | (0,1) | (0,8/189,-8/189) | 0 |
| P+u_0 u_0^T | (0,1) | (0,1040/15309,-1040/15309) | 0 |
| P+u_0 u_0^T | (2,9) | (-16064/107163,5008/35721,1040/107163) | 0 |

Run `python3 scripts/combined-ward-response/check_probe_paired_gauge_fixture.py`
with `--case isotropic`, `--case anisotropic-prefix`, or
`--case anisotropic-cross`. It writes respectively
`scripts/combined-ward-response/probe-paired-gauge-fixture-isotropic-zero.json`,
`scripts/combined-ward-response/probe-paired-gauge-fixture-anisotropic-zero.json`,
and `scripts/combined-ward-response/probe-paired-gauge-fixture-certificate.json`.
All matrix and contraction arithmetic is rational. Besides L184's
quartic placements, it independently forms the cubic <Lz,W>, including
both derivative slots, and contracts it with J through all three
covariances by Isserlis' theorem. The two expectations agree exactly.
The complete values, algebra checks and unmet nonzero-test records
were inspected, not inferred from previews.

All three discriminating nonzero tests fail. These exact zeros are
neither a universal cancellation theorem nor evidence of an actual
probe's coefficient. In particular, no tensor-specific comparison
between the actual rho_H and W has been made. This bounded synthetic
search is inconclusive for the approved joint limit. It does not
improve O(N^(7/2)) for the actual quartic, bound its actual sextic
partner, or control the independent co-closed zero-time flow. A further
synthetic search without a new discriminant is not the next step.

## Mathlib

Full matching actual-probe bound/limit and this pinned specialization:
**not checked**. Supporting transpose, trace and commutator coverage:
**not checked**; unknown coverage is not an absence claim. The proof
uses elementary finite-matrix identities, with L184/L187's previously
contracted tensor imported without redoing Isserlis' theorem. The
specialization is needed to distinguish the constant multiplication
term from the surviving prefix transport. The unchanged approved
[joint-group assessment](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md)
is reused; no further literature claim or general renormalization
reproof is made.
The later paired test additionally reuses L183's gauge retraction
and finite Gaussian integration by parts. Its elementary cubic
completion and exact synthetic zero tests have no checked Mathlib
match; they supply no actual-probe estimate or new literature claim.
