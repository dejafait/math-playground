# L043 — Exact reduced fourth-support incidence for a tau=1 triple

## Hypotheses

Let F=F_(97^20), let H be the order-sixteen subgroup of F_97^*,
and use C=RS[F,H,8], L010's shifted moments and the pinned cell
1/4<=delta<5/16. Take L041's **local converse**, without a sixteen-count
premise. After renaming the three errors, let
\[
 A_0=\{h,d,y_1,y_2\},\quad A_1=\{h,d,z_1,z_2\},\quad
 A_2=\{h,w_1,w_2,w_3\},
\]
with all nine labels distinct in H and three distinct original finite
parameters gamma_0,gamma_1,gamma_2 in F. Put
\[
 U=A_0\cup A_1\cup A_2,\quad
 Q(X)=\prod_{x\in H\setminus U}(X-x),\quad c_x=Q(x),
 \qquad v_x=(x,x^2,\ldots,x^8)^{\mathsf{tr}}.
\]
Use L041's nonzero lambda and alpha_i=gamma_j-gamma_k, with normalized
weights p,q,1-p-q at h and r,1-r at d. Retain exactly the gates
\[
 \lambda\ne0,\qquad p q(1-p-q)r(1-r)\ne0.               \tag{1}
\]
Each singleton weight is lambda*c_x/alpha_i; all other weights are
lambda*c_x times its normalized weight divided by alpha_i. The actual
syndrome pencil is s(T)=sigma(a)+T sigma(b), with these three prescribed
values. Weights, parameters and lambda range over F. L042, separately
audited, gives the nonzero determinant polynomial and all nonpersistent
coordinate locators. No rationality of the original chart or excluded
direction, global equality or completion is assumed.

Fix a four-subset K of H distinct from A_0,A_1,A_2. We seek exactly
when there is an additional full-weight error on K at an original finite
T different from all three gamma_i. Define
\[
 g=\gamma_1-\gamma_0,\quad
 \rho=(\gamma_2-\gamma_0)/g\notin\{0,1\},\quad
 t=(T-\gamma_0)/g,\qquad
 Y=\sum_{i=1}^2c_{y_i}v_{y_i},\quad
 Z=\sum_{i=1}^2c_{z_i}v_{z_i}.                         \tag{2}
\]
Y,Z and c_x belong to the prime field; rho,p,q,r need not.

For f_K(X)=product_(x in K)(X-x)=sum_(j=0)^4 f_j X^j, let
\[
 (\mathcal F_K m)_i=\sum_{j=0}^4 f_j m_{i+j}
                       \quad(1\le i\le4),\qquad
 C_K=(\mathcal F_K v_h,\mathcal F_K v_d).
\]
Set J={h,d} minus K and m=|J|. Choose any matrix B_K over F_97 whose
rows form a basis of the left kernel of C_K, and put
\[
 \mathbf y_K=B_K\mathcal F_K Y,\qquad
 \mathbf z_K=B_K\mathcal F_K Z.                       \tag{3}
\]
Their length is 4-m. All these tests are exact prime-field label tests.

## Conclusion

The following is necessary and sufficient, including all exceptional
quotient ranks and actual-weight gates. It is independent of the choice
of B_K.

**Nonuniversal systems.** If precisely one vector in (3) is zero, or
both are nonzero and linearly independent, K has no additional error.
If both are nonzero and proportional, write uniquely
\[
 \mathbf z_K=\mu\mathbf y_K,\qquad \mu\in F_{97}^{*}.
\]
There is no eligible parameter if mu=-1 or
\[
                 E=\rho-(1-\rho)\mu=0.               \tag{4}
\]
Otherwise the only candidate parameter is
\[
              T_K=\gamma_0+g\rho/E.                 \tag{5}
\]
It automatically differs from gamma_0,gamma_1,gamma_2. For x in J,
compute beta_x from
\[
 \sum_{x\in J}(\mathcal F_K v_x)\beta_x
                      =-\mathcal F_K(Z-\mu Y).        \tag{6}
\]
This system has a unique solution over F_97. It can be computed using
just the first m rows, with the m=0 system empty. Require exactly
\[
 \begin{cases}
 c_h(q-\mu p)=\beta_h,&h\notin K,\\
 c_d[1-(1+\mu)r]=\beta_d,&d\notin K.
 \end{cases}                                         \tag{7}
\]
No condition of (7) is imposed for a label contained in K. Define
\[
 N_K=Z-\mu Y+c_h(q-\mu p)v_h
                     +c_d[1-(1+\mu)r]v_d.            \tag{8}
\]
Once (7) holds, recover omega_x, x in K, by the four equations
\[
 \sum_{x\in K}\omega_x x^j=(N_K)_j\quad(1\le j\le4).
                                                               \tag{9}
\]
The last gate is product_(x in K) omega_x!=0. The actual fourth error
has precisely the weights
\[
                   e_K(x)=\lambda\omega_x/(gE).       \tag{10}
\]
Thus (7) and (9) are explicit affine equations and weight hyperplane
exclusions in the three normalized free weights, over F_97. In particular,
when d is absent, (7) forces
r=(1-beta_d/c_d)/(1+mu) in F_97. This is a local weight restriction,
not descent of the entire pencil or its original parameters.

