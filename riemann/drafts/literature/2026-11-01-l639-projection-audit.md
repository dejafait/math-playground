# L639 growing-jet projection — approved conceptual audit coverage

TARGET: Audit L639's uniform o(1) projection theorem, including full regular second-moment terms, growing-order endpoint and Cauchy costs, and the actual complex Gram.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-projection, stronger-result and duplicate/failure search in 2026-11-01-growing-jet-localization-projection-test.md; compared its inspected scopes with all of L639 and the relevant L637/L638/L465/L622 input ranges. No changed target or new theorem lead requires repeating that search.
SOURCE_EVIDENCE: Reopened Bettin arXiv:1111.0925v1 Theorem 1, p. 2 (2026-11-01); reused inspected small-shift proof cases pp. 9–10, DLMF 18.3.1/18.5.8/25.2.4 and classical strip coverage from the prior assessment. Local scope mapping is recorded below.
COMPARISON: L639 retains the regular arithmetic main term and proves a relative endpoint bound before using the power-saving analytic remainder. This differs from applying L638's fixed-order O(T) error to a growing Gram.
GAP: Source scope is ready; independently verify the full-main-term contraction, endpoint derivative constants, factorial losses, compact-strip uniformity and projection normalization. No source citation directly proves L639 (1) or (13).
REASON: Known inputs cover the analytic generator and classical tools, while the new growing-order specialization requires independent reproduction. Approval here concerns source coverage only and is separate from the deriving turn.
SCOPE: L639 as written, with L637's unchanged bump/weight and n=floor((log T)^(1/3)), complex coefficients, and uniform T<=X<=2T. No larger range, signed observer theorem or RH candidate.

## Reuse and critical claims

The invocation-start projection assessment remains unchanged. Its source
statements and proof-case review are reusable. This separate literature
turn approves the exact audit TARGET under SPECIALIZE; it does not perform
the audit or endorse the claimed estimate. Repeat external searches only
if that audit identifies a specific missing hypothesis or new lead.

The main gap remains actual-Xi initial signs at unbounded heights and
all-degree mixed positivity. This audit tests whether the newly proved
obstruction can safely park microscopic realization in the stated range.
Check in particular that the endpoint bound for the regular zeta terms
is relative to the same interval norm as the pole term, and that the
remaining coefficient/Cauchy cost is exp(O(n log(n+2))) against a genuine
power saving. A fixed-order O(T) substitution would invalidate this step.

Relevant local input proofs are L637's hypotheses, L638 Section 1 before
its simplification, L465 Sections 1--2 and 4, and L622's analytic phase.
L473 is background already carried by L638; no new use of its fixed-order
moment law is needed. Underlying arithmetic and strip theorems remain
named imports, not independently audited source manuscripts.

The acceptance test is an independent verification of L639 (1) and (13)
with all coefficients and X uniform. If a necessary estimate fails,
identify the exact failed inequality and revise or withdraw the affected
claim; a failed proof is not a countersequence to vanishing projection.
Even a successful audit leaves larger dictionaries, signed approximation,
useful margins and the RH signs unresolved. Mathlib coverage is not checked.


## Completed scope comparison — 1 November 2026

LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. The precise target is
unchanged. This turn read L639 in full to identify its inputs, without
replaying its inequalities or deriving a replacement result.

The primary theorem was reopened at [Bettin, arXiv:1111.0925v1,
Theorem 1, p. 2](https://arxiv.org/pdf/1111.0925v1#page=2).
It allows complex a,b with real parts O(1/log Y) and supplies the
complete two-term main integrand and the stated square-root-height
error; coincidence c=a-b=0 uses the combined limit. L639 uses bounded
scaled shifts ir/log T,is/log T and endpoints comparable to T. This
is within the recorded source scope; derivative order is not a theorem
parameter. The prior assessment's inspected small-shift proof cases
pp. 9–10 and opposite endpoint case p. 8 remain applicable. The
arithmetic proof is still a named import, not independently verified.

The local input read was deliberately restricted: L637 hypotheses fix
the bump, weight and complex norm; L638 hypotheses and Section 1 supply
the primitive-to-window conversion before discarding regular terms;
L465 Sections 1–2 and the opening uniform-strip argument in Section 4
supply analytic branches, sector estimates and the named strip input;
L622's analytic phase definition fixes the zero-safe Hardy normalization.
L639 does not invoke L638's fourth-moment theorem or a growing-order
version of its fixed-order O(T) remainder. Its Cauchy extraction must
instead start with a fixed-polydisc holomorphic remainder. This is a
scope distinction to verify, not an audit conclusion.

The inspected [DLMF Table 18.3.1](https://dlmf.nist.gov/18.3#T1),
[18.5.8](https://dlmf.nist.gov/18.5#E8) and
[25.2.4](https://dlmf.nist.gov/25.2#E4) remain adequate classical inputs.
They supply normalization, the finite Jacobi formula and the regular
Laurent part; they do not import the growing endpoint or Gram estimates.
The named Phragmen–Lindelof strip theorem, functional equation and sector
Stirling are the same inputs as before. L639's compact-strip application
and Hardy phase still require audit; no uniformity follows solely from
pointwise convexity constants. The precise book citation carried by
L465 is Titchmarsh, revised Heath-Brown, second edition (1986), Section
5.1, (5.1.1)–(5.1.5), pp. 95–96; it was not freshly retrieved here.
Prior Tao (35)–(38) coverage is retained with its exercise qualification.

Duplicate/obstruction comparison is unchanged but relevant: fixed-order
Bui–Hall moments do not settle arbitrary growing-order coefficients;
the filtered fourth-moment manuscript does not settle this second Gram;
L638's two-atom theorem and L637's sufficient TV-envelope stop do not
settle this projection. The unread Minamide–Tanigawa and Lavrik leads
remain optional and unused, with their prior access qualifications.
There is no essential source blocker for this bounded audit, and no
claim of originality or literature-wide absence.

The next research turn may reproduce and critically check only the
stated audit target. Reproof is justified for the quantitative local
specialization, not for the imported arithmetic theorem. Check all of
L639 (1) and (13), including arbitrary complex coefficients and uniform
X; reject or repair an invalid inequality rather than infer a false
projection theorem. Mathlib matching coverage remains not checked.
No lemma, mathematical script, DAG edge or argument overview changed.
