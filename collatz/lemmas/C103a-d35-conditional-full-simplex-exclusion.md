# C103a — Conditional literal d35 full-simplex exclusion

## Hypotheses

Take all 25 indexed pairs from L055's table in literal order, changing
only H_0=5 and H_24=32670656. Let b_0,...,b_24 be nonnegative
integers with sum b_i=B=9250245, and assume b_0=0. Set

\[
a_i=2+18b_i,\qquad \kappa=23/11,\qquad
G_i=(27/16)^{J_i}(3/2)^{H_i},\qquad
Q_i=(12/11)(3/2)^{H_i}+1.
\]

Suppose real s_0,...,s_25 satisfy s_25=s_0, s_i>=540/11 for
0<=i<25, and all 25 endpoint equations

\[
s_{i+1}=2^{-a_i}(G_i s_i-Q_i)+\kappa\quad(0\le i<25).
\tag{1}
\]

At each outgoing row's own input require both guards

\[
4J_i\log2\le\log s_i+\log(11/4),\qquad
H_i\log2<\log s_i+J_i\log(27/16)\quad(0\le i<25).
\tag{2}
\]

All logarithms are natural. The closing equation at i=24 remains
required when a_24=2. No minimum, seed, integer junction, parity,
residue, exact valuation, realization or primitive-period premise is
assumed. Repeated periods are allowed.

## Conclusion

No such tuple exists over the entire stated integer allocation simplex
conditional on b_0=0.

