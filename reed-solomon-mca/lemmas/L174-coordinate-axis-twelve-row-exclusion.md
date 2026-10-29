# L174 — Coordinate-axis exclusion for twelve fully gated rows

## Hypotheses

Let E be any extension field of k=F_97. Put

S={1,8,12,18,22,27,33},
J={47,50,64,70,75,79,85,89,96}, and H=S union J,

the order-sixteen subgroup of k^*. Use the shifted moment map
M:E^H -> E^8, M(w)_d=sum_(x in H) w_x x^d for 1<=d<=8.
A vector on S is extended by zero to H when M is applied.

Let A_j=I_j union K_j, 1<=j<=12, be twelve distinct supports with
I_j subset S, K_j subset J and |I_j|=|K_j|=2. Assume the family is
linear (distinct supports intersect in at most one label) and every
label of H has integer degree at most four. Set

g_j(X)=product_(y in J minus K_j)(X-y), O_j=S minus I_j.

Choose any z_j in O_j and use L109's four covectors
(Q_j w)_x=g_j(z_j)w_x-g_j(x)w_(z_j), x in O_j minus {z_j}.
Suppose a two-dimensional subspace L of E^S has all the following
properties:

- E e_i subset L for some i in S, where e_i is the coordinate vector;
- rank(Q_j restricted to L)=1 for every j;
- on the unique line L intersect ker Q_j, a nonzero h_j satisfies
  lambda_j=h_(j,z_j)/g_j(z_j) != 0 and
  h_(j,x)-lambda_j g_j(x) != 0 for both x in I_j.

The gates are homogeneous, so the choice of h_j does not matter.
If an original basis/chart is prescribed, its finite-direction gates
may additionally be imposed; the conclusion holds even without them.
No descent, genericity, finite-field assumption on E, or coding
realization is assumed. Linearity of the supports is retained from the
approved domain but is not needed in the proof.

## Conclusion

No such L exists, for any i in S or extension E/k. Thus no plane in
this coordinate-axis subclass can pass all original L109 gates for
twelve rows in the stated domain, in any prescribed original finite
chart. The contradiction is a required locator multiplicity of at
least 96 against an available degree of at most 64.

This is an applicability specialization of L010/L109, not a new general
coding theorem. L076 recorded the same 96-versus-64 mechanism for a
different incidence family; neither its unaudited conclusion nor its
automatic-fullness argument is an input here. There is no reduction of
arbitrary planes to this subclass and no pruning of the saved cover.

## Proof

### Moment transport and full recovered errors

The moment and Vandermonde identities of L010 are matrices over k.
Their nonzero eight-column minors remain nonzero in E. In particular
any at most eight moment columns are independent, and M restricted
to E^S is injective. Hence M(L) is a two-dimensional syndrome space
containing m_i=M(e_i), rather than a collapsed line.

The code C_E of degree-less-than-eight evaluations on H equals ker M.
For clarity about the changed field hypothesis, the annihilation of
the eight evaluation monomials by M is the same identity over k as
in L010 and persists in E. Both spaces have dimension eight, since
M has rank eight and evaluation is injective. Thus their inclusion is
equality over E. Sparse representatives of size at most four remain
unique: their difference has support of size at most eight and M
annihilates it, contradicting eight-column independence unless it is
zero. This justifies scalar extension of these specific L010 facts;
it does not apply a finite-field event-count formula to an infinite E.

The standard GRS distance input, when expressed as distance of C_E,
is nine. The precise imported result is J. I. Hall, *Notes on Coding
Theory*, Chapter 5, [Theorem 5.1.1, printed pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf).
It permits any field, distinct evaluation labels, nonzero multipliers
and positive dimension at most the length: here these are E, sixteen
distinct nonzero labels, unit multipliers and dimension eight. No new
general distance theorem is asserted or needed. L109's shortening
normalization is kept verbatim; we use its explicit recovery identity,
not a new shortening theorem.

All g_j values on S union K_j are nonzero, as their roots are precisely
J minus K_j. Rank one gives dim(L intersect ker Q_j)=1. The equations
Q_j h_j=0 give h_(j,x)=lambda_j g_j(x) on O_j, including z_j.
Define e_j in E^H by

    (e_j)_x = h_(j,x)-lambda_j g_j(x)  for x in I_j,
    (e_j)_x = -lambda_j g_j(x)          for x in K_j,
    (e_j)_x = 0                         otherwise.

On O_j, on I_j, on K_j and on J minus K_j separately, these formulas
give the complete identity

    h_j-e_j=lambda_j (g_j(x))_(x in H).

The right side is in C_E since deg g_j=7. Thus M(h_j)=M(e_j).
Both overlap gates and lambda_j!=0 imply supp(e_j)=A_j, of size four.
In particular this is full recovery, not just a projected kernel test.

### Thirteen distinct directions and an auxiliary chart

The lines E h_j are pairwise distinct. If h_j=c h_l for a nonzero
c, then M(e_j-c e_l)=0. Its support has size at most eight, so it is
zero by column independence. Fullness then gives A_j=A_l, a
contradiction. They also differ from E e_i: if h_j=c e_i, then
M(e_j-c e_i)=0 on at most five coordinates, forcing e_j=c e_i,
contrary to its full four-support. This includes every i in S and
all possible overlap positions; no nonzero lambda branch is divided
away without its explicit hypothesis.

