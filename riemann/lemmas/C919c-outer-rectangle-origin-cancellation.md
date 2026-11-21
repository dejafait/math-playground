# Corollary 919c: outer-rectangle origin cancellation and signed complement (audited)

## Hypotheses

Use L058's actual entire family F(lambda,z), L874's normalized germ,
and L919's complete opposite-pair sums, on 0<=lambda<=1/20:

    log(F(lambda,z)/F(lambda,0))
        = -sum_(j>=1) S_j(lambda) z^(2j)/j,
    H2=(S_(i+j+2))_(0<=i,j<=2),  D=diag(1,200,40000).

Use C919a's strip and opposing-component estimates and C919b's
audited vertical nonvanishing, including the latter's stated
Python 3.15.2 Decimal arithmetic contracts. The conclusion inherits
those contracts; no numerical certificate is strengthened here.
The zero-time open strip is L018's. Define

    Omega={z: |Re z|<100, |Im z|<1/2},
    I_k=(2*pi*i)^(-1) integral_(boundary Omega) z^(-2k) F_z/F dz,
           k=2,...,6,

with counterclockwise orientation. Every zero has its full
multiplicity. In sums over opposite classes {zeta,-zeta}, a class
of multiplicity m occurs m times. Put

    P_k=sum_(zeta in Omega) zeta^(-2k),
    T_k=sum_(zeta outside Omega) zeta^(-2k),
    w(zeta)=(zeta^(-2),200*zeta^(-4),40000*zeta^(-6))^T,
    A_Omega=sum_(zeta in Omega) w(zeta)w(zeta)^T,
    E_Omega=sum_(zeta outside Omega) w(zeta)w(zeta)^T.

These are opposite-class sums; every cutoff is invariant under
opposition and conjugation. The transpose is algebraic. There is
no assumption of RH, simple or real zeros, a fixed labeled census,
a computed S_k, or a positive head margin.

## Conclusion

The entire boundary is zero-free throughout the closed time band.
The five integrals are well-defined, and exactly

    I_k=-2S_k+2P_k=-2T_k,                 k=2,...,6.       (1)

Thus, writing J=(I_(i+j+2))_(0<=i,j<=2),

    E_Omega=-(1/2) D J D,
    A_Omega=D H2 D+(1/2) D J D.                           (2)

Both matrices are real symmetric. Uniformly on the band,

    E_Omega >= -epsilon_* I_3 > -epsilon I_3,
    epsilon_*=133662268399/267363281250000000000,
    epsilon=1/2000000000.                                (3)

In (3), > denotes strict quadratic-form order. A separately proved
uniform head margin inf_lambda lambda_min(A_Omega)>epsilon would
therefore imply strict H2 positivity on this band. No such head
margin, numerical I_k value, or numerical full-contour denominator
bound is established.

The outer-only head proposal stops at (1): these five observables
are exactly exterior powers. Recovering the head by the residue
identity still needs S_2,...,S_6 (or independent equivalent head
information); dropping the origin terms is invalid. This is an
exact representation obstruction, not an impossibility theorem
about every use of the actual F or every contour method. It does
not address an additional inner contour or a separate computation
of the origin coefficients. The result is a reproduction and
specialization of known residue/product and conjugate-block methods,
not progress beyond those methods or a solution of RH.

## Proof

### Boundary, endpoints, and the finite-contour theorem

At lambda=0, L058 gives F(0,z)=Xi(z), and L018 places every zero
strictly inside |Im z|<1/2. At 0<lambda<=1/20, C919a's application
of de Bruijn's theorem gives

    |Im zeta| <= (1/2)sqrt(1-8lambda) < 1/2.

In particular, at lambda=1/20 the upper bound is sqrt(3/20)<1/2.
The strict inequality for positive lambda is not extrapolated to
zero time: L018 pays that endpoint separately. Both horizontal
segments, including their corners, contain no zeros.

C919b gives F(lambda,100+iy)!=0 for the whole closed band and
|y|<=1/2, subject to its arithmetic contracts. L058's evenness
gives F(lambda,-100+iy)=F(lambda,100-iy)!=0, paying the other side.
Thus all four sides are covered, without assuming any interior
zero reality or simplicity. No explicit lower bound for |F| or
|F_z/F| on all of these sides is obtained from this argument.

