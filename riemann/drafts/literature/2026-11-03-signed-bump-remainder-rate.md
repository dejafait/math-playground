# Source assessment: the actual signed positive-bump remainder

TARGET: For the same fixed actual L703 profile at u_*=(3+4i)/10, determine the exponential rate of L713's signed positive-bump remainder R_n(3/20), without taking absolute values inside either integral.
CHECKED: 2026-11-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 174 compared exact/growing-product complex-saddle, uniform inversion and compact Gevrey-bump searches with L703/L708/L713 and the recorded absolute-contour and positive-blend stops; inspected primary statements and relevant deformation/error cases listed below. No matching signed-rate theorem was found in this bounded search; this is not a novelty claim.
SOURCE_EVIDENCE: Pemantle--Wilson arXiv:0903.3585v1 Theorem 2.3/Corollary 2.4 and Sections 4--5 https://arxiv.org/pdf/0903.3585v1 ; Johnson arXiv:1508.04376v1 Sections 2--3 https://arxiv.org/pdf/1508.04376v1 ; Colmey--Lascar arXiv:2503.04189v1 Lemmas 2.1/5.1 and proofs pp.5,20--23 https://arxiv.org/pdf/2503.04189v1 ; NIST DLMF 2.4(ii)--(v) https://dlmf.nist.gov/2.4 , 2.10.1 https://dlmf.nist.gov/2.10#E1 , 5.5.1 https://dlmf.nist.gov/5.5#E1 and 5.11(i)--(ii) https://dlmf.nist.gov/5.11 . Reuse L708's saved finite-complex-measure/inversion sources; exact hypotheses and reading limits below.
COMPARISON: Analytic saddle theorems require a paid contour, isolated nondegenerate critical points and analytic amplitudes; the inspected Gevrey tools allow nonanalytic amplitudes but give absolute stretched-exponential errors rather than the required signed relative control. Johnson treats explicit endpoint laws absent from the actual plateau bump. Product tools do not settle the outer cancellation. None imports the exact target.
GAP: Bound the actual signed R_n(3/20) on n=12q+3, retaining the same fixed plateau bump; justify finite-product uniformity, contour tails, competing contributions and possible cancellation zeros before comparing its upper/lower exponential rates with the actual P_n. A limit or nonvanishing is not assumed.
REASON: Essential general tool comparison is complete enough for one bounded mathematical attempt on the unchanged target; the unpaid signed analysis is the research gap, not an inaccessible essential theorem. EXPLORE approves an attempt only, not an asymptotic, a Gaussian constant or a Gevrey specialization. No new mathematical result is derived in this literature turn.
LITERATURE_REASON: The new relevant lead is signed complex-saddle analysis before either absolute value, replacing the now-obstructed absolute horizontal-contour certificate. Its uniformity and cancellation cases for a fixed compact Gevrey bump are outside the inspected source coverage.
SCOPE: Exactly TARGET, c=3/20, u_*=(3+4i)/10, n=12q+3, the original L703 choices fixed before n and L713's full signed definition; analysis in the rational integration variable may keep the bump variable real. No replacement bump, n-dependent profile, nonvanishing, saddle dominance, full-J_sp or Xi-sign premise is approved.

## Original nomination, preserved as historical scope

The paragraphs below record the pre-review nomination. Their requirement
for a literature-only next invocation has been discharged by step 174;
their mathematical restrictions and independent gaps remain.

The exact observable R_n(c), transform convention and complete-family
decomposition are in L713. Keep c=3/20 fixed and u_*=(3+4i)/10;
the profile, width and cutoffs precede n. Essential inputs are L666,
L703 and L708, with L713's new-center identity requiring careful
verification. L709--L712 are comparisons and possible source pointers;
their i/2-arc rate inequalities are not hypotheses at u_*.

The immediate discriminating comparison is the actual signed
remainder against the actual residue P_n, not against a numerical
sample or U_n. A rigorous subdominant remainder would remove one
obstruction to the boundary-peak test; the other frequency terms,
comb, both physical tails, finite moments, a spatial low-value arc
and persistence on an angular arc would still need proof. A rigorous
competing signed rate would change the peak choice. An inconclusive
saddle expansion without paid cancellation zeros would not decide it.

The literature review should preserve this mathematical target and
first retrieve exact hypotheses and relevant proof cases. In particular,
the amplitude is the ACTUAL fixed Gevrey bump, not an analytic
replacement or an n-dependent chosen profile; the product has n
factors; and neither an unproved relative error nor a lower bound for
an oscillatory transform may be assumed. Check duplicates and stronger
known results before deriving a new specialization. A primary theorem
meeting the hypotheses should be imported by precise citation; if none
is found by a bounded documented search, record EXPLORE without a
novelty claim. This nomination is not an assessment approval.

The possible downstream use remains the normalized spatial Jensen
defect test; actual-Xi signs, angular amplitude/full charge, H/support
and realization remain open. Full matching Mathlib coverage is not
checked. No lemma or mathematical script for this new target is
created by this nomination.

