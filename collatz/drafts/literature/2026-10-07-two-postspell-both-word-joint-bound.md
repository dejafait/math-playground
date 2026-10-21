# Both-word joint parameter restriction — completed scope review

TARGET: Establish explicit absolute A,B such that every actual closed two-postspell word satisfies max(4J_1+H_1,4J_2+H_2)<=A log(N)+B, retaining independent tails and repeated periods.
CHECKED: 2026-10-07
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Nine focused cycle-height, odd-run and exact-postspell queries completed; L031/L037 full proofs, L020 prefix formulas, L035 cycle application, L036 height/source ranges, prior joint/balance/reciprocal assessments, history 069/081 and Attempt 019 compared; queries and inspection limits below.
SOURCE_EVIDENCE: Hercher, JIS 26 (2023), Article 23.3.5, Lemma 20 and full proof p. 12, Theorem 21 statement and all proof cases pp. 13–14 inspected; Sodelin Postspell_Guarded_Root_Descent.md sections 1 and 3–4 inspected on live main; Simons–de Weger section 1.2 p. 52, Lemma 6 p. 58 and Lemma 12/Corollary 13 p. 61 compared, with prior complete proof coverage reused for Lemmas 7/8/12 and Hercher Theorem 16.
COMPARISON: Successive-local-minimum estimates retain intervening minima and do not directly state this both-word restriction; the inspected finite-word envelope precedes any final-halving size guard, so existing identities cover a quantitative junction transfer with arbitrary exact tails. The remaining combination and explicit constants are unproved specializations; no matching full theorem or novelty is established.
GAP: Use L037's selected-boundary size and parameter estimates with the cited actual-prefix formulas to bound the other junction, then use its own L031 valuations and intermediate height to seek the joint restriction with explicit absolute constants.
REASON: Essential transfer hypotheses and stronger-result comparison now have adequate coverage for one later REPRODUCTION proof attempt at the unchanged target; no new bound is derived or approved as true here.
SCOPE: Exactly L037's actual positive integer closure of W_1W_2, J_i>=2,H_i>=3, independent a_i>=0 congruent to 2 modulo 18, positive odd residue-20 n,x,n>1 and exact tails; N is the represented step count, and x=n and nonminimal periods remain allowed. Only the stated both-word joint restriction is approved for investigation, not bounds on tails, N or closure exclusion.
LITERATURE_REASON: Control of the other word is outside the previously approved selected-boundary target; the actual-prefix part of the source proof and the applicability of successor-minimum estimates required a separate comparison.

The main gap remains universal eventual descent. The intermediate target
addresses other-word asymmetry left by L037. Its plausible downstream use
is controlling the represented odd count in later integer-closure analysis.
Neither that use nor a bound on total N or the tails is established here.

Essential local inputs are L031, L035, L036 and L037. The candidate mechanism
is to follow the word starting at the selected smaller junction to its
actual other endpoint, retaining all affine offsets and its independent
final tail, then apply that endpoint's own height/valuation identities.
If the selected index is 2, propagation runs from x through W_2 to n;
if x=n, the tie is still admitted. This is a proposed test only.

## Primary transfer input and scope

Sodelin, node AC-POSTSPELL-GUARDED-ROOT-DESCENT-001,
[Postspell_Guarded_Root_Descent.md, section 1, "Exact orbit and margin proof"](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Postspell_Guarded_Root_Descent.md),
live main read 2026-10-07, states for an actual prefix from r>3:

\[
y=(27/16)^J(r+23/11)-23/11,\qquad
z=(3/2)^H(y+1)-1,
\]
\[
z<(3/2)^H(27/16)^J(r+3).
\]

These are inspected source statements, already represented in L020/L031,
not inequalities newly derived in this review. In the primary proof the
displayed upper envelope occurs before division by 2^e and before use of
e>=J+H. Thus the finite-prefix envelope does not need that size guard;
the later descent theorem does. Actual final E^a steps still require their
parities, which our scope expressly assumes. Their endpoint is z/2^a,
as already established in L031. No contraction or bound on a is imported.
The selected boundary is at least 47 by L037, so r>3 matches the source.

Section 3's exact terminal valuation uses the actual O^H E transition;
L031's complete general-tail proof gives the needed identities for either
word. Its independent a_i, rather than L024's E^2-only transport, is the
canonical input. Section 4 explicitly retains failed-halving examples:
the source's descent claim cannot be applied by dropping e>=J+H. Those
examples concern finite excursions, not the asserted closed-word bound.
No immutable source revision or successful Lean build is claimed.

L037's canonical proof provides a bound on the smaller designated boundary
and a joint restriction at that same index. L031 provides the other
boundary's valuation and actual intermediate height as well. Coverage
therefore reaches all inputs needed for the proposed transfer; it does not
complete that transfer or calculate its constants. The later proof must
justify each quantitative comparison instead of assuming two comparable
junctions. Reproducing general parity coding or transcendence theory is
unnecessary; the quantitative two-boundary combination is the remaining
specialization needed for this exact target.

