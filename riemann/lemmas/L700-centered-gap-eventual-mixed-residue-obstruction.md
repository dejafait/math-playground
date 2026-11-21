# Lemma 700: eventual opposite scalar residues in the centered-gap family

## Hypotheses

Fix any one reflection-symmetric Picard profile selected by L699 from
L694/L696. In particular all its choices, including the positive gap
width, precede n; its real shifts obey

    E=sum_(m in Z)|e_m|<infinity,  |e_m|<=1/8,
    e_(-m-1)=-e_m.

Use exactly L666/L699's constants and finite family:

    d=5/4, x=-d, R=11/8, U=121/64, A=27/10,
    n=12q+3, q>=1, J=n-1, M=4q+1, h=A/n,
    a_m=x+i*h*(m+1/2+e_m),  -2q<=m<2q,
    Z={x} union {a_m},  p_j=x*j/(U*n),
    c_(0,n)=R^(-1) sum_(a in Z) W_a,
    rho_(j,n)=Res_(u=p_j)c_(0,n)(u).

Keep the original unit masses, anchor, j=0 product factor, denominator
angle 1/u and all M spatial moments. A cancelled pole has residue zero.
No scalar-rate, sign, H/support or Xi-realization hypothesis is assumed.

## Conclusion

For every such fixed profile there is an N such that, for every allowed
n>=N, two indices j_+,j_- in {1,...,64} satisfy

    rho_(j_+,n)>0,             rho_(j_-,n)<0.                    (1)

Consequently no fixed profile in L699's stated class can have all its
interior residues nonzero of one common sign on an unbounded sequence.
This rules out that sufficient interlacing mechanism with its full
existential-profile and unbounded-subsequence quantifiers. It does not
refute L699's broader scalar logarithmic target, full-spatial compensation,
H/support, realization or RH. No effective N or uniform onset over
Picard choices is asserted.

The proof uses a fixed-index endpoint asymptotic and a finite exact
integer/interval certificate. It is a local obstruction relative
to the inspected sources, not a certified originality claim. Step 133
critically audited this proof, its required L699 reflection/residue input,
and every interval-certificate record; details are in Section 6. L699's
other conclusions were not audited in that step. No approximation to the Picard
profile, finite sample of n, or assumed Herglotz membership is used.

## Proof

### 1. Approved scope, exact residues and the needed normalization

Reuse the invocation-start EXPLORE assessment
`drafts/literature/2026-11-03-centered-gap-real-residue-sign.md`.
Its comparison with McKee--Smyth, *There are Salem numbers of every
trace*, arXiv:math/0308213v2, Lemma 4, p.3, and Reiffenstein,
arXiv:2108.10746v3, Theorem 2.2, pp.2--3, does not establish signs
for this family. Neither theorem is an input to the obstruction.
The complete finite-family residue expression is L699 (7), obtained
from L666's exact rational continuation. The present difference is
an estimate of those actual residues; no interlacing theorem is reproved.

For real y define w(y)=(1-i*y/d)^(-1)=x/(x+i*y), and for fixed
positive integer j<n define

    F_(j,n)(y)=w(y) product_(k=1)^(n-1)
                    (1-j*w(y)/k)/(1-j*k*w(y)/(U*n^2)),
    S_(j,n)=sum_(-2q<=m<2q) F_(j,n)(h*(m+1/2+e_m)).             (2)

Directly factoring a from A_a and -k*a/n from C_a in L699 gives

    (x/a)*C_a(p_j)/A_a(p_j)=[(n-1)!/n^(n-1)]*F_(j,n)(Im a).

Here J is even, so the displayed factorial factor is positive. The
anchor contributes no residue. All A_a(p_j) are nonzero, and the
remaining real prefactor in L699 (7) has sign (-1)^(j-1): A_x(p_j)>0,
and exactly j-1 factors U*p_j-t_k*x in its denominator are negative.
Reflection pairs y and -y; F_(j,n)(-y)=conjugate(F_(j,n)(y)). Thus
S_(j,n) is real and, whenever it is nonzero,

    sign rho_(j,n)=sign[(-1)^(j-1)*S_(j,n)].                    (3)