**Universal system.** Both vectors in (3) are zero if and only if
\[
                       K=K_*:=\{y_1,y_2,z_1,z_2\}.     \tag{11}
\]
For this unique support there is an additional full-weight error exactly
when
\[
             E_*=r+\rho-1\ne0,\qquad r q=(1-r)p.       \tag{12}
\]
It then has the unique original finite parameter
\[
                    T_*=\gamma_0+g\rho r/E_*           \tag{13}
\]
and actual weights
\[
 e_*(y_i)=\frac{\lambda}{g}\frac{1-t_*}{1-\rho}c_{y_i},
 \qquad
 e_*(z_i)=\frac{\lambda}{g}\frac{t_*}{\rho}c_{z_i},
 \qquad t_*=\rho r/E_* .                              \tag{14}
\]
All four weights are nonzero and t_* is different from 0,1,rho.
If E_*=0, the projected universal system has no eligible finite lift;
no projective-infinity point is counted. The original triple gates (1)
always remain in force, including 1-p-q!=0.

For completeness, rank(C_K)=m for each m=0,1,2, with no exceptional
label-dependent drop. When m=0, no support is eligible: both-zero and
nonzero proportional cases cannot occur. The tests above retain this
case without dividing by a missing coefficient.

Every full-weight error admitted by these tests is unique and is bad
on the same twelve-coordinate complement of K for the pinned event.
Conversely every additional full-weight error on K is admitted. A failed
weight gate in (9) can instead witness a lower-weight error; the criterion
must not silently count it as full weight. This result neither classifies
all lower-weight parameters nor bounds the total additional parameters.
Even all these local tests would leave counting, universal extraction and
ABF26 identification unresolved. This is a reproduction/specialization of
known recurrence and quotient methods. A separate critical audit on
2026-10-08 found no defect within these hypotheses; the checks appear below.

## Proof

### Imported recurrence and explicit normalization

Use Przemek Chojecki, *Shortening Bounds for Reed–Solomon MCA*, live author
TeX v9.2 dated July 17, 2026, inspected 2026-10-08, source lines 2785–2935:
`drc:lem-locator-recurrence` (DR2) and `drc:thm-exact-compiler` (DR6–DRC),
including both proofs and zero-direction cases, in the
[author source](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex).
This mutable source is not certified identical to ePrint 2026/1463.
The cited recurrence theorem identifies support-span membership with all
R-t locator recurrences for distinct weighted Vandermonde columns and
support size t<R. Here redundancy is R=8, support size is four, eta_j=s_(j+1)
for j=0,...,7, and the columns have nonzero multipliers x in H. Consequently
\[
 \mathcal F_K m=0\quad\Longleftrightarrow\quad
                 m\in\operatorname{span}_F\{v_x:x\in K\}.       \tag{15}
\]
The hypotheses impose no subfield condition on m. This imports the
annihilator theorem rather than reproving it. The known compiler supplies
fixed-support affine intersection tests, but not the present elimination
of L041's free weights and its recovered full-weight gates. L016's analytic
quotient is the local antecedent; its finite classification is not used.

