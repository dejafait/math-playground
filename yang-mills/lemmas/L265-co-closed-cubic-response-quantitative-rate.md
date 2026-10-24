# L265 — Quantitative bound for the complete co-closed cubic response

## Hypotheses

Use exactly L193's relative SU(2) box (-4,4)^4, sufficiently fine
admitted even N, a=8/N, tau=1/16, lower-rooted direction-1 forest,
stored dimensionless full-link coordinates and bare-first expansion.
The displacement and the two actual probes i=3,6 are unchanged.
All variable normal end edges, physical faces, allowed constant
own-direction modes and complete heat sums remain. Fixed links have
zero coordinates. All vertex prefixes retain their physical pins.

Write C=D_1, D=D_0, L=C^T C, Delta=L+DD^T,
P=1-D(D^T D)^(-1)D^T, Sigma=Delta^(-1), S=P Sigma P and
H_s=exp(-s Delta/a^2). The three colors of z have independent
covariance S. Keep L183's complete polynomials and maps

    t(z)=2SAz, rho_H(z)=script R_3(z)-d script S_3(z)[t(z)],
    b(z)=[z,q Phi z]/2-[D Phi z,q Phi z]/4,
    W(z)=P db(z)[t(z)], rho_F(z)=rho_H(z)-<Lz,W(z)>.

Here A=PAP is symmetric and includes both residual insertion forms;
it need not be positive. Both derivatives of the actual prefixes in
W are retained. The object to be bounded is precisely L193(1):

    F_i(z)=j_(i,3)(H_tau z)+integral_0^tau U_i(s,z) ds,
    U_i(s,z)=-(6/a^2)T(H_s z,H_s z,E_(i,s)z),
    E_(i,s)=H_(tau-s)Q_i H_tau,                         (1)

where T is the full action cubic's symmetric polarization. In
particular F_i(z) is not F_i(Rz). The independent prefix correction
J_i is not part of (1).

Import L190's full local cubic tensors, finite stencil counts,
positive tensor covariance comparison and signed whitened bound
||2 S^(1/2) A S^(1/2)||<=C N on im P. Import L193's compact-probe
mode regularity through the final flow endpoint, its exact cubic
heat-transfer identity, uniform W envelopes and O(N^2) final
observable response. Their upstream analytic and audit qualifications
are unchanged. The separate critical audit below accepts the new
estimate relative to those imports; it does not audit the inputs.

## Conclusion

For both actual probes, with mesh-independent constants,

    integral_0^tau |E[U_i(s,z)rho_H(z)]| ds
                         <= C_i N^2 log(eN)^(5/4),      (2)
    |E[F_i(z)rho_F(z)]|
      <= C_i [N^2 log(eN)^(5/4)+N^(5/2)log(eN)]
      <= C_i' N^(5/2)log(eN)^2.                        (3)

The small-time estimate used in (2) is uniform at finite mesh:

    ||rho_H(H_r z)||_2
       <= C N^3/(1+r/a^2)^(1/2), 0<=r<=tau/2.          (4)

It concerns rho_H only, not the full forest residual. Both flow
endpoints and every W placement are included in (3).

This supplies the approved co-closed component rate. It neither
assembles the full joint probe group nor bounds the independent
transverse-H remainder, proves the complete quantitative L011
assembly, audits L220's cancellation or supplies an interacting
reflected estimate. Continuum axioms, a nontrivial physical sector
and finite positive infrared mass remain unresolved. No candidate
solution to the main problem is claimed.

## Proof

### 1. A uniform two-smoothed-slot local tensor estimate

First work with the scalar component blocks of the full relative
Hodge covariance, not entries of the co-closed covariance. For
u>=0 in lattice heat units put

    G_u=exp(-2u Delta)Sigma, h=(1+u)^(1/2).

The range needed below is u=r/a^2, 0<=r<=tau/2, so u<=c_0 N^2
for a fixed c_0. The complete product spectrum in L189 section 2
has eigenvalues nu_k>=c|k|^2/N^2 and normalized squared mode
amplitudes at most C N^-4 on every row. The shell max k_j=m
has at most C m^3 labels. Thus, for every row e,

    (G_u)_(ee)
      <= C N^-2 sum_(m=1)^(N-1) m exp(-c u m^2/N^2)
      <= C/(1+u).                                      (5)