The strip source, already imported and specialized in C919a, is
D. H. J. Polymath, *Effective approximation of heat flow evolution
of the Riemann xi function, and a new upper bound for the
de Bruijn-Newman constant*, Research in the Mathematical Sciences
6 (2019), article 31, arXiv:1904.12438v2 (4 August 2019),
Theorem 3.2, https://arxiv.org/html/1904.12438v2#S3.
Its strict later-time hypothesis is used exactly as above; the
normalization F(lambda,z)=8H_(4lambda)(2z) is L919's. No new strip
proof, zero-free region or numerical-boundary audit is attempted.

For the contour calculation import the finite residue theorem,
NIST DLMF section 1.10(iv), equation (1.10.8), and the Laurent
coefficient convention in section 1.10(iii), (1.10.6)-(1.10.7):
https://dlmf.nist.gov/1.10.E8 and https://dlmf.nist.gov/1.10.iii.
The contour is a positively oriented piecewise smooth Jordan curve.
For each fixed lambda, F is entire and F(lambda,0)>0 by L058, so
it is not identically zero. Its zeros are isolated and there are
only finitely many in the compact closure of Omega. There are none
on the boundary. Thus z^(-2k)F_z/F is meromorphic near this closure,
with finitely many interior singularities and none on the contour.
These are precisely the finite-residue hypotheses; no infinite
contour limit or global logarithm is used.

### Origin residue, full multiplicities, and opposite pairs

Near zero the normalized logarithm exists. Its spatial derivative
is F_z/F because the normalizing value is independent of z. L874's
germ convention, or differentiation of its convergent power series,
therefore gives

    F_z/F=-2 sum_(j>=1) S_j z^(2j-1).

Multiplication by z^(-2k) makes the coefficient of z^(-1) equal
to -2S_k: it is precisely the term j=k. This is an interior
residue even though zero is not a zero of F. Terms with j<k
may contribute higher-order poles; they do not change the residue.

At a nonzero zero a of multiplicity m, locally
F(z)=(z-a)^m h(z), h(a)!=0. Thus
F_z/F=m/(z-a)+h'/h, and the weighted residue is m*a^(-2k).
The finite residue theorem gives

    I_k=-2S_k+sum_(all zeros a in Omega) mult(a)*a^(-2k).

Evenness preserves multiplicities at a and -a, and neither equals
zero. Omega contains both or neither. The even inverse power has
the same value at both. Passing to the specified opposite-class
multiset therefore changes the last sum to 2P_k, with no further
division by two for conjugate classes. This proves the first
identity in (1), for each of exactly k=2,...,6.

L919 proves S_k is the absolutely convergent full opposite-class
sum, using its normalized paired product. Its head/complement
partition here gives S_k=P_k+T_k. Substitution proves I_k=-2T_k.
The infinite sum is justified by that existing absolute convergence,
not by expanding F_z/F on the whole rectangle or enlarging the
contour to infinity. The statements hold at every parameter in
the closed band and need no continuous enumeration of the zeros.

### Matrix assembly and the exact cutoff difference

For d_0=1,d_1=200,d_2=40000, the (i,j) entry of w w^T is
d_i*d_j*zeta^(-2(i+j+2)). Consequently (1) gives (2) entry by
entry. In particular the exterior matrix, with all factors visible,
is

    -(1/2) [ I_2       200 I_3        40000 I_4
             200 I_3   40000 I_4      8000000 I_5
             40000 I_4 8000000 I_5    1600000000 I_6 ].

All zeros are in the open horizontal strip and none has |Re z|=100.
For this zero multiset, the rectangular complement is exactly
|Re zeta|>100, a subset of |zeta|>100. Every zero with |zeta|<=100
is in Omega: if |Re zeta|=100 and |zeta|<=100, it would have to
be one of the excluded points +/-100. This includes all radial
equality cases without an arbitrary boundary assignment.

The actual difference between the two heads consists of the classes

    Q={zeta: |zeta|>100, |Re zeta|<100}.

