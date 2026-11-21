# Complete neutral good-frequency payment screen — completed review861

TARGET: Assess the fixed good-frequency payment test c_E>M/(M+1) for the complete neutral Weil symbol on (0,4log(3)), including an effective two-moment concentration bound or one rigorous rejecting witness.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused discovery860 and804/855/856; searched exact Weil/good-frequency/Logvinenko and constrained concentration terms. Inspected Karnik-Romberg-Davenport2006.00427v2 Section2.2, Theorem3/Corollary3 and Section6; Johansson1802.07942v1 Section2 and endpoint cases. No exact two-moment payment theorem found in inspected sources; no novelty inference.
SOURCE_EVIDENCE: Reused Kovrijkine coverage from completed860 and normalization L744(6)-(8)/L741. Read continuous concentration hypotheses, eigenvalue bounds and continuous-limit proof cases in2006.00427v2; Johansson Section2 box/ellipse branches and Section3.2 manual tails; DLMF3.5.7-8,5.7.6,5.5.2,5.11.2/ii. L750 Sections1/3 supply the existing smooth witness recipe and derivative controls; changed-length checks remain required.
COMPARISON: Quantitative single-band concentration is known but does not supply the exact two-moment good-set lower bound. Integral monotonicity and Plancherel justify the squared-mass screen. One smooth neutral witness with certified mass in a subset of {w<1} can reject it without determining the whole good set; this is known-method specialization, not new signed observation.
GAP: No M value, good-set geometry, concentration constant, witness ratio or sign computed. One fixed L750-recipe witness has sufficient method coverage for a later calculation, conditional on changed-length applicability and interval errors. A successful lower-bound route remains uncovered.
REASON: Separate literature-only review861 completes nomination860 by restricting the next test to an existing smooth witness and validated integration. No new lemma or estimate. A new exact continuation is saved for separate supervisor approval; no research executed.
SCOPE: One interval (0,4log3), level1 and complete symbol; one real smooth L750-recipe witness with T changed to4log3, exact moments and all prime powers below81. Rejection or inconclusive result only; no optimization, concentration lower bound, wavelet retuning or Q-sign claim.

## Proposed test, with all quantities uncomputed

Put L=4log(3), I=(0,L). Use L744's zero extensions, Fourier convention
and dt/(2*pi). The proposed real multiplier is

    w(t)=Re psi(1/4+it/2)-log(pi)
         -2 sum_(2<=n<81) Lambda(n)/sqrt(n) cos(t log(n)).

All prime powers occur. The delay81 meets the enclosing length and
has zero overlap; no earlier prime term may be omitted as small.
The admissible class is

    N={0!=f in C_c^infinity(I;C):
       integral exp(x/2)f(x)dx=integral exp(-x/2)f(x)dx=0}.

Set, as definitions of the intended screening quantities,

    E={t in R:w(t)>=1},
    M=max(0,sup_(t in R)(-w(t))),
    c_E=inf_(f in N) integral_E |F_f(t)|^2dt
                         / integral_R |F_f(t)|^2dt.

The target is to assess whether one can rigorously test

    c_E > M/(M+1).

These definitions assert no value, finiteness proof, inequality or
payment theorem. The next source comparison must justify the proposed
sufficient-threshold logic from the complete form before approving its
application. In particular, it must distinguish an L2 norm bound from
its squared-mass version and normalize the source Fourier transform.
An existential observation constant is not a numerical certificate.

## Bounded continuation/abandonment test

Approve at most one fixed mathematical test only after its effective
source coverage is ready. Continuing requires a rigorous lower bound
for c_E exceeding a rigorous upper bound for M/(M+1), with tails,
every prime shift and exact moment constraints handled. A rigorous
upper bound from one admissible f, at most a rigorous lower bound for
M/(M+1), rejects this strict screening inequality. A failure of one
particular theorem bound to pay the threshold is not a rejection of
the true c_E inequality. Overlapping enclosures are inconclusive.

No witness is selected or derived here. The review may approve a
single source-covered rejecting-witness test if a useful full lower
bound would require a different, presently uncovered mechanism.
Do not use a sampled good set, approximate neutrality, spectral grids
or a finite retained matrix as the whole evidence. If effective sources
remain insufficient, identify the precise independent prerequisite;
do not begin another generic audit or silently change E or I.

