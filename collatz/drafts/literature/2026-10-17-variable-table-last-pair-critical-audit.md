# L077 critical audit — proposed source assessment

TARGET: Critically audit L077's variable-table last-pair cutoff and its complete L068 benchmark, including coefficient signs, uniform domain, boundary tests and small budgets.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step 286 discovery and theorem comparison; read full L077 and audited L068, relevant L051/L055/L064 passages, construction notes/history 286–287, and Attempts 026–031; no duplicate independent L077 audit was found in this scoped evidence.
SOURCE_EVIDENCE: Reused inspected Halbeisen–Hungerbuehler (1997), section 2 equations (2)–(4), Lemma 2 pp. 228–229 and essential induction cases, plus DLMF 4.5.1/4.6.4/4.2.19 positive-real coverage from steps 282/286; full L068 proof/audit and selected exact boundary/probe records were read without recomputation.
COMPARISON: Known finite affine composition and positive-real analytic tools cover the audit methods; audited L068 covers the complete fixed benchmark, but neither independently verifies L077's variable-table data tests, quantified sufficiency or small-budget cases.
GAP: Independently verify L077's coefficient signs, uniform-domain proof, boundary inequality directions, quantified cutoff and complete benchmark operands; no new source gap remains for this exact audit.
REASON: Separate source-scope comparison is complete for one later RESEARCH/REPRODUCTION proof audit; coverage approval is not a no-defect verdict or new mathematical result.
SCOPE: Only the exact TARGET with L077's literal indexed table/budget and endpoint/domain/non-strict own-input J subsystem; no new-table search, integer exclusion, order/support assembly or actual-word application.

The original proposal below is preserved; separate step-288 approval
follows it. It was not an approval or completed audit. The review compared the exact written L077 against reusable coverage in
`drafts/literature/2026-10-17-variable-table-last-pair-cutoff.md`.
Unchanged primary evidence need not be browsed again if adequate.

The main gap remains universal eventual descent. This intermediate audit
could validate a portable last-pair reduction for tables satisfying the
explicit tests. Combining it with L075/L076 and excluding the remaining
integer allocations are independent, unproved downstream steps. The
criterion establishes no new-table exclusion or Collatz candidate.

Essential inputs: full L077; L051 endpoint/J and pointwise shift passages;
complete audited L068 and its ready assessment; L055 table and Lambda
bounds; L064 analytic bounds and t=1 survivor facts. The construction
script/certificate are `scripts/postspell-word-count/certify_variable_table_last_pair.py`
and `scripts/postspell-word-count/variable-table-last-pair-certificate.json`.
No cross-notebook theorem input is proposed. L075/L076 are motivation only.

Retain integer r>=3, increasing integer J_i>=2, H_i>=3, B>=0,
early b_i=0, b_(r-2)=t, b_(r-1)=B-t, a_i=2+18b_i and all integers
0<=t<=B. Check all endpoints including closure, lower domain s_i>=540/11
and non-strict J guards at their own outgoing inputs. Data conditions
include the certified Lambda bracket, eta_0/eta_(r-1) lower bound,
strictly positive fixed-point denominator, rational incoming-prefix bounds
at tau, normalized-root upper bound and signed logarithm margin. No H/seed,
minimum, growing varying-row, integer/parity/valuation realization or
primitive/count-ray premise is available.

Audit the full formulas for n_0(t) and n_(r-1)(t), positive A,C,D,
parameter-independent earlier prefixes and the unchanged final product.
Check that the uniform domain uses only unchanged tail-2 growth and the
two tested eta bounds. Verify the sum and every inequality in the boundary
normalization, both logarithm coefficient signs, r=3, tau=0 or 1,
tau=B with final tail 2, tau>B, and B=0 or 1 with tau=2. Empty rejection
sets imply no guard verdict; endpoint/domain conclusions still need (3).

Recover the complete L068 benchmark 2<=t<=9250245 and exact margin
-474883782659/125000000000<-3.79. Import the t=0,1 survivors separately,
and preserve the failed optional <-4 probe and both rational witnesses.
Inspect full load-bearing certificate values rather than previews.
Continue if independent checks find no defect; otherwise identify the
precise gap or repair without expanding scope. Failed sufficient tests
prove neither feasibility nor infeasibility. Full matching Mathlib coverage
is unchecked. This proposal derives no further mathematical result.

## Separate source-scope approval — step 288, 2026-10-17

LITERATURE_REASON: The newly written L077 critical-audit target required separate scope approval; reuse ready source coverage rather than repeat discovery or external browsing.

The main gap is universal eventual descent. This step approves source
scope for an independent audit of the portable last-pair criterion, not
the criterion's correctness. A validated cutoff could later reduce the
parameters remaining after the separate order/support criteria. Their
assembly and survivor integer exclusion remain independent unresolved
steps. No new-table or universal exclusion follows from source approval.

### Exact source scope and comparison

Reused the complete construction assessment
[step 286](2026-10-17-variable-table-last-pair-cutoff.md), including its
two focused discovery queries, primary theorem/proof-case inspection and
stronger-result comparison. The target and analytic hypotheses have not
expanded beyond its finite affine last-pair mechanism. No external source
was newly retrieved. Unread rational/high-cycle leads remain unread and
are not essential to this audit; no failed search certifies novelty.

