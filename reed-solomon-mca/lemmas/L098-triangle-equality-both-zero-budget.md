# L098 — Equality-only two/one both-zero scalar budget

## Hypotheses

Use L059's hypotheses and notation: F=F_(97^20), F_0=F_97, H the
fixed order-sixteen subgroup of F_0^*, C=RS[F,H,8], unit multipliers,
and the pinned same-support event at 1/4<=delta<5/16. The nine labels in

    A_0={a,b,y_1,y_2}, A_1={a,c,z_1,z_2}, A_2={b,c,w_1,w_2}

are distinct. Put P={a,b,c}, U=A_0 union A_1 union A_2 and
V=H minus U, so |V|=7. Write

    Y_2=(X-y_1)(X-y_2), Z_2=(X-z_1)(X-z_2),
    W_2=(X-w_1)(X-w_2).

Fix gated normalized weights w=(p,q,r) in (F_0 minus {0,1})^3.
Let M(w) be L059's scalar union, with all projected and restored
equations imposed and mu!=0,-1, before imposing the original-chart
gate E=rho-(1-rho)mu!=0. Retain zero recovered weights at this stage.
Assume exactly |M(w)|=13.

Define M_00(w) as the subset of M(w) witnessed by at least one
both-zero nonbase four-subset K, in the sense of L065/L057. This is a
union of scalar values, not a count of witnesses. Use L086's audited
equality-linearity conclusion with its essential finite-computation
qualifications through L069 and L056/L051/L055.

## Conclusion

Every both-zero witness for a scalar of M_00(w) is contained in V, and

    |M_00(w)|<=2.

If Y_2,Z_2,W_2 are linearly dependent as quadratic polynomials, then

    |M_00(w)|<=1.

For these fixed labels and weights the same bounds hold for distinct
additional both-zero parameters in every allowed original finite chart,
including charts deleting one scalar of M(w). No original chart is
asserted rational. A general |D(w)|>=7 fiber without |M(w)|=13 does
not meet these hypotheses.

This conditional restriction does not exclude thirteen scalars, bound
the isolated recoveries, prove the uniform triangle twelve bound or
improve the global 11/q–16/q interval. No complete challenge candidate
is asserted. The separate critical audit of 2026-10-16 found no defect
in this conditional statement, with the computational qualifications retained.

## Proof

### Realize all scalars before using linearity

Apply L059's existing construction with gamma=(0,1,rho), lambda=1
and rho in F minus F_0. Such rho exists since [F:F_0]=20. Its
local-converse application gives actual words with the three stated
full base errors, nonzero determinant polynomial and every coordinate
locator nonzero as a polynomial. Since all eligible mu are rational,
E=0 would imply rho=mu/(1+mu) in F_0, which is impossible. Thus every
element of M(w) is realized as a distinct actual additional finite bad
parameter, with all eight moments and same-support failure, exactly as
proved in L059. Together with the three bases there are sixteen distinct
bad parameters. L059's application of L010 bounds the full set by sixteen
and supplies equality fullness and uniqueness of the actual errors and
their four-supports.

In particular a both-zero four-subset witnessing an admitted scalar
is the actual error support at its parameter: L059/L057 supply an error
supported on that four-set, and equality fullness says it has weight
four. Hence none of its four coordinates can have a zero recovered
coefficient. Uniqueness also precludes distinct four-set witnesses for
the same scalar. We do not discard relaxed witnesses before obtaining
this conclusion from equality.

The constructed pencil now meets every L086 hypothesis: the same
F,H,code,cell, polynomial nonvanishing and exactly sixteen actual finite
bad parameters. L086 therefore makes every pair of its distinct actual
four-supports intersect in at most one label, including pairs consisting
of a base support and an additional support. Its audited computational
inputs remain part of this application; no new certificate replay is
claimed.

### No both-zero support contains a singleton label

Let K be any both-zero witness admitted at these weights. By L065 it
misses P and contains each of the singleton pairs

    {y_1,y_2}, {z_1,z_2}, {w_1,w_2}

either in its entirety or not at all. If it contains the Y pair, then
|K intersection A_0|>=2. Its scalar is additional, so K and A_0 are
distinct actual equality supports. This contradicts L086. The Z and W
pairs give the identical contradiction with A_1 and A_2, respectively.
Thus K contains no singleton label and misses P as well, so K is a
four-subset of V. This rules out the one-pair categories rather than
counting their projected candidates as simultaneous recoveries.

### Independent pair quadratics

If Y_2,Z_2,W_2 are independent, L065's independent-branch conclusion
allows at most two both-zero candidate four-subsets entirely in V.
Every actual both-zero support has just been placed in this class.
L065's restored-pivot conclusion gives at most one eligible scalar per
both-zero support at fixed gated weights. Therefore |M_00(w)|<=2.
We use the proved candidate-support bound only as an upper bound; net
membership alone is not sufficient for an actual recovery.

