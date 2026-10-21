# Normal closure — weighted estimate with explicit j-pole support

TARGET: Test whether every L089 survivor and ordering satisfies D(C_o)+R_S(C_o)<=D(T)+R_S(T)+log(2^11*3^3*5^2), where S={p:v_p(j(E))<0}, D is normalized absolute different degree and R_S is normalized reduced degree over S.
CHECKED: 2026-10-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step385 reused step382, audited L094-L096 and ATTEMPTS/035; exact normalized-different/reduced-support search found no matching normal-closure theorem; targeted Milne completion search located author-hosted ANTc.pdf, whose Proposition 8.2 and full proof were inspected. Queries and bounded source readings below.
SOURCE_EVIDENCE: Reused step382 and fresh IV April 2020 reproduction Proposition 1.3(i)-(ii) and proof pp.11-12, Definition 1.9 pp.21-22, Theorem 1.10 definitions/proof(ii) pp.23-24; Milne ANT v3.08 (2020-07-19), Proposition 8.2 and full proof p.136, author-hosted ANTc.pdf. Local inputs are audited L094-L096.
COMPARISON: Known tame different and completion decomposition formulas cover the required local invariant and weights; audited L094-L096 cover every prime for these fields. The target is a finite weighted specialization with explicit support, not a matching published normal-closure theorem or native selected-support identification.
GAP: Source coverage is adequate; the four support/prime cases and weighted sum still require a separate mathematical application at the exact constant. Native selected support, exact generation, complete repair and essentiality remain independent gaps.
REASON: The missing tame formula and completion-weight input have now been inspected; approve only the unchanged exact target for a later mathematical turn, preserving all source-version qualifications.
LITERATURE_REASON: The target changes from local ramification to a normalized global different-plus-reduced-support inequality; the prior remaining-prime SCOPE does not cover that assembly.

SCOPE: Only the exact TARGET with the definitions and inherited fields below is ready for mathematical application; no native support identification, stronger constant, changed field or complete repair is covered.

## Retained proposal; source-approved at step385, mathematics unexecuted

The main gap remains original finite B>=A. The intermediate target
above could decide whether normal closure retains this numerical
allowance for the full j-pole support, while leaving the native
selected-support and initial-data obligations independent.

Retain audited L090 and inherited L089: the same survivor E/Q,
c,h,d_*,e_*, both fixed domains and closure, all six literal
full-coordinate Legendre models, T=Q(E[2])=Q(t_o),
G_o=T(iota,E_o[15]), and C_o=G_o^nor over Q. Proposed mathematical
inputs are audited L094,L095,L096. L092's factor-four relative
excess remains a separate obstruction; no local core cancellation
or replacement of G_o by C_o in initial data is authorized.

For a number field L in {T,C_o}, define

    D(L)=[L:Q]^(-1) sum_(z finite) a_z f_z log(p_z),
    R_S(L)=[L:Q]^(-1) sum_(z finite, p_z in S) f_z log(p_z),
    S={rational primes p : v_p(j(E))<0}.

Here a_z is the integer exponent of the absolute local different,
f_z is the residue degree over F_(p_z), and v_p(p)=1. Thus R_S is
the degree of the reduced divisor on the complete inverse image
of S, not a pullback divisor with ramification multiplicities.
These definitions specify the proposed test; no estimate is proved
here. S is finite since the survivor's nonzero j is rational.

The source review should first compare this exact statement with
the already inspected IV Proposition 1.3(i),(ii), Definition 1.9
and Theorem 1.10(ii). Inspect only missing essential cases. Account
for both membership cases p in S and p outside S at every small
prime, and for local-degree weights over every actual base place.
Do not assert a native conductor interpretation merely from the
choice of S or transfer a selected singleton from another curve.

Continue to a separately approved mathematical application only
if those cases and normalizations have adequate source coverage.
The later mathematical continuation test is the displayed constant
with all prime contributions included; any failed inequality or
unsupported hypothesis must be isolated, not hidden in a relaxed
constant. Even success would not establish native selected support,
exact generation, complete field repair or essentiality.

April reproduction authentication/current-version, the def= reading,
height-selected prime, independent initial data, native input/action/
factorization/pilot and original finite B>=A remain unresolved.
ATTEMPTS/035 stays parked. Mathlib coverage is unchecked. No new
lemma or complete-solution candidate is supplied. Step385 supplies source approval only.


## Step385 source comparison — 2026-10-21

### Exact imports, without reproof

