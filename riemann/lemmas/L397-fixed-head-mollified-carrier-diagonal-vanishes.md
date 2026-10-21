# Lemma 397: the fixed-head mollified carrier diagonal tends to zero

## Hypotheses

Use exactly Q_N(H) in L396 (1). Fix a positive integer N independently
of H, let ell=log H, Y=H^(1/100), and retain

    p_H(a)=(log(Y/a)/log Y)^2   (1<=a<=Y),
    q_H(m)=(1-log(m)/ell)^2.

Every ordered collision mn b=rs a in that definition is included.
The limit is H tending to infinity with N fixed. No RH, growing-N,
positivity, zero simplicity, disjointness or probabilistic phase
assumption is imposed.

## Conclusion

For all sufficiently large H (with an N-dependent implied constant),

    |Q_N(H)| <= C_N log log H / log H.

Consequently its limit is zero for every fixed N. By L396 (2),

    H^(-1) integral_[H,2H] Re(K E Z_N^2)|P_H|^2 = o_N(1).

This evaluates only the fixed-head carrier. It does not evaluate the
balanced mean, justify growing N, determine the complete signed physical
mean, or give any global discriminant sign, zero-count bound or RH result.
The separate step 70 critical audit below validates this fixed-N result.

## Proof

The unchanged prior assessment is
`drafts/literature/2026-10-11-mollified-carrier-diagonal-limit.md`
(EXPLORE). We derive the statistic's own Euler factors. The source's
different coefficient evaluations are not imported or reproved.

The only quantitative analytic input beyond absolute Dirichlet-series
convergence is the classical unconditional reciprocal-zeta bound

    |1/zeta(sigma+iv)| <= C log(2+|v|),
          1<=sigma<=2, |v|>=v_0,                     (3)

