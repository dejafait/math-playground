# L085 — Sixteen-count equality forces an actual gated tau-zero triangle

## Hypotheses

Let F=F_(97^20), let H be the order-sixteen subgroup of F_97^*, and
let C=RS[F,H,8] with unit evaluation multipliers. Fix a,b in F^H and
the pinned same-support event at 1/4<=delta<5/16. Write B(a,b) for
the original finite bad-parameter set and
\[
 s(T)=\sigma(a)+T\sigma(b),\qquad
 \sigma_j(z)=\sum_{x\in H}z_xx^j\quad(1\le j\le8).
\]
Assume L010's Hankel determinant D(T) and every coordinate locator
ell_x(T) are nonzero polynomials, and assume |B(a,b)|=16.
Parameters, input words and error weights may lie anywhere in F.
No rationality of the original affine chart is assumed.

Use the established local inputs with their stated qualifications:
L084's abstract extraction; L032 and L041's necessary classifications;
L015 and only the universal M(A)<=6 conclusion of L069; L033/L040's
full-bad-set bound; L082/L083's local-converse row bounds; and the
complete L043 setup with L042 and L056. The finite checks in L040,
L069 and L056's counting inputs remain essential computational inputs.

## Conclusion

There exist three distinct original finite parameters gamma_0,gamma_1,
gamma_2 in B(a,b), with their actual full-weight errors e_0,e_1,e_2,
and nine distinct labels h_01,h_02,h_12,y_1,y_2,z_1,z_2,w_1,w_2 in H,
such that
\[
 A_0=\{h_{01},h_{02},y_1,y_2\},\quad
 A_1=\{h_{01},h_{12},z_1,z_2\},\quad
 A_2=\{h_{02},h_{12},w_1,w_2\},
 \qquad A_i=\operatorname{supp}(e_i).
\]
These very errors enter L041's gated tau=0, (1,1,1) triangle row in
the unchanged original pencil. Explicitly, with U their union, put
\[
 \alpha_0=\gamma_1-\gamma_2,\quad
 \alpha_1=\gamma_2-\gamma_0,\quad
 \alpha_2=\gamma_0-\gamma_1,\qquad
 c_x=\prod_{t\in H\setminus U}(x-t)\quad(x\in U).
\]
There are lambda in F^* and p_01,p_02,p_12 in F minus {0,1} with
\[
 e_i(x)=\frac{\lambda c_x}{\alpha_i}b_{i,x}
 \quad(x\in A_i),\qquad \sigma(e_i)=s(\gamma_i),
\]
where singleton contributions are b_(i,x)=1 and the shared contributions
are (p_01,1-p_01) on indices (0,1) at h_01,
(p_02,1-p_02) on (0,2) at h_02, and
(p_12,1-p_12) on (1,2) at h_12. All absent weights are zero.

This is a necessary local reduction, not an equality construction or a
uniform triangle count. It leaves the twelve-additional-recovery bound
for arbitrary gated triangles unresolved. The global interval remains
11/q–16/q, and the challenge-definition and parameter qualifications
remain independent. The separate critical audit of 2026-10-14 found no
defect in this assembly within its stated scope, as recorded below;
it is not a complete challenge candidate or a claim of originality.

## Proof

### Extraction selects actual errors

L010's equality conclusion gives sixteen distinct four-element error
supports and degree four at every coordinate of H. All their weights
are nonzero, every error is unique, and its moments equal s(gamma) at
its associated original finite bad parameter gamma. Thus these supports,
with vertex set H, meet every hypothesis of L084: sixteen vertices,
sixteen distinct four-sets and degree exactly four. L084 supplies three
distinct supports with union U of size at most nine.

Select their actual errors and the associated parameters. These
parameters are distinct, since each parameter has only one sparse error.
No weights or parameters are assigned to an abstract edge independently
of the original pencil. Distinct four-sets imply |U|>=5. We treat
5<=|U|<=8 and |U|=9 separately, always retaining a,b and their full B.