For u<=1 use the finite sum; for 1<=u<=c_0 N^2 use Gaussian
integral comparison (with constants depending only on c_0).
This includes zero own-direction indices and all normal end rows.
There is no zero eigenvalue of the full relative one-form Laplacian.

Each scalar mixed Dirichlet/edge-Neumann Laplacian has nonpositive
off-diagonal entries, as used in L182 section 2. Its heat matrix
is entrywise nonnegative: for alpha at least its largest diagonal,
alpha I-Delta is entrywise nonnegative and
exp(-v Delta)=exp(-alpha v)exp(v(alpha I-Delta)). The positive
spectral gap therefore gives, within the same component block,

    0<=G_u(e,f)=integral_(2u)^infinity exp(-v Delta)(e,f) dv
                <=Sigma(e,f).

This entrywise comparison is used ONLY for these scalar blocks.
L166(11), as imported in L190(5), bounds Sigma(e,f) by
C[(1+d)^(-2)+N^-2], where d is the midpoint distance in lattice
units. Since every pair in the box has d<=C N, this is at most
C(1+d)^(-2). Positive matrix Cauchy--Schwarz and (5) also give
|G_u(e,f)|<=C h^-2. Combining the two bounds yields

    |G_u(e,f)|<=C(h+d)^(-2),
    |Sigma(e,f)|<=C(1+d)^(-2).                         (6)

Indeed min(h^-2,(1+d)^-2)<=4(h+1+d)^-2. Different component
blocks vanish. Fixed rows can be restored with zero values.

Let f be the complete color-ordered coefficient tensor of any
local cubic considered in L190 section 2. Suppose its absolute
coefficient sum at each anchor is at most B, its stencil radius
and number of words are bounded, and there are O(N^4) anchors
with bounded local multiplicity. Form the squared coefficient
norm with two covariance slots G_u and the third Sigma. A pair
of anchors at distance d contributes in absolute value at most

    C B^2 (h+d)^(-4)(1+d)^(-2).                        (7)

Bounded stencil shifts change only the constant in (6). All
components and color orders have already been included in f;
there is no factorial or deleted same-anchor term. For one anchor,
the full sum of this bound over the other anchors is at most

    C B^2 sum_(m=0)^infinity (1+m)/(h+m)^4
                         <= C B^2 h^-2.               (8)

To verify the last inequality, for m<=h sum (1+m)/h^4, obtaining
O(h^-2); for m>h sum O(m^-3), also obtaining O(h^-2).
Consequently the tensor norm is at most C B N^2/h. This bound
holds with any of the three choices of the unsmoothed slot.

It also holds with the two smoothed covariances H_r S H_r and
the third S, where u=r/a^2. In fact

    0<=H_r S H_r<=G_u,   0<=S<=Sigma.

The tensor product order follows by telescoping one positive
factor at a time, exactly as in L190(4). This is a comparison of
quadratic forms on coefficient tensors; no entrywise comparison
of S, its projection P, or the signed tilt is asserted. The same
argument bounds three smoothed slots by replacing one of them
by S before this comparison. Independent color second moments,
or Isserlis' theorem with the color-ordered convention of L183(23),
identify these coefficient norms with their polynomial L2 norms.

### 2. Keep two smoothed slots in each signed tilt placement

On E=im P choose Z=S^(1/2)|_E and independent standard Gaussian
coordinates xi^c in E, so z^c=Z xi^c. Write J=H_r|_E. Since S
commutes with H_r, H_r Z=Z J, and J is a symmetric contraction.
Set M=2 Z A Z. Then t(Z xi)=Z M xi and ||M||<=C N by the imported
full residual form bound. In particular

    t(H_r z)=Z M J xi,                                 (9)

with precisely this order. No commutation of M and J is used.

Let beta be the complete color-ordered tensor of script S_3(Z xi).
For the action derivative in rho_H(H_r z), one placement is
beta evaluated on (M J xi^1,J xi^2,J xi^3). In coefficient space
its tensor is

    (J M tensor J tensor J) beta
     =(J M tensor I tensor I)(I tensor J tensor J)beta.

Thus its norm is at most ||M|| times the norm with only colors
2 and 3 smoothed. Section 1 applies to that latter norm with
B=C, because the full action has bounded local coefficients.
It gives C N^2/h. The other two differentiated placements give
the same bound with the other two slots smoothed. Their sum
therefore has norm at most C N^3/h. This argument retains every
placement of the original signed tilt, while dropping heat on
only its coefficient-space output for an upper bound.

