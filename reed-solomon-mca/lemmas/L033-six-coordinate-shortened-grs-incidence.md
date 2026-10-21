# L033 — Six-coordinate pencils reduce to shortened-GRS line incidences

## Hypotheses

Let F=F_(97^20), let H be the order-sixteen subgroup of F_97^*, and
let C be the degree-less-than-eight evaluation code on H. Fix a,b in
F^H, use L010's shifted moments sigma_j(z)=sum_(x in H) z_x x^j for
1<=j<=8, and write s(T)=sigma(a)+T sigma(b). Retain the pinned cell
1/4<=delta<5/16 and the assumptions that D and every coordinate locator
are nonzero polynomials. Let B(a,b) be L010's bad finite-parameter set.

Assume three distinct finite bad parameters gamma_1,gamma_2,gamma_3
have full-weight four-errors with L032's union-six pattern and affine
relations. Explicitly, U is a six-subset of H partitioned into two-sets
Z_1,Z_2,Z_3, and there are c_x in F^* such that
\[
 f_x(T)=c_x(T-\gamma_i)\quad(x\in Z_i),\qquad
 f_x(T)=0\quad(x\notin U),\qquad \sigma(f(T))=s(T).       \tag{1}
\]
The three actual errors are f(gamma_i), supported on U minus Z_i.
L032 supplies precisely this hypothesis for an equality triple whose
union has size six. It also supplies independence of the coefficient
vectors u,v in f(T)=u+Tv. One may instead assume this explicit triple;
the reduction below does not require sixteen-count equality. Whenever
equality is invoked below, it is an additional hypothesis, not an
inference from local compatibility. Put J=H minus U, so |J|=10.

For every K subset J define the polynomial
\[
 g_K(X)=\prod_{y\in J\setminus K}(X-y).
\]
For a four-set K in J define a two-dimensional subspace of F^U
\[
 W_K^{(0)}=\operatorname{span}_F
       \{(g_K(z))_{z\in U},(z g_K(z))_{z\in U}\}.
\]
For x in U and a three-set K in J define
\[
 W_{x,K}^{(1)}=\operatorname{span}_F
       \{(g_K(z))_{z\in U},\delta_x\},
\]
where delta_x has value one at x and zero at the other U coordinates.
All generating vectors lie in F_97^U. Let
\(\ell=\mathbf P(\operatorname{span}_F(u|_U,v|_U))\)
and \(\iota(\gamma)=[f(\gamma)|_U]\).

## Conclusion

There are 210 indexed lines P(W_K^(0)) and 720 indexed lines
P(W_(x,K)^(1)) in P^5(F). No claim that all these lines are distinct is
needed. The pencil line ell differs from every one of them; hence it
meets each in at most one projective point. The finite parameter chart
is ell minus the single point [v|_U], with iota injective. The three
given points meet none of the indexed lines.

Every additional actual full-weight four-error, at a finite parameter
gamma different from gamma_1,gamma_2,gamma_3, is described by exactly
one of the following two cases. The stated conditions are sufficient
as well as necessary.

* **Disjoint support:** A=K is a four-set in J. There are alpha,beta in F,
  not both zero, with
  \[
    f_z(\gamma)=g_K(z)(\alpha+\beta z)\quad(z\in U),\qquad
    \alpha+\beta y\ne0\quad(y\in K).                    \tag{2}
  \]
  Thus iota(gamma) lies on P(W_K^(0)). The error is
  \(e_y=-g_K(y)(\alpha+\beta y)\) on K and zero elsewhere.
  Constant residual polynomials, alpha=0, and beta=0 are allowed when
  they meet these conditions.

* **One-coordinate overlap:** A={x} union K for x in U and a three-set
  K in J. There are lambda,mu in F^* with
  \[
    f(\gamma)|_U=\lambda(g_K(z))_{z\in U}+\mu\delta_x.  \tag{3}
  \]
  Thus iota(gamma) lies on P(W_(x,K)^(1)). The error has e_x=mu,
  \(e_y=-\lambda g_K(y)\) on K, and zero elsewhere.

