# Lemma 415: the negative first linear mean permits joint-sign avoidance

## Hypotheses

Use exactly the selected local-jet relaxation in L414, with its constants
c=1/(4pi), a_*, b_*, beta_*, kappa_*, full matrix Gamma, exact envelope
A, ordinary/envelope conversion, response annulus, lower bound and
qualitative pointwise bounds. In particular the constants in the bounds
may be chosen once, independently of H; they are not independently
prescribed smaller constants. Retain all five scalar benchmarks, all
21 matrix limits and both U envelopes in L414 (1), on the same law.
Let ell=log H and additionally require L369's first-mean constraint

    E Bcal=-b0+O(ell^(-1)+H^(-1/2)ell^2),
    b0=zeta(3)/(4pi)>0.                                  (1)

The support is still {Delta<=0 or Bcal>=0}. There is no uniform height
marginal, actual response realization at the model height, single global
function pair, or regulator-margin requirement. The new mean is imported
from audited L369 (2) with exactly its ordinary-derivative normalization;
no further actual-family moment is assumed.

## Conclusion

For every sufficiently large real H there is a law satisfying this entire
enlarged list, with fixed constants and one common onset. It has exactly

    E Bcal=-b0,       E Delta=-a_* ell.                   (2)

Its cubic mean is beta_* ell^2+O(ell), which meets the required
beta_* ell^2+o(ell^2); exact cubic equality is not claimed. All quartic
coefficients, including all 21 matrix entries, remain unchanged, and both
absolute power-three bounds are O(ell^2). Every listed moment is absolutely
integrable. The law avoids Delta>0 jointly with Bcal<0 and its negative-Bcal
clipped square mean is strictly negative.

Thus adding this known negative first mean still cannot force the joint
sign or a positive clipped mean from the selected information. This is a
local feasibility obstruction, validated by the separate step-145 critical
audit below. It is
not an actual-zeta realization or a conclusion about actual clipping,
the regulator scale/full-error margin, common-zero counts, mixed positivity,
zero exclusion or RH. POTENTIALLY_NEW records limited prior comparison,
not established originality or a new zeta-moment theorem.

