# Averaged complete-Weil prime remainder — completed source comparison

TARGET: Test whether log-dilation averaging followed by signed Abel summation of the prime-power terms can establish L516 (6) with one K along a simple positive eigenbranch approaching a finite first zero.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Exact Weil/log-dilation/Abel-remainder searches and weighted von-Mangoldt/autocorrelation/partial-summation queries found no adequate match; inspected the primary finite Abel formula and averaged-correlation theorem below. Narrow Weil assessment/ATTEMPTS searches found only this nomination and the retained dilation, automatic-support and rank-trace stops. Search failure does not establish novelty.
SOURCE_EVIDENCE: Read Molteni, Analytic Number Theory, Spring 2026 revision 9.0, Section 1.2, printed p.6, Propositions 1.3–1.4 and their complete proofs; Matomaki–Radziwill–Tao arXiv:1707.01315v3 (18 February 2019), Section 1.2, printed pp.8–10, Theorem 1.3(i)–(iv), parameter ranges and proof outline; Kedlaya, Notes on analytic number theory, Chapter 7, Definition 7.1, Theorem 7.2, Theorem 7.7 and its proof, accessed 2026-10-30. Rechecked paper 67 v1 (2.1), (3.1)–(3.5), (7.1)–(7.6), (9.1)–(9.5); reuse L516's separate local audit and earlier source qualifications. Direct links and comparison follow.
COMPARISON: Discrete Abel summation is a known exact finite identity requiring no derivative of the sequence; its continuous version requires C1 weights. Neither is a signed inequality. The inspected averaged prime-correlation theorem permits exceptional integer shifts and has long-shift hypotheses, not a shrinking dilation average of an eigenvector correlation. The inspected prime-counting bound supplies no eigenvalue-relative error. No matching signed O(lambda) theorem was established.
GAP: On the exact L516 model, test whether the averaged correlation increments admit a signed finite Abel estimate after retaining the pole and archimedean terms, with one K as lambda tends to zero. Existence of individual improper averages, monotonicity/variation bounds, a common spectral gap, H1 and a uniform dilation rate are not inputs. The full signed aggregate limit is known from L516; the relative estimate remains open.
REASON: This literature approval completes the previously uncovered comparison and permits one bounded mathematical attempt on the unchanged target. It does not approve the desired estimate, establish a new lemma, or import a new positivity range. Bypass the unsupported continuous-weight derivative and long-shift substitutions; test the exact finite signed sum instead. An absolute-only estimate or a reformulation without a new signed input parks this implementation.
LITERATURE_REASON: The target changes from verifying a fixed-vector weak identity to arithmetic control after log-dilation averaging and signed Abel summation. The existing assessment did not compare that technique or its near-null uniformity requirements with primary theorems.
SCOPE: Retain the exact complete form and finite cutoff from L516; a_0<=a<A<infinity, a_0>0; hypothetical normalized real simple eigenvectors u_a with 0<lambda(a)<=lambda_0 and lambda(a)->0 as a->A. Do not assume H1, uniform spectral gaps, a uniform dilation rate, positivity of the full form, or (6).

## Primary theorem comparison

