# Lemma 510: aggregate positivity without conserved pairwise allocation

## Hypotheses

Set h=11/16 and r=21/16. For c in {h,-h} and real x define

    K_c(x)=2((x-c)^2-1)/((x-c)^2+1)^2.

For real x other than +/-r put

    H(x)=K_h(x)+K_{-h}(x)+1/(x+r)^2+1/(x-r)^2.

An allowed allocation consists of four nonnegative real constants
alpha_h, alpha_{-h}, beta_h, beta_{-h}, satisfying

    alpha_h+alpha_{-h}<=1,    beta_h+beta_{-h}<=1.

Each conjugate-pair displacement and each real-zero budget is one.
No actual-Xi configuration or entire function with fractional zero
multiplicities is assumed.

## Conclusion

H(x)>0 for every real x!=+/-r. Nevertheless there is no allowed
allocation for which both expressions

    K_c(x)+alpha_c/(x+r)^2+beta_c/(x-r)^2

are nonnegative at every such x. Indeed, the c=h expression at
x=7/16 is at most -400/14161<0 for every allowed allocation.

Thus aggregate positivity does not imply this conserved pairwise
allocation condition, even in the nominated symmetric two-pair block.
The obstruction is stronger than shared-budget competition: a single
pair fails even if given both full unit budgets. No separation between
joint feasibility and individual full-budget feasibility is claimed.
This is a finite first-sign statement, not an RH result.

## Proof

### Clearing denominators on the entire domain

Write

    A(x)=(x-h)^2+1=x^2-(11/8)x+377/256,
    B(x)=(x+h)^2+1=x^2+(11/8)x+377/256,
    M(x)=x^2-r^2=x^2-441/256,
    D(x)=A(x)^2 B(x)^2 M(x)^2.

A(x), B(x)>=1 on the real axis, and M(x)!=0 precisely when
x!=+/-r. Thus D(x)>0 on the full domain of H; no sign can change
when multiplying or dividing by it there. The real-root terms sum to

    1/(x+r)^2+1/(x-r)^2=2(x^2+r^2)/M(x)^2.

Consequently the exact polynomial identity is

    D(x)H(x)
      =2((x-h)^2-1)B(x)^2 M(x)^2
       +2((x+h)^2-1)A(x)^2 M(x)^2
       +2(x^2+r^2)A(x)^2 B(x)^2
      =Q(x^2)/549755813888,                              (1)

where, in increasing powers of y,

    Q(y)= 1445312501451
         -16326866594048 y
         +61357440761856 y^2
         -566298148864 y^3
         -2203318222848 y^4
         +3298534883328 y^5.                             (2)

The first equality follows by the displayed common denominator;
expansion of the three explicitly given polynomials gives the second.
The exact-rational script below records their full coefficient arrays.

### A strict positivity certificate for all y>=0

Put S=50000000000000 and write Q(y)=q(y)+y^2 R(y), where

    q(y)=1445312501451-16326866594048 y+S y^2,
    R(y)=11357440761856-566298148864 y
         -2203318222848 y^2+3298534883328 y^3.

With c1=-16326866594048 one has the exact identity

    4S q(y)=(2S y+c1)^2+22495927510359459970973696.       (3)

Both S and the constant remainder are strictly positive, so q(y)>0
for every real y. For 0<=y<=1, the two negative terms of R are
bounded below by their coefficients, and its cubic term is nonnegative.
It follows that

    R(y)>=11357440761856-566298148864-2203318222848
         =8587824390144>0.                              (4)

For y>=1, y<=y^3 and y^2<=y^3. Multiplication by the two negative
coefficients reverses those inequalities, hence

    R(y)>=11357440761856
          +(3298534883328-566298148864-2203318222848)y^3
         =11357440761856+528918511616 y^3>0.             (5)

Equations (3)--(5) cover every y>=0, including y=0 and y=1.
They prove Q(y)>0 there. Since x^2>=0 for every real x,
(1) and D(x)>0 prove H(x)>0 throughout its asserted domain.

At either excluded point +/-r the corresponding real-root summand
tends to +infinity, while the other three summands stay bounded
(r>0 and A,B never vanish on the real axis). These points remain
excluded; the proof does not extend H to a finite value there.
Finally direct division in the original four summands gives

    lim_(|x|->infinity) x^2 H(x)=2+2+1+1=6.

Thus the all-real assertion has no missing tail, but it supplies no
uniform positive constant lower bound as x tends to infinity.

### Excluding every allocation

Nonnegativity of the other allocation constants and the two budget
inequalities imply alpha_h<=1 and beta_h<=1. At the allowed point
s=7/16, which differs from both +/-21/16, exact evaluation gives

    s-h=-1/4,       K_h(s)=-480/289,
    1/(s+r)^2=16/49,    1/(s-r)^2=64/49.

