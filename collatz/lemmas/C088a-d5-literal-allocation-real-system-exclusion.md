# C088a — d=5 literal full-allocation real-system exclusion

## Hypotheses

Use L055's 25 indexed pairs, replacing only H_0=40 by 35 and
H_24=32670621 by 32670626; all J_i and all other H_i are unchanged.
Set B=9250245, kappa=23/11,
G_i=(27/16)^{J_i}(3/2)^{H_i} and Q_i=(12/11)(3/2)^{H_i}+1.
Let b_0,...,b_24 be nonnegative integers with sum_i b_i=B, and put
a_i=2+18b_i. In literal indexed order require real s_0,...,s_25 with
s_25=s_0, s_i>=540/11 and, for every 0<=i<25,

\[
s_{i+1}=2^{-a_i}(G_i s_i-Q_i)+\kappa,                 \tag{1}
\]
\[
4J_i\log2\le\log s_i+\log(11/4),\qquad
H_i\log2<\log s_i+J_i\log(27/16).                    \tag{2}
\]

All logarithms are natural. Each guard belongs to the input of its own
outgoing indexed row. Every endpoint, including the closing edge, is
required. There is no minimum, seed, integer-junction, parity, residue,
exact-valuation, primitive-count or actual-word premise.

## Conclusion

No such real tuple exists over the full stated nonnegative integer
allocation simplex in literal order.