Plausible use: payment of the complete negative Fourier weight on one
neutral window, retaining joint arithmetic phases. The result could
screen support-aware observation as a mechanism for later uniform
estimates. Non-neutral directions, scale/window uniformity, global
assembly and actual-Xi mixed positivity remain independent gaps.
A rejected coarse screen is neither negative Q nor a disproof of RH.

## Inputs, existing stops and route

Essential input IDs: L744 and its L741 normalization; L750/L752/C998z/
C998 are scoped failure comparisons, not sign premises. Reuse
discovery859/review860's precise primary citations and804's verification
coverage where unchanged. No cross-notebook input, RH assumption,
semilocal H2-prime estimate, positive complement or Xi realization is
available. Matching Mathlib coverage remains not checked.

Kovrijkine's support hypothesis concerns the Fourier transform of the
observed function. For h=F_f its applicability requires the double
transform/inversion convention; it does not require h supported in a
real frequency interval. Its source theorem has no special hypothesis
of zeros at +/-i/2. Any improvement using those constraints is new
scope and needs its own source assessment. Do not reprove the general
Logvinenko-Sereda theorem just to obtain an ineffective bound.

Recommended immediate task: literature_comparison/standard/high,
because effective constants and a reproducible test remain uncovered.
A later known-method witness or constant calculation should be routed
calculation/standard/high, not called creative. A genuinely new signed
observation mechanism would require its own precise escalation and
bounded test. This nomination does not manufacture one to fill a quota.


## Completed source comparison861 — 13 November2026

The original nomination above remains historical proposed scope; the
current fields and this section complete its literature gate. This turn
made no mathematical calculation, new lemma, script or certificate.
NOVELTY_UNCHECKED labels this literature comparison, not its standard methods.
LITERATURE_REASON: nomination860 was REVIEW_REQUIRED for effective
concentration or witness coverage; general observation, wavelet and
Schur assessments were reused rather than searched again.

### Normalization and sufficient-screen logic

L744(6) on smooth zero extensions, its exact moments (7), and Plancherel
supply the interface. The nominated arithmetic sum contains exactly the
nonzero delays for this length;81 has no overlap. The cosine multiplier
represents the translation quadratic form on these supported tests, not
a form asserted for arbitrary unsupported functions. Both complex moments
must vanish before removing the pole product. No smaller-window sign is used.

The threshold is the standard monotonicity-of-the-Lebesgue-integral
comparison with the simple lower multiplier1 on E and -M elsewhere.
For a nonzero neutral smooth f, write p for its squared Fourier mass
ratio on E. The comparison to audit in the later application is

    Q(f)/||f||_2^2 >= p - M(1-p) = (M+1)p-M.

This is a known integral comparison, not a new estimate for Q,p or M.
Its use requires a finite global lower bound -M and exact Plancherel
normalization. L744(8)'s imported digamma remainder and the finite
arithmetic sum supply scalar coverage for checking finiteness and tails.
A norm-observation constant must be squared before use as p. No threshold
value or positive constant is certified here. The implication is only
sufficient; failure does not imply negative Q.

Kovrijkine's double-transform support convention and unavailable numeric
universal C remain as assessed in completed860. Extra exponential moments
are restrictions, not a theorem improving the constant by a known amount.
No general Logvinenko-Sereda reproof is needed.

### Effective concentration: useful scope, no matching import

