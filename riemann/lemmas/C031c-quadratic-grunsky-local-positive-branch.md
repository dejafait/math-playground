# Corollary C031c: a local positive branch of the quadratic Grunsky equations

## Hypotheses

Let A,B,C,D,E be finite strictly positive real constants, and assume
A/C<160000. Use C031a's real family

    f_b(z)=z/(1+sum_(j=1)^5 b_j*z^(j+1)),

and its six complete polynomial defects h=(h11,h12,h13,h22,h23,h33).
In particular the three full column supports are 5,10,15; no omitted
column tail or univalence hypothesis is present. Set

    b*=(1,0,0,0,0), u=400,
    F(b,tau,400,v)=h(b)-tau*(A,400B,vC,160000C,400vD,v^2E),
    v0=160000-A/C,
    a0=(-A/2,-200B,-v0*C/2,200*(B-v0*D),
                                      (A+v0*C-v0^2*E)/2).

For the actual-Xi application A,...,E are L025's S2,...,S6 with
positivity from L027, and the unchanged fixed1307 boxes imported in
C031a/C031b. Actual inclusion retains the L019,L021,L036,L037,L917
and1307 contracts, including the conditional Decimal arithmetic
qualifications. This step does not verify those contracts anew.
No RH, Hankel positivity, pole exclusion or whole-disk univalence
assumption is made.

## Conclusion

There are epsilon>0 and C1 real functions a:(-epsilon,epsilon)->R^5
and v:(-epsilon,epsilon)->R, with a(0)=a0, v(0)=v0, such that

    b(tau)=b*+tau*a(tau),
    F(b(tau),tau,400,v(tau))=0,
    v(tau)>0                                         (1)

throughout that interval after shrinking it if necessary. Thus for
every sufficiently small positive tau, C031a's six full equations
hold with t=tau>0, u=400>0, v=v(tau)>0. The b curve is C1,
b(0)=b*, and b'(0)=a0. For example its first-row defects are exactly
tau*A,400*tau*B,tau*v(tau)*C, all strictly positive when tau>0.

The divided residual

    G(tau,a,v)=F(b*+tau*a,tau,400,v)/tau, tau!=0      (2)

has a polynomial extension to all real (tau,a,v). Its dependent
derivative in (a1,...,a5,v) at (0,a0,v0) has determinant -32C.
The IFT graph is unique locally in these transformed variables.
This uniqueness does not classify all solutions of the original
system near tau=0: their scaled coefficient (b-b*)/tau need not
remain near a0.

For the fixed1307 actual constants the hypotheses hold because
C031b gives 56064<A/C<56065 and 103935<v0<103936. The existence
conclusion concerns those actual constants, conditional on their
inherited inclusion; it is not a solution for rational midpoints.
No effective epsilon, disk holomorphy, univalence, positive-semidefinite
defect, actual mixed-form sign, larger block or RH conclusion follows.
Other regular, singular, fractional-power or unbounded-weight branches
are not excluded. The earlier linear-prescription stops remain intact.

## Proof

**Polynomial extension on a real open neighborhood.** C031a supplies
the complete finite polynomials h, and C031b proves h(b*)=0 and its
five-column derivative J_b at b*. Consequently each component of
F(b*+tau*a,tau,400,v) is a polynomial in (tau,a,v) whose coefficient
of tau^0 is identically zero for every a and v. This verifies
vanishing on the entire zero slice, rather than at just (a0,v0).
Each monomial therefore has a factor tau. Removing that factor
defines a polynomial G on R x R^5 x R, agreeing with (2) for
tau!=0. This explicit single polynomial division is the coordinate
case of the known Hadamard lemma; it requires no infinite series,
convergence argument or interchange of limits.

