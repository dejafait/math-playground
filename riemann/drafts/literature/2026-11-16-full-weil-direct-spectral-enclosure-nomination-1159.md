# Direct complete-form spectral enclosure: completed source review1160

TARGET: Assess source coverage for a direct lower spectral enclosure of the complete Weil form at b=log(101)/2 using the first64 Dirichlet sine modes and a rigorously controlled infinite-dimensional complement.
CHECKED: 2026-11-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1160 searched logarithmic-Laplacian/sine/Galerkin lower enclosures and complete-Weil complement bounds; compared the named local1139/1140/1155,791/792,561/619/620 records and the signed-localization stop583/584. Reused the October30 support-enlargement assessment after finding its exact Zhu coverage; no novelty inference.
SOURCE_EVIDENCE: Inspected Liu2607.04247v1 Assumption2.1, Theorem2.2 and both proof cases, Lemma3.1/proof and Section4.1; Zhu2608.24827v2 Theorem1.1, Lemmas3.1/3.2, Section4/(12)-(13), Lemma6.1/proof, Section7 and Section11.1/(16); Teschl2009 Section6.3/(6.8)-(6.18),(6.21), Lemmas6.9/6.10 and proofs. Reuse1140/791 for Suzuki and C750f for the complete-form/domain qualification; exact URLs below.
COMPARISON: Direct Laplacian modal constants and paper162's Neumann-response constants do not transfer to the nominated sine split. Zhu supplies an explicit frequency-split lower form and a complete block-norm criterion; Teschl supplies basis-independent squared-kernel/tail control. These support one analytic feasibility specialization, not a ready sine-tail margin or a positive spectral enclosure.
GAP: At unchanged b,N=64, justify the closed-domain lower-form comparison and compute complete sine-complement/coupling bounds; source Legendre decay is inapplicable. A strict positive full lower bound remains unproved, as do all-support positivity and actual-Xi assembly.
REASON: The located quantitative lower-form mechanism passes the setup admission test, unlike finite Ritz values or qualitative compactness alone. Approve only a separately gated analytic feasibility attempt before head assembly, with failure stopping this fixed certificate. No calculation, lemma or mathematical script was produced here.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED concerned an unassessed fixed-domain sine projection; the exact lower-enclosure and tail hypotheses were essential missing coverage. Existing domain/Schur assessments were reused rather than refreshed indiscriminately.
SCOPE: Full complex unneutralized form at b=log(101)/2, all prime powers n<101 and both pole moments; first64 nominated sines unchanged. Known-method lower-form/tail specialization only, not a sine eigenbasis identification or a copied source certificate. The newly saved continuation requires separate next-turn approval.

## Completed comparison1160

Main gap: L030-L032/C032a actual-Xi mixed positivity in every degree.
The intermediate target is a lower enclosure on one complete supported
form. It could supply a finite-window input to later support work;
arbitrary supports and actual-Xi realization would remain independent.
No new inequality or numerical value is established in this source turn.

### Primary hypotheses and proof cases