This is local RESEARCH/REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-10-25-d35-conditional-support-assembly.md`.
It assembles audited inputs; it claims no progress beyond the inspected
general sources. The separate step478 critical audit below found no
defect within these hypotheses.
The premise b_0=0 is not established here. This is not a complete
Collatz candidate.

## Proof

Assume a tuple satisfying the hypotheses exists. Keep its indexed
table, allocation, literal cut and every coordinate fixed throughout.
The lower domain ensures that all logarithms in (2) are defined.

First omit only the H guards. The identical tuple then satisfies
L103's hypotheses: its table has exactly the same two H changes,
its full nonnegative integer budget is B, its b_0 is zero, every
tail is 2+18b_i, and its lower domain, endpoints, closure and
non-strict own-input J guards agree exactly. Import L103's conclusion,
secured by its step474 critical audit, to obtain

\[
b_1=\cdots=b_{21}=0.
\tag{3}
\]

No allocation or coordinate has been changed by this implication.
Together with b_0=0 and the original budget it gives

\[
b_{22}+b_{23}+b_{24}=B.
\tag{4}
\]

Suppose b_22>0. Define integers u=b_22 and v=b_23. Nonnegative
integrality and (4) give u>=1, v>=0, u+v<=B and
b_24=B-u-v. Equations (3) and b_0=0 make every a_i=2 for
0<=i<=21, while the last three tails are exactly

\[
(a_{22},a_{23},a_{24})
=(2+18u,\ 2+18v,\ 2+18(B-u-v)).
\tag{5}
\]

Thus, after omitting only the H guards, the same real tuple satisfies
L102's entire stated domain and equations. Both subtractions in (1)
are inside the tail division, and kappa remains outside, as in L102.
All 25 endpoints, including s_25=s_0, are retained. L102's exclusion,
secured by its step470 critical audit, contradicts existence for every
such u,v. In particular it covers v=0, u+v=B and their intersection
u=B,v=0; neither a zero row23 budget nor closing tail2 is omitted.
Consequently b_22 cannot be positive. Its nonnegativity implies
b_22=0.

Now (3) gives b_0=...=b_22=0 and (4) reduces to
b_23+b_24=B. Define the integer t=b_23. Then 0<=t<=B,
b_24=B-t and the complete tail list becomes

\[
a_i=2\ (0\le i\le22),\qquad
a_{23}=2+18t,\qquad a_{24}=2+18(B-t).
\tag{6}
\]

Retain both guard families in (2) for this application. The same
table, coordinates, lower domain, full endpoints and closure with
(6) are precisely C101a's hypotheses. Its exclusion, secured by
its step462 critical audit, applies to every integer 0<=t<=B.
It includes t=0, t=1 and t=B; these retain their original strict
H guards as well as the non-strict J guards. At t=B the closing
tail is 2, and at t=0 the row23 tail is 2. Neither equation is removed.
This is the final contradiction.

The support split is exhaustive: after (3), nonnegative b_22 is
either positive or zero, and in the latter case (4) parametrizes
all remaining allocations by t. In particular the full budget on
row22 is (u,v)=(B,0), on row23 is t=B, and on row24 is t=0.
Arbitrary zero intermediate or final budgets remain included. The
argument uses no assumption that more than one recipient is positive,
no rotation and no change to later tails or their actual inputs.

### Sources, overlap and qualifications

L055 supplies only its complete indexed table, not its original-table
witness, minimum or seed. The mathematical exclusions are imported
through L103, L102 and C101a with the audits cited above. No new bound,
endpoint-root calculation or certificate replay is required for these
same-tuple substitutions. The prior assessment records the scoped
duplicate search and primary-source comparison; no novelty is inferred.

The upstream finite affine source is Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section2 equations(2)–(4), Lemma2 pp.228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Its finite-real-word and nonzero-denominator specializations are used
through the audited inputs. Their analytic imports are NIST DLMF
[4.5.1](https://dlmf.nist.gov/4.5.E1),
[4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.2.19](https://dlmf.nist.gov/4.2.E19), with positive-real hypotheses,
finite remainders and amplified errors checked there and in the reused
assessments. No general source theorem is reproved by this assembly.

Attempt032's failed row0 tail20 sufficient test supplies no premise;
b_0=0 remains conditional. Both d0 witnesses and unfinished work are
preserved. Allocations with b_0>0, order exhaustion, entry, actual-word
transfer, other tables, unrestricted cycles, divergence and universal
eventual descent remain unresolved. A restricted real-system exclusion
does not establish integer-word realization or universal descent.

### Independent critical audit — 2026-10-25, step478

This RESEARCH/REPRODUCTION proof audit uses the unchanged prior SPECIALIZE
assessment `drafts/literature/2026-10-25-c103a-conditional-assembly-critical-audit.md`.
It checks the assembly against the complete input statements and their
quantified audit arguments. It imports the completed L103, L102 and
C101a audits; it does not independently recompute their analytic bounds
or numerical certificates. No new estimate or general-source reproof
is needed for the assembly.

**Common data and logical projection.** Inspection of all 25 L055 pairs
confirms the same indexed data in each input: only H_0=40 becomes 5 and
H_24=32670621 becomes 32670656. The literal order, B=9250245,
kappa=23/11, real coordinates and lower domain are identical. Expanding
Q_i in (1) gives exactly C101a's two negative terms inside the tail
division, with kappa outside; it is also exactly the endpoint used in
L102 and L103. All statements include i=24 and s_25=s_0. The input
bound 540/11 is positive, so no logarithm needs an added domain premise.
For L103 and L102, forgetting the H inequalities is a projection of
assumptions on the fixed tuple, not a modification of its coordinates
or tails. Those inequalities remain available for the final C101a case.

**Support exhaustion.** L103 is stated for the entire nonnegative
integer allocation simplex with b_0=0, with no restriction on later
support. Its audited least-recipient argument includes j=1 and j=21,
arbitrary later allocations and b_24=0. Therefore its conclusion applies
before any support reduction: every b_1,...,b_21 is zero. The unchanged
budget then gives (4). No existence of a positive earlier recipient,
no induction hypothesis about later recipients and no row0 elimination
is being assumed. Nonnegative b_22 is either positive or zero, which
exhausts the remaining support without rotating the literal cut.

If b_22>0, integrality gives u=b_22>=1. Setting v=b_23 preserves
v>=0 and u+v=B-b_24<=B. Every preceding tail is exactly 2 and
all three remaining tails are exactly (5). Conversely every integer
u>=1,v>=0,u+v<=B describes an allocation of this branch, with
b_24=B-u-v; the substitution loses no boundary. L102 excludes
this same tuple using its own-input J guard at s_23. The unused
H guards cannot rescue a tuple already excluded by those hypotheses.

If b_22=0, the remaining allocation is exactly
(b_23,b_24)=(t,B-t), with integer 0<=t<=B. All tails (6),
endpoints, closure and both own-input guard families match C101a.
Its step462 audit covers 2<=t<=B and the two remaining integer
values 0,1. This is not an inference from sampled parameter values.
In particular the H guards have not been dropped from this application:
their strict direction is essential in C101a's t=0,1 cases.

**Boundary checks.** The positive branch includes v=0, u+v=B
and their intersection (u,v)=(B,0); the last puts the full budget on
row22. The zero branch includes t=0 (full budget on row24),
t=B (full budget on row23), and t=1 with b_24=B-1. The last two
tails at t=0,1,B are respectively (2,166504412),
(20,166504394), and (166504412,2). When u+v=B or t=B,
the closing tail is exactly 2 and the closing endpoint is still
required. Zero budgets elsewhere are already admitted by the relevant
input domains. The all-zero allocation is not a missing case, because
the fixed B is positive. No conclusion for real-valued allocations or
for a variable B is asserted.

**Verdict and limitations.** C103a's conditional assembly is valid as
stated relative to its audited inputs. No repair, narrowing, new
mathematical premise or dependency change was needed. Its direct inputs
remain L055's table, L103, L102 and C101a, exactly as recorded in DAG.md;
the latter inputs carry their own upstream mathematics. Attempt032's
failed sufficient package is not used, and neither it nor the original
d0 witnesses establishes b_0=0. The audit secures an existing restricted
input, not a stronger theorem or a complete Collatz candidate. Row0
support, order exhaustion, entry, actual-word transfer, unrestricted
cycles and divergence remain open. PROOF.md and DAG.md are unchanged
because the argument is unchanged; this canonical verdict supersedes
the overview's pending-audit wording for C103a.

## Mathlib

Full matching coverage for this conditional assembly is unchecked,
not known absent. Supporting finite-case, affine and logarithm facts
are not a matching theorem. No Lean verification is claimed.