Directly from alpha_0=g(1-rho), alpha_1=g*rho and L041's weights,
affine interpolation through the first two syndromes gives
\[
 \frac{g}{\lambda}s(\gamma_0+gt)
   =H(t)v_h+D_d(t)v_d+A(t),                             \tag{16}
\]
where
\[
 H(t)=c_h\left(\frac{(1-t)p}{1-\rho}+\frac{tq}{\rho}\right),
 \quad
 D_d(t)=c_d\left(\frac{(1-t)r}{1-\rho}
                         +\frac{t(1-r)}{\rho}\right),
 \quad A(t)=\frac{1-t}{1-\rho}Y+\frac{t}{\rho}Z.        \tag{17}
\]
This is an identity for the given syndrome pencil, with no change to
its original excluded direction. The substitution is affine and invertible;
all denominators g,lambda,rho,1-rho are nonzero under the hypotheses.
We use it only for calculation and explicitly return T=gamma_0+g*t.

### Quotient ranks and all projected systems

For every label x,
\[
             \mathcal F_K v_x=f_K(x)(x,x^2,x^3,x^4)^{\mathsf{tr}}.
\]
A column is zero precisely when x in K. The remaining h,d columns are
independent: with both present, their first two rows have determinant
f_K(h)f_K(d)hd(d-h)!=0. With one present, its first entry f_K(x)x
is nonzero. Hence rank(C_K)=m, over F_97 and every extension F.
The kernel of B_K is the image of C_K: containment follows from its
definition and both dimensions are m. Thus membership of (16) in the
K-span requires, and is projectively compatible precisely when,
\[
                 \rho(1-t)\mathbf y_K
                          +(1-\rho)t\mathbf z_K=0.     \tag{18}
\]
Compatibility here allows arbitrary coefficients at the missing h,d
columns; it does not yet assert their actual values (17).

If only y_K is zero, (18) forces t=0; if only z_K is zero, it forces
t=1. These selected parameters are excluded. Two independent nonzero
vectors force simultaneously 1-t=0 and t=0, which is impossible.
For two nonzero dependent vectors, choose a nonzero entry of y_K;
the ratio of the corresponding z_K entry proves mu in F_97^*, even
over F. Equation (18) becomes rho-E*t=0. If E=0 it is inconsistent
since rho!=0; otherwise t=rho/E. This t cannot be zero or one.
It equals rho if and only if E=1, equivalently
(rho-1)(1+mu)=0, hence precisely mu=-1. This proves all exclusions
in (4)–(5), without assuming rho rational. Changing the left-kernel
basis multiplies both vectors by the same invertible matrix, preserving
all the cases and the unique mu.

### The unique universal system, including rank zero

The condition y_K=0 means mathcal F_K Y is in the image of C_K.
By (15), Y then has a moment representative supported in K union {h,d}.
Its original representative is the word with nonzero weights c_y at the
two y-labels. The union of both representatives' supports has size at most
eight: four K-labels, at most two h,d labels and two y-labels. L010's
injectivity of the moment map on every set of size at most eight forces
these words to be identical. Since neither y-label is h or d, both belong
to K. The converse is immediate from (15). The identical argument gives
\[
 \mathbf y_K=0\ \Longleftrightarrow\ \{y_1,y_2\}\subseteq K,
 \qquad
 \mathbf z_K=0\ \Longleftrightarrow\ \{z_1,z_2\}\subseteq K.
\]
The four singleton labels are distinct, so both zero is exactly (11).

If m=0, K contains h,d and its quotient is the full recurrence space.
Both zero is already impossible. If both vectors were nonzero and
proportional, (15) would put Z-mu Y in the K-span. Its four singleton
weights are nonzero, and their union with K has size at most eight.
Injectivity again forces all four singleton labels into K, impossible
because K also contains h,d. Thus all rank-zero cases are rejected by
the existing table; no additional rank-zero exception is omitted.

For K_*, A(t) lies in its span. The two absent columns are independent,
so (15)–(17) require H(t)=D_d(t)=0. Clearing the nonzero denominators
in D_d gives rho*r-(r+rho-1)t=0. If E_*=0 this equation has no finite
solution since rho*r!=0. Otherwise it gives t_*=rho*r/E_*.
The equations t_*=0, t_*=1 and t_*=rho would respectively contradict
rho*r!=0, (rho-1)(r-1)!=0 and rho*(rho-1)!=0. Substitution in H(t_*)
uses
\[
 (1-t_*)/(1-\rho)=(r-1)/E_*,\qquad t_*/\rho=r/E_*.
\]
It gives H(t_*)=c_h[(r-1)p+r q]/E_*, so H(t_*)=0 is precisely
(12). The four remaining coefficients in A(t_*) are nonzero and give
(14) after undoing the factor g/lambda. This proves the universal branch
in both directions. Under (12), p+q=p/r, so the retained triple gate
1-p-q!=0 is exactly p!=r; it was never dropped.

