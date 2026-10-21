# L082 — Mixed nine-union pencils have at most fifteen bad parameters

## Hypotheses

Let F=F_(97^20), let H be the subgroup of order sixteen in F_97^*,
and let C=RS[F,H,8], with unit evaluation multipliers. Use the pinned
same-support event at 1/4<=delta<5/16. For words a_*,b_* in F^H write
sigma_j(z)=sum_(x in H) z(x)x^j, 1<=j<=8, and
s(T)=sigma(a_*)+T sigma(b_*). Let B be their actual finite bad set.

Use L041's **local converse**, without assuming sixteen-count equality,
with tau=0 and (n_01,n_02,n_12)=(2,1,0). Explicitly, take nine distinct
labels a,b,c,y,z_1,z_2,w_1,w_2,w_3 in H and supports

    A_0={a,b,c,y}, A_1={a,b,z_1,z_2}, A_2={c,w_1,w_2,w_3}.

Let U be their nine-label union. Choose distinct original finite
parameters gamma_0,gamma_1,gamma_2 in F, put
alpha_0=gamma_1-gamma_2, alpha_1=gamma_2-gamma_0,
alpha_2=gamma_0-gamma_1, and Q(X)=product_(t in H minus U)(X-t).
Choose lambda in F^* and p_a,p_b,p_c in F minus {0,1}. Define errors
e_i with zero coordinates off A_i by

    e_i(x)=lambda Q(x) b_(i,x)/alpha_i  (x in A_i),

where b_(0,a)=p_a, b_(1,a)=1-p_a,
b_(0,b)=p_b, b_(1,b)=1-p_b,
b_(0,c)=p_c, b_(2,c)=1-p_c, and b_(i,x)=1 at every singleton
coordinate of A_i. Require sigma(e_i)=s(gamma_i) for i=0,1;
L041 supplies the third equality. Equivalently choose words realizing
the syndrome pencil interpolating these first two errors. The words,
weights and original parameters may all lie in F; no rational chart is
assumed. All these gates are part of the hypotheses.

## Conclusion

The full bad set satisfies |B|<=15, including every finite lower-weight
error. This closes this mixed local row, conditional on the audited
L040 bound and its complete finite certificates. It does not give
universal nine-union extraction, the uniform triangle twelve bound,
other support-pattern bounds or a challenge resolution. The global
interval 11/q–16/q remains unchanged. The separate scoped critical audit
of 2026-10-14 found no defect in this application, as recorded below.

## Proof

### Entry without equality and standard inputs

The supplied gates are exactly L041's local-converse gates. Its audited
converse gives three distinct finite actual bad parameters gamma_i with
full errors e_i, independent coefficient syndromes sigma(a_*),sigma(b_*),
and D(gamma_i)!=0. Since A_0 intersect A_1 intersect A_2 is empty,
every label is absent from at least one A_i. L041's pointwise locator
formula then supplies a nonzero value of its coordinate locator at that
gamma_i. Thus D and every locator are nonzero **polynomials**, although
singular parameter values remain allowed. No equality-conditioned
forward assertion of L041 is used to obtain these premises.

Import L010's ker(sigma)=C, uniqueness of errors of weight at most four,
same-support badness, the integer bound |B|<=16, and its equality
consequence: if |B|=16, all sixteen errors have weight four and each
label belongs to exactly four of their supports. The identification of
B with the sparse-error parameters holds under the polynomial premises
just verified, so lower-weight and singular events remain in B.

