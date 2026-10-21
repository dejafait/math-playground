# L035 — A packing obstruction for union-six equality completions

## Hypotheses

Use L033's full hypotheses and notation, including F=F_(97^20), H the
order-sixteen subgroup of F_97^*, the pinned cell, nonzero polynomial D
and all nonzero coordinate locators, and the explicit union-six lift
with three distinct finite full-weight errors. Assume N_3=0 and
N_ext=13. Thus L010 and L033 give sixteen-count equality.

Write U=Z_1 disjoint union Z_2 disjoint union Z_3, with |Z_i|=2,
and J=H minus U. By L034 there are exactly two additional supports
{x} union K_(x,1), {x} union K_(x,2) for each x in U, where each K is
a three-subset of J. There is exactly one additional support K_0
contained in J, of size four. Call x the tag of K_(x,i), and put
W=J minus K_0, of size six. All supports are those of actual distinct
finite bad parameters, with their full nonzero weights; these are not
abstract incidence hypotheses substituted for moment compatibility.

## Conclusion

The twelve triples K_(x,i) are distinct and intersect pairwise in at
most one label. Each meets K_0 in at most two labels. Each label of
K_0 belongs to exactly three triples, and each label of W to four.

Define the leave graph on J: a pair is an edge precisely when no triple
contains it. This is an ordinary simple graph, not the notebook DAG.
Its degree is three at each K_0 label and one at each W label. If n_i
counts the triples with |K intersect K_0|=i, then for an integer t,
\[
 (n_0,n_1,n_2)=(t,12-2t,t),\qquad 0\le t\le3.       \tag{1}
\]
The leave has 6-t edges inside K_0, 3-t inside W, and 2t between them.

At most one tag x has K_(x,1) intersect K_(x,2) nonempty. If such a
tag exists, there is p in W with
\[
 K_{(x,1)}=\{p,a,b\},\quad K_{(x,2)}=\{p,c,d\},
 \qquad K_0=\{a,b,c,d\}.                             \tag{2}
\]
The four pairs between {a,b} and {c,d} are leave edges. Necessarily
t=2, so (n_0,n_1,n_2)=(2,8,2). The two triples contained in W both
contain p and have different tags; their four other labels are distinct.
All other pairs with a common tag are disjoint. In particular, the
alternative with all six pairs disjoint remains allowed by this lemma.

These are necessary conditions on a thirteen-incidence completion.
They neither construct nor exclude every remaining configuration, and
they do not prove the twelve bound or the global fifteen bound.

## Proof

### Pair packing from the forbidden small unions

We apply L032 only to actual triples in this sixteen-count equality
family. It says that a union of at most eight labels has size five or
six; in particular unions of seven or eight are impossible. L032's
field-specific five-coordinate enumeration is not used.

Take two distinct additional overlapping supports with tags x,y,
allowing x=y, and outside triples K,L. One of the three selected
supports U minus Z_i contains both x and y: at most two of the three
Z_i contain either label, so choose a remaining Z_i. Its union with
these two supports has size exactly 4+|K union L|, because their tags
already lie in the selected support and K,L lie in J. If |K intersect L|
were at least two, then |K union L| would be three or four, making this
a forbidden union of seven or eight. Hence |K intersect L|<=1.
This also proves that the twelve triples are distinct.

Likewise choose a selected support containing the tag x of a triple K.
Its union with {x} union K and K_0 has size 4+|K union K_0|.
If K were contained in K_0 this would be eight, impossible. Thus
|K intersect K_0|<=2. All three parameters in each application are
distinct: selected, overlapping and disjoint supports belong to the
distinct errors provided by L033/L034.

Equality gives coordinate degree four in the entire sixteen-support
family by L010. No selected support meets J. The support K_0 uses each
of its labels once, leaving triple degrees three on K_0 and four on W.
Since the triples intersect pairwise in at most one label, triples
through a given label use disjoint pairs of other labels. A label in
d triples therefore has 2d covered neighbors out of nine. Its leave
degree is 9-2d, proving the stated degrees.

### The four possible intersection profiles

