# L037 — Five-label completion and a stronger exceptional labeling test

## Hypotheses

Retain L036's complete hypotheses, including L033's F=F_(97^20),
H of order sixteen in F_97^*, k=8, pinned four-omission cell, eight
shifted moments, nonzero polynomial D and all nonzero coordinate-locator polynomials,
three distinct finite full-weight errors with a union-six affine lift,
and N_3=0, N_ext=13. Thus L010 sixteen-count equality holds before any
balance or packing is used. Assume L035's exceptional intersecting tag
pair, with L036's notation
\[
 U=\{x,y,r,s,t,w\},\quad
 U'=\{x,p,a,b,c,d\},\quad U\cap U'=\{x\},
\]
\[
 A_1=\{r,s,t,w\},\ A_2=\{x,y,t,w\},\ A_3=\{x,y,r,s\},
\quad B_1=\{x,p,a,b\},\ B_2=\{x,p,c,d\},\ K_0=\{a,b,c,d\}.
\]
Their original finite parameters are respectively gamma_1,gamma_2,
gamma_3,tau_1,tau_2,tau_0, all distinct. All labels in U union U' are
distinct except the displayed shared x. Write
\[
 V=U\setminus\{x\},\quad V'=U'\setminus\{x\},\quad
 E=H\setminus(U\cup U'),\qquad |V|=|V'|=|E|=5.
\]
Use the actual affine lifts f,f' and quadratic pencil of L036:
\[
 f(T)-f'(T)=\operatorname{ev}_H(h(X)q(T,X)),\quad
 h(X)=\prod_{i\in E}(X-i),\quad q(T,X)=q_0(X)+Tq_1(X),\quad \deg q_i\le2.
\]
In particular f_x(T)=c_x(T-gamma_1) and
f'_x(T)=d_x(T-tau_0), with c_x,d_x nonzero. These are the original
finite chart and actual errors, not freely assigned projective points.

## Conclusion

The other ten supports are precisely
\[
 \{z_{ij},z'_{ij},i,j\}\qquad(\{i,j\}\subset E),       \tag{1}
\]
one for each of the ten unordered pairs, with z_{ij} in V and z'_{ij}
in V'. Every tag in V, and every tag in V', occurs twice. Its two pairs
in E are disjoint. Thus each tagging partitions the edges of the
complete graph on E into five matchings of size two. The label missed
by each matching gives a bijection from its five tags to E. No claim
of distinct tag pairs (z_{ij},z'_{ij}) is made.

For tags z,z' and an edge {i,j}, define
\[
 P_{z'}(X)=\prod_{b\in V'\setminus\{z'\}}(X-b),\quad
 Q_z(X)=\prod_{a\in V\setminus\{z\}}(X-a),\quad
 G_{ij}(X)=\prod_{e\in E\setminus\{i,j\}}(X-e).
\]
At its actual parameter tau, there are nonzero lambda,lambda' in F
such that
\[
 (X-i)(X-j)q(tau,X)=lambda P_{z'}(X)-lambda' Q_z(X),       \tag{2}
\]
\[
 f_x(tau)=lambda G_{ij}(x)P_{z'}(x),\qquad
 f'_x(tau)=lambda' G_{ij}(x)Q_z(x).                         \tag{3}
\]
Conversely, for a finite tau outside the six selected parameters,
(2) and the first equation of (3), with nonzero lambda,lambda', give
an actual full-weight four-error on {z,z',i,j}, satisfying all eight
moments and original same-support badness. The second equation of (3)
then follows from (2). Equation (2) alone is insufficient: it does not
remove a possible fifth error at x.

Every edge therefore needs at least one tag pair with
\[
 \Delta_{z,z'}(i,j):=P_{z'}(i)Q_z(j)-P_{z'}(j)Q_z(i)=0.      \tag{4}
\]
All factors here lie in F_97^* at i,j,x. Moreover
\[
 \frac{f_x(tau)}{f'_x(tau)}
 =\frac{P_{z'}(x)Q_z(i)}{Q_z(x)P_{z'}(i)}.                 \tag{5}
\]
This determines at most one original finite tau outside the six
selected values; its scalars in (3) are then uniquely determined.
Neither (4) alone nor (4) with (5) replaces the full polynomial test.

This excludes, over F and irrespective of weights, the following
specified labeling that passes L036's involution test:
\[
 (x,y,p)=(22,79,50),\quad
 \{r,s\}=\{1,96\},\quad\{t,w\}=\{8,89\},\quad
 \{a,b\}=\{64,33\},\quad\{c,d\}=\{27,70\}.              \tag{6}
\]
For its required edge {12,47}, all 25 values of (4) are nonzero.
This is a conditional completion restriction and one labeled exclusion,
not exclusion of every exceptional labeling, the all-disjoint branch,
the twelve-incidence bound or a global fifteen bound. It awaits a
separate critical audit.

## Proof

### Both actual clusters constrain the remaining supports

L036 constructs f' from the three actual errors B_1,B_2,K_0. Its use
of L032 gives omission pairs {c,d}, {a,b}, {x,p} respectively, with
nonzero slopes. Hence the complete L033 hypotheses apply also to U',
with the same s(T), D, locators, original finite parameter chart and N_3=0. Equality still
gives sixteen errors, so L033's accounting for this cluster gives
thirteen additional errors; L034 applies unchanged. Relative to U',
the unique disjoint support is A_1, which is disjoint by inspection.
Relative to U, it is K_0. The six displayed supports are distinct
actual supports at the six distinct finite parameters.

Four of these supports contain x: A_2,A_3,B_1,B_2. L010 equality gives
total coordinate degree four, so no remaining support contains x.
Each remaining support is additional for both clusters. L033 permits
overlap at most one with either cluster, while the disjoint support
for each has already occurred. Therefore it meets each in exactly one
label, necessarily z in V and z' in V'. Its other two labels lie in E.

L035's packing for the original cluster says its outside triples
{z',i,j} meet pairwise in at most one label. Thus two different
remaining supports cannot use the same pair {i,j}. There are ten
remaining supports and exactly ten pairs on E, proving (1). Every
V label occurs in two selected original supports and none of the
three alternate selected supports. L010 degree four therefore leaves
two occurrences among (1). The analogous count for V' gives two as
well; every E label occurs in four of (1).

The exceptional same-tag pair for U has tag x. L035 states that every
other tag pair is disjoint outside U, so the two E edges for each z
in V are disjoint. For U', A_2 and A_3 are an intersecting same-tag
pair with tag x and outside triples {y,t,w}, {y,r,s}. Their common
label is y and their four other labels form its unique disjoint
support A_1, exactly as required by L035. Applying that lemma to
this actual cluster shows that every tag in V' also has two disjoint
E edges. This is not an assumed symmetry of labelings or of weights.

In either tagging, a matching covers four E labels and misses one.
At any label of E, its four incident edges have four different tags,
since edges of the same tag are disjoint. Exactly one tag's matching
misses this label. Thus every E label is missed once, proving the two
claimed bijections. Repetition of an ordered tag pair is not excluded.

### Exact residual compatibility, including the shared label

For an actual remaining error e at tau, apply L033's overlap formula
to both clusters. Its codeword f(tau)-e is evaluated from
lambda G_{ij}P_{z'}, and f'(tau)-e from lambda' G_{ij}Q_z,
with both scalars nonzero. Each polynomial has degree seven. This uses
the already imported seven-deletion specialization of GRS shortening:
Marquez-Corbella and Pellikaan, *A characterization of MDS codes that
have an error correcting pair*, Finite Fields and Their Applications
40 (2016), 224–245,
[DOI 10.1016/j.ffa.2016.04.004](https://doi.org/10.1016/j.ffa.2016.04.004),
[accepted manuscript, February 29, 2016](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
section 5, Lemma 5.3 and following unnumbered GRS shortening formula,
printed pp. 7–8. The deleted labels are E minus {i,j} together with
V' minus {z'}, or V minus {z}, respectively. Each is a seven-set of
distinct labels; the final dimension is one, and all retained
multipliers are nonzero. At deletion stage r=0,...,6,
15-r>=8-r; dimensions remain positive. These are precisely L033's
assessed hypotheses over F. The generic theorem is not reproved.

Subtract the two degree-seven polynomials. Their evaluations equal
f(tau)-f'(tau), hence the evaluations of h q(tau). Evaluation on H
is injective for degree less than eight, as in L010, so the equality
is a polynomial identity. Cancel the nonzero polynomial G_{ij} from
it in F[X], using h=G_{ij}(X-i)(X-j), to obtain (2).
At x the actual error is zero, giving both equations of (3).

For the local converse suppose (2) and the first equation of (3)
hold with the stated finite tau and nonzero scalars. Define
e=f(tau)-ev_H(lambda G_{ij}P_{z'}). The second term is a codeword.
For a in V minus {z}, Q_z(a)=0 and f'_a(tau)=0, so (2), multiplied
by G_{ij}(a), gives f_a(tau)=lambda G_{ij}(a)P_{z'}(a).
Consequently e is zero there. It is zero at x by (3), at V' minus
{z'} by P's roots, and at E minus {i,j} by G's roots. At z',i,j,
its weights are -lambda G_{ij}P_{z'}, all nonzero since none of
those distinct labels is a root. At z, the multiplied identity gives
e_z=-lambda' G_{ij}(z)Q_z(z), also nonzero. Thus e has exactly the
required four nonzero weights. At x the same identity and (3) give
the other equation of (3). L010's kernel identity gives all eight
moments sigma(e)=sigma(f(tau))=s(tau). Its nonzero D/locator hypotheses
then supply original same-support badness. No merely projective point
or error of weight five has been counted.

Evaluate (2) at i and j to get lambda P(i)=lambda' Q(i) and
lambda P(j)=lambda' Q(j). All four evaluations are nonzero because
E,V,V' are pairwise disjoint. Eliminating the nonzero scalars proves
(4); combining either equality with (3) proves (5).
The ratio f_x(T)/f'_x(T)=(c_x/d_x)(T-gamma_1)/(T-tau_0)
is injective away from tau_0: equality at two finite parameters
cross-multiplies to their difference times a nonzero multiple of
gamma_1-tau_0. Its roots are distinct by hypothesis. Thus at most
one finite tau can satisfy (5). Some proposed ratios may occur only
at original infinity, and the six selected parameters remain excluded.
The affine parameter and scalar weights need not be rational; no
change of the original chart is made.

### A full exact table for one involution-passing labeling

The powers of 8 in F_97 give H; 8^4=22 and 8^8=-1 show order sixteen.
All eleven labels of (6) are distinct members. The four pairs are
opposite pairs, so phi(X)=-X exchanges them. Their R rows from L036
are (rs,0,1), etc., with different products (96 and 33 already differ),
so R has rank two. Its kernel generator (0,1,0) has AC-B^2=-1.
This labeling passes that necessary test.

Here V=(79,1,96,8,89), V'=(50,64,33,27,70), and
E={12,18,47,75,85}. The edge {12,47} is mandatory by (1).
In the listed V' order, the values (P(12),P(47)) are
\[
 (22,64),\ (31,17),\ (86,14),\ (4,68),\ (88,21).
\]
In the listed V order, the values (Q(12),Q(47)) are
\[
 (91,38),\ (63,79),\ (16,7),\ (52,31),\ (88,89).
\]
Each value is the displayed product of four label differences modulo
97. Thus the full matrix of P(12)Q(47)-P(47)Q(12), with rows V and
columns V', is
\[
 \begin{pmatrix}
 56&19&54&75&75\\
 34&20&92&9&3\\
 3&42&87&7&86\\
 70&77&95&80&84\\
 12&2&20&95&67
 \end{pmatrix}.                                      \tag{7}
\]
For example its first entry is 22*38-64*91=56 mod 97; the same
two-by-two determinant formula gives all 25 displayed entries.
Every entry is nonzero (their product is 67 mod 97). Hence no possible
tag pair for this mandatory edge satisfies (4). Nonzero F_97 elements
remain nonzero in F, proving the labeling exclusion for arbitrary
extension-field weights without needing an actual pencil construction.

The complete exact arithmetic certificate, including the values and
all 25 entries of (7), is
`scripts/exceptional-five-label/paired-label-test-result.json`.
Reproduce with `python3 scripts/exceptional-five-label/paired_label_test.py`.
Root-product evaluations are independently cross-checked by coefficient
expansion and Horner evaluation. Inspect the complete load-bearing
table with `python3 ../scripts/loop/inspect_json.py scripts/exceptional-five-label/paired-label-test-result.json --pointer /tests/1 --full`.
The script also records the other nine edge tests for this labeling;
they are unnecessary to this proof. The proof uses the complete table
above, not a sample, truncated preview or asserted exhaustive labeling
search. Actual minimum candidates for the chosen edge is zero; the
necessary threshold is at least one.

The new constraint reduces this exceptional completion branch to two
edge matchings and ten exact compatibility tests. It excludes one
labeling allowed by the involution condition, leaving other labelings,
possible repeated tag pairs, the original excluded point, full weights,
locators and same-support conditions to be checked. It does not improve
the global interval 11/q–16/q. The all-disjoint branch, universal cluster
extraction, challenge identification and stronger-source overlap remain
unresolved. The unchanged EXPLORE review permits this intermediate
obstruction; POTENTIALLY_NEW records unmatched coverage in the sources
checked, not certified originality. Needed earlier uses were inspected;
this and the unaudited conditional inputs require separate critical
review before any claimed completed resolution.

## Mathlib

Coverage of the full conditional completion restriction and exact
labeling exclusion is **not checked**. Supporting matching, polynomial,
finite-field and determinant results have not been looked up here.
No absence or formal-verification claim is made. All load-bearing
informal arguments and finite arithmetic values are given above.
