# Actual normal source fields — completed one-face transfer comparison

TARGET: Transfer L293's planar cancellation to L282's actual normal source fields on one flat-face patch away from edges, proving an o(N) bulk-subtracted pairing uniformly over the complete external-mode sum.
CHECKED: 2026-10-27
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed the bounded actual-source, discrete boundary-regularity and varying-field searches below; compared L281(3)–(11), L282(17)–(23), L287(1)–(6), L292(1)–(4) and L293(1)–(15) with the saved planar/bulk assessments and ATTEMPTS/005,018,024,048,049. No inspected matching transfer theorem was established; no novelty claim follows.
SOURCE_EVIDENCE: Newly inspected Brandt, Math. Comp. 20 (1966), Theorems 5.1/5.2, 7.1/7.2 and section 8, including the odd/even reflection proof cases and endpoint conventions; reused the versioned primary scalar/slab/power-counting readings in the two planar assessments. Strikwerda–Wade–Bube abstract/reference list and Johnson's plane-boundary result remain screening leads, not imported theorems. Rechecked the current Clay link and Jaffe–Witten section 4, printed p. 6.
COMPARISON: L282 establishes physical L2 convergence without a boundary trace statement, and L281/L287 provide N^2-scale external tails. L293 controls constant-depth normal plane waves. Scalar boundary regularity and corrected off-spectrum half-space resolvent convergence do not identify the complete finite-cube Wilson/density pairing or an N-scale tail. The precise proposed subtraction and missing estimates are specified below.
GAP: Establish actual normal-field trace/layer control with summable mode constants, a finite-cube-to-half-space comparison at o(N), and a surface-scale bound for the complete signed external-mode tail; retain all external-curl cubic terms and missing bulk second vertices. None is an imported premise.
REASON: Adequate bounded comparison is complete for a direct test from the exact relative tensor modes and Wilson kernels; no inaccessible source is essential to that attempt. EXPLORE permits investigation after separate approval, not a source-transfer theorem or absence-of-duplicates claim. This literature turn derives no estimate and changes no lemma or script.
LITERATURE_REASON: The turn-start assessment was REVIEW_REQUIRED for actual depth-varying fields, localized finite-cube subtraction and the stronger surface-scale tail, outside the ready L293 audit. Existing adequate bulk/planar coverage was reused.
SCOPE: Exactly TARGET for L280's SU(2) relative cube, even N>=2, a=8/N, all-face pins/fixed gauges, all normal endpoints, exact product bump, both source orders and real source domain, restricted to the normal-normal block on one fixed flat-face patch. The proposed definition and tests below fix the localization/subtraction; their existence and estimates remain research obligations. No other group, boundary stratum or full-box rate is covered.
COVERED_TARGET: Transfer L293's planar cancellation to L282's actual normal source fields on one flat-face patch away from edges, proving an o(N) bulk-subtracted pairing uniformly over the complete external-mode sum.

## Proposed bounded target and source obligations

The main gap remains the interacting continuum construction, nonzero
physical sector and positive mass. The proposed intermediate use is
to test whether the accepted planar cancellation controls an actual
normal boundary contribution below the N-squared coefficient scale.
The test concerns the normal-normal block of the complete
S_N=D_N-A_N/4+E_N/4 pairing with G_-+, localized by a smooth physical
tangential cutoff inside a single face, away from all edges. Preserve
the actual source order sum, density, Wilson slots and mode tail.
The precise depth localization and matching bulk subtraction must be
specified from the existing source formulas during the scope review;
no unrecorded choice is a mathematical premise.

Essential starting inputs are L280 L281 L282 L287 L292 L293. Retain
their inherited L003 L279 L283 L286 L288 L289 conventions, SU(2),
counting measure, even N>=2, a=8/N, all-face pins and fixed gauges,
every normal endpoint, the exact product bump and real source domain.
The slab comparison must respect its three excluded harmonic modes
and tangential-volume-before-thickness order. These are proposed
continuation assumptions, not a new graph or an established transfer.

The source representation and its stated regularity/tail scope have
now been inspected and compared below. Existing literature assessments
are reused where their hypotheses match. The present comparison does
not reopen the stopped generic gauge identity, integration-by-parts
or global absolute-norm mechanisms.

