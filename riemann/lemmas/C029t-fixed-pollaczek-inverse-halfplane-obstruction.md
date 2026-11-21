# C029t — The fixed Pollaczek inverse of full U_6 has two zeros below -2i

## Hypotheses

Use exactly the full real T_6, all odd and even coefficients, from C029n.
Set S=sin(pi/8)/sqrt(2)>0, U_6=T_6/S and

    A_k=[6!/((6-k)!6^k)] (beta_k/S), 0<=k<=6,
    U_6(t)=sum_(k=0)^6 A_k p_k(t),
    p_(-1)=0, p_0=1,
    (k+1)p_(k+1)=t p_k-(k+1/2)p_(k-1).

The beta_k are the exact finite formulas in C029n, using u_0 through
u_8, without auxiliary coefficient substitution. Their primary source
is Alexey Kuznetsov, *Expansion of the Riemann Xi Function in
Meixner-Pollaczek Polynomials*, Canad. Math. Bull. 51(4) (2008),
561–569, [source](https://doi.org/10.4153/CMB-2008-055-0), equations
(2), (4), (13), pp563/566 and weights pp568–569. Only finite formulas,
not any analytic convergence or numerical root assertion, are used.

Fix the real-polynomial operator

    B h(t)=(3/4-it/2)h(t+2i)+(3/4+it/2)h(t-2i).

## Conclusion

There is a unique real h of degree at most six with B h=U_6. It has
actual degree six and **exactly two** zeros in the open half-plane
Im(t)<-2, with algebraic multiplicity; it has no zeros on Im(t)=-2.
All six zeros are simple. Thus the fixed finite inverse does not meet
the proposed sufficient input threshold of at most one such zero.

This rejects only this N=6 baseline. It neither rules out an
eventual-only law nor supplies a uniform family estimate, an actual-Xi
index bound, or a proof/disproof of RH. It is a known-method finite
specialization, not a claimed new general zero-location theorem.
The finite assertion was independently audited in step2036.

## Proof

### Exact inversion, scaling and degree

Import [DLMF18.22.16–18](https://dlmf.nist.gov/18.22#ii): for
P_n=P_n^(lambda)(x;phi),

    A(x)P_n(x+i)-(A(x)+C(x))P_n(x)+C(x)P_n(x-i)
      +2n sin(phi)P_n(x)=0,
    A(x)=exp(i phi)(x+i lambda),
    C(x)=exp(-i phi)(x-i lambda).

Here lambda=3/4>0, phi=pi/2 in (0,pi), x=t/2 and
p_k(t)=P_k^(3/4)(t/2;pi/2). Thus A=-(3/4-it/2),
C=-(3/4+it/2), A+C=-3/2, and

    B p_k=(2k+3/2)p_k.

These are polynomial identities, so real-x source identities extend
to complex t. No common eigenvalue is assigned to a weighted sum.
The distinct numbers e_k=(4k+3)/2 are all strictly positive. Therefore
the exact preimage is

    h(t)=sum_(k=0)^6 [A_k/e_k] p_k(t).                 (1)

The recurrence gives deg(p_k)=k with leading coefficient 1/k!, so
p_0,...,p_6 form a real basis. Formula (1) proves existence and
uniqueness in degree at most six. C029n proves A_6<0; hence
[t^6]h=A_6/(720 e_6)<0. Both U_6 and h really have degree six.
No unproved degree or simplicity premise enters this step.

For an independent normalization check, expansion of the two binomials
gives the following matrix M of B in ascending monomials (rows and
columns numbered 0,...,6):

    [ 3/2   0    -6     0     24      0     -96 ]
    [  0   7/2    0    -26     0     152      0 ]
    [  0    0   11/2    0    -68      0     552 ]
    [  0    0     0   15/2     0    -140      0 ]
    [  0    0     0     0    19/2     0    -250 ]
    [  0    0     0     0      0     23/2     0 ]
    [  0    0     0     0      0       0     27/2].

Explicitly, the contribution for even l in B(t^k) is
(3/2) binom(k,l) 2^l (-1)^(l/2) t^(k-l); for odd l it is
binom(k,l) 2^l (-1)^((l-1)/2) t^(k-l+1). These formulas verify every
entry, including the leading 2k term. Write b_j=[t^j]U_6 and
c_j=[t^j]h. The exact computation verifies each basis eigenidentity,
each of the seven residual coefficients Mc-b=0 and agreement of (1)
with triangular back substitution. Its complete coefficients are
retained as elements of Q(sqrt(2))[pi] in the certificate below.

### Rational evaluation and complete root certificate

Reuse C029n's proved width-10^(-60) rational intervals for pi and
sqrt(2), including the Machin branch/remainder proof and squared
sqrt(2) endpoints. Their precision is unchanged. Retain the exact
Q(sqrt(2))[pi] coefficients through (1), then use rational interval
Horner evaluation. Addition adds endpoints; multiplication uses the
minimum and maximum of four endpoint products. The interval for
a+b sqrt(2) uses the sign of b. These elementary rules enclose every
actual value even when parameters occur repeatedly; no independence
is assumed. All certificate bounds use integer/Fraction arithmetic.

As a readable coefficient check, the following closed intervals for
c_j have endpoints that are exact rationals with denominator 10^12:

| j | lower | upper |
| --- | ---: | ---: |
| 0 | 1.681979532894 | 1.681979532895 |
| 1 | -0.587694840615 | -0.587694840614 |
| 2 | 0.115367538034 | 0.115367538035 |
| 3 | -0.011339645849 | -0.011339645848 |
| 4 | 0.000475796790 | 0.000475796791 |
| 5 | -0.000004329378 | -0.000004329377 |
| 6 | -0.000000091996 | -0.000000091995 |

The root certificate uses the full unrounded coefficient enclosures,
not these wider displayed intervals. Let r=1/100000. The six rational
disk centers are the decimals in the next table, interpreted exactly.
For each center z write

    h(z+w)=sum_(j=0)^6 d_j(z) w^j,
    d_j(z)=sum_(k=j)^6 binom(k,j)c_k z^(k-j).

Enclose the real and imaginary parts of every d_j with the above
rules and exact rational powers of z. If these intervals are I_j,J_j,
put m(I)=0 when 0 belongs to I and otherwise the smaller endpoint
absolute value; put M(I)=the larger endpoint absolute value. Then

    ell=max(m(I_1),m(J_1)) <= |d_1|,
    u_j=M(I_j)+M(J_j) >= |d_j|.

The certificate also rounds ell down and every u_j up to the grid
10^(-12), records all seven rounded u_j for every disk, and verifies
ell*r > u_0+sum_(j=2)^6 u_j*r^j even with those outward roundings.
Using the full bounds yields the following outward grid-10^(-12)
bounds L<=|d_1|r and R>=|d_0|+sum_(j=2)^6|d_j|r^j:

| center z | L | R |
| --- | ---: | ---: |
| -107.14057083 | 0.021838064313 | 0.000002676156 |
| 3.04261451-5.04707187i | 0.000002901608 | 0.000000001746 |
| 3.04261451+5.04707187i | 0.000002901608 | 0.000000001746 |
| 12.90364942-2.79469559i | 0.000001171601 | 0.000000000957 |
| 12.90364942+2.79469559i | 0.000001171601 | 0.000000000957 |
| 28.18741410 | 0.000019767405 | 0.000000002350 |

Every L>R is strict. Import the standard Rouché theorem, including
multiplicity, in the form stated and proved in Berkeley
[Lecture23, 22 April2026](https://math.berkeley.edu/~avizeff/complex_analysis_S26/lecture_23.html):
analytic functions on a neighborhood of a bounded domain's closure
have the same zero count when the perturbation is strictly smaller on
its piecewise smooth boundary. On each circle |w|=r compare
d_1 w with h(z+w). The displayed inequality is precisely its strict
boundary premise. Both functions are polynomials and d_1!=0, so each
disk contains exactly one zero with algebraic multiplicity, and its
boundary contains none.

The disks are pairwise disjoint: centers with different real parts
have real-part separation greater than 9; equal-real-part centers
have imaginary-part separation at least 5.58939118. Both lower bounds
exceed 2r. The certificate additionally retains all 15 exact squared
distance comparisons against (2r)^2. Six disks each containing one
zero exhaust the proved degree six (the fundamental theorem of
algebra). There are no other zeros; the six zeros are simple.

Exactly the disks at 3.04261451-5.04707187i and
12.90364942-2.79469559i lie strictly below Im(t)=-2, since their
center imaginary parts plus r are less than -2. Each of the other
four disks lies strictly above that line: its center imaginary part
minus r is greater than -2. These rational comparisons exclude a
boundary zero as well as any ambiguous disk crossing. Thus the
required count is exactly two, whereas the proposed threshold is one.

### Qualified de Bruijn application

Import N. G. de Bruijn, *The roots of trigonometric integrals*,
Duke Math. J.17(3) (1950),197–226, DOI10.1215/S0012-7094-50-01720-0,
[primary scan](https://repository.tudelft.nl/file/File_524a4d3c-0858-4c55-b425-8c8ce1fb89da),
Lemma2 and complete proof p215: for real polynomials U,V, if W=U+iV
has n zeros in the open lower half-plane, U has at most n nonreal
conjugate pairs, with the source's multiplicity conventions. Its proof
handles real common factors and a vanished leading real part; neither
coprimality nor full real-part degree is an added hypothesis.

Here set W(t)=(3/4+it/2)h(t-2i) and take U,V to be its coefficientwise
real and imaginary parts. Because h is real, on the real axis its
conjugate term is (3/4-it/2)h(t+2i), so 2U=B h=U_6 as a polynomial
identity. In particular U is nonzero of degree six. W has degree seven,
with leading coefficient i c_6/2; the leading real-part cancellation
is therefore real and is among the cited lemma's covered cases.
The prefactor has one simple zero at t=3i/2, in the upper half-plane.
Zeros of h(t-2i) are precisely alpha+2i for zeros alpha of h, with
the same multiplicity. Hence W has exactly two lower-half-plane
zeros. No zero is on its real axis, because h has none on Im(t)=-2
and the prefactor has none there. The source lemma consequently gives
only an at-most-two-pair bound for U_6. It does not furnish the
at-most-one input sought for the eventual C029m route. No entire
function theorem or finite-to-eventual inference is applied.

### Reproduction and limits

    python3 scripts/pollaczek/shift_inverse_halfplane_2034.py

Full exact coefficients, input/script hashes, matrix, all zero residuals,
unchanged input enclosures, complete complex Taylor intervals, rounded
modulus bounds, contour inequalities, all separations, counts and
failures are in `scripts/pollaczek/shift-inverse-halfplane-2034.json`.
All 52 checks pass; failures are empty. Native complex floating
iterations merely propose rational centers; none of their values or
convergence is a proof premise. The initially unavailable optional
mpmath package was not installed. This is a rational certificate of
this finite result; the separate audit below now validates its evidence.

No parameter, degree or precision campaign follows this failure.
Eventual uniform inverse counts, singular/boundary cases across N,
initialization and the qualified convergence/upstream[9] bridge remain
unresolved. The C029n metric and C029s differential stops are contrasts,
not premises of this inversion or root count.

### Independent audit2036

The unchanged SPECIALIZE assessment2034, approved2035, covers this exact
finite audit. A separate standard-library implementation imports none
of the original mathematical code. Reproduce it with

    python3 scripts/pollaczek/shift_inverse_audit_2036.py

The full comparison evidence is in
`scripts/pollaczek/shift-inverse-audit-2036.json`. All 253 checks pass,
with no failures. The original script, certificate and source input
hashes are retained; none was rewritten. Sparse rational polynomials
in pi and sqrt(2) reconstruct u_0,...,u_8, all seven beta coefficients
and all seven weighted coefficients from the stated C029n formulas.
The independently reconstructed Machin and squared sqrt(2) enclosures
agree exactly with the unchanged input intervals; the Machin branch
justification remains the complete proof in C029n, not a numerical check.

Direct Gaussian-rational expansion of both shifted monomials, including
the linear prefactors, reproduces every matrix entry and verifies that
the possible degree-seven term cancels. Its triangular solve agrees
with every one of the seven exact saved h coefficients and the spectral
formula (1). All basis eigenidentities and positive distinct eigenvalues
are checked, as are both nonzero degree-six leading coefficients and all
seven exact identity residuals. Thus uniqueness is justified in the
specified degree-at-most-six space, without an unproved inverse premise.

Every real and imaginary interval of all 42 Taylor coefficients agrees
with the original full certificate. All rounded modulus bounds, contour
totals and displayed grid roundings agree. Separately, expansion of the
exact symbolic h(z+w) before interval evaluation gives a second strict
Rouche inequality for each disk, without using the saved Taylor values.
All 15 squared separation comparisons and all six line placements are
recomputed. The smallest original strict gap is at least
585323/500000000000>0. Accordingly each disk contains one zero with
multiplicity; six disjoint disks exhaust degree six, establish simplicity
and exclude any root on Im(t)=-2. Exactly two disks are below that line.
Floating seeds enter neither reconstruction nor certification.

On paper, conjugacy for real t gives 2Re(W(t))=B h(t)=U_6(t), and this
extends as an identity of real-coefficient polynomials. The prefactor
zero is +3i/2 and the shift carries each h zero alpha to alpha+2i,
with multiplicity. Hence W has exactly two lower-half-plane zeros and
none on the real axis. Its degree-seven leading coefficient is i c_6/2,
while [t^6]Re(W)=27c_6/4!=0. The leading-real-part cancellation is
precisely the exceptional case covered by de Bruijn's full Lemma2
proof on p215; no degree-seven real-part or coprimality assumption is
inserted. The correct conclusion is at most two nonreal pairs for U_6.

No proof correction was required. This is independent reproduction of
the recorded finite stop, not a new theorem beyond the cited methods,
an eventual family result or an RH candidate. C029n remains its only
direct local mathematical input; C029m is motivation, not a premise.

## Mathlib

Full matching inverse/count result and supporting Pollaczek, de Bruijn
and rational complex-enclosure coverage were not checked. No absence
claim is made. Rouché is imported by the precise standard citation
above; no Lean verification is claimed.