The full local residual has coefficient sum B<=C N per anchor
by L190 section 2, including both Q insertion forms and both
force/vector orders. All three of its inputs are H_r z. The
three-smoothed-slot version of section 1 bounds its norm by
C N^3/h as well. The triangle inequality proves (4). It includes
r=0 and does not appeal to smooth-column residual consistency.
It does not estimate W, b, or the full forest cubic by local
stencil bounds; those are not local tensors of the type in (7).

### 3. Transfer the actual time s and retain the probe's time envelope

For 0<=s<=tau define the cubic polynomial

    g_(i,s)(v)=-(6/a^2)T(v,v,H_(tau-s)Q_i H_(tau-s)v).

Then U_i(s,z)=g_(i,s)(H_s z). The exact identity L193(11) gives

    E[U_i(s,z)rho_H(z)]
      =E[g_(i,s)(H_(s/2)z)rho_H(H_(s/2)z)].            (10)

Both cubics are color alternating and have no internal pairs.
Each cross covariance on the right is H_(s/2) S H_(s/2)=H_s S,
exactly the left cross covariance. This verifies applicability
also at s=0 and for singular S, without inverse heat or moving
heat past A. The nonlocal action-tilt tensor is allowed here.

We need the complete time-dependent norm of the first factor,
not L193's fixed-delta constant. Its short inputs are H_(s/2)z,
and its external Gaussian input is

    E^*_(i,s) z=H_(tau-s)Q_i H_(tau-s/2)z.

This is exactly L193(6)'s E_(i,s)^(r) at r=s/2<=tau/2. That
lemma's full compact-stencil mode estimate applies uniformly for
0<=s<=tau, including the endpoint with no left output heat.
Here is its needed covariance-column consequence. With physical
mode energies lambda_l and e_l=a^2 f_l, write

    E^*_(i,s)=a^2 sum_(k,l) d_(i;kl)^(s/2)(s)e_k e_l^T.

For every fixed polynomial p_0, L193(6) bounds the complete sum
of |d_(i;kl)^(s/2)(s)|p_0(k)p_0(l) uniformly. Moreover
E^*_(i,s)P=E^*_(i,s), because Q_i annihilates gradients. Thus
its external covariance is E^* Sigma (E^*)^T, with columns

    v_l=E^* Sigma^(1/2)e_l
       =a lambda_l^(-1/2) sum_k d_(i;kl)^(s/2)(s)e_k.

The full mode bounds ||e_k||_infinity<=C a^2 and
||C e_k||_infinity<=C a^3(1+|k|), including all end rows,
therefore give

    sum_l ||v_l||_infinity^2<=C_i a^6,
    sum_l ||C v_l||_infinity^2<=C_i a^8.                (11)

For example each square sum is bounded by the square of the
corresponding absolute double sum; the positive physical spectral
gap bounds lambda_l^(-1/2). This uses the entire mode series,
not a finite cutoff or a supremum contraction of P.

Now apply precisely L189 sections 1 and 4's full polarized action
estimate, with its short time changed to s/2 and external columns
(11). The circulation on the external leg gives
C_i ell(s/2+a^2)^(1/2); the other two placements together give
C_i(s/2+a^2)^(-1/2)ell(s/2+a^2)^(1/4), after retaining the sole
6/a^2. The independent-copy third-chaos inequality in that proof
is a norm bound for the correlated polynomial, not a change of
its law. Since s/2+a^2 is comparable to s+a^2, this proves

    ||g_(i,s)(H_(s/2)z)||_2<=C_i m_a(s),
    m_a(s)=ell(s+a^2)^(1/2)
                 +(s+a^2)^(-1/2)ell(s+a^2)^(1/4),
    ell(x)=1+log(1+1/x).                               (12)

Combining (4), (10), (12), and a=8/N yields the uniform inequality

    |E[U_i(s)rho_H]|
     <= C_i N^2 { (s+a^2)^(-1/2)ell(s+a^2)^(1/2)
                    +(s+a^2)^(-1)ell(s+a^2)^(1/4) }.   (13)

In particular (13) is finite at s=0. It has been proved before
any integration or mesh limit; no varying delta is substituted
in a qualitative positive-time result.