## Proof

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-15-compatible-jet-first-linear-mean.md`.
Reuse audited L414's weighted measure and rare component, changing only
its bulk atom. The source framework does not already give this simultaneous
calibration; the needed elementary specialization is proved here.

### Retained rare component

All model states have t=H. Write L_H=log(2+H), r_H=q(H)/L_H^2 and
v=(ca,-ch/2,-ca/4), with P,V obtained by L414's exact conversion.
L414's identities give

    Bcal=b_H(X;a,h)=c[a(x/4-z)-hy]-2r_H c a x,
    Delta=d_H(X;a,h),
    Ccal=c^2(a^2+h^2)/4-r_H c^2 a^2,                 (3)

where d_H is its exact quadratic polynomial, including curvature.
Use unchanged mu_H, orientation s_H, and
lambda_H=(integral |d_H b_H| dmu_H)/beta_* from L414 (6)--(10).
Their proved bounds are W_H=mu_H(1)=O(1), 0<lambda_-<=lambda_H<=lambda_+,
and r_H=O(H^(-2)L_H^(-2)). The rare measure has mass

    p_H=W_H/(lambda_H^4 ell^4)=O(ell^(-4))

and critical triple X=lambda_H ell^2 s_H n. It already has the required
support, response bounds and exact curvature. Write its unnormalized
integrals, not conditional expectations, as

    M_H=E_rare Delta=lambda_H^(-2) integral d_H dmu_H=O(1),
    J_H=E_rare Bcal=lambda_H^(-3)ell^(-2)
                              integral s_H b_H dmu_H=O(ell^(-2)). (4)

The last bound follows from uniform boundedness of b_H on the unit
sphere and response annulus. Its cubic integral is exactly beta_* ell^2.
Its Delta^2, Delta Bcal^2 and each Delta omega_i omega_j integral are
ell^4 times the corresponding mu_H integral in L414 (7), and hence have
exactly the required leading coefficients b_*, kappa_* and Gamma_ij.
These are all 23 quartic coordinates, not a selection of matrix entries.
No actual-to-leading quartic replacement is used to estimate J_H:
formula (4) is the exact first moment of the constructed component.

### Simultaneous bulk calibration

Let w_H=1-p_H. Eventually w_H>=1/2, |r_H|<=1/8,
b0+J_H>0 and a_* ell+M_H>0. Define

    Z_H=(b0+J_H)/(c w_H),
    Y_H=sqrt([Z_H^2+(a_* ell+M_H)/(c^2 w_H)]/(1-4r_H)). (5)

The positive square root exists, Z_H>0 is uniformly bounded, and
Y_H=O(sqrt(ell)). Place mass w_H at

    t=H, (a,h)=(1,0), X=(0,Y_H,Z_H), v=(c,0,-c/4).  (6)

The annulus contains (1,0). At this state exact conversion, without
dropping alpha or q terms, gives

    ell_F=Y_H^2,
    Ccal=c^2(1/4-r_H),
    Bcal=-c Z_H,
    Delta=c^2 Z_H^2-c^2(1-4r_H)Y_H^2
          =-(a_* ell+M_H)/w_H.                      (7)

For example P_0=0, P_1=Y_H, P_2=Z_H+2alpha Y_H/L_H,
V_0=c, V_1=alpha c/L_H; the two alpha terms in
2P_1 V_1-P_2 V_0 cancel exactly. The response curvature in (7) remains
in the denominator of (5). Thus Delta<0 and Bcal<0 at the new atom.
It lies in the allowed support. By (4)--(7),

    J_H+w_H(-c Z_H)=-b0,
    M_H+w_H Delta=-a_* ell,

proving (2) exactly and therefore (1) with zero error.

### Every remaining constraint

The bulk cubic contribution equals

    w_H Delta Bcal=c Z_H(a_* ell+M_H)=O(ell).         (8)

Adding the unchanged rare integral proves the asserted cubic benchmark.
The distinction from L414's stronger exact cubic conclusion is explicit:
the target requires its asymptotic benchmark, not that extra equality.
The other bulk contributions obey

    w_H Delta^2=(a_* ell+M_H)^2/w_H=O(ell^2),
    w_H Delta Bcal^2=-c^2 Z_H^2(a_* ell+M_H)=O(ell),
    |w_H Delta omega_i omega_j|=O(ell^2) (every i<=j). (9)

Indeed omega=(0,Y_H,Z_H,0,0,0) here, so each product is O(ell).
Consequently all additions in (9) are o(ell^4), including every zero or
nonzero off-diagonal target. The 23 rare quartic limits therefore remain
the required ones, without rounding or altering any constant.

For the absolute bounds, U=Y_H^2+Z_H^2=O(ell) on the bulk atom, giving
bulk contributions O(ell^2) to U^2, O(ell^(3/2)) to U^(3/2), and O(1)
to |Bcal|^3. L414 (13) gives unchanged rare contributions O(ell^4),
O(ell^2), O(ell^2), respectively. Hence both U envelopes and the absolute
third-moment benchmark hold; the two power-three totals are O(ell^2).

The response is unchanged in form throughout the law. Its model response
errors are zero, and L414 (14)--(15) supply fixed D_j, K=1 and
Ccal>=1/(128 pi^2 zeta(5/2)^2). Every critical triple has norm O(ell^2).
The conversion matrix has uniformly bounded entries since alpha is bounded
and q=O(H^(-2)), as established in L414. Thus |P_j|=O(ell^2), uniformly
on the entire support. Since ell^2 L_H^j/(1+H)^(1/2) tends to zero for
j=0,1,2, E_j=1 works for all sufficiently large real H. Take the maximum
of the finitely many onsets above and those of L414. All constants are
fixed independently of H. There is no subsequence or limiting-law assumption.
At each such H the support is bounded and all observables are measurable,
so every listed signed and absolute moment is integrable. Local Taylor-jet
compatibility follows from exactly the same conversion as L414; no global
pair or uniform height distribution is inferred.

### Optional finite law and limitation

Import Bayer and Teichmann, *The proof of Tchakaloff's Theorem*,
Proc. Amer. Math. Soc. 134 (2006), 3035--3040,
DOI [10.1090/S0002-9939-06-08249-9](https://doi.org/10.1090/S0002-9939-06-08249-9),
[arXiv:math/0502473v2, Corollary 2, pp. 3--4](https://arxiv.org/pdf/math/0502473v2#page=3),
without reproof. Its measurable-map statement applies to the constructed
positive law on its Borel support and the 30 integrable coordinates

    (1,Bcal,Delta,Delta^2,Delta Bcal,Delta Bcal^2,|Bcal|^3,
      (Delta omega_i omega_j)_(i<=j),U^2,U^(3/2)).

At each H it supplies at most 30 positive atoms preserving these integrals;
the constant coordinate preserves mass one, and the same support preserves
every pointwise condition. This is optional and proves no feasibility
before construction, uniform atom positions or actual realization.

On the support, Bcal<0 implies Delta<=0. Thus
Delta Bcal^2 1_(Bcal<0)<=0 everywhere, and (7) makes its bulk contribution
strictly negative. Integrability was proved above, so the constructed law
has a strictly negative clipped mean. The optional finite law at least
retains its nonpositive sign by support; its clipped value is not one of
the 30 preserved coordinates and strictness for that replacement is not
claimed. The known negative first mean alone does not repair the selected
information route. Independent actual-function and regulator obligations
remain unresolved.

### Separate critical audit — 2026-10-15, step 145

This REPRODUCTION proof_audit uses the unchanged SPECIALIZE assessment
`drafts/literature/2026-10-15-compatible-jet-first-mean-critical-audit.md`.
The conclusion passes within exactly the stated selected relaxation.
The direct inputs are audited L414 and L369's ordinary-derivative mean
(1)--(2). Their previously assessed analytic and quartic inputs are
imported in their existing scopes; this audit proves no new zeta moment
and makes no originality claim beyond the sources checked.

**Exact conversion and the two first means.** At the fixed output height
write r=q/L_H^2. Expanding the prescribed conversion gives

    ell_F=y^2-xz-r x^2,
    Ccal=v_1^2-v_0 v_2-r v_0^2,
    Bcal=2y v_1-xv_2-zv_0-2r x v_0.

All alpha terms cancel, and the discriminant has curvature correction
4r(xv_1-yv_0)^2, as established in L414's separate audit. Consequently
the bulk choice x=0, y=Y_H, z=Z_H, v=(c,0,-c/4) gives exactly

    ell_F=Y_H^2, Ccal=c^2(1/4-r), Bcal=-c Z_H,
    Delta=c^2 Z_H^2-c^2(1-4r)Y_H^2.

This checks the signs of the third coordinate and the denominator in
(5); no leading-response replacement or division by a critical jet
is involved. It also checks the normalization against L369 (1), whose
T^2 L^2 divisor is applied after ordinary differentiation.

For completeness let rho=lambda_H ell^2. A degree-k homogeneous
observable in the rare critical triple has integral
lambda_H^(k-4) ell^(2k-4) times its oriented mu_H integral. Thus at
k=1 its first Bcal integral is exactly J_H in (4), at k=2 its first
Delta integral is exactly M_H, at k=3 its Delta Bcal integral is
ell^2 S_H/lambda_H=beta_* ell^2, and at k=4 the factor is ell^4.
These are unnormalized rare integrals. The fixed compact state set,
W_H=O(1), and lambda_-<=lambda_H<=lambda_+ give

    p_H=O(ell^(-4)), M_H=O(1), J_H=O(ell^(-2)).

Choose one onset after which w_H>=1/2, |r|<=1/8,
b0+J_H>=b0/2 and a_* ell+M_H>=a_* ell/2. Since c,b0,a_*>0,
formula (5) then gives Z_H>0 with a fixed upper bound,
Y_H^2>0 and Y_H^2=O(ell). The factor 1-4r lies in [1/2,3/2].
Substitution yields

    w_H Bcal=-b0-J_H,
    w_H Delta=-a_* ell-M_H.

Adding the complete rare integrals proves both first means exactly,
including the constant-scale L369 mean. No quartic approximation has
been used to calibrate either first mean.

**Cubic tolerance and every quartic entry.** The bulk product is

    w_H Delta Bcal=c Z_H(a_* ell+M_H)=O(ell).

It is permitted by the required o(ell^2) cubic error. The extra exact
cubic equality of L414's particular construction was not a hypothesis
of the enlarged target. It must not be imported as an extra constraint.
At degree four, the rare component and its orientation are unchanged.
Its Delta^2 and Delta Bcal^2 integrals retain b_* and kappa_* from
audited L414 (7); the six diagonal and fifteen off-diagonal matrix
entries retain each Gamma_ij in the stated order. All these observables
are even under the common critical-jet sign reversal. In particular no
off-diagonal sign or factor of two is changed.

At the bulk atom omega=(0,Y_H,Z_H,0,0,0). Its only possibly nonzero
matrix products have indices (2,2), (2,3), (3,3); their absolute
Delta-weighted integrals are respectively O(ell^2), O(ell^(3/2))
and O(ell). The other eighteen are zero. Also its Delta^2 integral
is (a_* ell+M_H)^2/w_H=O(ell^2), and its Delta Bcal^2 integral is
-c^2 Z_H^2(a_* ell+M_H)=O(ell). Each is o(ell^4). This accounts
for all 21 signed matrix entries and both scalar quartic coordinates,
including entries whose required leading coefficient is zero. Their
finite collection of asymptotics has a common onset; no uniformity
over H-dependent test vectors or new moment limit is assumed.

**Support, absolute bounds and all real heights.** The rare support is
unchanged: L414's exact Borel orientation gives Bcal>=0 whenever
Delta>0, including the Bcal=0 boundary, and Delta=0 is itself allowed.
The new bulk atom instead has Delta<0 and Bcal<0, so is allowed as
well. Its contribution to the clipped mean is

    w_H Delta Bcal^2 1_(Bcal<0)
        =-c^2 Z_H^2(a_* ell+M_H)<0.

The rare contribution is nonpositive pointwise and integrable, so
strict negativity for the constructed law follows without cancellation.

Bulk U=Y_H^2+Z_H^2=O(ell) contributes O(ell^2), O(ell^(3/2))
and O(1) to U^2, U^(3/2) and |Bcal|^3 respectively. The unchanged
rare contributions in L414 (13) are O(ell^4), O(ell^2) and O(ell^2).
These prove both U envelopes and the absolute Bcal cube bound, with
O(ell^2) for the two power-three totals as claimed.

The annulus includes (1,0), and all states use the same model response
v=(ca,-ch/2,-ca/4). For |r|<=1/8, its exact Ccal is at least
c^2(a^2+h^2)/8>=1/(128 pi^2 zeta(5/2)^2). L414 (14)'s fixed D_j
bound the converted response coordinates and K=1 bounds their zero
model errors. Since alpha is bounded and q=O(H^(-2)), the conversion
matrix is uniformly bounded. Both components have |X|<=C ell^2
with one constant; hence |P_j| L_H^j/(1+H)^(1/2) tends uniformly to
zero for j=0,1,2. Thus E_j=1 works after a further finite onset.
Take the maximum of all finitely many onsets here and in audited L414.
The conclusions hold for every real H beyond it, with all constants
chosen independently of H. Neither a subsequence, a uniform height
marginal nor a single global function is needed or obtained. The same
local Taylor-jet assignments as L414 justify compatibility at each
state separately, not along a law of output states.

At each such H the law has bounded support in a finite-dimensional
Borel state set. The orientation and pushforward are measurable, and
all listed observables, including the clipped one, are measurable and
bounded on that support. This proves absolute integrability independently
of any assertion about signed moment convergence.

**Atomic theorem and limitations.** In the optional application of the
precisely cited Bayer--Teichmann Corollary 2 above there are
7+21+2=30 coordinates. The positive law, measurable support and absolute
integrability just verified discharge its hypotheses separately at each
H. The constant coordinate preserves mass, and atom membership in the
same support preserves all pointwise inequalities and their fixed
constants. The clipped coordinate is absent: the finite replacement
retains nonpositivity by support, but strict negativity for it does not
follow and is not claimed. No optimizer, strong duality or numerical
atom construction is invoked.

The step-141 audit concerns L414, not this enlarged calibration, so is
not a duplicate completed audit of L415. The step-143 pending-audit
qualification is discharged here. L410, L412 and L413 retain their
distinct scopes. This proves reliability of a local information
obstruction, not actual/global realization, a uniform height marginal,
an actual clipped mean, the full-error regulator margin, common-zero
upper counts, global mixed positivity, zero exclusion or RH. No
mathematical script or fresh external source retrieval was needed.

## Mathlib

Full matching coverage for this simultaneous construction, the measurable-map
theorem and complete zeta-moment inputs has not been checked. Unknown
coverage is not absence or formal verification. The canonical construction
is exact algebra on the audited L414 law; no numerical fit, solver or
mathematical script is used.
