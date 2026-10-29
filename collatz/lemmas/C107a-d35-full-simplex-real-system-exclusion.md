# C107a — Literal d35 full-simplex real-system exclusion

## Hypotheses

Take all 25 indexed pairs from L055's table in their literal order,
changing only H_0=5 and H_24=32670656. Let

\[
B=9250245,\qquad \kappa=23/11,\qquad
b_i\in\mathbb Z_{\ge0}\ (0\le i<25),\qquad
\sum_{i=0}^{24}b_i=B,
\]
\[
a_i=2+18b_i,\qquad
G_i=(27/16)^{J_i}(3/2)^{H_i},\qquad
Q_i=(12/11)(3/2)^{H_i}+1.
\]

Suppose real s_0,...,s_25 satisfy s_25=s_0, s_i>=540/11 for
0<=i<25, and every endpoint equation

\[
s_{i+1}=2^{-a_i}(G_i s_i-Q_i)+\kappa
\quad(0\le i<25).
\tag{1}
\]

At each outgoing row's own input require both guards

\[
4J_i\log2\le\log s_i+\log(11/4),\qquad
H_i\log2<\log s_i+J_i\log(27/16)
\quad(0\le i<25).
\tag{2}
\]

All logarithms are natural. Every zero budget is permitted, including
b_24=0; the row24 equation and closure still apply when a_24=2.
There is no minimum, seed, integer/parity/residue junction, exact
valuation, actual-word realization or primitive-period premise.
Repeated periods are allowed.

## Conclusion

No such real tuple exists for any allocation in this entire integer
simplex, without a restriction on the support of b.

This is local RESEARCH/REPRODUCTION under the invocation-start SPECIALIZE
assessment `drafts/literature/2026-10-26-d35-unrestricted-budget-assembly.md`.
It joins two audited local exclusions; it claims no discovery beyond
the inspected sources. The separate step519 critical audit below finds
no defect relative to the audited inputs. This is not a complete Collatz
candidate, and no actual-word transfer or arbitrary-order conclusion
is asserted.

## Proof

Assume an allocation and tuple satisfying all hypotheses exist. Keep
their original indices, allocation and coordinates fixed throughout.
Since every s_i>=540/11>0, all logarithms in (2) are defined.
Nonnegative integrality gives the exhaustive alternatives b_0=0 or
b_0>=1. No other budget coordinate is restricted by this split.

**Case b_0=0.** Apply C103a, with its step478 critical audit, to
this same allocation and tuple. Its literal table has exactly the
same two H changes, its constants are B=9250245 and kappa=23/11,
and its tails are exactly a_i=2+18b_i. Its lower domains, all 25
endpoint equations and closure are precisely (1) and the hypotheses
above: in particular Q_i, including both of its summands, is inside
the tail division, and kappa is outside. Both guard families in (2)
are retained, with their original non-strict J and strict H signs
and the same own-input s_i. The additional premise of C103a is
exactly this case's b_0=0. C103a therefore contradicts existence
over this entire branch, including every pattern of later zero
budgets and b_24=0.

**Case b_0>=1.** For each original input i, positivity and the
strict monotonicity of the real exponential give

\[
4J_i\log2\le\log s_i+\log(11/4)
\quad\Longleftrightarrow\quad
2^{4J_i}\le(11/4)s_i
\quad\Longleftrightarrow\quad
s_i\ge(4/11)2^{4J_i}.
\tag{3}
\]

Consequently the same tuple obeys the exact J guards in L107's
endpoint system (2). All its other hypotheses match: the literal
table and two H changes, the nonnegative integer budget summing to B,
b_0>=1, the individual tails, G_i, Q_i, kappa, all endpoints, closure
and the lower domains are unchanged. L107, with its step515 critical
audit, excludes this J-only system on the whole stated branch.
We apply that exclusion by forgetting only the H inequalities as
assumptions; we do not alter any coordinate or endpoint. A tuple
obeying both guard families would also obey this J-only system,
so its infeasibility is a contradiction. No converse implication
from the J guards to the H guards is used.

These two contradictions exhaust every admissible allocation. The
partition uses integrality: it does not assert coverage of fractional
budgets with 0<b_0<1. The total B remains fixed in each application,
and no support reduction, rotation, selection of a new endpoint root
or assumption on which input is smallest is made.

In particular b_0=1 and b_0=B are included in the positive branch;
when b_0=B all other budgets vanish, including b_24. The zero branch
includes the entire budget on any row1,...,24 and all intermediate
allocations, by C103a's quantified statement, not by sampling those
extremes. Closing tail2 in either branch retains its original row24
endpoint and s_25=s_0. Neither component assumes a primitive period,
so no repeated period is removed. This proves the conclusion.

### Sources, verification and qualifications

L055 supplies only the literal indexed table. Its original-H witness,
minimum and seed are not premises. C103a and L107 supply the exclusions
with their complete hypotheses and canonical audits. Their audited
bounds and certificates are imported unchanged: this finite case
application changes no operand and needs no new numerical estimate,
mathematical script or certificate replay.

