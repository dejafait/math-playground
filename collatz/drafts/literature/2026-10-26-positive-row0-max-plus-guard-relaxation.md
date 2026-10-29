# Support-wide cyclic guard relaxation — source comparison completed

TARGET: Assess a support-wide max-plus relaxation of all own-input J guards for the literal d35 positive-row0 allocation simplex.
CHECKED: 2026-10-26
DECISION: EXPLORE
SEARCH_EVIDENCE: Step511 ran the eight queries below and repeated the scoped terminology search in ATTEMPTS/, late-October assessments and L10*/C10*. Inspected primary finite-sum, GP and finite-affine statements; no inspected theorem decides this literal coupled simplex. Search absence establishes no novelty.
SOURCE_EVIDENCE: Read Boyd–Vandenberghe(2004), section3.1.5 p.72 and section5.8.3 pp.261–262; Blanchard–Higham–Higham(2019 author version), section4 equations(4.1)–(4.2) p.8; Boyd et al.(2007), sections2.1–2.3 pp.69–71 and9.1 pp.114–115; Halbeisen–Hungerbuehler(1997), section2 equations(2)–(4), Lemmas1/2 and printed induction pp.228–229. Reused step503 analytic/cycle comparisons; rechecked MathPrize's displayed target.
COMPARISON: Finite log-sum-exp comparison supplies a uniform log25 loss for a25-term positive numerator, not zero-loss equivalence. Standard GP uses posynomial upper inequalities; no inspected equivalent GP reformulation covers these lower guards. Finite-affine closure supplies no support-wide verdict or integer realization. Attempt033/C106a reject the old cap and fixed witness, not this coupled relaxation.
GAP: Essential method coverage is available; literal necessary reduction, coefficient enclosures, coupling all25 alternatives on one allocation and a complete feasibility/infeasibility certificate remain unproved and unimplemented.
REASON: Complete the gate-approved literature assessment and nominate a separate bounded mechanism test; no new lemma, mathematical script, relaxation derivation or feasibility verdict is produced in step511.
SCOPE: Literal chronological25 pairs with H0=5,H24=32670656; integers b_i>=0,sum b_i=9250245,b0>=1,a_i=2+18b_i,kappa=23/11. Keep original endpoints,closure,lower domains and own-input non-strict J guards. Omit H guards only as an explicit relaxation; no minimum,seed,integer/residue junction,realization or primitive-period assumption; repetitions allowed.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target introduces simultaneous maximum-term alternatives across unrestricted positive-row0 supports; fixed-cut affine/enclosure coverage did not compare this mechanism or its finite-sum loss.

## Gap, retained proposal and test

Universal descent remains the main gap. The intermediate target is a
support-wide necessary relaxation coupling all25 J guards in this literal
positive-row0 simplex. A rigorous exclusion could close this remaining
support case; arbitrary order, entry, actual-word transfer, unrestricted
cycles and divergence would still be unresolved. The original proposal
is retained: use all25 positive summands at every original cut and an
explicit finite-sum loss, rather than another fixed-support cap.

Continue if a correct necessary reduction admits a complete exclusion
certificate. A certified allocation satisfying the precise relaxation
would obstruct this relaxation alone, and should be preserved before
abandoning its exclusion claim. Inconclusive bounded search is not a
negative feasibility verdict. No mathematical test is performed here.
The separate proposed research scope is recorded in
`2026-10-26-positive-row0-max-term-feasibility-test.md`; its newly written
coverage receives separate supervisor approval on a later invocation.

## Discovery actually performed

Queries:

- `log sum exp maximum log n bound Boyd Vandenberghe convex optimization 3.1.5`
- `Collatz affine composition cycle formula Bohm Sontacchi real fixed point parity vector`
- `tropical approximation posynomial feasibility max plus log sum exp inequalities`
- `"Collatz" "max-plus" cycles guards`
- `"tropical" "posynomial" "lower" feasibility log sum exp`
- `Blanchard Higham Higham accurately computing log sum exp softmax 2019 pdf 1.3 bound`
- `site.stanford.edu boyd geometric programming posynomial inequality greater than reverse convex tutorial pdf`
- `site.stanford.edu "~boyd" "max" "log n" "log-sum-exp"`

The scoped local search for max-plus,tropical,log-sum,dominant-term,
largest-summand and disjunct terminology found the nomination only.
Read Attempt032/033/034; L055's literal table; L104's hypotheses;
L106's complete coefficient/enclosure/tuple/all-cut sections through(9);
C106a's source/qualification section; and the saved step503 assessment.
No sibling notebook or cross-notebook result was used.

## Inspected primary statements and applicability

