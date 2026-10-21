# L057 — Exact fourth-support recovery for a tau-zero triangle

## Hypotheses

Let F=F_(97^20), let H be the order-sixteen subgroup of F_97^*,
and let C=RS[F,H,8]. Use L010's shifted moments
sigma_j(e)=sum_(x in H) e(x)x^j, j=1,...,8, and the pinned cell
1/4<=delta<5/16. Take audited L041's **local converse**, without
assuming sixteen-count equality. Name its triangle supports
\[
 A_0=\{a,b,y_1,y_2\},\quad A_1=\{a,c,z_1,z_2\},\quad
 A_2=\{b,c,w_1,w_2\},                                  \tag{1}
\]
with nine distinct labels in H. Write P={a,b,c},
U=A_0 union A_1 union A_2, Q(X)=product_(h in H minus U)(X-h),
and c_x=Q(x) for x in U. Thus c_x is in F_97^*; the label c
and the indexed coefficient c_x are different objects. Put
v_x=(x,x^2,...,x^8)^tr.

Take three distinct original finite parameters gamma_0,gamma_1,gamma_2
in F, alpha_0=gamma_1-gamma_2, alpha_1=gamma_2-gamma_0,
alpha_2=gamma_0-gamma_1, and lambda in F^*. The normalized weights
on the shared coordinates, in L041's notation, are
\[
 \begin{array}{c|ccc}
  &a&b&c\\ \hline
  e_0& p&q&0\\
  e_1&1-p&0&r\\
  e_2&0&1-q&1-r
 \end{array}                                          \tag{2}
\]
where an entry for e_i at x denotes the actual weight
lambda*c_x times that entry divided by alpha_i. The two singleton
entries of each e_i are one in this normalization. Retain exactly
\[
       p(1-p)q(1-q)r(1-r)\ne0.                       \tag{3}
\]
All p,q,r,lambda and original parameters range over F. Let
s(T)=sigma(a_*)+T sigma(b_*) be the actual syndrome pencil with
s(gamma_i)=sigma(e_i). L041 supplies independence of its two coefficient
syndromes, nonzero D, and all nonpersistent coordinate locators because
tau=0. No prime-field chart, descent, equality or global extraction is
assumed. The names a_*,b_* for input words are distinct from labels a,b.

Fix any four-subset K of H different from A_0,A_1,A_2. We allow
vanishing recovered weights before imposing the full-four-error gate.
Define
\[
 g=\gamma_1-\gamma_0,\quad \rho=(\gamma_2-\gamma_0)/g,
 \quad t=(T-\gamma_0)/g,\quad
 Y=\sum_{y\in\{y_1,y_2\}}c_yv_y,\quad
 Z=\sum_{z\in\{z_1,z_2\}}c_zv_z.                     \tag{4}
\]
Here g!=0 and rho is not 0 or 1. Put f_K(X)=product_(k in K)(X-k),
J=P minus K, m=|J| in {0,1,2,3}, and
G_J(X)=product_(x in J)(X-x), including G_empty=1.

The following explicit vectors of length 4-m use only the labels:
\[
 \begin{split}
  \mathbf y_j&=\sum_{y\in\{y_1,y_2\}}
          c_y y f_K(y)G_J(y)y^j,\\
  \mathbf z_j&=\sum_{z\in\{z_1,z_2\}}
          c_z z f_K(z)G_J(z)z^j,
             \qquad 0\le j\le3-m.                   \tag{5}
 \end{split}
\]
For each x in J define the label polynomial
\[
 \ell_x(X)=\prod_{u\in J\setminus\{x\}}\frac{X-u}{x-u}
\]
and the two explicit scalars
\[
 \begin{split}
  \beta_x^Y&=-\frac{\sum_{y\in\{y_1,y_2\}}
                           c_y y f_K(y)\ell_x(y)}{x f_K(x)},\\
  \beta_x^Z&=-\frac{\sum_{z\in\{z_1,z_2\}}
                           c_z z f_K(z)\ell_x(z)}{x f_K(x)}.
                                                            \tag{6}
 \end{split}
\]
Every denominator in (6) is nonzero. All data in (5)–(6) lie in F_97.
There are no beta scalars when J is empty. Although (6) is always
defined, an individual beta^Y or beta^Z need not solve all four
recurrence rows unless its corresponding vector in (5) vanishes.