For completeness, the first function in braces has bounded
integral over [0,tau], uniformly in a: it is at most
s^(-1/2)ell(s)^(1/2) for s>0, whose integral converges by
s=exp(-v) near zero. For sufficiently fine meshes tau+a^2<=1.
On x in [a^2,tau+a^2], ell(x)<=1+log(2/x). Hence

    integral_(a^2)^(tau+a^2) ell(x)^(1/4) dx/x
      <= (4/5)[1+log(2/a^2)]^(5/4)
      <= C log(eN)^(5/4).                              (14)

The substitution v=1+log(2/x) proves the displayed bound by
integrating v^(1/4); dropping its positive lower-end value only
increases it. Integrating (13) proves (2), with the entire initial
interval, including s<a^2, and final interval retained.

### 4. Assemble the full co-closed response with all W placements

Use L183's exact finite Gaussian integration by parts:

    E[F_i rho_F]=E[F_i rho_H]-E[dF_i[W]].                (15)

L193(15) bounds the external W placement for every 0<=s<=tau
by C_i N^2 m_a(s). Its integral is O(N^2), since both terms of
m_a(s) have uniform integrable majorants at zero as in L189.
L193(16) bounds the sum B_(i,a)(s) of the two short-output
placements, retaining their original -12/a^2, by

    |B_(i,a)(s)|<=C_i a^(-5/2)
                    [(s+a^2)^(-1/2)+(s+a^2)^(-1)].

Thus their complete absolute time integral is at most

    C_i a^(-5/2)[2 sqrt(tau)+log(1+tau/a^2)]
                         <=C_i' N^(5/2)log(eN).        (16)

This imports L191/L192 through L193's verified full-endpoint
extension. It retains both moving prefixes, their correlations,
the upper jump, the projected smooth external output and every
source row; no field W is replaced by independent noise or
assigned input smoothness. The combined two-placement bound is
used as stated, without assuming a bound for each separated
signed summand or a cancellation with rho_H.

Finally L193(19)--(21) bounds the complete final-observable
response |E[j_(i,3)(H_tau z)rho_F]| by C_i N^2, with its W
derivative included. Add this once to (2) and the two complete
Duhamel derivative bounds. At fixed N the time-dependent
polynomials are continuous on a finite-dimensional space, so
all expectation/integral interchanges in (15) are legitimate.
This proves the first inequality (3). Since log(eN)>=1 and
N>=1, each of its two terms is at most a constant times
N^(5/2)log(eN)^2, proving the requested bound.

### 5. Verification and scope

Verification is analytic. The shell estimate (8) accounts for
every local anchor pair, including coincident anchors and physical
boundary layers. Scalar heat positivity in section 1 applies to
Sigma only, while the passage to S is a positive tensor-form
comparison. The key signed placement is J M, not M J, on the
coefficient tensor; its norm is bounded only after leaving the
other two J factors attached. Both residual subtractions remain.
The common-input heat transfer is exact on all three cross lines.
The actual compact probe coefficients supply (11) at s=tau;
final-time damping is not assigned to a short internal leg.

The complete allowances are N^2 log(eN)^(5/4) for the rho_H
Duhamel pairing, N^2 for the external W placement and final
observable response, and N^(5/2)log(eN) for the two short-output
W placements. These are upper bounds, not signed asymptotics or
lower growth claims. No mathematical script or numerical
certificate is required for these finite inequalities. The separate
audit below checks this component. All imported qualifications remain;
acceptance here does not audit a full assembly.

### Separate critical audit, 2026-10-23

**Verdict: accepted relative to the stated analytic imports.** The
unchanged SPECIALIZE assessment
`drafts/literature/2026-10-23-co-closed-response-rate-critical-audit.md`
authorizes exactly this audit. No inequality, rate, response definition
or direct mathematical input required correction. This verdict checks
the deductions (5)--(16), rather than recursively auditing the imported
local tensors, signed residual form bound or L193's W estimates.

**Relative scalar blocks and all rows.** The component decomposition
imported in L182/L189 has one edge direction and three interior-vertex
directions. To check its boundary identification, let B be the pinned
one-dimensional vertex incidence, with N edge rows and N-1 vertex
columns. Then B^T B is the Dirichlet tridiagonal matrix with diagonal
2 and off-diagonal -1. The edge matrix B B^T has endpoint diagonal
1, interior diagonal 2 and off-diagonal -1. The component Hodge
matrix is the tensor sum of one such edge matrix and three vertex
matrices; the mixed incidence terms cancel in C^T C+DD^T. Thus its
scalar off-diagonal entries are nonpositive even on both normal end
layers. The edge eigenvectors are N^-1/2 and
(2/N)^1/2 cos(k pi(ell+1/2)/N), 1<=k<N; the vertex eigenvectors are
(2/N)^1/2 sin(k pi j/N), 1<=k<N. Their squared tensor amplitudes are
at most 16/N^4. At least three indices are positive, so the full
matrix has a gap and the heat inverse integral converges.

