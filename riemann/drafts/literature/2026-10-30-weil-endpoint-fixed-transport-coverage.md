# Endpoint-fixed transport: source comparison

TARGET: Test whether endpoint-fixed smooth spatial transports of L516's conditional nullvector yield a signed commutator bound for L522's prime derivative sum that is stronger than the inward-dilation identity.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched logarithmic Laplacian inner variations/diffeomorphisms/shape derivative/domain perturbation/change of variables/commutator, generalized fractional Pohozaev vector fields, nonlocal inner variations and logarithmic Dirichlet Laplacian actions; compared the specific local finite-dilation, BV, nodal and L517/L518/support stops. The bounded search established no matching signed logarithmic/BV transport theorem; it establishes no novelty.
SOURCE_EVIDENCE: Newly read Djitte-Fall-Weth arXiv:2112.10653v1 Theorems 1.1-1.2, Corollaries 1.4/1.6-1.7, Lemma 2.1 and complete proof, Proposition 2.2 and Theorem 1.2 proof (2.5)-(2.10), Section 3 assumptions and Lemma 3.2 with complete proof, PDF pp.2-4/6-12; Gerontogiannis-Mesland arXiv:2309.16636v2 form (0.1), Proposition 5.8, and Section 5.5 Proposition 5.14 with its complete proof (5.9)-(5.11). Reuse Galerne Section 2 Lemma 1/Theorem 1 as precisely cited in L522 and the earlier Ros-Oton-Serra/Grubb/withdrawal/paper-67 comparison. Links and applicability below.
COMPARISON: Variable-field deformation forms and logarithmic domain-preserving actions are known in adjacent models. Neither inspected source gives a signed atomic commutator bound for this killed logarithmic operator. The fractional smooth-core and boundary arguments require different forcing/trace regularity; the logarithmic action theorem uses conformal distance identities. L522 supplies constant-shift BV limits only. Direct actual-domain and variable-shift justifications remain part of the bounded test, not imported premises.
GAP: Determine whether an admissible endpoint-fixed transport has an independently signed deformation contribution controlling L522's prime slopes beyond L516's identity. Prove actual part-domain admissibility and differentiation before using them; do not infer stationarity merely from form continuity or replace a BV derivative measure by an L2 generator.
REASON: Essential adjacent theorem hypotheses and proof cases are now inspected with no inaccessible essential source. EXPLORE permits one direct signed-commutator or obstruction test after separate approval of this changed assessment; it imports no transport identity and grants no favorable sign. An identity alone fails the continuation test.
LITERATURE_REASON: The turn began with REVIEW_REQUIRED coverage for variable transports, the logarithmic domain and BV atomic terms. This comparison supplies that missing source assessment; unchanged coverage should subsequently be reused.
SCOPE: Retain 0<a<A, ell=2a>log(2), L516's exact c, nu_rho, both prime shifts, every cutoff-equality atom and signed pole; a real normalized conditional nullvector and fixed-interval b>=0; L522's nonzero left trace and excluded reflected-image collision. The proposed flow field is smooth and vanishes near both endpoints. No H1 regularity, full-form contraction, simplicity, global positivity, trace vanishing, or first-zero/Xi realization is granted.

The main gap is actual-Xi all-degree positivity. The proposed
intermediate target is a signed estimate on the derivative observable
already identified in L522, potentially forcing S<=P-H at lambda=0.
That would imply zero flux by L516, while positive-eigenvalue family
rates, realization, collars and Xi transfer would remain independent.

The bounded source task is to compare primary hypotheses and relevant
proof cases for a smooth change of variables equal to the identity
near the two endpoints. A possible later test uses a transport field
that agrees with x away from shrinking endpoint collars and vanishes
near the endpoints. No flow formula, commutator identity or limit is
asserted here. Before any calculation, coverage must distinguish an
identity on smooth tests from a valid extension to this actual BV
nullvector and must retain the prime atoms at equality.

Continue only if source comparison identifies a justified test with
an independently checkable signed term capable of controlling the
prime slopes. If the proposal merely recovers L516's boundary flux,
requires that flux to vanish in order to pass a limit, or repeats the
withdrawn logarithmic Pohozaev import, park that implementation.
Full-form modulus/ground-state claims remain unavailable. This
continuation is not licensed by changing the name of the stopped
static nodal test. No cross-notebook input or Mathlib absence claim
is proposed; exact Mathlib coverage is unchecked.

## Primary comparison completed on 2026-10-30

