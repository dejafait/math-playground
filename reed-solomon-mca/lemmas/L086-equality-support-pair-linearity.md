# L086 — Every sixteen-count equality support family is linear

## Hypotheses

Let F=F_(97^20), let H be the order-sixteen subgroup of F_97^*, and
let C=RS[F,H,8] with unit evaluation multipliers. Fix a,b in F^H
and the pinned same-support event at 1/4<=delta<5/16. Write
B(a,b) for its original finite bad-parameter set and
sigma_j(z)=sum_(x in H) z_x x^j for 1<=j<=8. Put
s(T)=sigma(a)+T sigma(b).

Assume L010's Hankel determinant D(T) and every coordinate locator
ell_x(T) are nonzero polynomials, and |B(a,b)|=16. All weights and
parameters may lie anywhere in F; the original affine chart is arbitrary.
Use the audited L069 universal configuration bound M(A)<=6 for every
five-subset A of this H, and L056's audited full-bad-set bound in the
complete gated L043 setup. Their finite-computation qualifications remain
essential, including L056's L051/L055 counting inputs.

## Conclusion

For every two distinct original bad parameters gamma,eta, their actual
error supports A_gamma,A_eta satisfy
\[
                    |A_\gamma\cap A_\eta|\le1.
\]
Thus the sixteen distinct full four-supports form a linear four-uniform
family, with degree four at every label. This is a necessary equality
restriction, not an equality construction, uniform triangle count or
improved global error bound. The interval 11/q–16/q and independent
challenge-definition qualifications remain unchanged. The separate
critical audit of 2026-10-14 found no defect in this assembly, with the
computational qualifications retained. No complete challenge candidate
or originality is claimed.

## Proof

### Preserve an arbitrary nonlinear pair

L010 gives a unique full-weight four-error e_gamma at each gamma in B,
sixteen distinct supports, and degree exactly four at every label of H.
Their moments equal s(gamma). In particular distinct supports correspond
to distinct original finite parameters, and no weights are assigned
independently of these actual errors.

Fix any two distinct supports A,B and suppose r=|A intersection B|>=2.
Since the supports are distinct four-sets, r is either two or three.
Choose x in A intersection B. Exactly four equality supports contain x,
so choose a third support C distinct from A,B and containing x. Select
its actual error and parameter. Then, for U=A union B union C,
\[
 5\le |U|\le |A\cup B|+|C\setminus\{x\}|
             =(8-r)+3=11-r\le9.                       \tag{1}
\]
The lower bound uses distinct four-sets. Crucially the chosen pair is
retained, and A intersection B intersection C contains x. Every chosen
parameter remains finite in the original pencil. This selection uses
degree four, not L085's existential triangle conclusion or L084.

### Exclude unions at most eight

If |U|<=8, apply L032's necessary direction to these very three errors.
Its field, code, shifted moments, radius, polynomial premises, equality,
full weights and distinct finite parameters all hold. Its complete
classification gives only union five or union six; seven and eight
are impossible. The union-six row has empty triple intersection, so
it contradicts the common label x. Consequently |U|=5.

In that row L032 supplies an affine vector f(T)=u+Tv supported on U
with sigma(f(T))=s(T) identically. Comparing coefficients puts both
sigma(a) and sigma(b) in the moment image of the five-set U. The
remaining L015 hypotheses are exactly the retained F,H and polynomial
nonvanishing hypotheses. Thus L015 and only L069's universal
configuration assertion give
\[
                 16=|B(a,b)|\le5+M(U)\le11,             \tag{2}
\]
a contradiction. No triangle premise, additional-recovery set or
three-base subtraction from L069 is used. Its complete five-set census
and separate audit supply the imported bound six, without a fresh replay.

This excludes every selected triple of union at most eight. In particular
r=3 is impossible, since (1) then gives |U|<=8. We are left with r=2
and |U|=9, still with a nonempty triple intersection.

### Union nine is the gated common-coordinate row

L041's necessary direction applies to these actual errors: every
hypothesis is inherited, and now |U|=9. Its complete table has three
tau=0 rows and one tau=1 row. The common label x rules out all three
tau=0 rows, including the triangle row. The only possibility is
tau=1 and (n_01,n_02,n_12)=(1,0,0), up to renaming indices.
After this renaming the supports are exactly
\[
 A_0=\{h,d,y_1,y_2\},\quad A_1=\{h,d,z_1,z_2\},\quad
 A_2=\{h,w_1,w_2,w_3\},                               \tag{3}
\]
with nine distinct labels in H. Their triple label is h=x. The unique
pair of intersection size two is the original chosen pair. We need
neither the other nontriangle row bounds nor a union-six incidence bound.