### Small unions cannot occur at equality

For |U|<=8, all L032 hypotheses hold: the field contains H, the code,
moments and radius are the same, polynomial nonvanishing and equality
are retained, and the selected errors are distinct actual full errors
at distinct finite parameters. Its necessary classification leaves only
union five or union six; union seven and eight are excluded by that
result, rather than by an incidence assumption.

For union five, L032 supplies an affine vector f(T)=u+Tv supported
on U with sigma(f(T))=s(T). Comparing coefficients gives sigma(a),
sigma(b) in the five-set moment image U_U. The fixed F,H and
polynomial hypotheses are exactly L015's. Therefore
\[
 |B(a,b)|\le5+M(U)\le5+6=11,
\]
contradicting sixteen. The second inequality imports L069's universal
configuration assertion for every five-subset of this H. Its
triangle-specific hypotheses, additional-recovery set and three-base
subtraction are not used. The computation on all 273 five-set orbits
remains the qualification of this imported six bound.

For union six, L032 gives a partition U=Z_1 disjoint union Z_2 disjoint
union Z_3 into pairs and the exact identities
\[
 f_x(T)=d_x(T-\gamma_i)\ (x\in Z_i),\quad d_x\ne0,
 \qquad f_x(T)=0\ (x\notin U),\quad \sigma(f(T))=s(T).
\]
The selected full errors are f(gamma_i), and the coefficient vectors
are independent. These are L033's explicit supplied-triple hypotheses,
with nonzero slopes and the same three distinct finite roots; no fresh
construction or reparameterization is needed. L010's equality conclusion
also gives N_3=0, so L040's stated main branch applies and yields
N_ext<=12. L033's full accounting gives |B(a,b)|=3+N_ext<=15,
again a contradiction. L040's independent finite-certificate dependence
is retained. Its lower-weight alternative would also bound the full B
by fifteen, but equality already excludes that alternative here.

Consequently the extracted actual triple has union exactly nine.

### Necessary weights enter the local converses without scaling

All L041 necessary-direction hypotheses now hold, including equality
and the original polynomial premises. It gives its nonzero lambda,
the unscaled actual-weight formulas in the conclusion above, and its
complete four-row incidence table. Each alpha_i is nonzero by parameter
distinctness; each c_x is nonzero because its factors compare distinct
H labels. Every present normalized weight
\[
 b_{i,x}=\alpha_i e_i(x)/(\lambda c_x)
\]
is nonzero. At each label the present weights sum to one. At a double
label both p_x and 1-p_x are therefore nonzero; at a triple label all
of p_x,q_x,1-p_x-q_x are nonzero. These are actual gates, not choices
made to construct a different pencil. In particular we do not set
lambda=1 or scale the errors or words.

We may rename the three errors to the table's representative rows.
For precision, if pi permutes {0,1,2}, set gamma'_i=gamma_(pi(i))
and e'_i=e_(pi(i)). The definitions of alpha give
alpha'_i=sgn(pi) alpha_(pi(i)): a cyclic permutation preserves the
three differences and a transposition negates them after reindexing,
and those permutations generate S_3. U and c do not change. Thus
\[
 \sum_i\alpha'_i e'_i=\operatorname{sgn}(\pi)\lambda c,
 \qquad \lambda'=\operatorname{sgn}(\pi)\lambda,
 \qquad b'_{i,x}=b_{\pi(i),x}.
\]
Nonzero gates persist. This recomputation of the coefficient lambda
does not scale the actual errors or alter s(T), any gamma value, or
the original excluded direction. Label-role names simply name distinct
existing H elements; they impose no field-label symmetry.

After any such renaming, the first two exact identities
sigma(e'_i)=s(gamma'_i) anchor L041's local converse to the specified
original a,b. The third identity already holds. Hence the existing
local-converse row bounds apply to this same pencil, not merely to a
new pencil that happens to have locally compatible weights.

