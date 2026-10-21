# L066 — A full isolated triangle recovery bounds both-zero parameters by three

## Hypotheses

Use the full hypotheses of audited L057: F=F_(97^20), the fixed
order-sixteen H in F_97^*, nine distinct triangle labels, distinct
original finite gamma_i, lambda!=0, and
p(1-p)q(1-q)r(1-r)!=0. Use its actual syndrome pencil and retain
mu!=0,-1, E=rho-(1-rho)mu!=0, and all relaxed fourth weights.
Write P={a,b,c}, U for the nine-label union, and c_x=Q(x), where
Q is the product over H minus U. Write bold Y and bold Z for
L057's eight-component singleton moment vectors. Write instead

\[
Y_2=(X-y_1)(X-y_2),\quad Z_2=(X-z_1)(X-z_2),\quad
W_2=(X-w_1)(X-w_2),\quad S=Y_2Z_2W_2,
\]

and let \(\mathcal N=\operatorname{span}_F\{Z_2W_2,Y_2W_2,Y_2Z_2\}\)
be L065's quartic net. An isolated recovery means L057's two
projected vectors are nonzero and proportional. A both-zero recovery
means both projected vectors vanish and every restored lift gate passes.
Let R_00 denote the set of distinct additional original finite parameters
with a both-zero witness, allowing zero recovered weights.

For the first conclusion assume there is an actual additional isolated
recovery on a four-subset K_* disjoint from P whose four recovered
weights are all nonzero. Its original parameter and scalar are T_*,mu_*.
No descent of p,q,r or of the original chart is assumed.

## Conclusion

Under this full isolated-anchor hypothesis,

\[
                         |R_{00}|\le3.                         \tag{1}
\]

More explicitly, all both-zero scalars are roots of the single
nonzero polynomial Delta defined below, of degree at most three;
Delta(mu_*)!=0. This includes both branches of L065's quadratic
classification. Other recovered fourth weights can vanish.

Consequently, if an L057 pencil has thirteen distinct additional relaxed
recoveries, then at most three of them are both-zero, at least ten are
isolated, and at least four are isolated with supports disjoint from P.
This is a necessary restriction on a possible violation of twelve,
not an exclusion of that violation. Multiple isolated rows, other
patterns, arbitrary extraction and challenge-definition gaps remain.
A separate critical audit on 2026-10-11 found no mathematical defect
in this conditional scope; no complete candidate or stronger global
interval is claimed.

## Proof

### Assessed inputs and purpose

Use L057's full-moment recurrence and original-chart recovery, L065's
exact net classification and audited upper bound six on R_00, and
L010's moment factorization and sixteen-count equality consequences.
L060–L064 and their finite certificates are not inputs. The unchanged
ready triangle-count assessment covers this bounded specialization;
it supplies no matching simultaneous bound or certified originality.

The recurrence input is already imported in L057 from Przemek
Chojecki, *Shortening Bounds for Reed–Solomon MCA*, live author TeX
v9.2, July 17, 2026, DR2 (`drc:lem-locator-recurrence`) and
DR6–DRC (`drc:thm-exact-compiler`), source lines 2785–2935,
[author source](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex).
The mutable source is not certified identical to ePrint 2026/1463.
L057 verifies distinct nonzero labels, R=8, t=4, multiplier x and
all zero-direction cases; those hypotheses are unchanged here.
We do not reprove the general recurrence theorem. The additional work
is its restriction to the three-dimensional net and the use of one
actual full-weight anchor to prove a determinant is not identically zero.

### A division-free identity on the entire net

For f=\(\sum_{j=0}^4 f_jX^j\), including degree below four, define
\((\mathcal F_f n)_i=\sum_{j=0}^4f_jn_{i+j}\) for 1<=i<=4.
Put \(u_x=(x,x^2,x^3,x^4)^{tr}\), so
\(\mathcal F_f v_x=f(x)u_x\). For

\[
                    f=A Z_2W_2+B Y_2W_2+C Y_2Z_2,             \tag{2}
\]

the identities needed are

\[
\mathcal F_f\boldsymbol Y
 =-A\sum_{x\in P}c_xZ_2(x)W_2(x)u_x,\qquad
\mathcal F_f\boldsymbol Z
 =-B\sum_{x\in P}c_xY_2(x)W_2(x)u_x.                          \tag{3}
\]

