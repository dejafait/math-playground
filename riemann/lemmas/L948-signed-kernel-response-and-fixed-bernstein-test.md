# Lemma 948: signed kernel response and the fixed Bernstein test

## Hypotheses

Use precisely L938's actual density v, its 34 signed rows c_alpha,
twelve labelled factors, factorials and normalization M_0^12. On
[0,8] let k(x)=K(sqrt(x)), let p be its unchanged degree256 rational
polynomial, and let r=k-p. Retain all257 nodes, theta cutoff8,
precision200, coefficient grid10^-120 and the complete epsilon from
L938(15), so |r|<=epsilon, |k|<7 and |p|<8. Write v_p for the
polynomial-kernel density only on this compact interval. Put

    m=8.935649629627030*10^-35.

This is L947's qualified lower margin at energy4. Arithmetic claims
retain L938's directed Decimal/exponential enclosure and exact-integer
execution contracts. The node enclosure and prior audits are inherited,
not independently rerun here. No sign of r, its derivatives, independence
of residual values, density sign, RH or global crossing bound is assumed.

## Conclusion

There is an exact first-variation response J_p[r] on[0,8] such that

    v(E)-v_p(E)=J_p(r;E)+R_2(E),
    |R_2(E)|<=66 epsilon^2 8^10*pi^6*Z*E^17,
    Z=(293/540)/(2^36*17!).                                      (1)

The complete weighted second-order allowance on[4,8] satisfies

    1.495908638542977*10^-67 <= A_2 <=1.495908638542978*10^-67 < m. (2)

The exact response has the beta-weighted rational-polynomial form
(5) below. Equations(6)-(9) specify the fixed coefficient-wise absolute
Bernstein allowance; this is an upper bound, not an equality for the
actual error. The selected coefficient at full degrees(2816,2822),
last cell[31/4,8] and indices(2816,1411), satisfies

    -1.033700872796998*10^-46 <= b <= -1.033700872796997*10^-46.

Its single positive contribution to that allowance is enclosed by

    [3.306774699321707,3.306774699321708]*10^-74.

This term does not stop the test. It supplies no upper bound for the
full first-order norm or total replacement budget. Those remain open.
This is a specialization of known Taylor/beta methods, not a new
general theorem beyond the assessed sources. Polynomial negative
mass, the outer tail and all-degree mixed positivity remain separate.

## Proof

### Full Taylor remainder and singular faces

For fixed simplex energies x_i=Et_i consider

    g(s)=product_(i=1)^12 (p(x_i)+s r(x_i)),  0<=s<=1.