To check the local-converse gates explicitly, retain the actual errors
e_i and their original finite parameters gamma_i in this ordering. Put
\[
 \alpha_0=\gamma_1-\gamma_2,\quad
 \alpha_1=\gamma_2-\gamma_0,\quad
 \alpha_2=\gamma_0-\gamma_1,\qquad
 c_z=\prod_{t\in H\setminus U}(z-t)\quad(z\in U).
\]
Extend c by zero outside U. L041 gives a nonzero lambda with
sum_i alpha_i e_i=lambda c.
All alpha_i and c_z are nonzero. Its normalized actual weights
b_(i,z)=alpha_i e_i(z)/(lambda c_z) are one at singletons,
p,q,1-p-q at h, and t,1-t at d. Full weights give exactly
\[
                    pq(1-p-q)t(1-t)\ne0.                \tag{4}
\]
Here t is L042/L043/L056's normalized double-label weight r; it is
unrelated to the earlier integer intersection size.

These formulas use the reordered actual errors without scaling them.
Equivalently, under any permutation pi of a previous ordering, the
newly defined alpha'_i=sgn(pi)alpha_(pi(i)): check a cyclic permutation
and a transposition, which generate S_3. The coefficient becomes
lambda'=sgn(pi)lambda, so normalized weights simply reindex. Neither
the words a,b, their errors, their parameter values nor their chart
changes. This is the same weight-transfer check audited in L085.

All three original identities sigma(e_i)=s(gamma_i) still hold. In
particular the first two anchor L041's local converse to this s(T):
an affine vector polynomial through two distinct finite parameter values
is unique. The original a,b themselves satisfy these anchors. Thus
(3), (4), lambda!=0, all singleton formulas and original moments
verify the complete local setup of L042/L043. L042's audited
nonpersistence conclusion applies, consistently with the existing
polynomial premises; it adds no chart or rationality restriction.

We may therefore use L056's full finite bad-set conclusion for this
same pencil, obtaining |B(a,b)|<=15, a contradiction. This conclusion
retains the possible universal support and all finite events. It is
not obtained by subtracting three events from a triangle count. No
lower-weight or singular event is removed to make the application.

Both possible nonlinear intersection sizes have been excluded for the
arbitrary initial pair. Distinctness already excludes intersection four,
so every pair intersects in at most one label, as asserted.

### Citations, specialization and limitations

This is a REPRODUCTION specialization under the prior SPECIALIZE
assessment `drafts/literature/2026-10-14-equality-support-linearity.md`.
The added local input is the pair-preserving degree-four selection and
its complete applicability assembly; no new distance, shortening or
count theorem is proved. The audited input proofs and finite certificates
are reused. L085's audited transfers guide the check but its existential
conclusion is not a premise. The direct inputs are exactly those used
above; no extraction theorem or unrelated row exclusion is needed.