This includes the possibility of cancellation when S_(j,n)=0.

### 2. A finite-product limit with the explicit error needed below

Define an entire function by locally uniform convergence:

    Ecal(z)=lim_(K->infinity) K^z product_(k=1)^K(1-z/k),       (4)

where K^z=exp(z*log K) uses the real logarithm. The elementary
finite-ratio argument here supplies an explicit tail bound for the
certificate. No gamma-function asymptotic or uninspected special-function
theorem is needed. This short convergence calculation is included
because a qualitative product identity would not certify that bound.
For comparison, the classical identification is Ecal(z)=1/Gamma(1-z),
from [NIST DLMF 5.8.1--2](https://dlmf.nist.gov/5.8), with the entire
reciprocal extension described in [5.2(i)](https://dlmf.nist.gov/5.2#i).
The proof below retains the explicit absolute remainder needed here;
it does not present Euler's product as a new result.

For K>|z| and L>K, divide the L-th product by its K-th counterpart,
away from the finitely many zeros. The logarithm of this ratio is

    z*[log(L/K)-sum_(k=K+1)^L 1/k]
       +sum_(k=K+1)^L [log(1-z/k)+z/k].                        (5)

Every logarithm in the last sum uses its convergent power series at 1.
The real bracket increases with L, since
log(1+1/L)>1/(L+1), and lies in [0,1/K] by comparison with the
integral of 1/t. Its limit therefore exists. Also

    |log(1-v)+v|<=|v|^2/[2*(1-|v|)],        |v|<1,
    sum_(k>K) k^(-2)<=1/K.

The second sum in (5) converges locally uniformly. Its limit, plus
the first term, denoted T_K(z), satisfies

    |T_K(z)|<=|z|/K+|z|^2/[2*K*(1-|z|/(K+1))].                (6)

Multiplying the finite polynomial by K^z*exp(T_K(z)) defines (4)
on |z|<K, even at its integer zeros. These definitions agree as K
increases. They prove entire locally uniform convergence, with
O_B(1/K) absolute error on every fixed disk |z|<=B. Cauchy's
derivative estimate on a slightly larger disk gives the same error
for any fixed number of derivatives. The only zeros of Ecal are
the positive integers: for nonintegral z choose K>|z|; all finite
factors and exp(T_K(z)) are nonzero. In particular Ecal(j)=0 and
Ecal(j*w_*)!=0 for the nonreal w_* below.

For fixed j, put

    H_j(w)=w*Ecal(j*w)*exp(j*w/(2*U)).

Uniformly for y in [-Y,Y], where Y=A/6=9/20, and also for the
first y derivative, the finite product in (2) has the form

    F_(j,n)(y)=n^(-j*w(y))*[H_j(w(y))+O_j(1/n)].               (7)

To check the denominator, for sufficiently large n its logarithm is

    sum_(k=1)^(n-1) log(1-j*k*w/(U*n^2))
       =-j*w*(n-1)/(2*U*n)+O_j(1/n)
       =-j*w/(2*U)+O_j(1/n).

The quadratic remainder is O_j(sum k^2/n^4)=O_j(1/n), locally
uniformly in w. For the numerator use (4) at K=n-1 and
((n-1)/n)^(-j*w)=1+O_j(1/n), again on a fixed complex neighborhood.
Local uniformity and the derivative estimate justify differentiating
the bracket in (7). The bracket error is absolute, including w=1,
where H_j vanishes. No relative division by that zero is made.

Write L=log n and

    w_*=w(Y)=(625+225*i)/706=alpha+i*beta,
    alpha=625/706,             beta=225/706.

On [-Y,Y], Re w>=alpha and w'=(i/d)*w^2 never vanishes. Equation
(7) implies, for each fixed j,

    sup |F_(j,n)|<=C_j*n^(-j*alpha),
    sup |F'_(j,n)|<=C_j*(1+L)*n^(-j*alpha).                   (8)

All constants may depend on the fixed finite set of j under study.

### 3. The exact shifted finite sum has a universal outer-endpoint term

The unshifted ordinates h*(m+1/2) are midpoints of a mesh partition
of [-2q*h,2q*h]. This interval has endpoint

    2q*h=Y-A/(2*n).

Every segment between a midpoint and its displaced point remains
in [-Y,Y], by cap 1/8 and the exact finite endpoints. The mean
value bound from (8) therefore gives

    |S_(j,n)-sum_m F_(j,n)(h*(m+1/2))|
       <=h*E*sup |F'_(j,n)|
       <=C_j*E*(1+L)*n^(-j*alpha-1).                         (9)

For a complex C^1 function f, the midpoint error on each mesh cell
obeys |f(midpoint)-h^(-1) integral_cell f|<=h*sup|f'|/4.
Summing over these cells gives O(sup|f'|), since their total length
is bounded. Extending the interval from [-2q*h,2q*h] to [-Y,Y]
changes h^(-1) times the integral by O(sup|f|); the total added
length is h. Using (7)--(9) gives

    S_(j,n)=(n/A) integral_(-Y)^Y
                   H_j(w(y))*exp(-j*L*w(y))dy
             +O_j((1+L)*n^(-j*alpha))
             +O_j(E*(1+L)*n^(-j*alpha-1)).                    (10)

The absolute product error contributes only O_j(n^(-j*alpha))
after multiplying the integral by n/A. All endpoints, shifts and
the absence of an anchor term in the residue sum have been retained.

The integral is twice the real part of its positive-half integral.
Let H(y)=H_j(w(y)). Integration by parts there gives

    integral_0^Y H(y)*exp(-j*L*w(y))dy
       =-[H(y)*exp(-j*L*w(y))/(j*L*w'(y))]_0^Y
         +(1/(j*L)) integral_0^Y (H/w')'(y)*exp(-j*L*w(y))dy.

The lower boundary term vanishes because H(0)=H_j(1)=0 for
positive integer j. The derivative (H/w')' is bounded. To bound
the remainder, Re w(y)=1/(1+(y/d)^2) is strictly decreasing on
(0,Y], and its derivative is bounded away from zero on [Y/2,Y].
Hence for positive constants c,delta depending only on d,Y,

    integral_0^Y exp(-j*L*Re w(y))dy
       <=(Y/2)*n^(-j*(alpha+delta))
          +n^(-j*alpha)/(j*c*L)
       =O_j(n^(-j*alpha)/L).

Thus, with the nonzero constant

    B_j=-H_j(w_*)/(j*w'(Y))
       =i*d*Ecal(j*w_*)*exp(j*w_*/(2*U))/(j*w_*),              (11)

equation (10) becomes

    S_(j,n)=[2*n^(1-j*alpha)/(A*L)]
             *{Re[B_j*exp(-i*j*beta*L)]+o_(j,E)(1)}.         (12)

More explicitly the absolute normalized error inside braces is

    O_j(1/L+(1+L)*L/n+E*(1+L)*L/n^2).

It tends to zero for every fixed E. For finitely many j it does so
simultaneously. The prescribed-center Fourier gap is not used in
this estimate; l1, the cap and reflection, already satisfied by
every selected profile, suffice. In particular no finite Picard
approximation or uniform tail-decay rate is hidden in (12).

### 4. A complete finite phase certificate

Set

    D_j=(-1)^(j-1)*B_j/|B_j|,       f_j(theta)=Re[D_j*exp(-i*j*theta)].

The following certified inequality is the finite sign input:

    for every real theta,
    max_(1<=j<=64) f_j(theta)>1/2,
    min_(1<=j<=64) f_j(theta)<-1/2.                            (13)

The complete reproducible certificate is
`scripts/one-sided-hankel/centered-gap-residue-certificate-131.json`;
run `python3 scripts/one-sided-hankel/centered-gap-residue-certificate-131.py`.
The script uses only Python integers and outward Decimal intervals.
It stores every finite-product enclosure and a positive and negative
witness at each of the 2048 grid points. No library gamma or unbounded
floating-point transcendental evaluation is trusted.

Here are all the mathematical error estimates behind that finite check.
Use K=32768 and replace Ecal(j*w_*) by
K^(j*w_*) product_(k=1)^K(1-j*w_*/k). By (6), since |w_*|<1,
the exact logarithmic ratio to Ecal(j*w_*) has absolute value at most

    delta_j=j/K+j^2/[2*K*(1-j/(K+1))],
    delta_j<=delta_64<0.064575430457882.                       (14)

Its imaginary part controls the phase error. After normalization
to modulus one, the distance between the two unit complex numbers
is at most delta_j, since |exp(i*t)-1|<=|t|. Thus each corresponding
real f_j value has error at most delta_64.

All omitted factors from (11) are positive real except those retained
in the following direction vector for the finite approximation:

    (-1)^(j-1)*(9+25*i)
       *product_(k=1)^K [(706*k-625*j)-225*j*i]
       *exp(i*j*beta*(log K+1/(2*U))).                        (15)

Indeed i/w_*=(9+25*i)/25. The finite product and the multiplier
9+25*i are evaluated with exact integer complex arithmetic by a
balanced multiplication tree. Removing one common positive power of
two and enclosing the two scaled integers by adjacent integers
loses no direction: if shift=s, a/2^s is in
[a div 2^s,a div 2^s+1], also for negative a with floor division.
The script retains approximately 200 leading bits before outward
normalization by the Euclidean norm. Square-root endpoints are
checked by outward squaring, so the enclosing assertion is verified
arithmetically. Hashes identify both complete integer products; they
are reproducible from the script, not additional numerical premises.

For completeness, pi is enclosed using Machin's arctangent identity
pi=16*atan(1/5)-4*atan(1/239), with 120 alternating-series terms
and an explicit next-term bound. The identity follows from tangent
addition and the first-quadrant ranges. Also log K=15*log 2, where
log 2=2*sum_(r>=0) (1/3)^(2r+1)/(2r+1). After 100 terms the
remaining positive tail is at most
2*(1/3)^201/[201*(1-1/9)]. For sine and cosine, reduce by any
integer multiple of 2*pi with interval arithmetic, verify |v|<4,
then use Taylor polynomials through degree 161 and remainder
4^162/162!. All additions, products, divisions and series operations
are outward at 70 decimal digits. Those elementary series are used
with explicit remainders because ordinary sampled trigonometry would
not prove (13).

Let theta_k=2*pi*k/2048, 0<=k<2048. At each point the script
computes intervals for all 64 finite-product approximations to f_j
and retains indices with the largest positive lower endpoint and
largest negative magnitude lower endpoint. Every circle phase is
within pi/2048 of a grid point. Since |f_j'|<=j<=64, the additional
continuous-grid cost is

    64*pi/2048<0.098174770424682.                              (16)

Subtracting both (14) and (16) from the minimum of the two retained
lower margins, at every grid point, gives the recorded overall bound

    paid margin > 0.8038058493320059 > 1/2.                    (17)

All 2048 cells passed; the certificate's failure list is empty. This
is a check of the complete continuous phase circle, not a preview or
a claim from a sampled minimum alone. Equations (14)--(16) and the
outward finite arithmetic justify the inequality between samples.
The floating diagnostic in `centered-gap-residue-sign-131.json` is
retained separately, with its failure list, and is not a premise.

### 5. Quantifiers and the eventual obstruction

Use Re[(-1)^(j-1)*B_j*exp(-i*j*theta)]=|B_j|*f_j(theta)
and divide the error in braces by the fixed nonzero |B_j|. The real
scale 2*n^(1-j*alpha)/(A*L) is positive, and for all j<=64 this gives

    (-1)^(j-1)*S_(j,n)
       =[2*|B_j|*n^(1-j*alpha)/(A*L)]
          *{f_j(beta*log n)+o_E(1)}.                          (18)

Every B_j is nonzero and there are only 64 of them, so the error is
simultaneously smaller than 1/4 in absolute value for all sufficiently
large n. Enlarge this onset to put all 64 indices below n. Apply
(13) at the actual phase theta=beta*log n, without selecting a
subsequence or assuming any equidistribution. At least one bracket
in (18) is >1/4 and another is <-1/4. Equation (3) proves (1).

This argument works for each fixed admissible Picard choice, with
its own finite E and onset. Thus every such choice has only finitely
many n at which L699's strict common-sign condition could hold. It
cannot hold on an unbounded subsequence for any fixed choice. Nothing
here estimates the scalar numerator's other zeros or its complete
logarithmic rate. Mixed residues do not disprove those broader claims,
and they supply no information about actual Xi beyond eliminating
this sufficient model-family mechanism.

### 6. Critical audit, 3 November 2026 (step 133)

The ready EXPLORE assessment for the separate audit is
`drafts/literature/2026-11-03-centered-gap-mixed-residue-audit.md`.
The audit checked all of Sections 1--5 and the entire certificate
generator. Its outcome is verification of this existing local obstruction,
not a new sign theorem or an extension of its scope. The harmless inverse
power in the K=n-1 normalization and the wording preceding (18) were
made explicit; neither correction changes an estimate or conclusion.

**Required upstream inputs.** Starting from L666 (6), divide its full
products, including j=0, to obtain L699 (6). At p_j,
C_x'(p_j)=U*product_(k!=j)(U*p_j-k*x/n). The anchor is identically one
and has zero residue. Every A_a(p_j) is nonzero because the nonanchor
a has nonzero imaginary part. Since
A_x(p_j)=x^J*product_k(1-j*k/(U*n^2)), J is even and U>1, this is
positive. Exactly the k<j factors of C_x'(p_j) are negative. Factoring
-k*a/n from C_a and a from A_a gives the positive factorial in
Section 1, proving the normalization and sign (3) without assuming
the conditional common-sign assertion of L699.

For the selected profile, L696 (6) uses real even chi, and L694 uses
real even Phi. Thus the actual input is Q(t)=-exp(-pi*i*t)*chi(t)/(2*pi*i*t).
Direct substitution gives Theta Q=Q. Under m=-k-1 the nonlinear
summand with coefficient -alpha_k is exp(-2*pi*i*(k+1)*t) times
(exp(-2*pi*i*alpha_k*t)-1+2*pi*i*alpha_k*t)*Phi(t)/(2*pi*i*t).
This is precisely the kth summand of Theta R(alpha), proving the
equivariance in L699. L694 (3)--(9) give absolute convergence in the
Wiener norm at every iterate and at the same limit. Theta is a norm
isometry, so it passes to that limit. Hence e_(-m-1)=-e_m for every
fixed allowed prescription. The cap and l1 bound are exactly the
audited L694 inputs specialized in L696 Section 2; no uniform bound
over different cutoffs is asserted. No other L699 conclusion is needed.

**Analytic transfer.** The logarithm in (5) is a tail logarithm on
|z|<K, with no division by a finite-product zero after its exponential
representation is extended. Its harmonic bracket lies in [0,1/K];
the quadratic tail is bounded by (6). On each fixed disk this yields
absolute O(1/K) errors, and Cauchy on a larger fixed disk gives the
derivative error. In (7) the factors n^(-j*w) are kept exactly;
differentiating them costs O_j(log n), as already allowed in (8).
This avoids a relative estimate at w=1. For the exact endpoints,
2q*h=Y-h/2, and the displaced extreme ordinates are within
[-Y,Y] by the 1/8 cap. The midpoint error summed over all cells is
bounded by (total length)/4 times sup|F'|. The two added end intervals
have combined length h. The l1 perturbation costs only h*E*sup|F'|.
These facts give every error in (10).

On [Y/2,Y] the negative derivative of Re w is bounded below, giving
the 1/log n integral factor used after integration by parts. The
interval [0,Y/2] has a fixed strictly larger real part; its exponential
bound is smaller. At zero H_j(1)=0 exactly. Since w' never vanishes,
the integration by parts is legitimate and gives the sign and phase
of B_j in (11). At Y the argument j*w_* is nonreal, so Ecal(j*w_*)
is nonzero. All 64 fixed |B_j| are positive; no bound uniform in j
or in moving profiles is needed. After their normalization the displayed
errors tend to zero for every fixed E, including along every allowed n.

**Containment and complete replay.** The Decimal addition, multiplication
and reciprocal wrappers use directed endpoint operations; interval
negation uses exact copy_negate. All interval divisors exclude zero.
In square, the exponent 2 is an integer square. Although Decimal sqrt
uses nearest-even rounding independently of the context, the subsequent
assertions prove lo^2<=x.lo and hi^2>=x.hi using an upper square for lo
and a lower square for hi, with lo>=0. This verifies containment directly.
The exact integer product tree and floor shifts also enclose negative
coordinates. The normalization divides their rectangle by an enclosing
positive Euclidean norm, and preserves the exact direction.

The phase multiplier in (15) uses beta=225/706 and 1/(2U)=32/121.
Its remaining discarded factors are positive reals. The integer chosen
by cis need not be a rigorously rounded quotient: any integer reduction
is valid, and |v|<4 is asserted after outward subtraction of 2*pi*q.
The denominator 2*(PI.lo+PI.hi) in that choice is consistent with the
sum x.lo+x.hi; this checks the earlier factor-of-two regression. The
Taylor recurrences give cosine through degree 160 (also its degree-161
polynomial) and sine through 161, so 4^162/162! bounds both remainders.
The atan and log tails include the first omitted terms. Decimal tail
endpoints have at most the context's 70 significant digits, so the
unary negation used to form symmetric tail intervals is exact here.

Run `python3 scripts/one-sided-hankel/centered-gap-residue-audit-133.py`.
It executes the unchanged generator with a distinct output path,
preserves the original bytes, and compares every field of the complete
replay, including all product hashes, scaled integer enclosures, unit
direction intervals and all 2048 pairs of phase witnesses. Its additional
exact Fraction checks verify the Machin and log-series bounds against
the saved constant enclosures, both deducted costs, and each cell's
strict paid margin. Full evidence is in
`scripts/one-sided-hankel/centered-gap-residue-audit-133.json` and
`scripts/one-sided-hankel/centered-gap-residue-certificate-replay-133.json`.
All 64 product records and all 2048 cells matched; no failure occurred.
The exact recorded minimum is

    0.8038058493320059692331479488286023454911217959396881835845804411723740,

strictly greater than the required 0.5. Both signs use the same grid
phase and all phases, including the wraparound cell, are within
pi/2048 of a grid point. Paying the phase-tail and derivative costs
therefore verifies (13) over the whole circle. This is a full replay
plus a mathematical audit of its arithmetic, not formal verification.

The arithmetic semantics were compared in the ready assessment with
the [Python Decimal reference](https://docs.python.org/3/library/decimal.html)
and the [Decimal Arithmetic Specification v1.70, square root](https://speleotrove.com/decimal/daops.html#refsqrt).
Complex endpoint theory is compared there with
[DLMF 2.4(iii), equations 2.4.10--13](https://dlmf.nist.gov/2.4#iii).
No unchecked general endpoint theorem replaces the direct bounded
integration-by-parts proof above.

Finally (13) applies at the actual phase beta*log n without density or
subsequence arguments. Finitely many normalized errors become <1/4
simultaneously for each fixed profile. This proves the eventual
quantifier in (1), and thereby excludes an unbounded common-sign
subsequence for every such choice. It does not bound other numerator
zeros, scalar logarithmic compensation, H/support or actual-Xi signs.

## Mathlib

Full matching coverage for this fixed-index endpoint asymptotic,
finite integer/interval phase certificate and eventual sign obstruction
has not been checked. No absence claim or formal verification is made.
The Mahler-measure support recorded in L699 is not used to prove (1).