## Conclusion

The following is an exact test for a relaxed representative supported
in K at an original finite T different from all three gamma_i.
It retains every projected rank and recovers all eight moments.

**Projected test.** If exactly one vector in (5) is zero, or both
nonzero vectors are independent, there is no eligible recovery.
If both are nonzero and proportional, write uniquely
\[
        \mathbf z=\mu\mathbf y,\qquad\mu\in F_{97}^*.
                                                            \tag{7}
\]
Use that one mu, excluding mu=-1 and
\[
                    E=\rho-(1-\rho)\mu=0.             \tag{8}
\]
For both-zero vectors, m=3 necessarily. Form the three scalar pairs
\[
 \begin{array}{c|cc}
 x&A_x&B_x\\ \hline
 a&c_a(1-p)-\beta_a^Z&-c_a p+\beta_a^Y\\
 b&-\beta_b^Z&-c_b q+\beta_b^Y\\
 c&c_c r-\beta_c^Z&\beta_c^Y
 \end{array}.                                         \tag{9}
\]
The six entries in (9) cannot all be zero under (3). If all B_x
are zero there is no recovery. Otherwise choose any x with B_x!=0,
set mu=-A_x/B_x, and require every A_u+mu B_u=0 for u in P.
Exclude mu=0, mu=-1 and E=0. These tests are independent of the
chosen nonzero pivot. The mu in this both-zero case may belong to F
outside F_97. In particular, a both-zero quotient is never declared
a common intersection without this lift. The candidate is unique
in this case as well.

**Recover all lost coefficients.** In either surviving case require
exactly the following equations for labels missing from K:
\[
 \begin{cases}
 c_a[1-(1+\mu)p]=\beta_a^Z-\mu\beta_a^Y,&a\in J,\\
 -\mu c_b q=\beta_b^Z-\mu\beta_b^Y,&b\in J,\\
 c_c r=\beta_c^Z-\mu\beta_c^Y,&c\in J.
 \end{cases}                                          \tag{10}
\]
They are already imposed by (9) in the both-zero case. Do not impose
an absent equation for a label contained in K. For the isolated
case (7), these are explicit affine conditions on the three free
weights. Equivalently, where the respective label is in J,
\[
 \begin{split}
 p&=\frac{1-(\beta_a^Z-\mu\beta_a^Y)/c_a}{1+\mu},\\
 q&=\frac{\beta_b^Y-\beta_b^Z/\mu}{c_b},\\
 r&=\frac{\beta_c^Z-\mu\beta_c^Y}{c_c}.                \tag{11}
 \end{split}
\]
Thus an isolated recovery with K disjoint from P forces all three
normalized pair weights into F_97, without rationalizing the original
parameters, lambda or excluded direction. Conditions (3) still apply.

**Recover the fourth error.** For every surviving mu, the original
finite parameter and the syndrome numerator are
\[
 \begin{split}
 T_K&=\gamma_0+g\rho/E,\\
 N_K&=Z-\mu Y+c_a[1-(1+\mu)p]v_a-\mu c_b q v_b+c_c r v_c.
                                                            \tag{12}
 \end{split}
\]
For xi in K put
L_xi(X)=product_(k in K minus {xi})(X-k)/(xi-k). Define
\[
 \begin{split}
 \omega_\xi=\xi^{-1}\bigg[&
   \sum_{z\in\{z_1,z_2\}}c_z z L_\xi(z)
  -\mu\sum_{y\in\{y_1,y_2\}}c_y y L_\xi(y)\\
 &+c_a[1-(1+\mu)p]a L_\xi(a)
   -\mu c_b q b L_\xi(b)+c_c r c L_\xi(c)\bigg].       \tag{13}
 \end{split}
\]
Then the unique representative supported in K has actual weights
\[
                 e_K(\xi)=\frac{\lambda}{gE}\omega_\xi.
                                                            \tag{14}
\]
These satisfy all eight moments, including when some weights vanish.
It is a full four-error on exactly K iff
product_(xi in K) omega_xi!=0. A failed full-weight gate is retained
as a relaxed lower-weight recovery, not counted as a full K error.
Every admitted recovery is bad on the same twelve-coordinate
complement H minus K for the pinned event. Distinct witnesses K
for a lower-weight parameter are not asserted to be distinct parameters.