Every allowed allocation therefore satisfies

    K_h(s)+alpha_h/(s+r)^2+beta_h/(s-r)^2
      <=-480/289+16/49+64/49
       =-400/14161<0.                                  (6)

This contradicts even the c=h inequality required for feasibility.
The argument covers all four constants; it neither assumes a symmetric
allocation nor derives one by averaging. The second pair's inequality
need not be tested to obtain the contradiction. Equations (1)--(5)
retain both signed pair terms and prove that their aggregate is positive.

### Verification, source comparison and limitations

Run from the notebook:

    python3 scripts/signed-allocation/finite_grid_separation.py

The program writes the complete certificate to
`scripts/signed-allocation/finite-grid-separation-certificate.json`.
It nominates grid points using samples m/2000, -10000<=m<=10000,
then stops at the first point with the exact certificate (1)--(6).
The lexicographic prefix contains 341 points, ending at (j,k)=(11,21).
Of the preceding 340 points, 182 have exact rational negative-H
witnesses and 158 remain unresolved. An earlier numerical-only pilot
sampled 450 grid points through (15,2), yielding eight nominations but
no certificates; its bounds and nominations are recorded in the artifact.
No exact certificate search was performed after (11,21), and grid points
after (15,2) were not sampled even numerically.
No equivalence or feasibility conclusion follows from those unresolved
or untested points. All-real positivity of the selected point follows
from the polynomial proof, not from its numerical screen. The certificate
has 11 successful exact checks and no failures; this is auxiliary
evidence from the original calculation.

An independent audit on 30 October 2026 reproduced all coefficients
and bounds above, using a separate integer-polynomial derivation rather
than importing the generator or repeating its grid. Specifically, put
y=x^2, U=256y+377, and

    C=(256A)(256B)=U^2-352^2 y
      =65536y^2+69120y+142129.

Then 256A=U-352x, 256B=U+352x and 256M=256y-441. Consequently

    ((256A)-512)(256B)^2+((256B)-512)(256A)^2
      =2UC-2048U^2+1024C.

Substituting this into the common-denominator numerator in (1) gives

    Q(y)=(2UC-2048U^2+1024C)(256y-441)^2
         +(256y+441)C^2,

because 256^5=2*549755813888. Expanding this expression gives
all six coefficients of (2). The denominator is independently
C^2(256y-441)^2/256^6, and its full coefficients agree with the saved
certificate. The range estimates (4)--(5) can also be checked through
explicit nonnegative remainders. With a=566298148864 and
b=2203318222848, they are

    R(y)-8587824390144
      =a(1-y)+b(1-y^2)+3298534883328y^3       (0<=y<=1),
    R(y)-(11357440761856+528918511616y^3)
      =a(y^3-y)+b(y^3-y^2)                  (y>=1).

Every displayed summand on each right side is nonnegative on its
range; in the second range y^3-y=y(y-1)(y+1) and
y^3-y^2=y^2(y-1). Thus the audit verifies the complete unbounded
domain, not a finite sampling surrogate. Equation (6) still uses only
the original nonnegative budgets, without a symmetry assumption.

The independent reproduction command is

    python3 scripts/signed-allocation/l510_independent_audit.py

Its complete evidence is `scripts/signed-allocation/l510-independent-audit.json`:
31 exact checks pass, with no failures. This verifies the fixed finite
claim and the selected certificate, not the original grid's screening
history, the external manuscripts or any actual-Xi application.

The saved assessment
`drafts/literature/2026-10-30-shared-budget-finite-test.md` covers this
exact finite grid under EXPLORE. Its reused comparison inspected
Csordas, *Fourier transforms of positive definite kernels and the
Riemann xi-Function*, arXiv:1309.0055v2, Proposition 2.2 equation (2.3),
and Proposition 2.3 ([primary text](https://arxiv.org/html/1309.0055v2)).
That signed logarithmic-derivative identity explains the zero-block
interpretation but supplies no conserved fractional allocation or sign.
The present proof is standalone rational algebra and imports no
nontrivial sign conclusion. The compared zero-count and all-order
results likewise do not establish this allocation conclusion; no
novelty certification or source-manuscript audit is asserted.

L509 is an isolated-pair benchmark and L251/L257 are masking contrasts,
not mathematical inputs to this proof. L354/L471/L508 route stops remain
in force. Actual-Xi geometry, a convergent collective assembly, unmatched
pair mass and all higher signs remain unproved. The finite obstruction
only warns that a pairwise sufficient criterion can lose positive
contributions of other signed pairs. The fixed finite statement and
selected certificate passed the independent audit described above;
this is local verification, not an originality certification.

## Mathlib

Full-result and supporting-identity coverage is unchecked. No absence
claim or matching theorem name is asserted. The proof uses elementary
rational and polynomial arithmetic and inequalities on the real axis.
