# Corollary C028h: centered companion terminal-three cost floor

## Hypotheses

Use the actual real reciprocal Jensen coefficients and centered monic
polynomial of C028d, for each integer d>=3:

    P_d(x)=sum_(j=0)^d binom(d,j)b_j x^(d-j),  b_0=1,
    Q_d(y)=P_d(y-b_1)=sum_(k=0)^d c_(d,k)y^(d-k),
    c_(d,k)=binom(d,k)sum_(j=0)^k binom(k,j)b_j(-b_1)^(k-j).

C028a supplies the fixed, finite actual constants

    S_2=b_1^2-b_2>0,
    2S_3=b_3-3b_1 b_2+2b_1^3>0.

Let A_d be the real Frobenius companion with entries

    (A_d)_(j+1,j)=1  (1<=j<d),
    (A_d)_(j,d)=-c_(d,d-j+1)  (1<=j<=d),

and all other entries zero. These two prescriptions occupy disjoint
positions. Let D=diag(delta_1,...,delta_d), where every delta_j>0,
and set

    B=D A_d D^(-1),  H=(B-B*)/(2i),  K_d(D)=||H||_1.

Here * denotes conjugate transpose and ||.||_1 is the Schatten trace
norm, not the entrywise norm. D may depend arbitrarily on d. No RH,
real/simple-root hypothesis, diagonalizability, irreducibility, positive
symmetrizer or condition-number bound is assumed. Write H_d for the
sum of absolute imaginary parts of the roots of P_d, with algebraic
multiplicity, as in C028d. This K_d(D) is distinct from C028d's scalar
coefficient cutoff K_d without a diagonal argument.

## Conclusion

Define the fixed positive constant

    c = sqrt(min{4S_3/(27 sqrt(S_2)), S_2/4}) > 0.

For every integer d>=3 and every positive diagonal D,

    H_d <= K_d(D),                 K_d(D) >= c*d.           (1)

In particular no sequence of these positive diagonal similarities has
K_d(D_d)=o(d). This stops this companion trace-norm majorant as a
sublinear payment mechanism. A lower bound on this upper majorant
does not lower-bound H_d and does not imply a nonreal root or refute RH.

More precisely, put

    a=binom(d,2)S_2,  b=2binom(d,3)S_3,
    x=delta_(d-1)/delta_(d-2),  y=delta_d/delta_(d-1).

The last three principal coordinates of H have trace norm exactly

    R(x,y)=sqrt{x^2+b^2/(x^2 y^2)+(a/y-y)^2}.             (2)

Its infimum over positive x,y is attained at

    x=sqrt(b/y_*),
    y_*^4-b*y_*-a^2=0,

where y_* is the unique positive solution of this equation. The
resulting exact block minimum is

    sqrt{2b/y_*+(a/y_*-y_*)^2}.                          (3)

No equality between the minimum of this compression and the minimum
of the full K_d(D) is asserted.

## Proof

### Imported matrix inputs and applicability