They also satisfy |Im zeta|<1/2 and hence
100<|zeta|<sqrt(10000+1/4). The set is finite and invariant under
conjugation and opposition. If W_Q is the sum of w w^T over Q,
then, with A,E as in L919, exactly

    A_Omega=A+W_Q,       E=E_Omega+W_Q.

There is no assertion that W_Q has a sign. In particular the lower
bound for E alone could not be subtracted through W_Q to prove (3).

### Restricting the opposing-component budget

Use the stronger, already proved component decomposition of C919a.
For each opposite class write w=a+ib with real vectors a,b. For
any conjugation-invariant subset of the strict radial tail, equal
conjugate multiplicities cancel the imaginary cross terms, giving

    sum w w^T = sum a a^T - sum b b^T.

This retains one copy per multiplicity of each opposite class.
A pair of distinct conjugate classes contributes 2m aa^T-2m bb^T;
a real class contributes m aa^T. Purely imaginary classes cannot
occur in this tail by the strip bound. Norm convergence follows
from L919's sums at powers 4,8,12, since

    ||a||^2+||b||^2=||w||^2
        =|zeta|^(-4)+40000|zeta|^(-8)+1600000000|zeta|^(-12).

Thus this regrouping and restriction are justified for the infinite
rectangular complement as well. C919a proves, before discarding
the positive component, the complete bound

    sum_(|zeta|>100) ||b||^2 <= epsilon_*.

Restricting this nonnegative scalar sum to |Re zeta|>100 can only
decrease it. For every real vector c, therefore,

    c^T E_Omega c
      =sum_(outside Omega) (c^T a)^2-sum_(outside Omega) (c^T b)^2
      >=-||c||^2 sum_(outside Omega) ||b||^2
      >=-epsilon_* ||c||^2.

C919a's exact rational comparison epsilon_*<epsilon proves (3).
This imports its existing full tail bound, not a fresh arithmetic
claim or an absolute-norm estimate. Conjugation invariance and the
same convergence give real symmetric A_Omega,E_Omega. Adding
the separately required head margin to (3), then using invertible
congruence by D, proves only the stated conditional implication.

### Discriminating test and limits

The five tested integrals contain exactly the five exterior powers
in (1). The identity for a head coefficient is P_k=S_k+I_k/2,
and its matrix version is the second line of (2). Treating I_k/2
alone as a head coefficient deletes the required origin Laurent
contribution, rather than evaluating it. No independent relation
recovering the missing S_k from these five exterior powers is
proved or assumed. An accurate enclosure of these integrals alone
would therefore certify exterior data, not the proposed head margin.

This stops only that outer-only mechanism. A separately paid origin
observable or changed contour would require its own applicability
and accuracy argument. The prior moment-box and shared-parameter
stops L917/L920/L922 are unaffected. There is no numerical head
margin to compare with epsilon, and all higher-degree and global
positivity obligations remain open. No mathematical script or
numerical integration is needed for this finite analytic audit.

### Independent conceptual audit, 21 November 2026 (step2158)

**Verdict and scope.** Accepted with exactly the original hypotheses,
including C919b's Python 3.15.2 Decimal contracts. This is the first
independent critical review of this corollary, not a second derivation
claimed as a new result. No identity, numerical bound or dependency
needed correction. The argument establishes (1)-(3) and the conditional
head implication; it supplies neither a head sign nor an RH candidate.
The unchanged ready step2155 assessment covers this specialization.

**Finite residues and the germ.** Rechecked NIST DLMF 1.10(iii)-(iv),
(1.10.6)-(1.10.8), on 21 November 2026, at the URLs cited above.
The finite theorem permits the extra interior singularity at zero;
it does not require a global logarithm. At each fixed time, positivity
of F(lambda,0) excludes an identically zero function. Isolated zeros
and compactness give a finite interior set, and the paid boundary
allows the weighted meromorphic integrand on a neighborhood of the
closed rectangle. On a sufficiently small zero-free origin disk,
termwise differentiation of the convergent normalized germ gives
the coefficient -2S_k of z^(2k-1). Multiplying by z^(-2k) selects
exactly that coefficient as the residue, for every k=2,...,6.
No contact or semidefiniteness hypothesis from L874 is used.

