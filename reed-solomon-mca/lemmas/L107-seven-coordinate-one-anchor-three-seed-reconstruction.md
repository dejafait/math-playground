# L107 — Three support seeds reconstruct the seven-coordinate t=1 profile

## Hypotheses

Let F=F_(97^20), F_0=F_97, H the order-sixteen subgroup of F_0^*,
and C=RS[F,H,8]. Use L010's shifted moments and the pinned same-support
event on 1/4<=delta<5/16. The actual Hankel determinant D and every
actual coordinate locator are nonzero polynomials. Both coefficient
syndromes belong to U_S for a seven-set S subset H. Let f(T) be the
unique affine lift supported on S, as in L104, and assume |B(a,b)|=16.

Assume L104's equal-vector count t is one. Write gamma_0 for that
original finite parameter, P={x in S:f_x(gamma_0)=0}, R=S minus P,
and J=H minus S. Thus |P|=3 and |R|=4. For K subset J of size two put
g_K(X)=product_(z in J minus K)(X-z). All original coefficients,
weights and parameters may belong to F. The original chart is arbitrary.
The inherited finite-certificate qualifications of audited L103 remain.

## Conclusion

Put r=n_2, the number of actual errors other than f with two labels
in S. Then 9<=r<=12. Every such overlap I is either a pair in P or
a pair {x,y} with x in P and y in R. No I repeats. At least six rows
are of the latter kind.

Three of the r support rows can be chosen as follows:

* I_1={x_1,y_1}, I_2={x_2,y_2}, with x_1!=x_2 in P and y_1!=y_2 in R;
* I_3 contains neither y_1 nor y_2;
* A_j=I_j union K_j, with |K_j|=2 and K_j subset J.

These support labels alone uniquely reconstruct, or fail an explicit
gate for, a rational projective lift

\[
 w(\mu)_x=p_x\quad(x\in P),\qquad
 w(\mu)_z=A_z\mu+B_z\quad(z\in R),                     \tag{1}
\]

zero off S, with p_x,A_z in F_0^*, B_z in F_0. Fix any p_* in P
and require p_(p_*)=1. The first two seeds have mu=0,1. The third has
a uniquely determined theta in F_0 minus {0,1}. The base direction
mu=infinity has representative w_infty=(0,A), full on R.

For fixed (S,P), at most

\[
 \binom32\binom42\,2\cdot36\cdot35\cdot9\cdot36
       =14,696,640                                           \tag{2}
\]

support seeds cover every assumed equality pencil. Each surviving seed
has 15*36=540 explicit remaining support tests, with no unknown field
coefficients or recovery parameters. Each successful full test gives a
rational scalar mu. In a prescribed original chart delete its one omitted
point mu_*, which is finite and need not be rational. Equality requires
at least nine distinct remaining scalars; an evaluated upper bound below
nine would exclude this profile. No such table is evaluated here.

The construction converse realizes the base and three seed events with
actual polynomial nonpersistence. It does not realize nine rows, sixteen
events, or the t=1 equality profile. The fifteen bound, t=0, other
profiles and challenge-definition qualifications remain unresolved.
The separate step-294 critical audit found no defect in this necessary
reduction or its qualified local converse; no finite table was evaluated.

## Proof

### Existing inputs and forced support seeds

