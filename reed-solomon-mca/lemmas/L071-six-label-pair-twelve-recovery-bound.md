# L071 — A six-label pair bounds triangle recoveries by twelve

## Hypotheses

Let F=F_(97^20), H the order-sixteen subgroup of F_97^*, and
C=RS[F,H,8]. Work in the pinned cell 1/4<=delta<5/16 with L057's
gated tau-zero triangle and actual shifted-moment pencil
s(T)=sigma(a_*)+T sigma(b_*), where
sigma_j(z)=sum_(x in H) z(x)x^j for 1<=j<=8.
The original three finite base parameters gamma_0,gamma_1,gamma_2 are
distinct. The nine triangle labels are distinct, lambda!=0, and the
normalized weights satisfy p(1-p)q(1-q)r(1-r)!=0. All weights and
parameters may lie in F; the original finite chart is unrestricted.

Let B be the actual finite bad-parameter set for these input words and
the pinned same-support event. Let R_add be the image set of all admitted
L057 relaxed additional recoveries, counted by distinct original finite
parameters. Retain both-zero projected cases, the restored equations,
all finite gates and vanishing recovered fourth weights. Multiple
support witnesses for one parameter count only once.

Suppose two distinct parameters eta_1,eta_2 in R_add have actual
full-weight four-errors e_1,e_2 with supports K_1,K_2 and
|K_1 union K_2|=6. No third additional error, equality count, ratio
rationality or useful-pair extraction is assumed.

## Conclusion

The full bad set satisfies |B|<=15, and |R_add|<=12.
This is a conditional specialization of audited L070 and L040, closing
the six-label-pair branch of the triangle twelve problem. It proves no
universal pair existence, uniform triangle bound, arbitrary-family
extraction or challenge resolution. The global interval 11/q–16/q is
unchanged. The separate scoped critical audit of 2026-10-12 found no
defect in this application; its checks and limits are recorded below.

## Proof