For clarity, rank of the eliminated-column system is always m, with
no exceptional label-dependent drop. When m<=2, y=0 iff both y labels
are in K, and z=0 iff both z labels are in K. When m=0 the two vectors
are necessarily nonzero and independent, so there is no recovery.
When m=3, (5) consists of one explicit scalar for each singleton pair;
it permits cancellations outside K and (9) handles them fully.
No classification or count of such label choices is claimed.

This is a local reproduction/specialization of the assessed recurrence
and quotient mechanism. It supplies explicit label tests, pair-weight
equations and finite recovery, not an additional-parameter bound,
universal extraction, a challenge solution or a certified originality
claim. A separate critical audit on 2026-10-10 found no mathematical
defect in this local criterion; it supplies no simultaneous count.

## Proof

### Imported input and the actual original-chart pencil

Import Przemek Chojecki, *Shortening Bounds for Reed–Solomon MCA*, live
author TeX v9.2, dated July 17, 2026, reinspected 2026-10-10, source
lines 2785–2935: `drc:lem-locator-recurrence` (DR2) and
`drc:thm-exact-compiler` (DR6–DRC), including both full proofs and
zero-direction cases, in the
[author source](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex).
The mutable source is not certified identical to ePrint 2026/1463.
DR2 covers distinct weighted Vandermonde columns with nonzero
multipliers, redundancy R and support size t<R. Specialize R=8,
t=4, eta_j=s_(j+1) for j=0,...,7 and multiplier x at each x in H.
There is no subfield hypothesis on the syndrome. If
f_K(X)=sum_(j=0)^4 f_j X^j and
\[
        (\mathcal F_K n)_i=\sum_{j=0}^4 f_j n_{i+j}
                     \quad(1\le i\le4),
\]
the imported conclusion is
\[
 \mathcal F_K n=0\quad\Longleftrightarrow\quad
                    n\in\operatorname{span}_F\{v_x:x\in K\}.
                                                            \tag{15}
\]
The compiler gives full-recurrence finite intersection tests including
zero directions. It does not supply this triangle's quotient lift
or its equations in p,q,r. Those are the specialization below.
No general annihilator, distance or shortening theorem is reproved.
L010 supplies the shifted-moment kernel, eight-column independence,
sparse-error uniqueness and same-support facts; audited L041 supplies
the exact weights and nonpersistence in the triangle. L016 and L043
are methodological comparisons, not mathematical inputs to this proof.

From alpha_0=g(1-rho), alpha_1=g rho and affine interpolation of the
first two actual syndromes, obtain the identity
\[
 \frac{g}{\lambda}s(\gamma_0+gt)
 =\frac{1-t}{1-\rho}[Y+c_a p v_a+c_b q v_b]
   +\frac{t}{\rho}[Z+c_a(1-p)v_a+c_c r v_c].           \tag{16}
\]
Every denominator here is nonzero. This is a computation in the
original affine pencil, not a claim that the original chart is rational.
Additional original finite parameters are exactly finite
t not in {0,1,rho}. For such t set
\[
 \mu=-\frac{\rho(1-t)}{(1-\rho)t}.
\]
This change of variable is a bijection between those eligible finite t
and finite mu in F with mu!=0,-1 and E=rho-(1-rho)mu!=0.
Indeed E=rho/t, t=rho/E, mu=0 corresponds to t=1, and mu=-1
corresponds to t=rho. Conversely rho!=0 and rho!=1 ensure the
inverse avoids all three selected parameters. Substitution into (16)
gives
\[
                  \frac{gE}{\lambda}s(T_K)=N_K.        \tag{17}
\]
Thus E=0 is an excluded point at original infinity; it is not counted.

### Explicit quotient, exact ranks and all projected cases

For any label x the recurrence column is
\[
 \mathcal F_K v_x=f_K(x)(x,x^2,x^3,x^4)^{tr}.           \tag{18}
\]
It vanishes exactly for x in K. The nonzero columns at P are precisely
those at J. Their first m rows have determinant, for any ordering of J,
\[
       \left(\prod_{x\in J}x f_K(x)\right)
                \prod_{x<u\text{ in that ordering}}(u-x)\ne0.
                                                            \tag{19}
\]
For m=0 use the empty invertible matrix. Therefore the 4-by-m matrix
C_J of these columns has rank m over the prime field and over F.