## Completed comparison — step 174, 3 November 2026

The main gap is actual-Xi all-degree mixed positivity. This intermediate
target tests the proposed peak in the complementary spatial Jensen
defect argument: an actual signed remainder subordinate to the residue
would remove one local obstruction; a certified competing contribution
would require revising that peak. Neither outcome pays the complete
logarithmic mean or transfers the constructed family to Xi.

### Exact data and local duplicate/failure check

L713's Hypotheses and Section 1 define R_n and P_n, with h=(27/10)/n,
c_0=1/8 and the rational product W_n. In particular its (2)--(4) retain
the signed contour identity and every complete-family correction.
Those formulas are the proposed input, not an independently audited
result of this source review. L703's Hypotheses prescribe a fixed even
Gevrey-2 plateau eta, its support, positivity and plateau interval;
they do not prescribe an explicit endpoint asymptotic. Any conclusion
must state its dependence on the already selected eta and w. Quantified
generically, it must hold for the stated selections, rather than choose
a more convenient bump after n varies.

The specific prior records checked were
`ATTEMPTS/2026-11-03-spatial-boundary-absolute-contour-stop.md`,
`drafts/literature/2026-11-03-fixed-profile-spatial-jensen-defect.md`,
L708's source/width sections, and
`drafts/literature/2026-11-02-positive-blend-saddle-audit.md` with
its corresponding ATTEMPTS record. The real signed-blend argument
concerns other profiles and observations. L713's absolute-envelope
failure is not a signed lower bound. Neither duplicate settles this
unchanged fixed-bump observable. Earlier i/2 arc rates are not data at
u_*. No zero-free-region or reciprocal-series route is reopened.

### Inspected primary results and their boundaries

1. **Analytic complex phase.** R. Pemantle and M. C. Wilson,
   *Asymptotic expansions of oscillatory integrals with complex phase*,
   arXiv:0903.3585v1 (20 March 2009), Theorem 2.3 and Corollary 2.4,
   PDF pp.4--5; Theorem 4.1, pp.7--8; deformation arguments pp.10--14.
   Theorem 2.3 assumes a compact oriented real-analytic stratified
   d-space in C^d, A and phi analytic near it, Re(phi)>=0, and finitely
   many stationary points (critical with Re(phi)=0), each interior
   and with nonsingular complex Hessian. It gives an additive saddle
   expansion with phase-dependent contributions. Corollary 2.4 permits
   boundary points locally modeled on a halfspace, with half weight.
   Read the strict-minimum contour projection and the Section 5 flow,
   holomorphic Stokes step, localization and halfspace case. These
   use holomorphy, not merely C-infinity regularity. The coefficient
   sum itself can cancel. No uniform triangular-array conclusion is
   asserted in these statements. The printed v1 Gaussian coefficients
   are not imported or independently normalization-audited here; the
   author offprint returned 403. This review uses the hypotheses and
   proof mechanism, not a numerical prefactor.

2. **Specific flat endpoints.** S. G. Johnson, *Saddle-point integration
   of C-infinity “bump” functions*, arXiv:1508.04376v1 (18 August 2015;
   note updated 19 August), Sections 2--3, PDF pp.2--5. Read the
   endpoint expansion, accessible complex saddle, deformed Gaussian
   path and generalized explicit endpoint family. The starting bump
   is exp(-1/(1-x^2)) on (-1,1); the answer is the real part of an
   oscillatory complex expression with a stretched-exponential
   envelope. It is not a nonzero lower bound. No theorem there treats
   every compact Gevrey plateau or this growing rational product.
   Its numerical comparison is not proof of our target. Replacing
   eta by this explicit non-plateau bump is outside scope.

