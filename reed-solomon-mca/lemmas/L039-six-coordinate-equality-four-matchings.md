# L039 — Union-six equality reduces to four perfect matchings

## Hypotheses

Retain all of L033's hypotheses: F=F_(97^20), H the order-sixteen
subgroup of F_97^*, k=8, the pinned cell 1/4<=delta<5/16, eight shifted
moments, nonzero polynomial Hankel determinant D and every nonzero
coordinate-locator polynomial, and an explicit union-six affine lift
with three distinct finite full-weight errors. Assume N_3=0 and N_ext=13.
L010/L033 then give sixteen-count equality.

Use L035's notation. The selected supports are U minus Z_i, where
U=Z_1 disjoint union Z_2 disjoint union Z_3 and |Z_i|=2. Put J=H minus U.
The additional supports are the unique four-set K_0 contained in J,
and {x} union K_(x,j) for x in U and j=1,2. Put W=J minus K_0, so
|W|=6. Every support is that of an actual distinct finite bad parameter,
with all four error weights nonzero. Equality precedes every packing
argument below; abstract incidences are not moment representatives.

## Conclusion

Every outside triple K_(x,j) meets K_0 in exactly one label. In particular
L035's profile is (n_0,n_1,n_2)=(0,12,0), rather than any of its other
three possibilities. For each a in K_0, the three triples containing a
are {a} union e, where the three edges e form a perfect matching M_a
on W. The four M_a are edge-disjoint. The three unused W edges form
a fifth perfect matching M_*, so these five matchings partition the
edges of the complete graph on W.

The six tags in U pair the twelve triples into disjoint pairs: each
pair has different K_0 labels and disjoint W edges. This is a necessary
form for thirteen incidences, uniform over every labeling by H and all
extension-field weights. It does not exclude that form or establish
N_ext<=12.

The remaining form has abstract realizations satisfying all the L032
triple-union conditions, L035 packing and degree conditions, and L010's
support-degree balance. Indeed every construction of this form with
disjoint tag pairs has just one triple of supports with union at most
eight: the three selected supports, with union U of size six. Thus no
six supports have union at most eight either. These are support-only
statements; no actual parameters, field labels, error weights or moment
compatibility are asserted by their converse.

## Proof

### Elimination of the other three profiles

L038 gives disjointness of the two outside triples for every common tag.
L035 gives pairwise intersection at most one for all outside triples,
degrees three on K_0 and four on W, and
(n_0,n_1,n_2)=(t,12-2t,t) for 0<=t<=3. L032 applies to any three
distinct actual errors: unions of seven or eight labels are impossible.
We do not use its five-coordinate enumeration comparison.

Suppose two outside triples K,L each contain two K_0 labels. Each has
one W label. Write x,y for their tags. If x!=y, the union of the three
actual supports K_0, {x} union K and {y} union L consists of K_0,
one or two W labels and two U labels, and hence has size seven or eight.
If x=y, L038 gives K intersect L empty, so their W labels differ; the
same union has size four plus two plus one, or seven. Each case
contradicts L032. Hence n_2<=1.

If n_2=1, then n_0=1 and n_1=10. Write the unique two-K_0 triple as
K={a,b,w}, where w is in W, and let its tag be x. Any one-K_0 triple L
containing w has a tag y different from x, by L038. The union of K_0,
{x} union K and {y} union L then has exactly four K_0 labels, two W
labels (the W pair in L includes w), and two U labels: size eight.
Again L032 forbids it. Therefore w occurs in no one-K_0 triple. It
occurs in at most the unique two-K_0 triple and the unique zero-K_0
triple, so its outside-triple degree is at most two. L035 requires degree
four at w. This contradiction proves n_2=0, and the profile follows.

All three supports used in these applications are actual errors at
distinct finite parameters: K_0 is the unique disjoint additional error,
and the tagged supports are distinct overlapping additional errors by
L033/L035. The field and full-weight hypotheses have not been dropped.

### The perfect-matching organization

Fix a in K_0. Its degree in the outside triples is three. Since each
triple has exactly one K_0 label, these triples have the form {a} union e
for three two-subsets e of W. The pair-packing conclusion of L035 says
two such triples cannot share a W label: otherwise they would share
both that label and a. Thus their three W edges are disjoint and cover
all six W labels, giving M_a.

Two different M_a cannot use the same W edge, again by pair packing.
There are twelve distinct covered W edges out of fifteen. At every W
vertex the four matchings cover four of its five neighbors, so the
three uncovered edges have degree one at every vertex and form M_*.
This proves the five-factor partition without importing a classification
of one-factorizations. L038 says the two triples tagged by x are
disjoint; therefore both their K_0 labels and their W edges are disjoint.

### An abstract converse and the support-only stopping test

Conversely take pairwise disjoint auxiliary sets U,K_0,W of sizes six,
four,six. Partition U into three two-sets Z_i. Take four edge-disjoint
perfect matchings M_a of the complete graph on W, indexed by a in K_0.
Pair the twelve triples {a} union e (e in M_a) into six disjoint pairs,
one pair for each x in U. Form the sixteen supports
\[
 U\setminus Z_1,\ U\setminus Z_2,\ U\setminus Z_3,\ K_0,
 \quad \{x\}\cup\{a\}\cup e
 \quad\text{for the two triples assigned to each }x.       \tag{1}
\]
The first three supports have the L032 union-six pattern. All supports
are distinct four-sets. Each U label occurs in two selected supports
and two tagged supports, each K_0 label in K_0 and its three triples,
and each W label once in each of four matchings. All degrees are four.
Different outside triples meet in at most one label: within one matching
they share only a; between matchings their W edges are distinct and
can share at most one endpoint. The two triples at each tag are
disjoint by construction. All L035 support conditions follow.