This is local RESEARCH/REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-10-20-d5-literal-allocation-assembly.md`.
It assembles audited inputs, with no new numerical certificate or claim
of progress beyond the inspected source machinery. The separate critical
audit below found no defect. Cyclic-order reduction and actual-word transfer
are not supplied; universal eventual descent remains unresolved. Both
original d=0 rational witnesses and Attempt 032 remain valid.

## Proof

Suppose such a tuple exists. Its positive lower domain defines every
logarithm in (2). Temporarily ignore only the H guards. The remaining
hypotheses are exactly those of audited L086: the same changed table,
B, nonnegative integer allocation, tails, literal cyclic endpoints,
lower domain and non-strict own-input J guards. In particular no tail
or closing equation is removed. L086 therefore gives

\[
b_0=\cdots=b_{22}=0.                                  \tag{3}
\]

Set t=b_23. Since all b_i are nonnegative integers, (3) and their total
budget give b_24=B-t, with integer 0<=t<=B. Consequently the full tail
list, not merely its sum, is

\[
a_i=2\ (0\le i\le22),\qquad
 a_{23}=2+18t,\qquad a_{24}=2+18(B-t).                 \tag{4}
\]

If 2<=t<=B, equations (1), the lower domain and the J half of (2),
with precisely (4), satisfy every hypothesis of audited L087. Its
full-interval exclusion contradicts the assumed tuple. This includes
t=B, where a_24=2 and (1) still imposes the closing edge. No growth
premise or sampling of interior parameters is added. Thus t<2.
Together with integer 0<=t this leaves exactly t=0 or t=1.

For t=0 the final two tails in (4) are 2 and 166504412. For t=1 they
are 20 and 166504394. Both lists, the changed pair table, all 25
endpoints and s_25=s_0 match audited L088 exactly. For each specified
parameter L088 asserts a unique real endpoint tuple. The tuple assumed
here satisfies those very equations at the same literal cut, so it is
that unique tuple. L088 requires no guard, domain, minimum, seed or
feasibility premise to identify it. Its conclusion at the outgoing
row18 input is

\[
\log s_{18}+J_{18}\log(27/16)-H_{18}\log2
<-\frac{81550766911}{50000000000}<0.                   \tag{5}
\]

But the H half of (2) at that same input, with the unchanged pair
J_18=693015,H_18=3295208, says this expression is strictly positive.
This contradicts (5) for each of t=0 and t=1. The integer interval
0<=t<=B has been exhausted, proving the conclusion.

No cyclic relabeling occurs: every application uses the original
s_i as the input of outgoing row i. In particular row18's H guard is
never transported to another input, and every closing equation remains
unchanged. No assertion that either candidate satisfies the other
guards is needed. Nor is any integrality of s_i or s_i-kappa used.

### Sources, overlap and qualifications

Only the audited statements L086, L087 and L088, and L055's indexed
table identification, are imported. The upstream formal affine input is
Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The analytic inputs are the previously inspected positive-real
[DLMF 4.5.1](https://dlmf.nist.gov/4.5.E1),
[4.6.4](https://dlmf.nist.gov/4.6.E4) and
[4.2.19](https://dlmf.nist.gov/4.2.E19).
Their hypotheses, fixed-point denominator and outward numerical bounds
have already been specialized in the canonical inputs. This proof uses
no fresh affine, logarithmic or exponential estimate and does not
reprove those known results. Its sole additional argument is the
exhaustive budget case split and the matching of the strict H guard.

C082a treats d=1 and includes an all-order reduction; it is not a d=5
input or duplicate of this literal statement. Attempt 032 still stops
the full C077a sufficient-test conjunction at d=5. Neither that
unavailable conjunction nor L083's full theorem is invoked here. The
separate canonical inputs suffice despite the failed support datum.
The d=0 tables of the two original rational witnesses differ from this
one, so those witnesses are unaffected. No nonliteral order, actual
word, arbitrary cycle, divergence or universal-descent conclusion is
asserted.

### Independent critical audit — 2026-10-20, step 361

This RESEARCH/REPRODUCTION proof audit uses the prior SPECIALIZE
assessment `drafts/literature/2026-10-20-d5-literal-allocation-critical-audit.md`.
It found no defect in the stated literal real-system exclusion. This
verifies the existing assembly; it adds no exclusion family, analytic
estimate or progress beyond the inspected source machinery.

**Identical table and hypotheses.** L055's complete pair table has
H_0=40 and H_24=32670621. The two replacements here give precisely
H_0=35,H_24=32670626 in each of L086, L087 and L088; every other
pair is identical, including (J_18,H_18)=(693015,3295208).
All four statements use B=9250245, kappa=23/11, natural logarithms
and the same two endpoint offsets. Expanding G_i and Q_i in (1)
gives exactly the displayed endpoints of L087 and L088.
The lower domain makes all assumed logarithms meaningful.
Dropping the H half of (2) leaves every L086 hypothesis, including
nonnegative integer allocations, literal chronology, every non-strict
own-input J guard and the closing equation. L086's audited conclusion
is unconditional on any last-pair or H verdict. Its step-349 audit
explicitly checks the cap's all-allocation quantifier and both end
recipients. Thus (3) requires neither the failed full support criterion
nor an assumption that row0 receives extra tail.

**Exhaustive budget and both interval endpoints.** After (3),
sum_i b_i=B reads b_23+b_24=B. Nonnegativity and integrality give
t=b_23 in {0,...,9250245} and b_24=B-t. Each early tail is therefore
exactly 2, not merely bounded by 2. The identity
18B=166504410 gives all three boundary checks:
at t=0 the last pair is (2,166504412); at t=1 it is
(20,166504394); at t=B it is (166504412,2).
Every tail remains at least 2 and congruent to 2 modulo 18.
For the entire closed interval 2<=t<=B, the original tuple satisfies
L087's endpoints, lower domain and J guards with these same tails.
L087 and its step-353 audit include t=2 and t=B explicitly; their
conclusion is uniform, not a finite sampling claim. In particular,
row24's tail 2 still occurs in the closing equation. Once this interval
is excluded, integer t<2 with t>=0 leaves exactly {0,1}; there is no
uncovered fractional interval or out-of-budget survivor.

**Same fixed root and strict contradiction.** For either remaining t,
the complete tail list and every endpoint are exactly those of L088,
at the same literal cut. Its endpoint-uniqueness conclusion assumes
no J/H feasibility. The step-357 audit establishes uniqueness from
the positive fixed-point denominator while retaining both varying
tails and closure. Therefore the hypothetical tuple is the tuple to
which L088's bound applies; uniqueness is not inferred from a sampled
root, a minimum choice or the original d=0 witness.
At the unchanged input s_18, (2) requires
log s_18+693015 log(27/16)-3295208 log2>0.
L088 gives that identical expression strictly below
-81550766911/50000000000<0, since 81550766911>0 and
50000000000>0. These two strict inequalities are incompatible. The argument
does not require a verdict on any other guard at either root.

**Scope and preserved failures.** The complete proof has no rotation
or new cut, so no outgoing guard changes its
input. Upstream numerical bounds are imported through the already
audited statements; no discrepancy calls for rerunning their analytic
certificates. The primary citations above remain upstream inputs only,
with no new specialization of a source theorem in this audit.
C082a's d=1 all-order argument is a contrast, not an input.
Attempt 032's failed full conjunction and both d=0 rational witnesses
remain valid. No minimum/seed, integer-junction, realization or
actual-word premise has entered. Cyclic-order reduction, actual-word
transfer and universal eventual descent remain unresolved.

The argument and direct dependencies are unchanged. Accordingly
PROOF.md and DAG.md are not edited for audit status alone; this
canonical audit supersedes their pending-audit wording for C088a.

## Mathlib

Full matching Mathlib coverage has not been checked. Supporting facts
about finite sums, integer intervals, affine maps and logarithms do not
constitute a formalization of this table-specific assembly. No absence
or formal verification is claimed.
