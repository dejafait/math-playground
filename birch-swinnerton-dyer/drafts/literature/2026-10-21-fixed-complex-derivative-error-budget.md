# Fixed derivative error budget — source-linked specialization

TARGET: Establish a complete second-derivative error budget for E=[0,1,1,-2,0] at Fourier cutoff M=128 and kernel cutoff Y=128, seeking total omitted analytic error at most 2^-30 and stating the finite-arithmetic enclosure contract, without evaluating the derivative.
CHECKED: 2026-10-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse this turn's exact-kernel, derivative-error, Wuthrich, DLMF and rigorous-integration search and local duplicate/failure comparison in drafts/source-notes/2026-10-21-complex-derivative-sources.md; no separate discovery or novelty claim.
SOURCE_EVIDENCE: Cremona (1997), Section 2.13 pp.42–44, Proposition 2.13.1 and Mellin proof https://johncremona.github.io/book/fulltext/chapter2.pdf#page=36; Wuthrich v2 Lemma 4 pp.6–7 and Section 4.1 p.9 https://arxiv.org/pdf/1608.06423v2#page=7; DLMF 4.5.4 https://dlmf.nist.gov/4.5.E4; Johansson v1 Section 2 pp.2–4 https://arxiv.org/pdf/1802.07942v1#page=2; FLINT official source callback/integration/accuracy sections https://raw.githubusercontent.com/flintlib/flint/main/doc/source/acb_calc.rst (accessed 2026-10-21).
COMPARISON: The identity, coefficient bound, logarithm comparison and rigorous finite integration are known. The necessary specialization is both complete improper remainders and outward parameter/signed-arithmetic bookkeeping at fixed cutoffs; L031 does not prove these and L035's published result is excluded as a premise.
GAP: The proposed 2^-30 threshold is unproved and untested; fixed applicability, both remainders and finite-error contract remain the mathematical attempt. No derivative value or executable backend is supplied.
REASON: Primary results cover the inputs and standard bounding mechanisms, so one proof specialization is justified; derive only the identified difference. This approves a test, not its truth; the separate step-393 literature review confirms this unchanged target is covered for the next research invocation.
SCOPE: Proof only for this model and M=Y=128; no scripts, derivative evaluation, installation, cutoff enlargement, published-order import or general BSD claim.

## Exact attempt and inputs

Use L030 for the model, conductor and modular newform, audited L099
for independent rational directions and foundations/02 for the
analytic-zero/one theorem. L031 supplies only its independently certified
bad-prime coefficient/sign, with Wuthrich's convention. L100 is motivation;
L035 is overlap. Check lower vanishing and Fricke sign against the actual
r=2 hypotheses before using Cremona.

Primary proof cases, coefficient/sign coverage, integration callback/branch
and accuracy qualifications, and duplicate/failure checks are in
[the source record](../source-notes/2026-10-21-complex-derivative-sources.md).
Do not reprove the Mellin identity or low-rank theorem.

Bound the n>128 series and y>128 tails of all 128 retained kernels,
uniformly on an explicitly justified positive enclosure of
c=2*pi/sqrt(389), seeking sum <=2^-30. This is a prospective threshold,
not a bound asserted here. Include the unnormalized L'' scale, every
coefficient/sign and finite parameter/integration/summation requirements.
Actual output enclosures must control finite error; precision/tolerance
settings alone do not. No period or Manin normalization is required.

Success could support a later finite interval excluding zero. If either
bound misses the threshold or a source hypothesis fails, record the
actual obstruction and park this schedule without changing cutoffs.
Backend availability, coefficient production/replay and actual
nonvanishing remain independent limitations. Arbitrary-curve comparison,
full Sha finiteness and the refined formula remain open. Mathlib coverage
is not checked.

## Separate approval and URL repair (step 393)

Reused the step-392 theorem comparison and duplicate/failure review.
Reopened the direct primary sources above and checked the proposition's
hypotheses/Mellin proof, coefficient-majorant passage, logarithm domain
and finite-integration contract. The rendered FLINT documentation returned
HTTP 403 in this retrieval; the official repository documentation was
accessible and supplied the callback, finite-path and accuracy sections.
Its `main` URL is a mutable source accessed on the stated date, not a
pinned release or a claim of installed-backend compatibility. No
implementation is authorized by this proof-only assessment. The source
record retains the distinction between tolerance settings and the actual
returned enclosure.

The recovery issue was missing direct URLs in this assessment's source
field, not a mathematical obstruction or changed hypothesis. SPECIALIZE
is confirmed for the exact TARGET above. Both remainder inequalities,
parameter enclosure and finite-error bookkeeping remain unproved. This
is a process repair, with no new mathematical input or bound.