All eight moments and actual same-support badness hold for these
converses. No other overlap is possible, including when values cancel
in f(gamma)-e. A projective intersection alone is not a full-weight
certificate: in (2) a residual zero on K invalidates the four-support;
in (3) mu=0 invalidates the overlapping four-support. Every such finite
invalid intersection, away from the three selected parameters, instead
gives an actual weight-three error. Errors of weight at most two are
impossible here. Any weight-three parameter excludes sixteen-count
equality by L010. Distinct valid indexed incidences give distinct finite
parameters, even at exceptional shared intersections.

Let N_ext be the number of valid indexed incidences in (2) and (3),
counting only points iota(gamma) in the stated finite chart outside
the selected three. Let N_3 be the number of weight-three parameters.
Then the exact accounting is
\[
 |B(a,b)|=3+N_{\rm ext}+N_3.                            \tag{4}
\]
If N_3>0 the existing L010 bound already gives |B(a,b)|<=15. Otherwise
the desired analytic bound is N_ext<=12. In particular a sixteen-count
equality pencil in this branch would need thirteen valid additional
incidences and N_3=0. This reduction proves neither the twelve bound nor
universal extraction of a union-six triple. The global interval remains
11/q–16/q, and this is no resolution of the main challenge.

## Proof

### Standard shortening input and its exact specialization