Use L010's moment injectivity on at most eight coordinates, unique
weight-at-most-four errors, pointwise determinant factorization,
same-support badness and equality balance. Audited L104 supplies the
exact one-row shortening criterion, including zero weights before
equality. Its standard inputs are imported with their checked hypotheses:
J. I. Hall, *Notes on Coding Theory*, GRS chapter, Theorem 5.1.1,
[pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
applies to our sixteen distinct labels, nonzero unit multipliers and k=8
over F; I. Marquez-Corbella and R. Pellikaan, *A characterization of MDS
codes that have an error correcting pair*, FFAA 40 (2016), 224–245,
[DOI 10.1016/j.ffa.2016.04.004](https://doi.org/10.1016/j.ffa.2016.04.004),
[accepted manuscript, February 29, 2016](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
section 5, Definitions 5.1–5.2, Lemma 5.3 and following unnumbered
shortening formula, pp. 7–8, applies to shortening at exactly J minus K.
L104 checks all seven deletions, positive remaining dimensions 7 through
1 and nonzero retained multipliers, and restores all eight moments.
This proof uses that application without reproving either source theorem.

Audited L103 excludes an inactive coordinate of the seven-set lift:
otherwise the same coefficient syndromes lie in a six-set moment space
and its full original bad-set bound is fifteen. Thus every coordinate
of f on S is active. Equality gives full errors, distinct supports and
degree four at every label by L010. As in L105, if two distinct actual
errors had union W of size at most six, their moment identities at
distinct finite parameters would place sigma(a),sigma(b) in U_W.
Enlarging W to six labels would contradict L103, with the same actual
polynomials and original chart. Hence every two equality supports
intersect in at most one label. This is a new application of L103, not
an assumption of support linearity or an invocation of L086.

The base error is f(gamma_0), full on R. Each other two-overlap I meets
R in at most one label. Its only shapes are therefore PP and PR as in
the conclusion. Two such I cannot coincide, by support linearity.
L104 gives r=9+n_0 and n_1=6-2n_0, so 0<=n_0<=3 and 9<=r<=12.
There are only three PP pairs, leaving at least six PR pairs.

View those PR pairs as edges of a simple bipartite graph on P and R.
There are two edges disjoint in both endpoint sets. Indeed, if no two
were disjoint, choose two with different P endpoints; these exist since
a single P endpoint has only four neighbors, less than six. They must
share an R endpoint y. Every other edge must meet both of them. Any
edge not incident with y would need both different P endpoints, which
is impossible. All edges would then be incident with y, giving at most
three, a contradiction. Choose these two edges as I_1,I_2.

For z in R, its base occurrence consumes one of its four equality
incidences. At most three of the r two-overlap rows therefore contain z.
At most six contain y_1 or y_2. Since r>=9, there is a third row
containing neither, as required. It differs from the first two. Its I_3
is either one of three PP pairs or one of six PR pairs using
R minus {y_1,y_2}. This proves seed existence before any reconstruction.

### Projective normalization without changing the original event

Put tau=T-gamma_0. On P write f_x(T)=d_x*tau with d_x!=0. On R write
f_z(T)=a_z+b_z*tau with a_z!=0; b_z may vanish. At seed j=1,2 the
original tau_j and shortening scalar lambda_j are nonzero. The first is
nonzero because the seed is not the base, the second because its two
outside weights are full. L104 gives f_x(T_j)=lambda_j*g_(K_j)(x)
for x in P minus {x_j}. Thus

\[
 p_z/p_{z'}=g_{K_j}(z)/g_{K_j}(z')
       \quad(z,z'\in P\setminus\{x_j\}),\quad j=1,2.   \tag{3}
\]

The two different edges on the three vertices of P form a connected
tree. They determine exactly one normalized nonzero p over F_0, since
all g evaluations on S are nonzero elements of F_0. Actual data have
d=alpha*p, alpha=d_(p_*)!=0, by uniqueness of that tree solution.

For tau!=0 divide f by alpha*tau and put nu=1/tau. This gives p on P
and (a_z/alpha)*nu+b_z/alpha on R. The two seed values nu_1,nu_2 are
distinct and nonzero. Normalize

\[
 \mu=(\nu-\nu_1)/(\nu_2-\nu_1).
\]

It follows that (1) holds, initially over F, with

\[
 A_z=(a_z/\alpha)(\nu_2-\nu_1)\ne0,\qquad
 B_z=(a_z/\alpha)\nu_1+b_z/\alpha.                     \tag{4}
\]

This is an invertible projectivity on the syndrome line. Independence
also follows from the disjoint nonzero P entries of w(0) and R entries
of w_infty; moment injectivity on S preserves it. The base is infinity.
Original infinity is the single omitted finite value

\[
 \mu_*=-\nu_1/(\nu_2-\nu_1),                          \tag{5}
\]

different from 0,1 and every selected finite event. It may lie outside
F_0. The normalization does not assert rationality of original parameters
or original error weights. At every finite original nonbase parameter,
the scale alpha*tau is nonzero and restores its original moments and
error. At the base, f(gamma_0) is the nonzero scalar
alpha/(nu_2-nu_1) times w_infty, so that event is retained too.

### Explicit reconstruction from the three support labels

Here are all gates, interpreted as rejection tests for proposed support
seeds. First solve (3). Write g_j=g_(K_j), and choose any z in P minus
I_j to define c_j=p_z/g_j(z), for j=1,2,3. Test

\[
          p_z=c_jg_j(z)\quad(z\in P\setminus I_j).     \tag{6}
\]

The first two tests hold by (3); the third is a genuine test when I_3
is PR. Every c_j is in F_0^*. For actual data it equals
lambda_j/(alpha*tau_j), not the unnormalized original multiplier.

Let Z=R minus {y_1,y_2}, of size two. For z in Z set

\[
 B_z=c_1g_1(z),\qquad A_z=c_2g_2(z)-c_1g_1(z).        \tag{7}
\]

Reject if either A_z is zero. Equation (4) proves these are nonzero
for actual data, including original constant coordinates. Since I_3
contains at most one R label, Z minus I_3 is nonempty. Choose one z_*
there by a fixed ordering and set

\[
 \theta=(c_3g_3(z_*)-B_{z_*})/A_{z_*}.                 \tag{8}
\]

Reject theta=0 or 1, and test A_z*theta+B_z=c_3*g_3(z) for every
z in Z minus I_3. Actual data pass, since their third event is distinct.
Both missing coordinates y_1,y_2 are observed by the third row. Set

\[
 A_{y_1}=\frac{c_3g_3(y_1)-c_2g_2(y_1)}{\theta-1},
 \qquad B_{y_1}=c_2g_2(y_1)-A_{y_1},                  \tag{9}
\]
\[
 B_{y_2}=c_1g_1(y_2),\qquad
 A_{y_2}=\frac{c_3g_3(y_2)-B_{y_2}}{\theta}.          \tag{10}
\]

Reject either new A equal to zero. All quantities are now rational and
unique. To make all remaining conditions explicit, put mu_1=0, mu_2=1,
mu_3=theta and test, for each seed,

\[
 w(\mu_j)_z=c_jg_j(z)\quad(z\in S\setminus I_j),
 \qquad w(\mu_j)_i-c_jg_j(i)\ne0\quad(i\in I_j).       \tag{11}
\]

These include the earlier consistency checks; no generic rank claim
replaces any of them. Actual data pass every test by (4) and L104.
Conversely, a passing seed has all these full recoveries by L104's
moment identity. The outside weights are -c_j*g_j(k), k in K_j, hence
nonzero. Equations (7)–(10) are just interpolation at distinct points;
they exhibit uniqueness rather than leaving extension-field alternatives.

### Complete necessary finite test and size bound

For any of the fifteen possible overlap pairs I (three PP and twelve
PR) and any two-set K subset J, choose a fixed z in P minus I, put
c=p_z/g_K(z), and test p_x=c*g_K(x) on all P minus I. Choose a fixed
y in R minus I; it exists and A_y!=0. The only possible scalar is

\[
                  \mu=(c g_K(y)-B_y)/A_y.             \tag{12}
\]

Check w(mu)_x=c*g_K(x) for all x in R minus I and both nonzero
weights w(mu)_i-c*g_K(i), i in I. Together these are necessary and
sufficient for a full two-overlap error on I union K for this projective
lift. Subtracting c*g_K on all H verifies the entire codeword difference,
not merely a quotient equation. They are exactly L104's recovery
criterion, with lambda=c. In particular all successful mu lie in F_0;
no nonrational recovery scalar can be missed because (12) has a nonzero
slope. Infinity is the separate base, not a two-overlap error.

Delete mu_* for the original finite chart, and count distinct mu. Two
different successful full supports at the same scalar would violate
L010's sparse-error uniqueness, so deduplication is safe. All other
possible bad-support shapes remain outside this necessary filter. Lower
weights are excluded here only after L010 equality supplies fullness;
they remain in L010's full bad-set bound before equality is assumed.

There are 36 unordered pairs of disjoint PR edges: choose two P and
two R vertices, then one of the two matchings. Order each pair by a fixed
rule. There are 36 choices for K_1 and 35 for K_2, since equality
support linearity forbids K_1=K_2. There are nine I_3 choices avoiding
y_1,y_2 and at most 36 K_3 choices. This proves (2), allowing redundant
or invalid seeds. Any additional pair-intersection filter can only reduce
the count. For unknown P there are binom(7,3)=35 choices, all covered
without assuming label symmetry. The formulas apply in particular to
S={1,8,12,18,22,27,33}; no table, maximum or census is asserted for it.

### Local converse and exact limitations

For a passing seed define w_0=(p,B), w_infty=(0,A), zero off S.
Choose xi in F minus F_0 and set

\[
        h(T)=T w_0+(1+\xi T)w_\infty.                 \tag{13}
\]

At T=0 the base is w_infty. For T!=0, its direction is
mu=xi+1/T, with nonzero scale T; the only omitted point is xi.
All rational successful rows, including the three seeds, are therefore
finite. The four seed/base events are distinct and full by the gates.
The base omits all P and J. Each R label is omitted by at least one
of the first two seed supports, since their R labels y_1,y_2 differ.
Thus these full events collectively omit every coordinate of H.
L010's pointwise determinant factorization, which does not assume
polynomial nonpersistence, proves D nonzero at each full event and
each locator nonzero at a full event omitting its label. The actual
polynomials for h are consequently nonzero. Only now apply L010's
same-support bad-event conclusion. Every lift coordinate is active:
p is nonzero and all A_z are nonzero. Moment independence is as above.

This construction establishes the selected events, not their completion
to equality or even nine two-overlap rows. It need not have t=1 among
all its bad parameters. The finite reconstruction is thus a necessary
equality reduction with a qualified local converse, not a proof of the
desired count. Other original charts delete the prescribed mu_* instead;
they are not rationalized by (13). The global interval remains 11/q–16/q.

The unchanged prior EXPLORE assessment is
`drafts/literature/2026-10-17-seven-coordinate-syndrome-bound-review.md`.
This is REPRODUCTION: a local application of the assessed shortening and
affine interpolation tools. L105 motivates the changed t=1 profile but
its t=2 formulas are not mathematical inputs. No originality or progress
beyond the sources checked is claimed. No finite enumeration, mathematical
script, cross-notebook result or new source review is used. The separate
critical audit below validates the reduction, not a challenge candidate.

### Separate critical audit, 2026-10-17

Step 2026-10-17-mca-294-seven-coordinate-one-anchor-critical-audit
checked the complete argument under the unchanged ready seven-coordinate
EXPLORE assessment. It found no mathematical defect or missing direct
input. This is validation of a reproduced partial reduction, not a new
count, a finite census or a claim beyond the sources checked. L010's
kernel, pointwise factorization, event and equality proofs were checked
directly; the exact L103/L104 statements and their completed audits were
reused. Hall Theorem 5.1.1 and the cited shortening formula retain the
field, distinct-label, nonzero-multiplier and dimension hypotheses verified
above. L103's L040/L069 finite-certificate qualifications remain essential;
their computations were not rerun in this audit.

Equality is used before assuming full errors or coordinate balance. An
inactive lift coordinate puts both coefficient syndromes in a six-set,
so L103 applies with the unchanged actual D, locators and original chart.
For two actual errors e_1,e_2 at distinct original parameters gamma_1,
gamma_2, their union W contains representatives of both coefficient
syndromes: sigma(b)=(sigma(e_2)-sigma(e_1))/(gamma_2-gamma_1) and
sigma(a)=sigma(e_1)-gamma_1*sigma(b). If their intersection had size
at least two, |W|<=6 and L103 would contradict equality. Thus all pairs
are linear without importing L086 or assuming a rational chart.

The t=1 base is full on R and zero on P, of respective sizes four and
three. L104 gives n_1=6-2n_0 and r=9+n_0, so 9<=r<=12. Linearity
permits only PP and PR overlap pairs and forbids repeated pairs. At most
three are PP; at least six PR edges remain. A pairwise-intersecting
simple bipartite edge family here is a star, of size at most four:
the proof's two edges with different P endpoints force every other
edge through their common R endpoint. Hence two vertex-disjoint PR
edges exist. Each of their R endpoints occurs in at most three of the
nonbase rows because its base occurrence already consumes one of four
incidences. Their union therefore covers at most six of r>=9 rows.
A third row avoiding both endpoints exists. It is PP or PR, so it
observes at least one of the other two R coordinates. This includes
the PP case and does not assume a third PR row.

Every P coordinate is a nonzero affine polynomial vanishing at gamma_0,
so its slope d_x is nonzero. The complement pairs P minus {x_1} and
P minus {x_2} are distinct edges of a tree on three vertices. Their
nonzero g-ratios therefore determine exactly one normalized p. Setting
alpha=d_(p_*) gives d=alpha*p. On R the nonzero base values a_z,
not the possibly zero original slopes b_z, give
A_z=(a_z/alpha)(nu_2-nu_1)!=0. Distinct nonbase finite parameters make
tau_1,tau_2,nu_1,nu_2 and nu_2-nu_1 nonzero. Thus all four R slopes
in the normalized chart are nonzero, including original constant cases.

Every g_K evaluation used as a divisor is on S or K, disjoint from
its seven roots J minus K. Every P minus I is nonempty, so c_j is
defined and nonzero. Equations (7) determine the two commonly observed
R coordinates at mu=0,1. One of these is observed by row three, and
its nonzero A determines theta by (8); actual distinct events make
theta neither zero nor one. The other common observation, if present,
is tested rather than presumed. Coordinate y_1 is then observed at
1,theta and y_2 at 0,theta, precisely giving (9) and (10). Their
denominators are justified, and both newly computed slopes must pass
the nonzero gate. Equation (11) retains every unused observation and
both residual overlap weights. No branch with a vanishing pivot that
could represent actual equality data has been discarded.

For any remaining PP or PR row, the P equation fixes its nonzero c.
At least three R coordinates are outside I and all their slopes are
nonzero. Equation (12) consequently gives the only possible scalar,
in F_97, while all other observation equations and the two overlap
weights are separately checked. On J minus K both w and g vanish;
on K the error is -c*g; on S minus I the observation equations hold;
and on I the recovered difference is w-c*g. Hence w-e=c*g on every
coordinate. This verifies all eight moments through L010's kernel
identity and the degree-seven codeword, not merely projected recovery.
Zero weights are rejected only inside this equality-conditioned filter;
L010 continues to handle every lower-weight original event beforehand.

There are binom(3,2)*binom(4,2)*2=36 unordered disjoint PR edge pairs.
A fixed order loses none, since any such actual pair can be normalized
to 0,1 in that order. The 36*35 outside choices retain every possible
ordered K_1,K_2; equality excludes K_1=K_2 by pair linearity. Row three
has 3+3*2=9 overlap choices and 36 outside choices. The product is
36*1260*324=14,696,640. The complete subsequent filter has
(3+3*4)*36=540 indexed rows, including the seeds, not 540 additional
events. Overcounting invalid seeds is harmless for this upper bound.
Distinct successful full supports cannot represent the same scalar by
sparse-error uniqueness. Nevertheless the required output is the set
of distinct scalars, with nine necessary at equality, not the row count.

The chart map is an invertible projectivity: the base tau=0 maps to
infinity, while original infinity maps to the finite mu_* in (5).
All other original parameters have nonzero scale alpha*tau; the base
has the separate nonzero scale stated after (5). Independence of the
syndrome directions follows from the P coordinates of w_0, the nonzero
R vector w_infty and injectivity on S. Thus no projective directions
collapse. The omitted mu_* need not be rational and must be deleted
when counting in the prescribed chart. A count before deletion is
only an upper bound; original parameter rationality is never inferred.

For the local converse, (13) has original coefficient words w_infty
and w_0+xi*w_infty, supported on S. Its base T=0 is full on R, and
each seed scalar mu gives T=1/(mu-xi)!=0 and the full error T*e(mu).
These three parameters and zero are distinct. The base omits P and J;
each R label is omitted by seed one or seed two because their sole
R labels differ. At each full event L010's pointwise factorization
gives D!=0, and at a full event omitting x it gives ell_x!=0. These
facts establish polynomial nonpersistence before the same-support
badness conclusion is used. The new lift is fully active: its P
coordinates have slopes p_x!=0 and its R coordinates have constants
A_z!=0. This proves precisely four selected actual events, with no
assertion about t, nine recoveries or completion to sixteen.

The audited statement is therefore a complete necessary finite filter
for the stipulated t=1 equality profile with a limited local converse.
No table maximum, global fifteen bound or universal seven-coordinate
representation follows. No mathematical script was needed for this
analytic audit, and no new DAG edge is introduced.

## Mathlib

Full matching t=1 three-support reconstruction and seven-coordinate count:
**not checked**. Supporting affine interpolation, finite-field, GRS
shortening and projective-coordinate results: **not checked**. Unknown
coverage is not absence. L103's audited finite-certificate qualifications
remain part of the equality restriction; no global count is proved here.
