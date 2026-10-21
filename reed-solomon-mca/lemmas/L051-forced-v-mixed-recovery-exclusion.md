# L051 — The forced-V mixed profile excludes twelve with two d-tags

## Hypotheses

Use the complete gated tau=1 local pencil of L043 over
F=F_(97^20), with H the order-sixteen subgroup of F_97^*, k=8 and
1/4<=delta<5/16. In its notation,

    A_0={h,d,y_1,y_2}, A_1={h,d,z_1,z_2}, A_2={h,w_1,w_2,w_3},
    B={h,d,y_1,y_2,z_1,z_2}, O=H minus B, W={w_1,w_2,w_3}.

All nine labels are distinct, lambda!=0, the original finite gamma_i
are distinct, and p*q*(1-p-q)*r*(1-r)!=0. Weights and the original
chart are arbitrary over F. Let R count distinct original finite
nonuniversal parameters satisfying L043 (4)–(7), with witnesses other
than A_0,A_1,A_2,K_*. No recovered-weight gate is imposed on R.

Suppose two distinct members of R have witnesses {d} union S and
{d} union S', with S,S' three-subsets of O. Use the audited L048–L049
conclusions: S intersect S'={s}, s in W, and

    P=S minus {s}, P'=S' minus {s}, W_0=W minus {s}

are three pairwise disjoint two-sets. Put V=P union P',
B'={d,s} union V and T_0=H minus (B union B'). Thus |T_0|=5.

The complete exact fixed-H certificates and their reproduction checks
below are essential computational hypotheses of this informal result.
Their proof/certificate reduction received a separate critical audit
on 2026-10-10, recorded below, with no mathematical defect found and
the export-identity verification completed. Neither L044 descent, the
full L045–L046 results,
L040's unverified bound, a universal lift nor extraction is assumed.

## Conclusion

In this two-d-tag branch, |R|<=11. Consequently any violation of the
uniform eleven target must have at most one d-tagged parameter.

More specifically, once the two d-tag recoveries and a full finite V
recovery exist with full weights, there is at most one distinct scalar
admitted on the mixed supports

    {b,b',t,t'}, b in B minus {d}, b' in B' minus {d},
    {t,t'} subset T_0, |{t,t'}|=2,

even when E=0 is ignored and mixed recovered weights are allowed to
vanish. L050 would require nine such distinct parameters at twelve.
This stronger profile exclusion is specific to the fixed H and relies
on complete finite certificates; it is not an abstract incidence bound.

The fewer-than-two-d cases, uniform eleven, other triple patterns,
universal extraction and ABF26 identification remain open. The global
11/q–16/q interval is unchanged. This is a partial conditional result,
not a complete challenge candidate or certified originality.

## Proof

### Reduction to a full forced-V profile

Assume |R|>=12. L050, whose scoped audit found no defect, supplies
|R|=12, full actual errors at every finite sparse parameter, and an
eligible original finite full error on exactly V. The two selected
d-tag parameters and V are distinct. The nine remaining members have
exactly the displayed mixed supports. In particular all the full-weight
uses below follow from the high count through L010, rather than from
the relaxed definition of R. There are nine distinct mixed parameters
to exclude. No sixteen-count equality is assumed.

Normalize labels by x -> x/h. This permutes H and sends h to 1.
Moment vectors change by the invertible diagonal map with entries
h^-j for j=1,...,8. The degree-seven Q changes to h^-7 Q(hX), so
c'_x=h^-7 c_(hx); replacing lambda by h^7 lambda preserves the actual
error weights and all p,q,r gates. Original gamma_i and rho are
unchanged. Cubic evaluation ratios are unchanged by the common h^-3
factor. Thus normalization preserves every used recovery condition
without replacing the original finite chart.

### A local, justified finite weight reduction

For any set D write f_D(X)=product_(x in D)(X-x), and also write
W(X)=f_W(X). L048's audited full-moment argument gives nonzero u,u'
and distinct mu,nu in F_97 minus {0,-1} such that

    -mu f_S(y_i)=u W(y_i), f_S(z_i)=u W(z_i),
    -nu f_S'(y_i)=u' W(y_i), f_S'(z_i)=u' W(z_i),
    (q-mu p) f_S(h)=u W(h),
    (q-nu p) f_S'(h)=u' W(h).