Counting triples and their incidences with K_0 gives
\[
 n_0+n_1+n_2=12,\qquad n_1+2n_2=4\cdot3=12.
\]
Consequently n_0=n_2=t and n_1=12-2t. Pairs in triples are never
repeated. Inside K_0 exactly n_2=t pairs are covered. Inside W the
number covered is 3n_0+n_1=12+t. Across K_0,W the number covered is
2n_1+2n_2=24-2t. Subtracting from the available 6,15,24 pairs proves
the three leave-edge counts. The nonnegative count 3-t gives t<=3;
t>=0 follows from its definition. This proves (1) without enumeration.

### A repeated tag with an intersecting pair

Suppose K_(x,1) and K_(x,2) intersect. The packing property gives a
single common label p, so write them as {p,a,b} and {p,c,d}, where
p,a,b,c,d are distinct. None of the four pairs between {a,b} and
{c,d} can occur in another triple M. To see this, suppose M contains
a' in {a,b} and c' in {c,d}. It cannot contain p, as that would repeat
a pair in one of the first two triples. Its third label cannot be any
other label of their union, for the same reason. Thus the three outside
triples have union of size six. M has tag y different from x, because
there are exactly two triples with tag x. The corresponding three
actual supports then have union consisting of these six J labels and
the two distinct U labels x,y, of size eight. L032 excludes this.
Hence all four cross pairs are leave edges.

Each of a,b,c,d now has at least two neighbors in the leave. A W label
has leave degree one, so all four must lie in K_0. They exhaust K_0,
and p belongs to W. This proves (2). Of the six pairs inside K_0,
the pairs {a,b},{c,d} are covered by the displayed triples and the four
cross pairs are uncovered. Thus exactly two pairs inside K_0 are
covered. The count in the preceding paragraph gives t=2. There are
therefore exactly two triples with two K_0 labels, namely the displayed
ones, and exactly two triples contained in W.

Any intersecting pair of triples with a common tag, by the same argument,
would use two triples with two K_0 labels. Only the displayed two are
available, and they already have tag x. Hence no other tag has an
intersecting pair. This proves the at-most-one assertion, including all
other cases of t.

Finally p has triple degree four. Its first two triples already use
all four K_0 labels as partners. Pair packing forbids either of its
remaining two triples from using a K_0 label. They are therefore the
two triples contained in W. They meet only at p, so their four other
labels are distinct. They cannot have the same tag: that would be a
second intersecting pair with a common tag, which was just excluded.
This completes the dichotomy.

### Applicability, source coverage and limitations

The inputs are L010's equality degree balance, L032's conditional
small-union classification, L033's actual finite incidence accounting,
and L034's overlap distribution. The entire proof of L034 was inspected
before use; only its distribution is needed here, not rational descent.
All uses of L032 occur after equality has been deduced. Its elementary
fixed-block argument is already canonical there and is not reproved.
The RS distance input underlying that argument is J. I. Hall,
*Notes on Coding Theory*, GRS chapter, Theorem 5.1.1, printed pp. 63–64
([primary PDF](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf)),
as imported with distinct labels, multipliers one, n=16,k=8 over F in
L032/L033. No new source specialization or theorem reproof is needed.

The unchanged EXPLORE assessment for the twelve-incidence target permits
an intermediate obstruction to thirteen incidences. The elementary
packing specialization above is written out because the inspected
sources do not provide it for these actual supports. POTENTIALLY_NEW
means coverage was not established in that bounded comparison, not
certified originality. No finite search, sample or L015 maximum is used.

The obstruction excludes repeated outside pairs and all but the stated
exception for common-tag intersections. The remaining packing patterns
still require moment-compatible full weights, all eight shifted moments,
nonpersistent locators, absence of weight-three parameters and the
original finite chart. Abstract satisfaction of (1) or (2) is not a
counterexample. Rationality from L034 does not remove those requirements.
This new conditional result awaits a separate critical audit.

## Mathlib

Coverage of this full conditional obstruction is **not checked**.
Supporting finite-set counting and simple-graph results have not been
looked up here; no absence or formal-verification claim is made.