The precise general reference is M. Kunzinger, *Lie Transformation
Groups: An Introduction to Symmetry Group Analysis of Differential
Equations*, Summer Term2015 notes, December2024 correction preface,
[Theorem3.2.15, printed p44](https://www.mat.univie.ac.at/~mike/teaching/ss15/ltg.pdf).
It gives smooth division for functions vanishing on a regular zero
set. The coordinate defining function P=tau has rank one on the
whole zero slice. No general division theorem is reproved here;
the exact factor check is the required specialization for these
finite polynomial residuals. The extension is C1 on a real open
neighborhood containing both signs of tau.

The coefficient of tau^1 in the numerator is J_b*a minus the target
vector. Using C031b's derivative gives the full quotient zero slice

    G(0,a,v)=(-2a1-A,
              -2a2-400B,
              -2a3-vC,
              -2(a1+a3)-160000C,
              -2(a2+a4)-400vD,
              -2(a1+a3+a5)-v^2E).                  (3)

This coefficient identity holds with a,v unrestricted. It is not a
definition that sets the quotient to zero by fiat.

**Base zero and invertibility.** Substitute v0 and a0 into (3).
The first three entries vanish by their definitions. The fourth is
A+v0*C-160000C=0, since C*v0=160000C-A. The fifth vanishes because

    a02+a04=-200B+200(B-v0D)=-200v0D.

For the last entry, a01+a03+a05=-v0^2E/2, so it vanishes too.
All six equations hold exactly. Division by C is legitimate since
C>0, and v0>0 follows from A/C<160000. No smallness of the finite
weights is required.

Differentiating (3) in the indicated dependent-variable order gives
at v=v0 (and in fact at every a on the zero slice)

    M(v0)=[ -2  0  0  0  0       0
             0 -2  0  0  0       0
             0  0 -2  0  0      -C
            -2  0 -2  0  0       0
             0 -2  0 -2  0  -400D
            -2  0 -2  0 -2  -2v0E ].              (4)

Subtract row11 and row13 from row22. That row becomes
(0,0,0,0,0,C). Expanding along it gives sign (-1)^(4+6)=+1
times C and the minor in rows11,12,13,23,33 and the first five
columns. This minor is lower triangular with all diagonal entries
-2, so det M=C*(-2)^5=-32C!=0. The v column is essential: this
is the divided derivative, not C031b's unscaled rank-five matrix.
Neither the value of a0 nor the possibly large value v0 alters
this determinant.

**Imported ordinary implicit-function theorem.** Use O. R. B. de
Oliveira, *The Implicit and the Inverse Function Theorems: Easy
Proofs*, Real Anal. Exchange39(1)(2013/2014),207–218,
[arXiv1212.2066v1, Section3 Theorem2](https://arxiv.org/html/1212.2066v1).
For a C1 map on an open subset of R^n x R^m, a base zero and an
invertible partial derivative in the m dependent variables give a
unique local C1 graph. Apply it with independent variable tau,
dependent variable (a,v) in R^6, map G, base (0,a0,v0), and
derivative (4). Polynomial regularity supplies the open-domain C1
hypothesis; (3) supplies the base zero; -32C!=0 supplies the
invertible partial derivative. These verifications justify importing
the theorem without reproving it or invoking any simple-bifurcation
classification.

It gives a C1 graph (a(tau),v(tau)) on an open interval about zero
with G=0. The polynomial identity F(b*+tau*a,tau,400,v)=tau*G
then proves (1), including tau=0. Since v is continuous and v0>0,
shrink the interval so |v(tau)-v0|<v0/2. For positive tau in that
interval, t,u,v are strictly positive. The product formula makes
b C1 and b'(0)=a0. Uniqueness is exactly the graph uniqueness in
the theorem's dependent-variable neighborhood, with no exhaustion
claim for other original-system branches.

**Actual specialization and exact evidence.** The unchanged C031b
ratio bounds give the strictly positive v0 quoted above. The other
positive finite boxes ensure that all entries of a0 are defined and
finite. These hypotheses suffice for the qualitative theorem at the
fixed actual constants. No new quadrature, interval refinement,
parameter sweep, higher-order branch expansion or effective onset is
used. No uniform interval radius over all enclosing boxes is claimed.

Reproduce the finite check from this notebook with

    python3 scripts/grunsky/divided-residual-1318.py

The complete
[certificate1318](../scripts/grunsky/divided-residual-certificate-1318.json)
stores all six substituted numerators and full quotient polynomials,
all zero-slice and reconstruction residuals, the quotient zero slice,
base numerators with positive common denominator 2C^2 and all six
cleared base residuals, the full dependent derivative and determinant,
input boxes, exact bounds, hashes, checks and failures. It compares
the saved full1314 equations with a direct reconstruction of every
complete column, then checks the quotient and base algebra exactly.
All13 checks pass with no failures. Complete zero-slice formulas,
derivative, determinant, base evidence, identity residuals, bounds and
checks were inspected. The proof above separately establishes the
polynomial extension, base zero, determinant and theorem hypotheses;
a preview of a large quotient is not used as proof.

The exact determinant lies in

    [-66303168031/3125000000000000000,
      -3315158401/156250000000000000] < 0,

as also follows immediately from C>0. This is local progress by
specialization of classical division and IFT, not a new general
existence theorem or progress beyond the checked sources' tools.
It settles finite nonlinear matching in the specified regular class.
Any Grunsky sign transfer still needs a separately proved whole-disk
holomorphic univalent realization. No such analytic property follows
from the current local graph. The larger-block, identification,
initialization and singular-case gaps remain unresolved.

## Mathlib

The reused source assessment1315 records supporting official tools
`HasStrictFDerivAt.implicitFunction` and `ContDiffAt.implicitFunction`
in [Mathlib.Analysis.Calculus.Implicit](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Implicit.html)
and [ImplicitContDiff](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/ImplicitContDiff.html).
Full matching Grunsky/actual-Xi/local-branch or Hadamard-specialization
coverage is unchecked; supporting IFT tools alone do not verify this
instance's hypotheses. No absence claim or Lean verification is made.
The exact Python certificate and inherited Decimal contracts are not
formal Mathlib proofs.
