# Proposed source comparison: a nonuniform-lattice contour kernel

TARGET: Assess whether nonuniform-lattice interpolation theorems supply a unit-residue replacement for L690's equally spaced contour kernel with quantitative costs sufficient for L666's full-cube complete logarithmic-loss bound.
CHECKED: 2026-11-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 104 searched Kadec/Kadets generating functions, sine-type growth/derivatives, nonuniform unit-residue kernels and perturbed cotangent quadrature; followed Lindner's and the primary literature's Levin--Ostrovskii references. Reused the earlier independent-grid, angular-sampling and Mahler-homotopy assessments and read the relevant local failure/proof ranges. No matching complete-logarithmic bound was found; this is not a novelty certification.
SOURCE_EVIDENCE: Kadets, Dokl. Akad. Nauk SSSR 155(6) (1964), 1253--1254, Theorem 1 and full finite-coefficient proof; Lindner, Growth estimates for sine-type-functions and applications to Riesz bases of exponentials, 20-page author manuscript, Definition 1.1, Theorem 1.4, Theorems 2.1/2.3 and their complete proofs pp.6--10; Levin--Ostrovskii, Math. USSR-Izv. 14(1) (1980), 79--101, Section 2 Theorem 1, Lemmas 2/4 with remarks, full Theorem 1 proof and corollary pp.80--85; NIST DLMF 3.3(i), equations 3.3.1--3.3.3_2 and 3.3.6 with hypotheses. Links, scope and access qualifications below.
COMPARISON: Kadets controls a Riesz basis, not a finite unit-residue contour. Sine-type growth is an additional hypothesis with a precise interpolation criterion; the inspected logarithmic-derivative estimate gives algebraic vertical convergence, not L690's exponential rate. Finite-support extensions satisfy a qualitative source criterion but provide no uniform-in-n costs. Reciprocal generating functions still need residue normalization; finite interpolation supplies no adequate growth estimate. L665 already stops restoring an o(1) inherited-anchor error for the full cube.
GAP: Control the signed, generally nonvanishing kernel correction in the complete logarithmic mean, with absolute constants/onset and every finite side/charge retained. Neither an interpolation basis nor qualitative sine type pays n/100+C*log n. No source supplies this difference, and no new bound or kernel impossibility is proved here.
REASON: Essential primary comparison is complete for one bounded signed-correction test, with the ready Mahler/finite-contour coverage reused. Park direct black-box replacement and exponential anchor recovery. EXPLORE permits the identified mathematical difference; it does not accept a kernel or the desired loss. Newly written continuation scope requires the supervisor's separate next-turn approval.
LITERATURE_REASON: The saved REVIEW_REQUIRED target needed the previously unread nonuniform generating-function hypotheses, residue normalization and vertical/finite-contour estimates. This turn fills that coverage rather than repeating sparse-support or quadrature reviews.
SCOPE: L666's exact full cube and all of the original TARGET; one signed canonical-product correction test for its complete A_n loss is covered. Preserve real independent |e_m|<=1/8, all endpoints and straight paths, unit original residues, fixed anchor, j=0 product, denominator angle 1/u, all M moments and L657's complete K/Q,m_0,Z_n,P_n. No symmetry, periodic shift sequence, uniform sine-type constants, torus separation, small anchor error or unsigned-log transfer may be assumed.
COVERED_TARGET: Test whether the signed canonical-product kernel correction for L666's full independent cube yields A_n(e)>=A_n(0)-n/100-C*log n along every straight displacement path, retaining finite endpoints and L657's complete charges.

## Exact scope and relevance