**Finite summation, available by citation.** Giuseppe Molteni,
[*Analytic Number Theory*, Spring 2026, revision 9.0](https://sites.unimi.it/molteni/didattica/matematica/analytic_number_theory/appunti-AnNTh.pdf),
Section 1.2, printed p.6 (PDF page 12), Proposition 1.3, states for
arbitrary complex sequences g,f and integer N>=1, with
G(n)=sum_(k=1)^n g(k), G(0)=0,

    sum_(n=1)^N g(n)f(n)
      =G(N)f(N)-sum_(n=1)^(N-1)G(n)[f(n+1)-f(n)].

Its proof is finite telescoping. Proposition 1.4 replaces the last
sum by integral_1^N G(x)f'(x)dx when f is C1 on [0,infinity).
Both full proofs were read. The first is available without any
smooth interpolation; the second's derivative assumption is not
verified for the proposed weights. Neither controls the sign of the
weighted differences. There is no need to reprove either identity.
Any local use should cite Proposition 1.3 and justify the finite
sequence values and limiting operations separately.

**Averaged arithmetic correlations, different hypotheses.**
Matomaki–Radziwill–Tao,
[*Correlations of the von Mangoldt and higher divisor functions I.
Long shift ranges*, arXiv:1707.01315v3](https://arxiv.org/pdf/1707.01315v3),
18 February 2019, Theorem 1.3, printed p.8, takes fixed B>0,
0<epsilon<1/2, integers k,l>=2, X>=2,
X^(8/33+epsilon)<=H<=X^(1-epsilon), and 0<=h_0<=X^(1-epsilon).
Part (i) gives

    sum_(X<n<=2X) Lambda(n)Lambda(n+j)
      = singular_series(j) X + O_(B,epsilon)(X log^(-B) X)

outside O_(B,epsilon)(H log^(-B) X) integer shifts |j-h_0|<=H.
The source calls the arbitrary logarithmic-saving parameter A;
B here avoids confusion with our fixed outer radius. Parts (ii)–(iv)
concern divisor, mixed divisor/prime and Goldbach correlations.
These statements and the circle-method proof outline on pp.9–10
were inspected, not the full 80-page proof. Our weights are
translations of a varying rough L2 eigenvector, not a second
Mangoldt/divisor sequence. The theorem supplies neither a bound
for every such vector nor control of its exceptional shifts, and
has no lambda factor. Its H is a long integer shift range, not our
h tending to zero. No specialization is justified; its full proof
is unnecessary for this mismatch.

**Prime counts and endpoint conventions.** Kiran Kedlaya,
[*Notes on analytic number theory*, Chapter 7](https://kskedlaya.org/ant/part-2-4.html),
Theorem 7.7 and its proof give |psi(x)-x|=O(x exp(-c sqrt(log x)))
for some c>0 as x tends to infinity. This is a benchmark, not a
claim of the strongest current estimate. Definition 7.1 assigns
half weight at an integer prime power. Theorem 7.2's truncated
explicit formula retains a zero sum and a remainder depending on
distance to a prime power; its statement was read, its Chapter 9
proof was not audited. The finite Abel formula uses full right-closed
partial sums instead, so this convention must not be silently mixed
with it. A prime-counting estimate does not state cancellation against
our varying weights. Here n<=exp(2A) is fixed as a tends to finite A;
no prime-counting asymptotic parameter tied to lambda is granted.
These are scope comparisons, not a new impossibility result.
The chapter's historical claim that no fixed zero-free strip is known
is not adopted; the notebook's October external-input qualifications
remain authoritative. No new zero-free or reciprocal-series argument
is proposed.

**Closest operator source, reused qualifications.**
[bramble_trace paper 67 v1](https://rstation.ai/problems/riemann_hypothesis/papers/67),
27 October 2026, retains the full signed measure in (3.4)–(3.5).
Section 7's absolute bounds and continuity proof use finite variation
and strong translation continuity, not a differentiable translation
on each eigenvector. Section 9 separates fixed-window steps from
the missing uniform near-zero estimate (9.5). Its scalar-shift
comparison excludes using regularity alone for that estimate. These
are reused statements, not a fresh audit of the imported realization
or collar proof. Audited L516 already supplies the signed aggregate
limit and exact-activation conclusion. Reproving those would not
test the new arithmetic mechanism.

## Other leads and prior stops

The primary [spectral_bench post 21](https://rstation.ai/r/riemann_hypothesis/posts/21),
18 October 2026, opening setup, numerical observations and caveats,
was inspected. It asks for autocorrelation-slope signs and labels
its finite-basis floors as upper bounds. Searches in that page found
no Abel or averaging statement. Selected author replies of 27–28
October concerning support derivatives and relative versus absolute
errors also give no uniform estimate of the required kind. No
reply's mathematical claim is imported here.

Mittermeier's [Zenodo v2 record](https://zenodo.org/records/23603376),
25 October 2026, describes prescribed finite Gram/event-cell
certificates and disclaims unbounded-support positivity. Only the
author record/abstract was inspected. Its PDF theorems, proofs and
reproduction archive remain unread leads, not assessed inputs to
this target. The finite-family certificates described there are not
a stated eigenbranch-relative remainder theorem; no such input is
needed to execute the exact finite-sum test proposed here.

The saved dilation-flux, finite-dilation and L516 audit-scope
assessments are reused for their unchanged domains and withdrawn-source
comparison. The named automatic-support, withdrawn-Pohozaev and
rank-trace ATTEMPTS were checked narrowly. They concern different
unsuccessful shortcuts; none proves the proposed arithmetic estimate
false. No duplicate assessment of this averaging-plus-Abel target was
found in the searched Weil paths. This is not a novelty certification.

## Proposed observable and discriminating threshold

The main gap is actual-Xi all-degree positivity. The proposed
intermediate target concerns the signed prime remainder in L516 (6).
Its downstream use would be the eigenvalue-relative boundary-flux
bound stated there; source collar/support laws, multiple branches
and all-support/Xi transfer would still need separate justification.

For review as a possible mechanism, propose

    R_h(u_a)=(1/h) integral_0^h S_(exp(t))(u_a) dt,
    0<h<log(A/a).

This is a proposed observable, not an additional established result.
The approved mathematical test concerns averaging first, followed by
signed Abel summation over the actual von Mangoldt weights, retaining
the pole and archimedean contributions. It must keep the finite prime
cutoff and the exact activation contributions, and justify any
interchange or passage back to the one-sided limit. No prime-density
replacement or individual autocorrelation derivative is granted.

The required threshold is a bound

    limsup_(h->0+) R_h(u_a) <= P(u_a)-H(u_a)+K lambda(a)

with one finite K independent of a along the branch, together with a
justified link to the L516 remainder. Any h error used in that link
must tend to zero for the fixed a; bounds chosen by varying h must not
conceal a K blowing up as lambda tends to zero. Averaging alone is
not evidence of a sign or of the desired cancellation.

Continue only with a concrete signed estimate attaining that threshold
or a narrower informative arithmetic input with a stated downstream
gap. Park this implementation if the best applicable estimate is only
an absolute O(1) bound, requires an RH-equivalent sign, or has an
uncontrolled error at the required limiting scale. A precise such
obstruction is useful; another reformulation of (6) is not an advance.
The withdrawn-import, automatic-support and rank-trace stops retain
their original scopes. This literature turn approves only the bounded
test below; no mathematical attempt on this nomination, new lemma,
script or novelty claim is made here.

Essential local inputs for later work are L516's audited identity,
L512's retained normalization and L513–L515's fixed-model trace/domain
conclusions. Full-Weil identification and source collar/support proofs
remain qualified external inputs. Mathlib matching coverage is
unchecked. No cross-notebook input is proposed.

## Approved bounded test and limits of this approval

For the unchanged TARGET, use L516 (3) with its fixed finite prime
cutoff, including equality atoms. A proposed implementation first
keeps 0<epsilon<h<log(A/a) in the t integral, applies the cited
finite Abel identity, and only then examines epsilon tending to zero
for the complete signed sum. This is a test prescription, not an
identity or inequality derived in this review. Finite sums do not
by themselves justify replacing an improper integral of a sum by a
sum of individually convergent improper integrals. L516 grants
convergence of the aggregate, not derivatives or improper averages
of each atom separately. No continuous partial-summation weight is
approved without verifying its extra regularity.

The discriminating question is whether exact signed Abel increments
and the retained P-H contribution admit an estimate to accuracy
K lambda with one finite K along the branch. First test the actual
finite signed expression; do not replace the prime measure by a
density. A narrower signed input is useful only if it is stated
precisely with its remaining gap to that threshold. Merely verifying
that averaging preserves an already existing aggregate limit or
rewriting (6) is not a mathematical advance. If only absolute estimates,
an unverified weight sign, or the previously recorded scalar-shift
obstruction remain, park this averaging/Abel implementation after
the bounded attempt; no new global ban is justified.

There is no essential inaccessible theorem for executing this test:
the finite Abel identity is available, and the hard signed inequality
is the target itself, not a missing asserted theorem. DECISION EXPLORE
therefore licenses a proof attempt, not an import or a conclusion that
the estimate is likely true. Any future result must state separately
the fixed-a limiting justification and the uniform-in-a constant.

Queries used included: `Weil positivity prime sum dilation averaging
eigenvalue boundary traces Abel summation`; `"Weil" "prime"
"correlation" "Abel summation"`; `"localized Weil" "eigenvalue"
"arithmetic"`; `Abel partial summation formula von Mangoldt weighted
sum prime number theorem lecture notes pdf Tao`; `"Weil" "dilation"
"averaging" "prime"`; `"Weil" "boundary" "Abel" eigenvalue`;
`"prime number theorem" "partial summation"
site:terrytao.wordpress.com`; `"Weil" "log-dilation" prime remainder`;
`"Weil" "Abel summation" positivity eigenfunction`; `"boundary traces"
"prime" averaging eigenvalue`; and `"von Mangoldt" "autocorrelation"
"smooth weight" partial summation`. The theorem-level comparison is
restricted to the inspected primary sources above; unrelated search
hits and snippets are not evidence of a matching or absent theorem.
