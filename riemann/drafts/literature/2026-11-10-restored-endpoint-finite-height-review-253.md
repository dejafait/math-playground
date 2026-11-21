# Restored endpoints at finite height — completed source review254

TARGET: Assess a finite-height Landau-formula representation of L988's restored endpoint sums at H=exp(n), retaining both endpoints, analytic multiplicities and the exact arithmetic jump terms.
CHECKED: 2026-11-10
DECISION: IMPORT
SEARCH_EVIDENCE: Searched uniform Landau-Gonek formula, truncated explicit formula with prime-power distance, and explicit formula for sum Lambda(m)m^(-s); followed the weighted-formula lead to Gorodetsky2211.08973v6 Lemma5.2 and its AppendixA. Exact local searches for Gorodetsky/2211.08973/truncated Landau found no previous assessment of this input; reused review249 and the recorded centered-Vaughan stop.
SOURCE_EVIDENCE: Inspected Gorodetsky2211.08973v6 (19December2023), Section5.2 Lemma5.2, PDF p15/(5.5)-(5.6), and complete AppendixA pp21-22, including the explicit s=1 double-pole case, exact closed-height restoration and all contour errors. Also inspected Montgomery-Vaughan Chapter12 pp397-401, Theorem12.5 and its supporting contour lemmas. Canonical input: foundations/2026-11-10-finite-weighted-landau-input.md.
COMPARISON: The weighted primary theorem directly retains rho-1 via its explicitly included s=1 case, midpoint jumps, nearest-other-prime-power term, analytic orders and all real T>=2. It supplies representation coverage beyond the prior sharp pointwise source. It supplies no sign for the retained weighted arithmetic prefix or for B_n; the n-dependent two-endpoint error cost is not calculated here.
GAP: Source access and exact finite-height hypotheses are resolved. Still need a separate specialization retaining K_n(n), K_n(2n), the -1, both signs, gamma_E, trivial-zero series, full endpoint weights and every source error; test the total error against exp(n/2)*n^(-3/2). The signed arithmetic prefix is unpaid even if that test passes.
REASON: Import the printed weighted theorem rather than reprove a contour formula or force the unweighted Landau formula into a denominator it does not have. A separate bounded specialization can test whether cutoff/jump costs are negligible without endpoint separation; no new lemma or mathematical script is authorized in this source turn.
LITERATURE_REASON: Changed target from the absolutely summable R_n to the restored E_n sums at growing H=exp(n); essential finite-height primary theorem hypotheses and errors remain unread.

## Original source test and its disposition

Use L988's definitions without modifying K_n or replacing its sharp
block by a smooth weight. The exact finite expression to be assessed
is the sum of E_n(rho) over |Im(rho)|<=H, with analytic multiplicity,
at H=exp(n). Both u=n and u=2n evaluations, their signs, the
denominator rho-1 and the -1 in K_n must survive. Conjugation is
available; it is not by itself a signed estimate. A theorem for
sum x^rho without a denominator would need its own justified
applicability argument, not a silent replacement of the target.

Retrieve a primary uniform finite-height Landau explicit formula,
or an explicitly applicable truncated explicit formula, starting
with its complete statement and essential proof cases. Landau's
formula and uniform refinements are search leads, not inspected
inputs. Check zero-ordinate endpoints, the convention at prime
powers, real x=e^n,e^(2n), and all errors before reading larger
passages. A theorem only for fixed x or a subsequence of heights
must not be described as uniform at the prescribed H.

Continue toward a mathematical nomination only if a precisely
cited result supplies a finite-height representation with every
error and arithmetic term explicit, and offers an independently
testable gain or obstruction relative to the benchmark
exp(n/2)*n^(-3/2). Record an informative source limit if it merely
returns the same unsigned arithmetic residual, requires unavailable
endpoint separation, or leaves errors at least as large as that
benchmark. Do not infer such a failure in advance.

L985's exact finite connection, audited L988 and L987's contextual
benchmark are the local inputs to the proposed comparison. L987
does not realize a zeta zero. Actual B_n, low-zero cancellation,
both complements, L984(H), and signed Xi positivity remain open.
No cross-notebook input is proposed. Full matching Mathlib coverage
is unchecked; no absence claim is made.

This source review is now complete. No concrete signed gain
surviving endpoint restoration is established. The new
[specialization assessment](2026-11-10-weighted-endpoint-error-specialization-254.md)
requires separate next-turn approval. It tests the error cost,
not a newly claimed signed mechanism. Preserve the exhausted
Vaughan and smooth-weight stops.

## Inspected coverage, source limits and remaining test

The exact theorem, qualifications and proof cases are in the
[canonical source input](../../foundations/2026-11-10-finite-weighted-landau-input.md).
For the intended s=1, the theorem's x>=4 and T>=2 conditions
include x=e^n,e^(2n), T=e^n for integers n>=2. The source itself
handles the pole at1; no analytic limit is newly justified in this
turn. Its closed cutoff includes zeros at T and uses analytic
multiplicities through residues. Its arithmetic sum is a midpoint
sum; neither a zero-ordinate clearance nor a lower bound on the
distance to a prime power is a theorem hypothesis.

In particular, the denominator problem is genuinely covered by a
primary theorem, rather than an unsupported integration of an
unweighted Landau error. The exact errors still have to be
multiplied by the two n-dependent kernel values. Retaining the
min{1,x/(T*<x>)} factor makes an independently testable
separation-free bound possible to investigate; its sufficiency
has not been proved here. The two-endpoint arithmetic terms
are weighted prefixes S_1, not a signed estimate for the original
Laguerre block. A passing cutoff test would isolate a technical
cost; it would leave the central signed forcing gap unresolved.

Discovery queries included `Gonek uniform Landau formula x T
distance nearest prime power theorem`, `truncated explicit
formula psi x T real x error distance prime power Davenport
theorem`, and `reference explicit formula sum Lambda(n)n^-s`.
A MathOverflow reference answer was used only to locate the
primary Gorodetsky paper; its displayed formula was checked
against the primary statement and proof, not imported on that
answer's authority. The primary PDF and HTML differ in equation
numbering, as recorded in the canonical input.

Gonek's *A Formula of Landau and Mean Values of zeta(s)*,
Topics in Analytic Number Theory (1985), pp92-97, Theorem1,
was a discovery lead at its author-hosted
[PDF](https://www.sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/8-landau-form.pdf).
The search extraction exposed its uniform unweighted statement,
but the scan's proof could not be inspected through available
image output and subsequent retrieval timed out. It is not an
imported theorem here. Ford-Zaharescu's author-hosted Lemma1
was another unweighted lead, not an essential input. The weighted
primary source resolves the essential coverage independently;
there is no persistent source blocker and no reason to retry
Gonek before the nominated calculation.

No actual finite-height endpoint bound, signed gain, new lemma,
or RH candidate was derived. Mathlib coverage remains unchecked.