The local factorization at a zero of order m gives residue
m*a^(-2k), without a simplicity assumption. Opposition is fixed-point
free because zero is not a zero of F, preserves multiplicities, and
preserves the even weight. Thus its quotient contributes 2P_k.
Conjugation does not create a further factor of two in this quotient.
This checks both the sign and the normalization of the finite formula.

**Product and convergence.** Checked L919's actual normalization and
its product/coefficient proof, including its independent step204
audit. Its growth bound gives order at most one; paired genus-one
factors cancel their exponentials, evenness removes the remaining
linear exponent, and normalization removes the constant. Its p=2
tail and a common small origin disk justify the logarithm series and
coefficient extraction. Hence the S_k used in the germ are precisely
the absolutely convergent opposite-class sums used here. Splitting
that sum at this finite rectangle is legitimate and proves -2T_k.
This check uses neither a large-contour limit nor differentiation
of a time-dependent enumeration. L919's powers 4,8,12 also dominate
every matrix summand and both real quadratic components absolutely.

**Closed-band boundary.** Rechecked Polymath v2 Theorem 3.2's exact
t>t0 and y0>0 hypotheses and its citation of de Bruijn Theorem 13.
This is a theorem import, not a reproof of the strip theorem. With
the verified source coordinates t=4lambda and source zero 2zeta,
the local squared height bound is 1/4-2lambda. It is strictly below
1/4 for positive time, including 1/20. The t=0 case is instead
paid by L018's open strip. C919b explicitly includes the zero-time
endpoint and both vertical-height endpoints under its contracts;
evenness supplies the left side with the sign of y reversed. Corners
are therefore covered as well. No quantitative minimum on a contour
neighborhood, differentiated approximation error or new quadrature
certificate follows from this qualitative boundary check. C919b's
accepted arithmetic proof was used as an input, not rerun or upgraded.

**Sets, multiplicities and the one-sided budget.** Because no zero
lies on any side and all have |Im zeta|<1/2, the complement on the
zero multiset is exactly |Re zeta|>100. It is a subset of |zeta|>100.
A zero with |zeta|=100 must be in the rectangular head: equality of
its real modulus with 100 would force one of the excluded points
+/-100. The displayed Q is the exact finite difference of the heads;
no sign of its matrix is needed or inferred.

Checked the realification before any inequality: equal conjugate
multiplicities cancel the imaginary cross terms. Real classes have
b=0, and purely imaginary classes cannot occur in either tail.
Absolute convergence permits restriction to the conjugation-invariant
rectangular complement. For an arbitrary real c, each retained
(c^T a)^2 is nonnegative, while (c^T b)^2<=||c||^2||b||^2.
The complete radial sum of ||b||^2 is the quantity bounded in
C919a(8), not merely a lower bound on the signed radial matrix.
Restricting this scalar sum proves (3), with the exact inherited
epsilon_* and strict rational reserve in C919a. No signed shell is
subtracted through a matrix inequality. Entrywise multiplication by
D checks all five indices and the factors through 1600000000 I_6
in (2). Invertible congruence preserves the claimed strict positivity
only if the separately required head-margin hypothesis is supplied.

**Meaning of the stop.** Acceptance is limited to the proposed
residue reconstruction: its head entries are S_k+I_k/2, so the five
outer integrals do not eliminate the unpaid S_k. This is not a
proof that the five exterior values fail to encode lambda injectively
on the particular actual-family curve, nor a theorem excluding some
additional relation using other information about F. No such relation
is supplied. The existing outer-only stop therefore remains valid in
its stated scope, without strengthening it to general impossibility.
The fixed inner-evaluator stop and moment-enclosure failures are
independent and unchanged. This review accepts a local known-method
specialization and its limitations, with no progress beyond the
checked methods. No mathematical script or numerical integral was
needed. Full matching Mathlib coverage remains unchecked.

## Mathlib

Full matching coverage of this heat-band residue identity, the
computer-assisted boundary premise and the restricted opposing
budget has not been checked. C919a/L919 record supporting Jensen
coverage `AnalyticOnNhd.circleAverage_log_norm` at
https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/JensenFormula.html#AnalyticOnNhd.circleAverage_log_norm.
That supports the existing counting input, not the full corollary.
No matching formal residue or de Bruijn theorem is asserted here;
unknown coverage is not evidence of absence.