Import the distance-nine theorem from J. I. Hall, *Notes on Coding
Theory*, GRS chapter, Theorem 5.1.1 and complete proof, printed pp. 63–64
of the [author-hosted chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
undated copy inspected in the October 13 assessment. Its hypotheses
are a field, distinct labels, nonzero multipliers and 0<k<=n.
Here F is a field, the sixteen H labels are distinct, all multipliers
are one and k=8, so every nonzero codeword has weight at least nine.
This known distance theorem is not reproved.

The six-label pair below consists of **base** errors of a mixed row.
L070's statement requires additional errors of an L057 triangle and
therefore cannot be invoked. We extend its audited affine-lift argument
in the next two paragraphs, using only the premises established above.
This repetition is needed to remove those triangle/additional-error
hypotheses; it is a REPRODUCTION specialization under the prior
SPECIALIZE coverage, not a claim of a new distance or shortening result.
L071 and its separate step-170 audit supply the application comparison.

### Pair lift, equal-vector exception and every cancellation

Set V=A_0 union A_1={a,b,c,y,z_1,z_2}, R=A_0 intersect A_1={a,b},
and Delta=gamma_1-gamma_0!=0. Define the vector-valued affine polynomial

    f(T)=((gamma_1-T)e_0+(T-gamma_0)e_1)/Delta.

It is zero off V, has f(gamma_i)=e_i for i=0,1, and satisfies
sigma(f(T))=s(T) as a polynomial identity: both sides are affine and
agree at two distinct field parameters. At T in B, let e_T be L010's
unique error of weight at most four. If e_T!=f(T), their difference is
a nonzero codeword, because their eight syndromes agree. With
m_T=|V intersect supp(e_T)|, distance gives

    9 <= wt(f(T)-e_T) <= |V union supp(e_T)|
      = 6+wt(e_T)-m_T <= 10-m_T,

hence m_T<=1. The fixed set V, rather than supp(f(T)), is used in
this upper bound. Every vanished lift coordinate, cancellation against
e_T and possible error using a vanished coordinate is covered. This
argument does not apply when e_T=f(T); that exception is essential.

Suppose |B|=16 and no T outside {gamma_0,gamma_1} has e_T=f(T).
The two base errors contribute four V incidences each, and the other
fourteen contribute at most one each. Their total is at most 22.
L010's equality balance requires 6*4=24. Therefore some original
finite eta distinct from gamma_0,gamma_1 has e_eta=f(eta).
Equality has already made e_eta full of weight four. At eta, the two
coordinates A_0 minus A_1={c,y} have values
e_0(x)(gamma_1-eta)/Delta!=0, and the two coordinates
A_1 minus A_0={z_1,z_2} have values
e_1(x)(eta-gamma_0)/Delta!=0. Consequently both coordinates in R
must vanish; no other cancellation can produce this four-error.

For x in R put r_x=e_1(x)/e_0(x) in F^*. The coordinate formula is

    f_x(T)=e_0(x)[gamma_1-r_x gamma_0+(r_x-1)T]/Delta.

If r_x=1 it is the nonzero constant e_0(x). Otherwise its only root
is (gamma_1-r_x gamma_0)/(1-r_x). At the forced eta the formula gives

    r_x=(eta-gamma_1)/(eta-gamma_0).

The denominator is nonzero. Thus |B|=16 forces r_a=r_b=r in
F minus {0,1}; nonzero follows from the full pair weights, and r=1
would force gamma_0=gamma_1. If the two ratios differ or either is one,
this necessary condition fails and L010's integer bound gives |B|<=15.
Fullness and balance were used only within this sixteen-count
contradiction, not to discard lower-weight parameters beforehand.

### Common-nonunit branch and the complete L040 application

It remains to handle r_a=r_b=r!=0,1, without assuming |B|=16. Put

    eta=(gamma_1-r gamma_0)/(1-r).

This lies in F in the original finite chart. Its differences from
gamma_0 and gamma_1 are Delta/(1-r) and r Delta/(1-r), respectively;
both are nonzero. The same coordinate formulas show that f(eta)
vanishes on R and is nonzero on every coordinate of
{c,y,z_1,z_2}. It is therefore a full four-error with syndrome s(eta).
L010 gives uniqueness and actual same-support badness at eta. In this
mixed pattern eta cannot equal gamma_2: uniqueness would then identify
its support {c,y,z_1,z_2} with A_2={c,w_1,w_2,w_3}, which is impossible.
The argument below only needs its distinction from gamma_0,gamma_1.

Verify L033's alternative **explicit-triple** hypotheses directly.
Partition V into pairs

    Z_1=A_1 minus A_0, Z_2=A_0 minus A_1, Z_3=R,
    t_1=gamma_0, t_2=gamma_1, t_3=eta.

For x in Z_1 let d_x=e_1(x)/Delta; for x in Z_2 let
d_x=-e_0(x)/Delta; for x in Z_3 let
d_x=e_0(x)(r-1)/Delta. Every d_x is nonzero. The displayed lift
then has f_x(T)=d_x(T-t_i) on Z_i and is zero off V. Its three
values at the distinct finite t_i are the actual full errors, with
supports V minus Z_i, and sigma(f(T))=s(T) holds in all eight moments.
Its coefficient vectors u,v in f(T)=u+Tv are independent: any linear
relation would give the same relation between sigma(a_*),sigma(b_*),
already independent by L041. Restriction to V loses no coordinates.
The field, H, code, cell, original finite chart and polynomial D/locator
premises are unchanged. This verifies every explicit L033 premise;
no L032 equality classification, L057 recovery formula, rational
descent or third additional-event assumption is used.

Import the audited L040 full-B bound for this explicit L033 lift. To
keep its cases visible, L033's accounting relative to t_1,t_2,t_3 is

    |B|=3+N_ext+N_3.

If N_3=0, L040's audited complete finite certificates give N_ext<=12,
hence |B|<=15. If N_3>0, L040's separate lower-weight branch imports
L010's multiplicity bound and gives |B|<=15 directly. That branch uses
no equality matching test. L033 also excludes weights at most two for
this explicit lift; more generally any such error already excludes
sixteen by L010. Every finite error is retained by this accounting,
including singular errors and vanishing coefficients on relaxed
four-support witnesses. No recount of L040's audited certificates is
needed for the unchanged fixed-field hypotheses. Together with the
unequal/unit-ratio branch this proves the conclusion.

### Sources, proof status and scope

The gate assessment, saved before this attempt, is
`drafts/literature/2026-10-13-mixed-nine-union-six-label-application.md`.
It compares the stronger inspected results and preserves the failures
ATTEMPTS/025,027,029,030. None is a stopped form of this mixed-base-pair
application. No new census, enlarged sweep, mathematical script or
cross-notebook input is used.

L033/L040 import the shortening formula from I. Marquez-Corbella and
R. Pellikaan, *A characterization of MDS codes that have an error
correcting pair*, FFAA 40 (2016), 224–245,
[DOI 10.1016/j.ffa.2016.04.004](https://doi.org/10.1016/j.ffa.2016.04.004),
accepted manuscript dated February 29, 2016, section 5, Definitions
5.1–5.2, Lemma 5.3 and following unnumbered GRS formula, printed pp. 7–8
([primary manuscript](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf)).
The assessed six/seven-deletion applications retain positive dimensions
and nonzero label differences. L041's seven-deletion application uses
the original nine labels and retains dimension one. The new pair
selection changes neither application; no generic shortening theorem
is reproved. L040's complete certificates and October 7 critical audit
are imported in their exact scope, not represented as new calculations.

The local result is established by this written specialization and
passed the separate critical audit below. It supplies a conditional
branch bound, not a complete UNVERIFIED CANDIDATE for the challenge.
The precise ABF26 event and parameter qualifications remain uncertified,
and other local patterns and arbitrary-family extraction remain open.

### Separate critical audit, 2026-10-14

Step 199 checked the existing proof under the prior EXPLORE scope in
`drafts/literature/2026-10-13-mixed-nine-union-fifteen-audit.md`.
No mathematical defect or missing application premise was found.
This is a REPRODUCTION audit, not a new bound, a repaired argument or
progress beyond the sources checked. The completed L010/L033/L040/L041
input audits are reused; L070/L071 are comparisons, not extra inputs.

**Local-converse entry.** The nine distinct labels give exactly the
three stated four-supports, with empty triple intersection and union
nine. The three original parameters make every alpha_i nonzero;
lambda, Q(x), p_x and 1-p_x are nonzero at each required coordinate.
At each label the normalized present weights sum to one, so the gated
errors satisfy L041's converse relation with its nonzero codeword
defect. Anchoring the first two moments therefore anchors the third.
The converse independently proves full weights, distinct actual base
events and independent coefficient syndromes. It does not import the
forward statement's equality assumption. L010's pointwise factorization
is available before polynomial nonpersistence: D(gamma_i) is nonzero,
and a base support omitting x gives ell_x(gamma_i) nonzero. Every x has
such an omission. Hence L010 applies to the original words and counts
all sparse finite errors, including singular and lower-weight ones.

**Lift and equality deficit.** Delta is nonzero, the two interpolation
coefficients sum to one, and their parameter-weighted sum is T. Thus
all eight syndrome identities hold identically. If the actual error
differs from f(T), their difference is a nonzero codeword. The fixed-set
estimate 9<=6+wt(e_T)-m_T<=10-m_T covers every cancellation and does
not require a nonvanishing lift on all of V. It is not used for equal
vectors. Only after assuming sixteen parameters does L010 supply
fullness and exactly four incidences at each label. With only the two
base equalities the incidence total is at most 22, against required 24.
The forced third equality is a finite member of B. Its four exclusive
coordinates are nonzero since it differs from both original parameters;
both shared coordinates must therefore vanish. Their displayed affine
formulas retain the constant case r_x=1 and give the same nonunit ratio
at both coordinates. This exhausts the complementary unequal/unit cases.

**Unconditional common-ratio branch.** The two differences
eta-gamma_0=Delta/(1-r) and eta-gamma_1=r Delta/(1-r) are nonzero.
The four exclusive weights are nonzero, both shared weights vanish,
and the syndrome is s(eta). L010 proves actual same-support badness
without a sixteen-count assumption. The support differs from A_2, so
sparse uniqueness also justifies the optional observation eta!=gamma_2.
No rationality or new affine chart is introduced.

For L033, Z_1,Z_2,Z_3 are disjoint pairs partitioning V. Each displayed
d_x is nonzero. Substitution gives f_x(T)=d_x(T-t_i) in all three
classes, including the minus sign on Z_2 and factor r-1 on Z_3.
Their three distinct finite roots give exactly the three full errors.
The coefficient syndromes are the original independent pair, hence
the coefficient vectors are independent too. This checks the explicit
alternative of L033; it needs neither L032's equality-conditioned
construction nor the triangle/additional-event premises of L070.

**Full-B transfer.** The field, subgroup, code, shifted moments,
radius cell and polynomial nonpersistence are precisely L040's.
L033 excludes weights at most two and accounts for every finite event
as 3+N_ext+N_3 relative to this new triple. When N_3=0, the audited
L040 certificate bound N_ext<=12 gives fifteen. When N_3>0, L010's
bound is |B|<=16-3N_3<=13, already recorded in L033; it implies
fifteen without the equality matching test. Thus no lower-weight event
or relaxed witness with vanishing weight is lost. There is no subtraction
of an unrelated base triple in this application.

The unchanged arbitrary-field distance/shortening specializations are
covered by the precise citations above and their saved inspected
extracts. The October 7 L040 audit covers both complete certificates
and its essential forward inputs. No application discrepancy requires
replay, and none is claimed here. No mathematical script or certificate
changed. Direct inputs remain L010, L033, L040 and L041; no DAG edge
changes. The validated local fifteen bound leaves arbitrary-family
extraction, the uniform triangle bound, other patterns and challenge
qualifications unresolved.

## Mathlib

The full mixed-pattern fifteen bound and the specialized pair-lift/count
assembly are **not checked**. Supporting GRS distance/shortening,
shifted-moment kernels, affine interpolation, sparse uniqueness and
incidence counting are **not checked** in Mathlib for this step.
The canonical inputs retain their stated coverage. No matching Mathlib
theorem, Lean verification or certified originality is claimed.
