# L104 — Seven-coordinate two-overlap recovery and simultaneous compatibility

## Hypotheses

Let F=F_(97^20), H the order-sixteen subgroup of F_97^*, and
C=RS[F,H,8]. Use the pinned same-support event on 1/4<=delta<5/16,
L010's shifted syndrome sigma, and the actual polynomials D and ell_x.
Initially assume all these polynomials are nonzero. Let a,b be arbitrary
words over F whose coefficient syndromes belong to U_S for a seven-set
S subset H. Put J=H\S. By L010's injectivity there is a unique affine
lift f(T)=u+Tv supported on S with sigma(f(T))=sigma(a)+T sigma(b).
Neither independence of the syndromes nor a rational original chart is
assumed. Constants and all cancellations are allowed.

For I subset S and K subset J with |I|=|K|=2, set

\[
 A=I\cup K,\qquad g_K(X)=\prod_{y\in J\setminus K}(X-y).
\]

In the equality conclusions assume |B(a,b)|=16 and all seven lift
coordinates active (not identically zero). The converse construction below
instead starts from the explicitly specified row data and proves actual
polynomial nonpersistence; it does not assume an equality pencil exists.

## Conclusion

For any original finite gamma, there is an error supported on A, allowing
zero weights, if and only if a scalar lambda satisfies

\[
 f_x(\gamma)=\lambda g_K(x)\quad(x\in S\setminus I).       \tag{1}
\]

The scalar is unique. The recovered error is

\[
 e_i=f_i(\gamma)-\lambda g_K(i)\ (i\in I),\qquad
 e_k=-\lambda g_K(k)\ (k\in K),                          \tag{2}
\]

and zero elsewhere. It is full on A exactly when lambda!=0 and both
displayed I-weights are nonzero. Every recovered parameter is in the
original bad set, including zero weights and lambda=0.

At equality, let t count actual errors equal to f at their parameters,
and n_m count the other errors with |supp(e) intersect S|=m. Then

\[
 0\le t\le2,\quad m\in\{0,1,2\},\quad
 2n_0+n_1=4+2t,\quad r:=n_2=12-3t+n_0\ge6.             \tag{3}
\]

All r two-overlap rows have a simultaneous reduction to an explicit
(5r-14)-by-r homogeneous matrix, defined in (4) below. Its kernel must
contain a vector with every entry nonzero and satisfying the recovered
I-weight gates. This eliminates all fourteen affine lift coefficients
and all four error weights per row. It is stronger data reduction than
independent eight-moment tests, but supplies no rank obstruction yet.

For prescribed distinct finite parameters and support rows of coordinate
degree at most four, those matrix and weight conditions are also sufficient
to construct a nonpersistent fully active seven-coordinate pencil realizing
all the rows in that finite chart. They do not construct its other required
equality events. The fifteen bound and the global 11/q–16/q interval remain
unresolved. The separate step-292 critical audit found no defect in
this partial reduction; its inherited computational qualifications remain.

## Proof

### Imported distance and shortening; exact one-row recovery