### Dependent pair quadratics

In this branch L065 supplies all two-element fibers B_1,...,B_m of

    h in V -> [Y_2(h):Z_2(h)],

where these sets are pairwise disjoint and m<=3. Its complete
classification says that each both-zero four-subset entirely in V is
exactly B_i union B_j for some i<j. If two distinct such supports
existed among actual equality errors, their two index sets would be
distinct two-subsets of an m-set with m<=3. They must have a common
index, so the supports would share the corresponding entire fiber of
size two, contradicting L086. This also covers m<2 (no candidate) and
m=2 (only one candidate). Hence at most one actual both-zero support
is possible. The same restored-pivot uniqueness gives |M_00(w)|<=1.
No fiber or quadratic degree-drop branch is omitted: those cases were
retained in L065's complete dependent-branch classification.

### Transfer to any original chart and scope of the specialization

Keep the labels and w fixed and now allow arbitrary admissible distinct
finite gamma_i, nonzero lambda and rho not in {0,1}. Any additional
both-zero recovery in that chart satisfies the same projected and
restored tests defining M_00(w). L059 proves its scalar is rational,
including both-zero lifts, and retains precisely the additional gate
E!=0. Conversely each scalar of M_00(w) passing that gate gives a
both-zero recovery in the prescribed chart by the same exact recovery
formula. The scalar-to-parameter map is injective, so the set of these
parameters is in bijection with

    M_00(w) minus {rho/(1-rho)}.

Taking a subset cannot increase either bound. We applied equality
linearity in the chart realizing all M(w), not in a prescribed chart
that might contain only twelve additional parameters. Original gamma_i,
rho and lambda are never rationalized. All finite gates, both-zero
pivots and scalar deduplication are retained.

The pre-existing EXPLORE assessment
`drafts/literature/2026-10-16-triangle-equality-both-zero-budget.md`
approves exactly this two/one test; the source search did not establish
a matching result. POTENTIALLY_NEW classifies this local combination
only, and does not certify originality. The additional argument is the
exclusion of complete singleton pairs against the actual base supports,
followed by the dependent-fiber intersection test. L066's bound of
three and L064's fixed-support-pair bound are comparisons, not inputs.
No stopped cross-difference or fixed-label sweep is reopened.

The standard RS/GRS ingredients remain imported in these inputs from
J. I. Hall, *Notes on Coding Theory*, GRS chapter, Theorem 5.1.1 and
proof, printed pp. 63–64
([author chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf)),
and I. Marquez-Corbella and R. Pellikaan, *A characterization of MDS
codes that have an error correcting pair*, FFAA 40 (2016), 224–245,
section 5, Lemma 5.3 and the following unnumbered shortening formula,
printed pp. 7–8 of the
[2016-02-29 accepted manuscript](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf).
The retained distinct sixteen labels, nonzero unit multipliers and
dimension eight satisfy Hall's field-independent hypotheses; L041's
existing seven-deletion specialization satisfies 16-7>=8 and has nonzero
difference multipliers. L057's recurrence input retains Chojecki,
*Shortening Bounds for Reed–Solomon MCA*, author TeX v9.2, July 17,
2026, DR2 and DR6–DRC, source lines 2785–2935
([author source](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex));
its weighted Vandermonde hypotheses specialize to R=8,t=4 with
nonzero multiplier x on H. That mutable source is not certified
identical to ePrint 2026/1463. The saved assessment and canonical inputs
provide the inspected theorem/proof coverage. None of these general
theorems is reproved here; the support-intersection specialization is
written in full because none of the inspected sources supplies this
conditional two/one count.

### Separate critical audit — 2026-10-16

The pre-invocation EXPLORE assessment
`drafts/literature/2026-10-16-equality-both-zero-budget-critical-audit.md`
approved exactly this audit. The complete proof was checked against
L059's scalar definition, chart construction and canonical audit;
L065's complete classification, both branches and pivot audit; and
L086's hypotheses, conclusion and completed equality-linearity audit.
The relevant L010, L041 and L057 statements and realization/recovery
proof passages were checked directly. No defect, missing case or
required theorem repair was found. The following details record the
load-bearing checks, rather than infer correctness from the earlier
source-scope approval.

**Equality and actual supports.** The extension has degree twenty, so
rho outside F_97 exists in the prescribed field and is different from
zero and one. With gamma=(0,1,rho), lambda=1 and the retained gates,
L041's local converse applies without assuming equality. The three
base supports have empty common intersection. Its pointwise locator
identity therefore certifies every locator nonzero at a base event
omitting that label, and D is nonzero at each full base event. These
are precisely L010's polynomial hypotheses, before using its bound.
The definition of M retains all restored equations; L057 supplies all
eight moments and same-support failure, even with relaxed coefficients.
For every mu in M, mu!=-1 and E=0 would force
rho=mu/(1+mu) in F_97, a contradiction. The map
T=gamma_0+g*rho/E is injective and avoids the three bases. Thus there
are at least sixteen bad parameters, and L010 gives exactly sixteen.
Its weighted bound forces full weight at all of them. Distance-nine
uniqueness identifies every witnessing four-set with the actual support;
the equality conclusion also gives distinct supports at distinct
parameters. No padded or duplicate witness remains when L086 is used.

