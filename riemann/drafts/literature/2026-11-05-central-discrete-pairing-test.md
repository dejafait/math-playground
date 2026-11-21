# Central (R2) regime — bounded algebraic test

TARGET: Test whether L791's three exact central quotient equations admit positive parameters for arbitrarily large degrees in the (R2) regime, with at least one paired difference in {1,...,d-1} and the other either in that set or greater than d-2, covering both pairings by one bounded algebraic argument.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step601's completed comparison in 2026-11-05-central-discrete-pairing-feasibility.md records changed-hypothesis searches, local duplicates/failures and limits; no exact central feasibility theorem located, no originality claim.
SOURCE_EVIDENCE: Martinez-Finkelshtein–Morales–Perales https://arxiv.org/pdf/2309.10970v3 (8)–(14), (30), Remark4.1/(60)–(61), Table2, Theorem3.1/proof, Proposition2.7(iii), (75), Proposition4.15(ii)/(R2), printed pp.5–6,9,11–12,15–16,22–23,33–34; Holland https://arxiv.org/html/2608.08682v1 Lemma6.2/proof and (66)–(71); exact conditions, normalization and multiplicity cases inspected in step601.
COMPARISON: Conditional matching and per-degree positive-root preservation are known; exact central compatibility with freely varying tuples in this discrete/mixed regime is the local specialization. L817 and L818 have different hypotheses.
GAP: Prove unbounded-degree feasibility or an all-tuples obstruction within precisely this regime; separation, signed residual control and actual-Xi positivity remain independent gaps.
REASON: This changed sufficient regime offers an independently testable algebraic compatibility question without repeating strict-gap or fixed-tuple stops or reproving known root results.
SCOPE: One bounded proof attempt; no degree sweep, precision ladder, complete parameter classification, new evaluator, extra matching indices or automatic signed transfer. Newly written ready continuation requires separate approval next turn; no feasibility result established in step601.

Use the completed [comparison](2026-11-05-central-discrete-pairing-feasibility.md)
for L791's exact q values and full enclosures. Retain L791 and
L018/L021/L776/L778's completion, normalization, analytic-error,
data, evaluator and software contracts. Ratios stay fixed and correlated;
tuples may depend on d. D is free; the original box is not imposed.

For either pairing (A_d,B_d),(C_d,D_d) or
(C_d,B_d),(A_d,D_d), require both differences to belong to
{1,...,d-1} union (d-2,infinity), with at least one in the integer
set. All parameters are positive; d>=2 is an integer. For k=0,1,2:

    q_k=(A_d+k)(B_d+k+1)(C_d+k)(D_d+k+1)
        /[(A_d+k+1)(B_d+k)(C_d+k+1)(D_d+k)].

Try one algebraic necessary-condition/elimination mechanism. A finite
cap or incompatibility must cover all tuples, both pairings and the
case of only one discrete gap. A construction must meet the exact
actual equations for unbounded degrees; asymptotic residuals do not
establish existence. An obstruction on the whole enclosure product
includes actual data; interval feasibility does not establish actual
existence. Do not assume integer gaps are uniformly bounded in d,
or that a varying family has a convergent parameter subsequence.

Record a proved obstruction, exact construction, or the precise
remaining condition after this one attempt. Continue only if exact
feasibility or a discriminating surviving necessary test supports it;
a uniform obstruction stops this regime alone. A finite parameter
scan or failed solver is inconclusive. Repeated roots are allowed;
no simple-root mesh or signed residual conclusion is assumed.
Preserve the earlier fixed/strict stops. No cross-notebook input.
Mathlib coverage unchecked. This is established-route development,
not a creative claim at the central signed-positivity gap.
