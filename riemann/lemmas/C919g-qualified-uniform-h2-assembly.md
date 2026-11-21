# Corollary 919g: qualified uniform H2 assembly

## Hypotheses

Use the actual family, normalized logarithmic germ and complete
opposite-class convention of C919c, inherited from L019/L058 and
L919 (the H2 convention is L874's):

    F(lambda,z)=integral_0^infinity exp(lambda*u^2) K(u) cos(zu) du,
    log(F(lambda,z)/F(lambda,0))
        =-sum_(k>=1) S_k(lambda) z^(2k)/k,
    H2(lambda)=(S_(i+j+2)(lambda))_(0<=i,j<=2),
    D=diag(1,200,40000),
    Omega={z: |Re z|<100, |Im z|<1/2},
    0<=lambda<=1/20.

Retain C919c's boundary, complete-sum and signed-exterior conclusions,
C919d's reality of every interior zero on the closed time band,
C919e's full closed-box Gram bound, and C919f's six uniform signs
and their three-box existence conclusion. These inputs have the
independent audits recorded in their canonical proofs. No new audit
of their numerical artifacts or analytic component proofs is claimed.

In particular retain C919b/c/d's Python 3.15.2 Decimal contracts:
directed basic operations, representable neighbors and correctly
rounded HALF_EVEN exp and ln, with the checked square-root enclosures
and exceptional-signal guards specified in C919b. Retain C919f's
correct CPython integer/Fraction arithmetic and libmpdec directed
operations, neighbors and correctly rounded HALF_EVEN exp. Its
recorded runtime is CPython3.15.2/libmpdec4.0.1. The boundary uses
100-digit contexts and the six-sign evaluator uses 80-digit contexts;
neither implementation is formally verified by this argument.
These correctness contracts remain explicit qualifications.

The inherited source normalization is F(lambda,z)=8H_(4lambda)(2z).
Zeros and their multiplicities are those of this fixed local F.
Every opposite class {zeta,-zeta} occurs with its common multiplicity;
there is no zero at the origin. No RH, initial simplicity, exact
zero census, labeled zero branches or reality of exterior zeros is
assumed. No contact or positivity hypothesis from L874 is imported.

## Conclusion

Let B be the positive rational constant from C919e, explicitly

    B=9038116652331572962135737621217329139050385873
      /13463243595254160685006848000000000000,
    epsilon_*=133662268399/267363281250000000000,
    mu=1/B-epsilon_*.

Throughout the entire closed time band, under the stated contracts,

    D H2(lambda) D >= mu I_3,
    mu > 1/700000000-1/2000000000
       = 13/14000000000 > 0.                              (1)

Here >= is real symmetric quadratic-form order. Equivalently,

    H2(lambda) >= mu D^(-2)
               > (13/14000000000) D^(-2) > 0.             (2)

In particular H2 is uniformly positive definite, including lambda=0
and lambda=1/20. This is a qualified finite-degree certificate and
a citation-based application classified KNOWN_IMPORTED, not a new
general theorem or progress beyond the checked methods. Higher-degree
and global signs, and the actual-Xi all-degree mixed positivity gap,
remain open. This is not a complete RH candidate. The separate step2173
assembly audit below accepts this conclusion under the same qualifications.

## Proof

### Imported finite real matrix facts

Import Stephen Boyd and Lieven Vandenberghe, *Convex Optimization*,
Cambridge University Press (2004), corrected seventh printing (2009),
Section 2.2.5, pp.34-35 (positive semidefinite cone and closure under
nonnegative sums), Section 8.3.1, p.406 (finite real Gram matrices),
and Appendix A.5.2, pp.646-647 (real symmetric spectral theorem,
minimum Rayleigh quotient and matrix order):
https://stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf.
For addition and invertible real congruence also use Stanford EE263,
Autumn 2007, Homework 8 solutions, Problems 14.3-14.4(a), printed p.4:
https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/hw/hw8sol.pdf.
The source statements and relevant quadratic-form proofs were
inspected in the unchanged assembly source assessment. Only finite
real matrices and invertible real congruence are used here. There is
no need to reprove these facts or C919e's inverse-Vandermonde bound.

### The complete head, with every multiplicity retained

Fix any lambda in [0,1/20]. C919c gives a finite multiset of interior
opposite classes, no zero on the boundary or at the origin, and the
complete identity

    D H2 D = A_Omega + E_Omega,
    A_Omega=sum_(interior opposite-class occurrences) w(zeta)w(zeta)^T,
    w(zeta)=(zeta^(-2),200*zeta^(-4),40000*zeta^(-6))^T.   (3)

Its absolutely convergent exterior sum E_Omega includes every
remaining occurrence. We use this rectangular partition exactly;
no radial-head substitution or shell subtraction is made.

C919d says every zero in Omega is real, even at lambda=0 when
multiplicities may exceed one. Each class thus has a nonzero positive
representative x, and w(x) is a real vector. Changing from -x to x
does not change w because every exponent is even. Each occurrence
contributes one such real Gram term in (3), with no extra factor of
two from opposition or conjugation.

For this same fixed lambda, C919f gives real zeros x_1,x_2,x_3 with

    x_1 in (14,29/2),
    x_2 in (41/2,43/2),
    x_3 in (49/2,51/2).

All three intervals are positive, disjoint and inside Omega. The
selected zeros therefore belong to three distinct opposite classes,
each with multiplicity at least one. Select exactly one occurrence
from each of these three classes. Let R_Omega be the sum of w w^T
over every other occurrence of the complete interior multiset.
This includes every unselected class and, if a selected class has
multiplicity m>1, its remaining m-1 copies. Thus precisely

    A_Omega=G+R_Omega,
    G=sum_(j=1)^3 w(x_j)w(x_j)^T,
    R_Omega >= 0.                                       (4)

The final inequality follows from the imported finite real Gram
theorem: the remainder is a finite sum of real outer products, with
nonnegative integer occurrence counts. If empty it is the zero
matrix. No sign of an algebraic complex square has been asserted.

Each chosen x_j belongs to the corresponding closed box of C919e.
Its weights and transpose are exactly those in (3). That theorem
and the imported minimum-Rayleigh-quotient characterization give

    G >= (1/B) I_3,
    A_Omega >= (1/B) I_3,       1/B > 1/700000000.         (5)

The bound holds for every allowed choice of the three zeros. We
need no selection continuous in lambda, motion law, constant census
or use of C919d's additional positive-time simplicity conclusion.

### Signed exterior, strict reserve, and congruence

C919c gives for exactly the exterior in (3)

    E_Omega >= -epsilon_* I_3,
    epsilon_* < 1/2000000000.                            (6)

This is the signed rectangular lower bound, not L919's larger
absolute tail-norm budget. E_Omega is real symmetric by the complete
conjugate pairing and absolute convergence already proved in C919c;
its individual complex terms need not be positive semidefinite.
No exterior term is removed in this application.

Addition of (5) and (6) in (3) proves D H2 D >= mu I_3. Both strict
comparisons are inherited exact rational bounds. Their difference is

    1/700000000-1/2000000000
      =(20-7)/14000000000=13/14000000000,

so mu strictly exceeds the fixed positive reserve in (1). This is
not a rounded eigenvalue comparison or an observed sample margin.
The diagonal D is real and invertible. Applying the imported
congruence fact with D^(-1) gives H2 >= mu D^(-2), and D^(-2) is
positive definite, proving (2).

The chosen lambda was arbitrary. All four inputs cover both closed
time endpoints with the same constants. At zero time, repeated
zeros merely repeat nonnegative head terms; at the final time the
same decomposition and inequalities apply directly. No endpoint
limit, infimum over an unproved zero labeling, or new interchange
of an infinite sum and a time derivative occurs.

The new contribution is this complete actual-family application of
the already established inputs. C919f supplies the previously missing
placement, while C919d pays the sign of the whole unselected head.
The old coefficient-width, inner-evaluator and unlocated-box stops
remain valid in their original scopes. No estimator was rerun or
retuned, no numerical certificate was upgraded, and no all-degree
or global conclusion follows from the finite 3 by 3 result.

### Independent assembly audit, 21 November 2026 (step2173)

**Verdict and scope.** Accepted without a mathematical correction,
changed constant or changed dependency. This first assembly audit is
KNOWN_IMPORTED under the unchanged IMPORT assessment2171. It checks
the application of the cited finite real matrix facts, not a reproof
of the accepted analytic components, a replay of their numerical
certificates or a verification of their backends. All hypotheses
and qualifications above remain in force.

**Complete occurrences and units.** Read this entire proof and the
canonical component hypotheses and conclusions. C919c's partition
uses opposite classes repeated with their common multiplicity, and
all powers in w are even. C919d covers every interior class, including
the unselected ones and repeated initial zeros. Thus each head
occurrence is a real Gram term. C919f's positive disjoint open
intervals lie strictly inside Omega and within C919e's corresponding
closed boxes. They supply three distinct opposite classes at each
fixed time. Removing one occurrence per selected class leaves all
other occurrences, including m-1 copies of any selected class of
multiplicity m. This proves the remainder's nonnegative quadratic
form with neither a census nor a simplicity premise.

The (i,j) entry of w w^T is d_i d_j zeta^(-2(i+j+2)); the range
is precisely k=2,...,6. This agrees with the logarithmic indexing,
the algebraic transpose and all weights in C919c/e. C919c's identity
is D H2 D=A_Omega+E_Omega, with no extra opposing or conjugating
factor. Its inherited paired-product normalization cancels the
factor 8 at the origin; L919's substitution u=2w gives source time
4lambda and source position 2z. No source-coordinate S_k is silently
substituted for the local coefficient. Only L874's germ convention
is used, without its contact/nullvector hypotheses.

**Entire signed exterior.** C919c's complement is the full
conjugation-invariant rectangular complement, not a shortened radial
tail. Its real symmetric sum has lower bound -epsilon_* I; individual
complex summands need not be positive. Its proof restricts the
nonnegative opposing-component budget, not a signed shell or an
absolute tail-norm estimate. Hence (6) applies to exactly the
remainder in (3). There is no omitted zero occurrence or unpaid
real-vector claim in the exterior.

**Exact reserve and uniformity.** An independent Fraction check uses
the B and epsilon_* printed in both the assembly and their canonical
inputs. It finds the strictly positive exact differences

    1/B-1/700000000
      =386153864346339517369055978782670860949614127
       /6326681656632101073495016334852130397335270111100000000,
    1/2000000000-epsilon_*
      =9686113/133681640625000000000.

Their sum equals mu-13/14000000000. Both denominators are positive;
the comparison is strict. Thus addition of the two imported matrix
bounds yields (1). Congruence by the real invertible D inverse yields
(2), with D^(-2)=diag(1,1/40000,1/1600000000)>0. All four inputs
use the same closed time band and constants. The selected occurrences
are chosen anew at each fixed time, so neither time labeling nor an
endpoint limit is needed. Initial multiplicities add nonnegative
copies, and the final endpoint is covered directly.

The reproducible exact check is

    python3 scripts/h2-head/assembly_audit_2173.py

Full evidence is `scripts/h2-head/assembly_audit_2173.json`: all twelve
scalar, box and unit checks pass, with no failures. The complete
scalar and check records were inspected, including the exact reserve
surplus; acceptance also uses the occurrence and matrix arguments
above, not a printed PASS label. No component evaluator was rerun or
retuned. Correct CPython integer/Fraction arithmetic is retained;
this check does not attest the inherited Decimal/libmpdec contracts.

The former coefficient-width, inner-evaluator and unpaid-placement
stops206/2157/2161 remain in their original scopes. This audit confirms
a qualified finite H2 input and no new general theorem. It gives no
higher-degree, all-degree, exterior-reality or global result. Full
matching Mathlib coverage remains unchecked.

## Mathlib

Full matching Mathlib coverage of this actual-family, closed-band,
qualified H2 statement has not been checked. The cited sources supply
the finite real matrix facts, and the canonical inputs retain their
own coverage statements. No formal Lean verification of the assembly,
the numerical certificates or their arithmetic backends is asserted;
unknown coverage is not evidence of absence.