L086 concerns every pair in this same full bad set, including the
bases. Its F,H,code,cell, nonpersistence and exact-count hypotheses
have now all been verified. No rational original chart or conclusion
about general seven-scalar D fibers is needed or inferred.

**Complete-pair exclusion.** L065 makes a both-zero K disjoint from P
and puts each singleton pair either wholly inside or wholly outside K.
A scalar in M is additional, so its actual support is distinct from
each base support. Containing Y, Z or W would give an intersection of
at least two with A_0, A_1 or A_2 respectively, contrary to L086.
Consequently every admitted K lies in V. This uses equality fullness
before the intersection argument and needs no assumption that a
projected net member passes the restored equations.

**Both quadratic branches.** Independence of Y_2,Z_2,W_2 makes L065's
seven projective evaluation points distinct: coordinatewise inversion
and the invertible quadratic coefficient matrix recover [1:h:h^2].
Different candidate quartics determine different lines. Their four-sets
in a seven-set intersect exactly once, so their three-element complements
are pairwise disjoint; three candidates would require nine labels.
This verifies the imported at-most-two support bound without assuming
generic positions or actual recovery of every candidate.

In the dependent case, disjoint singleton pairs give
W_2=alpha Y_2+beta Z_2 with alpha,beta nonzero. L065's invertible
coefficient change identifies the net with binary quadratics in Y_2,Z_2.
A nonzero binary quadratic has at most two projective zero values;
each fiber on V has at most two labels. A degree-drop fiber polynomial
has at most one root, and a repeated binary root supplies at most one
fiber, so neither can supply a distinct four-set. Hence every candidate
in V is exactly two distinct two-label fibers. There are at most three
such fibers because they partition subsets of a seven-set. Two different
candidate supports would share a whole fiber, violating L086 if both
were actual. With fewer than two fibers there is no candidate; with
two there is only one. This checks the small-fiber, degree-drop,
infinity and multiplicity cases of the imported classification.

**Scalars, pivots and arbitrary charts.** For a fixed both-zero K,
L057's restored equations are A_x+mu B_x=0 for x in P. Their coefficients
are rational at the stated rational weights. If all B_x vanish, the
system is inconsistent: vanishing of all A_x as well would put the
full base error on a four-set disjoint from P, contradicting sparse-error
uniqueness. Otherwise one nonzero B_x fixes mu=-A_x/B_x, with every
other equation and mu!=0,-1 still imposed. Thus each support supplies
at most one eligible scalar, including before any E gate. The support
bounds really imply the scalar bounds two and one.

For any prescribed admissible chart, the same label, weight and restored
tests define M_00. Only E!=0 remains. Since g*rho and 1-rho are nonzero,
equality of two recovered T values implies equality of their E values
and then of their scalars. The excluded scalar is rho/(1-rho), and
the inverse formula retains exactly the other eligible scalars. This
proves the asserted bijection with M_00 minus that singleton. In
particular a chart deleting a scalar need not have sixteen events;
linearity was applied only in the realizing chart. The proof never
rationalizes gamma_i, rho or lambda.

**Computational and source qualifications.** L086 imports L069's
universal five-set configuration bound, not merely its triangle
application. Its completed audit covers the 273-orbit census with
maximum six. L056 supplies the full original bad-set bound fifteen,
using its audited L051/L055 simultaneous counts and retaining all
lower-weight, universal and finite cases. These established computations
remain essential to L098. The census count paths share a
compiler and residue field; none of this is formal verification. Their
canonical audited scopes suffice here, no discrepancy required another
replay, and no fresh replay is claimed. The precise primary citations
and specializations above are unchanged and reused from ready coverage;
no new source search, general theorem reproof or novelty certification
was performed.

No formula, hypothesis, conclusion or mathematical dependency changed.
This canonical verdict
supersedes the unchanged overview's pending-L098-audit wording; the
argument itself does not require a PROOF.md update. The audit validates
the local two/one restriction, not an isolated-row bound, a thirteen-scalar
exclusion, or progress beyond the checked literature. Few/no-both-zero
fibers and the independent challenge qualifications remain open.

## Mathlib

Full matching conditional count: **not checked**. Supporting polynomial,
finite-set, interpolation, moment-independence and GRS results: **not
checked anew**; the canonical inputs retain their existing qualifications.
No Mathlib absence or formal-verification claim is made.