### Every nontriangle union-nine row is excluded

For tau=0 and (n_01,n_02,n_12)=(3,0,0), let P be the three double
labels, y and z the singleton labels of A_0 and A_1, and W the four
singleton labels of A_2. These roles are disjoint, with sizes 3,1,1,4.
The actual normalized weights at x in P are p_x,1-p_x with
p_x not in {0,1}; every singleton has weight lambda c_x/alpha_i.
The same original first two moment identities verify L083's anchoring
hypotheses. Its full-bad-set conclusion gives |B(a,b)|<=11,
contradicting equality. No triangle additional-recovery theorem is
invoked in this row.

For tau=0 and (2,1,0), name the two {0,1} labels a_0,b_0 and the
{0,2} label c_0. Name the singleton sets {y}, {z_1,z_2},
{w_1,w_2,w_3}. The supports are then exactly L082's displayed
mixed row (with its label names a,b,c replaced by a_0,b_0,c_0).
At the three double labels the actual index-0 normalized weights
p_a,p_b,p_c are outside {0,1}, and their partners are 1-p_a,
1-p_b,1-p_c. All singleton formulas, lambda, alpha_i, Q and the
two anchored syndrome equations coincide with L082. Its full-B
bound is fifteen, a contradiction. We use that audited row result;
we do not apply triangle-only L070/L071 to these base errors.

For tau=1 and (1,0,0), name the unique triple label h and the unique
double label d. The singleton sets have sizes two, two and three,
giving precisely L043's supports. Write the actual normalized weights
at h as p,q,1-p-q and at d as r,1-r. Their nonzero values verify
\[
 \lambda\ne0,\qquad pq(1-p-q)r(1-r)\ne0.
\]
The original gamma_i remain finite and distinct and all nine labels
remain distinct. These facts and the actual three syndrome identities
meet L042's complete local-converse hypotheses; its audited conclusion
verifies the nonpersistent common locator required in the L043 setup.
The original L010 hypotheses already gave polynomial nonpersistence,
so this use neither imports a new condition nor replaces the pencil.
We now have exactly the complete gated L043 setup used by L056.
L056's full finite bad-set bound gives |B(a,b)|<=15, contradicting
sixteen. Its statement covers the possible universal support and all
finite events; we do not assume that universal lift exists or discard
lower-weight parameters to make this application.

L041's only remaining row is tau=0 and (1,1,1). Name its unique
double labels h_01,h_02,h_12 and its two singleton labels per error
as Y,Z,W. Its already established actual-weight formulas and gates
are exactly those stated in the conclusion. This proves the reduction.

### Sources and limits