[Djitte--Fall--Weth, *A generalized fractional Pohozaev identity and
applications*, arXiv:2112.10653v1, 20 December 2021](https://arxiv.org/pdf/2112.10653v1),
Theorem 1.2, assumes a bounded C^{1,1} domain, 0<s<1, zero-exterior
u in H^s, and a globally Lipschitz vector field. Its forcing is bounded;
if 2s<=1 it must additionally be locally C^alpha with alpha>1-2s.
Lemma 2.1 requires compactly supported C^alpha data with
alpha>max(1,2s). Proposition 2.2 uses the Hölder extension of
u/delta^s and a weighted gradient bound. Lemma 3.2, under Section 3's
C^2 family of C^{1,1} diffeomorphisms based at the identity, treats
differentiability of the pulled-back fractional form. Corollary 1.6
adds divergence/displacement bounds (1.15) and a local nonlinearity
with nonnegative primitive. Read the smooth-core integration, boundary
cutoff limits and uniform kernel-remainder proof cases, not just the
statements. V1 contains inconsistent variables and missing epsilon
factors in its displayed Lemma 3.2 proof; those displays are not used
as certificates here.

The proposed logarithmic signed-convolution equation is not this
fractional equation or its stipulated local nonlinearity. L515's
bounded data and L521's BV conclusion do not verify the cited forcing
and weighted-trace assumptions. No s->0 passage or hidden interior
C^1 regularity is licensed. The useful precedent is differentiating
the transformed form rather than assuming an L2 derivative of the
transported vector. Applying that method to L516, including its atoms,
is a proposed direct test, not a theorem imported from this source.
In particular the source's signed estimate cannot be copied without
checking its extra hypotheses and the complete retained kernel.

[Gerontogiannis--Mesland, *The logarithmic Dirichlet Laplacian on
Ahlfors regular spaces*, arXiv:2309.16636v2, 11 July 2024](https://arxiv.org/html/2309.16636v2#S5.SS5),
Proposition 5.14, proves domain preservation and a bounded commutator
for the Jacobian-weighted action of SO^+(n+1,1) on the sphere with
chordal metric and round volume. Its proof uses the exact conformal
distance and measure identities (5.9)--(5.11), then an absolute L2
commutator bound. Proposition 5.15 treats convex cocompact Kleinian
limit sets. The form (0.1) integrates over the underlying space;
the closed-interval example, Proposition 5.8, is a regional form.

Neither the conformal action hypotheses nor the regional operator
identify the killed, zero-extension logarithmic operator in L515.
No domain-preserving theorem for arbitrary endpoint-fixed flows, no
derivative with respect to a flow parameter, and no favorable signed
prime estimate is imported from these propositions. They do show
why the phrase logarithmic domain preservation alone does not settle
this target. The difference between regional and killed forms must
remain explicit in any later proof.

Galerne's deterministic derivative-measure theorem is reused with its
precise citation, hypotheses and proof scope in L522; no new source
review of that unchanged result is needed. Its constant translations
and C_0 testing do not themselves state a variable-spatial-flow
theorem. A proposed extension must justify its own measure convergence
and uniform bounds. No derivative of an atomic measure as an ordinary
density, product of distributions, or H1 generator test is available.

## Duplicates, stopping evidence and one bounded continuation

The local comparisons are the finite-dilation and dilation-flux
assessments, the BV and individual-prime assessments, and
`ATTEMPTS/2026-10-30-weil-nodal-compression-slope-gap.md`,
`ATTEMPTS/2026-10-30-weil-averaged-abel-energy-closure-stop.md`,
`ATTEMPTS/2026-10-30-weil-raw-renewal-adjoint-cancellation-stop.md`
and the automatic-support source stop. L523 constrains static overlaps;
L517 obstructs generic form-energy control; L518 retains a raw-adjoint
residual. These are not global bans on an eigenvector-specific
transport test. The withdrawn logarithmic Pohozaev argument remains
unavailable, as recorded in the earlier source comparison.

The exact TARGET is retained. EXPLORE covers one attempt using a smooth
field equal to x in a fixed interior bulk and zero near both endpoints,
starting with finite changes of variables in the complete form. It
must establish actual smooth-core part-domain admissibility before
using the null equation. It must then justify the logarithmic and
continuous signed-measure terms and the variable-shift BV pairings,
with the normalization explicitly fixed. No formula for them is
asserted or approved in this literature turn. A lack of a matching
theorem is a reason for this direct bounded test, not for reproving
the fractional theorems or claiming an original transport theorem.

The discriminating object is the sign of the deformation contribution
after the signed prime-slope terms are isolated using the actual
null equation. A coefficient comparison or an additional inequality
on this nullvector must supply information not already in L516/L522.
Only if that fixed-collar calculation identifies such information may
the same attempt examine shrinking collars to connect it to S. Every
error in that passage must be controlled without assuming zero trace;
endpoint fixation alone is not that control. Retain equality atoms,
nu_rho, both shifts and the negative measure contribution of the pole.

Continue only for a justified upper sign strong enough to imply
S<=P-H at lambda=0, or a strictly identified independent signed
intermediate estimate with a stated remaining gap. An exact local
stationarity identity with no favorable comparison, a reproduction of
the known flux, or a trace-vanishing premise fails this implementation's
test and parks it. An obstruction to one field or limit is not a
counterexample to the complete equation or RH. No uniform
positive-eigenvalue saving, first-zero realization, collars, or Xi
transfer is inferred. No mathematical result was derived here;
Mathlib matching remains unchecked and there is no cross-notebook input.

This changed ready assessment receives separate next-turn approval
under the supervisor's rule. The completed literature step is
EXPLORATION, not an established sign result or mathematical advance.
