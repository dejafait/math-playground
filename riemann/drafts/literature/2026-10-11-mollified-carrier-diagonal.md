# Fixed-head mollified carrier: proposed sharp diagonal reduction

TARGET: Establish a sharp o(1)-error diagonal reduction for H^(-1) integral_[H,2H] Re(K(t)E(t)Z_(+,N)(t)^2)|P_H(t)|^2 dt with fixed N and L395's mollifier.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed bounded complete-mean search and exact same-height/cross-mollifier comparison in 2026-10-11-mollified-fixed-head-mean.md; no separate inspected theorem states this physical carrier reduction and no duplicate was found in the selected local records.
SOURCE_EVIDENCE: Bui–Conrey–Young, https://aimath.org/~kaur/publications/69.pdf#page=8, Acta Arith. 150 (2011), 35–64, Lemma 4.1 and full gamma-Mellin proof, pp. 42–43; (2.3), Theorem 3.2 and Lemma 5.1 through (5.7) for the explicit changed-mollifier contrast; Bourgain https://arxiv.org/pdf/1408.5794v2#page=2, Theorem 5 (0.5), p. 2; audited L395 definitions and weighted jet control, L390 carrier definition, L381 Section 4 and L391 exact ordinary-jet/connector tools.
COMPARISON: A uniform small-complex-shift same-height product formula and unconditional contour bounds are known; the actual physical jet conversion, growing square cutoff, rational collisions and sharp endpoint error are local application obligations. The evaluated cross-mollifier theorem has different hypotheses and is not an input.
GAP: Need an explicit finite H-dependent carrier diagonal and a proved normalized o(1) remainder; its limiting coefficient, the balanced mean and the complete signed coefficient may remain unresolved.
REASON: This independently testable obligation retains the whole carrier at its required constant scale and can unlock a later complete-mean calculation without an unproved negligibility premise; cite known theorems and prove only the changed application.
LITERATURE_REASON: Supervisor recovery requires direct primary-source URLs and separate approval of the saved carrier target; reuse step 62 coverage without expanding the target or repeating discovery.
SCOPE: Fixed positive integer N before H tends to infinity; exactly L395's length H^(1/100), mu coefficients and u^2 polynomial, and L390's K,E,Z_(+,N); ordinary derivatives through order two, signed sharp endpoints, all rational collisions. No growing N, coefficient sign or carrier o(1) assumption.

## Proposed attempt and its test

The main gap remains global actual-theta mixed positivity. The downstream
use of this reduction is a later signed coefficient test for a positive
physical discriminant witness. The balance between the carrier and balanced
term must be computed before any such witness is asserted.

Essential input IDs are L390 and audited L395. L381 Section 4 and L391's
exact ordinary-jet and connector passages are available tools; their
unweighted fixed-twist bounds are not automatically valid after inserting
the growing mollifier. Use the full inspected source evidence in
[the completed comparison](2026-10-11-mollified-fixed-head-mean.md).
The cited primary product formula allows small complex shifts uniformly;
fixed-order derivatives must be justified by Cauchy, not by differentiating
an unspecified remainder. A holomorphic height shift is another available
method, but must retain the exact physical polynomial, finite weight and
all endpoint edges. Reproof of the source theorem is unnecessary.

Seek an explicit finite arithmetic expression Q_N(H), retaining every
zero-frequency collision, for which the displayed sharp carrier mean is
Q_N(H)+o(1). This is a sought conclusion, not an asserted identity. A proof
of convergence of Q_N(H) is not required in this bounded step; retain any
unresolved limiting arithmetic for a separately assessed continuation.
Do not discard the carrier, replace it by a modulus square, differentiate
the mollifier as though it were a physical jet, or use a positive endpoint
bracketing argument for this signed statistic. Establish uniformity of
summed errors over its actual growing support before taking the height
limit. Fix N throughout; L395's uniform tail transfer may be used only
after fixed-head statements have been established.

Continue only if the complete ordinary-jet reduction and all normalized
approximation, off-diagonal and sharp-endpoint errors tend to zero.
If any available certificate leaves an order-one or larger remainder,
record the specific failed threshold and preserve it; do not infer that
the carrier itself is large or that the desired mean fails. A positive
coefficient, balanced-head evaluation, total L367 margin, eventual D sign,
actual common-zero upper bound, low-index and above-forty signs, and
endpoint arithmetic margin are independent unproved obligations. No RH,
simplicity, disjointness or phase independence is assumed. Full matching
Mathlib coverage is not checked. The separate source approval below covers this exact continuation before
a later mathematical invocation.


## Separate source approval and URL repair — 2026-10-11, step 63

Reused the completed step 62 search, cross-mollifier comparison and local
duplicate/failure record. Reopened only the essential primary statements
to verify direct access. This is a STALLED process repair: the SPECIALIZE
decision is unchanged, and no new mathematical evidence is claimed.

[Bui–Conrey–Young, Lemma 4.1 and proof, printed pp. 42–43](https://aimath.org/~kaur/publications/69.pdf#page=8)
was inspected completely. Its domain is log^2 T <= |t| <= 2T, with
complex shifts uniformly O(1/log T). The one-series approximation has
exponential cutoff exp(-l/T^3) and error O(T^(-1+epsilon)). The proof
crosses the gamma pole and both moving zeta poles, then bounds the
remaining line before choosing V=T^3. The inspected statement supplies
product approximation only; it does not evaluate our weighted integral.
The changed cross-mollifier theorem remains excluded for the reasons
recorded in step 62.

[Bourgain, arXiv:1408.5794v2, Theorem 5 (0.5), p. 2](https://arxiv.org/pdf/1408.5794v2#page=2)
was directly inspected: its unconditional critical-line bound has exponent
13/84+epsilon. It supplies a contour tool, not a theorem for growing
mollifiers or signed sharp endpoints. No reproof of either theorem is
needed or authorized by this assessment.

The reviewed scope remains exactly the saved TARGET. L390 and audited
L395 specify the actual carrier and mollifier; L381 Section 4 and L391
provide previously reviewed application tools. Their fixed-twist constants
must not be silently extended to growing support. Ordinary-jet conversion,
Cauchy control of differentiated errors, full collision sums and both sharp
endpoint estimates remain proof obligations. The downstream coefficient
and all independent sign/count gaps listed above remain unresolved.
Mathlib coverage of the full target remains not checked.

Source coverage is ready (SPECIALIZE) for one bounded proof attempt on
the unchanged target. Approval covers trying the stated reduction, not
asserting its success. Continue only at normalized error o(1); an order-one
or larger retained bound stops that certificate without deciding the
carrier's signed value. No lemmas or mathematical scripts were changed.
