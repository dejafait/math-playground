# C093a — Uniform literal full-allocation real-system exclusion

## Hypotheses

Fix an integer d with 6<=d<=33. Use L055's 25 indexed pairs,
changing only H_0=40-d and H_24=32670621+d; all J_i and all other
H_i are unchanged. Put B=9250245, kappa=23/11,
G_i=(27/16)^{J_i}(3/2)^{H_i} and Q_i=(12/11)(3/2)^{H_i}+1.
Let b_0,...,b_24 be nonnegative integers with sum_i b_i=B, and set
a_i=2+18b_i. In literal indexed order suppose real s_0,...,s_25
satisfy s_25=s_0, s_i>=540/11 and, for every 0<=i<25,

\[
s_{i+1}=2^{-a_i}(G_i s_i-Q_i)+\kappa,                 \tag{1}
\]
\[
4J_i\log2\le\log s_i+\log(11/4),\qquad
H_i\log2<\log s_i+J_i\log(27/16).                    \tag{2}
\]

Logarithms are natural. Each guard belongs to its outgoing row's own
input. All endpoints, including closure, are required. No minimum,
seed, integer-junction, parity, residue, exact-valuation, primitive-count
or actual-word premise is imposed.

## Conclusion

No such real tuple exists for any specified d over the full stated
nonnegative integer allocation simplex in literal order.

