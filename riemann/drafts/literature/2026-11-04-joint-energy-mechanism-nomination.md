# Joint arithmetic/archimedean control: completed source comparison

TARGET: Compare frequency-localized prime-delay bounds, neutral-cell Schur complements and resonance penalties as joint arithmetic/archimedean controls, and select one explicit intermediate inequality not excluded by L743 or the recorded signed-tail stops.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 286 searched joint Weil frequency/Schur/resonance estimates and uniform Sobolev modulation; compared exactly the three nominated mechanisms with the named local stops. Primary passages and exact queries are recorded below; search silence is not evidence of originality.
SOURCE_EVIDENCE: Read Zhu 2608.24827v2 Thm1.1, (2)-(4), Lem3.1, complete Section4 and Lem6.1/proof; rechecked Dritschel-Rovnyak 0903.3639v1 Appendix A.1/A.2 with proofs; read SRFP311T1 October2026 high_frequency_coercivity ThmsA-C, Definition2.1/Remark2.2, Sections3-4, Prop5.1 statement/Step1, Section6/Lem6.2 proof and Section9.3; DLMF5.11.2 and complex remainder paragraph in 5.11(ii). Reuse audited L740/L741/L743 and the parent assessment; no source computation replay.
COMPARISON: Generic finite-band lower reduction with paid tail coupling is already covered by Zhu. Positive-block Schur factorization does not supply a missing complement sign. The new envelope source studies a different core form and distinguishes sparse from collective control. Select only a uniform complete-energy modulation penalty, with known asymptotics imported and the correction/uniformity specialization left unproved.
GAP: Full signed interactions, moment complements and support-uniform positivity remain open. Even the selected fixed-window, bounded-H2-envelope inequality is not established here; its exact statement and application obligations are in the separate continuation assessment.
REASON: This source screen eliminates direct import of the mismatched envelope theorem and duplicate generic finite reduction as new sign mechanisms. A supported-family resonance penalty is independently testable beyond L743's unweighted equality, without asking for RH-equivalent positivity or reopening a signed-slope stop.
SCOPE: Literature-only comparison and nomination; no lemma, mathematical script, new energy derivation, sign theorem, source-proof certification or RH candidate. The new SPECIALIZE continuation requires separate approval before research.
LITERATURE_REASON: The invocation-start joint-energy target was REVIEW_REQUIRED; its full-form frequency/Schur/resonance coverage was missing, unlike the ready prime-only L743 audit.

## Original nomination, preserved

The following was the uncovered nomination at the beginning of step 286.
The main gap remains unconditional actual-Xi mixed positivity. Discovery
should identify one concrete inequality useful in a finite-window lower
certificate, even if support enlargement or global positivity remains
independently unresolved. No such inequality is asserted here, and none
of the three mechanisms is preapproved.

Read the exact complete energy convention in L741 and the narrowly needed
L740 formulas before comparing primary theorem hypotheses and relevant
proof cases. L742 contributes only its neutral-space definition: its RH
conditional spectral representation is forbidden as an unconditional
premise. Preserve L741's unreplayed source-computation qualification.

Compare at most these three mechanisms. Frequency localization must pay
the Fourier-weight and localization errors jointly with the compressed
prime-delay form. A signed Schur complement must pay its complement and
off-diagonal terms without assuming a positive unknown block. A resonance
penalty must estimate supported tests in the complete energy, not a
pointwise prime comb or just the frequency of one chosen modulation.
Do not retry L743 or infer positivity from a factorization whose
hypotheses already include it.

Recorded contrasts to check narrowly are the step-283 comparison in
[the parent assessment](2026-11-04-neutral-cell-coherent-mechanism-discovery.md),
[the signed neutral Gram-dual stop](../../ATTEMPTS/2026-11-03-signed-neutral-tail-gram-dual-source-stop.md),
and the nullvector [modulation](../../ATTEMPTS/2026-10-30-weil-nullvector-modulation-source-stop.md)
and [weighted-localization](../../ATTEMPTS/2026-10-30-weil-nullvector-multiplier-source-stop.md)
stops. The latter leave a signed displacement-slope comparison unpaid;
they are not global bans on frequency estimates. Any reuse must identify
a materially different paid quantity rather than rename that target.

