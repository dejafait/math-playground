# L065 — Triangle both-zero supports and simultaneous recovery bound

## Hypotheses

Use audited L057's full hypotheses: F=F_(97^20), H the order-sixteen
subgroup of F_97^*, C=RS[F,H,8], and the pinned four-omission cell.
The nine triangle labels are distinct, the original finite gamma_i are
distinct, lambda!=0, and p(1-p)q(1-q)r(1-r)!=0. No descent of weights
or original parameters is assumed. Retain all relaxed fourth weights
and the exclusions mu!=0,-1 and E!=0 of L057.

Write P={a,b,c}, and introduce monic pair polynomials (different from
L057's moment vectors Y and Z)
\[
 Y_2=(X-y_1)(X-y_2),\quad Z_2=(X-z_1)(X-z_2),\quad
 W_2=(X-w_1)(X-w_2),\quad S=Y_2Z_2W_2.
\]
Put V=H minus U, so |V|=7. For a four-subset K disjoint from P, let
f_K=product_(k in K)(X-k). A support is **both-zero** precisely when
both scalar projected vectors in L057 (5) vanish. By L057 every
both-zero support is disjoint from P, so this definition covers all of
them. Define R_00 to be the distinct additional original finite
parameters recovered on such supports, with every L057 lift gate still
imposed. Zero recovered fourth weights remain admitted.

## Conclusion

The exact projected classification is
\[
 K\text{ is both-zero}\quad\Longleftrightarrow\quad
 f_K\in\operatorname{span}_{F_{97}}\{Z_2W_2,Y_2W_2,Y_2Z_2\}.       \tag{1}
\]
Such a K contains either both or neither labels of each singleton pair.
A K containing two singleton pairs has no gated recovery. Every other
both-zero support is either one singleton pair plus a two-subset of V,
or a four-subset of V.

If Y_2,Z_2,W_2 are linearly independent as quadratics, there are at most
three projected candidate supports of the first type for each fixed
singleton pair, and at most two of the second type. Consequently
\[
                         |R_{00}|\le5.                         \tag{2}
\]

If they are dependent, write uniquely W_2=alpha Y_2+beta Z_2, with
alpha,beta!=0 and alpha+beta=1. On V take the fibers of
\[
                       h\longmapsto[Y_2(h):Z_2(h)].             \tag{3}
\]
Every fiber has at most two elements. Let B_1,...,B_m be exactly its
two-element fibers; m<=3. The projected candidates not containing two
original singleton pairs are exactly
\[
 \{y_1,y_2\}\cup B_i,\quad\{z_1,z_2\}\cup B_i,\quad
 \{w_1,w_2\}\cup B_i,\quad B_i\cup B_j\ (i<j).                 \tag{4}
\]
Their number is 3m+binom(m,2)<=12, and
\[
                 |R_{00}|\le3+\binom m2\le6.                   \tag{5}
\]
All candidate counts precede the restored equations and weight gates;
(1) and (4) do not assert actual recoveries. At fixed gated weights and
in a fixed original chart, at most one distinct additional parameter
has a both-zero support containing any specified singleton pair.
This last fact is used in (2) and (5), instead of counting all candidate
supports as simultaneous parameters.

Thus seven distinct disjoint-P recovery scalars, if present, cannot all
come from both-zero supports. The isolated rows and their interaction
with these supports remain uncontrolled. This is a partial restriction
toward the twelve bound, not that bound or a global improvement. Its
separate critical audit found no mathematical defect in this scope.

## Proof

### Inputs and purpose of the specialization

Use L010's independence of every set of at most eight moment columns,
audited L041's kernel vector on U, and audited L057's exact projected
criterion and original-chart recovery. Their standard RS/GRS and
recurrence inputs are already imported there, with the precise citations
to Hall, *Notes on Coding Theory*, GRS chapter, Theorem 5.1.1,
[author chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
printed pp. 63–64; Marquez-Corbella–Pellikaan, FFAA 40 (2016),
section 5, Lemma 5.3 and the following shortening formula,
[accepted manuscript dated 2016-02-29](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
printed pp. 7–8; and Chojecki, *Shortening Bounds for Reed–Solomon
MCA*, [author TeX v9.2](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex)
dated July 17, 2026, DR2 and DR6–DRC, source lines 2785–2935.
The mutable Chojecki source is not certified identical to ePrint
2026/1463. No general distance, shortening or recurrence
theorem is reproved. The ready triangle-count assessment supplies no
simultaneous both-zero count. The new work here is the six-evaluation
specialization and its support geometry. L064 is not assumed: the
short common-pair argument is given below so that this restriction does
not depend on its pending audit.

### Six singleton evaluations

Let G_P=product_(x in P)(X-x) and Q=product_(h in V)(X-h), as in
L057. Since H is precisely the simple zero set of X^16-1, at every
singleton x,
\[
 16x^{15}=Q(x)G_P(x)S'(x),\qquad
                c_x xG_P(x)=16/S'(x).                         \tag{6}
\]
All differences and 16 are nonzero in F_97, and x^16=1. By L057,
both-zero implies m=3. Its two projected equations are therefore
\[
 \sum_{y\in\{y_1,y_2\}}f_K(y)/S'(y)=0,\qquad
 \sum_{z\in\{z_1,z_2\}}f_K(z)/S'(z)=0.                         \tag{7}
\]
Apply the standard named Lagrange interpolation formula on the six
distinct singleton labels to a polynomial f of degree at most four:
\[
        f(X)=\sum_{s:S(s)=0}\frac{f(s)}{S'(s)}\frac{S(X)}{X-s}.
                                                                    \tag{8}
\]
The coefficient of X^5 is zero on the left, so the six ratios sum to
zero. Thus (7) also forces the W-pair sum to vanish. In each pair
(s_1,s_2), write the two ratios as t and -t. Its contribution in (8) is
\[
 t\left(\frac{S}{X-s_1}-\frac{S}{X-s_2}\right)
          =t(s_1-s_2)\frac{S}{(X-s_1)(X-s_2)}.                  \tag{9}
\]
This proves the forward direction of (1). Conversely, each of the
three product quadratics has opposite f(s)/S'(s) values on its omitted
pair and zero values on the other two pairs, as (9) or (8) shows.
Every linear combination therefore satisfies (7). This proves (1)
in both directions, over F_97 as stated (and over F as well).

The three product polynomials in (1) are independent: evaluation at
y_1 forces the coefficient of Z_2W_2 to be zero in any zero linear
combination; evaluation at z_1 and w_1 forces the other coefficients
to be zero. The respective products are nonzero at these labels.
In (7) and its W counterpart, one zero evaluation forces the other
evaluation in the same pair to be zero. Since f_K has precisely its
four distinct roots K, singleton labels enter K in complete pairs.

### Two original singleton pairs cannot pass the lift

Let bold Y,bold Z,bold W be the three moment sums with coefficients
c_x on their singleton pairs, and v_x the moment columns. L041 gives
\[
       \boldsymbol Y+\boldsymbol Z+\boldsymbol W
                          +\sum_{x\in P}c_xv_x=0.              \tag{10}
\]
For a both-zero K, L057's restored vectors satisfy
bold Y+sum beta_x^Y v_x in span(K), and similarly for Z. Define
beta_x^W=c_x-beta_x^Y-beta_x^Z; (10) supplies the same restored
membership for W. If the corresponding singleton pair is contained
in K, all its beta entries are zero: its recurrence is zero, and the
three restored recurrence columns are independent by L057 (19).

For K equal to the Y and Z pairs, beta^Y=beta^Z=0, so L057 (10)
at b forces q=0 (mu!=0). For the Y and W pairs,
beta^Y=beta^W=0 and hence beta^Z=c, so the c equation forces r=1.
For the Z and W pairs, beta^Z=beta^W=0 and beta^Y=c, so the b
equation forces q=1. Each contradicts a retained weight gate. These
are all two-pair possibilities.

### One-pair supports

If K contains the Y pair, evaluation at that pair in (1) forces its
Z_2W_2 coefficient to vanish. Dividing by Y_2 gives
\[
              f_K/Y_2\in\operatorname{span}\{Z_2,W_2\}.        \tag{11}
\]
Conversely (11) makes K both-zero. The two residual roots must lie
in V after the preceding two-pair exclusion. At h in V the ratio
Z_2(h)/W_2(h) is defined and nonzero. Equation (11) requires the
two residual labels to have the same ratio. Every such fiber has
at most two labels, because Z_2-tW_2 is a nonzero polynomial of
degree at most two: distinct monic quadratics with disjoint roots
cannot be proportional. Distinct two-label fibers are disjoint, so
there are at most floor(7/2)=3 residual pairs. The proof for the Z
and W pairs exchanges the names and uses the identical nonzero
denominators. This is a projected support count, not a lift count.

### Independent quadratics: at most two supports entirely in V

Assume Y_2,Z_2,W_2 are independent. At h in V put
\[
                e(h)=[Z_2(h)W_2(h):Y_2(h)W_2(h):Y_2(h)Z_2(h)].
                                                                    \tag{12}
\]
These projective points are distinct for distinct h. Indeed, taking
coordinatewise reciprocals, with nonzero coordinates, recovers
[Y_2(h):Z_2(h):W_2(h)]. Independence means the coefficient matrix
of the three quadratics is invertible, so equality of these latter
points implies [1:h:h^2]=[1:h':h'^2], and hence h=h'.

Every both-zero K contained in V corresponds via (1) to a nonzero
coefficient vector, whose projective line contains e(h) for all h in
K. Distinct K give distinct lines: the product-polynomial basis is
independent, and proportional quartics with monic normalization have
the same roots. Two distinct lines meet in only one projective point,
so any two such K intersect in at most one label. Their sizes four
inside a seven-set force intersection exactly one. Their complements
in V are therefore disjoint triples. Three such complements would
require nine distinct labels, so there are at most two K. This
argument uses projective linear algebra, not sampled labels.

### Dependent quadratics: the complete fiber family

Y_2 and Z_2 are independent, since they are distinct monic
quadratics. Dependence gives W_2=alpha Y_2+beta Z_2, with
alpha+beta=1 from leading coefficients. Neither coefficient is zero,
since W_2 has roots disjoint from both other pairs. For a coefficient
triple (A,B,C), its quartic in (1) becomes
\[
 A Z_2W_2+B Y_2W_2+C Y_2Z_2
   =B\alpha Y_2^2+(A\alpha+B\beta+C)Y_2Z_2+A\beta Z_2^2.       \tag{13}
\]
The change between these coefficient triples and binary quadratics
in Y_2,Z_2 is invertible: the square coefficients recover B and A,
then the mixed coefficient recovers C. Thus a nonzero quartic
corresponds to a nonzero homogeneous binary quadratic. It vanishes
on at most two values of [Y_2(h):Z_2(h)] in P^1(F_97). Each such
value has at most two preimages in V, since its fiber equation is a
nonzero polynomial of degree at most two. A quartic with four
distinct roots in V must therefore use exactly two two-element
fibers, and contains both entire fibers.

Conversely any two different two-element fibers in V are the roots
of two nonproportional quadratics in span{Y_2,Z_2}. Each quadratic
has degree exactly two because it has two distinct roots; their
product, with monic normalization, is f_(B_i union B_j). By (13)
the product lies in the net (1). This proves the last family in (4).

For a one-pair support, the other two pair quadratics span exactly
span{Y_2,Z_2}: alpha,beta!=0. Condition (11) therefore says precisely
that its residual roots form a two-element fiber (3). The same
argument gives all three first families in (4). There are no other
candidate shapes by the complete-pair property. Fiber disjointness
gives m<=3 and the asserted candidate count. No lift has been inferred.

### Simultaneous parameters and all gates

Suppose two distinct additional original finite parameters T,T' have
relaxed witnesses K,L containing the same singleton pair B. Let e_i
be the actual base error whose support A_i contains B. Its weight at
each of the two P labels in A_i is nonzero by the weight gates.
The three syndrome values at gamma_i,T,T' are affinely dependent,
with respective coefficients T-T', T'-gamma_i, gamma_i-T, all
nonzero. Hence
\[
          (T-T')e_i+(T'-\gamma_i)e_K+(\gamma_i-T)e_L             \tag{14}
\]
is in the moment kernel. Its support lies in A_i union K union L,
which has size at most eight: K and L share B, and A_i adds at
most its two P labels. At either such P label both relaxed errors
vanish, whereas the base term is nonzero. This is a nonzero kernel
word on at most eight labels, contradicting L010. Zero recovered
weights and K=L cause no exception to this argument. Therefore at
most one distinct parameter belongs to each singleton-pair category.

L057 admits at most one eligible scalar, and hence one original
finite parameter, for each both-zero K at fixed gated weights.
The independent case consequently has at most three pair-category
parameters plus two entirely-V parameters. The dependent case has
at most three pair-category parameters plus binom(m,2) entirely-V
parameters. Taking a union can only reduce these bounds, so (2)
and (5) hold even if witnesses have zero weights or are duplicated.
All parameters used in (14) are actual, finite and distinct and have
passed mu!=0,-1 and E!=0. Removing an original infinity or any other
failed gate can only lower the count. No rational original chart or
weight descent was used.

### Separate critical audit (2026-10-11)

The audit checked the entire classification and both parameter bounds
against L010's moment-kernel proof, L041's local-converse statement and
shortening specialization, and L057's full symbolic recovery argument.
L041's equality hypotheses are not assumed: its local converse supplies
the three full base errors and actual affine syndrome pencil used here.
L060–L064 and the two selected algebra regressions are not inputs.
The following checks verify the potentially exceptional cases.

**Normalization and exact net.** The nine-label union and its complement
partition H, so Q G_P S=X^16-1. Differentiating at a singleton x gives
Q(x)G_P(x)S'(x)=16x^15; multiplying by x and using x^16=1 gives
(6), with c_x=Q(x). Thus the two scalar equations in L057 (5) for
m=3 are exactly 16 times (7). No unknown weights occur in these tests.
The degree-five coefficient in the six-node interpolation formula is
the sum of all six ratios, so the third pair sum vanishes as well.
The sign in (9) is s_1-s_2. Its coefficients are in F_97 since the
labels and monic f_K are in that field. Conversely each product has
zero values on two pairs and opposite ratios on the remaining pair.
Evaluation at one label in each omitted pair proves independence of
the three quartic products, even when the pair quadratics are dependent.
This verifies (1) over F_97 and its extension-field interpretation.

**Shapes and restored exclusions.** A zero at one singleton forces a
zero at its partner. Four distinct roots therefore allow exactly two
original pairs, one pair plus two labels in V, or four labels in V.
There are no missing mixed shapes. In the both-zero case all P labels
are absent from K. L057 (19) has rank three, so a pair contained in K
has identically zero restored beta vector. Relation (10) then gives
beta^W=c-beta^Y-beta^Z, with the stated sign. For Y+Z the b equation
is -mu*c_b*q=0, forcing q=0. For Y+W the c equation is c_c*r=c_c,
forcing r=1. For Z+W the b equation is -mu*c_b*q=-mu*c_b,
forcing q=1. These exhaust the two-pair cases and use only retained
nonzero c_x, mu and the base weight gates; no fourth weight is divided
out. For a one-pair support the remaining quadratic belongs exactly
to the other two quadratics' span. Its ratio denominator has no zero
on V. Distinct monic quadratics with disjoint root pairs cannot be
proportional, so every fiber equation is nonzero of degree at most two.
The bound three counts disjoint two-label fibers, including in the
independent branch, without asserting that any passes the lift.

**Independent branch.** All coordinates of e(h) are nonzero on V;
coordinatewise inversion gives [Y_2(h):Z_2(h):W_2(h)]. The invertible
quadratic coefficient matrix identifies this with [1:h:h^2]. Thus
different labels give different projective points, over F as well as
over F_97. A nonzero quartic in the net determines a line; two different
supports determine different lines by independence of the quartic
products and monic normalization. Two such lines share at most one
of these points. Two four-subsets of a seven-set share at least one
label, so their intersection is exactly one and their three-element
complements are disjoint. Three distinct supports would require three
pairwise-disjoint triples in V, which has size seven. This proves the
bound two without any generic-position assumption.

**Dependent branch and exceptional fibers.** The unique relation
W_2=alpha Y_2+beta Z_2 is defined over F_97: Y_2,Z_2 are independent
prime-field coefficient vectors. Disjoint root pairs force alpha and
beta nonzero, and monicity gives alpha+beta=1. Formula (13) is an
invertible change of three coefficients: its outer coefficients are
B*alpha and A*beta, with C then determined by the mixed coefficient.
Consequently no nonzero net polynomial is represented by the zero
binary quadratic. A nonzero homogeneous binary quadratic has at most
two distinct zeros on P^1, including a possible zero at infinity.
Here Y_2 and Z_2 have no zeros on V, so the values [0:1] and [1:0]
are absent; the W_2-zero value is absent as well. Every other fiber
is defined by a nonzero polynomial in span{Y_2,Z_2} of degree at most
two. If leading terms cancel, the degree is at most one and it cannot
contain two distinct labels; a double root also gives at most one label.
Thus four distinct V roots require two distinct projective values,
each with exactly two labels. A repeated root of the binary quadratic
cannot supply four distinct labels. Conversely two such fibers have
coprime degree-two defining polynomials, whose product has exactly
their four distinct roots; monic normalization and (13) place it in
the net. For each original singleton pair, the other two quadratics
span the same pencil, so precisely the same two-element fibers give
its possible residual pairs. This proves every inclusion in (4);
degree loss, infinity and multiplicities introduce no further supports.

**Actual parameters, pivots and deduplication.** For two additional
finite parameters with witnesses containing a fixed singleton pair B,
the corresponding base support is B plus two P labels. The witnesses
miss P and have union size at most six, so (14) has support of size
at most eight. Its moment is zero because the coefficients sum to zero
and their parameter-weighted sum is zero. At either base P label its
coefficient is (T-T')e_i(x), nonzero since T!=T' and the base weight
is nonzero. L010's eight-column independence therefore contradicts
such a pair of parameters, even if K=L or recovered coefficients vanish.
This checks the category bound on parameters, rather than witnesses.

For one both-zero support, L057's restored system is A+mu B=0.
If all B entries vanish it is inconsistent: all A entries cannot also
vanish, since that would put the full base error e_0 in the disjoint-P
K span, contradicting sparse-error uniqueness. Otherwise a nonzero
pivot fixes at most one mu over F; the other equations and all gates
still apply. For eligible mu, E!=0 and T=gamma_0+g*rho/E. Equality
of two T values implies equality of E, since g*rho!=0, and then
equality of mu, since rho!=1. L057's bijection also excludes every
base parameter using mu!=0,-1. It verifies all eight moments and
same-support failure even for relaxed weights. These facts justify
at most one actual parameter per entirely-V support, three parameters
over the pair categories, and the bounds 3+2 and 3+binom(m,2).
Coincident witnesses or parameters only decrease these union bounds.
Neither nonprime weights nor an original nonprime chart changes them.

No formula, bound or direct mathematical dependency required repair.
The audit validates this existing partial input, not a new stronger
bound or certified originality. The uniform twelve target and the
other independent gaps remain open. No computational certificate is
needed for any of the uniform arguments above.

## Mathlib

The full matching classification and bounds are **not checked** in
Mathlib. Lagrange interpolation, polynomial root bounds, Vandermonde
independence and projective linear algebra are supporting mathematics;
their exact Mathlib theorem names are not checked here. No absence or
formal-verification claim is made. The ready literature comparison
did not establish a matching import; that is not certified originality.