This proof assembles previously assessed and audited inputs. L084
imports David Ellis and Nathan Linial, *On regular hypergraphs of high
girth*, arXiv:1302.5090v5 (12 July 2017), Section 2, Lemma 1,
equations (5)–(6), printed pp. 5–6
([versioned primary text](https://arxiv.org/pdf/1302.5090v5)); its
canonical specialization verifies the nonlinear and component cases.
L010/L041 and the row bounds use J. I. Hall, *Notes on Coding Theory*,
GRS chapter, Theorem 5.1.1, printed pp. 63–64
([primary chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf)).
Here F is a field, the sixteen labels are distinct, multipliers are
one and 0<8<=16, as required for its dimension and distance result.
L041's shortened-kernel specialization uses I. Marquez-Corbella and
R. Pellikaan, *A characterization of MDS codes that have an error
correcting pair*, FFAA 40 (2016), 224–245, section 5, Lemma 5.3 and
the subsequent unnumbered GRS shortening formula, printed pp. 7–8 of
the accepted manuscript dated 2016-02-29
([primary manuscript](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
[DOI](https://doi.org/10.1016/j.ffa.2016.04.004)). Its established
seven deletions retain nonzero distinct-label multipliers and leave
dimension one. None of these general theorems is reproved here.

The saved SPECIALIZE comparison covers precisely this actual-error
assembly. This is REPRODUCTION: local progress consists in verifying
the bridges and exhausting the rows, without claiming progress beyond
the sources checked or originality. Audited finite conclusions are
reused without new certificate execution; a preview is not offered
as verification. The separate audit below checks this assembly itself.
The stopped stronger incidence routes in ATTEMPTS/016,017,027 are
not reopened. In particular a necessary triangle does not force a
useful additional pair, and no uniform triangle count is proved.

### Separate critical audit — 2026-10-14

Step 211 used the prior SPECIALIZE assessment
`drafts/literature/2026-10-14-equality-triangle-critical-audit.md`
for exactly its approved proof-audit target. It found no missing
applicability premise, sign defect or uncovered finite event. This is
verification of an existing REPRODUCTION, not a new bound or progress
beyond the sources checked. The following checks concern the assembly;
completed input audits, including their full finite-certificate checks,
are reused rather than represented as new replays.

**Extraction and the original errors.** The radius cell imposes an
agreement threshold of twelve, since 11<16(1-delta)<=12. L010 is
therefore the correct sparse-error theorem for these same words.
Its nonzero-polynomial premises hold by hypothesis, including singular
values in its count. Sixteen forces all errors to have weight four,
distinct supports and degree four at each of the sixteen labels.
Thus L084 applies to a simple four-uniform family, with no unused
vertex or unverified regularity assumption. Its conclusion is three
distinct edges, not three unspecified weight assignments. Selecting
their associated errors retains the actual moments and finite
parameters. Sparse uniqueness makes their parameters distinct. Their
union has size at least five and at most nine. No extension of an
abstract incidence example to a pencil is presumed.

**Both small-union branches.** L032 is invoked in its necessary
direction, where equality, full weights, distinct finite parameters,
the moment map and |U|<=8 are all available. Its affine lift is a
polynomial identity sigma(f(T))=s(T), not merely an interpolation of
one moment. Consequently its coefficient identities put both original
syndromes in the five-set image when |U|=5. L015 accepts precisely
this F,H, event and nonpersistence. It counts at most five cancellation
parameters, including lower weights, and at most M(U) others on the
extension-field pencil line. Its rational-line argument descends a line
through two rational configuration points, not the original chart.
L069 explicitly proves M(A)<=6 for every five-set A separately from
its triangle application. The already audited census covers all 273
orbits; no triangle premise or three-base subtraction is used here.
Thus the asserted entire-B contradiction is 16<=11.

For |U|=6, the disjoint Z_i pairs, nonzero slopes and three distinct
roots in L032 are exactly the explicit-triple alternative of L033.
Its coefficient independence holds over F; no rational lift is needed.
The supplied errors are f(gamma_i), and the moment identity is for the
original s(T). Equality gives N_3=0 before L040 is applied. Its count
is N_ext<=12 in the same finite chart; L033 then gives
|B|=3+N_ext+N_3<=15. This does not substitute projective compatibility
for valid incidences. If a lower-weight event were present it would
already contradict the equality premise by L010, so no event is
discarded to enter the N_3=0 case. Unions seven and eight are excluded
by L032 itself. These checks leave exactly union nine.

**Weights, permutations and anchoring.** L041's necessary direction
now applies to this actual triple. Every alpha_i and c_x is nonzero.
Its relation sum alpha_i e_i=lambda c has lambda nonzero, so its
coordinate equations give the stated gates for the actual weights.
In particular the use of the local converse does not replace these
weights by arbitrary solutions of the same support pattern.

For the cyclic renaming (0,1,2)->(1,2,0), the three newly defined
differences are the old differences with the same cyclic order. For
the transposition (0,1,2)->(1,0,2), they are
(-alpha_1,-alpha_0,-alpha_2). These permutations generate S_3,
verifying alpha'_i=sgn(pi)alpha_(pi(i)) for every renaming. The vector
c is unchanged, and uniqueness of the nonzero coefficient in L041's
relation gives lambda'=sgn(pi)lambda. Hence
alpha'_i e'_i(x)/(lambda' c_x)=b_(pi(i),x). Gates survive with
unchanged actual words, weights and parameter values. No normalization
lambda=1 or projective reparameterization is performed.

The prescribed sigma(e'_0),sigma(e'_1) equal the values of the original
s at two distinct original parameters. An affine vector polynomial
through those two values is unique, so the local-converse pencil is
exactly s. All downstream results apply to every pair of words with
those coefficient syndromes; alternatively the original a,b themselves
satisfy their anchoring equations. No equality of chosen representatives
a_*,b_* with a,b is required, and no change of the bad event is made.

**All three nontriangle rows.** The full S_3 action on the three pair
types gives L041's complete four-row list; its singleton counts are
retained. For (3,0,0), the disjoint roles P,{y},{z},W have sizes
3,1,1,4 and meet every displayed L083 hypothesis. Its three p_x gates
are exactly the actual double weights and its first two anchors hold.
Its conclusion is |B(a,b)|<=11 for the entire original pencil, not
an additional-error bound. For (2,1,0), the pair types {0,1},{0,2}
have multiplicities two and one, with singleton sizes 1,2,3.
Naming their common index 0 gives precisely L082's three supports.
Its p_a,p_b,p_c, Q, alpha and nonzero lambda are the recomputed
actual quantities. Its anchored local-converse theorem gives |B|<=15
in both its pair-ratio branches. The audited L082 application retains
the equal-vector exception and all cancellations, and invokes L040's
full-B alternatives, not a triangle-only pair theorem.

For tau=1 the triple and double labels are h and d, and singleton
sizes are 2,2,3. The actual weights give
pq(1-p-q)r(1-r)!=0, exactly L042/L043/L056's gates. L042's
local-converse statement accepts arbitrary nonzero lambda and all three
original finite parameters. Its nonpersistence conclusion is consistent
with the existing L010 hypotheses and adds no hidden assumption.
L043's complete setup therefore holds for this same s(T).

L056 explicitly concludes an entire-B bound of fifteen. Its equality
contradiction first uses L010 to obtain fullness, excludes a repeated
base support by polynomial nonpersistence, and then applies L043's
exhaustive classification. The unique universal support contributes
at most one eligible finite parameter, and all others belong to its
relaxed nonuniversal set of size at most eleven. Thus sixteen would
require at least twelve such parameters. The proof does not presume
the universal lift exists, count infinity, or lose lower-weight events:
those are excluded only under the sixteen-count contradiction premise.
This verifies the full-B conclusion needed here, rather than attempting
to obtain it by subtracting base events from an unrelated count.

**Verdict and limits.** The surviving row is exactly tau=0,(1,1,1),
with its three double labels and two singleton labels per error. Its
unscaled formulas and original moment identities are those in the
conclusion. No uniform triangle count is used anywhere in the audit.
All listed direct inputs are genuine mathematical inputs; no new
input or dependency edge is introduced. L040, L069 and L056's counting
inputs retain their finite-computation and implementation qualifications.
No discrepancy justified rerunning those complete certificates, and
none was rerun. The exact primary citations and specializations above
remain unchanged. Mathlib coverage remains as stated below.

This canonical audit supersedes pending-audit wording in the unchanged
overview; the argument itself has not changed. The global interval
remains 11/q–16/q. Uniform triangle twelve and the challenge-definition,
field-size and endpoint qualifications remain unresolved. The historical
stops in ATTEMPTS/016,017,027 concern stronger incidence implications
and neither validate nor invalidate this actual-error assembly.

## Mathlib

Full matching coverage for this assembly has not been checked. The
input files retain their individual supporting-result and computational
qualifications. This informal case assembly is not a Lean verification;
unknown library coverage is not evidence of absence.
