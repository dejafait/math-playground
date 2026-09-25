# Affine locator incidence at four omissions

Date: 2026-09-26. One focused step in the pinned affine-line model.

## Gap, intermediate target, and decision test

For C=RS[F_(97^20),H,8], with H the order-16 subgroup of F_97^*,
the cell [1/4,5/16) has bounds 10/q and 69/q. The budget permits
fifteen challenges; sixteen would prove unsafety. The intermediate target
is an upper count of sixteen, with precise equality conditions, for
affine eight-moment pencils whose 4-by-4 Hankel determinant and all
sixteen fixed-coordinate locator polynomials are nonzero polynomials.
This could reduce a broad class to a single extremal count. Excluding or
constructing that equality case, treating pencils outside these hypotheses,
and resolving the ABF26 source correspondence would still remain.

The [official statement](https://proximityprize.org/) was reread today.
Its preliminary target, listed rates, and unspecified field-size
qualification are unchanged. The July paper remains uncertified; no
identification with its error is made. Existing local edits to the three
overview/checkpoint files and the L009 artifacts were inspected and are
preserved. No other notebook is edited. Exploration count starts at zero.

L009 excludes full subgroup orbits but does not bound a general pencil.
L008 supplies ten challenges, below sixteen. The distance hypotheses
behind L006 and L007 fail at four omissions. Thus this is a different
mechanism rather than a repeat of the orbit search or distance argument.

Continue if a uniform root-incidence proof handles singular parameter
values within the stated class and gives usable necessary and sufficient
conditions for sixteen. Abandon the claimed bound if such values escape
the incidence count, or if the original same-support event is not controlled.
No finite search will be treated as an extension-field upper bound.

## Saved unfinished reasoning

Write s_j(T)=sigma_j(a)+T*sigma_j(b), j=1,...,8, and let
D(T)=det(s_(i+j+1)(T)) for 0<=i,j<=3. Append the row
(1,X,X^2,X^3,X^4) to the four moment rows of width five to define
L(T,X); its X^4 coefficient is D(T), and every L(T,x) has
T-degree at most four. At a parameter with a weight-four representative
e, Vandermonde factorization should give
L(T,X)=D(T)*product_(x in supp(e))(X-x), with D(T) nonzero.
At a representative of weight at most three the four moment rows have
rank at most three, so all sixteen coordinate locators vanish. Each
such parameter therefore consumes more of the common root budget.

The proposed incidence count is 4*N_4+16*N_<=3 <= 64. It would give
N_4+N_<=3 <= 16-3*N_<=3 and force all sixteen parameters in an
equality case to have exactly four errors. Equality would also require
every coordinate locator to have degree four, four distinct field roots,
and no roots wasted at parameters outside the decoding set. The reverse
implication, same-support failure, and possible multiplicity refinements
still need proof. These are working statements, not completed results.

## Proof refinement saved before auxiliary checks

At a weight-w parameter with w<=3, every 4-by-4 moment minor is
divisible by (T-gamma)^(4-w): in its multilinear expansion, fewer than
4-w perturbed rows leave more than w rows from a rank-w matrix.
Thus the refined count is

    4*N_4 + 16*N_3 + 32*N_2 + 48*N_1 + 64*N_0
        <= sum_(x in H) deg_T L(T,x) <= 64.

For the reverse locator test, D(gamma)!=0 makes L(gamma,X)/D(gamma)
the unique monic fourth-order recurrence polynomial for the eight moments.
If it has four distinct roots in H, solving the first four Vandermonde
equations gives error weights; the recurrence then reproduces all eight
moments, and D(gamma)!=0 forces each weight nonzero.

The same-support issue also has a direct argument. If the direction b
were a code restriction off a decoded error support A, its syndrome
would have a representative supported on A. The entire pencil would
then have representatives on that fixed set. For |A|<=3 this forces
D identically zero; for |A|=4 it forces L(T,x) identically zero for
x in A. Both contradict the hypotheses. Consequently every decodable
parameter in this class is bad on its full agreement support.

These arguments give equality precisely when every L(T,x) is a split
squarefree quartic and every parameter root has D!=0 and occurs for
exactly four coordinates. Equality would give sixteen distinct supports,
each of size four, with each coordinate occurring four times. An explicit
check against the two-block example and lower-weight multiplicities is
pending; no equality configuration or global bound is claimed.

## Completed assessment

The full proof in [L010](../lemmas/L010-affine-locator-incidence-bound.md)
establishes the weighted incidence bound over every finite field containing
H, with no restriction on the coefficients of a and b. It proves both
the inverse locator test and failure on the same agreement support.
Individual singular parameter values are included. Sixteen occurs exactly
when all coordinate locators are split squarefree quartics and each root
parameter has nonzero Hankel determinant and belongs to four locators.
This gives sixteen distinct four-error supports, each coordinate used four
times. Any failure of these equality conditions gives at most fifteen
within this class. No equality configuration has been found or excluded.

The auxiliary command `python3 scripts/locator-incidence/check.py`
uses exact arithmetic over F_97 and an independent interpolation test on
all 2517 supports of size at least twelve. The two-block example has ten
bad parameters and locator incidence 40 out of degree budget 64. Four
additional pencils have a sole prime-field bad parameter at zero, with
weights 0,1,2,3 and respective incidence costs 64,48,32,16. All five
satisfy the polynomial nonvanishing assumptions. The check verifies
the locator converse at all 97 parameters and the forced multiplicities.
A pencil on one fixed four-set has 97 decodable parameters but only four
bad ones; it has persistent coordinate roots and is correctly excluded.
These examples do not constitute an exhaustive search or determine their
counts over extension fields.

Outcome: ADVANCE. The intermediate target is proved, and consecutive
exploration turns reset to zero. The achieved upper count sixteen is
still one above floor(97^20/2^128)=15. The global error bounds remain
10/q and 69/q because identically singular pencils and persistent
coordinate roots have not been bounded here. The next direction is a
structured test of the equality case: four disjoint four-coordinate error
spaces can constrain candidate syndrome lines by ordinary linear algebra,
without the full-orbit equivariance that failed in L009. Its specific
test is the sole Next action in PROGRESS.md. No additional search was
performed in this step, and no complete challenge candidate is present.