Continuation test: select a mathematical attempt only after recording a
precise inequality, essential input IDs, checked source hypotheses,
required threshold and discriminating test. Reject a mechanism that
merely rephrases full positivity, omits a signed cost, uses RH or repeats
an exhausted route without new input. If all three fail, record the new
scope evidence and park them; do not manufacture a creative attempt.
A sign-producing mechanism and its coverage are currently missing, so
creative proof routing is not justified yet. This nomination resets no
exploration or recovery counter. Full matching Mathlib coverage is
unchecked; discovery should distinguish supporting facts from a match.

## Completed comparison, 4 November 2026, step 286

The main gap remains unconditional actual-Xi mixed positivity. The
deliverable here is source-level discrimination and one exact intermediate
target, not a mathematical proof attempt. L740 (4)/(5), L741 (1)-(5)
and its complete scalar/pole normalization, and L743's correction
construction (9)-(13) fix the objects. Only L742's neutral-space definition
is an input; its RH-conditional atomic representation is forbidden.
L741's cited computation remains unreplayed and is not needed for the
selected penalty. The October baseline/register were read before this
arithmetic comparison; no zero-free estimate is being proposed.

### 1. Frequency localization: useful but already covered reduction

[Zhu, arXiv:2608.24827v2](https://arxiv.org/html/2608.24827v2),
2 September 2026, Theorem 1.1 and complete Section 4, gives a lower
frequency reduction for real even tests supported in [-a,a]. It requires
Tsharp with beta=log(Tsharp/(2pi))-1/Tsharp-A_a>0, where
A_a=sum_(log n<2a) 2 Lambda(n)/sqrt(n). Its certified threshold is
min(lambda0,beta-epsilon_D)-epsilon_B>0, including the retained-to-tail
coupling. Lemma 6.1 and the paragraph after its proof keep the negative
odd pole and extend the reduction through parity to complex tests.
Thus a generic paid finite-frequency certificate is known. Centering
our length-L window uses a=L/2. Nothing here supplies the finite-block
margin for growing windows, or makes that condition uniform in L.
The source computation is not replayed. Lemma 3.1 is a direct
high-frequency symbol bound, not a supported-family uniform modulation
or exact-correction theorem. These are statement/application comparisons,
not an independent audit of the manuscript.

### 2. Neutral-cell Schur complements: missing paid complement

Reuse step 283's exact Fejer-Riesz comparison. A fresh narrow read of
[Dritschel--Rovnyak, arXiv:0903.3639v1](https://arxiv.org/pdf/0903.3639v1),
21 March 2009, Appendix Lemmas A.1/A.2, printed pp.28-30, confirms the
boundary: for a bounded block operator, A.1 requires nonnegative
diagonal blocks and a contraction factorization of its off-diagonal
block. A.2 starts with a nonnegative whole operator. Their proofs do
not provide the missing neutral/complement estimates for this form.
The bounded theorem cannot be applied directly to an unbounded energy
without a form realization or justified normalization. L741 supplies
one small-window sign; it does not supply all-window complement signs.
No independent paid neutral/complement bound was found. Park generic
Schur algebra as a sign mechanism; retain it as a tool once those
estimates exist. This is a source-scope decision, not an impossibility
theorem for a future arithmetic Schur estimate.

### 3. Resonance penalties: form and uniformity matter

The primary author page [SRFP311T1, High-Frequency Coercivity](https://srfp311t1.com/high_frequency_coercivity),
heading dated October 2026, has Theorem A for collective envelope spaces
with e^R=o(log T), and Theorem C for fixed-sparsity spaces at
R=theta log T, 0<theta<=1/2. Sections 1 and 9.3 distinguish cumulative
row control from pairwise bounds. Definition 2.1 (2.6) uses prime
coefficient Lambda(q)/sqrt(q) multiplying the real autocorrelation;
our complete energy uses twice this coefficient. Remark 2.2 explicitly
omits poles. Thus this is not a matching theorem for L740's energy.
Its Section 6 oscillatory remainder argument is a lead, not an imported
estimate here. Search indexing returned a September heading and broader
collective claim at the same URL; use the opened October text, not that
stale snippet. No source theorem from this page is adopted and its
remaining proof is not certified.

The selected alternative is a uniform penalty for a supported family
with a fixed H2 envelope bound, followed by L743's exact cell correction.
It pays the entire finite arithmetic operator and tests the complete
energy. This is stronger in quantifiers than checking one modulated
profile, and weaker than signing all supported tests. It asks neither
for sparse-to-dense transfer nor for preservation of the energy norm.

[NIST DLMF 5.11.2 and 5.11(ii)](https://dlmf.nist.gov/5.11),
accessed 4 November 2026, supplies the digamma expansion with principal
logarithm in |arg z|<=pi-delta and its complex remainder bound: the
first neglected term is multiplied by sec^(2n+1)(arg(z)/2). The line
z=1/4+it/2 stays within the right half-plane. The source supplies symbol
asymptotics, not permission to exchange an unbounded logarithmic
multiplier with a varying-family limit. That uniform application and
the correction's logarithmic-energy cost are the explicit remaining
obligations. Reproof of Stirling/digamma asymptotics is unnecessary.

### Selected target, downstream use and test

The exact inequality, supported family and all qualifications are in
[the new continuation assessment](2026-11-04-uniform-neutral-modulation-energy-penalty.md).
It asks for E_L(v_t)/||v_t||^2 >= log(|t|/(2pi))-A_L-epsilon(t),
epsilon(t)->0 uniformly over unit smooth cell trains with bounded H2
norm and their fixed exact corrections. Here A_L is the entire finite
prime coefficient mass, with the full factor two. No inequality is
derived this turn.

If valid, this quantifies why L743's prime-preserving returns are costly
in complete energy and supplies one paid high-carrier class for a later
joint certificate. A bounded-frequency signed block, its complement,
and control when the envelope complexity or support grows remain
independent gaps. Continue only with a uniform error and a nonzero
corrected denominator; a pointwise-in-profile argument fails the test.
Stop after one bounded attempt if that uniformity is not obtained,
recording the precise failure. Do not reinterpret this restricted
penalty as energy-normalized Rayleigh equality or global positivity.

No justified creative central-sign attempt emerges from the three
sources: no independent favorable estimate for the growing low-energy
block is identified. The nominated specialization is reproduction of
standard high-frequency analysis, not creative sign production. Its
new assessment must receive a separate approval turn. This comparison
resets no exploration/recovery counter.

### Search scope and retained failures

Exact web queries included `Weil quadratic form frequency localization
Schur complement logarithmic symbol prime tail positivity`, `Riemann
Weil positivity resonance prime archimedean uncertainty compact support
logarithmic energy`, `"Weil" "resonance" "uncertainty" positivity`,
`"neutral" "Weil" "Schur" complement`, `"Weil" "frequency"
"localization" prime bound logarithmic`, `"Weil quadratic form"
modulation "Sobolev" uniform`, `"Weil" "neutral" "high frequency"
energy`, and `"digamma" "modulated" "quadratic form"`.
No matching exact corrected-family theorem was located; this is not a
novelty finding. The finite Guinand-Weil dictionary 2607.02828 was
screened only at its Section 2 definitions/Theorem 2.5, not its complete
proof: finite-vector identification is not a paid complement bound and
is not an input. Other search snippets and trial-space leads are unread
leads, not assessed theorems.

Read the named signed neutral-tail Gram-dual, nullvector modulation and
weighted-localization attempt records; use the parent assessment's
factorization comparison. Their unpaid quantities are respectively a
growing Gram-dual norm and an eigen-equation-sensitive signed slope.
The proposed H2-family frequency penalty addresses neither quantity,
so does not reopen those exhausted implementations. L743's prime-only
stop remains intact. Full matching Mathlib coverage is unchecked;
standard Fourier/Hilbert facts are supporting inputs, not a full match.
PROOF.md and DAG.md are unchanged because no argument changed.