Freshly inspected [IV April 2020 reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf),
Proposition 1.3(i)-(ii), printed pp.11-12, including its proof:
for finite local fields K subset L with absolute v_p(p)=1,

    d_p(L) >= d_p(K) + 1/e_K - 1/e_L,

with equality for tame L/K. Part (ii) gives the upper bound
already imported in L094-L095 under its Galois/tame-intermediate
hypotheses. The proof reduces to total ramification, handles the
tame derivative case, then uses induction and a Kummer estimate.
No stronger bound is imported.

Definition 1.9(i), printed pp.21-22, uses residue-field logarithms
and total field degree. Theorem 1.10, pp.23-24, uses the reduced
selected support and the displayed pre-ell constant. Its hypotheses
are not asserted for C_o. The explicit S in TARGET is a different,
fully specified support; the inequality must be specialized separately.

Freshly inspected [Milne, Algebraic Number Theory v3.08](https://www.jmilne.org/math/CourseNotes/ANTc.pdf),
19 July 2020, Proposition 8.2 and complete proof, printed p.136:
for a finite separable extension L/K and an archimedean or discrete
nonarchimedean absolute value v,

    L tensor_K K_v = product_(w|v) L_w.

The proof uses a primitive element, factorization over K_v and
Chinese remainders, with Proposition 8.1 identifying the factors as
the actual extending completions. Characteristic-zero number fields
meet separability. This provides the degree accounting both for
C_o/T at each v and for T/Q at p, without equal-place assumptions.
The source is an author-hosted alternate file bearing the same version
and date, not an authentication of the IV reproduction.

### Normalizations and complete case coverage

Reuse step382's source-definition translation: at a finite place z
of L above p the weights are [L_z:Q_p]/[L:Q], the different order
is a_z/e_z, and the reduced-support order is 1/e_z on S and zero
off S. Relative and absolute ramification indices must remain distinct.
Proposition 8.2 supplies the weight regrouping needed over each base
place. The mathematical turn must write that regrouping explicitly.

The case inventory for the later application is exhaustive:

| Prime and support case | Available input | Remaining elementary check in the mathematical turn |
| --- | --- | --- |
| p outside {2,3,5}, p in S | L096 tameness; imported tame equality | Combine with the two reduced coefficients using the same actual tower. |
| p outside {2,3,5}, p outside S | L096 unramifiedness | Check both the different and the absent reduced terms under regrouping. |
| p in {2,3,5}, p in S | L094/L095 with allowances 10,2,1 and base inverse index | Include both reduced coefficients before bounding the remaining inverse index. |
| p in {2,3,5}, p outside S | L094/L095 with the same allowances | Bound the base inverse index; both reduced coefficients vanish. |

Only positive integral ramification indices and their tower relation
are needed in these arithmetic checks. No unproved small-prime good
reduction or tame hypothesis is needed. S is fixed over Q, hence its
complete inverse images supply consistent support at every base and
extending place. No exact global sum or new inequality is established
in this literature step. The displayed threshold remains the required
one; it is not enlarged to absorb an unchecked term.

### Search, duplication, failures and limits

Reused the step382 assessment, the conclusions and import sections of
L094-L096, histories 382/384, and ATTEMPTS/035. Their recorded work
supplies local bounds and source conventions, not a completed proof
of this exact global target. No local proof was rederived. No
cross-notebook input was used.

Fresh queries were `"normalized" "different" "reduced" "ramification"
Mochizuki "1.10"`, `site.jmilne.org/math/CourseNotes/ANT.pdf "8.2"
"sum" "degrees"`, `site.jmilne.org "PROPOSITION 8.2" "completions"`,
and `site.stacks.math.columbia.edu "sum" "completions" "degree"
"discrete valuation"`. No matching normal-closure result was identified;
this is not a novelty claim. Search hits other than the inspected
primary IV reproduction and author-hosted Milne text were not used
as mathematical evidence. ANT.pdf retrieval timed out; ANTc.pdf was
successfully read, so no essential source blocker persists for this target.
No IV authentication attempt was reopened.

Decision SPECIALIZE approves the exact saved action only. The next
turn should be RESEARCH / REPRODUCTION: import the formulas and prove
or isolate failure of the stated all-place specialization, without
reproving general ramification or completion theorems. Continue only
if every support case and weight meets the exact threshold; abandon
this estimate mechanism if an actual failed term or unsupported
hypothesis is found. A failure of an available upper bound alone is
not a counterexample. Mathlib full/supporting coverage remains
unchecked. No essential IUT flaw, complete repair or verified candidate
is claimed; original finite B>=A remains open.