Nicholas J. Higham, *What Is a Companion Matrix?*, 23 March 2021,
updated 9 April 2021,
[opening determinant identity (*) and alternative placements](https://nhigham.com/2021/03/23/what-is-a-companion-matrix/),
gives the characteristic polynomial identity for the Frobenius
companion, including its transposed/permuted conventions. Our
last-column/subdiagonal convention therefore has characteristic
polynomial Q_d. Similarity preserves that polynomial, and translation
by real b_1 preserves imaginary parts and algebraic multiplicities.

Gerhard Schmeisser, *Estimates for the Imaginary Parts of the Zeros of
a Polynomial*, Mathematica Balkanica 16 (2002), 203-217,
[Section 3, Lemma 1, printed pp.211-212](https://www.math.bas.bg/infres/MathBalk/MB-16/MB-16-203-217.pdf),
states that for an arbitrary square complex matrix the vector of
absolute imaginary eigenvalue parts is weakly majorized by the
singular values of its Hermitian imaginary part. Taking the full
partial sum applies to B and gives H_d<=K_d(D), including repeated
roots; the lemma has no orthogonal-polynomial or normality premise.

John Watrous, *The Theory of Quantum Information*, 2018 author-hosted
pre-publication version,
[Section 1.1, (1.165)-(1.175), (1.179)-(1.181), pp.32-34](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf),
supplies the Schatten norms and ideal inequality

    ||U X V||_p <= ||U||_infinity ||X||_p ||V||_infinity,
    1<=p<=infinity,

for compatible rectangular operators. If E:C^3->C^d includes the last
three coordinates, ||E||_infinity=||E*||_infinity=1. Taking p=1 gives

    ||E* H E||_1 <= ||H||_1=K_d(D).                      (4)

These three results are imported, not reproved. Assessment1523 and its
separate approval1524 cover exactly these hypotheses. The calculation
below is needed to retain the actual centered cubic coefficient,
all binomial factors and arbitrary positive scaling ratios; none of
the cited general matrix results evaluates that specialization.

### Exact terminal block

C028d's formula and C028a's central cubic identity give exactly

    c_(d,1)=0,
    c_(d,2)=-binom(d,2)S_2=-a,
    c_(d,3)=binom(d,3)(b_3-3b_1 b_2+2b_1^3)=b>0.

Consequently the terminal block of A_d is

    [ 0  0  -b ]
    [ 1  0   a ]
    [ 0  1   0 ].

This includes d=3, where it is the entire matrix. Scaling first and
then compressing gives

    M:=E* B E = [ 0  0  -b/(xy) ]
                [ x  0    a/y  ]
                [ 0  y     0   ].

Because compression commutes with taking adjoints,
E* H E=(M-M*)/(2i). No similarity invariance of the norm is used.
For R^2=x^2+b^2/(x^2 y^2)+(a/y-y)^2, direct evaluation of the
three-by-three characteristic determinant yields

    det(lambda I-(M-M*)/(2i))=lambda*(lambda^2-R^2/4).

This Hermitian matrix has eigenvalues 0,R/2,-R/2. Its singular values
are their absolute values, so its trace norm is R, proving (2).
The factors 1/(2i) and the two nonzero singular values cancel exactly.

### Unrestricted finite optimization

For every positive x,y, the elementary inequality u+v>=2sqrt(uv),
applied to u=x^2 and v=b^2/(x^2 y^2), gives

    R(x,y)^2 >= 2b/y+(a/y-y)^2=:f(y).                    (5)

Equality holds exactly when x^2=b/y, an admissible positive ratio.
Every positive x,y is realizable by a positive D (take the terminal
diagonal entries 1,x,xy and any positive earlier entries).

Expanding f(y)=y^2-2a+a^2/y^2+2b/y shows

    f'(y)=2y-2a^2/y^3-2b/y^2,
    f''(y)=2+6a^2/y^4+4b/y^3>0.

The derivative tends to minus infinity at zero and to plus infinity
at infinity. Thus it has a unique positive zero y_*, which is the
global minimizer because f tends to infinity at both ends. Multiplying
f'(y_*)=0 by y_*^3/2 gives y_*^4-b*y_*-a^2=0. Every positive
solution of that equation is a derivative zero, so uniqueness holds
in the stated positive domain. This proves the exact minimum (3).
There is no restriction on how the optimizing ratios vary with d.

### Uniform degree-linear bound, with onset d=3

It is unnecessary to solve the quartic numerically. For every d>=3,

    a <= (S_2/2)*d^2,
    b = (S_3/3)*d^3*(1-1/d)*(1-2/d)
      >= (2S_3/27)*d^3.                                (6)

The last inequality follows from (1-1/d)>=2/3 and
(1-2/d)>=1/3. Put L=sqrt(S_2)>0. Split all positive y into two
exhaustive ranges, without assuming any bound on x or D.

If y<=L*d, equations (5)-(6) give

    R(x,y)^2 >= 2b/y >= [4S_3/(27L)]*d^2.

If y>=L*d, then a<=L^2*d^2/2<=y^2/2. Hence

    y-a/y>=y/2,
    R(x,y)^2 >= (a/y-y)^2 >= y^2/4 >= (S_2/4)*d^2.

Both estimates are valid at the shared endpoint. Taking their smaller
positive constant and using (4) proves K_d(D)>=c*d for all d>=3.
The threshold sought was K_d(D_d)/d->0; (1) instead gives a fixed
positive lower bound even for arbitrary degree-dependent scalings.

This meets the stipulated abandonment test for this majorant family.
All other coordinates can only increase its cost relative to this
compression; they were omitted solely through (4). The estimate does
not claim that actual imaginary root heights are large. In particular
H_d<=K_d(D) and K_d(D)>=c*d cannot be reversed or combined to infer
H_d>=c*d. The actual-Xi height payment and all-degree positivity remain
unproved. C028a/c's different reference-family stops are preserved and
are comparisons, not additional mathematical inputs here.

### Independent finite audit1527 (2026-11-18)

The proof was replayed under assessment1525, separately approved1526.
No correction to its statement, direct inputs or constant is needed.
This verifies the existing specialization; it supplies no stronger
theorem or new discovery beyond the assessed matrix methods.

Expanding the centered coefficients for k=1,2,3 gives respectively
b_1-b_1=0, b_2-2b_1^2+b_1^2=-S_2, and
b_3-3b_1*b_2+3b_1^3-b_1^3=2S_3, before multiplying by
binom(d,k). C028a's already audited local logarithm supplies the two
strict signs without RH. Thus the last column is (-b,a,0), in that
order. For B=D A_d D^(-1), an entry (j,k) is multiplied by
delta_j/delta_k: the subdiagonal entries are x,y, and the other two
entries are -b/(xy),a/y. The ratios are not inverted. At d=3 the same
three coordinates are the whole matrix, with a=3S_2 and b=2S_3.

For a direct determinant check put q=b/(xy) and r=a/y-y. Then

    2i E*HE = [ 0 -x -q; x 0 r; q -r 0 ] =: N.

This real skew-symmetric odd-order matrix has determinant zero, since
det N=det N^T=det(-N)=-det N. Also
tr((E*HE)^2)=(x^2+q^2+r^2)/2=R^2/2 and tr(E*HE)=0.
The characteristic polynomial of the three-by-three Hermitian matrix
is therefore lambda^3-(R^2/4)lambda. Its two nonzero eigenvalues have
absolute values R/2 each, so the trace norm is R, not R/2 or sqrt(2)R.
Watrous's p=1 compression inequality has factor one even when d=3;
there is no entrywise-norm substitution or similarity-invariance claim.

For fixed y>0, equality in the two-term bound occurs at x^2=b/y>0.
The displayed f'' is strictly positive; f' has opposite infinite
limits at the two ends. Thus the positive critical point exists and
is unique, and multiplying f'=0 introduces no extraneous positive
solution. Both optimizing ratios are realizable by D. This concerns
the block minimum only; no attainment statement for the full-matrix
minimum is used.

Finally b/d^3=(S_3/3)(1-1/d)(1-2/d)>=2S_3/27 for every d>=3,
with equality at d=3. The upper bound a<=S_2*d^2/2 and the split
y<=sqrt(S_2)d or y>=sqrt(S_2)d require no bound on D. The first
range gives R^2/d^2>=4S_3/(27sqrt(S_2)); the second gives
R^2/d^2>=S_2/4, because a/y<=y/2. Both hold at the common
endpoint. Their minimum is fixed and strictly positive. This confirms
the all-d abandonment test even for unbounded, degree-dependent
scalings. Schmeisser's upper comparison H_d<=K_d(D) counts all
algebraic multiplicities but cannot turn this cost floor into a lower
height bound. The method-specific stop is now audited; actual S_F=0,
H_d=o(d) and RH remain unresolved.

## Mathlib

Not checked. A full matching theorem for this actual centered
companion specialization, its optimized terminal block and its uniform
degree bound has not been checked in Mathlib; no absence or formal
verification is claimed. The general matrix results above are imported
with precise citations, and their elementary finite specialization is
proved in full here. This is reproduction/specialization of known
matrix methods, not a claim of a new general norm theorem.