Here is a complete check of the L032 triple-union restriction. Write
A_i=U minus Z_i, B=K_0 and S={x,a} union e for a tagged support.
Every triple other than A_1,A_2,A_3 has union at least nine:

* Two selected supports with B have union ten, and with S have union
  nine, since the selected pair covers U.
* A_i,B,S have at least four U labels, four K_0 labels and two W labels,
  hence at least ten.
* For A_i,S,T, if S,T have the same K_0 label, their W edges are
  disjoint and the union has at least 4+1+4=9 labels. If the K_0 labels
  differ, their distinct W edges use at least three labels, giving
  at least 4+2+3=9.
* For B,S,T, equal tags force disjoint W edges and give 4+1+4=9 labels.
  Different tags give at least 4+2+3=9.
* For three tagged supports with three different tags, if all three
  K_0 labels differ there are at least three W labels; if exactly two
  differ, the two W edges in the repeated matching are disjoint and
  use four W labels; if all coincide, the three W edges use six.
  The respective lower bounds are 3+3+3=9, 3+2+4=9, and 3+1+6=10.
  If there are only two tags, the repeated-tag pair has distinct K_0
  labels a,b and disjoint W edges e,f. Its outside union has six labels.
  The third outside triple adds a label. If its K_0 label differs from
  a,b, this is immediate. Otherwise, say its label is a, its W edge g
  is disjoint from e because both belong to M_a. It cannot be contained
  in e union f: that would force g=f, whereas f belongs to the
  edge-disjoint matching M_b. Thus g adds a W label. The resulting
  union has at least seven outside labels plus two tags, or nine.
  Three supports cannot all have one tag because each tag occurs twice.

These cases exhaust all triples. Hence the sole union of size at most
eight is the prescribed union-six triple. Any six supports contain a
triple other than this one and consequently have union at least nine;
no extra small-six-union obstruction is needed for this construction.

To verify that the required disjoint pairing exists, label W by
0,1,2,3,4,5, and K_0 by a_0,a_1,a_2,a_3 (auxiliary names, not field values).
Use these perfect matchings, where ij denotes the edge {i,j}:
\[
\begin{array}{c|ccc}
M_{a_0}&05&14&23\\
M_{a_1}&15&02&34\\
M_{a_2}&25&13&04\\
M_{a_3}&35&24&01\\
M_*&45&03&12
\end{array}
\]
They partition all fifteen edges, with three disjoint edges in each row.
Assign the six U tags x_0,...,x_5 to the following pairs of triples:
\[
\begin{array}{c|cc}
x_0&(a_0,05)&(a_1,34)\\
x_1&(a_0,14)&(a_1,02)\\
x_2&(a_0,23)&(a_1,15)\\
x_3&(a_2,25)&(a_3,01)\\
x_4&(a_2,13)&(a_3,24)\\
x_5&(a_2,04)&(a_3,35)
\end{array}
\]
Each pair is disjoint and every triple appears once. Choose
Z_1={x_0,x_1}, Z_2={x_2,x_3}, Z_3={x_4,x_5}. This gives an explicit
abstract witness to (1). The preceding proof, rather than a sample,
establishes its support conditions. These auxiliary labels may be
bijected to H for incidence purposes; no bijection is claimed to
permit moment-compatible errors or a pencil.

### Verification, citations and limitations

The supplementary exact check is
`scripts/all-disjoint-packing/profile-witness-result.json`; reproduce with
`python3 scripts/all-disjoint-packing/profile_witness.py`. It records the
complete support table, tag pairing, all 560 triple checks and all 8008
six-subset checks. For this witness the only small-union triple is the
selected one; the actual minimum six-support union is eleven, against
the necessary threshold nine. There are zero failures. The complete
factor table, tagged triples, check flags and summary were inspected
with the shared JSON inspector using their selected pointers and `--full`.
The computed minimum eleven is auxiliary and is not used in the proof.

The direct mathematical inputs are L010/L033's equality accounting,
L032's forbidden triple unions, L035's exact distribution and packing,
and L038's disjoint-tag conclusion. Their relevant proof passages were
inspected before reliance; this is not their separate critical audit.
The standard distance input remains J. I. Hall, *Notes on Coding Theory*,
GRS chapter, Theorem 5.1.1, printed pp. 63–64
([primary PDF](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf)),
already specialized in L032/L033 to distinct labels, multipliers one,
n=16,k=8 and distance nine over F. No new specialization, reproof of
distance, source classification of matchings, or L015 enumeration is used.

The unchanged EXPLORE assessment authorizes this intermediate obstruction
within the twelve-incidence attempt. POTENTIALLY_NEW means the bounded
source comparison did not establish this local application; it is not
a certified originality claim for the elementary packing facts. This
result narrows equality to t=0, but the abstract witness ends an attempt
to exclude that profile using only the present triple-union conditions.
Future exclusion must add actual moment or other compatibility information.
All eight shifted moments, nonzero full weights, original finite chart,
nonpersistent D/locators, and absence of weight-three parameters remain
essential. No actual thirteen-incidence example, twelve bound, universal
union-six extraction or global fifteen bound follows. L039 awaits a
separate critical audit, as do its newer conditional inputs.

## Mathlib

Coverage of this full conditional matching reduction and its abstract
converse is **not checked**. Supporting finite-set and perfect-matching
coverage is also not checked; no absence or formal-verification claim
is made. The complete elementary arguments needed here are written above.
