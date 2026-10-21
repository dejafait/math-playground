# L046 — Shared outside pairs force opposite tags and a cross-ratio

## Hypotheses

Use the full local tau=1 setup and gates of L043, over F=F_(97^20)
with H the order-sixteen subgroup of F_97, k=8 and the pinned cell.
Thus the distinct labels give

    A_0={h,d,y_1,y_2}, A_1={h,d,z_1,z_2}, A_2={h,w_1,w_2,w_3},
    B={h,d,y_1,y_2,z_1,z_2}, O=H minus B,
    Q(X)=product_(x in H minus (A_0 union A_1 union A_2))(X-x),
    c_x=Q(x), W(X)=product_(i=1)^3(X-w_i).

The original finite gamma_i are distinct, lambda!=0 and
p*q*(1-p-q)*r*(1-r)!=0. All these free quantities may lie in F.
Consider distinct original finite parameters admitted by L043 (4)–(7)
on nonuniversal witnessing four-sets K and K', excluding the three
stipulated supports and K_*. Do not impose its fourth-weight gate (9).
Retain mu,nu!=0,-1, E(mu),E(nu)!=0 and every quotient case from L043.
Assume these two witnesses overlap B exactly once each:

    K={b} union S, K'={b'} union S',
    b,b' in B, S,S' subsets of O, |S|=|S'|=3.

No twelve-count premise, equality, prime-field free weights, rational
original chart or finite universal lift is assumed.

## Conclusion

The triples S,S' are distinct. If |S intersect S'|>=2, their intersection
has size exactly two, and the tags must be opposite singleton types:
one y_i and one z_j. Interchange the two witnesses if necessary to write
b=y_i, b'=z_j, and let y and z denote the other y-label and other z-label.
Then necessarily

    r*q/((1-r)*p) = (h-y)*(d-z)/((h-z)*(d-y)).             (1)

All denominators are nonzero. The right side belongs to F_97 and is
not one. For fixed p,q,r and the six B labels, the permissible pairs
of y- and z-tags in (1) form a matching: there are at most two such
pairs, with no shared tag. This restricts tag types, not the number
of support pairs realizing one type.

In particular, if rq=(1-r)p, all outside triples from distinct
nonuniversal overlapping candidates meet pairwise in at most one label.
This applies whenever L043's universal finite-lift gates hold, but needs
only their weight equation; it also applies when E_*=0 excludes that lift.
The same no-repeated-pair conclusion holds if rq/((1-r)p) is not in F_97.

This is an intermediate uniform recovery restriction toward eleven,
not an eleven bound or a twelve-candidate counterexample. It does not
handle candidates whose supports avoid B, force a repeated pair to
exist, or bound all families with no repeated pair. It is a local result
under the saved EXPLORE assessment, without a claim of certified
originality beyond the sources checked. Separate critical audit remains.

## Proof

### Recover the five evaluation equations from full moments

L043 (4)–(7), before its fourth-weight gate, puts the moment vector

    N=Z-mu*Y+c_h*(q-mu*p)*v_h+c_d*(1-(1+mu)*r)*v_d

in the span of K. Define the word n supported in B by

    n_x=c_x*a_x(mu),
    a_y1(mu)=a_y2(mu)=-mu, a_z1(mu)=a_z2(mu)=1,
    a_h(mu)=q-p*mu, a_d(mu)=1-r-r*mu.

Let omega be the recovered word supported in K, allowing zero weights.
Its full eight moments equal N by L043, so sigma(n-omega)=0. L010's
kernel identity gives a polynomial P of degree at most seven evaluating
to n-omega on H. This word is nonzero: at least three of the four
singleton labels are outside K, and n has nonzero coefficients at all
four. The word vanishes on O minus S, which consists of seven labels.
The root bound and factor theorem therefore give

    P(X)=u product_(o in O minus S)(X-o), u!=0.

For f_S(X)=product_(s in S)(X-s), the factorization
product_(o in O)(X-o)=Q(X)W(X) implies, for x in B minus {b},

    a_x(mu)*f_S(x)=u*W(x).                              (2)

