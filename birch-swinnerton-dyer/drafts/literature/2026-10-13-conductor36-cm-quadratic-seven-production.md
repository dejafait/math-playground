# Fixed CM finite coefficient production — separate scope approval

TARGET: Produce a finite L057 quadratic-coefficient enclosure for y^2=x^3+1 at p=7 using audited L056 symbols, testing n=2,3,4 with M=n+1 and stopping at the first strict bound min(n-1,M)>v_7(b), with complete independent replay.
CHECKED: 2026-10-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused CM scope/audit discovery and prior conductor-eleven seven-adic production coverage; searched canonical L038/L056/L057, history/196 and ATTEMPTS/022; compared the named prime-level coefficient programs with the general-relative and conductor36-table interfaces. No matching CM finite coefficient certificate was identified in these scoped records; no novelty inference.
SOURCE_EVIDENCE: Reopened Balakrishnan--Muller--Stein publisher offprint, Math. Comp. 85 (2016), pp.991--993, plus-symbol definition, measure, equations (2.6)--(2.9), Proposition 2.9 and complete proof; reused BSD-196 coverage of running c_A=1, Stein--Wuthrich Corollary 3.3/Proposition 3.5 and Conrad Theorem 4.1. Reused L038 ready coverage of Stein 2007 Propositions 3.10--3.11/Theorem 3.13 and Cremona 1997 Propositions 2.2.1--2.2.2 for composite-level paths/cosets.
COMPARISON: Known CM-inclusive analytic convergence and audited L057 cover the bound; audited L056 supplies all 72 exact values and denominator 12. The new finite adapter must use full level-36 unit orbits and the 13-dimensional integral quotient, rather than the conductor-eleven prime-level lookup, scale or schema. Existing sources supply the method, not this executable certificate or scheduled success.
GAP: Exact residues, rational unit-root approximations, every coefficient-stage path and finite b remain unproduced; no source guarantees strict success at n=2,3,4. Complete independent replay and preserved unsuccessful depths remain required. No CM rank implication, lower vanishing, Sha or complex-order comparison is covered.
REASON: Separate implementation-scope comparison now approves the unchanged target for a later known-method reproduction; retain all audited source qualifications and require the complete table/path adapter obligations below.

Main gap: arbitrary-curve rank equality at complex analytic order at least
two. Intermediate target: the actual conditional-bound test for this CM
instance. Downstream use: a certified analytic quadratic coefficient,
without a CM arithmetic rank theorem. Essential inputs are L057, L056's
72 exact values and full relative presentation, L038's audited N=36
domain inherited there, L028's orientation, L050 and L052's arithmetic
and differential scale. L051's total-period convention is retained
through L056. No cross-notebook result is involved.

Proposed finite contract: primitive untwisted trivial branch, gamma=8,
C=0, t=-4, exact rational unit u=-4 modulo seven and residual valuation
at least M=n+1. Certify every Teichmuller residue, all required oriented
cusp paths and both symbol families, and every binomial(j,2) summand.
Independent replay must reconstruct values from the full table and
integral quotient; expected nonvanishing must not be an input. Preserve
each unsuccessful depth and original evidence. Test exactly n=2,3,4,
stopping at the first strict success; if none succeeds, record that
finite failure without extrapolating vanishing or extending the schedule.

Remaining assumptions and limits: certified exact finite data are still
to be produced; no useful coefficient, lower vanishing, rational
directions, Sha or complex-order comparison is granted. L004 remains
unavailable for this CM curve. Full matching Mathlib coverage is not
checked. ATTEMPTS/022's stop on input-free reaudits and every earlier
analytic/workload stop remain intact. The original proposal requested separate approval. The review below
now supplies scope approval, without executing the proposed mathematics.

## Separate implementation-scope review, 2026-10-13, BSD-197

LITERATURE_REASON: The saved REVIEW_REQUIRED target changes the executable model, composite-level coset lookup and symbol-table schema; ready analytic coverage alone did not compare these essential adapter obligations.
SCOPE: Exactly the TARGET above; minimal optimal model [0,0,0,0,1], N=36, p=7, primitive untwisted trivial branch, total real minimal period, gamma=8, C=0, t=-4, audited L056 full-relative functional, depths n=2,3,4 and M=n+1, complete independent replay and first strict-success stopping.

### Primary inputs and applicability