There are thirteen distinct E-rational lines in L under consideration.
The projective line of L has at least 98 points because E contains k.
Choose an omitted line outside these thirteen, a nonzero v on that
line, and u independent of v. Each h_j has a unique projective
normalization h_j/alpha_j=u+gamma_j v with alpha_j!=0. The axis
similarly gives c e_i=u+gamma_0 v with c!=0. All thirteen gamma values
are finite elements of E and are distinct. Define a,b in E^H by
extending u,v by zero off S. At gamma_j the error is e_j/alpha_j,
still full on A_j; at gamma_0 it is c e_i, of weight one. The
corresponding differences from a+gamma b are codewords, by their
moments. This chart is a proof device for an impossibility argument.
It asserts nothing about rationalizing or replacing a prescribed
original chart for a claimed survivor.

### Actual locator nonvanishing

Form s_d(T)=M(a)_d+T M(b)_d and the actual D(T), L(T,X) and
ell_y(T)=L(T,y) of L010. These are defined over E. Each ell_y has
degree at most four, because its coefficients are four-by-four minors
of a matrix whose entries are affine in T.

L010's pointwise full-error factorization is algebraic: for an error
of full support A at gamma, its moment matrix is

    R(gamma)=V_A diag(e_x x) W_A,
    (V_A)_(r,x)=x^r (0<=r<=3),
    (W_A)_(x,s)=x^s (0<=s<=4).

Consequently, over E just as over k,

    D(gamma)=det(V_A)^2 product_(x in A)(e_x x) != 0,
    L(gamma,X)=D(gamma) product_(x in A)(X-x).

This uses four distinct labels and nonzero full weights, both already
checked; the normalization by alpha_j does not change nonvanishing.
In particular D is a nonzero polynomial. For each y in H, at most
four of the twelve supports contain y, so at least eight omit y.
At any corresponding full event gamma_j the displayed formula gives
ell_y(gamma_j)!=0. Thus every actual ell_y is a nonzero polynomial.
Nonpersistence is proved before using a degree or root budget; it is
not inferred from an abstract exterior kernel. No sixteen-event or
t=0 completion is assumed.

### Finite multiplicity budget over every extension

We use only the thirteen selected parameters, rather than an event
count over all E. At the weight-one parameter gamma_0 the four-by-five
moment matrix R(gamma_0) has rank at most one by the same factorization.
For each four-by-four minor, write its matrix as B_0+(T-gamma_0)B_1.
In the determinant expansion by rows, a term of degree at most two
uses at least two rows of B_0, which are dependent because rank B_0<=1.
Every such term is zero. Thus every four-by-four minor is divisible
by (T-gamma_0)^3. Expansion of L along its last row shows this for
every coefficient in X, and therefore for every ell_y.

At a full event gamma_j, ell_y(gamma_j)=0 whenever y in A_j.
The gamma_j are mutually distinct and different from gamma_0. If
d_y is the number of selected supports containing y, the powers of
these distinct linear factors imply

    deg ell_y >= 3+d_y.

This uses only divisibility of finitely many pairwise coprime linear
factors in E[T]. It is valid for infinite and finite E alike, and
requires neither algebraic closure nor separability of other roots.
Since every ell_y is nonzero, summing gives

    64 >= sum_(y in H) deg ell_y
       >= sum_(y in H)(3+d_y)
        = 16*3 + 12*4 = 96,

a contradiction. This is exactly the relevant weight-one and
weight-four part of L010's weighted-locator argument. Its reproduction
is necessary to justify the all-extension specialization, since
L010's stated event-count theorem assumes a finite field.

### Same-support event qualification and limits

Although the contradiction needs only moments and locators, actual
same-support failure also follows over E. For any selected error e
at gamma with support A, suppose b agrees with a codeword on H minus A.
Subtract that codeword to obtain f supported on A with M(f)=M(b).
Then all pencil moments equal those of e+(T-gamma)f, supported on A
over E(T). If |A|=1, its moment rank forces D identically zero. If
|A|=4, appending the row indexed by any x in A to R(T) forces
ell_x identically zero. Both contradict the proved nonvanishing.
Thus these are actual same-support failures, when interpreted as the
pinned event, not just small error representatives.

For an actual L109 equality pencil, the implication to these plane
gates retains its original hypotheses: F=F_(97^20), this H, k=8,
unit multipliers, 1/4<=delta<5/16, syndromes in U_S, sixteen finite
bad parameters, t=0, nonzero actual D and every locator, arbitrary
original coefficients/chart, and the inherited representation and
finite-certificate qualifications. Such a pencil cannot have its
unique seven-coordinate lift plane contain a coordinate axis. This
conditional exclusion does not represent arbitrary pencils, identify
a pair, change any saved cover obligation, improve the global radius
interval or identify the pinned model with the unread ABF26 definition.

## Mathlib

Full matching Mathlib coverage of this coordinate-axis class exclusion
and of the weighted multiplicity bound is **not checked**. Coverage of
supporting base change, determinant, Vandermonde and polynomial
multiplicity results is **not checked**. No Lean verification or absence
claim is made. The imported general GRS statement is Hall Theorem 5.1.1
above; the specialized moment, recovery and multiplicity details are
written here. This proof has a same-step written hypothesis check in
the working record; a separate critical audit remains pending.
