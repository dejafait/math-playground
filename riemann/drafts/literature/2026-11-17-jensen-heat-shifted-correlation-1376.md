# Proposed signed shifted-correlation test1376

TARGET: Assess primary-source coverage for the negative shifted-correlation test (C) for C019k's moving-time sum at h_d=3*pi/log(Y_-), including the actual cutoffs and gamma phase.
CHECKED: 2026-11-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1377 searched shifted Hardy-Z/heat correlations, the exact deformed Riemann-Siegel terminology, Selberg's cited formula, Bettin1111.0925 and Atkinson1948; read the primary items and proof cases below and reused assessment1372/stops1345/1355/559. No matching heat-weighted theorem was located; no novelty inference.
SOURCE_EVIDENCE: Read Bettin1111.0925v1 Theorem1/Lemmas1-2/proof, Koesters0803.1141v2 Theorem1.1 and Section2/(2.4)-(2.6), AppendixA.1-A.3, Gonek-Ivic1604.00517v1 Lemma3/(2.9), and Mawia2019 pp239-240 cutoff correction; refreshed Polymath1904.12438v2/(5),(13)-(19). Exact scope and unread originals below.
COMPARISON: Ordinary microscopic shifted moments and an explicit real-part product proof mechanism are known; the present band has length comparable to its height, so the old microscopic-outer-window objection is not the obstacle. No inspected theorem covers the actual moving heat weights, gamma phase and two source floors in (C).
GAP: Directly test the signed leading coefficient and remainder on the B_d*log(Y_-) scale with both actual floors, retaining conjugated and unconjugated products and the heat phase. Negativity and every transferred sign/root conclusion remain unproved.
REASON: The source comparison is complete for a bounded direct finite-sum attempt, not an import of (C). Primary proof cases and standard oscillatory tests are available; inaccessible historical originals are not premises of that independent attempt.
SCOPE: C019k's exact actual-xi normalization, integer d tending to infinity, t_d(Y)=Y^2/(2*d), both actual floor cutoffs, no RH, simplicity or nonvanishing, and an existential onset. This file nominates a question only.
LITERATURE_REASON: The target changes from a uniform approximation to a microscopic shifted signed product; the essential shifted-moment theorem and its applicability have not been assessed.

## Proposed bounded mathematical test, not a derived claim

Use C019k's exact S_d, Y_-, Y_+ and t_d. Put
B_d=Y_+-Y_- and h_d=3*pi/log(Y_-). The proposed test asks whether
there is an absolute c>0 such that, for all sufficiently large integers d,
\[
 \int_{Y_-}^{Y_+-h_d} S_d(Y)S_d(Y+h_d)\,dY
       \leq -c B_d\log Y_-.                                  \tag{C}
\]
Both factors use their own t_d value and their own source floor.
The fixed shift constant 3*pi is a trial choice, not an optimized or
source-justified constant. All integrals and the assertion are proposed;
no expansion, diagonal computation or asymptotic is proved in step1376.

The mechanism to test is signed cancellation in the real sum's
microscopic autocorrelation, using its gamma phase and finite frequencies.
Unlike direct inequality (A) of nomination1372, (C) asks first for one
band average, without the unverified Mobius weight or a prescribed number
of blocks. It could supply opposite-sign pairs and a concrete starting
point for quantitative sign distribution. It would not by itself pay
amplitude control, error transfer to C019j's heat observable, disjoint
sample selection, c*sqrt(d) roots, or separation from bulk counts.
Those are independent gaps, and even a growing partial root count would
leave every-degree hyperbolicity and RH unresolved.

Read a primary shifted Hardy-Z second-moment theorem with its exact real
phase, shift range, averaging length and proof cases before broader
extraction. Compare with C019k's gamma multiplier, Y-dependent coefficients
and two moving floors; ordinary zeta-modulus correlations are not automatic
substitutes. Reuse assessment1372 for prior source scope, stops1345/1355/559
and the parked direct (A) route. Follow its Selberg lead only if necessary
for this different observable. Search the exact test and standard shifted
Hardy-Z terminology, as well as stronger applicable results and recorded
local failures, before assigning IMPORT, SPECIALIZE or EXPLORE.