Here we used P(x)=n_x and cancelled Q(x)!=0. All f_S(x) and W(x)
are nonzero at these labels, so (2) also proves a_x(mu)!=0 there;
no such nonvanishing was presumed at the tag. Repeating for K' gives

    a_x(nu)*f_S'(x)=u'*W(x), x in B minus {b'}, u'!=0.   (3)

This justifies the earlier draft's equation afresh without using it as
a theorem input. It uses the full-moment membership already proved in
L043, not an unchecked truncated recurrence or a reproof of its imported
compiler. Its recurrence input is Chojecki, *Shortening Bounds for
Reed–Solomon MCA*, live author TeX v9.2, July 17, 2026, source lines
2785–2935, `drc:lem-locator-recurrence` (DR2) and
`drc:thm-exact-compiler` (DR6–DRC), as inspected and specialized in L043
([author source](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex)).
The new calculation couples two actual recoveries, which the cited
fixed-support compiler does not count simultaneously.

### Repeated pairs require opposite singleton tags

By L043 (5), distinct original parameters have distinct mu,nu. Indeed,
equality of their gamma_0+g*rho/E values, whose numerator g*rho is
nonzero, gives equal E; its slope rho-1 is nonzero, giving mu=nu.

Suppose first S=S'. If at least one z-label is outside {b,b'}, equations
(2)–(3) at that label force u=u'. If a y-label is also outside them,
these equations then force mu=nu, a contradiction. The only uncovered
possibilities have both tags collectively removing both y-labels or
both z-labels. If b,b' are the two y-labels, the common z-labels give
u=u', and the common d-label gives 1-r-r*mu=1-r-r*nu, again mu=nu
since r!=0. If b,b' are the two z-labels, the common y-labels give
u/u'=mu/nu. The common d-label then yields

    (1-r-r*mu)*nu=(1-r-r*nu)*mu,

so (1-r)*(nu-mu)=0, again impossible. Thus S!=S'. This argument includes
coincident tags; they leave a common y and z. No division by a vanishing
h or d coefficient has occurred.

Now suppose their intersection has at least two elements. They are
three-sets and distinct, hence

    S=R union {c}, S'=R union {e}, |R|=2, c!=e.

Put kappa=u/u'!=0. At every x in B minus {b,b'}, cancellation of the
common nonzero factors in (2)–(3) gives

    a_x(mu)*(x-c)=kappa*a_x(nu)*(x-e).                 (4)

If both z-labels are common, (4) says the linear polynomial
(X-c)-kappa*(X-e) has two distinct roots. It would be zero, implying
kappa=1 and c=e, impossible. Thus one tag must be a z-label. If both
y-labels are common, the same argument applied to
mu*(X-c)-kappa*nu*(X-e) gives mu=kappa*nu and then c=e, since
mu!=0. Thus one tag must be a y-label. There are just two tags, so
these are exactly the opposite singleton types asserted.

### Retain both shared-label recovery equations

Order the witnesses so b=y_i and b'=z_j, and let y,z be their other
singleton labels. The common B labels are exactly y,z,h,d. Set

    U(X)=(X-c)-kappa*(X-e),
    V(X)=mu*(X-c)-kappa*nu*(X-e).

Equation (4) at z,y respectively gives U(z)=0 and V(y)=0.
Neither polynomial is identically zero: that would give c=e by the
coefficient comparisons above. Each is linear with a root, so

    U(X)=a*(X-z), V(X)=v*(X-y), a*v!=0.

At h,d equation (4) becomes

    q*U(h)=p*V(h), (1-r)*U(d)=r*V(d).

All four evaluations in these equations are nonzero since the B labels
are distinct. Put eta=v/a. The gates p,r,1-r!=0 give

    q/p=eta*(h-y)/(h-z),
    (1-r)/r=eta*(d-y)/(d-z).

Division proves (1), with all its denominators justified. Its right
side differs from one because the numerator of their difference is

    (h-y)*(d-z)-(h-z)*(d-y)=(h-d)*(y-z)!=0.

For fixed y, equality of the right sides for z and z' would force
(d-z)/(h-z)=(d-z')/(h-z'); cross multiplication and h!=d give z=z'.
For fixed z, the identical calculation with (h-y)/(d-y) forces uniqueness
of y. Complementation within the two y-labels and within the two z-labels
is bijective. Hence the permissible tag pairs form a matching of size
at most two. This is not a bound of two on repeated outside pairs.
All no-repeated-pair consequences now follow directly from (1).

The proof retains relaxed recovered weights, all original finite gates,
and arbitrary extension-field free weights. L045 is not a proof input:
its twelve profiles motivate the application, but were not needed in
this two-candidate argument. No conclusion about equality, a finite
universal lift or the main challenge is inserted as a premise.

## Mathlib

Full two-candidate cross-ratio restriction and its tag-matching consequence:
**not checked**. Supporting polynomial root bounds, Vandermonde/kernel
identities and elementary field algebra: **not checked** in Mathlib for
this step. The informal inputs are L010 and audited L043, with the latter's
precise imported recurrence cited above. No absence claim, Lean proof or
independent critical audit is asserted.