A row functional on these four recurrence entries corresponds to a
polynomial h(X) of degree at most three: its value on (18) is
x f_K(x)h(x). Annihilating every nonzero column at J is equivalent
to h vanishing on J, hence to h=G_J(X)k(X), deg k<=3-m.
The polynomials G_J(X)X^j, j=0,...,3-m, are an explicit independent
basis. Their corresponding row matrix B has rank 4-m, annihilates
C_J, and has kernel exactly im(C_J) by dimensions. Applying these
rows to mathcal F_K Y and mathcal F_K Z gives precisely (5).
This establishes the quotient without assuming a generic rank.

The P terms in (16) vanish after this quotient, so projected
compatibility is exactly
\[
             \rho(1-t)\mathbf y+(1-\rho)t\mathbf z=0,
\]
or, at eligible t, z-mu y=0. If y=0,z!=0 it forces t=0;
if z=0,y!=0 it forces t=1. Independent nonzero vectors give no
solution. For dependent nonzero vectors, a nonzero coordinate of y
gives the unique ratio (7), in F_97^* since both vectors have
prime-field coordinates. Hence (7)–(8) are the complete projected
test in this case. If both vectors vanish, the quotient imposes
no restriction on mu; the lift must still be checked.

The useful zero classification for m<=2 follows from L010's
independence on every set of at most eight moment columns. If y=0,
then mathcal F_K Y lies in im(C_J), so (15) puts Y in the span
of the columns indexed by K union P. Any resulting relation is
supported on K union P union {y1,y2}, with size at most
4+m+2<=8. Thus every y label outside K union P would have its
nonzero coefficient c_y in an impossible relation. Since no y
label is in P, both must lie in K. The converse follows from
mathcal F_K Y=0. The identical argument applies to Z. Both zero
would therefore force K={y1,y2,z1,z2}, which misses all three P
labels and has m=3, a contradiction to m<=2. This proves that
the both-zero case in (9) always has m=3.

When m=0, K contains all of P and only one other label. Neither
singleton pair is contained in K, so neither vector is zero. If
they were proportional, Z-mu Y would be in the K span by (15).
The resulting relation is supported on at most the eight labels
K union {y1,y2,z1,z2}. At least one y or z label is outside K,
with nonzero coefficient, contradicting the same independence.
Thus this case has no eligible recovery. When m=3 no such
eight-column argument is available; retain the explicit scalar
tests and their cancellations, rather than transferring the
tau=1 universal-support classification.

### Recovering all eliminated coefficients

Suppose the projected tests permit a particular mu. Then
mathcal F_K(Z-mu Y) lies in im(C_J). There is a unique beta with
\[
               C_J\beta=-\mathcal F_K(Z-\mu Y).        \tag{20}
\]
The first m rows determine it by (19). To evaluate it without an
unspecified linear solve, write ell_x(X)=sum_(j=0)^(m-1) ell_(x,j)X^j.
For unknown beta_u, the first m entries of C_J beta are
sum_(u in J) beta_u u f_K(u) u^j, j=0,...,m-1.
Their linear combination with the coefficients ell_(x,j) equals
beta_x x f_K(x), since ell_x(u) is one at u=x and zero at the
other J labels. Applying that same combination to the right side
of (20) gives exactly
\[
                   \beta_x=\beta_x^Z-\mu\beta_x^Y,    \tag{21}
\]
with (6). Because the full solution exists, its first-row solution
also satisfies every remaining recurrence row. This justifies (21)
even when beta^Y and beta^Z separately solve only their first m rows.
For J empty, projected compatibility already means the residual
recurrence is zero and no coefficients need recovery.

In N_K the actual P coefficients are the three displayed in (12).
Columns belonging to P intersect K are zero in its recurrence.
Independence of the remaining columns makes mathcal F_K N_K=0
equivalent to matching each remaining actual coefficient with (21).
These are precisely (10), so the lift is both necessary and sufficient.
The optional rearrangements (11) divide only by nonzero c_x, mu
and 1+mu after their exclusions. In case (7) every scalar on the
right side is prime-field, proving the stated local rational-weight
restriction. It says nothing about the original affine chart.

