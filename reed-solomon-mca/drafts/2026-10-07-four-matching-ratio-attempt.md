# Four-matching moment-ratio attempt — checkpoint before computation

Approved target: Prove or refute that every L033 union-six pencil over F_(97^20) with no weight-three parameter has at most twelve valid additional finite incidences.

Main gap: arbitrary-family sixteen-count equality; within the approved
union-six branch L039 leaves four perfect matchings with actual moment
compatibility unresolved. Intermediate target: exclude that form by the
necessary paired evaluation-ratio condition. Downstream use: such an
exclusion, together with L010/L033 and L039, would give the conditional
twelve bound. Universal extraction and challenge identification remain open.

Inputs inspected: L010's statement, moment kernel, uniqueness and
same-support proof; L032's classification and affine lift; L033's full
shortening, overlap and lower-weight proof passages; L034's paired-ratio
proof; L035's packing proof; L038's statement and exceptional reduction;
L039's whole proof; ATTEMPTS/021. This is not a separate audit of the
newer conditional inputs. Reuse the supplied unchanged EXPLORE assessment
and its inspected standard shortening/distance coverage. No L015 finite
enumeration or field-label sampling is authorized or used. The surviving
ratio mechanism is absent from the narrowly searched prior attempt notes.

Assume N_3=0 and N_ext=13 before invoking L039. Fix a selected pair
Z_i={p,q}. Put h(X)=prod_(y in J)(X-y) and
Q_K(X)=prod_(y in K)(X-y). For any outside triple K whose tag is outside
{p,q}, L033 gives c_p/c_q=g_K(p)/g_K(q). Since g_K=h/Q_K,
Q_K(p)/Q_K(q)=rho=(h(p)/h(q))/(c_p/c_q). This holds for exactly eight
actual triples; all denominators are nonzero. For K={a,w,t} in L039's
form, write b_z=(p-z)/(q-z). The necessary equation is
b_a b_w b_t=rho. The four K_0 labels are distinct and disjoint from
W,p,q. Each of their matchings has three edges. Thus at least eight
of the twelve colored matching edges must satisfy this equation.

Bounded test: exhaust all normalized pairs p=1,q in H minus {1}, all
six-sets W in H minus {p,q}, all rho in F_97^*, and all possible four
K_0 labels in the remaining eight labels. First compute the upper bound
obtained by summing the four largest edge-product multiplicities over
those eight candidate labels. Multiplication of all labels by p^(-1)
permutes H and preserves every b_z, justifying this complete normalization.
Each product class on W is a matching because z -> b_z is injective;
no matching extension, tag pairing, other selected pairs, moment parameters
or full-weight sufficiency is assumed by this relaxation.

Continue if this uniform relaxed maximum is below eight. If it reaches
eight, inspect a full extremal witness and test whether four edge-disjoint
perfect matchings can attain eight; otherwise save the exact failed
threshold. A surviving necessary condition is not an actual pencil or a
refutation of the twelve bound. No decision is presumed before the check.

## Intermediate checkpoint

The complete 45045-case relaxation has maximum eight, required eight;
24 cases reach seven and twenty reach eight. The first maximum witness
has four rows of two good edges. Each row has a unique perfect-matching
completion, and those completions repeat W edges. The first threshold
therefore fails to settle the branch, but its complete threshold list
permits one dependent check within the same ratio mechanism: exhaust all
rho/K_0 choices in all twenty cases at eight and every matching completion.
A uniform failure closes the necessary-condition test; a surviving
completion leaves other pairs, tags and actual pencil gates open.

## Completed attempt

[L040](../lemmas/L040-six-coordinate-paired-ratio-exclusion.md) records the
full reduction and complete computational proof. The relaxed maximum
eight is attained in twenty q,W cases. All seventy-two threshold choices
have profile (2,2,2,2), forcing a unique third edge in every row; every
completion repeats two edges. Thus no edge-disjoint four-matching family
can realize the eight actual overlap ratios. Candidate N_ext<=12 meets
the required bound, conditional on L033 and the essential matching chain.
The entire critical-case list and forced-edge table were inspected.

No extension-field error weights were sampled. The rationality of rho
comes from an actual witnessed triple, independently of L034's projective
descent, and normalization acts on labels/ratios only. The proof remains
an UNVERIFIED CANDIDATE pending critical audit. Universal extraction,
arbitrary-family equality, global fifteen and challenge identification
remain unresolved. Continue by separate scope approval and critical
review, abandoning the candidate if a concrete dependency, normalization,
finite-coverage or forced-edge error is found. No new ready audit scope
is approved in this mathematical turn.