* Xuefeng Liu, *Guaranteed Lower Eigenvalue Bounds for Spectral Galerkin
  Methods with Application to Schrodinger Operators*,
  [arXiv2607.04247v1](https://arxiv.org/html/2607.04247v1), served header
  5July2026, internal submission24August2026: Assumption2.1 and
  Theorem2.2/(2.1)-(2.4), both injective and noninjective proof cases;
  Lemma3.1/(3.3)-(3.4) and proof; Section4.1/(4.6)-(4.9).
  The positive-form theorem needs an energy-orthogonal projection and
  its error constant. The explicit modal constant uses an exact
  reference eigenbasis; the Schrodinger application has gradient energy
  and a nonnegative bounded multiplication potential. Those are not
  this logarithmic form with signed shifts/poles. A shift would still
  require a quantified error constant. No such constant is imported.

* Xuefeng Zhu, *Weil positivity in compact windows*,
  [arXiv2608.24827v2](https://arxiv.org/html/2608.24827v2), header
  2September2026/internal3September: Theorem1.1/(4), Lemmas3.1/3.2,
  full Section4/(12)-(13) proof, Lemma6.1 and Section7.
  For T>=15/4 the symbol envelope uses the full positive comb mass A;
  the split needs beta=log(T/(2pi))-1/T-A>0. It retains the pole and
  bounds the entire omitted frequency integral from below. Its block
  criterion pays complement deviation and coupling separately.
  The Legendre decay constants cannot be used for sines. Section11.1
  gives exactly the nominated sine space and transforms(16), for
  upper trials. The support2.38 lower claim is retracted. Only the
  analytic reduction and generic block criterion are proposed inputs;
  no source numerical certificate or fitted law is imported.

* Gerald Teschl, *Mathematical Methods in Quantum Mechanics*, GSM99,
  [author version12February2009](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf),
  Section6.3 pp139-141: (6.8)-(6.13), Lemma6.9/proof, Lemma6.10/proof,
  Corollary6.11/proof and (6.21). A square-integrable kernel defines
  a Hilbert-Schmidt operator; its squared norm equals the complete
  sum over any orthonormal basis and dominates operator norm.
  Orthogonal compressions remain in the ideal. This allows squared
  tails, rather than assuming absolute row sums converge. Any
  application must first identify the bounded reduced operator and
  justify its kernel and complete projected-tail integrals. It does
  not apply automatically to the unbounded original log multiplier.

Reused source scope: Suzuki2606.09096v3 Theorem1.1/Corollary1.2 and
Sections3.2,4.1-4.4 as inspected791/1140 provide realization, core and
qualitative compactness/continuity, not the needed sine error constant.
Laptev-Weth revised2020 Section2 and Theorem4.1, including its counting
proof, concern the zero-extension compressed log multiplier; its
spectral count is not coercivity on an arbitrary sine complement.
The primary URLs are retained in1140. C750f's cited paper162/v1(2),
(4)-(7) and Section6 were checked against the primary text:
https://rstation.ai/problems/riemann_hypothesis/papers/162 .
Its explicit boundary representation uses different, Neumann-endpoint
parity coordinates; its theorem ends at9/4, and its Schur margins are
not numerical full floors at the nominated support.

### Duplicate/failure comparison and decision

The October30 support-enlargement assessment already read Zhu's lower
reduction and retraction; this review reuses that finding and reads the
newly relevant exact sine and squared-tail cases. This is not discovery
of a new source method. Its Liu tail-dropping obstruction concerns a
specified different comparison, not an automatic refutation of Zhu's
complete frequency-split lower form. No old comparison is reopened.
Reviews561/619/620 use neutral endpoint/energy-image coordinates;
791/792's full odd test uses a different window and Fourier split.
The signed-localization583/584 stop warns that coefficient support is
not Fourier support. None supplies the present sine complement sign.
The retired C750i/k/l trace/fixed-middle family,1139/1140 relative
budget and C750f's external-certificate qualifications are preserved.

The direct generic-Galerkin shortcut is rejected. A concrete alternative
within the SAME enclosure target is the cited bounded frequency-split
lower form followed by squared-kernel estimates in the unchanged sine
coordinates. This gives computable full-complement and coupling objects
without assuming a baseline floor. Their effectiveness at64 is UNKNOWN.
The next assessment specifies one fixed source cutoff and analytic
admission test; no matrix run, new bound, positivity, or theorem
specialization has been performed or proved in1160.

If these explicit bounds fail to leave positive complement coercivity,
stop this certificate without increasing64, changing support, optimizing
the cutoff or starting head assembly. If they leave room, save the
complete coupling/error requirement for a later separately assessed
head certificate; this turn does not authorize it. Failure of a lower
comparison is not a negative original-Weil direction or a disproof of RH.

Search queries included `logarithmic Laplacian rigorous eigenvalue lower
bounds Galerkin complement sine basis`, `Weil quadratic form lower
complement spectral`, `eigenvalue lower bounds block operator complement
coercivity residual Schur Rayleigh Ritz unbounded operator`, `Weil form
Dirichlet lower bound sine`, and exact radius/log101 positivity searches.
No stronger endpoint theorem matching b was found in this bounded search.
Paper163/v1's Theorems1/2 and near-radical statements appeared as a lead:
they expressly supply no complementary gap; no claim or proof from them
is imported. Other search hits and unseen supplements remain unread.
No essential source-access blocker was encountered. Matching Mathlib
coverage is unchecked; unknown does not mean absent. No cross-notebook
input. There is no justified creative nomination: the paid all-support
signed resource remains missing, and this is ordinary specialization.

Outcome: EXPLORATION, LITERATURE/REPRODUCTION. Source coverage now
supports a bounded quantitative test, not an advance beyond the sources
or a solution. No lemmas/, scripts/, DAG or PROOF changes. The initial
status output and one batched read were oversized/truncated; no claim
uses their previews. Needed statements were subsequently read narrowly.

## Original nomination1159 (historical scope; unchanged mathematics)

## Main gap and proposed bounded object

L030–L032/C032a require actual-Xi mixed positivity in every degree.
A complete positive lower bound at one larger support could provide
an independently checked finite-window input for later support work;
all supports and the main mixed-positivity gap would still remain.
The point of this nomination is to test that intermediate input
directly, without spending further turns on the fixed97 allocation.

Use the complete form with the Fourier/digamma, pole and prime
normalizations recorded in C750f and paper162/v1(2), now on (-b,b).
The exact larger-support formula and closure must be checked from the
primary source before any use. Define the proposed L2 projection onto

    phi_n(x)=b^(-1/2)sin(n*pi*(x+b)/(2b)),  |x|<b,
    phi_n(x)=0 outside (-b,b),  n=1,...,64.

This defines a test space only. No matrix entry, complement bound,
ground-state approximation, sign or Schur identity is established by
writing it down. Both reflection sectors and arbitrary complex
coefficients are retained. Neither neutrality nor a pole cancellation
may be imposed. Do not confuse the supported sine projection with a
whole-line frequency cutoff, or compression of log|D| with the log
of a Dirichlet Laplacian.

## Three mechanisms compared and recovery decision

1. An arbitrary-interior trace minimization could retain more of J
   than C750l, but assessment1155 has no quantitative supported trace
   lower bound. The audited positive affine minimum supplies only an
   upper trial value for such a minimization. More response shapes
   would repeat the retired witness search and are not selected.
2. A complete energy-relative dilation bound is already parked in
   review1139/1140. Its missing effective baseline comparison is not
   repaired by the finite-family exclusion. Generic KLMN and unknown
   constants do not justify reopening it; its stop is preserved.
3. The selected direct target works at the final support and seeks a
   lower enclosure of the entire form through one fixed projection
   plus its infinite complement. It avoids a presumed baseline floor
   and includes every signed interaction. Its own quantitative tail
   and mixed-block obligations are essential and are currently open.

The bounded source test is whether an inspected theorem, with all
hypotheses matched, yields computable complement and coupling bounds
for this fixed projection, sufficient to set up one full-domain
strict-positive-lower-bound test. First check duplicates and failures
in the named local records; follow only narrowly relevant references.
If the exact result is already known, import it precisely. If only
finite Ritz values, a qualitative compact-resolvent statement, an
unavailable spectral floor or the same stopped neutral-coordinate
allocation is obtained, record that obstruction and park this target
without increasing64, changing the support or starting a matrix run.
An inconclusive enclosure would not be a counterexample to positivity.

No external source access failure is asserted by this nomination.
The source scope is incomplete because the object has changed; the
next turn is literature-only. Potential standard-method specialization
must not be labeled creative. A central creative nomination remains
blocked until an independently signed all-support mechanism or a
specific new way to pay these full-domain bounds is identified. No
novelty, spectral sign, lemma or mathematical script on this new target
is produced or approved during audit1159.

Essential prospective inputs are L030–L032/C032a for the goal,
L744(6) and C750f for exact complete-form normalization/domain and
source qualifications, and review1139/1140's fixed-endpoint comparison.
The local complement/parity records are contrasts, not mathematical
premises. C750i/k/l contribute no bound on the full Weil operator.
The baseline paper162 numerical supplement remains externally
qualified and is not replayed here. Matching Mathlib coverage is
unchecked. No cross-notebook input is proposed.
