# L091 — Remaining cyclic gates and a single-label reconstruction limit

## Hypotheses

Use exactly L089's F=F_(97^20), order-sixteen subgroup H of
F_97^*, bijection h:Z/16Z -> H, unshifted moment columns, blocks,
circuit coefficients d_(t,i), reconstructed coefficients w_(s,i), and
full alternating kernel K. All indices are modulo sixteen. For a fixed
t abbreviate the following distinct labels:

    u=h(t-2), a=h(t-1), b=h(t), x=h(t+1), q=h(t+2),
    c=h(t+4), y=h(t+5), d=h(t+6), z=h(t+7),
    e=h(t+8), f=h(t+9), k=h(t+10).

Only the labels occurring in a particular equation below are needed
for that equation. No actual errors, weights, finite parameters or
original chart are assumed.

## Conclusion

L089's first shared-coordinate gate is equivalent to

    (c-a)(x-z)(x-e)(d-u)/((c-e)(x-u)(x-a)(d-z))
      +(x-b)(y-f)/((x-f)(y-b))=1.                       (F_t)

Its second gate is equivalent to

    (q-e)(z-a)/((q-a)(z-e))
      +(q-b)(q-x)(d-k)(e-f)/((q-f)(q-k)(d-x)(e-b))=1. (S_t)

Thus K!=0 implies these equations and L090's third-gate determinants
D_t. Given all other labels of F_t, any one label except x is uniquely
determined in P^1(F_97). Given all other labels of S_t, any label except
q,e is uniquely determined in P^1(F_97). A value at infinity, outside H,
or already used cannot extend to a bijective labeling. D_t similarly
determines any one of its six labels from the other five, by L090.
These are necessary deductions, not sufficient conditions for K!=0.

Consider only the following abstract-index propagation procedure:
start with seven known indices, and repeatedly apply one of these
single-unknown rules to mark a new index as known. Even granting all
the rules without any field-membership or consistency rejection, no
seven-index seed set generates all sixteen indices. The maximum closure
size is nine, from a complete test of all binomial(16,7)=11,440 seed sets.
This conclusion has explicit finite-computation dependence.

This is a limitation of this particular propagation procedure, not a
lower bound on the number of labels that can determine a solution by
simultaneous equations. It does not exclude seven-seed reconstruction
with branching, or imply any labeling exists. Neither rank R=2 nor its
uniform exclusion is established; rank R>=3 is still the desired
threshold. The global 11/q–16/q interval is unchanged.

## Proof

### Exact window reductions

The direct inputs are L089's coefficient definitions and gates and
L090's third-gate deduction. The ready EXPLORE assessment
`drafts/literature/2026-10-14-cyclic-family-alternating-kernel.md`
covers the unchanged full-kernel target. No new external theorem is
imported. The following calculation specializes the existing circuit
formulas to the two gates that the previous pass left unused.

For any index i in both relevant windows, write l=h(i). Cancellation
in the products defining d gives

    d_(t-1,i)/d_(t,i)=(l-e)/(l-a),
    d_(t-2,i)/d_(t,i)=(l-z)(l-e)/((l-u)(l-a)),
    d_(t+1,i)/d_(t,i)=(l-b)/(l-f),
    d_(t+2,i)/d_(t,i)=(l-b)(l-x)/((l-f)(l-k)).        (1)

Every application below uses indices in both stated windows. Distinct
indices in these windows have distinct labels, including at wraparound.
Consequently every d coefficient and displayed difference divided by
is nonzero.

Use L089's triangle scalars, denoted alpha,beta,gamma here:

    alpha=d_(t,t),
    beta=d_(t,t+5)/w_(t+1,t+5),
    gamma=d_(t,t+3)/w_(t+2,t+3).