Continuation test: approve a subsequent mathematical attempt only
after the localized pairing and an independently testable boundary
trace/layer estimate with complete mode summability are precise and
covered. An O(N^2) tail estimate alone cannot establish the requested
o(N) bound. If the available estimates cannot supply the surface-scale
test, record that exact mismatch and refine or park this transfer
without treating L293 or the main Yang–Mills target as refuted.

Other field components, other coefficient groups, edges/corners, a
full-box o(N) error, the uniform higher remainder and the interacting
construction remain independent unresolved steps. Full/supporting
Mathlib coverage for this transfer is not checked. This file completes
source coverage for future work; it does not perform that work. The
newly ready assessment receives separate approval next turn.

## Local statement comparison and duplicate/failure check

The actual fields are L282(20)'s
X_(pm,k,a)=(L/a^2)^(-1)(C*/a)(f_* psi_(pm,k,a)), with the reflected
source on the minus side. L282(21) proves fixed-k strong convergence
in physical norm by relative tensor modes. Its paragraph before (19)
explicitly makes no boundary pointwise assertion. Smooth compact
support of the forcing does not itself constitute the missing trace
estimate for its inverse. Keep the cosine grid in the component's own
direction and the sine grids in the other three, with both normal
endpoints. Do not replace the vector inverse by scalar Dirichlet
inverses on every component.

L282(22) retains all three colors and both source orders. Its (23)
controls absolute tails after division by N^2, not by N. L281(7)
has an explicit exponentially summable separated-mode majorant, so
this is not a source-access obstruction. It does not yet bound the
mode constants in a boundary trace norm or the localized signed
defect at surface scale. A growing mode cutoff would also require
uniform approximation errors over that cutoff; fixed-k convergence
alone supplies neither route. No strengthened tail is derived here.

L287(5) discards an O_f(N sqrt(log(eN))+log(eN)) external-curl
reduction error at bulk scale. It cannot be discarded in this test.
Use the complete E from L292(1), including both crossings and all
terms of L293(7), not only E^int. L282's polynomial-density bulk
passage and L288's operator approximation likewise do not assert
an o(N) localized error. L293(10) includes the missing full-line
second vertices; simply subtracting the bulk kernel on the common
positive-depth domain is a different quantity.

No completed actual-source transfer appears in these relevant local
statements or the two planar assessments. This is a scoped duplicate
check, not an assertion about all literature. ATTEMPTS/005 stops the
direct fixed-box locality import. ATTEMPTS/018 and 024 retain their
actual gradient-block and bulk-profile obstructions in the older axial
representation; they warn against an unproved localization, without
proving failure of the present relative-Coulomb signed contraction.
ATTEMPTS/048–049 stop the stated norm-only and generic gauge-identity
arguments. The next attempt uses actual relative fields and the
particular Wilson kernels, and must justify every replacement.

## Proposed localized test: definition, not a new result

Fix the face x_1=-4, which permits a nonzero normal component of
the 12-source field. Set d=x_1+4. Choose fixed smooth real cutoffs
chi on its tangential coordinates and eta on d>=0, with eta=1 near
d=0. Their support is contained in a collar disjoint from every
other face and a fixed positive distance from all edges. Fix them
before N tends to infinity. Let w=chi eta, sampled at normal-edge
centers, and set u_(pm,k,a)=w (X_(pm,k,a))_1 on those edges, zero
on all other components. This is a normal-normal block test; it is
not an assertion that projecting the full field preserves the full
coefficient or its cancellations.

Let S_N^(1) be one fixed color block of the exact S_N=D_N-A_N/4+E_N/4
from L292(1), on the finite cube. Let S_inf^(1) be the corresponding
full-lattice massless Wilson/density kernel, with exactly the same
raw slots and counting measure. Its construction and the convergence
needed for its use are obligations, not new imported conclusions.
For the bulk comparison extend the scalar normal amplitude evenly
across this face: in normal-link indices n>=0, reflection sends
n to -n-1. Denote this extension by u^ev; extend by zero beyond the
cutoff support in other directions. This specifies a comparison
convention, not an assumed identity for the finite-cube inverse.

For ordered signs epsilon,epsilon' define the proposed finite sums

