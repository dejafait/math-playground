# Three-particle complete current — nomination979, source review980

TARGET: Assess source coverage for a complete localized Stokes identity for C466x's three-particle raw flow under sqrt(3)a+M_1 T_0<R, including outer-exit exclusion and every collision/initial-diagonal cutoff flux.
CHECKED: 2026-11-14
DECISION: EXPLORE
SEARCH_EVIDENCE: Review980 reused reviews975/977/960/964 and compared C466x, C466u's complete-minor/cutoff proof, C466t's earlier-stop case and closure979; new logarithmic-flow, singular-pullback, Vandermonde-collision and finite-volume-current searches located Harvey–Lawson but no inspected matching theorem. Queries, primary cases and qualifications appear below; no novelty inference.
SOURCE_EVIDENCE: Reuse TNV https://arxiv.org/pdf/1706.03822v2 Appendix B (B.1)-(B.5), p22, and Teschl https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf Lemma2.14/Corollary2.15 p52, Theorem6.1/proof pp189-190 from review964. Rechecked WKM https://arxiv.org/pdf/2008.10321v2 Section3.1 (29), Theorem4/Proposition5 and full proofs, pp8-9. Reuse HP https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6102-11511_2008_Article_BF02838327.pdf Theorem2.1/Lemma2.2 pp40-41, Theorem4.1(b) pp45-46, Theorem5.2/proof pp48-49 from review960; fresh PDF request timed out. Newly read Harvey–Lawson https://www.math.stonybrook.edu/~blaine/FiniteVolFlows.pdf arXiv:math/0101268v1, Definition1.1/Theorem1.2 and full proof pp4-5. None is imported as the proposed identity.
COMPARISON: C466x is spatial only and C466u is a one-divisor complete identity under different hypotheses. WKM covers all exterior degrees on compact smooth survivors, not weighted endpoint limits. HP needs unpaid neighborhood-mass or trace hypotheses; Harvey–Lawson needs a smooth compact-manifold flow and finite graph volume and retains a limiting current. No direct import settles the intersecting-divisor zero extension.
GAP: Prove or refute the exact buffer exclusion, complete beta/gamma L1_loc control and zero weak cutoff flux at every collision and initial diagonal, including triple intersections; all remain mathematical obligations.
REASON: Essential changed-scope literature coverage is now sufficient for one bounded established-tool proof/defect attempt, without deriving any new specialization or claiming the identity. The completed C466x audit and earlier-grazing stop remain closed in their exact scopes.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED covered a new complete-form/intersecting-divisor target; reused adequate local-tool assessments and checked only missing theorem-level scope rather than repeating the spatial-bound literature.
SCOPE: Exactly the fixed data and proposed conclusion below; one complete-current attempt may be nominated for separate approval, with no new estimate, regular lifetime, endpoint trace, restart, symmetry, sign or Xi conclusion assumed.

## Exact proposed statement to assess

Retain C466x's finite 0<a<R, M_1,M_2>=0, complex H_0,
holomorphic H on B={|z_j|<R} in C^3 with H(0)=H_0 and
whole-B Hermitian bounds ||grad H||<=M_1, ||D^2H||_op<=M_2.
Let Delta=product_(i<j)(z_j-z_i), S=-2 log Delta+H,
F=Delta^2 exp(-H), and dot X=conjugate(grad S), X(0,u)=iu,
for pairwise distinct u in I=(-a,a)^3. Tau is the first maximal
lifetime in B minus {Delta=0}. Keep the unit flat metric and raw time.

Add the proposed strict buffer

    T_0>0,   sqrt(3)a+M_1 T_0<R.

Whether this excludes all prior outer exits is a proof obligation,
not a deduction made in this nomination. It is stronger than a<R;
the C466u restriction is not silently transferred to this geometry.
Do not treat M_1 as a bound for the full singular velocity.