The inspected primary interval formulas are J. S. Dowker,
*Heat-kernels on the discrete circle and interval*,
[1207.2096v2](https://arxiv.org/pdf/1207.2096v2), 31 August 2012,
section 7 (29)--(31), printed pp. 10--11, and section 8 (34)--(37),
printed pp. 12--13, with the generator normalization in section 2
(1)--(3), p. 1. For its Neumann interval use p=N and vertex label
j=ell+1, so its half-integer cosine argument is ell+1/2. For the
Dirichlet factors use p=N and j=1,...,N-1. These are precisely the
matrices above, with unhalved second differences. The constant edge
mode is retained, not inverted in isolation. The four-dimensional
Green bound is the separate imported L166(11), whose full-row image
and long-time argument was inspected; no continuum scalar bound is
substituted for it.

For (5), the shell has at most C m^3 labels, each squared amplitude
is at most C N^-4 and its inverse eigenvalue at most C N^2/m^2.
This gives exactly N^-2 sum m exp(-c u m^2/N^2). For 1<=u<=c_0 N^2,
the sum is at most C N^2/u by a Gaussian integral bound; for u<=1
it is at most C N^2. The constant may depend on the fixed c_0.
The resulting diagonal bound is uniform at both normal end layers.
Metzler heat positivity and the inverse integral compare G_u with
Sigma entrywise only inside the scalar blocks. Positive-matrix
Cauchy--Schwarz bounds |G_u(e,f)| by C/(1+u). The finite box has
d<=C N, so L166's N^-2 term is absorbed by C(1+d)^-2. Combining
these two estimates proves (6), also at u=0 and u comparable to N^2.
No positivity assertion is made for the entries of S.

**Joint tensor sum and tilted order.** In (7), two smoothed covariances
and one raw covariance give (h+d)^-4(1+d)^-2. Bounded stencil shifts
cost a fixed constant, including d smaller than the stencil radius.
The four-dimensional anchor shell has at most C(1+m)^3 members;
therefore its product sum is C sum (1+m)/(h+m)^4. Splitting at h
gives respectively h^-4 O(h^2) and O(sum_(m>h)m^-3), both O(h^-2).
The coincident shell is included. There are O(N^4) first anchors,
so the squared coefficient norm is at most C B^2 N^4/h^2.
This checks the entire box, including every boundary anchor, without
an interior-support premise for the local cubic.

All covariance factors in this comparison are positive semidefinite.
Tensor-product telescoping therefore applies even though S is
singular, without any covariance entry comparison or factor
commutation. The exact distinct-color second moment is L190(4);
there is no factorial. On im P, Z=S^(1/2) commutes with J=H_r and
t(H_r z)=Z M J xi. Transposing the tilted input to coefficient space
gives J M, not M J. In the first color placement the tensor is
(J M tensor I tensor I)(I tensor J tensor J) beta. Its norm is at
most C N times the two-smoothed-slot norm because ||J||<=1 and
||M||<=C N. The other two placements have the corresponding other
two smoothed factors. This verifies all three derivatives while
leaving heat attached before taking the tilt norm. The local
residual has B<=C N and three smoothed slots; replacing one of their
covariances by its raw positive upper bound gives the same C N^3/h
allowance. Both residual insertion forms and both force/vector
orders belong to that imported complete tensor. This proves (4)
relative to its stated inputs, without any local model for W.

**Exact heat transfer and the actual final endpoint.** Both cubics in
(10) contain one of each color, hence have only the three cross
contractions, including for nonlocal rho_H. Each is H_s S on both
sides because S commutes with heat. The identity neither commutes A
with heat nor transfers a forest prefix correction. Its first
factor has short time s/2 and external map
H_(tau-s)Q_i H_(tau-s/2), exactly L193(6) with r=s/2.

The physical eigenvalue normalization is important here:
Sigma^(1/2) e_l=(a sqrt(lambda_l))^-1 e_l, while the external matrix
has coefficient a^2 d_(kl). Its covariance column is consequently
a lambda_l^(-1/2) sum_k d_(kl)e_k, as written before (11), giving
row size a^3 and circulated row size a^4. The full absolute mode
sum in imported L193(6), and the positive physical gap, bound the
sum of their squares as in (11). The replacement of S by Sigma is
an equality on this external leg because the map annihilates
gradients on its right. There is no such replacement for the two
short legs. At s=tau the left heat is the identity; L193's repeated
physical-difference argument on the actual compact Q_i stencils
supplies the output-mode decay instead. It covers both the triplet
and polarized shear form, all allowed constant indices and all
high labels. This endpoint regularity is an explicit import, not
an independently re-audited probe theorem.

Applying L189's full polarized action estimate now gives (12):
external circulation uses the a^4 column bound with two short
covariances, while the two other placements use the a^3 bound with
one short circulation. Its independent-copy inequality bounds the
actual third-chaos norm; it asserts no independence of the actual
slots. The sole 6/a^2 is retained. Since
N^3/(1+s/(2a^2))^(1/2)<=C N^2/(s+a^2)^(1/2), Cauchy--Schwarz in
(10) gives exactly (13), uniformly before integrating. This also
checks the region s<a^2. The first integral in (13) has the
integrable majorant s^(-1/2) ell(s)^(1/2). For the second use
x=s+a^2 and v=1+log(2/x), reversing the limits because dx/x=-dv;
integrating v^(1/4) gives (4/5)v^(5/4).
Thus the complete rho_H allowance is N^2 log(eN)^(5/4), with no
mesh-dependent delta in L193's qualitative theorem.

**All remaining placements and assembly.** L183's finite Gaussian
IBP gives the minus sign in (15): W is divergence-free in the
co-closed Gaussian coordinates, with both prefix derivatives
retained. The first directional derivative differentiates F, not W.
L193(15) is the external W placement with its sole -6/a^2;
its m_a envelope has a uniformly bounded integral. L193(16)
already combines the two short-output placements with -12/a^2.
Dividing its a^3 factor gives a^(-5/2), exactly (16). The two
integrals are bounded by 2 sqrt(tau) and log(1+tau/a^2), so their
allowance is N^(5/2) log(eN). No individual bound for an uncombined
signed summand or smoothness for a rough tilted prefix is assumed.
All source/end rows, correlations and the upper jump remain in
these imported W bounds. Their full-endpoint use is the explicit
L193 extension checked for compatibility here, not a new audit of
L191/L192.

Finally the O(N^2) final-observable bound from L193(19)--(21) already
includes its W derivative. It is added once, rather than again
using (15) for that observable. Finite-mesh continuity permits each
time integral before any refinement. The resulting three complete
allowances are those stated in section 5; log(eN)>=1 puts all of
them within N^(5/2) log(eN)^2. The conclusion concerns precisely F_i(z)
paired with rho_F and does not estimate F_i(Rz), the independent
prefix sextic/quartic group or the full forest residual's norm.

This audit validates an existing local standard-method result; it
establishes no stronger rate or originality beyond the checked
sources. No mathematical script or numerical test is needed for
these analytic estimates. The original DAG inputs are unchanged.
All upstream analytic and pending-audit qualifications, the
independent transverse-H rate, quantitative assembly and interacting,
continuum and infrared construction gaps remain unresolved.

## Mathlib

Full matching result and supporting relative-cochain heat/tensor
coverage: **not checked**. Unknown availability is not absence.
The named Gaussian input is Isserlis' theorem; a precise inspected
source is H. Munthe-Kaas, O. Verdier and G. Vilmart, *A short proof
of Isserlis' theorem*, author PDF dated 7 March 2025, Theorem 1,
p. 1, and Theorem 4, p. 3,
[author PDF](https://www.unige.ch/~vilmart/paper_isserlis.pdf).
The singular-covariance/color specialization and exact heat transfer
are already justified in L183, L189, L190 and L193. They are reused,
not reproved as general theorems. The present work supplies only
the missing uniform two-smoothed-slot estimate and its actual-probe
application. Primary full renormalized-flow results are not used
as bounds on this selected bare group; see the unchanged approved
[assessment](../drafts/literature/2026-10-23-co-closed-cubic-response-quantitative-rate.md).
Classification: REPRODUCTION, local progress using standard tensor,
heat and Gaussian estimates, without a certified novelty claim.