L010 gives ker(sigma)=C, injectivity on at most eight coordinates, unique
weight-at-most-four errors, the full original bad-event interpretation and
equality balance. Distance nine is the specialization of J. I. Hall,
*Notes on Coding Theory*, [GRS chapter, Theorem 5.1.1, pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
to sixteen distinct evaluation labels, unit multipliers and dimension
eight over F. The theorem permits any field and 0<k<=n; all hypotheses
hold. The ready assessment's inspected source is reused, not reread.

Import the single-coordinate shortening formula from I. Marquez-Corbella
and R. Pellikaan, *A characterization of MDS codes that have an error
correcting pair*, FFAA 40 (2016), 224–245,
[DOI](https://doi.org/10.1016/j.ffa.2016.04.004),
[accepted manuscript, February 29, 2016](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
section 5, Definitions 5.1–5.2, Lemma 5.3 and the immediately following
unnumbered GRS shortening formula, printed pp. 7–8.

If e is supported on A and sigma(e)=sigma(f(gamma)), then c=f(gamma)-e
is a codeword zero on J\K. Shorten successively at precisely these seven
labels, permuting coordinates to apply the single-coordinate formula.
After j deletions the length and dimension are 16-j and 8-j. Each step
starts with positive dimension at least two and leaves positive dimension;
distinct retained labels and the products of nonzero label differences
give nonzero multipliers. After seven steps, the length-nine,
dimension-one code on S union K consists exactly of lambda*g_K evaluated
there. Reinsert zeros on J\K to recover c on all H. This is an application
of the cited formula, not a reproof of general shortening.

On S\I, c=f(gamma), giving (1); on I and K, subtraction gives (2).
Conversely, (1) and (2) give f(gamma)-e=lambda*g_K on all H. This
degree-seven polynomial evaluates to a codeword, so all eight shifted
moments agree. Since g_K(x) is nonzero for every x in S union K,
any one of the five equations determines lambda uniquely and the stated
fullness gates are exact. Lambda=0 makes e=f(gamma) supported on I;
it is retained as a possible weight-at-most-two event, not divided out.
L010 proves same-support badness and uniqueness for every such recovery.
There is no rationality restriction on gamma or lambda.

### Why equality needs at least six two-overlap rows

If the active lift set has size at most six, extend it to a six-set and
apply audited L103 with the same actual D, locators and finite chart.
It gives at most fifteen, retaining its finite-certificate qualifications.
Thus a seven-set equality pencil must have all seven coordinates active.

Assume equality and let E={gamma in B:e_gamma=f(gamma)}. L010 makes all
sixteen errors full of weight four and every coordinate's degree four.
For gamma outside E, c=f(gamma)-e_gamma is a nonzero codeword. If m is
the intersection size of its error support with the fixed S, then
9<=wt(c)<=|S union supp(e_gamma)|=11-m, hence m<=2.
The fixed-set upper bound retains vanishing lift coordinates and every
cancellation. It is not applied when c=0.

At each gamma in E, exactly three of the seven active affine coordinate
polynomials vanish. The zero triples at distinct finite gamma are disjoint,
because a nonzero affine polynomial has at most one root. Constants have
no roots and are allowed. Consequently 3t<=7 and t<=2. The total count
and S-incidence balance are

\[
 t+n_0+n_1+n_2=16,\qquad 4t+n_1+2n_2=28.
\]

Eliminating n_1,n_2 gives (3). This proves occurrence of the selected
rows; occurrence was not assumed in using shortening.

### Eliminating the lift from simultaneous recoveries

Index the r=n_2 rows by j, with distinct original finite gamma_j and
supports A_j=I_j union K_j, |I_j|=|K_j|=2. Write g_j=g_(K_j) and
lambda_j for (1)'s scalar. For x in S define
R_x={j:x notin I_j} and d_x=|{j:x in I_j}|. Equality balance gives
d_x<=4; r>=6 therefore gives |R_x|>=2. Choose two distinct anchors
p_x,q_x in R_x. No choice of affine or projective parameter chart is made.

For every j in R_x\{p_x,q_x}, impose the following linear equation
in the r unknown scalars lambda_1,...,lambda_r:

\[
 (\gamma_{q_x}-\gamma_{p_x})g_j(x)\lambda_j
 -(\gamma_{q_x}-\gamma_j)g_{p_x}(x)\lambda_{p_x}
 -(\gamma_j-\gamma_{p_x})g_{q_x}(x)\lambda_{q_x}=0.       \tag{4}
\]

Call this matrix M. It has exactly
sum_x(|R_x|-2)=7r-sum_x d_x-14=5r-14 rows, since sum_x d_x=2r.
This counts equations, not their rank. Every actual pencil supplies a
kernel vector whose entries are all nonzero, by full outside weights.

Conversely, (4) is precisely the condition that all prescribed values
lambda_j*g_j(x), j in R_x, lie on the same affine function of gamma_j.
Indeed, the two anchors uniquely define

\[
 F_x(T)=\frac{(\gamma_{q_x}-T)\lambda_{p_x}g_{p_x}(x)
                +(T-\gamma_{p_x})\lambda_{q_x}g_{q_x}(x)}
               {\gamma_{q_x}-\gamma_{p_x}}.              \tag{5}
\]

The denominator is nonzero because parameters are distinct. Substitution
at each other j is equivalent to (4), with no further division. Thus
the matrix is necessary and sufficient for the simultaneous equations
(1) on some affine lift. For a supplied original lift it reproduces that
lift, because both anchor values agree. Choice of anchors changes the
presentation, not the solution condition.

For the construction converse, prescribe r>=6 distinct finite parameters,
rows I_j,K_j of the stated sizes, and coordinate degrees at most four
for all labels of H in A_j. Suppose M has a vector with all lambda_j!=0
and, for both i in I_j, the additional gates

\[
 F_i(\gamma_j)-\lambda_jg_j(i)\ne0.                     \tag{6}
\]

Define F off S to be zero, a=F(0), and b the coefficient of T in F.
Every F_x on S is active: at its first anchor its value is
lambda_(p_x)*g_(p_x)(x)!=0. Equations (1)–(2) now give full errors on
A_j with all eight moments correct. L010's pointwise determinant
factorization (which does not require polynomial nonpersistence) gives
D(gamma_j)!=0 and L(gamma_j,X)=D(gamma_j)prod_(z in A_j)(X-z).
Every x in H is omitted by some row, since its occurrence count is at
most four while r>=6. At such a row ell_x(gamma_j)!=0. Hence D and
every ell_x are nonzero polynomials. L010 now applies in full, proving
these are actual same-support bad events in the constructed finite chart.

This also shows why the matrix test is useful: the existence question for
these simultaneous full rows has no remaining hidden moment or locator
gate. A kernel of positive dimension alone is insufficient: one vector
must pass all entry and residual gates. Neither (4) nor (6) supplies
sixteen total events, their remaining balance, or an inactive coordinate.
Even a successful r=6 construction would only realize six events.

### A local survivor and the exact limit of the current attempt

Two full two-overlap recoveries alone do not force an inactive coordinate,
even with actual polynomial nonpersistence. This has a direct construction
over the prime subfield, requiring no census. Choose disjoint two-sets
I_0,I_1 in S and disjoint two-sets K_0,K_1 in J. On S put
F^j_x=g_(K_j)(x)+1_(x in I_j) for j=0,1, and put F^j=0 off S.
Let f(T)=(1-T)F^0+TF^1, a=F^0 and b=F^1-F^0.
At gamma_j=j, take lambda_j=1. Equation (1) holds, and (2)'s I_j
weights are exactly one; its K_j weights are -g_(K_j)(k)!=0.
The two error supports are disjoint, so every coordinate is omitted by
at least one. The same pointwise factorization proves nonzero D and
all nonzero polynomial locators; L010 gives original badness at 0 and 1.
Every coordinate in S is active: the other endpoint is a nonzero g value
if it belongs to one of the I_j, and both are nonzero outside their union.
This verifies all assertions without needing to evaluate the full bad set.

This is a local survivor, not a sixteen-count witness or a counterexample
to an equality-conditioned reduction. No assertion about minimal support
among other representatives is made. The completed bounded attempt obtains
(4)–(6) and the compulsory threshold r>=6. It does not resolve feasibility
there or force an inactive coordinate. The next substantive test must use
the forced many-row system, not repeat the two-row local argument or the
six-set zero count.

Source scope is the prior EXPLORE assessment
`drafts/literature/2026-10-17-seven-coordinate-syndrome-bound-review.md`.
This is a local reproduction/specialization of shortening and affine
interpolation; no originality or progress beyond the checked literature
is claimed. No new finite computation or cross-notebook input is used.

### Separate critical audit, 2026-10-17

Step 2026-10-17-mca-292-seven-coordinate-fixed-split-critical-audit
checked this full proof, L010's kernel, pointwise factorization,
same-support and equality arguments, and L103's exact hypotheses and
completed audit. The unchanged ready seven-coordinate assessment supplies
the inspected Hall and shortening inputs. No mathematical error or new
dependency was found; no source theorem is reproved here.

The shortening set is exactly J minus K, of size seven, independent
of the parameter and any vanishing lift coordinate. Its successive
dimensions are 8 through 1; retained multipliers are products of
distinct nonzero differences. Equations (1) and (2) give equality of
the entire vectors f-e and lambda*g_K, including the seven deleted
coordinates. Thus the equivalence restores all eight moments, permits
lambda=0 and both canceled overlap weights, and invokes same-support
badness only with the actual nonpersistent polynomials available.

At equality L010 supplies full four-errors and coordinate degree four.
For e!=f the nonzero difference is a codeword supported in a union of
size 11-m, so distance nine gives m<=2 even with cancellations. This
argument does not discard the e=f exception. Each such exception has
exactly three zeros among seven active affine coordinates; disjointness
of these zero triples gives t<=2, including constant coordinates.
The two exact balances in the proof then give 2n_0+n_1=4+2t and
r=12-3t+n_0>=6. Inactive coordinates instead enter L103 with precisely
the same coefficient syndromes, actual polynomials and original chart.

For every x, coordinate degree at most four gives at least r-4>=2
actual anchors. Their distinct original finite parameters justify the
only denominator in (5). Each remaining equation is precisely affine
interpolation, and sum_x d_x=2r gives 5r-14 rows without asserting rank.
In the construction converse, nonzero lambda makes every anchor value
nonzero and (6) makes all selected errors full. Since r>=6 while every
coordinate has degree at most four, each label is omitted at a full
event. L010's pointwise factorization proves D and each locator are
nonzero polynomials before its bad-event theorem is applied. The
two-row local example uses disjoint supports for the same nonpersistence
check, without asserting a six-row or sixteen-event completion.

This audit validates only the stated recovery and matrix reduction.
The rank obstruction and uniform seven-coordinate count remain open.
L103's imported L040/L069 finite-certificate qualifications are reused,
not removed or independently rerun by this audit.

## Mathlib

Full matching seven-coordinate recovery, equality reduction and simultaneous
matrix theorem: **not checked**. Supporting GRS shortening, finite-field,
affine interpolation and matrix-kernel coverage: **not checked**. Unknown
coverage is not absence. The smaller-class use of L103 retains its audited
finite-certificate inputs; the full seven-coordinate bound is not proved.
