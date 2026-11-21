# C029o — Full tilted T_6 Bezoutian: exact metric, unresolved inertia

## Hypotheses

Use exactly C029n's full Kuznetsov T_6, retaining every odd coefficient,
its normalization S=sin(pi/8)/sqrt(2)>0, and U=T_6/S. Thus

    U(t)=sum_(k=0)^6 A_k p_k(t),
    A_k=[6!/((6-k)!6^k)] beta_k/S,
    p_(-1)=0, p_0=1,
    (k+1)p_(k+1)=t p_k-(k+1/2)p_(k-1).

The u_0,...,u_8 and beta_0,...,beta_6 are the finite formulas of
Alexey Kuznetsov, *Expansion of the Riemann Xi Function in
Meixner-Pollaczek Polynomials*, Canad. Math. Bull. 51(4) (2008),
561–569, recurrence (2), coefficients (4)/(13), pp563/566, and weights
pp568–569, [DOI](https://doi.org/10.4153/CMB-2008-055-0), as stated
and audited in C029n. Import C029n's A_6<0, degree six, the descending
evaluation comrade C, and positive diagonal D. In particular

    Phi=(p_5,p_4,p_3,p_2,p_1,p_0)^t,
    C Phi=t Phi-(6/A_6)U e_1,     A=D^(-1)CD,
    (D_1^2,...,D_6^2)=(693/256,315/128,35/16,15/8,3/2,1).

For the finite interval diagnostic use only C029n's audited 60-decimal
rational enclosures of pi and sqrt(2), including its Machin/isqrt proof.
No root simplicity, nonzero minor or inertia hypothesis is made.

## Conclusion

The uniquely defined full-bulk real symmetric matrix B satisfying

    Phi(x)^t B Phi(y)=(U(x)U'(y)-U(y)U'(x))/(x-y)

obeys C^t B=BC. Its congruently scaled matrix G=DBD obeys A^t G=GA.
There is no restriction fixing any bulk block of B or G.

The specified expanded-determinant interval Horner calculation proves
Delta_1>0 and Delta_2>0, where Delta_j=det B[1:j,1:j]. Its complete
computed intervals for Delta_3,...,Delta_6 all contain zero. Thus this
diagnostic is **inconclusive**: it establishes neither complete inertia,
nonsingularity, simplicity, nor negative index<=1 or >=2. It does not
assert that any actual determinant vanishes. The finite representations
are known-method specializations; no advance beyond the checked source
theory or toward an eventual uniform bound is claimed.

## Proof

### Exact construction and convention

All coefficients are calculated in R=(Q[s]/(s^2-2))[X], evaluated at
(s,X)=(sqrt(2),pi). Denote by b_i=[t^i]U, 0<=i<=6, with
d_i=(i+1)b_(i+1) for 0<=i<6 and d_6=0. The coefficients b_i are
exactly sum_(k=i)^6 A_k[t^i]p_k. Here b_6=A_6/720!=0. A complete
division-free construction of the monomial kernel matrix K is

    sum_(a,b=0)^5 K_ab x^a y^b
      =sum_(0<=j<i<=6) (b_i d_j-d_i b_j)
         * sum_(l=0)^(i-j-1) x^(i-1-l)y^(j+l).              (1)

Multiplying each inner sum by x-y gives x^i y^j-x^j y^i by telescoping,
so (1) times x-y is the required numerator in all 49 coefficients.
The numerator and denominator both change sign on swapping x,y;
hence the quotient is symmetric. Its degree is at most five in each
variable. Since p_k has degree k and leading coefficient 1/k!, the
six basis elements span uniquely every polynomial of degree at most
five. Let V_ik=[t^i]p_k for 0<=i,k<=5. This is invertible triangular.
Define the rational matrix R by t^i=sum_k R_ik p_k, and let R_d reverse
its columns. Thus the monomial column is R_d Phi and

    B=R_d^t K R_d,    K=V_d B V_d^t,

where V_d is V with columns reversed. These equations construct every
entry of B and prove its uniqueness and symmetry. The certificate
retains V, R, all basis polynomials, K, B and all numerator coefficients;
it checks every conversion coefficient, not just selected entries.

This is the application of H. Wu, X. Wu and Z. Yang, *More on polynomial
Bezoutians with respect to a general basis*, ELA21 (2010), 154–171,
definition (1.1), Lemmas2.1–2.2 and Propositions2.5–2.6, pp154–159,
[primary PDF](https://emis.de/ft/34467). Their hypotheses are actual
degree n, numerator degree<=n and an invertible degree-graded basis.
Here n=6 and numerator U' has degree five. Their coefficient comrade
orientation differs from the evaluation orientation used here; we check
the finite specialization explicitly to prevent a transpose error.

Indeed the x^5 coefficient of the kernel is b_6 U'(y). Comparing with
the leading coefficient 1/120 of p_5 gives

    e_1^t B Phi(y)=120 b_6 U'(y)=(A_6/6)U'(y).             (2)

Using the imported evaluation identity for C in both variables,

    Phi(x)^t(C^t B-BC)Phi(y)
      =(x-y)Phi(x)^t B Phi(y)
        -(6/A_6)U(x)e_1^t B Phi(y)
        +(6/A_6)U(y)Phi(x)^t B e_1=0

by the kernel identity, (2) and symmetry. Independence of the basis
products proves C^t B=BC. This is an orientation check for the approved
finite application, not a new general symmetrizer theorem. The script
also verifies all 36 entries exactly after clearing A_6, already proved
nonzero in C029n, and verifies all 42 comrade coefficients. All involved
computations are finite polynomial identities; no roots or limits enter.

Since D is real, diagonal and positive, D is invertible, and substitution
into A=D^(-1)CD gives

    A^t G-GA=D(C^t B-BC)D=0,    G=DBD.

Congruence preserves inertia even for singular B; it does not guarantee
nonsingularity. No floating square roots of the D entries are used.

### Determinants and exact enclosure failure

For each j=1,...,6 the program expands Delta_j as a polynomial in R by
the finite Leibniz definition. Its recursion expands the first row over
the ordered remaining columns, with sign (-1)^k for the k-th remaining
column, using determinant 1 for the empty matrix. Induction on matrix
size proves equality with the Leibniz sum; caching column subsets only
reuses identical sums and changes no arithmetic. Literal permutation
sums independently agree for j=1,2,3. There is no matrix division,
floating approximation, zero-minor rule or external interval contract.
The six resulting exact X-degrees are 18,36,54,72,90,108; every
coefficient is retained in the certificate.

Each coefficient a+b*s is enclosed using the sign of rational b and
the fixed sqrt(2) enclosure. Interval Horner evaluation at the fixed pi
enclosure uses endpoint sums and the minimum/maximum of four endpoint
products. These rules enclose all sums and products by order and
bilinearity; induction through Horner proves enclosure of each exact
determinant. C029n proves that the input intervals contain pi and
sqrt(2). The script also reconstructs every u, beta, A and Jensen weight
and compares all coefficients exactly with that audited input.

The following are outer rational bounds for the *computed intervals*.
Decimals denote exact rationals, and the final column multiplies both
endpoints. The artifact retains the complete unrounded endpoints.

| j | Lower | Upper | Multiplier |
| --- | ---: | ---: | ---: |
| 1 | 1.332652 | 1.332653 | 10^(-7) |
| 2 | 1.024767 | 1.024768 | 10^(-12) |
| 3 | -1.062637 | 1.088468 | 10^(-10) |
| 4 | -1.145816 | 1.155234 | 10^7 |
| 5 | -1.868877 | 1.874129 | 10^24 |
| 6 | -5.632156 | 5.637589 | 10^41 |

In addition to outward containment, exact rational comparisons prove
that the complete raw intervals for j=3,4,5,6 contain, respectively,
[-10^(-11),10^(-11)], [-10^6,10^6], [-10^23,10^23] and
[-10^40,10^40]. Thus their zero containment is not merely an artifact
of rounding this table. It reflects failure of this expanded-polynomial
enclosure method with these fixed inputs; it is not information that
the exact determinant itself is zero or close to zero.

Jacobi's theorem, Michel Coste, *An Introduction to Semialgebraic
Geometry* (October2002), section1.4.2 p19,
[primary notes](https://perso.univ-rennes1.fr/michel.coste/polyens/SAG.pdf),
would give negative index as the number of sign changes in
(1,Delta_1,...,Delta_6) if all six minors were proved nonzero. That
hypothesis is unpaid here, so the theorem is not applied. Likewise
G. Heinig and K. Rost, *Bezoutians*, Chemnitz2008-09,
[primary preprint](https://www.tu-chemnitz.de/mathematik/preprint/2008/PREPRINT_09.pdf),
Example7.2 p40, Proposition7.15/(7.11) p45 and Theorem10.4 with its
repeated-root discussion pp59–60, identify the derivative Bezoutian's
inertia with the Newton-sum Hermite form, including singular cases.
Its negative index counts distinct conjugate pairs, not their algebraic
multiplicities in singular cases. Representation by this known form
supplies no negative-index bound. This test makes no simplicity claim.

Reproduce from the notebook with

    python3 scripts/pollaczek/tilted_bezoutian_n6_2014.py

Full coefficients, basis conversion, kernel/comrade/metric residuals,
six determinant polynomials, exact intervals, zero-containment witnesses,
input checksum, signs and failures are in
`scripts/pollaczek/tilted-bezoutian-n6-2014.json`. All 34 construction,
comparison and reporting checks pass; the four unresolved signs are
explicitly recorded as incomplete certification, not hidden as success.
The only implementation repair enabled serialization of generated
integers longer than Python's default 4300-digit limit; it changed no
calculation or numerical budget. Full selected bounds, checks and
zero-containment witnesses were inspected, rather than relying on a
preview. No independent audit of this new artifact is claimed.

This is one N=6 reproduction under assessment2013. It does not reopen
the boundary-supported ansatz, degree24 runtime or summability stops.
C029l/C029m remain downstream context only: their eventual uniform
index premise and qualified compact convergence, including upstream[9],
are neither used nor established. The main actual-Xi positivity gap
L030–L032/C032a is unchanged, and there is no RH candidate.

## Mathlib

Full matching finite statement, Bezoutian identities, inertia sources
and exact coefficient/enclosure coverage were not checked in Mathlib.
No absence or formal verification is claimed. The known source theory
is imported precisely; only the approved finite application and its
failed sign-separation diagnostic are recorded here.
