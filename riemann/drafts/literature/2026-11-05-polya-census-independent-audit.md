# Independent audit nomination for the partial Pólya census

TARGET: Audit L815 and scripts/polya-census/census-579.py with its certificate for full-tail inclusion, outward rounding and every claimed event exclusion on [0,6.5], retaining unresolved [6.5,40].
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step578/implementation coverage; inspected actual operation names, Python3.15.2 decimal contracts and libmpdec4.0.1 primary arithmetic/context documentation; targeted query site:bytereef.org libmpdec mpd_qpow integer exponent correctly rounded.
SOURCE_EVIDENCE: Reuse drafts/literature/2026-11-05-polya-certified-event-census.md (Hickey–Ju–van Emden2001 Section4.8 Thms9–10; Johansson1802.07942v1 Sections2/2.1,3.2); Python3.15.2 decimal Decimal.exp/next_minus/next_plus and Context.power https://docs.python.org/3.15/library/decimal.html ; mpdecimal4.0.1 Arithmetic Functions power and Context Correct Rounding https://www.bytereef.org/mpdecimal/doc/libmpdec/arithmetic.html#power and https://www.bytereef.org/mpdecimal/doc/libmpdec/context.html#correct-rounding .
COMPARISON: Known inclusion methods cover strict cell exclusions only after enclosure justification. Primary Decimal/libmpdec contracts do not give a blanket correctly rounded C power guarantee; actual integer-power calls require an independently checked justification. This is an audit obligation, not a demonstrated erroneous enclosure.
GAP: Actual L815 bounds and census arithmetic remain unaudited; no actual failing power input identified. Audit must establish inclusion or flag affected claims unsupported; no events on unresolved cells, global sign or RH conclusion follows.
REASON: Essential backend contracts are now inspected; approve the saved bounded conceptual audit using standard inclusion methods, with power as the first contractual checkpoint. No repeat census or new mechanism is authorized.
SCOPE: Preserve original artifacts. Essential inputs L016/L019/L020/L021/L814/L815 and exact certificate; no reference-zero theorem, cross-notebook theorem or new sign mechanism. Full matching Mathlib coverage unchecked.

Before the audit, approve its source scope in a separate turn using the
existing assessment where adequate. Inspect primary Decimal guarantees
only for operations whose actual rounding contracts are still essential
and unread; no repeat search for an actual-family census is needed.
The audit must check all derivative orders, both omitted tails,
normalization denominator, Machin/Taylor error bounds, double-angle
propagation, whole-cell interval integration and shared endpoints.

A passed audit can validate the bounded partial exclusion. A failed
contract or enclosure invalidates affected claims and requires correction
with old evidence retained. Do not extrapolate or reinterpret unresolved
boxes as roots. Current boxes give no event candidate to orient.

## Completed source review — step580, 5 November 2026

The prospective nomination above is preserved. This review approves the
exact TARGET for a separate mathematical audit; it does not pass that audit.
Reused step578's inspected theorem hypotheses and proof cases rather than
reopening general root-isolation discovery. Read L815 and the actual code
to identify contracts; no bound, event exclusion or algorithm was reproved.
The fixed-cap failure in ATTEMPTS/2026-11-05-polya-direct-interval-census-cap.md
still applies: tiny tails do not repair finite-integral cancellation loss.

### Essential backend source scope

[Python3.15.2 decimal](https://docs.python.org/3.15/library/decimal.html),
Decimal construction/exp/next_minus/next_plus, Context.power and rounding
modes: string/integer construction preserves input digits; exp is correctly
rounded with half-even; neighbors are adjacent representable values in the
specified context. Floor and ceiling specify opposite rounding directions.
The C power contract is only almost-always correct rounding, unlike the
Python implementation. Context precision alone is therefore insufficient
as a general power inclusion justification.

[mpdecimal4.0.1 Arithmetic Functions, power](https://www.bytereef.org/mpdecimal/doc/libmpdec/arithmetic.html#power)
states integer powers are exact when finite and fitting the precision;
the general power error is below 1ULP+t in directed modes, t<=0.1ULP,
and correct rounding is not guaranteed.
[Context, Correct Rounding](https://www.bytereef.org/mpdecimal/doc/libmpdec/context.html#correct-rounding)
excludes pow and invroot from its allcr guarantee. These are primary
version-matched contracts, not tests of installed behavior.

The code's I.__pow__ calls lo.power/hi.power without neighbor expansion;
atan uses those powers. Establishing whether the actual positive-integer
calls preserve the required outward direction is a load-bearing audit
question. The general warning is not a counterexample for these calls.
A version-specific implementation justification, exact-value checking of
all relevant calls, or an independently justified enclosure is needed if
the public contracts do not settle their direction. Do not silently add
an integer-case guarantee absent from the inspected sources. Backend
implementation internals have not been inspected in this source step.
No new analytic theorem or numerical certificate is claimed here.

### Approved bounded test and limits

Start with the arithmetic contract and its actual uses; if unresolved,
identify affected exclusions as unsupported rather than performing a
replacement census. If inclusion is justified, audit L815's three orders,
both tails, exact Q normalization with positive denominator, Machin/Taylor
remainders, midpoint radius and double-angle propagation, whole-cell
integration, and all thirteen exclusion cells and shared endpoints.
The nominal grid arithmetic also needs checking wherever it uses the
ambient Decimal context. Check certificate provenance before relying on
its stored intervals. No interval containing zero certifies equality.

Continue only with complete relevant evidence: a passed audit certifies
bounded event exclusion, or a concrete failed/unsupported inclusion
changes reliance on that evidence. Preserve all old artifacts and the
unresolved [6.5,40]; no scan repetition, multiple-root guarantee,
all-real-reference assumption or global conclusion is licensed. Required
local inputs remain L016/L019/L020/L021/L814/L815 and the full relevant
certificate. Those mathematical inputs are for the audit, not imported
as newly verified results in this literature step. No cross-notebook use.
Full matching Mathlib coverage remains unchecked. A genuinely new signed
central mechanism is still unprepared; the necessary audit takes priority
and is not classified as creative work.