All values being divided by are nonzero because S,S',W lie outside B.
The z equation determines u in F_97, and likewise u'. Put
a=u W(h)/f_S(h), a'=u' W(h)/f_S'(h). The two h equations force

    p=(a-a')/(nu-mu), q=a+mu p,

so p,q belong to F_97. This is the elementary local solve already
used in L044 and the earlier fixed-label calculation, not a new
global descent claim. Its determinant nu-mu is nonzero by L043's
injective scalar-to-parameter formula.

For the forced support V, use L043's full recurrence operator F_V.
Write Fh=F_V v_h, Fd=F_V v_d, FY=F_V Y, FZ=F_V Z. Its equations
are precisely

    mu_V*(FY+c_h p Fh) - beta_d Fd = FZ+c_h q Fh,       (1)
    beta_d=c_d[1-(1+mu_V)r].

The two columns in (1) are independent. Fd is nonzero because d
is absent from V. Any dependence with a nonzero coefficient of
FY+c_h p Fh would put the moments of a word on {y_1,y_2,h,d}
with nonzero y coefficients in the V-span. The union of these four
labels with V has size eight. Eight-column independence from L010
forces that word to equal a V-supported word, a contradiction at y_1.
Thus (1) has rank two. Its coefficients are in F_97, so if consistent
over F, its unique mu_V,beta_d lie in F_97, determined by two
independent rows with the other two rows still checked. Since mu_V!=-1,

    r=(1-beta_d/c_d)/(1+mu_V)

also lies in F_97. This uses V's actual full recurrence and both
missing-label equations; projected compatibility alone is insufficient.
No assumption on rho, lambda or the original gamma_i follows.

### Complete mixed-support test, retaining all eight moments

Fix b in B minus {d} and a mixed support K={b} union D, where
D={b',t,t'} is outside B. For any prospective scalar m set

    a_h(m)=q-m p, a_d(m)=1-(1+m)r,
    a_yi(m)=-m, a_zi(m)=1,
    n_m(x)=c_x a_x(m) on B, zero elsewhere.

This is the word whose moments are N_K in L043 (8). K has an
all-eight-moment relaxed recovery if and only if some u!=0 satisfies

    a_x(m) f_D(x)=u W(x) for every x in B minus {b}.    (2)

Here is the full equivalence, without assuming a weight gate. If a
K-supported word omega has the same moments as n_m, their difference
is the evaluation of a degree-at-most-seven polynomial by L010's
kernel identity. It vanishes at the seven labels O minus D. It is
nonzero because at least one surviving z-label has coefficient c_z!=0.
Therefore it equals u f_(O minus D) for some nonzero u. Evaluating
at B minus {b}, multiplying by f_D, and using
f_O=Q W and c_x=Q(x) gives (2).

Conversely, if (2) holds, subtract the evaluation word
u f_(O minus D) from n_m. It vanishes on B minus {b}, and outside
B union D both words vanish. Thus it is supported on K, and the
subtracted polynomial has degree seven and zero eight-moment syndrome.
All eight moments match. Its weights may vanish, which only enlarges
the tested family. This is the same shortening mechanism as the
audited L048 input, with the explicit changed missing tag justified
here; no unaudited full L046 result is imported.

There is at least one surviving y-label and one surviving z-label.
Choose such labels y,z. Equation (2) forces

    u=f_D(z)/W(z), m=-u W(y)/f_D(y).                   (3)

Every denominator is nonzero. Compute these two prime-field scalars,
reject m=0,-1, and check all five equations (2), not only the two
used for (3). This gives the complete eligible scalar set on that
mixed support. There are exactly 5*5*C(5,2)=250 mixed supports in
every forced-V configuration. Distinct eligible scalars, rather than
support or equation counts, are the quantity of interest.

### Complete finite evidence and independent checks

The already audited L049 certificate
`scripts/simultaneous-recovery/disjoint-d-pair-result.json` contains
all 8190 ordered choices of unordered disjoint Y,Z pairs from H minus
{1}, and partitions all 165 outside cubics for each choice by their
two evaluation ratios. For every possible d pair, W,S,S' are three
distinct cubics in one class. L049's separate complete partition and
ratio checks are reused, rather than treating a saved positive list
as exhaustive. For each class, choose every W and every unordered
pair of remaining cubics; then choose every d outside
{1} union Y union Z union W union S union S'. This enumerates all
labelings in the present branch, including unordered residual pairs.
It has 75600 W/pair presentations and 302400 distinct d configurations.

`scripts/simultaneous-recovery/forced_v_mixed.py` computes the local
p,q solve, every equation of (1), every original normalized gate,
and the actual eight-moment recoveries on V and the two selected
d supports. There are 4960 configurations with the excluded V scalar
and 7952 with r=0 or 1. There are no inconsistent V systems or
lower-weight selected/V recoveries among the remaining configurations.
Exactly 289488 full forced-V configurations remain. All 250 mixed
supports of every one are tested by (2)–(3), including rejections.
The complete certificate is
`scripts/simultaneous-recovery/forced-v-mixed-result.json`.

It reports 72372000 mixed-support tests. The histogram of distinct
eligible mixed scalars is 287788 configurations with zero and 1700
with one. The maximum is one, strictly below the required nine.
Every admitted mixed recovery is independently checked against all
eight moments inside the producer, before any full-weight filtering.

Two separate verifiers additionally check the complete evidence:

* `check_forced_v_coverage.py` independently regenerates every source
  presentation and d choice. It uses two-by-two determinant solves
  for (1) instead of producer RREF, checks rejected V/gate cases,
  and verifies equality of the complete retained configuration set.
  It recomputes the label sets, all c values and profile supports,
  checks 870164 full eight-moment weight records and 289488 original
  gated affine triples. Its complete counts and no-failure result
  are in `scripts/simultaneous-recovery/forced-v-mixed-coverage.json`.
* `verify_forced_v_mixed.cpp` checks all 72372000 mixed supports using
  the original four locator recurrence rows on n_0+m(n_1-n_0),
  independently of the producer's five-value cubic equations.
  It solves the unique scalar equation when possible, retains all
  row conditions and selected-scalar exclusions, and compares the
  entire admitted (support,scalar) set for every configuration. All
  289488 sets agree, including 1700 admitted memberships and every
  rejection. It also checks V and both selected d recoveries.
  The no-failure certificate is
  `scripts/simultaneous-recovery/forced-v-mixed-recurrence-verification.json`.

Reproduction, from this notebook:

```text
python3 scripts/simultaneous-recovery/forced_v_mixed.py
python3 scripts/simultaneous-recovery/export_forced_v_mixed.py
clang++ -O3 -std=c++17 scripts/simultaneous-recovery/verify_forced_v_mixed.cpp -o scripts/simultaneous-recovery/verify_forced_v_mixed
scripts/simultaneous-recovery/verify_forced_v_mixed scripts/simultaneous-recovery/forced-v-mixed-verifier-input.txt scripts/simultaneous-recovery/forced-v-mixed-recurrence-verification.json
python3 scripts/simultaneous-recovery/check_forced_v_coverage.py
```

The complete compact C++ input is exported from every JSON case, not
a sample. The coverage verifier checks its source JSON's retained profile
identities and sets; the separate audit's `audit_forced_v_artifacts.py`
checks every compact export row against that JSON. The producer's
`independent_completeness_check_pending`
flag records its production-time state. The two subsequent verifier
certificates above supply the completed checks; it is not silently
treated as a cleared flag. This step inspected their complete summary
and filter values and a complete one-mixed-candidate case. Those small
reads supplement the exhaustive verifiers; previews alone are not proof.

### Original chart, contradiction and source qualification

The enumeration ignores E(m)=0, so it is an upper bound for every
original chart. L043 proves that distinct eligible finite parameters
have distinct scalars m; an excluded scalar can never add a parameter.
The enumeration forces p,q,r into F_97 only in this two-d-and-V
branch, and imposes no field condition on rho. To see that no hidden
chart condition was used, choosing any rho outside F_97 makes E(m)
nonzero for every m in F_97 minus {0,-1}: an E=0 solution would force
rho=m/(1+m) in F_97. Such rho exist in F_(97^20), and L041's local
converse with the retained normalized gates gives the original triple.
This observation is a qualification of the test, not a twelve witness.

Under |R|>=12, L050 requires nine distinct mixed original finite
parameters. The exhaustive upper bound permits at most one distinct
mixed scalar. This contradiction proves |R|<=11 in the stated branch.
It does not impose a mixed-support restriction on low-count pencils
where L050 has not forced that profile.

Known recurrence coverage is reused precisely from L043: Przemek
Chojecki, *Shortening Bounds for Reed–Solomon MCA*, live author TeX
v9.2 dated July 17, 2026, source lines 2785–2935, DR2
`drc:lem-locator-recurrence` and DR6–DRC `drc:thm-exact-compiler`,
[author source](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex).
The specialization is eight shifted moments, four distinct support
labels, four recurrence rows and nonzero column multipliers x in H,
including extension-field moment vectors. The imported equivalence
justifies (1) and the independent recurrence checker; it is not reproved.
The source is mutable and not certified identical to ePrint 2026/1463.
The supplied simultaneous-count assessment found no matching import
for this numerical branch bound. POTENTIALLY_NEW reports that search
scope only. The local weight solve and shortening test are acknowledged
reproductions; the new evidence is their complete simultaneous profile
count. The separate audit below validates this existing scoped result and
its implementation; no full challenge resolution is asserted.

### Separate critical proof and certificate audit (2026-10-10)

The audit found no mathematical defect in the conditional eleven bound.
It completed one missing verification link: the original text attributed
compact-export identity to the coverage checker, which never opens the
export. The supplementary checker below now verifies every exported row,
without changing the enumeration, old certificates or theorem. This is
local verification progress and a repair of the evidence chain, not a new
numerical bound or a claim beyond the inspected literature. The approved
recurrence/MDS/shortening coverage was reused; no unread source or full
L044–L046 result enters the audit. Direct mathematical inputs and DAG
edges are unchanged.

Under |R|>=12, audited L050 applies to the relaxed definition of R
verbatim. Its L010 weighted bound supplies full actual errors before any
full-weight gate is used here. The two d supports and V are distinct
actual finite recoveries, and the remaining nine parameters have the
mixed form. This does not impose that profile on low-count pencils.

Multiplication by h^-1 bijects H and multiplies shifted moment j by
h^-j, an invertible diagonal change. The complement defining Q has seven
roots, so its normalized monic polynomial is h^-7 Q(hX). Consequently
c'_(x/h)=h^-7 c_x and lambda'=h^7 lambda preserve actual error values
and normalized triple weights. The gamma_i, rho and excluded original
direction are untouched. Sorting within Y or Z changes no support or
equation; swapping their roles is not presumed a symmetry.

L048's audited full-moment equations give the two h equations before
requiring full recovered weights. Their z evaluations put u,u' in
F_97^*, since all cubic roots avoid B. The h denominators are nonzero
for the same reason. Distinct finite parameters give mu!=nu by L043.
Subtracting q-mu p=a and q-nu p=a' yields (nu-mu)p=a-a', so p,q are
rational before their use in (1). Their three nonzero gates remain.

The sign in (1) follows by applying the full recurrence to
Z-mu_V Y+c_h(q-mu_V p)v_h+beta_d v_d. Its two columns are
FY+c_h p Fh and -Fd, with Fd!=0 because d is outside V. Dependence
would put Y+c_h p v_h minus a multiple of v_d in the V-span, by the
recurrence theorem. The union of these supports has at most eight labels
and the y coefficients are nonzero, contradicting L010's eight-column
independence. Thus rank is two over F_97 and every extension. Any
consistent F-valued solution is the unique rational solution given by
a nonzero minor, with the other rows still imposing consistency.
Nonzero c_d and 1+mu_V justify the r formula. The deletions mu_V=0,-1
and r=0,1 are required by the original gates. No rationality of lambda,
rho or gamma_i follows or is assumed.

For each mixed support K={b} union D, D has three distinct labels
outside B, so O minus D has seven labels. A surviving z-label has a
nonzero n_m coefficient and lies outside K, making n_m-omega nonzero.
L010's kernel identity and these seven roots force its polynomial to be
a nonzero scalar times f_(O minus D). At B minus {b}, multiplication
by f_D and f_O=QW give all five equations (2), dividing only by nonzero
Q values. Conversely subtracting that degree-seven evaluation word
kills every coordinate outside K and all eight moments. This proves
both directions without a recovered-weight gate. A surviving y and z
give (3), with all denominators and u nonzero; every other equation is
still checked. Thus this test forces m rational even if it initially
ranges over F. The 250 supports are distinct: their intersections with
the two disjoint tag sets and T_0 recover their unique indices.

The L049 source partition is byte-identical by SHA-256 to the artifact
validated in its separate audit. That audit established all 8190 ordered
Y,Z choices, all 165 cubics per choice and every ratio group. An actual
pair gives three distinct cubics W,S,S': equality with W forces mu=-1;
S=S' forces mu=nu by z then y evaluations. The singleton equations put
them in one group. Enumerating every W and unordered remaining pair
therefore loses none. The d loop removes exactly already-used labels.
The independent coverage replay checks every presentation, including
rejected V/gate cases, with a determinant solve instead of producer RREF.
Its explicit missing-case branch recovers V and both selected errors
and would fail on an omitted full eligible case. Duplicate-key counters
are zero in these complete data, so deduplication hides no presentation.

The producer tests all five cubic equations. The C++ verifier instead
constructs the affine word n_m, evaluates all four original locator rows,
and solves their scalar equation. A zero direction with nonzero constant
is rejected; both zero would abort as an unexpected universal case and
did not occur. A nonzero direction fixes m and every row is checked.
Only m=0,-1 are deleted; E is ignored. All modular products and sums fit
the C++ integer type. Comparing the entire (support-mask,scalar) set for
each case checks every negative membership as well as all 1700 positives.

The original coverage verifier and a freshly compiled C++ verifier were
replayed. Python assertions were enabled (optimization level zero).
The coverage output is byte-identical to its saved version; the separately
named recurrence replay equals the complete saved result. The producer
was inspected, not rerun: independent complete coverage, moment and
recurrence replays verify its saved output. No positive sample or
unchecked regeneration substitutes for this verification.

The new `scripts/simultaneous-recovery/audit_forced_v_artifacts.py`
checks all 289488 compact rows exactly against the complete JSON,
including header, ordered profile data, selected scalars, every mixed
membership and end of file. It independently aggregates the histogram,
checks mixed-record uniqueness, stored N_moments, selected-scalar
disjointness, subgroup metadata, filter totals and all verifier summary
fields. Its SHA-256 manifest preserves all original sources and artifacts
used, and matches the source partition to L049's audited hash. This
completes the export check previously misattributed to the coverage
verifier, which validates JSON identities rather than compact text.

Reproduce these added checks from this notebook after the original
coverage checker command listed above:

```text
clang++ -O3 -std=c++17 scripts/simultaneous-recovery/verify_forced_v_mixed.cpp -o scripts/simultaneous-recovery/verify_forced_v_mixed_audit
scripts/simultaneous-recovery/verify_forced_v_mixed_audit scripts/simultaneous-recovery/forced-v-mixed-verifier-input.txt scripts/simultaneous-recovery/forced-v-mixed-audit-recurrence.json
python3 scripts/simultaneous-recovery/audit_forced_v_artifacts.py
```

The saved pre-replay manifest is
`scripts/simultaneous-recovery/forced-v-audit-before.json`; preserve it
rather than recreate it during reproduction. The complete added audit
record is `scripts/simultaneous-recovery/forced-v-critical-audit.json`.
Together the replays cover 302400 configurations, 289488 retained
profiles, 870164 eight-moment weight records and 72372000 mixed-support
tests. The rejected categories are exactly 4960 excluded V scalars and
7952 failed r gates. The complete histogram remains 287788 zero-scalar
profiles and 1700 one-scalar profiles. All checks passed: actual maximum
one is below nine required. The production-time pending flag remains
historical data; the separate replay and identity artifacts establish
completion. No preview is used in place of complete evidence.

Finally T=gamma_0+g*rho/[rho+(rho-1)m] is injective on eligible m:
g*rho and rho-1 are nonzero and the denominator has not vanished.
Ignoring E=0 only enlarges the tested scalar set. Nine required distinct
finite parameters would therefore give nine distinct tested scalars,
contradicting the verified maximum one. No extension scalar, original
infinity point or zero mixed weight is silently discarded. This validates
|R|<=11 with the stipulated two d-tags on this fixed H and field.
Zero/one-d profiles and the global interval remain unresolved. This
scoped audit is neither a full challenge review nor a Lean verification.

## Mathlib

The full fixed-H forced-V profile count and two-d-tag eleven bound:
**not checked** for matching Mathlib coverage. Supporting moment-kernel
and Vandermonde independence are used through L010; the recurrence
theorem is used through L043. Factor and root bounds have the supporting
Mathlib names already inspected in L048–L049, including
`Polynomial.dvd_iff_isRoot` in
[Div.lean](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Polynomial/Div.lean)
and `Polynomial.card_le_degree_of_subset_roots` in
[Roots.lean](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Polynomial/Roots.lean).
These are mutable-master supporting references, not a matching full
theorem or Lean verification. No new lookup or absence claim is made.