Continue toward a mathematical attempt only if the source comparison
covers a rigorous expansion with a discriminating test of the negative
constant in (C). A nonnegative leading term, an uncontrolled error on the
B_d*log(Y_-) scale, or an essential inaccessible source is a reason to
reject or park this specific test. Failure of (C) is not failure of RH.
Do not replace (C) by a general moment or resume (A) without a fresh exact
assessment. No creative proof is approved by this nomination, and no
originality classification is inferred from the narrow local search.
Matching Mathlib coverage is unchecked.

## Completed source comparison1377 — 17 November 2026

This review completes the saved source question only. The proposed (C)
above is unchanged; no product expansion for C019k, asymptotic, sign,
lemma or mathematical script was derived. A separate ready continuation
is nominated in assessment1377. Its new gate assessment receives separate
approval before mathematical invocation.

### Searches, local reuse and actual access

Queries included `Hardy Z shifted second moment Selberg Z(t+a) Z(t+b)
sine short interval`, `"heat" "Riemann" "shifted" "correlation" Z_t`,
`"Hardy" "shifted second moment"`, `"second shifted moment" zeta
function Bettin`, `"deformed" "Riemann-Siegel" "correlation"`,
`Hardy Z function autocorrelation microscopic shifts sine kernel theorem`,
`"heat" "Hardy" "shifted moment"`, and the exact Atkinson title.
Search hits on random ensembles, numerical Gram laws, zero correlations
under RH and general signal correlations were not used as theorems.
The original Selberg full proof remains unread. Atkinson's publisher PDF
request returned metadata; its first-page image was inaccessible. Shell
curl failed DNS, but browser HTML and Mawia PDF text were accessible.
No purchased access, API key or access circumvention was used.

The narrow duplicate/failure check used C019k including audit1376,
assessment1372's source comparison, stops1345/1355, and the exact
history559 source-screen record. The latter stops concern exterior
control, fixed endpoint signs, and automatic unshifted bulk imports;
none proves or refutes this different signed product test. Direct (A)
remains parked. Existing unfinished proofs and source notes are retained.

### Primary statements and essential proof cases inspected