If y=z=0, the separate full systems C_J beta^Y=-mathcal F_K Y
and C_J beta^Z=-mathcal F_K Z do exist; (6) therefore solves
both. Here m=3, so (10) is precisely (9)'s A_x+mu B_x=0.
If all A and B vanished, both vectors
\[
       Y+c_a p v_a+c_b q v_b,\qquad
       Z+c_a(1-p)v_a+c_c r v_c
\]
would satisfy the full recurrence and lie in the K span by (15).
The first is a nonzero scalar multiple of sigma(e_0). Sparse-error
uniqueness from L010 would force its full four-support A_0 to be K.
But K is disjoint from P while A_0 contains a,b. This contradiction
excludes the all-zero case. If all B vanish, some A is nonzero and
the system is inconsistent. Otherwise any nonzero B pivot determines
one mu, and checking the other two equations makes that value both
necessary and sufficient. The finite and selected-parameter exclusions
are still required. No zero projected direction has been discarded.

### Fourth weights, all moments and the same-support event

After (10), (15) supplies N_K=sum_(xi in K) omega_xi v_xi with
unique coefficients. They are determined by the first four moments
because the four-point shifted Vandermonde is invertible. Writing
L_xi(X)=sum_(j=0)^3 L_(xi,j)X^j and combining those first four
moment equations shows
omega_xi=xi^-1 sum_(j=0)^3 L_(xi,j)(N_K)_(j+1).
Substituting (12) is exactly (13). Since the full K-span assertion
was established before this four-moment recovery, these coefficients
satisfy all eight moments, not merely their first four. Equation (17)
then proves the actual scaling (14). Its factor lambda/(gE) is nonzero,
so full weight is exactly the stated product gate. There is no loss of
cases with vanishing fourth coefficients.

The kernel identity in L010 gives a_*+T_K b_*-e_K in C, hence
agreement on H minus K, of size twelve. If b_* restricted to that
same complement belonged to C restricted there, subtracting a
codeword would give f supported in K with sigma(f)=sigma(b_*).
Then the whole syndrome pencil would be in the K span because its
value at T_K is in that span. In particular e_0 would have a
representative supported in K of weight at most four. L010's
uniqueness forces that representative to equal e_0, so its full
four-support A_0 would be K, contrary to the hypothesis on K.
Thus input failure and agreement use the same twelve-coordinate
support even for a relaxed recovery with zero coefficients. This
verifies the pinned event rather than substituting closeness for
badness. The same conclusion holds for any words with this syndrome
pencil; adding codewords does not affect it.

Conversely, every representative supported in K at an eligible original
finite parameter supplies mu through (16), passes the projected test,
must satisfy (20) and (10), and has the weights (13)–(14) by uniqueness.
This completes necessity and sufficiency in every rank and finite case.
It is not a simultaneous count: in particular the m=3 quotient has
dimension one, so its generic proportionality leaves all three actual
pair equations essential. Counting, arbitrary-family extraction and
the other triple patterns remain open.

### Selected regression, not a uniform certificate

Run `python3 scripts/triangle-recovery/check_selected.py`. The complete
selected-pencil evidence is saved in
`scripts/triangle-recovery/selected-regression.json`. The three selected
prime-field gated pencils use gamma=(7,18,51), lambda=5 and free weights
(2,3,4), (96,86,63), (94,95,44). For each, all 1817 nonbase four-supports
and all 94 eligible parameters in F_97 were checked. The criterion's
predictions were compared against independently computed first-four
Gaussian recovery followed by every one of the eight moment equations.
Actual/required discrepancies are 0/0. The second pencil exercises an
isolated full-weight recovery; the third exercises a both-zero full lift
at K={18,22,64,89}, T=41, with weights (49,64,38,10) in that order.
The complete corresponding certificate row, including both projections,
both recovered beta vectors and both weight calculations, was inspected.
This is a formula regression only: it does not check every labeling,
extension-field weight, extension-field parameter or same-support gate
computationally. The symbolic proof above establishes those claims.
No uniform count or critical audit follows from this regression.

### Separate critical audit (2026-10-10)

The separate audit reused the approved SPECIALIZE scope and the inspected
primary inputs cited above. It checked the complete statement and proof,
L010's kernel and uniqueness before its global count, and audited L041's
local converse. No mathematical defect or missing premise was found.
This certifies the existing local reproduction, not a new count or an
advance beyond the inspected sources.

The principal checks were as follows.