for some fixed v_0 and C. A precise citation is E. C. Titchmarsh,
*The Theory of the Riemann Zeta-function*, second edition, revised
by D. R. Heath-Brown (1986), Theorem 3.11, equation (3.11.8), pp. 60–61:
[primary book](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=35).
The explicit published statement inspected in the separate coverage review
is S. Baluyot and S. M. Gonek, *Explicit formulae and discrepancy estimates
for a-points of the Riemann zeta-function*, Pacific J. Math. 303 (2019),
47–72, Section 2, p. 53, immediately before (2-3),
[published statement](https://msp.org/pjm/2019/303-1/pjm-v303-n1-p02-p.pdf#page=9),
DOI 10.2140/pjm.2019.303.47. Citing Titchmarsh (3.11.8), it states
|zeta(sigma+iv)|>=c/log v for sufficiently large positive v and
sigma>=1-A/log v, with fixed positive constants. Restriction to
1<=sigma<=2 and complex conjugation give exactly (3). Direct inspection
of the cited book pages is not claimed. This is the reciprocal bound
covered by the saved assessment;
M. P. Young, *A short proof of Levinson's theorem*, Arch. Math. 95
(2010), 539–548, proof of Lemma 7, p. 546, explicitly uses this input:
[inspected primary proof case](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf#page=8).
We require (3) only to the right of Re s=1. It assumes neither RH
nor a stronger zero-free region. Nonvanishing on Re s=1 away from
the pole, also in that standard input, supplies bounded reciprocals
on compact sets away from s=1. At the pole, 1/zeta(1+w) is analytic
and O(|w|) in a fixed disk, by the Laurent expansion with residue one.
These facts imply, for a sufficiently small fixed d>0, constants
C_d and 0<c<c_0, and |alpha|,|beta|<=c/4, that

    |1/zeta(1+c+iu+alpha)|
      <= C_d |c+iu|                       (|u|<=d),
      <= C_d log(2+|u|)                   (|u|>d),       (4)

and the identical bounds with beta. For the first line choose d,c_0
so the arguments remain in the Laurent disk and use
|c+iu+alpha|<=5|c+iu|/4. For the second, (3) controls large |u|;
the intervening compact set is bounded away from the pole and from
zeros, uniformly for these shifts. The real parts lie between
1+3c/4 and 1+5c/4, within [1,2].

### Exact collision series, including exceptional primes

For fixed k>=1 and complex alpha,beta set

    d_(alpha,beta)(j)=sum_(mn=j) m^(-alpha)n^(-beta),
    J_k(alpha,beta)=sum_(a,b<=Y; b|ka)
         mu(a)mu(b) p_H(a)p_H(b) d_(alpha,beta)(ka/b)/a.

J_k is a finite entire function of the two shifts. The collision gives
sqrt(abmn)=sqrt(k)*a. Thus, with

    D_ell=(1+ell^(-1) partial_alpha)^2
                 (1+ell^(-1) partial_beta)^2,

the exact original diagonal is

    Q_N(H)=(1/2) sum_(r,s<=N) (rs)^(-3)
                              [D_ell J_(rs)]_(alpha=beta=0).   (5)

Indeed partial_alpha m^(-alpha)=-(log m)m^(-alpha), so the
operator produces exactly both q_H factors. No divisor is deleted,
and both a,b cutoffs still occur in J_k.

Put lambda=log Y and c=1/lambda. On Re s=Re t=c and
|alpha|,|beta|<=c/4 introduce

    F_k(s,t;alpha,beta)=sum_(a,b>=1; b|ka)
           mu(a)mu(b) a^(-1-s)b^(-t) d_(alpha,beta)(ka/b).       (6)

Here s,t are Mellin variables, unrelated to the response index s in
(5). To compute its local factors, write e=v_p(k) and

    D_e=sum_(j=0)^e p^(-j alpha-(e-j)beta),
    D_(-1)=0,
    X=p^(-1-s-t), U=p^(-1-s-alpha), V=p^(-1-s-beta).

The four possible squarefree exponents of a,b give the following complete
list; the divisor exponent is e+v_p(a)-v_p(b).

| v_p(a) | v_p(b) | allowed | signed contribution |
| --- | --- | --- | --- |
| 0 | 0 | every e>=0 | D_e |
| 0 | 1 | e>=1 | -p^(-t) D_(e-1) |
| 1 | 0 | every e>=0 | -p^(-1-s) D_(e+1) |
| 1 | 1 | every e>=0 | X D_e |

Their signed sum is precisely

    L_e=(1+X)D_e - p^(-t)D_(e-1) - p^(-1-s)D_(e+1).          (7)

In particular L_0=1+X-U-V, a finite factor, not a geometric
sum of squarefree b powers. For primes outside k, the corresponding
absolute local mass is at most

    1+p^(-1-2c)+2p^(-1-3c/4).

Its product converges for each c>0. The finitely many primes dividing
k cause no convergence issue. Thus (6) and its Euler product are
absolutely convergent, uniformly in imaginary s,t and in the shift
bidisk, for each fixed c. This also justifies their identification.

Define the exact arithmetic factor without dividing by L_0:

    A_k= product_p [L_(v_p(k)) (1-X)/((1-U)(1-V))].             (8)

For p not dividing k its local factor equals

    1 - (X-U)(X-V)/((1-U)(1-V)).                              (9)

Since |X|,|U|,|V|<=1/p and |1-U|,|1-V|>=1-1/p,
the deviation in (9) is bounded by 4/(p-1)^2. This bound is
summable over primes, giving an absolute uniform upper bound on their
product. The bound is valid even if an individual factor vanishes;
we never need its reciprocal or a lower bound.

For p dividing the fixed k, (7) has finitely many terms. Uniformly
on the stated lines and bidisk, |p^(-t)|<=1,
|p^(-1-s)|<=1/p, and |D_j|<=(j+1)p^(j c_0/4).
The denominators in (8) have the same lower bounds as above, while
|1-X|<=1+1/p. The exceptional-prime product is therefore bounded
by a k-dependent constant independent of c, s,t,alpha,beta. We obtain

    |A_k(s,t;alpha,beta)|<=C_k,
    F_k = zeta(1+s+t) A_k /
                       [zeta(1+s+alpha)zeta(1+s+beta)].        (10)

All zeta Euler products in this identity are in their absolute
convergence half-plane. Both reciprocal factors involve s; the factor
with a potential coupled pole involves s+t. No factor with t+beta
is substituted from the opposite-height moment. No exceptional-prime
cancellation is assumed.

### Full degree-two cutoff integral and its tails

For every x>0 and c>0, the elementary degree-two Perron identity is

    (1/(2 pi i)) integral_(Re s=c) x^s ds/s^3
            = (1/2)(max(log x,0))^2.                         (11)

The integral is absolutely convergent. For x>1, shift to Re s=-R
with R>0 fixed and first let the rectangle's height tend to infinity.
The horizontal integrals vanish, since their finite width and numerator
bound depend only on x,c,R while the denominator grows cubically. The
enclosed residue is (log x)^2/2. The new vertical integral in absolute
value is at most x^(-R)/(pi R^2), which tends to zero as R tends to
infinity. For x<1 shift instead to Re s=R>c, crossing no pole;
the same procedure gives bound x^R/(pi R^2), tending to zero.
For x=1, the antiderivative -1/(2s^2) gives zero directly. Thus the
integer-boundary case also has the desired zero cutoff weight.

Using (11) twice yields the exact identity

    J_k(alpha,beta)=4/lambda^4 * (1/(2 pi i)^2)
       integral_(Re s=c) integral_(Re t=c)
                   Y^(s+t) F_k(s,t;alpha,beta) ds dt/(s^3 t^3). (12)

For justification before evaluating or estimating, the absolute mass
of the series (6) is finite for each c, uniformly on both lines and
the bidisk, as proved above. Also |Y^(s+t)|=Y^(2c)=exp(2),
and each integral of |c+iu|^(-3) is 2/c^2. Their product times
that finite mass is an integrable majorant. Fubini therefore permits
termwise integration and both cutoffs in (12). This argument does
not interchange a limit c->0 with an unbounded integral.

For the estimate in (12), use the absolute Dirichlet-series bound

    |zeta(1+s+t)| <= zeta(1+2c) <= 1+1/(2c) <= C/c.          (13)

This holds for every imaginary s,t and controls the entire coupled
pole neighborhood, including opposite large imaginary parts.
From (4), (10) and (13), writing s=c+iu, we obtain

    |F_k(s,t;alpha,beta)|
      <= (C_k/c) |c+iu|^2                   (|u|<=d),
      <= (C_k/c) log^2(2+|u|)               (|u|>d).          (14)

These are independent of imaginary t. Integrating the small and large
s regions separately gives

    integral_(|u|<=d) du/|c+iu| = 2 asinh(d/c)
                                    <= C_d(1+log(1/c)),
    integral_(|u|>d) log^2(2+|u|) du/|c+iu|^3 <= C_d.

The second integral includes the full infinite tail and is uniform
for small c; its integrand is bounded by log^2(2+|u|)/|u|^3.
Integrating all imaginary t costs exactly 2/c^2. Therefore (12)
and lambda^(-4)=c^4 imply the uniform bound

    sup_(|alpha|,|beta|<=c/4) |J_k(alpha,beta)|
                   <= C_k c(1+log(1/c)).                     (15)

There are no omitted boundary pieces, contour shifts through poles,
or uncontrolled order-one tails. The coarse bound (13) is sufficient;
we need neither residues nor a leading nonzero asymptotic constant.

### Both derivative weights and the limit

Since J_k is entire, two-variable Cauchy estimates on the circles of
radius c/4 give for 0<=i,j<=2

    |partial_alpha^i partial_beta^j J_k(0,0)|
        <= i! j! (4/c)^(i+j) C_k c(1+log(1/c)).              (16)

The coefficients of D_ell are
binom(2,i)binom(2,j)ell^(-i-j). Since ell=100 lambda=100/c,
the product of each derivative loss with its normalization is
at most i!j!(4/100)^(i+j). Including the binomial coefficients,
the sum of the nine loss factors is exactly

    [sum_(i=0)^2 binom(2,i) i! /25^i]^2 = (677/625)^2.

Thus the operator preserves the bound C_k c(1+log(1/c)), including
the mixed derivative of order four. Equation (5), with
finitely many r,s, proves

    |Q_N(H)| <= C_N (1+log log Y)/log Y
              = O_N(log log H/log H) = o_N(1).

This proves the stated zero limit with every q weight, p weight and
ordered collision retained. Applying L396 (2) gives the fixed-head
physical carrier conclusion. Constants and the onset may depend on N;
there is no implicit diagonal passage N=N(H). The argument proves a
local specialization using standard reciprocal-zeta bounds, not a
mathematical discovery certified as original or a proof of RH.

### Separate critical audit — step 70

Under the unchanged EXPLORE assessment
`drafts/literature/2026-10-11-mollified-diagonal-limit-audit.md`, the audit
passes for exactly the stated fixed-N hypotheses. L396 (1) has the
denominator (rs)^(5/2) sqrt(abmn)=(rs)^3 a on its collisions, verifying
the factor and the ordered multiplicities in (5). The table above checks
all allowed local exponents, including e>=1; (9) follows by expanding
(1+X-U-V)(1-X)-(1-U)(1-V)=-(X-U)(X-V).
No extra coprimality assumption or reciprocal local factor is introduced.

For clarity, choose c_0 small enough that c_0/4<d/2 and that
|c+iu+alpha| stays in the Laurent disk when |u|<=d. The whole closed
shift bidisk has real part at least 1+3c/4 in both reciprocal arguments.
For |u|>d their heights stay at least d/2 away from zero until the
large-height estimate (3) applies, so the intervening compact bound is
uniform. The exceptional-prime estimates remain independent of both
Mellin heights and c, with k fixed. The product upper bound is sufficient
even at a zero of A_k.

The Fubini majorant is needed only at each fixed c>0; its mass may grow
as c decreases, and no uniform limiting interchange is used. The improved
bound (14), rather than that preliminary majorant, is then integrated.
Writing K_d for the finite large-u integral bound, the resulting cost is

    C_k c^4 c^(-1) (2/c^2) [2 asinh(d/c)+K_d]
         <= C'_k c(1+log(1/c)).

The t integral here is over the entire real line. Bound (13) covers its
coupled numerator even when Im t=-Im s at arbitrarily large heights;
the s tail is likewise untruncated. Equality at either Perron cutoff
has weight zero. The explicit nine-term Cauchy sum above verifies that
both q_H factors preserve this cost. Summing only the fixed finite set
k=rs completes the audit; L396 (2) supplies the physical conclusion.

This is verification of the existing local specialization, not an
additional theorem or an originality claim. The downstream balanced mean,
complete signed mean, any growing-N passage, and all global sign/count
claims are outside the audited result. No RH candidate follows.

## Mathlib

Full matching coverage of this weighted collision-limit theorem has not
been checked. No library absence or Lean verification is claimed.
Supporting ingredients include squarefree Mobius Euler products,
absolute convergence/Fubini, Cauchy's integral formula and elementary
Perron inversion. These do not replace the cited unconditional
reciprocal-zeta input. Step 70's mathematical audit validates the
exceptional-prime factors, full Mellin bounds and derivative transfer;
it is not a formal-library verification.