This is local RESEARCH/REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-10-21-uniform-literal-allocation-assembly.md`.
It assembles audited implications without a new numerical estimate or
claim of progress beyond the inspected source machinery. The separate
critical audit below found no defect. Cyclic-order reduction, actual-word
transfer and universal eventual descent remain unresolved. Attempt 032
and both original d=0 rational witnesses remain valid.

## Proof

Suppose a tuple satisfies the hypotheses, and keep this same d and tuple
throughout. Its lower domain makes all logarithms meaningful. Disregarding
only the H half of (2) leaves exactly the hypotheses of audited L091:
the identical table, budget, nonnegative integer allocation, literal
endpoints, lower domain and own-input non-strict J guards. Expanding
G_i,Q_i gives its displayed endpoint with both subtracted offsets inside
tail division and kappa outside. No endpoint or allocated tail is removed.
Hence L091 gives

\[
b_0=\cdots=b_{22}=0.                                  \tag{3}
\]

Set t=b_23. Integrality and nonnegativity give integer t>=0, and the
budget with (3) gives b_24=B-t>=0, hence t<=B. The complete tail list is
therefore

\[
a_i=2\ (0\le i\le22),\qquad
 a_{23}=2+18t,\qquad a_{24}=2+18(B-t).                 \tag{4}
\]

If 2<=t<=B, this same tuple meets every hypothesis of audited L092.
Indeed its fixed d, all indexed pairs, every tail in (4), all 25
endpoints with s_25=s_0, lower domain and own-input non-strict J guards
are identical. L092 excludes the entire closed integer interval, giving
a contradiction. At t=B, (4) is (a_23,a_24)=(166504412,2), and the
closing equation at that final tail 2 remains part of (1). No varying-row
growth or sampled-parameter premise is needed. Thus t<2. Since t is a
nonnegative integer, the only remaining cases are t=0 and t=1.

For t=0 the final pair in (4) is (2,166504412); for t=1 it is
(20,166504394), using 18B=166504410. Each complete tail list and every
endpoint in (1), at the same literal cut and the same d, is exactly
L093 (1). Audited L093 asserts uniqueness among all real endpoint
tuples for each such d,t. Thus the assumed tuple is the tuple to which
its conclusion applies; no feasibility of any other guard is assumed
in making this identification. In particular L093 (2) gives

\[
\log s_{18}+693015\log(27/16)-3295208\log2
<-\frac{203648044633}{100000000000}<0.                \tag{5}
\]

The row18 pair is unchanged from L055:
(J_18,H_18)=(693015,3295208). The H half of (2) at precisely the
same outgoing input s_18 requires the expression in (5) to be strictly
positive. This is a contradiction in each remaining case. The budget
split exhausts all nonnegative integer allocations, proving the claim.

No rotation or change of cut occurs. Every application uses the original
s_i with its outgoing indexed row and retains closure. No integrality of
s_i or s_i-kappa is used. The endpoint-root identification requires no
minimum, seed or successful guard at either remaining root.

### Sources, overlap and qualifications

The direct inputs are L055's pair table and the audited conclusions of
L091, L092 and L093. C088a is the d=5 precedent only, not an input or
a theorem for this changed range. L084's earlier full-test exclusions
cover d=1,...,4, not this assembly. The prior assessment checked these
scopes and duplicates; no originality follows from the local search.

The upstream affine source already specialized in those inputs is
Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Its finite real affine composition and nonzero-denominator fixed-point
formula are imported through the canonical inputs, without an integer
or parity-realization converse. Their analytic bounds reuse inspected
positive-real [DLMF 4.5.1](https://dlmf.nist.gov/4.5.E1),
[4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.2.19](https://dlmf.nist.gov/4.2.E19).
No new source specialization, analytic reproof or numerical rerun is
needed: the only additional argument is the exhaustive budget split
and same-input strict H contradiction above.

Attempt 032's failed support datum for every d>=5 remains intact.
Neither the full C077a conjunction nor the full L083 theorem is invoked.
The independent audited inputs suffice despite that failed criterion.
Both d=0 witnesses use different tables and are unaffected. This is a
literal real-subsystem exclusion only; nonliteral orders, actual words,
other tables, unrestricted cycles, divergence and universal eventual
descent are not settled.

### Independent critical audit — 2026-10-21, step 398

This RESEARCH/REPRODUCTION proof audit uses the prior SPECIALIZE
assessment `drafts/literature/2026-10-21-uniform-literal-allocation-critical-audit.md`.
It found no defect in the stated literal full-allocation exclusion.
This verifies an existing local assembly, not an additional exclusion,
improved estimate or discovery beyond the inspected sources.

**Same table and same tuple.** The full L055 table, the statements of
L091–L093 and their completed step-386/390/394 audits agree on every
indexed pair after precisely the two stated H replacements. Here d is
the H-transfer parameter, not L055's historical period multiplier.
Throughout 6<=d<=33, H_0 ranges from 34 down to 7; both range endpoints
are covered. The unchanged row18 pair is (693015,3295208). Only L055's
table is used, not its witness, minimum, seed or primitive scaling.
All statements use B=9250245,kappa=23/11 and natural logarithms.
Expanding G_i s_i-Q_i gives the displayed endpoints of L092/L093:
both subtracted terms stay inside 2^{-a_i}, and kappa stays outside.

Dropping only the strict H guards leaves every L091 hypothesis at
the original inputs: the full integer simplex, literal order, lower
domain, all non-strict J guards and all 25 cyclic equations. Its audited
early-support conclusion assumes no last-pair allocation or feasibility.
Thus (3) applies to this very tuple without the failed full support
criterion. The lower domain makes all assumed logarithms meaningful.

**Exhaustive integer split and closed boundaries.** Equation (3) and
the budget give b_23+b_24=B. Therefore t=b_23 is an integer in [0,B],
b_24=B-t, and every early tail is exactly 2. This establishes the
complete tail list (4), not just its total. Since 18B=166504410:

| t | (a_23,a_24) |
|---:|---:|
| 0 | (2,166504412) |
| 1 | (20,166504394) |
| 2 | (38,166504376) |
| B | (166504412,2) |

Every tail remains at least 2 and congruent to 2 modulo 18. On the
entire interval 2<=t<=B the original tuple meets all L092 hypotheses.
Its completed audit confirms the uniform implication including both
closed endpoints, not extrapolation from the t=2 test. At t=B row24's
tail 2 remains in the closing equation s_25=s_0. No varying-row growth
condition enters. The complement within the integer interval is exactly
{0,1}; fractional, negative and out-of-budget cases are inadmissible.

**Unique roots and the identical strict guard.** For either remaining
t, all 25 endpoints and the entire tail list are precisely L093 (1),
with the same d and literal cut. Its audited uniqueness is among all
real endpoint tuples, independent of J/H feasibility, minimum or seed.
Consequently its conclusion concerns the assumed tuple itself.
L093 gives M_18<F_18(d)<=-203648044633/100000000000<0,
where M_18 is the expression in (5). The first strict inequality and
the following weak bound justify the strict inequality in (5), including
d=6 where F_18 attains that rational upper bound. C093a (2) at the
same s_18 requires M_18>0, contradicting this in both cases. No verdict
on any other guard of either root is required.

**Scope and evidence limits.** No rotation or change of cut occurs;
each outgoing row retains its own input and tail. The direct inputs
are exactly L055,L091,L092,L093, matching the DAG. C088a is a checked
d5 comparison only. Attempt 032's failed full conjunction and both d0
witnesses remain valid. No integer-junction, realization or primitive-count
premise enters. Existing audited analytic and finite-data conclusions
are imported, not independently reconstructed in this assembly audit;
no discrepancy warrants rerunning their programs. The precise primary
citations above remain upstream coverage, with no new source theorem
specialization or numerical certificate claimed here.

The argument and direct inputs are unchanged. PROOF.md and DAG.md are
therefore unchanged; this canonical audit supersedes their pending-audit
wording for C093a. Cyclic-order reduction, actual-word transfer, other
tables and universal eventual descent remain unresolved.

## Mathlib

Full matching Mathlib coverage has not been checked. Supporting facts
about finite sums, integer intervals, affine maps and logarithms do not
constitute a formalization of this changed-range assembly. Unknown
coverage is not absence; no Lean verification is claimed.