The prior assessment records the primary-source comparison and the
bounded duplicate/failure search. The upstream finite-affine source is
Halbeisen and Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[section2 equations(2)–(4), Lemma2 pp.228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The finite-maximum source used through L107 is Blanchard, Higham and
Higham, *Accurate Computation of the Log-Sum-Exp and Softmax Functions*,
MIMS EPrint2019.16, author version 2019-09-08,
[section4 equations(4.1)–(4.2), printed p.8](https://eprints.maths.manchester.ac.uk/2728/1/paper.pdf).
The analytic source coverage reused by the assessed components includes
NIST DLMF version1.2.8,
[4.5.1](https://dlmf.nist.gov/4.5.E1),
[4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.2.19](https://dlmf.nist.gov/4.2.E19).
Their domain, denominator and finite-error qualifications remain in
the component proofs. None of these sources is asserted to state
this literal full-simplex verdict; no general source theorem is
reproved here. The only additional steps are the integer partition,
the positive-domain guard conversion (3), and the same-tuple applications.

Attempt032's failed sufficient package, Attempt033's endpoint-only cap
counterexample and Attempt034's failed fixed full-guard witness supply
no premise. Attempt035's stop on repeated L107 source approval does
not block this separately approved assembly. All remain preserved.
This result removes the support restriction only for this fixed table,
order, budget and real system. Actual-word transfer, arbitrary order,
entry, unrestricted cycles, divergence and universal eventual descent
remain unresolved; excluding a restricted real system proves none of
those claims by itself.

### Independent critical audit — 2026-10-26, step519

This RESEARCH/REPRODUCTION proof audit uses the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-26-c107a-full-simplex-assembly-critical-audit.md`.
The complete C107a, C103a and L107 proofs, including the canonical
step478 and step515 audits, and all25 indexed pairs in L055 were read.
The component exclusions and their audited numerical bounds are imported;
this audit checks their applications without replaying certificates or
asserting a new bound. The primary-source qualifications above and in
the components remain in force.

**Common object.** All three statements use the same indexed pairs,
changing only the original H0=40 to5 and H24=32670621 to32670656.
They have the identical B=9250245, kappa=23/11, nonnegative integer
allocation with sum B, and tails a_i=2+18b_i. The common endpoint is

\[
s_{i+1}=2^{-a_i}\bigl((27/16)^{J_i}(3/2)^{H_i}s_i
                  -(12/11)(3/2)^{H_i}-1\bigr)+23/11.
\]

Both subtractions are inside the division by 2^{a_i}; the final
23/11 is outside. Neither application introduces a shift, reindexing,
new endpoint root or allocation. The common lower domain is s_i>=540/11
for i=0,...,24, and the i=24 equation has the original s25=s0.
Closure also gives the same positive lower domain at s25. L055 supplies
its table only, not its original-H witness, seed or minimum premise.

**Exhaustive partition and zero branch.** For a nonnegative integer
b0, either b0=0 or b0>=1, with no restriction on the other24 coordinates.
When b0=0, C103a's additional hypothesis holds and every other hypothesis
is identical, including both inequalities at each row's own s_i.
The H guard stays strict and is retained for C103a's C101a application;
the J guard stays non-strict. Its audited conclusion excludes the whole
branch, not sampled supports. Its internal support reduction is a proved
implication on this tuple, not an extra premise of C107a.

**Positive branch and implication direction.** At every original input
s_i>0. Thus exp(log s_i+log(11/4))=(11/4)s_i, while
exp(4J_i log2)=2^{4J_i}. Applying the strictly increasing exponential
and multiplying by positive 4/11 proves exactly (3), with non-strict
inequalities in both directions. Each logarithmic J guard therefore
supplies precisely L107's s_i>=g_i. Its remaining hypotheses, including
b0>=1, already hold on the same tuple. L107's conclusion explicitly
excludes its endpoint system (2), not merely an unrelated selected
maximum-term branch. Forgetting H guards enlarges the assumed feasible
set; infeasibility of that enlarged set excludes the full-guard tuple.
No H guard is deduced from J, and no converse to L107's necessary
relaxation is used.

**Boundaries and scope.** The positive branch includes b0=1,b0=B
and arbitrary permitted zero budgets; at b0=B all other budgets vanish.
The zero branch includes full budget on any one of rows1–24 and every
other allocation quantified by C103a. An all-zero allocation is
inadmissible because B>0. If b24=0 in either branch, a24=2 and the
closing equation is still required. Neither component assumes primitive
period, so repetitions remain included. The proof does not extend the
integer partition to fractional 0<b0<1, change B or add junction
integrality, residues, valuations or word realization.

**Verdict.** C107a is valid as stated relative to its audited components.
No repair, narrowing or dependency change is required. Direct inputs
remain L055 (table only), C103a and L107, exactly the existing DAG row.
This secures an existing restricted input, not a stronger theorem or
progress beyond the sources checked. The argument is unchanged, so
PROOF.md and DAG.md are unchanged; this canonical verdict supersedes
their pending C107a-audit wording. Full-support actual-word transfer,
arbitrary order, entry, unrestricted cycles, divergence and universal
descent remain unresolved. No complete candidate is asserted.

## Mathlib

Full matching coverage for this assembly is unchecked, not known absent.
Supporting integer-case, logarithm, exponential and affine coverage is
also unchecked here; no Lean verification is claimed. The result is
the explicit informal application above of the audited local inputs.