On Q=(0,T_0) times I and
D={(t,u) in Q: Delta(u)!=0, t<tau(u)}, let Psi=X on D only.
For every real or complex chi in C_c^infinity(B), define

    Omega=F dz_1 wedge dz_2 wedge dz_3,
    beta=Psi^*(chi Omega),
    gamma=Psi^*(dchi wedge Omega).

These are ordinary complex-valued real differential forms. Beta
includes its spatial coefficient and all three coefficients with a
dt slot; gamma is the full four-form. Orientation is
dt wedge du_1 wedge du_2 wedge du_3. Bars denote coefficientwise
zero extension to Q, including all initial coincidences and stopped
parameters. No stopped-map derivative or post-exit flow is defined.

The proposed conclusion is: no first outer exit up to T_0, both
bar(beta) and bar(gamma) have coefficients in L1_loc(Q), and

    d bar(beta)=bar(gamma) in distributions on Q.

No regular lifetime, smooth collision preimage, unique limiting
endpoint, symmetry of H, spacing cutoff or collision restart may be
assumed. The statement retains simultaneous triple collisions and
tests meeting every initial diagonal, including their intersection.
It does not assert a sign or a globally conserved integral.

## Bounded source test and continuation threshold

Reuse the primary hypotheses and relevant proof cases already recorded
in reviews975/977 and current reviews960/964 before any new retrieval.
Check exact/stronger results for zero extension of pulled-back forms
under logarithmic flows with intersecting divisors, and compare their
boundary/removability assumptions with this four-real-parameter domain.
Distinguish complete forms from the single spatial coefficient.
Inspect additional primary cases only where this changed scope needs
them; the old approval/retrieval loop is closed, not a source blocker
to be retried. In particular, any HP import must handle the actual
inhomogeneous equation and singular-set hypotheses, not just its title.

For a possible later proof, one concrete sufficient test is to construct
smooth survivor cutoffs eta_epsilon approaching 1 with local L1
convergence of eta_epsilon beta and eta_epsilon gamma to the zero
extensions, and, for every scalar phi in C_c^infinity(Q),

    integral_D phi d eta_epsilon wedge beta -> 0.

This is an unproved threshold. The review may approve a rigorously
equivalent weak-limit method. It must not approve a new estimate on
the basis of this nomination or an analogy with C466u. An admissible
nonzero distributional defect or nonintegrable complete coefficient
would refute the proposed identity; failure of one sufficient estimate
would only stop that method. A source mismatch or persistent essential
access blocker parks the dependent proposal in favor of independent
work. No proof, mathematical script or new lemma was produced here.

## Relevance, duplicate comparison and limits

This is a distinct complete-current question after audit979 validated
C466x's mass estimate. If proved, it could pay an intersecting-divisor
boundary step in later signed contour assembly. Actual-H realization,
patch/global assembly, determinant phase and all-degree positivity in
L030-L032/C032a remain independent. A modulus is never an algebraic
square sign. C466x is a possible spatial input; C466u is only a
single-divisor comparison until its machinery is justified in the new
setting. C466t's earlier-grazing defect remains an obstruction to the
unrestricted-time statement. Stops971/972/974 concern sign ansatzes,
not the proposed weak identity; the November1 heat-divisor flux stop
concerns a different atomic heat-evolution law, not this raw flow.

Three continuations were compared: higher-particle modulus bounds
would keep the same estimate mechanism without paying a signed step;
a general determinant-phase theorem has no assessed bridge to actual
H and would exceed the stopped affine/mixed families; the complete
three-particle current has an explicit independently testable cutoff
threshold and uses the newly audited local input. Select its source
review. No justified central creative mechanism from modulus to
actual-Xi positivity has yet been specified, so none is invented or
called creative for routing purposes. A later mathematical attempt,
if approved, would be established-route development.

Next invocation: literature_comparison, standard/high. The changed
complete-form and intersecting-divisor hypotheses need comparison,
not mechanical retrieval. Mathlib matching coverage remains unchecked.
No cross-notebook input is proposed. This REVIEW_REQUIRED nomination
does not reject or reopen the completed C466x audit.