### Missing-column recovery and every fourth weight

For an eligible isolated candidate t=rho/E, equations (17) become
\[
 A(t)=(Z-\mu Y)/E,\quad
 H(t)=c_h(q-\mu p)/E,\quad
 D_d(t)=c_d[1-(1+\mu)r]/E.                             \tag{19}
\]
Equation (18) ensures mathcal F_K(Z-mu Y) belongs to the image of C_K.
Its independent nonzero columns are exactly those indexed by J, so
(6) has a unique solution. The first m rows form an invertible square
matrix by the determinants already checked; solving these rows yields
the full solution because existence is known. All coefficients lie in
F_97, hence beta does too. With m=0, this states simply that
mathcal F_K(Z-mu Y)=0, and no inverse or division is performed.

In the recurrence of the actual syndrome (19), columns for h or d in K
are zero. For the absent columns independence forces precisely (7).
Thus (7) is necessary and sufficient for N_K in the K-span, by (15).
To expose the actual weights, the coefficient matrix in (9) is an
ordinary four-point Vandermonde times a diagonal matrix with nonzero
entries x, hence is invertible. Since N_K is in the K-span, its unique
span coefficients agree with this first-four-moment solution, including
all eight moments. Equations (16) and (19) give
s(T_K)=lambda*N_K/(gE), proving (10). There is no unspecified remainder
or four-moment-only test. Nonzero lambda,g,E ensure that all four actual
weights are nonzero exactly when every omega_x is nonzero.

These arguments prove necessity and sufficiency and retain every possible
cancellation at a shared coordinate. If an omega vanishes, the equations
still supply the actual weight-at-most-three representative at that
parameter, but it is outside the full-weight conclusion. Conversely,
no full-weight error can be lost through such a cancellation gate.
The division by 1+mu in the optional formula for r is valid precisely
because the excluded third-parameter case mu=-1 was removed first.

Finally L042 gives L010's nonpersistent hypotheses for every gated local
triple considered here. L010 therefore makes any admitted sparse error
unique and guarantees failure of b on exactly its agreement complement.
For full K that complement has twelve coordinates and meets the pinned
radius cell. The converse is a statement about the fixed original pencil,
not only a manufactured locator or compatibility of supports. No point
at original infinity, no finite-field sample and no completion premise
is used. The unique universal support and isolated support tests do not
provide a total count or improve the global 11/q–16/q interval.

### Separate critical audit (2026-10-08)

The separate audit checked the complete necessity/sufficiency claim under
the saved scope, without a sixteen-count premise. No mathematical defect
or missing premise was found. This verifies the local reproduction, not
an additional-parameter bound or the challenge. The load-bearing checks
are as follows.

The imported DR2 recurrence uses eight syndrome entries, four distinct
support labels, four recurrences and nonzero column multipliers x. The
shift eta_j=s_(j+1) gives exactly (15), including arbitrary F-valued
moments. The source's full-vector zero-direction case is not applied to
the quotient by the h,d columns. The latter loses information that must
be recovered by (7) or (12); this distinction is essential.

For the normalization, alpha_0=g(1-rho), alpha_1=g*rho and alpha_2=-g.
Thus (16) interpolates the actual first two syndromes with precisely
their original lambda and free weights. L041 gives the third value.
Neither scaling nor affine substitution replaces the fixed pencil.
All denominators used here are nonzero, and the original excluded point
remains infinity under T=gamma_0+g*t.

For m=0,1,2, the first m recurrence rows have respectively the empty
invertible matrix, entry f_K(x)x, and determinant
f_K(h)f_K(d)hd(d-h). The nonempty expressions are nonzero because J
contains only labels absent from K. Hence rank(C_K)=m over both fields.
A left-kernel basis has 4-m rows and annihilator exactly im(C_K), also
after scalar extension. Changing its basis preserves zeros, dependence
and mu. A nonzero coordinate of y_K determines mu in F_97, without
forcing rho, p, q or the original parameters into that subfield.