## Stronger-result comparison and imported cycle inputs

Christian Hercher, [*There are no Collatz m-Cycles with m <= 91*](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf),
JIS 26 (2023), Article 23.3.5, Lemma 20 and full proof, printed p. 12,
give n_{i+1}<n_i^delta for successive local minima of a nontrivial cycle,
delta=log(3)/log(2). The proof uses an exact maximal odd run, its following
even run, a positive integer multiplier and n_i>X_0>3. Theorem 21,
pp. 13–14, states a refined cycle-ratio bound involving the full minimum
count m, a chosen positive m_2<=m and its stated K/X_0 threshold. Its full
proof, including m_2=m-1 and m_2=m, was inspected. The run comparison in
that proof retains delta^ell when passing ell successive minima.
These theorems are comparators only. The two designated junctions have
intervening minima; neither theorem treats them as consecutive or states
the exact both-word logarithmic bound. No new minimum-count calculation
is made here. Reuse L034 and history 069's established count mismatch.

John Simons and Benne de Weger, [*Theoretical and computational bounds for
m-cycles of the 3n+1-problem*](https://www.impan.pl/shop/en/publication/transaction/download/product/82263),
Acta Arithmetica 117 (2005), 51–70, section 1.2 p. 52 permits nonminimal
return periods. Lemma 6 p. 58 is a successive-minimum chaining estimate;
the previously inspected Lemmas 7/14 retain m-dependent constants.
Lemma 12 p. 61 supplies the precise lower linear-form input already used
in L036/L037. Corollary 13 bounds the global minimum with a factor m,
not either designated junction. Those statement passages were compared;
reuse the complete proof coverage in the balance/joint assessments for
Lemma 12's Lemma 8 and Rhin inputs. Do not identify a junction with the
global minimum or put m=2. No new transcendence-source search is needed.

Hercher's Theorem 16, pp. 10–11, remains the precisely cited cycle-ratio
input to L035. Reuse the reciprocal assessment and canonical application,
including its represented-occurrence and primitive-period justification.
The local K,N, actual nontrivial cycle and repeated periods are unchanged.
Rhin's original proof and source computations remain imported rather than
independently certified. No extra conditional excursion/delay conjecture
or computational verification threshold is added to the proposed target.

## Search, duplicates and evidence limits

Queries: `Collatz cycle "maximum" "minimum" "log" run lengths`;
`Collatz cycles "postspell" "parameters"`;
`Collatz cycle logarithmic odd run length boundary height Simons de Weger`;
`"Collatz" "postspell" "closed" "bound"`;
`"Collatz" "maximum" "minimum" "Simons" "Lemma 7"`;
`"Collatz" "odd run" "logarithmic" cycle bound`;
`"Collatz" "postspell" "joint"`;
`"Collatz" "two" "OOEO" cycle logarithmic`;
`"Collatz cycles" "run length" "upper bound"`.
No inspected theorem states the exact target. This bounded search does not
establish novelty or the absence of a stronger theorem. Hits for recent
94/95-minimum claims, binary-structure and other cycle preprints, rational
cycle bounds, forums and repository indexes are discovery leads only;
their theorem proofs were not inspected or imported. The parked blocked
source route was not reopened. Only the named primary passages above and
ready local assessments establish coverage.

L037 is a narrower result, not a duplicate of this maximum-over-both-words
target. Attempt 019 remains evidence that boundary guards alone do not
exclude integer closure. The present proposed test asks for a quantitative
consequence with an independent lower linear-form input. History 069's
count-only failure is preserved. No cross-notebook input was read.

The [MathPrize page](https://mathprize.net/posts/collatz-conjecture/), dated
2021-07-07, was rechecked on 2026-10-07: every positive integer is asserted
to reach 1 under x/2 for even x and 3x+1 for odd x. This agrees with the
canonical foundation's exact target; the shortcut convention and its
equivalence remain unchanged. Prize rules are separate.

Mathlib: matching both-word restriction, imported effective cycle bounds
and supporting arithmetic declarations are **not checked**. No full match
or absence from Mathlib is asserted.

## Approved later test and stopping condition

Approve exactly TARGET for one later mathematical attempt, classified
REPRODUCTION if successful. Seek explicit absolute A,B valid at both
indices by the selected-word transfer and the endpoint's own identities.
Continue only if the proof retains both offsets, arbitrary independent
exact tails, both index orders, repetitions and x=n. Abandon if it requires
unsupported height/parameter comparisons or proves only the already known
selected-index bound. Do not assume the new conclusion to make the transfer.

Positive integer closure exclusion, total length, independent tails,
universal entry, other cycles, divergent orbits and eventual descent
remain unresolved. This LITERATURE / NOVELTY_UNCHECKED step is EXPLORATION:
it supplies completed scope evidence and an actionable test, not a new
mathematical input or discovery beyond the inspected sources. It spends
no mathematical exploration turn and claims no counter reset. No bound,
constants, lemma or mathematical script was derived or changed. The saved
target is unchanged and now has its separate literature approval.