The precise standard input is Halbeisen–Hungerbuehler, *Optimal bounds
for the length of rational Collatz cycles*, Acta Arithmetica 78 (1997),
227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The reused inspection covers the finite binary-word affine composition,
fixed-point formula, length-one and appended-zero cases; appended one
is printed as analogous. Import only formal affine algebra for a finite
nonempty word with nonzero fixed-point denominator. L077's integer row
parameters define such words, while its explicit positive-Lambda test
must establish the denominator condition. L055's numerical Lambda bounds
apply only to the benchmark. Coordinate matching is a local proof
obligation; no parity/integer-realization converse or general coding
reproof is needed. Lemma 4's equal-count, every-prefix domination result
orders scalar numerators, not simultaneous own-input guards, and is not
an input to this audit.

Reuse positive-real analytic coverage from
[step 282](2026-10-17-variable-table-early-support-criterion.md):
NIST DLMF [4.5.1](https://dlmf.nist.gov/4.5.E1),
[4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.2.19](https://dlmf.nist.gov/4.2.E19). The recorded domains include
these positive-real arguments; L055/L064/L068 supply the exact finite
remainder and outward-rounding evidence. The sources were inspected in
the reused reviews, not reopened here; no current release number was
verified this turn. The audit must check the uses, signs and exact
operands, and distinguish imported benchmark enclosures from newly
computed checks. Full matching Mathlib coverage remains unchecked.

Read full L077, then full L068 including its independent audit. Read
L051's endpoint/J conditions and pointwise shift, L055's complete table,
counts/Lambda enclosure, and L064's analytic method, t=1 comparisons and
relevant audit passages. Only these elementary endpoint/guard passages
are inputs: L051's minimum, seed, H and primitive-count hypotheses are
not available. The known affine theorem is not already a proof of
L077's parameter-dependent domain and sufficient boundary tests.

### Duplicate, failure and evidence checks

The supplied overview/DAG and scoped construction/audit records show
L068's fixed-table audit is complete, while L077's independent audit is
pending. L075/L076 concern different conditions and are motivation only.
Read Attempts 026–031: real witnesses and prime cancellations stop their
specified exclusions, while one permuted guard failure concerns one
order. None answers the present sufficiency audit or warrants rejecting
the two known rational witnesses. No stopped diagnostic is reopened.

The JSON inspector located all certificate fields. Read the complete
selected /boundary record (all 25 rows and incoming exponents) and
/preserved_optional_probes. The stored boundary margin is
-474883782659/125000000000; the optional requested bound <-4 is false.
These are accessible stored claims, not independently verified arithmetic.
The root preview establishes only evidence location. All prefix bounds,
17 rational check operands, 11 integer checks, the exponential sum's
41 terms, and imported analytic qualifications remain for the audit.
No mathematical program was run or changed, and no certificate was
regenerated. The inspector's unsupported slash-root pointer was retried
with its default root preview; this was an inspection error only.

### Approved bounded continuation

SPECIALIZE approves exactly TARGET for one later RESEARCH/REPRODUCTION
proof audit. Essential IDs: L077 in full; L051 endpoint/J/shift passages;
complete audited L068 and its ready assessment; L055 table/Lambda and
L064 analytic/t=1 facts. Check all r>=3, increasing integer J_i>=2,
H_i>=3, B>=0, early zero support, both varying tails, every closed integer
t parameter, every endpoint including closure, s_i>=540/11 and own-input
non-strict J guards. No H/seed, minimum, growing varying-row, integer
realization or primitive/count-ray premise may be added.

Independently check (7)–(12), every positive coefficient and denominator,
parameter-independent incoming prefixes, the complete invariant product,
both eta-domain tests and unchanged-row growth. Check the full sum and
normalization inequalities, log coefficient signs and strict rejection
against a non-strict guard. Retain r=3, tau=0/1/B or >B, B=0/1 with tau=2,
and the closing tail-2 edge. Empty rejection intervals imply no guard
verdict, and their endpoint/domain claim still needs (3).

Reconstruct the complete benchmark arithmetic independently of the
construction program; a rerun or stored pass flag alone is not an audit.
Use L068's complete audited benchmark evidence for imported enclosures
and both t=0,1 survivors with exactly matching tails. Do not transfer
fixed-table numerical properties to arbitrary tables. Inspect complete
load-bearing evidence and preserve the original certificate and failed
<-4 probe. Continue to a no-defect verdict only after all essential
obligations pass; otherwise identify the exact defect and its effect,
repair within scope if possible, or stop that claim. Failed sufficient
tests imply neither feasibility nor infeasibility. No new table,
order/support assembly, integer arithmetic or actual-word bridge is
approved. There is no essential source blocker or cross-notebook input.

Completed LITERATURE/NOVELTY_UNCHECKED, outcome EXPLORATION: a new
source-scope comparison makes the unchanged audit target ready; no
mathematical result, independent audit or certified novelty is claimed.
Mathematical exploration usage remains zero after step 287.