Keep L666's n=12q+3, M=n/3, fixed x=-5/4, R=11/8, h=27/(10n),
unit original residues, independent real |e_m|<=1/8, and the same vector
at every angular value. The candidate kernel would have to handle
the real scaled nodes m+1/2+e_m, -2q<=m<2q, with the fixed spatial
anchor accounted for separately. No analytic regularity of the shift
sequence, symmetry, periodicity or fixed number of interfaces is given.
Keep all M moments, the j=0 product, denominator angle 1/u and L657's
complete charges. The intended bound is the existing
A_n(e)>=A_n(0)-n/100-C*log n, with absolute constants and onset,
also at each t*e along the straight path. No part of it is derived here.

The proposed difference from exact annihilation is to seek control of
the entire perturbed lattice through a residue representation, rather
than spend two spatial degrees per changed node. The L692 degree/cost
stop remains valid. A representation alone is inconclusive: its residues
must equal one, and its contour and normalization costs must be compared
with L690's finite products and the actual logarithmic target. A bound
on each term, or a norm inequality for different Fourier columns, does
not pay cancellation or complete-logarithm costs.

Retrieve primary statements and essential proof cases for nonuniform
interpolation/generating functions first. Compare with the earlier
angular-sampling assessment without repeating its inspected finite
Fourier and rational quadrature review. Do not assume that a basis
stability result implies a unit-residue kernel, exponential decay,
finite truncation control or a Mahler lower bound.

The original source-review test was to identify a precisely applicable result
and one quantitatively discriminating kernel test, or document the
normalization/decay/finite-endpoint obstruction and park this lead.
Persistent source blockage requires a different independently testable
target, not repeated access attempts. Essential continuation inputs
are L666's exact family/path, L690's contour/kernel and baseline,
L691's two-half comparison, L692's audited degree/cost limitation,
and L657's complete integrability/charges. H/support, actual-Xi
realization and all-degree positivity remain separate unresolved gaps.
Mathlib coverage for this proposed mechanism is unchecked.

## Completed primary comparison — step 104

Representative executed queries were `Kadec one quarter theorem sine
type generating function canonical product perturbed integers pdf`,
`sine type functions perturbation integers bounded Kadec generating
function logarithmic derivative interpolation`, `Kadec exact value
Paley Wiener constant 1964 theorem 2 pdf Kadets`, `nonuniform unit
residues kernel interpolation`, `sine-type logarithmic derivative
interpolation kernel`, `perturbed cotangent kernel quadrature residue`,
and `Levin Ostrovskii small perturbations set zeros sine type 1979
43 87 110 theorem pdf`. Search/catalog passages only located sources;
the decisions below rely on the inspected primary texts. No assertion
of novelty follows from these bounded searches.

### Sources and exact reading limits