Karnik, Romberg and Davenport, *Improved bounds for the eigenvalues of
prolate spheroidal wave functions and discrete prolate spheroidal
sequences*, [arXiv:2006.00427v2](https://arxiv.org/html/2006.00427v2),
28 September2020: read Section2.2, Theorem3, Corollary3 and Section6,
including Lemma3 and limiting cases. The transform is exp(-i omega t),
with 1/(2pi) inverse. Their concentration operator uses one time interval
of length T and one band [-Omega,Omega], c=Omega*T/2. Theorem3 bounds
transition counts for c>0,0<epsilon<1/2; Corollary3 bounds eigenvalues
on its stated index ranges. Section6 transfers discrete bounds with
quantified error tending to zero at fixed c. It does not address this
multi-component level set, two imaginary zeros, or their compressed
largest eigenvalue. Deleting the first two prolate eigenvectors does
not enforce the exponential moments. No numerical bound is imported
or claimed to fail the payment test.

### Effective witness coverage and qualifications

Johansson, *Numerical integration in arbitrary-precision ball arithmetic*,
[arXiv:1802.07942v1](https://arxiv.org/html/1802.07942v1),22 February2018,
Section2 steps2-4 and Section3.2: read direct-box and analytic-ellipse
branches and manual truncation. Valid enclosure callbacks give integral
boxes without analyticity; accelerated Gaussian errors require verified
analyticity and a magnitude bound on the whole ellipse. Evaluation limits
do not certify requested accuracy. Nonanalytic flat joins must use valid
real interval boxes or independently justified smooth quadrature. Infinite
tails need symbolic bounds. This is optional implementation coverage,
not a replayed computation.

NIST DLMF version1.2.8 (15 September2026), inspected13 November2026:
[3.5.7-8](https://dlmf.nist.gov/3.5#ii) gives composite Simpson error
(b-a)h^4 sup|g^(4)|/180 for real C4 integrands and an even subinterval
count. Split real and imaginary parts when needed.
[5.7.6](https://dlmf.nist.gov/5.7.E6) gives the digamma partial fractions
away from nonpositive-integer poles;
[5.5.2](https://dlmf.nist.gov/5.5.E2) gives recurrence;
[5.11.2/ii](https://dlmf.nist.gov/5.11#ii) gives the complex remainder
with its secant factor, already specialized in L744(8). These cover
scalar enclosure methods, not the needed numerical values. Recurrence
plus a sector remainder is allowed on this right-half-plane line with
all errors retained. An unbounded truncated-series error is insufficient.

Reuse L750(2)/(4), Proof Sections1/3 for the symmetric flat-cutoff sine
witness and exact moment-ratio method. Its T=8log3 is NOT the present
length; its old certificate and signs are not inputs. The later attempt
must verify smoothness, nonzeroness, positive denominator, reflection
and both moments for T=4log3. This is an existing construction at a
changed scale, not a new neutralization lemma. Derivative bounds require
the actual scale factors; old numerical errors cannot be copied.
Reuse804's roundoff principles; no finite matrix or external Q-sign is needed.

A rejection need not integrate the indicator of the whole unknown E.
A finite union J of boxes certified w<1 permits a lower bound on bad
mass. Nonnegative mass elsewhere can be omitted in that direction;
Plancherel gives total mass from the spatial norm. One negative value
of w can lower-bound M without being the global minimum. These are
standard set-inclusion/integral comparisons, not bounds established for
the selected witness here. The next assessment fixes the obligations.

### Searches, duplicates and decision

Queries issued: `time frequency concentration prolate spheroidal
constrained moments interval rigorous eigenvalue bounds Slepian Pollak`;
`digamma real part lower bound psi x iy logarithm DLMF5.9 integral`;
`"Weil" "good frequencies" concentration neutral`;
`"Weil" "Logvinenko" positivity`;
`"Arb" "numerical integration" Petras Johansson rigorous integration2018`.
Read primary passages listed above. Web snippets, an experimental
scale-resolved repository and secondary prolate summaries were leads
only; no positivity claims from them were used. Local comparisons were
restricted to860/804/855/856, L744/L741/L750 and C998 plus exact neutral/
good-frequency and named stop records. No matching ready certificate
was located there; this does not establish absence or novelty.

L750 rejects a localization defect; L752 rejects absorption without new
sign input; C998z rejects modulus replacement; C998 rejects a fixed
half-contraction. None rejects this observation screen. Their stops
remain scoped and are not reopened. Full matching Mathlib coverage has
not been checked. No cross-notebook input is used.

Outcome EXPLORATION: method coverage and one concrete witness continuation,
no c_E bound, advance beyond inspected sources, mathematical negative
result or RH candidate. No calculation budget is spent or reset. Save
[fixed-witness861](2026-11-13-neutral-good-frequency-fixed-witness-861.md)
for separate supervisor approval. No justified creative mechanism is
ready: the global signed/Xi bridge is uncovered; standard witness
calculation must not be relabeled creative.