Divide the first gate alpha w_(t,t+1)+beta=d_(t,t+1)
by its nonzero right side. The coefficient definitions give its two
terms as

    [d_(t,t+4)/d_(t,t+1)]
    [d_(t-1,t+6)/d_(t-1,t+4)]
    [d_(t-2,t+1)/d_(t-2,t+6)],

    [d_(t,t+5)/d_(t,t+1)]
    [d_(t+1,t+1)/d_(t+1,t+5)].

Substitute (1) and cancel the d_(t,i) factors. The first expression
becomes

    [(d-e)(c-a)/((d-a)(c-e))]
    [(x-z)(x-e)(d-u)(d-a)/((x-u)(x-a)(d-z)(d-e))],

which is F_t's first term. The second becomes
(x-b)(y-f)/((x-f)(y-b)). This proves F_t's equivalence.

For the second gate beta w_(t+1,t+2)+gamma=d_(t,t+2),
cancel w_(t+1,t+5) before simplifying. Its first normalized term is

    [d_(t,t+7)/d_(t,t+2)]
    [d_(t-1,t+2)/d_(t-1,t+7)]
      =(q-e)(z-a)/((q-a)(z-e)).

The final ratio in w_(t+2,t+3) cancels d_(t,t+3), giving

    gamma/d_(t,t+2)
      =[d_(t,t+8)/d_(t,t+2)]
       [d_(t+2,t+2)/d_(t+2,t+6)]
       [d_(t+1,t+6)/d_(t+1,t+8)]
      =[(q-b)(q-x)(d-f)(d-k)/((q-f)(q-k)(d-b)(d-x))]
       [(d-b)(e-f)/((d-f)(e-b))].

Cancellation yields S_t's second term. All steps are reversible under
the distinct-label hypotheses; no coefficient-zero branch is removed.

### Unique single-unknown deductions

Each allowed unknown occurs in only one summand and in just one of
the following fractional linear factors, with other factors known and
nonzero:

| Gate | Unknown | Factor |
|---|---|---|
| F_t | u | (d-u)/(x-u) |
| F_t | a | (c-a)/(x-a) |
| F_t | b | (x-b)/(y-b) |
| F_t | c | (c-a)/(c-e) |
| F_t | y | (y-f)/(y-b) |
| F_t | d | (d-u)/(d-z) |
| F_t | z | (x-z)/(d-z) |
| F_t | e | (x-e)/(c-e) |
| F_t | f | (y-f)/(x-f) |
| S_t | a | (z-a)/(q-a) |
| S_t | b | (q-b)/(e-b) |
| S_t | x | (q-x)/(d-x) |
| S_t | d | (d-k)/(d-x) |
| S_t | z | (z-a)/(z-e) |
| S_t | f | (e-f)/(q-f) |
| S_t | k | (d-k)/(q-k) |

In each row the numerator root differs from the denominator root by
bijectivity. Its two-by-two matrix is therefore invertible, so the
factor is a bijection of P^1(F_97). The equation specifies a unique
projective value of the factor and hence of the unknown. A recovered
value outside the admitted finite, distinct H-labels invalidates the
partial assignment. Such rejections cannot enlarge its continuation.
No single-unknown rule is asserted here for F_t's x or S_t's q,e.

For the third gates, the load-bearing part of L090 was checked in this
pass. Its consecutive-window cancellations reduce the normalized third
gate to

    (d-e)(c-a)/((d-a)(c-e))
      +(d-b)(e-f)/((d-f)(e-b))=1.

Subtracting the first term and clearing only nonzero differences gives
P(d)Q(e)-P(e)Q(d)=0 for P=(X-a)(X-b), Q=(X-c)(X-f).
Expansion gives (d-e) times the determinant with rows
(ab,a+b,1), (cf,c+f,1), (de,d+e,1), exactly L090's D_t.
For any one unknown, the other four labels in the two fully known
pairs determine their unique involution. Its coefficients (A,B,C)
have AC-B^2 nonzero: otherwise both disjoint pairs would contain
the same root of Ax+B, or A=B=C=0. The remaining known label
has exactly one projective image. This verifies the deduction used
here, without claiming a separate critical audit of all of L090.