## Completed bounded source review980 — 14 November 2026

The nomination text above is preserved as the invocation-start proposal;
its final REVIEW_REQUIRED sentence records that earlier state. This section
completes source coverage only. The strict buffer and the proposed weak
identity are neither proved nor refuted in this literature-only step.

### Discovery and duplicate/failure comparison

Read the relevant primary-source comparisons in reviews975/977/960/964,
C466x's imported-tools and weighted-estimate passages, and C466u's complete
coefficient, support, shell-time and weak-limit proof, (9)-(27). Compared
C466t's hypotheses, conclusion and earlier-stop example, together with
closure979. The earlier sign stops971/972/974 were already assessed in
those unchanged comparisons and were not reopened as sign proposals.
The newly paid spatial bound is not a duplicate proof of a complete
current. C466u's single collision coordinate and inward-shell argument
are not a theorem for the coupled three-divisor geometry. In particular,
no independent pair-coordinate or regular triple-collision preimage
assumption is licensed. C466t still blocks using ambient chi alone to
ignore a previous escape; the proposed buffer must be checked against
the actual singular ODE, not treated as a full-speed estimate.

New queries included `"logarithmic" "gradient flow" "divisor" Stokes
differential forms`, `"Lefschetz" "fermion determinant" "boundary"
"Stokes" flow singularities`, `"pullback" "removable singularities"
"differential forms" L1 Stokes`, `"Vandermonde" "flow" "Stokes"
collision`, `"logarithmic gradient" "currents" collisions`,
`"Vandermonde" "gradient flow" "current"`, `"logarithmic" "flow"
"zero extension"`, `"Lefschetz" "intersecting" "divisors" flow`,
and `Harvey Lawson finite volume flows currents Morse theory Stokes
theorem`. The primary Harvey–Lawson paper was followed from the last
lead. Generic thimble/Stokes-phenomenon hits and secondary summaries
were not treated as theorem evidence. This bounded search identifies
no inspected exact or stronger theorem, not an exhaustive absence
result or evidence of originality.

### Primary hypotheses and essential proof cases