[Balakrishnan--Muller--Stein, Math. Comp. 85 (2016),
983--1016, DOI 10.1090/mcom/3029](https://wstein.org/papers/mcom3029.pdf#page=9),
pp.991--993, defines the plus symbol, ordinary unit-root measure and
finite polynomial in the 1+p coordinate. Proposition 2.9 and its complete
proof give coefficientwise convergence and explicitly carry over the
coefficient bounds. Equation (2.9) retains the ordinary interpolation
multiplier. These inspected passages match L057's two symbol arguments,
root powers and six-class sum. No CM exclusion is imposed by this input.
Reuse the unchanged period/differential applicability checked in BSD-196:
coefficient field Q, optimal degree-one quotient and differential scale
one from L052, total real period and exact ordinary arithmetic from
L050/L052. No central nonvanishing or lower-coefficient vanishing is
required. The cited theorem does not guarantee a useful finite quadratic
coefficient at these three depths.

The retained precision sources are [Stein--Wuthrich, Math. Comp. 82
(2013), Section 3, Corollary 3.3 and Proposition 3.5,
pp.1764--1765](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=8),
through the CM-inclusive carryover, and [Conrad, *Hensel's Lemma*,
Theorem 4.1, printed p.6](https://kconrad.math.uconn.edu/blurbs/gradnumthy/hensel.pdf#page=6).
Their hypotheses and essential zero/trivial-character cases were already
inspected for L057; this review does not reopen its mathematical audit
or rederive its bound. Rational u must be a unit congruent to -4 modulo
seven, not necessarily the integer -4, with the exact residual and unit
derivative certified at each M. The ordinary measure, rather than a
main conjecture or arithmetic rank theorem, is the imported input.

For the full relative path adapter reuse the ready construction and
implementation assessments, canonical L038 steps 1 and 3, [Stein,
*Modular Forms, a Computational Approach*, GSM 79 (2007),
Propositions 3.10--3.11, Theorem 3.13](https://wstein.org/books/modform/stein-modform.pdf),
and [Cremona, *Algorithms for Modular Elliptic Curves*, corrected second
edition (1997), Propositions 2.2.1--2.2.2,
pp.15--16](https://johncremona.github.io/book/fulltext/chapter2.pdf).
Their arbitrary-level integral relative presentation, composite projective
cosets and continued-fraction path method already cover this mathematical
domain. No new path theorem or universal software correctness claim is
needed. Original Manin/Kannan--Bachem references remain indirect,
nonessential leads; their unread status is unchanged.

### Interface comparison and complete evidence contract

Read the relevant code ranges of
`scripts/conductor-eleven/quadratic-seven/build_certificate.py` and
`verify_certificate.py`, `scripts/general-relative/build_certificate.py`
and `scripts/conductor36-table/build_table.py`/`verify_table.py` without
execution. The conductor-eleven coefficient builder uses an inverse of
the bottom-left entry modulo a prime and the list (0,1),(1,t); its checker
hardcodes that list, twelve generators, dimension three and scale 1/5.
These cannot be transferred as constants or as a composite-level lookup.
General-relative `build` instead supplies all primitive bottom-row unit
orbits, assignments, lifts and exact Gamma_0 membership witnesses.

Bind `scripts/conductor36-table/presentation.json` with inputs N=36,
P empty, all 72 original generators, 144 source relations, 59 saturated
columns, quotient section and 72-by-13 generator coordinates. For every
segment, reconstruct its primitive bottom row and full unit-orbit coset,
check the determinant-one lift and h*g_i^(-1) in Gamma_0(36), ordered
endpoints, adjacency and telescoping. Independent replay must reconstruct
orbit completeness and locate each segment independently of the producer's
lookup; a noninvertible bottom-left residue is an ordinary case.

Read L056's canonical table statement and quotient reconstruction proof.
Its actual schema is `conductor36-coupled-table-v1`: normalized values
are each generator row's `value`, and quotient values are
`relations.quotient_values`, with common denominator twelve. They are
already normalized, so no conductor-eleven scale or new calibration is
to be applied. All sixteen zero values, all generator ordering, source
relations, saturated columns and quotient reconstruction must be retained.
The bounded JSON previews were used only to locate fields, not as proof
of their contents; correctness here is imported from audited L056.
The later coefficient replay must read and check the complete relevant
evidence, run the existing full table/upstream verifiers to fresh output
paths, and preserve the original bytes. Audit flags or hashes alone are
not mathematical verification. The saved table's historical
`critical_audit_complete: false` is a production-era field; the separate
canonical BSD-192 audit supplies its actual audited status.

At each reached depth record all six Teichmuller residues, their residual
and derivative checks, least-positive residues of w*8^j, both exact cusp
arguments and oriented paths, every binomial(j,2) term including zeros,
and the complete exact rational sum. Replay must recompute these without
importing the coefficient producer or using expected nonvanishing as an
input. Path raw-table and full-quotient evaluations must agree. A stored
reverse path must be negated according to L028/L057. The primitive
multiplier, gamma=8 and all finite newform Euler factors remain fixed.

### Duplicates, failures, decision and limitations

The scoped prior records contain L033/L042 seven-adic production for
other models and L047's depth-four success at five. Those are method
examples, not evidence for this CM coefficient. ATTEMPTS/022 prohibits
input-free conditional reaudit as production; audited L056 now supplies
the missing symbols, and BSD-196 supplies the distinct CM analytic
application. Preserve that stop and ATTEMPTS/025--028's wrapping/workload
failures. None is a failure of this exact finite rational sum. The new
comparison supplies adapter obligations, not a new mathematical result
or a claim of novelty; no wider discovery search was needed.

DECISION SPECIALIZE approves only later known-method reproduction of
this exact finite contract. Stop at first strict N>v_7(b), with
v_7(0)=infinity; otherwise retain all three inconclusive depths and
reassess before any extension. Stop a dependent inference on an essential
path, root, normalization or replay failure. Sources do not guarantee
schedule success. No calculation, new lemma, mathematical script or
proof/DAG change was made during this literature turn. Full matching
Mathlib coverage remains not checked. Rational directions, lower
vanishing, divisible/full Sha and arbitrary complex-order/rank comparison
remain unresolved, and L004 is still unavailable for this CM curve.
