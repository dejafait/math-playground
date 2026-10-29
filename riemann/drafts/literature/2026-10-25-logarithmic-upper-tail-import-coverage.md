# Conditional logarithmic upper-tail import coverage

TARGET: Import bramble_trace v4 Theorem 1b as conditional eventual positivity of D_n(Xi;a) for every integer 2n>=c_0 log(|a|/(2pi)), for each fixed c_0>3/8, retaining L461's external premise and allowing central zeros.
CHECKED: 2026-10-25
DECISION: IMPORT
SEARCH_EVIDENCE: Reuse the completed initial-sign comparison, including the exact logarithmic-order searches, local v3 screen and v4 change; this import is the source-covered proper input identified there, not a new sign mechanism.
SOURCE_EVIDENCE: bramble_trace, Generalized Laguerre positivity at growing orders, rStation paper 41, displayed v4, 24 October 2026, 07:18 UTC, equation (1), Theorem 1b (4b), and Sections 4.2–4.5 (18a)–(18n), read 25 October 2026; source and applicability details in the initial-sign comparison.
COMPARISON: Theorem 1b directly supplies the positive Xi coefficients for every integer 2p>=c_0 log(t/(2pi)) at all sufficiently large positive t, for each fixed c_0>3/8 under sigma_0=7/8. Its p equals the notebook n. L018 supplies the identical Xi and evenness for the negative-height applicability check.
GAP: Only a precise citation, matching coefficient definitions, positive/negative-height applicability and retained qualifications are authorized. No reproof, lower-order positivity, endpoint result, effective threshold or external-source correctness audit is needed or covered.
REASON: A ready published manuscript statement covers this exact upper-tail target; canonical import avoids duplicate saddle work and makes a useful partial input reviewable. This newly completed assessment requires separate approval next turn.
SCOPE: Actual Xi; every fixed c_0>3/8; a common existential onset in |a|, independent of n; all orders above the exact stated threshold, no upper cutoff; arbitrary central multiplicities. Use precisely L461's external premise and the cited manuscript's theorem, without upgrading either to an independently audited result.

## Citation and permitted application

bramble_trace, [Generalized Laguerre positivity at growing orders,
rStation paper 41](https://rstation.ai/problems/riemann_hypothesis/papers/41),
v4 displayed 24 October 2026 at 07:18 UTC, Theorem 1b, equation (4b).
The primary main page, not the stale v2 search preview or v3 archive,
was inspected. The version-specific /v4 and Markdown endpoints did
not return content; the main theorem and its relevant proof cases
were accessible. Record the version/date in the canonical citation;
if the page materially changes, reassess rather than silently cite a
different theorem.

The source assumes 1/2<=sigma_0<1 and zero-freeness of zeta on
Re(s)>sigma_0. For every fixed c_0>sigma_0-1/2 it asserts a single
height onset for strict positivity of its Xi Laguerre expression
at every integer 2p>=c_0 log(t/(2pi)), without an upper order cutoff.
Use sigma_0=7/8 only with the retained input. The coefficient definition
is equation (1), with Xi exactly equation (2); it is the analytic
product coefficient, not a complex-y modulus-square replacement.

The authorized mathematical work is importing this named theorem
and writing the necessary applicability argument using L018's Xi
normalization/reality/evenness. Check negative real a through that
symmetry, every allowed integer n, and central zeros without dividing
by Xi(a). Cite the full source proof rather than reproduce its moving
saddle or product-tail lemma. A common existential onset is sufficient;
make no claim that it lies below the separately verified finite height.
Do not replace log(|a|/(2pi)) by log(2+|a|) without an explicit justified
change of constants or range. The exact source threshold suffices here.

The source's Sections 4.2–4.4 cover its full coefficient tail and
overlap, including repeated and zero local roots. Section 4.5 retains
the shifted saddle and strict fixed margins. These essential cases
were read in the [completed comparison](2026-10-25-initial-laguerre-sign-coverage.md);
they are available source coverage, not a locally completed critical
audit of the manuscript. Its attached reviewer report is not a
substitute for such an audit.

Essential inputs: L018 for the actual entire Xi and its symmetries;
the cited Theorem 1b for the sign; precisely the external premise of
L461, not L461's witness conclusion. The external September 30
Theorem 1.1 is pinned to commit
1581d4cbdd69a0faf34b2089614fe2a814316a6a, strict Re(s)>7/8, pole
allowed, manuscript/import closure locally unaudited. Retain the
[register](../../foundations/2026-10-quasi-riemann-input.md).

Downstream use is an upper-tail input that can replace repeated
later-band work where only a sign is needed. It does not prove the
initial segment beginning at n=1, bounded-height overlap, mixed
positivity or RH. C460b remains the canonical separately audited
partial band with its stronger quantitative margin; this sign-only
import does not erase that information or upgrade the source audit.

Continue if the exact source statement matches these hypotheses
and the elementary symmetry/normalization check succeeds. Stop or
narrow the import if an order-dependent onset, excluded central zeros
or a stronger zero-free hypothesis is found. Classification for the
approved research import is KNOWN_IMPORTED only. Full matching
Mathlib coverage is unchecked; absence is not asserted. No reproof
or independent new result is authorized by IMPORT.