**WKM, reused and spot-checked in the all-degree scope.** Wu,
Kanevskiy and Margaliot, *k-Contraction: Theory and Applications*,
[arXiv:2008.10321v2](https://arxiv.org/pdf/2008.10321v2),
27 September 2021, Section3.1, (29) and continuity assumption p8,
Theorem4/Proposition5 and their complete proofs pp8-9. For a continuous
real A and its fundamental matrix, Proposition5 bounds the kth
multiplicative compound norm by the exponential of the integral of
the matrix measure of the kth additive compound, for every 1<=k<=n.
The proof uses compound evolution and Coppel's inequality. Uniform
negative measure is needed for contraction, not the upper bound.
This supplies a local tool in real dimension six, including exterior
degrees three and four. It gives no uniform weighted singular bound,
no initial-velocity bound and no collision cutoff estimate. Applying
it to the velocity and parameter columns, and estimating their
weighted complete minors, remains a later specialization to justify.
No reproof of this known tool is warranted.

**Harvey–Lawson, newly inspected comparison.** F. Reese Harvey and
H. Blaine Lawson, Jr., *Finite volume flows and Morse theory*,
Ann. of Math.153 (2001),1-25,
[arXiv:math/0101268v1](https://www.math.stonybrook.edu/~blaine/FiniteVolFlows.pdf),
1 January 2001, Section1, Definition1.1, Theorem1.2 and entire proof,
pp4-5. They assume a smooth vector field on a compact oriented
manifold and finite volume of its forward flow graph in the induced
product metric. The theorem gives current limits and the boundary
identity partial T=[diagonal]-P. Its proof uses mass convergence
and continuity of current boundary; P is retained, not asserted zero.
Our survivor map is singular and stopped, on a parameter subdomain,
and no such compact-manifold smooth flow or graph-volume premise is
supplied. C466x's one weighted minor is not that premise. This is
therefore a comparison, not an imported removability conclusion;
a current framework still requires the relevant boundary payment.

**HP and ODE coverage reused without redundant discovery.**
Harvey–Polking, *Removable singularities of solutions of linear
partial differential equations*, Acta Math.125 (1970),39-56,
[primary PDF](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6102-11511_2008_Article_BF02838327.pdf),
Theorem2.1/Lemma2.2 pp40-41, Theorem4.1(b) pp45-46 and
Theorem5.2/proof pp48-49, are used only in review960's recorded scope.
Theorem2.1 requires L1 neighborhood mass o(epsilon^m) along a
liminf for an order-m homogeneous smooth-coefficient operator;
Theorem4.1(b) requires bounded coefficients and zero H^(n-m)
measure of the exceptional set. The jump theorem requires a smooth
hypersurface and matching weak normal jets. Neither the geometry of
the exceptional set in Q nor a homogeneous formulation of our
inhomogeneous equation is supplied. A new HP PDF request timed out;
the earlier inspected hypotheses/proof cases remain available and
are sufficient for this non-import comparison. No new source blocker
or fresh theorem-page inspection is claimed.

Teschl's precise continuation and local-flow results and TNV's
real-variation/raw-blow-up cases are reused from reviews960/964/975,
at the primary URLs and locations in SOURCE_EVIDENCE. They apply on
compact survivor intervals in the punctured open ODE domain. They
do not extend a trajectory through a collision, prove the proposed
buffer, or remove an interior stopped boundary. TNV's complete
modified flow changes the metric. Review960's rough-chain and
worldvolume comparisons likewise retain unpaid smoothness, trace or
chain-evolution hypotheses; they are not needed as new imports for
the direct cutoff approach. Further pursuit of those frameworks is
not essential unread coverage for this attempt. No full matching
Mathlib theorem has been checked; unknown coverage is not absence.

### Decision and mathematical continuation

EXPLORE is appropriate: primary tools and their limitations have been
assessed sufficiently for one bounded full-form proof/defect attempt.
No source conclusion supplies the full requested identity. Its
uncovered singular-flow specialization must therefore be attempted,
not cited as already known. It is justified to use the existing
spatial estimate and known local machinery without reproving either;
that does not excuse any missing complete coefficient or limit.

The later test must first prove the exact buffer excludes every prior
outer exit, including limiting simultaneous events, or exhibit a
counterexample. It must then establish complete-form integrability
and a defect-free weak limit under the full coupled-H assumptions.
The cutoff criterion in this nomination is sufficient as a proposed
method; it is not a result derived in this review. A useful cutoff
must have genuinely interior survivor support after zero extension,
handle all initial diagonals and all triple intersections, and pay
the full d eta wedge beta term, not just its time derivative. No
shell residence estimate transfers from C466u by citation. A different
weak-limit method is permitted only if it proves the same statement.

Continue only on the complete identity or an admissible nonzero defect
or nonintegrable coefficient. If a chosen estimate fails, record that
method limitation without declaring the target false. Save partial
reasoning before lengthy work. No new mathematical estimate, lemma,
script or main-argument/DAG change was made here. The outcome is
EXPLORATION with LITERATURE/NOVELTY_UNCHECKED, not an advance beyond
the sources or a mathematical exploration-budget reset.

The precise research continuation is nominated in
[assessment980](2026-11-14-three-particle-complete-current-attempt-980.md)
for separate approval next turn. It is established-route development;
no source-assessed implication from a modulus or local current to
actual-Xi positivity exists here to justify a central creative label.
A successful identity could pay a multidivisor boundary step but would
leave actual-H realization, phases, signed/global assembly and all-order
positivity unresolved. No cross-notebook input or RH candidate.