**Kadets.** M. I. Kadets, *The exact value of the Paley--Wiener
constant*, Dokl. Akad. Nauk SSSR 155(6) (1964), 1253--1254,
[original Russian paper](https://www.mathnet.ru/php/getFT.phtml?jrnid=dan&option_lang=eng&paperid=29485&what=fullt).
Theorem 1 assumes real lambda_k=k+delta_k with sup|delta_k|<1/4
and concludes that exp(i*lambda_k*t) is a Riesz basis of L2(-pi,pi).
Read its full proof: the finite-coefficient Fourier expansion bounds
the perturbation by 1-cos(pi*d)+sin(pi*d)<1, then applies the
Paley--Wiener perturbation lemma. Theorem 2 is not needed.
Translation by 1/2 and a zero extension of the finite shifts meet this
basis theorem's real perturbation hypothesis. This comparison supplies
no claim that the actual rational W belongs to a Paley--Wiener space,
no finite endpoint estimate and no unit-residue kernel.

**Lindner.** A. M. Lindner, *Growth estimates for sine-type-functions
and applications to Riesz bases of exponentials*,
[undated 20-page author manuscript](https://www.uni-ulm.de/fileadmin/website_uni_ulm/mawi.inst.050/people/lindner/lindner3.pdf),
checked 3 November 2026. Definition 1.1 requires entire exponential
type and C1*exp(sigma*|y|)<=|F(x+iy)|<=C2*exp(sigma*|y|) for
|y|>=tau, uniformly in x. Theorems 2.1 and 2.3, pp.6--10, require
these growth constants and a zero-count bound S_r in every real
interval of length 2r; 2.3 additionally requires separation delta.
They quantify lower bounds away from zeros and C3<=|F'(lambda)|<=C4.
Read both proofs: vertical product comparison, near/far zero groups,
the limit at a simple zero, and the maximum-principle upper bound.
The constants retain C1,C2,tau,S_r,r,delta and zero-strip width.
These results do not assert sine type from a small perturbation alone,
constant derivatives at the nodes, or one-sided exponential decay of
a unit-residue kernel. Section 3's basis estimates are not imported.

**Levin--Ostrovskii.** B. Ya. Levin and I. V. Ostrovskii, *On small
perturbations of the set of zeros of functions of sine type*,
Math. USSR-Izv. 14(1) (1980), 79--101,
[English primary text](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=1676&what=fullteng),
Section 2, pp.80--85. Theorem 1 assumes a sine-type S, S(0)=1,
and bounded zero shifts psi_k. Its normalized perturbed product is
sine type iff a bounded-on-R entire phi of type at most sigma meets
phi(lambda_k)=psi_k*S'(lambda_k) at simple zeros, with the stated
Hermite conditions at multiple zeros. Read the full proof, including
the logarithmic-ratio remainder, necessity/sufficiency, and the
ell^p (1<p<infinity) corollary. A finite zero extension meets that
corollary, but it gives no n-uniform constants. Lemma 2 and its
proved remark, pp.81--82, bound S'/S away from zeros and obtain
uniform limits -i*sigma above and +i*sigma below, with the displayed
O(1/(|y|-H)) estimate. This is algebraic, not the required exponential
estimate. Lemma 4 and remarks retain bounded logarithmic ratios.
Later asymptotic expansions are unread and not inputs.

**Finite normalization comparison.** [NIST DLMF 3.3(i)](https://dlmf.nist.gov/3.3#i),
equations 3.3.1--3.3.3_2, gives unique degree-at-most-s-1
interpolation at s distinct complex nodes and explicit derivative
weights 1/omega'(lambda_k). Equation 3.3.6 assumes analyticity in
a simply connected domain and a positive simple contour enclosing
the evaluation point and nodes. The real differentiable remainder
3.3.5 cannot be used for a complex contour. These formulas make
finite residue normalization an explicit problem; they do not bound
its contour growth at the needed scale. No normalization polynomial
or specialized remainder was constructed in this turn.

The TUM Lindner mirror returned HTTP 429 on follow-up; the author copy
resolved access. Mathnet mobile/full-text calls initially timed out;
the desktop links above subsequently exposed the primary texts and
relevant proofs. There is no remaining essential source blocker.
Austin--Trefethen's arXiv statement was initially opened, then the
adequate published-version review in
`2026-11-02-independent-grid-displacement-paid-arc.md` was found and
reused; its proof was not reviewed again. Kadec's original lead is now
inspected, rather than left at the older angular-sampling search stage.

### Normalization, decay and finite costs

L690 (7)--(12) uses actual unit residues and a kernel bound proportional
to n*exp(-lambda*n*(-v)_+), lambda=20*pi/27, on every side of
Gamma_n=[-2qh,2qh]+i[-2/25,1/8]. Its signed integral includes
the fixed anchor separately and the entire M-term spatial polynomial.
The saved contour envelope has margin 1/500 before its explicit
finite-side O(1) cost. It is this exponential payment, rather than
basis conditioning, that makes the anchor approximation work.

The following are comparisons with the needed hypotheses, not new
theorems or same-turn derivations:

- A reciprocal generating function has the simple-pole normalization
  1/S'(lambda_k); the previously inspected simple-pole rule requires
  correcting these values to recover original residue one. Merely
  bounding their magnitudes does not correct their phases or values.
- The logarithmic derivative uses unit multiplicities at simple zeros,
  but the inspected vertical estimate does not supply L690's decay.
  An infinite sequence and a bounded-width strip estimate do not by
  themselves pay the finite rectangle's sides after rescaling by h.
- The source ell^p corollary applies qualitatively to each finite
  extension. Its unrestricted dependence on that extension cannot be
  replaced by constants uniform over all q and all shift vectors.
- Polynomial interpolation can enforce finite values. Its degree,
  normalization and contour growth remain costs; existence alone
  does not prove a complete-logarithm comparison near torus zeros.

Thus the black-box sources do not import the desired kernel or the
complete loss bound. This is a source mismatch, not a proof that every
possible nonuniform kernel or the full-cube inequality fails.

### Duplicates, failures and the changed route

Read L666's exact family/path and L657's complete identities,
L690 Sections 2--4, L691's exact two-half statement, and L692's
complete-mean statement and Sections 5--6. Reused
`2026-11-03-independent-shift-mahler-homotopy.md` for growing-degree
Mahler variation/zero-crossing coverage and
`2026-11-02-displaced-signed-angular-sampling.md` for the already
inspected finite Fourier and rational quadrature comparisons.

Targeted failure searches located
`ATTEMPTS/2026-11-02-independent-displacement-anchor-transfer-stop.md`
and its canonical L665. Read L665 hypotheses, conclusions and
Sections 2--3: its one-node family is exactly a permitted L666 shift,
and its response has an order-one limiting anchor error at u=-1.
Its separate absolute node-polynomial comparison is also stopped.
L665 remains unaudited; this review does not independently certify it.
Nevertheless a proposal requiring the already contradicted o(1)
anchor conclusion cannot silently ignore that recorded evidence.
L692's 2s old-and-new degree stop remains a different, intact limit.
The clustered minimum-interpolant stop concerns different support;
it is not a global prohibition on separated-lattice interpolation.

Park **direct** recovery of L690's pointwise decaying remainder for
the full cube. A viable continuation must permit a nonvanishing
signed correction and test its logarithmic contribution, rather than
renaming the absolute finite-kernel comparison. This distinction was
absent from the original unread nonuniform-source proposal.

### One bounded continuation

The exact COVERED_TARGET is a proposed mathematical test, not a result.
Use the normalized perturbed sine product and the logarithmic-ratio
decomposition in the inspected Section 2 proof to organize the signed
kernel correction. Start with its exact finite residue census and
keep the correction in the response, including both vertical sides;
do not assume it is a small error or use a basis-norm-to-log bridge.

The discriminating test is whether this signed correction can pay
the complete loss <=n/100+C*log n with absolute C/onset along the
whole straight path. Continue only for a proved such bound or an
explicit partial signed-charge estimate leaving a quantified budget.
An admissible asymptotic countersequence, or a proved excess cost for
this specific signed decomposition, is a useful negative. A repeat of
L665's o(1)-anchor contradiction or of its unsigned contour estimate
is not new evidence. If the decomposition only returns that stopped
estimate, abandon this mechanism without another identical attempt.

Essential inputs are L666's exact independent family, L657's complete
integrability/charges, L690's audited baseline, L691's allowance for
nonvanishing corrections, L692's full-support degree stop, and the
known-source inputs just compared. Uniform finite constants,
normalization, the signed-log transfer and torus-zero accounting are
unresolved. H/support, actual-Xi realization and all-degree positivity
remain independent gaps. No specialized kernel, inequality or RH
candidate was derived or adopted into the proof in this literature turn.

**Mathlib.** Full matching coverage for nonuniform sine-type kernel
normalization and this signed complete-logarithm comparison is unchecked.
Reuse the earlier assessed univariate Mahler support only within its
recorded hypotheses; it supplies no full-cube estimate. No general
source theorem is to be reproved in the proposed attempt.