### Complete abstract-index obstruction certificate

The whole index sets and allowed new indices are the following offsets
from t, reduced modulo sixteen:

    D: whole {-1,0,4,6,8,9}; allowed all six;
    S: whole {-1,0,1,2,6,7,8,9,10};
       allowed {-1,0,1,6,7,9,10};
    F: whole {-2,-1,0,1,4,5,6,7,8,9};
       allowed {-2,-1,0,4,5,6,7,8,9}.

A rule can add an allowed index precisely when every other index in
its whole set is known. Starting with a fixed seed set, repeatedly
adjoining such indices terminates, since there are only sixteen indices.
The terminal set is independent of application order: it is closed under
every rule, contains the seeds, and is contained in every closed set
containing the seeds, by induction on the additions. It is thus the
least closed set containing the seeds. This justifies using two different
update orders for complete replay.

Reproduction commands, relative to this notebook:

    python3 scripts/cyclic-shared-gates/seed_reconstruction.py
    python3 scripts/cyclic-shared-gates/verify_seed_reconstruction.py

The producer examines every seven-subset in lexicographic order and
saves its entire terminal closure in
`scripts/cyclic-shared-gates/seed-reconstruction-result.json`.
It reports actual maximum nine, required sixteen, no witness, all
11,440 seed sets examined, zero field assignments and zero rank tests.
Although it can stop at a successful witness, no success occurs; the
verifier requires exactly binomial(16,7) rows in the complete order.

The independently written verifier uses whole-set bit masks and adds
all currently deducible indices simultaneously, rather than the
producer's sequential individual-rule updates. It reconstructs every
closure from the seven seeds, compares every index in every saved row,
checks complete seed coverage, and verifies the claimed maximum. The
full replay passed, with zero failures. Its audit and certificate hash
are in `scripts/cyclic-shared-gates/seed-reconstruction-audit.json`.
Both programs use the same explicitly stated gate templates and Python
runtime; they are independent update implementations, not independent
formal proofs or kernel computations.

One attaining case, inspected in full, has seeds {0,1,2,3,5,7,9} and
terminal closure {0,1,2,3,5,7,9,10,14}. The extra labels follow from
D_1 and D_10. This example alone proves no upper bound; the upper bound
uses every row and its complete replay. Omitting consistency checks
only grants more deductions, so their absence does not weaken this
negative conclusion about the specified index procedure. There is no
claim of an optimal reconstruction algorithm or a count of possible
H-labelings.

The negative finding stops only the attempt to reduce eight seeds to
seven by these one-unknown rules. It leaves simultaneous equations,
branching, unused gates and the full rank test unresolved. It does not
change the actual-error argument or constitute progress beyond the
inspected sources in any certified originality sense. This local result
and its computational input passed the separate step-242 critical audit
recorded below.

### Separate critical audit — October 15, 2026, step 242

The pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-15-cyclic-remaining-gates-critical-audit.md`
licenses exactly this audit. Full L091, L089's coefficient definitions
and shared gates with its step-226 audit, audited L090's determinant
and involution input, and both complete closure programs were checked.
No mathematical defect was found. This is verification of the saved
specialization and finite certificate, not a new gate, a stronger
propagation theorem or a uniform rank exclusion.

**Hypotheses and circuit normalization.** Keep exactly F_(97^20), the
fixed order-sixteen H, arbitrary bijective h, and the unshifted columns.
All deductions take place in F_97 because their known labels and
coefficients lie there. K!=0 is used only to assert L089's three gates;
the algebraic equivalences themselves hold for every bijection. No
actual error, original chart, rank-27 existence or later lemma is used.
L089's audited nonzero d and w coefficients justify division by the
three right-side circuit coefficients and the singleton normalizers.

For i in the overlaps, put l=h(i). The nine-index window T_(t-1)
removes e from T_t and adds a; T_(t-2) removes z,e and adds u,a.
Similarly T_(t+1) removes b and adds f, and T_(t+2) removes b,x and
adds f,k. Taking reciprocals of their product definitions gives all
four ratios in (1), with exactly the stated orientation. All indices
in the union of these windows have offsets -2 through 10, which are
thirteen distinct residues modulo sixteen; wraparound loses no
nonvanishing condition. The labels x,d used for the two-step backward
ratio, c,d and q,z for the one-step backward ratio, x,y and d,e for
the forward ratio, and q,d for the two-step forward ratio are in their
respective overlaps. Thus no ratio is evaluated outside its definition.

**First gate.** Expanding w_(t,t+1) along its three defining factors
and cancelling alpha=d_(t,t) gives the first displayed three-ratio
product. Expanding w_(t+1,t+5) gives exactly the second product.
The first reduces to

    [(d-e)(c-a)/((d-a)(c-e))]
    [(x-z)(x-e)(d-u)(d-a)/((x-u)(x-a)(d-z)(d-e))],

and the second to (x-b)(y-f)/((x-f)(y-b)). The cancelled d-a and d-e
are nonzero. The surviving denominator factors are c-e, x-u, x-a,
d-z, x-f, y-b. Each is a difference of two distinct indexed labels.
Hence both normalized summands, their sum and the equivalence to F_t
are valid, including a vanishing sum after subtraction; no sum is
inverted.

**Second gate.** Dividing w_(t+1,t+2) by w_(t+1,t+5) first leaves

    [d_(t,t+7)/d_(t,t+5)]
    [d_(t-1,t+2)/d_(t-1,t+7)].

Multiplication by beta's numerator and division by d_(t,t+2) yield
the first normalized term (q-e)(z-a)/((q-a)(z-e)). In the other term,
w_(t+2,t+3)'s final factor is d_(t,t+3)/d_(t,t+8); cancelling its
nonzero numerator against gamma leaves exactly L091's three-ratio
expression for gamma/d_(t,t+2). Substituting the forward ratios gives

    [(q-b)(q-x)(d-f)(d-k)/((q-f)(q-k)(d-b)(d-x))]
    [(d-b)(e-f)/((d-f)(e-b))].

Both cancelled factors d-b,d-f are nonzero. The surviving denominator
factors for S_t are q-a, z-e, q-f, q-k, d-x, e-b, all nonzero.
The cancelled coefficient at t+3 is also nonzero, despite its label
not appearing in the final equation. No zero-coefficient branch or
original finite parameter has been suppressed.

**Every permitted rule.** For each of the nine F rows and seven S
rows in the table, the unknown appears in exactly that single factor
and nowhere in the other summand or remaining multiplier. The latter
multiplier is a product of known nonzero label differences. For F the
unordered numerator/denominator root pairs, in table order, are

    {d,x}, {c,x}, {x,y}, {a,e}, {f,b},
    {u,z}, {x,d}, {x,c}, {y,x};

for S they are

    {z,q}, {q,e}, {q,d}, {k,x}, {a,e}, {e,q}, {d,q}.

All pairs consist of distinct known labels. Each factor therefore has
nonzero determinant as a fractional-linear transformation, irrespective
of its signs. Solving for its value requires only division by the
known nonzero multiplier; the value may be zero. Inverting the
projective transformation gives exactly one point of P^1(F_97).
Infinity, a repeated label or a value outside H is a rejection, not
another branch. A recovered pole cannot satisfy the original finite
equation. No inference for F's x or S's q,e has been added. Audited
L090 supplies D's unique image from five distinct known labels,
including its affine-involution and finite-pole cases. Its determinant
pairs have offsets {-1,0}, {4,9}, {6,8}, exactly the stated D template.

Reading the F and S equations gives precisely their whole sets; deleting
x (offset 1) for F, and q,e (offsets 2,8) for S, gives precisely their
allowed sets. This checks the equation-to-rule bridge at all sixteen
translations without treating any translation as a symmetry of h.

**Known closure result and its local implementation.** The standard
background is William F. Dowling and Jean H. Gallier, *Linear-Time
Algorithms for Testing the Satisfiability of Propositional Horn
Formulae*, Journal of Logic Programming (1984), 267–284, Definition 1,
Algorithm 1, Theorems 2–3 and the least-assignment corollary,
pp. 269–273, DOI 10.1016/0743-1066(84)90014-1
([author-hosted primary text](https://www.seas.upenn.edu/~cis5110/Dowling-Gallier-Horn-sat.pdf)).
The ready assessment records inspection of the relevant proof cases.
Here each known index is a proposition, each seed is a unit fact, and
each permitted deduction is a definite Horn clause with the other
whole-set indices as antecedents. There are no negative clauses.
Thus the standard least-closure conclusion applies. L091's short
induction is retained as a direct check of these programs' finite
update semantics, not a claim to reprove new general closure machinery:
each addition lies in every closed superset of the seeds, and a
terminating pass with no addition is closed. This proves that the
sequential and simultaneous implementations must agree when correct.
The source does not give these cyclic templates or the number nine.

**Complete certificate audit.** The producer's definitions enumerate
16*(6+7+9)=352 target/prerequisite rules, with all offsets taken modulo
sixteen. Its sets have no repeated offsets. It visits every seven-subset
in lexicographic order unless it attains sixteen, records the full
terminal set, and terminates each closure after at most nine additions.
The verifier independently presents the same templates as 48 whole/
allowed mask pairs. For each pair, `whole & ~current` gives precisely
the missing indices; the nonzero power-of-two test detects one missing
index, and intersection with the allowed mask enforces the exclusions.
All additions in a pass are simultaneous. Closure stops only when none
is available. The finite whole masks make Python's unbounded complement
harmless. Both templates were compared against the equations above.

Executed both reproduction commands without changing either program.
The verifier checks exactly binomial(16,7)=11,440 rows, the full ordered
seed list in each row, and every index of each recomputed terminal
closure. Thus there are no omitted, repeated, sampled or merely
positive cases. It also checks the maximum, required sixteen, null
witness, and zero field/rank-test counters. The replay passed all
11,440 rows with zero failures and maximum nine. The fully inspected
attaining case is exactly the seven seeds and nine-element closure
printed above: D_1 has only index 10 missing, then D_10 only index 14.
The upper bound uses the complete replay, not this example.

Before/after SHA-256 comparisons found both programs, the full result
and its replay report byte-identical. The report's embedded certificate
hash equals the complete regenerated result hash. Full comparison
values are saved in
`scripts/cyclic-shared-gates/seed-reconstruction-critical-audit.json`;
pre-replay hashes are in
`drafts/2026-10-15-cyclic-remaining-gates-audit-before.json`.
The shared Python runtime and explicitly identical templates remain a
qualification on implementation independence; this is no formal proof
or H-label enumeration. Omitting field consistency can only enlarge
what this specified procedure marks known. Maximum nine therefore
certifies its failure to reach sixteen, with no statement about other
rules, simultaneous nonlinear equations or possible labelings.

The audit validates the saved local input and stop evidence. It does
not alter the mathematical argument or its direct inputs L089/L090;
PROOF.md and DAG.md require no argument update. Uniform rank R>=3,
rank-27 existence, arbitrary-family coverage, the triangle bound and
challenge qualifications remain open. No progress beyond the checked
classical sources is asserted.

## Mathlib

Matching coverage for these cyclic gate formulas and the exact
propagation obstruction has not been checked. No absence or formal
verification claim is made. The mathematical inputs are the existing
moment and involution calculations; the new finite certificate is an
explicitly qualified computational check.