Import the GRS shortening formula from I. Marquez-Corbella and
R. Pellikaan, *A characterization of MDS codes that have an error
correcting pair*, Finite Fields and Their Applications 40 (2016),
224–245, DOI [10.1016/j.ffa.2016.04.004](https://doi.org/10.1016/j.ffa.2016.04.004).
Use the [accepted manuscript dated February 29, 2016](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
section 5, Definitions 5.1–5.2, Lemma 5.3 and the unnumbered GRS formula
immediately following it, printed pp. 7–8. Shortening means restricting
to codewords zero on the deleted labels before deleting them. For a
single deleted label y, the formula reduces the GRS dimension by one
and multiplies every retained multiplier at z by z-y.

Here the original multipliers are one. Permuting coordinates to apply
that single-coordinate formula and iterating on a set R of six or seven
labels gives retained labels H minus R, dimension 8-|R|, and multiplier
\(\prod_{y\in R}(z-y)\) at each retained z. At an intermediate stage
with r deleted labels, n=16-r and k=8-r; for the next deletion
n-1=15-r>=8-r=k, the stated MDS parameter condition holds, and the new
dimension remains positive through r+1<=7. Labels remain distinct and
each retained multiplier is nonzero. These checks justify the iteration
over F, not merely over F_97. No dual multiplier or puncturing formula
is substituted. The resulting codewords, extended by zero on R, are
exactly evaluations of
\[
  \prod_{y\in R}(X-y)h(X),\qquad \deg h<8-|R|.         \tag{5}
\]
This is an application of the cited formula with its evaluation
definition, not a reproof of generic shortening.

The distance-nine input is J. I. Hall, *Notes on Coding Theory*,
[GRS chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
Theorem 5.1.1 and proof, printed pp. 63–64, undated author-hosted copy
inspected 2026-10-05. It assumes distinct evaluation labels, nonzero
multipliers and 0<k<=n over any field. With n=16,k=8 and multipliers
one its hypotheses hold. L010 already provides ker(sigma)=C, uniqueness
of representatives of weight at most four, and same-support badness
under the nonzero D/locator hypotheses. We reuse these results and
L032's lift, rather than reprove distance, interpolation or the moment
kernel.

### Exhaustive support split

The rank check in L032 uses only (1): for x in Z_1 and y in Z_2,
the coefficient columns (-c_x gamma_1,c_x) and
(-c_y gamma_2,c_y) have determinant c_x c_y(gamma_2-gamma_1)!=0.
Thus u,v remain independent when the explicit triple is assumed
without sixteen-count equality.

By (1), f(gamma_i) has weight four, and f(gamma) has weight six at
every other finite parameter: its six nonzero coordinate polynomials
have roots exactly among the selected three. There are no other
cancellation parameters of the lift. Independence of u,v also implies
f(gamma) is never zero.

For such another gamma let e be an actual weight-four error and put
A=supp(e), K=A intersect J, and t=|A intersect U|. The vector
c=f(gamma)-e has zero syndrome, hence is in C by L010. It is nonzero
because f(gamma) has weight six and e has weight four. Its support is
contained in U union A, of size 6+4-t. Distance nine forces t<=1.
Cancellations at overlapping coordinates only shrink this support and
cannot invalidate that exclusion. This separates all possibilities,
without an assumption that the supports are disjoint in advance.

If t=0, K=A has size four and c vanishes at R=J minus K, a six-set.
Use (5): c is the evaluation of g_K(X)(alpha+beta X). On U, e=0,
so its evaluation equals f(gamma), giving (2). On K, f=0 and e=-c;
full weight is exactly the nonvanishing in (2). Conversely (2) constructs
that codeword and error on all sixteen coordinates, with the indicated
weights. Since c is in ker(sigma), sigma(e)=sigma(f(gamma))=s(gamma)
for all eight shifted moments. Subtracting from a+gamma b gives a
codeword, and L010 proves failure on the complement of K. Both
alpha and beta may be individually zero, but they cannot both be zero
because f(gamma)|_U is nonzero.

If t=1, write A={x} union K with |K|=3. Now c vanishes at the seven-set
R=J minus K. Formula (5) makes c the evaluation of lambda g_K.
Its nonzeroness implies lambda!=0. On U minus {x}, c=f(gamma);
at x the difference f_x(gamma)-lambda g_K(x) is e_x=mu. Thus (3)
holds, with mu!=0 precisely because x is in the actual support.
Conversely (3) gives the stated error by subtracting the evaluation of
lambda g_K from f(gamma). Values g_K(y) are nonzero at every y in K
and U, since these labels are disjoint from its roots. Hence all four
error weights are nonzero. The same kernel identity verifies all eight
moments, and L010 again verifies same-support badness. In particular
one cannot silently discard an overlap where f_x and e_x partially
cancel; equation (3) retains their exact difference.

### Lower weights and exceptional intersections

At a selected parameter the unique representative of weight at most
four is already f(gamma_i), so no other error can occur there. At any
other gamma an error of weight w<=2 would make f(gamma)-e a nonzero
codeword of weight at most 6+w<=8, which is impossible. If w=3, its
support must be disjoint from U, since an overlap would again give
weight at most eight. Such weight-three errors are possible candidates;
they are not assumed absent. L010 supplies their badness and excludes
sixteen-count equality whenever one occurs.

Consider a finite intersection with P(W_K^(0)) away from the selected
parameters. Taking the actual vector f(gamma)|_U rather than its
projective class determines unique alpha,beta in (2). Because f(gamma)
is nonzero on every U coordinate, this residual polynomial is nonzero.
If it has a root in K, beta!=0 and it has exactly one such root;
subtracting the same codeword therefore gives an actual weight-three
error supported on K minus that root. Otherwise it is a valid four-error
incidence. Zero on a U label is impossible at this gamma. This treats
constant residuals and all zero coefficient cases.

For an intersection with P(W_(x,K)^(1)), its actual vector likewise
determines unique lambda,mu. Its values on the five labels U minus {x}
force lambda!=0. If mu=0, the same subtraction gives a full-weight
three-error on K. Otherwise it is the valid overlapping four-error
of (3). Thus every finite intersection in question has an actual
representative of weight three or four; none is treated as automatically
full weight. A common point of indexed lines is handled by these same
tests individually. If two indexed incidences at that finite point
were valid, their distinct indexed supports would yield different
errors of weight four for the same syndrome. L010's uniqueness excludes
this. The index-to-support map itself is injective: K determines the
disjoint support, while x and K determine its unique U overlap in the
other case. If one intersection is valid and another is invalid, the
weight-four and weight-three representatives would also contradict
uniqueness. Shared finite intersections can therefore produce only
lower-weight representatives, not duplicated valid parameters.

### Projective chart and exact counting target

All g_K values on U are nonzero. For W_K^(0), the two generators are
independent because the six labels in U are distinct. Every nonzero
vector in that space has at least five nonzero coordinates on U: a
nonzero polynomial alpha+beta X has at most one zero among those
labels. For W_(x,K)^(1), independence follows from the five nonzero
g_K values outside x. A nonzero vector with lambda!=0 has at least
five nonzero coordinates, whereas one with lambda=0 has weight one.
Neither type of space contains a vector of weight four. But ell contains
the selected weight-four f(gamma_i)|_U. It follows that ell equals none
of their projectivizations and its three selected points lie on none.
Two distinct projective lines have at most one common point, since two
common independent vectors would make their two-dimensional spaces
equal. These facts include nongeneric and shared intersections; no
transversality assumption is used.

Independence of u,v from L032 proves gamma -> [u+gamma v] injective:
if u+gamma v=rho(u+eta v), comparison of coefficients gives rho=1
and gamma=eta. The points on ell are exactly these finite points and
[v]. Indeed, a nonzero vector au+bv has a finite form when a!=0;
when a=0 its class is [v]. The latter point is not an original finite
parameter and is never counted. No projective change removes a finite
parameter, including any of the three selected ones.

Since |J|=10, the indexed configurations have binom(10,4)=210 and
6 binom(10,3)=720 lines. This is a closed-form count of their indices,
not a finite-field search or an incidence bound of twelve. The lines
are defined over F_97, but ell and its intersection points need not be.
Meeting rational lines does not imply that ell descends to F_97, and
no such descent is used.

Every additional full-weight four-error occurs by the exhaustive split,
and every valid incidence gives such an error. Uniqueness and the
finite-chart injection show that N_ext counts distinct parameters,
rather than multiple descriptions of one parameter. The selected three
are disjoint from this count. All remaining bad parameters have weight
three by the preceding lower-weight check and L010's identification of
badness with a representative of weight at most four. This proves (4).
When N_3>0, L010's inequality |B|<=16-3N_3 implies the stated <=15
(in fact <=13). When N_3=0, (4) makes <=15 equivalent in this branch
to N_ext<=12. A sixteen-count candidate would require N_ext=13.

This exact reduction replaces the eight moment equations by two explicit
shortened evaluation spaces per support type, with necessary and
sufficient nonvanishing tests. It supplies a concrete incidence problem,
not its solution. Universal triple extraction, an analytic twelve bound,
extension-field incidence control, arbitrary-family fifteen, stronger
source overlap and ABF26 identification remain unresolved. The standard
shortening and distance statements are imported by citation; the local
support specialization is recorded as REPRODUCTION, with no originality
or progress beyond the assessed sources claimed. The separate critical
audit below found no defect in this specialization.

### Critical audit, 2026-10-07

This audit checks the existing reduction, not an incidence estimate.
Its explicit-triple hypotheses suffice without invoking L032's equality
hypothesis: the displayed nonzero two-column determinant proves rank two
directly from (1). Each of the six coordinates has precisely its assigned
root gamma_i, so the lift has weight four at those three parameters and
weight six elsewhere. All reasoning takes place over F; the constants
c_x and the parameters need not lie in F_97.

L010's shifted moment kernel, distance, uniqueness and same-support
arguments were checked at their uses. The kernel calculation uses
subgroup powers 1 through 15 and the nonzero shifted Vandermonde
determinant, so it is the stated unweighted evaluation code C. The pinned
radius interval has agreement threshold twelve. For an error on A with
|A|<=4, failure of b on H minus A follows from the nonzero polynomial
D/locator assumptions, including singular finite parameters: otherwise
the entire syndrome pencil is representable on A, forcing D identically
zero when |A|<=3 or a persistent locator when |A|=4. Thus the converses
establish the actual event, not just closeness.

For an additional error, f-e is nonzero because its two terms have
different weights. The bound wt(f-e)<=10-t gives t<=1 regardless of
cancellation on the overlap. The actual zero sets used for shortening
are J minus K, with six deletions for t=0 and seven for t=1. They need
not be the complete zero sets of the codeword. Successive shortened
parameters are [16-r,8-r]; every next step meets 15-r>=8-r, and the
final dimensions are two and one. Every retained multiplier is a
product of nonzero differences. These are precisely the hypotheses and
factor convention of the cited single-coordinate shortening formula;
neither dual-code weights nor a prime-field restriction enters.

Both subtraction signs check: in the disjoint case c=g_K(alpha+beta X)
equals f on U and e=-c on K; in the overlap case c=lambda g_K equals
f off x in U and e_x=f_x-c_x=mu, while e=-c on K. Both codewords
vanish on J minus K, so these are identities on all sixteen coordinates.
Their degree bounds are at most seven. Consequently sigma(e)=s(gamma)
in all eight entries. The conditions on alpha+beta y, lambda and mu are
exactly the required full-weight conditions, not merely sufficient tests.
Cancellation at x causes no omitted case: a nonzero c in the overlap
case has lambda!=0 and g_K(x)!=0.

For lower weights, wt(f-e)<=6+w rules out w<=2 away from the three
selected parameters; for w=3, distance forces disjointness from U.
At the selected parameters uniqueness already excludes any alternative.
At a disjoint-line intersection the residual linear polynomial is
nonzero, and an invalid four-error has exactly one root on K, hence
weight exactly three. At an overlap-line intersection the five nonzero
coordinates outside x force lambda!=0; the only invalid case is mu=0,
also giving weight exactly three. No weight-zero vector or vanishing
lambda escapes these checks. L010 charges a three-error sixteen locator
root multiplicities rather than four, giving |B|<=16-3N_3 here.

The two generators of each indexed space are independent. Its nonzero
vectors have weight at least five on U, or, only for the overlap space
with lambda=0, weight one. Thus the selected weight-four vectors belong
to none of the indexed spaces. This proves both exclusion of the three
selected points and noncoincidence with ell; it does not assume that
different indexed lines are distinct. Each index can therefore contribute
at most one intersection with ell. If different indices had a common
valid finite point, their injectively indexed four-supports would give
different representatives of the same syndrome, violating uniqueness.
A valid and an invalid incidence cannot share a finite point either.
Shared invalid points are permitted and are counted by their parameters
in N_3, never by their number of indices.

Finally rank two makes gamma -> [u+gamma v] injective and omits exactly
[v], the original parameter infinity. Counts 210=binom(10,4) and
720=6 binom(10,3) concern indices, not distinct geometric lines or bad
parameters. Every bad parameter is either one of the selected three,
a unique valid additional incidence, or a weight-three parameter, and
these alternatives are disjoint. This verifies (4) with its original
finite chart. No bound N_ext<=12 follows from the audit. The uses of
L010 and L032 match the existing DAG, with the external standard inputs
cited above; no new mathematical premise or field descent was added.

## Mathlib

Coverage of the complete six-coordinate incidence reduction, its
full-weight converses, and the exact cited shortening transformation is
**not checked**. No matching Mathlib theorem, absence claim or Lean
verification is asserted. The cited primary inputs and informal proof
above supply the argument. ArkLib's pinned event is definition support,
separate from Mathlib and from the unread ABF26 definition.