Here no division by f(x) occurs. To prove the first, let
G_P=product_(x in P)(X-x) and R_Y=G_P Y_2. Since
Q G_P S=X^16-1, differentiating at the singleton y gives
\(c_y y=16/(G_P(y)S'(y))\). At x in P it gives
\(c_x x=16/(G_P'(x)S(x))\). The factors are nonzero because
all nine labels are distinct and nonzero. For 1<=i<=4 these identities
and (2) show

\[
 (\mathcal F_f\boldsymbol Y)_i
 +A\sum_{x\in P}c_xZ_2(x)W_2(x)x^i
 =16A\sum_{t:R_Y(t)=0}\frac{t^{i-1}}{R_Y'(t)}=0.              \tag{4}
\]

The final equality is the coefficient of X^4 in the standard Lagrange
interpolation formula for X^(i-1) at the five distinct roots of R_Y;
i-1<=3. The same argument on R_Z=G_P Z_2 proves the second identity,
with B replacing A. Thus (3) holds for every coefficient triple,
even if f vanishes at shared labels or loses its leading coefficient.

### The cubic determinant and its exact kernel

Let mu be an indeterminate over F and put

\[
d_a=1-(1+\mu)p,\quad d_b=-\mu q,\quad d_c=r,\qquad
N(\mu)=\boldsymbol Z-\mu\boldsymbol Y+\sum_{x\in P}c_xd_xv_x.
                                                                    \tag{5}
\]

This is exactly L057's syndrome numerator for eligible scalars. Define
the 3-by-3 matrix M(mu), with rows x=a,b,c, by

\[
 M_x(\mu)=\big((d_x+\mu)Z_2(x)W_2(x),\quad
                  (d_x-1)Y_2(x)W_2(x),\quad
                         d_xY_2(x)Z_2(x)\big),\qquad
 \Delta(\mu)=\det M(\mu).                                  \tag{6}
\]

All entries have degree at most one, so deg Delta<=3 unless Delta
is zero. By (3), for f represented by (A,B,C),

\[
 \mathcal F_fN(\mu)
   =\sum_{x\in P}c_xu_x\,
                      \big(M_x(\mu)(A,B,C)^{tr}\big).        \tag{7}
\]

The three vectors u_a,u_b,u_c are independent: their first three
rows form a Vandermonde matrix times the nonzero diagonal a,b,c.
Also c_x!=0. Therefore, at every mu in F,

\[
 \mathcal F_fN(\mu)=0\quad\Longleftrightarrow\quad
                         M(\mu)(A,B,C)^{tr}=0.               \tag{8}
\]

L065 proves the three net generators independent by evaluation at
one singleton of each pair. Thus a nonzero coefficient triple always
gives a nonzero polynomial. No assumption on the rank of the three
pair quadratics was made, and no exceptional f(P)=0 case was removed.

If mu is an eligible both-zero recovery scalar with witness K, then
L065 gives f_K in the net and L057 gives
\(\mathcal F_{f_K}N(\mu)=0\). Equations (8) and (6) imply
Delta(mu)=0. This argument uses actual recovered moments and allows
zero fourth weights. Roots of Delta are only a necessary condition;
they need not supply split quartics, lifts or eligible finite parameters.

### The isolated anchor excludes the zero polynomial

At the anchor, L057 gives
\(N(\mu_*)=\sum_{k\in K_*}\omega_kv_k\) with every omega_k!=0:
the actual scaling lambda/(g E) is nonzero. L010's four-support
moment factorization shows that its degree-at-most-four recurrence
kernel is the one-dimensional space spanned by f_(K_*). Explicitly,
the four recurrence equations for any f say
\(\sum_{k\in K_*}\omega_k k^i f(k)=0\), i=1,...,4.
The shifted four-point Vandermonde and the four nonzero weights are
invertible, so all f(k)=0. A polynomial of degree at most four with
these four distinct zeros is a scalar multiple of f_(K_*).
This is precisely the full-weight specialization of L010's
factorization, not a claim of uniqueness at a lower-weight recovery.

If Delta(mu_*) were zero, a nonzero M(mu_*) kernel vector would by
(8) give a nonzero net polynomial in that recurrence kernel. Hence
f_(K_*) would belong to the net. Because K_* is disjoint from P,
L065's equivalence would make it both-zero, contradicting its isolated
projected test. Membership over F suffices here: L065's interpolation
identity holds over F, so it forces vanishing of the prime-field
projected vectors without requiring any descent argument.
Thus Delta(mu_*)!=0 and Delta is a nonzero polynomial of degree at
most three. It has at most three roots in F. L057's retained finite
change of variables T=gamma_0+g rho/E is injective in eligible mu;
duplicate supports or zero recovered weights cannot increase the
number of parameters. This proves (1), with all original exclusions.

### Consequence for a hypothetical thirteen-additional pencil

The three base events together with thirteen distinct additional
recoveries give sixteen distinct actual bad parameters by L057.
Its triangle nonpersistence verifies L010's hypotheses. L010 then
forces all sixteen errors to have full weight four, their supports
to be distinct, and each label to occur in exactly four supports.
Each label in P already belongs to two base supports. Thus the
thirteen additional supports have exactly six incidences with P,
and at most six of them can meet P. At least seven are disjoint
from P. This argument counts actual supports only after fullness.

L065 bounds all both-zero parameters by at most six, irrespective
of its quadratic branch. Thus one of those seven disjoint-P supports
is isolated; its weight is full by the preceding paragraph. It is
a valid anchor for (1), so in fact at most three of all thirteen
additional parameters are both-zero. Every successful L057 projected
case is either isolated or both-zero. Consequently at least ten are
isolated in total, and among the at least seven disjoint-P supports
at least four are isolated. No existence of such a pencil is inferred.

The anchor need not be rational in the original chart. No lower-weight
anchor is upgraded to full weight away from the sixteen-total threshold.
The proof does not assert a bound on isolated rows or that a nonzero
determinant alone bounds all disjoint-P recoveries. The analytic bound
uses no selected-label computation or unaudited table maximum.

### Separate critical audit (2026-10-11)

The approved audit checks (1) and the thirteen-additional consequence,
with direct mathematical inputs exactly L010, audited L057 and audited
L065. The recurrence import and its distinct-label, nonzero-multiplier,
R=8, t=4 specialization above are unchanged. The standard named
Lagrange interpolation formula is applied over F to five distinct
nodes; it needs neither a prime-field chart nor degree exactly four.
The following checks found no formula, hypothesis or counting defect.

**All four division-free rows.** At a Y singleton y, (2) gives
f(y)=A Z_2(y)W_2(y). Since
S'(y)=Y_2'(y)Z_2(y)W_2(y) and
R_Y'(y)=G_P(y)Y_2'(y), differentiation of Q G_P S=X^16-1
and y^16=1 give, separately for i=1,2,3,4,

\[
 c_y y^i f(y)=\frac{16A y^{i-1}}{R_Y'(y)}.
\]

At a shared node x, R_Y'(x)=G_P'(x)Y_2(x), so the same
differentiation gives

\[
 c_x Z_2(x)W_2(x)x^i=\frac{16x^{i-1}}{R_Y'(x)}.
\]

Their sum is (4). The five-node interpolation formula for
X^j, j=0,1,2,3, has zero coefficient of X^4, proving the
vanishing in every row. At a Z singleton use
f(z)=B Y_2(z)W_2(z) and R_Z=G_P Z_2; the shared-node
calculation replaces Y_2 by Z_2. This proves both signs in (3).
All displayed derivative denominators are nonzero products of
distinct label differences; 16 is nonzero in characteristic 97.
No f(x) or leading coefficient has been divided by. In particular,
the calculation admits f(P)=0, degree loss, A=0 or B=0, and the
dependent-quadratic branch of L065.

**Exact matrix kernel.** For each x in P, expanding (7) gives

\[
 d_x f(x)+\mu A Z_2(x)W_2(x)-B Y_2(x)W_2(x)
 = (d_x+\mu)A Z_2(x)W_2(x)
   +(d_x-1)B Y_2(x)W_2(x)+d_x C Y_2(x)Z_2(x).
\]

This verifies every column of (6) against the actual numerator (5).
The first three entries of u_a,u_b,u_c have determinant
abc(b-a)(c-a)(c-b), for this ordering, which is nonzero.
Multiplication by the three nonzero c_x preserves independence,
so vanishing of all four recurrence entries is exactly (8).
Evaluation at y_1,z_1,w_1 proves independence of the net generators
even when Y_2,Z_2,W_2 themselves are dependent. Thus a nonzero
matrix-kernel vector gives a nonzero polynomial of degree at most four.
Each eligible both-zero witness has its monic support quartic in this
net by L065 and annihilates its actual N by L057. It therefore supplies
a root of Delta even if some of its recovered fourth weights vanish.
No converse from a determinant root to a recovery is used.

**Nonvanishing at the actual anchor.** L057 (17) says
s(T_*)=lambda N(mu_*)/(gE_*), with lambda,g,E_* nonzero.
Its recovered numerator weights omega_k=(gE_*/lambda)e_*(k)
are consequently nonzero at all four distinct nodes of K_*.
For any degree-at-most-four f annihilating that numerator, the full
four recurrence rows are

\[
 \sum_{k\in K_*}k^i\omega_k f(k)=0,\qquad i=1,2,3,4.
\]

Their coefficient determinant is a four-node Vandermonde determinant
times product_(k in K_*) k omega_k, hence nonzero. All f(k)
vanish. Factoring out the four distinct linear factors shows that
any such nonzero f is a nonzero scalar multiple of f_(K_*);
degree below four cannot occur here. If Delta(mu_*)=0, (8) and net
generator independence supply precisely such a nonzero net f.
Therefore f_(K_*) is in the net over F. Since K_* misses P,
L065's two-way interpolation equivalence makes both of its projected
vectors zero. This contradicts its isolated test, in which both
vectors are nonzero. The argument proves Delta(mu_*)!=0 for the
given actual anchor, and does not replace that assertion by generic
nonvanishing or by lower-weight uniqueness.

**Parameters and threshold.** The now nonzero Delta has degree at
most three, so the polynomial root bound over F limits its distinct
roots to three. For two eligible scalars mu,nu,

\[
 T(mu)-T(nu)
 =\frac{g\rho(1-\rho)(\mu-\nu)}{E(mu)E(nu)}.
\]

Every factor outside mu-nu is nonzero by L057. This proves
injectivity in the unrestricted original finite chart. Roots with
mu=0,-1 or E=0 are excluded; failed lifts are excluded; repeated
support witnesses cannot add parameters. These exclusions can only
reduce R_00. A full anchor also cannot have a different both-zero
four-support witness: L010's sparse-error uniqueness makes that witness
equal to its full support K_*. Other parameters may have lower-weight
or duplicate witnesses without affecting the root bound.

For thirteen distinct additional relaxed recoveries, L057 supplies
thirteen actual bad parameters different from the three actual base
parameters, and its L041 input supplies nonzero D and every nonpersistent
locator. L010's bound and equality consequence therefore apply to all
sixteen. Fullness, support distinctness and coordinate degree four
are obtained before counting witnesses as supports. Each P label
is in exactly two base supports, leaving two additional incidences
per P label and six in total. Hence at most six additional supports
meet P, leaving at least seven disjoint-P supports. L065's bound six
on all both-zero parameters forces one of these seven to be isolated;
it has full weight by L010 and is a valid anchor. Applying (1) gives
at most three both-zero parameters, at least thirteen-minus-three=ten
isolated parameters overall, and at least seven-minus-three=four
isolated disjoint-P parameters. At this threshold every parameter has
a unique full support, so the isolated/both-zero counts are unambiguous.

The audit establishes the existing conditional restriction, with no
new count or dependency. It uses no selected-label certificate, rational
original chart, unproved pair/table bound, or hypothesis that thirteen
recoveries exist. Multiple isolated recoveries and the uniform twelve
bound remain open, as do other patterns, extraction and challenge
definitions. Full matching and supporting Mathlib coverage remain
not checked. This is local validation beyond the inputs used, not a
claim of certified originality or progress beyond unread sources.

## Mathlib

The full matching net/anchor bound is **not checked** in Mathlib.
Supporting mathematics consists of Lagrange interpolation, Vandermonde
invertibility, determinant/kernel equivalence and the polynomial root
bound; exact Mathlib theorem names for these are not checked here.
No absence, formal-verification or certified-novelty claim is made.