This is a polynomial in s and hence C^2 on the whole closed interval.
Import Taylor's theorem with its integral remainder, NIST DLMF
[1.4.35-37](https://dlmf.nist.gov/1.4#E35), at order1, and Leibniz's
rule [1.4.12](https://dlmf.nist.gov/1.4#E12). The entire interpolating
amplitude is bounded by8 since p+s r=(1-s)p+s k. The second derivative
is the sum over12*11 ordered distinct pairs, with two residual factors
and ten interpolating factors. Therefore

    |g''(s)|<=132 epsilon^2 8^10,
    g(1)-g(0)=g'(0)+integral_0^1(1-s)g''(s)ds.

The last term is bounded by66 epsilon^2 8^10. This exact remainder
pays every term with at least two residual factors, including all
higher mixed terms; it is not an asymptotic truncation.

Multiply by each row's L938(9) simplex weight and normalization.
All beta parameters k_i+1/2 are positive. On0<=E<=8 the bounded
amplitudes, their s derivatives and the residuals are dominated by
constant multiples of this integrable weight. Dominated convergence
and absolute Fubini therefore justify the finite differentiation,
the remainder integration and the simplex integration, including
all singular faces. No face is removed or assumed to have a bounded
unweighted integrand. Sum with |c_alpha| for the remainder only.
L938's exact beta/gamma cancellation yields Z and proves(1).
At E=0 the continuous densities and both derivative integrals vanish.

The positive exponential majorant exp(E/10)<=exp(4/5) gives

    A_2=exp(4/5)*66 epsilon^2 8^10*pi^6*Z*(8^18-4^18)/18.       (3)

The rational evaluation uses the full epsilon, positive Machin pi
enclosure and degree32 positive exponential-series enclosure retained
in C947b. All constants are unchanged. Equivalently, the rowwise
linear allowance there is multiplied by (11/16)epsilon. This relation
is only a convenient check; the script evaluates(3) directly. It
proves(2), so coefficient work is permitted by the stipulated test.

### Exact signed response reduction

Use L938's integer Q_k(z), positive common C, and polynomial
P(A)=sum_alpha c_alpha product A_k^alpha_k from(5),(18). Define

    D_k(z)=(partial P/partial A_k)(Q_0(z),...,Q_6(z))
          =sum_(l=0)^2816 d_(k,l) z^l,       0<=k<=6.

Every derivative monomial has eleven factors and total index12-k.
The factor alpha_k from differentiation counts the labelled choice
of the residual position. There is no additional permutation or
multinomial coefficient. All34 signed rows are combined in D_k
before any absolute value is taken.

For y>0 the convolution of the eleven unchanged polynomial factors,
summed with these signed multiplicities, is

    H_k(y)=pi^(11/2)/C^11 *sum_l d_(k,l)
                         y^(33/2-k+l)/Gamma(35/2-k+l).         (4)

To check(4), each individual power coefficient has gamma-weighted
Laplace coefficient sqrt(pi) Q_(k,l)/C. Iterated beta integration
divides their product by the gamma function of the sum of their
eleven positive parameters. That sum is12-k+11/2+l=35/2-k+l.
The minimum is23/2>0. The finite polynomial expansion is exact;
no infinite series is interchanged here. This is the positive beta
identity [DLMF5.12.1](https://dlmf.nist.gov/5.12#E1) already justified
for L938's singular factors, with the half-integer gamma recurrence
and duplication identities [DLMF5.5.1/5](https://dlmf.nist.gov/5.5#E5).

The first variation is

    J_p(r;E)=sum_k integral_0^E
                x^(k-1/2) r(x)/(2(2k)!) *H_k(E-x) dx.

Set x=Et, then y=1-t. For h=17-k+l put

    f_(k,l)=d_(k,l)4^h h!/[2 C^11 (2k)! (2h)!],
    Q(E,y)=sum_(k,l) f_(k,l) E^l y^(l+6-k)(1-y)^k,
    w(y)=y^(21/2)(1-y)^(-1/2).

All remaining powers l+6-k and k are nonnegative integers, including
k=6,l=0. Cancelling Gamma(h+1/2) gives the exact formula

    J_p(r;E)=pi^5 E^17 integral_0^1
                         r(E(1-y)) w(y) Q(E,y)dy.             (5)

In particular deg_E Q<=2816 and deg_y Q<=2822. The weight w is
positive and integrable: its beta parameters are23/2 and1/2.
Each term reproduces the original beta parameters after restoring
the displayed powers. Fubini is justified by absolute integrability
of this finite sum against |r|<=epsilon. Thus(5) is valid without
assuming a sign for r or treating its values as independent. It
controls the absolute response for each E before integration in E.

### The fixed full-degree Bernstein allowance

Let D=2816,N=2822 and B_i^d(u)=binom(d,i)u^i(1-u)^(d-i).
For each of the sixteen prescribed cells[a,a+1/4] in[4,8], set
u=4(E-a), and write the unique common-degree representation

    Q(a+u/4,y)=sum_(i=0)^D sum_(j=0)^N b_(a,i,j) B_i^D(u)B_j^N(y).

The bases are nonnegative and sum to1. Apply the coefficient-wise
triangle inequality, then integrate the positive beta weight. This
is the Bernstein convex-combination bound from R. T. Farouki,
*The Bernstein polynomial basis: a centennial retrospective*,
[author slides](https://faculty.engineering.ucdavis.edu/farouki/wp-content/uploads/sites/41/2013/02/Bernstein-polynomial-basis.pdf),
PDF pp12,16-18, as inspected in assessment85. No claim about exact
range attainment or sharpness of this upper bound is imported.
With

    m_(a,i)=integral_a^(a+1/4) E^17 B_i^D(4(E-a))dE,
    nu_j=binom(N,j)(2j+22)!(2N-2j)! /
               [4^(N+11)(j+11)!(N-j)!(N+11)!],

the beta integral is integral_0^1 w(y)B_j^N(y)dy=pi nu_j.
Both m_(a,i) and nu_j are strictly positive rationals. Consequently

    integral_4^8 exp(E/10)|J_p(r;E)|dE <= A_1,
    A_1=exp(4/5)epsilon*pi^6
                *sum_(a,i,j) |b_(a,i,j)|m_(a,i)nu_j.          (6)

The complete replacement certificate requires A_1+A_2<m. Computing
only a selected coefficient cannot prove this inequality, but one
oversized positive summand can disprove that inequality for this
prescribed allowance. It does not lower-bound the actual error.
The alternative maximum-coefficient allowance is at least A_1,
because it replaces each |b| by their cellwise maximum.

### One selected coefficient with no omitted-degree error

Choose the last cell a=31/4, its endpoint index i=D, and j=1411.
Evaluation at u=1 shows that these b_(a,D,j) are exactly the
degree-N Bernstein coefficients of Q(8,y). For A=l+6-k, the exact
degree-elevation identity is

    y^A(1-y)^k
      =sum_j [binom(N-A-k,j-A)/binom(N,j)] B_j^N(y),

where the coefficient vanishes unless A<=j<=N-k. To verify this
particular normalization, multiply the binomial expansion of
(y+(1-y))^(N-A-k) by y^A(1-y)^k; no approximation is involved.
Here A+k=l+6<=N, so

    b_(31/4,D,j)=sum_(k,l) f_(k,l)8^l
                      binom(N-l-6,j-l-6+k)/binom(N,j).        (7)

For j=1411 every l>1411 has l+6-k>j, for all0<=k<=6. Those terms
are identically zero in this coefficient. Thus exact derivative
prefixes through1411 suffice for(7), while the full basis degrees
remain D=2816,N=2822. The calculation does not approximate Q by a
truncation or discard any contribution to a claimed norm bound.
In the polynomial ring modulo z^1412, all multiplication prefixes
are exact because powers are nonnegative. This proves applicability
of the truncated integer products for this selected coefficient only.

The endpoint energy mass is the exact positive rational

    m_(31/4,D)=sum_(z=0)^17 binom(17,z)(31/4)^(17-z)
                                  (1/4)^(z+1)/(D+z+1).      (8)

It follows by expanding (a+u/4)^17 in the integral of u^D.
Equations(6)-(8) give the rigorous allowance contribution

    A_1 >= exp(4/5)epsilon*pi^6
                  |b_(31/4,D,1411)|m_(31/4,D)nu_1411.        (9)

This implication concerns the positive finite coefficient sum in(6).
It does not replace |J_p[r]| by a lower bound, and no cancellation
after the signed E integral is used as absolute-density evidence.

### Execution and limitations

Producer: `python3 scripts/heat/l938-signed-response-89.py`.
The complete report is `scripts/heat/l938-signed-response-89.json`;
the exact derivative-prefix certificate is
`scripts/heat/l938-signed-response-coefficients-89.json`.
All10270 producer checks pass with no failures. It reconstructs the
complete power basis from all257 rational Chebyshev coefficients,
reconstructs full epsilon, checks the unchanged input hash and all
5682 earlier allowance flags, and combines every contributing signed
row in each D_k. The original integer multiplication implementation
is imported for its exact finite algebra, without invoking its main
producer or changing any original file. L938's balanced-digit proof
and execution qualification apply to these multiplications. Modular
checks remain sanity checks, not mathematical identities by themselves.

The selected coefficient uses a common factorial denominator with
H=1428 and (2H)!, checking every required factorial division exactly.
All seven derivative prefixes, seven signed contracted numerators,
the final signed coefficient and both numerical allowances are saved
in full. Directed displays are checked against exact rationals.
The complete second-order upper rational and complete small result
fields were inspected; no sampled coefficient or truncated JSON
preview was substituted for the actual computation.

The additional contraction check is

    python3 scripts/heat/check-l938-signed-response-89.py

Its full report is `scripts/heat/l938-signed-response-check-89.json`.
All19735 checks pass with no failures. It consumes every saved prefix
coefficient and independently clears the half-integer gamma factors
using the odd products O_h=product_(r=1)^h(2r-1), so
4^h h!/(2h)!=2^h/O_h. A common O_H replaces (2H)! in the new
contraction. It checks equality of the entire selected signed rational
coefficient, all contributing degree-elevation identities against
the falling-factorial formula, and nu_j against the odd-product beta
formula. This checks the new contraction, not the producer's derivative
prefix multiplication or inherited theta approximation independently.

The positive selected contribution is between
[3.700653938307707,3.700653938307708]*10^-40 times m. The complete
positive sum in(6) still needs to be bounded. A small summand is not
an upper bound for that sum, and no total norm inequality follows
from this one coefficient. No infeasibility or oversized-bound stop
has been established. The unfinished fixed norm test may continue
without modifying any degree, precision, mesh, kernel or error bound.

## Mathlib

Full or supporting Mathlib coverage of this specialized signed response
and certificate has not been checked. Unknown availability is not
evidence of absence. The standard inputs are the cited Taylor theorem,
Leibniz rule, positive beta/gamma identities and Bernstein partition
of unity. Their specialization above pays the full remainder and
singular faces explicitly; none supplies the required numerical norm.