**Bettin**, *The second moment of the Riemann zeta function with unbounded
shifts*, [arXiv:1111.0925v1](https://arxiv.org/html/1111.0925v1),
3 November 2011, Theorem1, Section2/Lemmas1-2, (1)-(10).
For complex shifts a,b fixed with respect to integration, c=a-b,
|Re a|,|Re b|=O(1/log X), the printed main integrand is
\[
 \zeta(1+c)+\zeta(1-c)
 \chi(1/2+a+iv)\chi(1/2-b-iv),
\]
for the product zeta(1/2+a+iv)zeta(1/2-b-iv) integrated from 0 to X.
The error is O((sqrt X+sqrt|Im a|+sqrt|Im b|)log^2 X);
c=0 uses a pointwise limiting integrand. Restrict attention to small
bounded shifts: the proof's standing assumptions include
|Im a|,|Im b|=O(X^2). No assertion outside that scope is needed.
Read the shifted divisor sum argument, gamma-ratio Lemma2, and theorem
proof: contour shift, both signs of Im b in (9), large/small Im c,
and the W1/W2 split preceding (10). This is a complex zeta moment,
without heat weights; it cannot be replaced by a modulus square or
inserted under an arbitrary varying real multiplier without proof.
No such conversion is performed here.

**Koesters**, *On the Occurrence of the Sine Kernel in Connection with
the Shifted Moments of the Riemann zeta function*,
[arXiv:0803.1141v2](https://arxiv.org/html/0803.1141v2),
5 September 2008, Theorem1.1, Section2/(2.4)-(2.6), AppendixA.1-A.3.
For fixed real mu,nu and X0>1, the normalized zeta product with ordinates
v+2pi*mu/log v and v+2pi*nu/log v, integrated from X0 to X and divided
by X log X, tends to exp(-i*pi*(mu-nu))*sinc(pi*(mu-nu)). This is
not a Hardy real-product theorem as printed. The Atkinson1948 discussion
uses an exact theta-phase displacement; its displayed notation is not
used for an import here. Section2 proves the fourth-moment theorem, not
Theorem1.1: its real-part products retain conjugated and unconjugated
terms, split unequal/equal indices, retain entry endpoints, and use first
and second derivative estimates before extracting the diagonal. Those
proof cases were inspected through (2.6); their coefficients are divisor
coefficients, not C019k's weights. The three standard auxiliary estimates
needed for a direct attempt are recorded precisely in assessment1377.
No higher-moment conjecture is used.

**Gonek-Ivic**, *On the distribution of positive and negative values of
Hardy's Z-function*, JNT174 (2017), 189-201,
[arXiv:1604.00517v1](https://arxiv.org/html/1604.00517v1),
Lemma3 proof/(2.9), reread with assessment1372.
Their quoted real shifted integral is
\[
 \int_X^{X+U}X_0(v+h)X_0(v+k)|\eta_h(v)\eta_k(v)|^2\,dv
 =\sqrt{2\pi}\,U K(h-k)+O(X^{1/2}\xi^7),
\]
where their X-function is a real gamma normalization of Hardy Z,
xi=X^((2a-1)/20), 1/2<a<3/5,
X^a<=U<=X^(3/5), 0<=h,k<=H<=1/sqrt(log xi).
K is their displayed four-mollifier-coefficient arithmetic kernel.
Their application obtains K(u)=O(1), not the desired negative heat
coefficient. This is an inspected primary paper quoting Selberg,
*Collected Papers I*, Lemma15, pp100,108,113; the original proof is
not independently checked. It supplies neither (C) nor arbitrary-weight
coverage. No RH-dependent Theorem2 is used.

**Mawia**, *On the distribution of values of Hardy's Z-functions in
short intervals II: The q-aspect*, Moscow J.Combin.Number Theory8
(2019), 229-245,
[primary PDF](https://msp.org/cnt/2019/8-3/moscow-v8-n3-p03-s.pdf),
corrigendum p231 and Lemma9 proof pp239-240.
The character theorem fixes a primitive conductor q>1; no printed q=1
specialization is claimed. The relevant proof correction retains
n<=sqrt(qv/(2pi)), rewrites the pair integral using the entry time
max(X,2pi*m^2/q,2pi*n^2/q), and separately handles new diagonal
entries and off-diagonal endpoints. Read those cases and their stated
bounds. This is a method for honoring a moving cutoff, not a theorem
for the two shifted heat floors. Their inversion and the amplitudes
in C019k still need direct treatment.

**Polymath1904.12438v2** Theorem1.3/(5),(13)-(19) was refreshed only
for the already audited observable. Assessment1374 and C019k/audit1376
remain the canonical applicability proof. The phase, coefficient and
floor data agree with the proposed factors; no new approximation is
imported. Mathlib coverage for any matching shifted heat theorem is
unchecked, not asserted absent.

### Decision and relevance of the proposed continuation

The old short-outer-window objection to (A) does not rule out (C):
C019k's band is comparable to its height, directly from its endpoints.
The source mismatch that remains is the actual observable. In particular,
the existing bound t_d(Y)(1+log Y)^2=O(1) does not establish that the
heat factors may be replaced by 1. A phase-free modulus correlation,
one frozen heat time, a freely frozen floor, or a lone diagonal without
the other real-product terms would not test (C).

EXPLORE authorizes only preparing the direct finite-sum attempt saved
in assessment1377. Its available tools are finite sums, the exact
C019k functions, standard Stirling/oscillatory estimates and entry-time
partitioning. It does not assume an unavailable shifted-heat theorem,
Selberg's original Lemma15, or Atkinson's original proof. Thus the
historical access limits are nonessential leads for this independent
test, rather than a reason to repeat access searches.

The decisive evidence sought is a rigorous sign for the full leading
band coefficient and an error below its negative margin. A nonnegative
leading coefficient with a controlled remainder would reject (C);
an unpaid error or boundary phase would park this specific attempt
without disproving it. No sign or asymptotic has been established by
this literature turn. Opposite-sign pairs, even if later obtained, still
leave robust amplitude/error transfer, disjoint ordering, c*sqrt(d)
roots, bulk separation, every-degree hyperbolicity and RH unresolved.