\[
\begin{split}
F_{N,k}^{\epsilon,\epsilon'}={}&
 \sum_{e,f\in E_N^\perp}u_{\epsilon,k,a}(e)
       (S_N^{(1)})_{ef}u_{\epsilon',k,a}(f)\\
 &-\sum_{e\in E_N^\perp}\sum_{f\in E_\infty^\perp}
       u_{\epsilon,k,a}(e)(S_\infty^{(1)})_{ef}
       u^{\rm ev}_{\epsilon',k,a}(f),\\
\mathcal F_N={}&3a^2\sum_{k\in\mathcal K_N}b_{k,a}
       (F_{N,k}^{+,-}+F_{N,k}^{-,+}).
\end{split}
\]

E^perp denotes normal edges; cutoff factors make the displayed
external sums finite. Internal contractions remain complete.
The prefactor is the source/color normalization of L282(22): writing
both orders separately gives 3a^2 with counting sums, rather than
6a^2 for two equal orders. No equality to the entire original
coefficient is asserted. This definition subtracts the full bulk
second-vertex sum, including reflected missing vertices, with only
the first anchor restricted to the cube. It fixes the ambiguity left
in the initial registration. The requested threshold for this one
test is mathcal F_N/N -> 0 through even N, with the complete mode sum.
Changing the bulk extension, collar or assignment of missing rows
requires an explicit comparison, not an implicit new premise.

## Independently testable obligations and abandonment test

A subsequent bounded attempt should first test actual-source control
on this collar from the exact tensor modes. Seek boundary values
converging to the corresponding continuum normal trace, a uniform
physical Lipschitz bound in tangential and normal directions, and
mode-dependent envelopes A_(k,N) with

\[
 \lim_{R\to\infty}\sup_{N\ {\rm even}}
   \sum_{\substack{k\in\mathcal K_N\\|k|>R}}
                 b_{k,a} A_{k,N}^{\,2}=0.
\]

These are desired estimates, not consequences asserted of L282.
One concrete layer test is replacement, for fixed lattice depth M,
of the actual normal fields by their boundary traces with error
vanishing as N->infinity, with mode constants controlled by that
same sum. The exact discrete boundary trace convention must be
matched to the midpoint normal grid, rather than a guessed vertex
value. A direct spectral proof is justified as the missing stronger
boundary/mode statement, not a reproof of L282's L2 convergence.

Then test an N-scale bound for the complete ordered defect, of the
form |3a^2(F_(N,k)^(+,-)+F_(N,k)^(-,+))| <= C N A_(k,N)^2,
or another bound giving the displayed summable tail. The absolute
values are taken after retaining the complete signed contractions;
do not use this proposal to assume an individual-diagram cancellation.
For each fixed mode the actual finite-cube-to-half-space comparison,
deep-layer error and tangential localization error must be o(N)
in this normalization before applying L293's continuous zero value.
The desired remainder split is a depth tail tending to zero after
division by N as M->infinity, plus an error tending to zero at fixed
M as N->infinity, with summable mode constants. This is a test
specification, not a proved decomposition or a new lemma.

Continue on a proved actual-source layer estimate and surface-scale
tail, followed by the stated fixed-mode transfer; a partial source
estimate can be useful even if independent kernel gaps remain.
If the complete signed kernel has no justified N-scale control or
the envelopes are not summable, preserve that precise failure or
unfinished reduction and narrow or park the full transfer. An N^2
tail, frozen plane wave, fixed-depth preview or assumed uniform
cube-to-slab limit fails this test. Keep L292/L293's exact three-mode
harmonic exclusion and tangential-volume-before-thickness order in
any auxiliary slab passage; the original cube's inverse is unchanged.

## Primary results and source access

A. Brandt, *Estimates for Difference Quotients of Solutions of
Poisson Type Difference Equations*, Math. Comp. **20** (1966),
473–499, [author copy](https://www.wisdom.weizmann.ac.il/~achi/LOP3.pdf).
Read Theorems 5.1/5.2, pp. 488–491, 7.1/7.2, pp. 495–497,
and section 8, pp. 497–498, including reflection proofs. The scalar
rectangle results assume zero Dirichlet data or a centered ghost-point
Neumann condition and bounds on the discrete Laplacian. First
differences are bounded; second differences can have logarithmic
mesh losses, with extra corner/Hölder conditions for stronger bounds.
Odd/even reflection preserves the corresponding extended forcing;
section 8 discusses forward conditions. This supports examining
reflection of the exact modes, but does not directly cover our mixed
staggered vector domain, source-mode weights or Wilson pairing.
No theorem from it is imported and no specialization is claimed.

Reuse the primary statements and proof-case readings in
[the planar-boundary comparison](2026-10-26-planar-boundary-mixed-sector.md)
and [the varying-momentum comparison](2026-10-26-planar-normal-external-momentum.md).
In particular Cornean–Garde–Jensen 2211.01974v3, Theorem 3.2 and
appended corrigendum, is an off-spectrum scalar resolvent theorem
with corrected Neumann boundary weights, not a uniform zero-energy
trace theorem for our counting-measure edge grid. Luescher et al.
hep-lat/9207009v1 sections 4.3–4.5 and 6.5 retain different slab
backgrounds and O(a) boundary improvement. Kennedy–Sint 1511.08539v1
sections 2–3.4 provide the inspected scalar wall-renormalization
argument, and Adams–Lee 0709.0781v3 Appendix A retains its infrared
finiteness and parameter-dependent constants. None is an identified
theorem for the localized complete source sum. The assessed continuum
heat coefficients likewise do not identify that sum. Their precise
versions, hypotheses and proof cases remain in those assessments;
there is no reason to reread unchanged passages for a new import.

Strikwerda, Wade and Bube, SIAM J. Numer. Anal. **27** (1990),
292–322, [publisher abstract/reference list](https://doi.org/10.1137/0727020),
exposed a general regularity lead and Johnson, Math. Comp. **28**
(1974), 909–935, *Estimates near plane portions of the boundary for
discrete elliptic boundary problems*. The SIAM full theorem text
was not exposed; the AMS issue/cross-reference fetch failed. These
are unread theorem-level leads, not evidence of applicability or
nonapplicability. Further access is not essential to the proposed
direct exact-mode/kernel test: it assumes no general boundary theorem
from them. Any later decision to invoke them requires separate source
coverage. No purchase, key, general theorem hypothesis or inaccessible
result is hidden in the EXPLORE decision.

The [current Clay page](https://www.claymath.org/millennium/yang-mills-the-maths-gap/)
on 2026-10-27 still links the 14-page
[Jaffe–Witten description](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf).
Section 4, printed p. 6, retains every compact simple group, nontrivial
continuum R^4 theory, axiomatic existence and finite positive mass.
No version change to foundations/01-target-and-scope.md was found.

## Bounded search record and routing

Queries on 2026-10-27 included:

- `discrete elliptic boundary regularity finite difference Neumann Green function smooth forcing rectangular domain estimates`
- `lattice half space boundary layer quadratic form slowly varying external field surface asymptotics gauge theory`
- `finite difference elliptic equations boundary Schauder estimates discrete Green function rectangle`
- `"Regularity Estimates up to the Boundary" Strikwerda Wade Bube pdf`
- `"lattice" "surface" "slowly varying" "one-loop"`
- `"discrete" "boundary Schauder" estimates Poisson lattice`
- `"discrete" "Neumann" "Schauder estimates"`
- `"Estimates near plane portions" discrete elliptic boundary problems pdf`
- `"lattice gauge" "boundary" "external field" "surface" one loop`
- `"Schrödinger functional" "boundary" "spatially varying" perturbation`
- Exact-title/author searches for Johnson and Brandt to locate primary text.

Periodic parabolic Schauder estimates and unrelated finite-element
Green functions were screened out, not imported. A failed search or
unread lead does not establish novelty. The ready bulk and planar
assessments were reused rather than refreshing their searches.

Completed work: literature_comparison, NOVELTY_UNCHECKED,
EXPLORATION. No mathematical advance or informative negative bound
is claimed. Recommend proof_attempt/development, deep_research/xhigh,
for the exact registered target after the supervisor's separate
approval of this changed assessment. The benefit is testing whether
the already audited planar cancellation survives actual fields at
surface scale. The missing trace, complete tail and finite-domain
comparison make this a difficult analytic development, not routine
specialization. Full/supporting Mathlib coverage is not checked.