Equation (18) was checked before dividing by either projected vector.
With y_K=0 and z_K nonzero it forces t=0; with z_K=0 and y_K nonzero
it forces t=1. Independence is inconsistent. When both are nonzero
and proportional, the scalar equation is rho-E*t=0. E=0 is inconsistent,
not an omitted finite parameter. Otherwise t is nonzero, and t=1 would
give (1-rho)mu=0. Further,
E-1=(rho-1)(1+mu), so t=rho occurs exactly when mu=-1. In that case
E=1, even for nonrational rho. These exhaust the projected cases.

The universal classification uses injectivity only on a union of at
most eight labels: K, the two shared labels and the two y-labels
(or the two z-labels). Equality of the resulting words, including
their nonzero singleton coefficients, forces both relevant singleton
labels into K. Thus both zero occurs exactly for K_*. With m=0,
proportionality would instead identify the full four-singleton word
Z-mu Y with a word on K. Their union still has at most eight labels;
all four singleton labels would lie in K, impossible when h,d also
lie there. Neither the both-zero nor proportional branch is hidden
in the rank-zero case.

For K_*, the actual missing-column equations are H(t)=D_d(t)=0,
not merely the identically satisfied quotient equation. Multiplying
D_d(t)/c_d by rho(1-rho) gives rho*r-E_*t. When E_*=0 its constant
term is nonzero. When E_* is nonzero, t_*=rho*r/E_* satisfies

    t_*-1=(rho-1)(r-1)/E_*,
    t_*-rho=rho*(1-rho)/E_*.

Together with rho*r!=0 these exclude all three selected parameters.
The y- and z-coefficients are respectively (r-1)/E_* and r/E_*,
both nonzero. Substituting into H gives exactly rq=(1-r)p.
The retained gate 1-p-q!=0 is still required; under this equation
it is equivalent to p!=r. This checks existence, uniqueness and
all actual weights for the universal lift, including the failed
finite-denominator case.

For the nonuniversal lift, at t=rho/E one has
(1-t)/(1-rho)=-mu/E and t/rho=1/E. These identities give every
term and sign in (19). The quotient condition puts the right side
of (6) in im(C_K), so solving its first m rows recovers the unique
solution of all four rows; this is not an unsupported truncated
solve. The absent-column coefficients must equal beta exactly,
as in (7). Coefficients of shared labels contained in K impose no
recurrence equation, but remain in N_K and affect its recovered weights.
This verifies necessity and sufficiency of (7), including arbitrary
cancellations, rather than just necessity of the projected test.

Once (7) holds, (15) already gives all-eight-moment membership in
the K-span. Its unique coefficients are recovered by the invertible
first-four-moment matrix (9); no unchecked higher moments remain.
The actual weights are lambda/(gE) times these coefficients. This
nonzero scalar cannot conceal a zero weight, and a zero coefficient
stays outside the full-weight claim. The optional formula forcing r
into F_97 when d is absent divides by 1+mu only after mu=-1 has
been excluded. It makes no descent claim for the whole pencil.

As an analytic consistency check only, specialize to L016's labels,
gamma_i=0,1,2 and lambda=1. If P,Q_0,z denote its actual free weights,
then p=-P/c_h, q=2Q_0/c_h and r=-z/c_d. Formula (13) becomes
t_*=2z/(z-c_d); the h equation becomes 2zQ_0=(z+c_d)P, exactly
P+t_*(Q_0-P)=0 after the nonzero denominator is cleared. This checks
the universal signs; it imports neither the finite table nor count five.

Finally the gates and support pattern are precisely L042's audited
domain. Its nonzero D and coordinate polynomials admit this original
pencil to L010. The moment-kernel identity gives agreement on H minus K,
while L010 separately proves input failure on that same set. Its size
twelve meets the radius cell. Distance nine supplies uniqueness for
weight-at-most-four representatives. The audit assumes no rational
chart, equality, generic quotient rank or completion, and introduces
no new mathematical input beyond those already used in this proof.

## Mathlib

The full reduced incidence criterion, projected-vector classification,
weight recovery and chart qualifications: **not checked**. Supporting
Vandermonde rank, finite-field linear algebra, moment-kernel and recurrence
results: **not checked** in Mathlib in this step. L010, L041, audited L042
and the precise imported recurrence theorem above are the informal inputs.
No matching Mathlib theorem, absence result or Lean verification is claimed.
The required elimination is supplied because the cited fixed-support
compiler does not state L041's free-weight equations or actual-weight gates.
No originality beyond the sources checked is asserted. The separate
informal audit above is not a Mathlib formalization or a global resolution.