3. **Gevrey alternative.** B. Colmey and R. Lascar, *Partial Differential
   Operators and Fourier Integral Operators in the Gevrey setting and
   applications*, arXiv:2503.04189v1, PDF pp.5 and 20--23, Lemmas 2.1
   and 5.1. Lemma 2.1 assumes uniformly Gevrey-s phase and symbol,
   compact integration support, Im(f)>=0 and Re(f'_x) nonzero where
   Im(f)=0 on that support. It gives an absolute exp(-h^(-1/s)/C)
   bound, with locally uniform parameter derivatives. Lemma 5.1 uses
   the special phase a(y,X)=(y-z)eta+phi(z), Im(phi)>=0, a real base
   critical point with nonsingular Hessian, local compact Gevrey
   amplitude and an almost-holomorphic extension. Its Stokes error
   (5.40) is of absolute size exp(-h^(-1/(2s-1))/C). Read the
   integration-by-parts optimization and the complex proof
   (5.17)--(5.40), including the parameter-analyticity qualification
   before (5.35). It does not directly assert our general two-variable
   rate. The HTML and PDF were inspected; isolated notation/sign
   slips are not silently repaired or used as new inputs. References
   [3], [4] and [6] were identified, not independently re-audited.

4. **Contour and inversion reference.** NIST DLMF version 1.2.8
   (15 September 2026), 2.4(ii)--(v), especially (2.4.7)--(2.4.15).
   Read the inverse-transform subtraction conditions, analytic-path
   hypotheses, convergence and strict complementary real-part gap,
   and the interior-minimum split. With no saddle, the two formal
   expansions cancel; with a simple saddle the half-integer expansion
   requires nonzero second derivative and the permitted paths.
   The coalescing-saddle discussion assumes analytic phase/amplitude
   in the integration variable and parameter continuity. These
   statements do not provide our missing contour or lower bound.
   The cited book proofs and additional coalescence sources were
   not independently read; no coalescence is assumed absent here.

5. **Finite-product tools.** DLMF (2.10.1) assumes integer endpoints
   and positive integer order m, with the required derivatives and
   absolutely integrable 2m-th derivative, and includes its explicit
   Bernoulli integral remainder. It can be used on complex functions
   componentwise after fixing a legal logarithm. DLMF (5.5.1) is the
   gamma recurrence, as a meromorphic identity. DLMF (5.11.1)--(5.11.3)
   gives sectorial Stirling expansions away from the negative ray;
   5.11(ii) gives complex remainder bounds. Its fixed-shift ratio
   formulas are not uniform theorems for shifts growing with n.
   Read these statements and error conditions; their cited book
   derivations were not audited. No product-to-gamma reduction,
   logarithm choice or derivative bound is derived here.

### Applicability, unpaid estimates and permission to attempt

The analytic inner integration variable and the real fixed-bump
variable need separate justification. Keeping the bump variable real
avoids demanding its holomorphic extension, but does not remove its
oscillatory integral. A locally valid inner saddle expansion with an
absolute error may still be useless relative to the signed outer
integral. Uniformity must be paid over the actual support, for the
finite n-factor product and the unbounded integration tails. The
original branch/pole structure cannot be replaced by a modulus
Riemann sum. Possible saddle collisions, endpoints, residues and
competing contributions have to be retained if encountered.

In particular the Gevrey tools reviewed above do not supply a linear
exponential accuracy claim for this observable. They are comparisons,
not a lower-bound theorem. A proof may use known contour/product
inputs by citation and then supply the family-specific estimates;
there is no justification to reprove the general analytic or Gevrey
theorems. If a stronger general theorem becomes essential, its new
hypotheses require another source gate. Otherwise this EXPLORE
assessment permits the bounded attempt on TARGET without more
routine browsing.

The continuation test is to obtain a proved signed upper/lower
exponential comparison with the actual P_n, along the full permitted
sequence or with explicitly recorded exceptional/zero subsequences.
Use extended logarithms with log(0)=-infinity; do not infer that a full
limit exists. A strict subordinate rate would permit this local peak
test to continue. A proved competing contribution or forced
cancellation would change the peak mechanism. If only U_n, an
uncertified saddle picture or an absolute error larger than the
proposed signed main term is obtained, record that failure and do
not repeat it without materially new input. No such comparison is
established by this review.

Essential local inputs remain L703, L708 and L713, with L666 supplying
the complete family. L713 is unaudited. Other frequencies, the comb,
both finite physical tails, all moments, an angular arc, complementary
defect, amplitude/full charge, H/support and Xi realization remain
unpaid. Full matching Mathlib coverage is not checked. None of the
general results reviewed is a formalization of this target.

### Bounded search and access record

Queries actually issued included:

- `uniform asymptotic saddle point integrals smooth nonanalytic amplitude Gevrey complex phase cancellation`
- `growing product rational functions Laplace inversion saddlepoint uniform asymptotic theorem`
- `Steven Johnson saddle point integration C infinity bump functions Fourier transform asymptotics`
- `Pemantle Wilson "Asymptotic expansions of oscillatory integrals with complex phase" pdf theorem 2.3`
- `Gevrey complex stationary phase theorem smooth amplitude almost analytic exponential remainder`
- `uniform saddlepoint approximation sums independent non identical complex measures cancellation product rational`
- `"Partial Differential Operators and Fourier Integral Operators in the Gevrey setting" stationary phase`
- `"Gevrey" "stationary phase" "complex" Hitrik Lascar Sjostrand Zerzeri theorem`
- `"Gevrey" "plateau" "saddle" "Fourier"`
- `"rational product" "saddle point" Laplace integral asymptotic`
- `"compactly supported" "nonnegative" "Laplace transform" complex zeros asymptotic Gevrey`
- `"0903.3585" "Theorem" "uniform"`

The probability-saddle abstracts concern positive random laws and
are unread at theorem level; they cannot be applied to the complex
factor measures at u_*. The Padova preliminary Gevrey note timed out;
the NSF-hosted complex stationary-phase PDF returned 502. They remain
unread leads, not essential blockers after the accessible primary
alternatives above. The mistaken unrelated arXiv URL 2503.13657v1
was discarded without using its content. A local curl attempt failed
DNS resolution; primary text remained available through web access.
No search failure establishes novelty or impossibility. Stop the
source search here and attempt the assessed mathematics next.