### Reused coverage and original recovery set

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-11-six-label-pair-clustered-bound-application.md`,
saved before this application. Its completed-input scope covers L070's
separate October 11 audit and L040's separate October 7 audit, including
the essential chain and complete finite certificates. Reuse those
conclusions; no new enumeration or reproof of the clustered estimate is
needed. L033 is used only for its explicit-triple hypotheses and accounting.

L057, through L041's local converse without any equality assumption,
supplies independent coefficient syndromes, nonzero polynomial Hankel
determinant D, every nonzero coordinate-locator polynomial and three
distinct full base errors at gamma_0,gamma_1,gamma_2. These are the
nonpersistence hypotheses for the imported bounds, rather than
pointwise nonvanishing at every parameter. L057's full-moment converse
and same-support conclusion give

    R_add subset B minus {gamma_0,gamma_1,gamma_2}.

This inclusion holds before any full-weight gate on other recoveries:
a vanishing fourth coefficient still gives an actual bad parameter.
Both-zero projected rows are admitted only after all restored and finite
gates, so they also belong to this same set. We bound its image in the
original finite chart, rather than the number of support witnesses.

### Exhaustive ratio split

Put V=K_1 union K_2 and R=K_1 intersect K_2, so |R|=2. Full weights
make r_x=e_2(x)/e_1(x) in F^* well defined for each x in R.
The pair satisfies all of L070's hypotheses by the preceding paragraph.

If the two ratios differ, or either equals one, L070's complementary
branch already gives |B|<=15. It applies to the full bad set, keeping
the other recoveries relaxed; no equality/fullness assumption is added.

Otherwise both equal a common r_pair in F minus {0,1}. Import L070's
unconditional construction in this branch. It supplies the original
finite parameter

    eta_3=(eta_2-r_pair eta_1)/(1-r_pair),

distinct from eta_1,eta_2, and an actual full error on
(K_1 minus K_2) union (K_2 minus K_1). Its explicit lift f has
sigma(f(T))=s(T) and, for the disjoint pairs

    Z_1=K_2 minus K_1, Z_2=K_1 minus K_2, Z_3=R,

the coordinates f_x(T)=d_x(T-eta_i) for x in Z_i, with d_x!=0,
and zero coordinates off V. The values f(eta_i) are the three actual
full errors. All three parameters are in the original finite chart.
L070's audited applicability check also supplies independence of the
coefficient vectors of f, from the unchanged independent syndromes.

These are exactly L033's alternative explicit-triple hypotheses with
U=V, selected parameters eta_i and coefficients c_x=d_x. That
alternative requires neither an equality assumption nor a fresh use of
L032 to construct the third error. The fixed field, subgroup, code,
cell, shifted moments and polynomial nonpersistence assumptions agree.

Apply L040's audited full-B conclusion to this L033 pencil. More
explicitly, relative to the selected triple eta_1,eta_2,eta_3, L033's
accounting is |B|=3+N_ext+N_3. If N_3=0, L040 gives N_ext<=12 and
therefore |B|<=15. If N_3>0, L040's separately stated lower-weight
branch gives |B|<=15 directly. No matching-certificate equality argument
is applied to the latter branch, and no lower-weight parameter is
discarded. This proves |B|<=15 in every ratio case.

### Subtract the original triangle bases

Return to gamma_0,gamma_1,gamma_2. They are three distinct members of B,
and the earlier inclusion gives

    |R_add| <= |B minus {gamma_0,gamma_1,gamma_2}| = |B|-3 <= 12.

The extracted eta_3 may equal one of these original bases. L040's
selected-triple N_ext need not equal |R_add|; only its full-B bound
is transferred. The two selected eta_1,eta_2 are additional by hypothesis,
but no additional status is imposed on eta_3. All counts remain counts
of distinct original finite parameters. Neither a rational original
chart nor a third additional event is used.

### Citations and qualifications

This is a REPRODUCTION application within the ready SPECIALIZE scope,
not a new bound beyond the sources compared. The new content is the
local assembly and the change of reference triple in the subtraction.
L070 and L040 carry the precise standard distance citation: J. I. Hall,
*Notes on Coding Theory*, GRS chapter, Theorem 5.1.1, printed pp. 63–64,
[author-hosted chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf).
Its field, distinct labels, nonzero unit multipliers and 0<8<=16
hypotheses give distance nine here over F.

L033/L040 carry the shortening input: I. Marquez-Corbella and
R. Pellikaan, *A characterization of MDS codes that have an error
correcting pair*, FFAA 40 (2016), 224–245,
[DOI 10.1016/j.ffa.2016.04.004](https://doi.org/10.1016/j.ffa.2016.04.004),
accepted manuscript February 29, 2016, section 5, Definitions 5.1–5.2,
Lemma 5.3 and following GRS formula, printed pp. 7–8
([primary manuscript](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf)).
Their audited six/seven and essential five-deletion applications retain
positive dimensions, distinct labels and nonzero multipliers. No new
shortening specialization, source claim or reproof is required here.

The existing failure evidence in ATTEMPTS/007,025,026 remains intact:
this application uses neither a five-coordinate generation search,
formal common-root sampling nor the false two-antipodal isolated bound
three. It is not a finite search for arbitrary pairs and supplies no
universal existence theorem. No cross-notebook result is used.

### Separate critical audit, 2026-10-12

Step 170 checked this assembly under the previously saved EXPLORE scope
in `drafts/literature/2026-10-11-six-label-pair-twelve-application-audit.md`.
No mathematical defect or missing application hypothesis was found.
This is a REPRODUCTION audit of the existing conditional result, not a
new bound, a repaired proof or a claim of progress beyond checked sources.
The completed L070 and L040 audits, including L040's essential forward
chain and complete certificates, are imported within their recorded
scope. No discrepancy required replaying those certificates.

First, L057 explicitly takes L041's local converse, which does not
assume equality. Its nine labels are distinct, all three base errors
are full by the stated gates, and their supports have empty common
intersection. The converse gives independent coefficient syndromes.
At each base parameter, the pointwise Hankel formula gives nonzero D;
for each label some base error omits it, giving a nonzero evaluation
of that coordinate's locator. These are precisely polynomial
nonvanishing, not pointwise nonvanishing everywhere. Thus the L070
and L033/L040 nonpersistence premises hold for the original input
words, without assuming that the other recoveries are full.

For the recovery-set inclusion, L057 first establishes all eight moments
and same-support failure on H minus K; this remains true when recovered
weights vanish. Its both-zero cases require the pivot, all restored
equations and the same finite gates. With t=(T-gamma_0)/g=rho/E,
rho!=0,1, mu!=0,-1 and E=rho-(1-rho)mu!=0, t cannot be zero;
t=1 would force mu=0, and t=rho would force mu=-1. Consequently every
admitted parameter avoids all three original bases. These observations
verify the inclusion used in the proof for the image set of all
recoveries; no witness-to-parameter injectivity is presumed for lower
weights. L041 separately puts each original base parameter in B.

The two intersection weights are nonzero, so their ratios lie in F^*.
Unequal ratios or a unit ratio exhaust the complement of the
common-nonunit case. The audited complementary conclusion of L070
already concerns this same full B. In its common-nonunit construction,
eta_3-eta_1=(eta_2-eta_1)/(1-r_pair) and
eta_3-eta_2=r_pair(eta_2-eta_1)/(1-r_pair) are nonzero. Hence all
three selected parameters are distinct and finite in the original chart.
The partition Z_1,Z_2,Z_3 consists of three disjoint two-sets, its
coordinate slopes are nonzero, and sigma(f(T)) is the unchanged pencil.
All three values f(eta_i) are actual full errors, including eta_3 by
L070's unconditional converse. A relation between the coefficient
vectors of f would induce the same relation between the independent
coefficient syndromes, so those vectors are independent as required
for L033's projective chart. These checks match L033's explicit-triple
alternative; its equality-conditioned construction from L032 is not
being applied to an arbitrary triple.

The field, subgroup, dimension, shifted moments and pinned radius cell
in L040 coincide exactly. Its N_ext is relative to the selected eta
triple. L033 excludes weights at most two and accounts for every
remaining parameter by 3+N_ext+N_3, with distinct valid incidences
and weight-three parameters counted separately. When N_3=0 the audited
L040 bound gives 3+12=15. When N_3>0 the imported multiplicity bound
gives |B|<=16-3N_3<=13, which in particular implies the stated fifteen.
Thus use of L040's combined conclusion neither assumes away lower
weights nor applies its equality/matching argument to them. The sharper
thirteen here is already in L033, not a new result of this audit.

Finally B and the original gamma triple have not changed. The latter
has exactly three distinct members of B, so its complement has size
|B|-3 irrespective of whether eta_3 is one of them. Combining this
identity with the verified recovery-set inclusion gives twelve.
No equality between N_ext and |R_add| is needed or asserted. All
counts are finite-parameter counts in the original chart; no rational
chart, third additional event or universal useful pair has entered.

The Hall and Marquez-Corbella–Pellikaan citations and their already
inspected hypotheses remain as above. This application changes neither
their specialization nor the finite-certificate scope. The direct
mathematical inputs remain L033, L040, L057 and L070; the older inputs
enter through their existing proofs. No mathematical script, new
enumeration or DAG change was required. The conditional threshold
twelve is verified locally; uniform triangle twelve, useful-pair
extraction and the challenge-definition gaps remain unresolved.

## Mathlib

The full six-label-pair bound and this assembly are **not checked** in
Mathlib. Supporting shifted-moment kernels, code distance, affine lifts,
finite-set accounting and the two imported conditional bounds are also
not checked for Mathlib coverage here. No absence or formal verification
claim is made. Existing audited informal inputs are reused; the separate
scoped informal audit above found no defect and supplies no Lean verification.