- L041's converse, rather than its equality-conditioned necessary
  direction, provides (2)–(3), independence and tau=0 nonpersistence.
  Every alpha_i is nonzero and every singleton weight is nonzero.
  The imported recurrence has R=8, t=4, nonzero multiplier x and
  eta_j=s_(j+1); no prime-field syndrome assumption is introduced.
- In (16), alpha_0=g(1-rho) and alpha_1=g*rho have the stated signs.
  Direct substitution gives E=rho/t and (17). The inverse t=rho/E
  is nonzero; t=1 iff mu=0 and t=rho iff mu=-1. Thus the map excludes
  exactly the three base parameters and original infinity. Its scale
  lambda/(gE) is nonzero, even for nonrational rho and mu.
- For each m=0,1,2,3 the first m recurrence rows have nonzero determinant
  (19). Polynomial multiples G_J X^j form all 4-m quotient rows, so
  their common kernel equals the eliminated-column span over F as well
  as F_97. This verifies all ranks, not only generic label choices.
  When m<=2 the zero-vector argument uses at most 4+m+2<=8 distinct
  columns with a nonzero coefficient outside K. Both-zero therefore
  requires m=3. For m=0 a putative proportionality uses at most eight
  columns and also has a nonzero coefficient outside K, which is
  impossible. No nine-column independence is assumed in the m=3 case.
- Nonzero projected proportionality gives a unique prime-field ratio
  from a nonzero coordinate. Exactly-one-zero and independent systems
  cannot yield an eligible finite parameter. In the both-zero case the
  three affine lift equations are retained. If all six A,B entries
  vanished, the full A_0 syndrome would have a representative on the
  disjoint-from-P set K, contradicting uniqueness and its nonzero a,b
  weights. All B zero is consequently inconsistent if it occurs;
  otherwise one nonzero B pivot plus all residual equations is both
  necessary and sufficient. No common intersection is inferred merely
  from the zero quotient, and mu need not be prime-field here.
- Once projected compatibility holds, the full solution of (20) exists
  and is unique. Lagrange combinations of its first m rows give (21).
  It is the combined beta^Z-mu*beta^Y that solves every row; the proof
  never needs that assertion for each beta separately in the isolated
  case. Matching its entries with the actual P coefficients gives all
  and only (10). Rearrangement (11) divides only by quantities already
  excluded from zero. The rational-weight conclusion is restricted to
  isolated recoveries with all three shared labels absent.
- Full K-span membership is established before (13) solves the first
  four moments, so the recovered weights satisfy all eight. Vanishing
  weights cause no division or loss of necessity/sufficiency. If the
  direction word agreed on H minus K, the entire syndrome pencil
  would lie in the K span; uniqueness would then put the full A_0
  error on K, contrary to K!=A_0. This proves the same-support failure
  also for lower-weight recoveries and for any realizing input words.

The existing regression program was read in full and rerun. Each of its
three cases checks all 1817 nonbase supports at all 94 eligible prime-field
parameters by direct shifted-Vandermonde inversion followed by all eight
residual equations. Actual/required discrepancies were 0/0, with the
complete empty failures array inspected. Both complete positive rows were
inspected: case 1, row 1167 has K=(18,27,47,64), projected vectors (86),
(40), mu=14, T=67 and weights (75,23,30,22); case 2, row 1140 has
K=(18,22,64,89), both projections zero, T=41 and weights (49,64,38,10).
The first case has no positive row. All positive rows have full weights;
there is no claim that this regression exercises positive zero-weight or
extension-field recoveries. Those cases are covered by the symbolic
necessity/sufficiency proof, not by the finite replay. Certificate path
and reproduction command are in the preceding subsection.

The audit changes no formula or mathematical dependency. It establishes
neither a simultaneous parameter count nor extraction from arbitrary
equality families, and does not resolve the challenge-definition gap.

## Mathlib

The full triangle projected-label and finite recovery criterion:
**not checked**. Supporting polynomial root/divisibility facts,
Lagrange interpolation, Vandermonde independence, finite-field linear
algebra, shifted-moment kernel and locator recurrence: **not checked**
in Mathlib for this step. The informal proof uses L010, audited L041
and the precise recurrence citation above. No matching Mathlib theorem,
Lean verification, uniform finite certificate or certified originality is
claimed. The selected regression above is supporting verification only.