The underlying distance input is J. I. Hall, *Notes on Coding Theory*,
GRS chapter, Theorem 5.1.1 and proof, printed pp. 63–64
([primary chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf)).
Distinct H labels, unit nonzero multipliers and 0<k=8<=n=16 meet its
hypotheses over F and give distance nine, already specialized in L010.
L041's existing shortened-kernel input is I. Marquez-Corbella and
R. Pellikaan, *A characterization of MDS codes that have an error
correcting pair*, FFAA 40 (2016), 224–245, section 5, Definitions
5.1–5.2, Lemma 5.3 and the following unnumbered GRS shortening formula,
printed pp. 7–8 of the accepted manuscript dated 2016-02-29
([primary manuscript](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
[DOI](https://doi.org/10.1016/j.ffa.2016.04.004)). Seven deletions
leave 16-7>=8 positions, dimension one and nonzero distinct-label
multipliers. These imported standard facts are not reproved here.

The conclusion supplies no bound on the number of supports in an
arbitrary linear family, nor a uniform twelve-additional-recovery bound.
The abstract linear obstruction in L072 remains relevant. The stopped
incidence routes in ATTEMPTS/016,017,027 are not restarted: their
incidence hypotheses alone do not supply the actual moment exclusions
used here. There is no claim beyond the sources checked or claim of
mathematical novelty. The separate critical audit below checks this assembly.

### Separate critical audit — 2026-10-14

The prior SPECIALIZE assessment
`drafts/literature/2026-10-14-equality-support-linearity-critical-audit.md`
approved this REPRODUCTION audit. It found no missing case, invalid
transfer or out-of-scope count application. The theorem and its proof
are unchanged. This verifies a local necessary restriction, not a
stronger count or progress beyond the checked source results.

**Selection and universal quantifier.** L010 gives actual unique errors
at sixteen distinct finite parameters, distinct four-supports, and
degree exactly four at every label. Fix the pair before selection.
Intersection four would identify its supports and is excluded;
intersection two or three supplies a common x. Of the four distinct
supports through x, two are the fixed pair, leaving two permissible
third supports. Either has its own actual error and distinct parameter.
For r=2 the union is at most nine, and for r=3 it is at most eight.
Distinct four-sets give the lower bound five. The triple intersection
remains nonempty. No use of L085's existential conclusion, or renaming
of an already selected triangle, supplies the universal quantifier.

**Every small-union case.** The actual triple meets L032's equality
and nonpersistence hypotheses. Its affine lift retains nonzero constant
coordinates and removes unused coordinates before classification.
Its only rows have union five with common intersection size two, or
union six with empty common intersection. The common x excludes the
latter; seven and eight are impossible, and no smaller distinct-four-set
case exists. For union five, sigma(f(T))=s(T) is a polynomial identity.
Coefficient comparison puts both coefficient syndromes in that moment
image. Equivalently, two actual errors in it give
sigma(b)=(sigma(e_1)-sigma(e_0))/(gamma_1-gamma_0) and
sigma(a)=sigma(e_0)-gamma_0 sigma(b), with nonzero denominator.

This is precisely L015's containment hypothesis on the retained F,H
and nonzero polynomial determinant and locators. L015 permits arbitrary
extension-field coefficients and separately handles dependent coefficient
syndromes. It counts cancellations and external rational points to bound
the full original B by 5+M(U). L069's universal configuration assertion
is independent of its triangle-specific application: its census covers
every five-set orbit before that application. Only M(U)<=6 is used.
Thus 16<=11 is a contradiction without a triangle premise, subtraction
of base events, or rational original chart. This eliminates r=3 too.

**All union-nine rows and actual gates.** For the surviving r=2 and
union-nine case, L041 applies to the same actual errors. Its membership
identity m_2+2m_3=3 and the common label force m_3=1,m_2=1.
All three tau-zero table rows are excluded. The unique double pair is
the fixed pair, whose intersection size is two; all other pair
intersections have size one. Renaming that pair as 0,1 gives the
singleton counts 2,2,3 and exactly (3), with nine distinct H labels.

The seven omitted labels make c_z nonzero on U; distinct finite
parameters make every alpha_i nonzero. The shortened-kernel relation
has lambda nonzero because at a singleton its left side has one
nonzero term. Dividing only by these nonzero quantities gives
p,q,1-p-q at h and t,1-t at d. Full actual weights give exactly (4),
and singleton weights are lambda c_z/alpha_i. Lambda is not set to one.
For a cyclic permutation the alpha values cycle; for exchanging 0,1
they become (-alpha_1,-alpha_0,-alpha_2). These generate all renamings.
Lambda changes by the same sign, so normalized weights simply reindex
and the actual errors, parameters and input words remain unchanged.

The actual moment vectors at gamma_0,gamma_1 anchor the local converse
to s(T): two distinct finite values uniquely determine an affine vector
polynomial. The original a,b satisfy these anchors. Alternatively the
L041 representatives differ from a,b by codewords because their
coefficient syndromes agree, preserving agreement and input failure on
each support. Thus the bad set is the same original B. The local
g=gamma_1-gamma_0 and rho=(gamma_2-gamma_0)/g satisfy g!=0 and
rho not in {0,1}; no rationality or new infinity condition is required.

**Full-B contradiction and computation.** These are exactly L042 and
L043's local-converse hypotheses, including arbitrary nonzero lambda
and extension-field weights. L042's nonpersistence conclusion agrees
with the original assumptions. L056 expressly bounds the entire finite
B by fifteen. Its reviewed full-B argument obtains fullness from
equality, excludes repeated base supports by polynomial nonpersistence,
and uses L043's exhaustive classification for every remaining full
error. The universal support contributes at most one eligible finite
parameter; all others enter the relaxed set bounded by eleven.
Sixteen would require at least twelve there. An absent universal lift
strengthens this contradiction. Lower-weight and singular events are
not discarded: equality first excludes lower weights by L010, and the
conclusion concerns all original finite bad parameters.

The audit reuses L069's completed all-orbit census audit and L056's
completed assembly audit with its L051/L055 finite inputs. The census
covers 273 orbits with maximum six; its two count paths share a compiler
and residue field. These exact computational dependencies are not
formal verification. No discrepancy in this application required fresh
replay, and none was performed. Primary citations, their specializations
and Mathlib qualifications remain unchanged. The existing eight direct
DAG inputs match the proof; L085 is comparison evidence only.

This canonical audit supersedes pending-L086-audit wording in the
unchanged overview. No argument change requires editing PROOF.md.
L086 does not classify linear families or bound simultaneous triangle
recoveries. Uniform triangle twelve and independent challenge
qualifications remain open. ATTEMPTS/016,017,027 remain valid stop
evidence for their stated incidence implications.

## Mathlib

Full universal pair-linearity theorem: **not checked**. Supporting
finite-field, incidence, moment and GRS coverage: **not checked anew**;
the canonical input files retain their qualifications. No full matching
Mathlib theorem, formal verification or library absence is claimed.