**Finite-sum comparison.** Stephen Boyd and Lieven Vandenberghe,
*Convex Optimization*, Cambridge University Press,2004,
[section3.1.5, printed p.72](https://stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf),
states for every real vector x of positive finite dimension m:
max(x)<=log(sum exp(x))<=max(x)+log m. The upper bound is tight
when entries coincide. Section5.8.3 pp.261–262 supplies the alternative
for Ax<=b: lambda>=0,A^T lambda=0,b^T lambda<0. This certifies
a complete linear system, not an unexamined union of branches. Use only
after the literal reduction and exact coefficient control. No convex
lower-superlevel feasibility conclusion is imported.

Pierre Blanchard, Desmond J. Higham and Nicholas J. Higham,
*Accurate Computation of the Log-Sum-Exp and Softmax Functions*,
[author version dated2019-09-08, section4 equations(4.1)–(4.2), printed p.8](https://eprints.maths.manchester.ac.uk/2728/1/paper.pdf),
reads y=xmax+log(1+sum_(i!=k)exp(x_i-xmax)) and obtains
xmax<=y<=xmax+log m. Read the full displayed argument with the
selected maximum and m=1 case; ties require no uniqueness. Import this
finite real identity/bound without reproof. The repository cover labels
MIMS EPrint2019.16; the paper is also arXiv:1909.03469v1. The published
revised title is *Accurately computing ...*, IMA Journal of Numerical
Analysis41(4)(2021),2311–2330, DOI10.1093/imanum/draa038. Numbering
here pins the inspected author version. Floating-point stability
estimates are not exact-arithmetic certificates and are not used.

L106 equation(9) has25 positive numerator summands, within the theorem's
m=25 scope. Keep the fixed positive closure denominator and the log25
loss in the necessary direction. Handle s_i=n_i+23/11 exactly: applying
a25-term comparison to s_i while dropping its shift is outside coverage;
a26-term representation instead needs its26-term loss. No literal guard
alternative or numerical threshold is derived here.

**Stronger optimization claims screened.** Stephen Boyd, Seung-Jean Kim,
Lieven Vandenberghe and Arash Hassibi, *A tutorial on geometric programming*,
Optimization and Engineering8(2007),67–127, DOI10.1007/s11081-007-9001-7,
[sections2.1–2.3 pp.69–71 and9.1 pp.114–115](https://stanford.edu/~boyd/papers/pdf/gp_tutorial.pdf).
Read positive-variable monomial/posynomial definitions, standard
posynomial<=1 and monomial=1 constraints, and the signomial extension's
local approximation/trust-region discussion. It explicitly allows
nonconvergence and nonglobal solutions. The intended guards have a
lower-bound direction on positive sums. No inspected equivalent GP
reformulation covers them. Thus local optimization failure cannot certify
infeasibility. This is scope comparison, not a complexity or impossibility
claim about this instance. No algorithmic efficiency guarantee is imported.

**Finite-affine cycles.** Lorenz Halbeisen and Norbert Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*,
Acta Arithmetica78(1997),227–239, DOI10.4064/aa-78-3-227-239,
[section2, equations(2)–(4), Lemmas1/2 pp.228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Read binary-word definitions, real affine composition, numerator
recursion/concatenation and the complete printed induction: length-one,
appended-zero calculation, appended-one stated analogous. Lemma2 gives
the affine expression and fixed point with denominator2^length-3^ones;
Lemma1's cycle interpretation is in rationals with odd denominator.
Only finite-affine composition is relevant. Shifted25-block applicability
and positive denominator are local obligations, treated for the fixed
tuple in L106; no word realization follows for arbitrary allocations.
No general coding reproof is needed.

## Reused coverage and obstruction comparison

Reuse `2026-10-26-row2-guard-positive-row0-row1-full-support.md`'s
step503 primary comparison: DLMF4.6.4,4.5.8–4.5.11,4.2.19 with their
positive-real and remainder qualifications; Halbeisen–Hungerbuehler's
minimum/prefix comparisons; Simons–de Weger(2005), Lemmas4/6/7 and
their integer/minimum/global-height hypotheses. Those hypotheses do not
become available by naming25 rows or omitting H guards. Knight's
publisher preview remains an unread-theorem lead, not an input.
L104's audited enclosure requires identical K=397573379,N=630138897;
it does not bound arbitrary prefixes. L106's all-cut argument uses one
closed tuple; its extension to each allocation must be justified, rather
than treating the fixed allocation itself as a general premise.

Attempt032 rejects an old sufficient certificate; Attempt033 rejects
the endpoint-only row2 cap; C106a/Attempt034 reject one full-guard
witness. Preserve each scope. None bans guard coupling or excludes this
simplex. No certificate replay was needed for this source comparison.

Search results also surfaced informal Collatz repositories, a claimed
Lean formalization, tropical matrix/game material and tropical
approximation papers. Their theorem-level content was not inspected or
imported. A Collatz–Wielandt spectral theorem is not by name a Collatz
iteration theorem. No adequate direct verdict was found in the inspected
primary statements; no originality claim follows.

## Target version, remaining obligations and source access

Rechecked [MathPrize](https://mathprize.net/posts/collatz-conjecture/)
on2026-10-26: its page dated2021-07-07 still states eventual arrival
at1 for every positive integer under even x/2 and odd3x+1. This agrees
with GOAL.md. Reward adjudication is separate.

The continuation has25 guards against25 summands on one shared integer
allocation. Construct its alternatives only in the separate research
turn, retaining finite-sum loss, original cuts, closure and coefficient
errors. A feasible relaxed allocation would not establish original guard
or word feasibility. An exclusion needs complete coverage of alternatives
and allocations with exact checkable evidence, not a failed branch or
solver status. A bounded inconclusive search remains EXPLORATION.
Do not attempt an unbounded enumeration or substitute an isolated cap.
No uniform margin, allocation or feasibility verdict was calculated here.

No essential access blocker remains. The initial Stanford book host
request timed out; its author-hosted alternate worked. The publisher
LSE page failed; the author PDF supplied the required identity/bound.
A tutorial screenshot timed out; primary extracted text was read instead.
Mathlib full matching and supporting coverage were not checked, and are
not claimed absent. No PROOF.md,DAG.md,lemma or script changes are needed:
the mathematical argument did not change.
