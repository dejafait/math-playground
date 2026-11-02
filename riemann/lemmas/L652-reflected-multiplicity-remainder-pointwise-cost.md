# Lemma 652: reflected multiplicity remainder has an excessive pointwise cost

## Hypotheses

Retain L651's full family and notation: n>=5, x=-d=-5/4,
R=11/8, U=R^2, eta=1/100, t_j=j/n; common distinct poles a with
Re(a)=x, |a|<=R-eta, including x; positive integer original residues
r_a, M=sum r_a<=n/3 and P(z)=product_a(z-a)^(r_a). All grid factors
and their conjugated denominator angles are retained. Means are
normalized, and <f,g>=mean f conjugate(g) is linear in the first entry.
There is no separation, symmetry or coefficient-integrality assumption.
In particular

    B_u(z)=product_(j<n) R(z-t_j*u)/(U-t_j*z/u),
    W_a(u)=B_u(x)/B_u(a),  b_u(zeta)=B_u(R*zeta),
    f_u(z)=conjugate(W_(2x-conjugate(z))(u))
          =conjugate(B_u(x))/B_(conjugate(u))(2x-z).

Write f_u=N_u/D_u as a rational function. Let H_u be its remainder
modulo P: deg H_u<M and D_u H_u-N_u is divisible by P. Define

    s_u(zeta)=H_u(R*zeta),
    e_u=P_-(b_u J s_u),  v_u=P_+(b_u J s_u),
    J s=zeta^(-1)conjugate(s),
    K_n(u)=|<F_u,v_u>|^2/||v_u||_2^2,
    A_u=R^(-1)sum_a r_a |W_a(u)|^2.

F_u is the full component in L650/L651, not a grid prefix. Use
sigma=sqrt(137/5000), delta=log(26/19)-(log 2)/3,
epsilon_n=exp(-delta*n), tau_n=(M/sigma)epsilon_n from L651.

## Conclusion

The remainder is well defined, including repeated roots, and has
H_u(a)=conjugate(W_a(u)). Its complete response and norm satisfy

    <F_u,v_u>=B_u(x)<L(R*zeta),e_u>-A_u,
    ||v_u||^2=||s_u||^2-||e_u||^2,
    ||e_u||<=epsilon_n||s_u||,
    |B_u(x)<L(R*zeta),e_u>|<=tau_n||s_u||.                (1)

Thus the positive residue pairing costs the entire polynomial norm:

    max(0,A_u/||s_u||-tau_n) <= sqrt(K_n(u))
       <=(A_u/||s_u||+tau_n)/sqrt(1-epsilon_n^2).         (2)

This norm need not be affordable even on a single repeated anchor.
For n=12q>=24, m=n/3, Z={x}, r_x=m and u=1, put

    lambda_*= (26/47+60/161+85/362+76/603)/32 > 1/25.

Then the exact remainder obeys

    ||s_1|| >= (exp(lambda_* n)-(125/128)^m)/sqrt(m)
             >= exp(n/25)/(2sqrt(m)).                    (3)

Here D_single,n=m^2/(U-d^2)=64m^2/21, and

    exp(n/16) K_n(1)/D_single,n
      <=(26/5)(U-d^2) [ (4m/R^2)exp(-7n/400)
                       +sigma^(-2)exp(-(2delta-1/16)n) ]
      ->0.                                               (4)

This is an admissible countersequence to a *pointwise*, all-angle
rate-1/16 certificate using this specific multiplicity remainder.
It is not a countersequence to its angular mean or to the joint target.
On exactly this family the joint space contains b_u/zeta, with norm
one and response -m/R, so at every angle

    ||Proj_D F_u||^2 / D_single,n >=21/121.               (5)

For the single anchor of residue one the remainder itself is s=1.
For L650's close pair x,a=x+i*2^(-n), both residues one, n>=10,
the remainder satisfies uniformly in u

    s_u(zeta)=1+[(conjugate(W_a(u))-1)/(a-x)]*(R*zeta-x),
    ||s_u||<=13n,  A_u>=1/R,
    sqrt(K_n(u))>=max(0,1/(13Rn)-(2/sigma)epsilon_n).     (6)

Consequently this pair gives K_n(u)>=1/(26Rn)^2 beyond a uniform
onset, and D_single,n<40. It does not obstruct the requested rate.
For fixed n and total multiplicity, the remainder also has a finite
confluent limit when poles with unequal integer residues coalesce;
this is continuity, not a uniform estimate as n increases.

The result stops the pointwise cost argument for this chosen remainder.
The angular mean of K_n, the full joint inequality, Xi realization
and signs remain open. This specialization is separately unaudited;
no certified originality or RH resolution candidate is asserted.

## Proof

### 1. Source scope and exact remainder

The unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-02-joint-full-grid-polynomial-dual.md`
covers this joint space, its full cost and finite polynomial/residue
algebra. Reuse its primary comparison; no new general approximation
or interpolation theorem is assumed. The local comparison read L650's
full polynomial response and close-pair proof, L651's complete proof,
L649's coefficient/diagonal definitions, C645y's component construction,
and the recorded angular-moment and polewise stops. The new test is
the specified multiplicity remainder, not a separately normalized pole
column, a prefix or the untruncated reflected input.

The standard inputs, already inspected in that assessment chain, are
the Hardy projections in L. Baratchart, S. Chevillard and T. Qian,
*Minimax principle and lower bounds in H2-rational approximation*,
J. Approx. Theory 206 (2016), 17--47, preprint v2, 24 March 2015,
[Section 4, (17)--(19)](https://arxiv.org/pdf/1501.01161v2), and
scalar Fourier orthogonality/Parseval in A. Levitt, *Analyse de Fourier
et applications*, version retrieved 2 November 2026,
[Theorem 1.3/Exercise 1.2 and Theorem 1.11/Corollary 1.12,
printed pp.6,8](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf).
The simple-pole rule is R. W. Howell and J. H. Mathews, *Complex
Analysis*, online edition, front matter updated 22 August 2025,
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html).
Their application here is L650 (9)--(10); no reproof or fresh source
audit is claimed. The finite specialization below is needed to evaluate
the actual norm and exponent, which those source statements do not give.

The possible finite poles of f_u are 2x-t_j*conjugate(u), of modulus
at least 2d-t_j>3/2>R. Thus D_u has no zero in the pole region and
is relatively prime to P. Multiplication by D_u is invertible in
C[z]/(P): a polynomial annihilated by it modulo P is divisible by P,
since each root of P is not a root of D_u, including multiplicities.
This is an injective map of an M-dimensional space to itself, hence
surjective. It defines a unique representative H_u of degree <M.
It agrees with f_u and its derivatives through order r_a-1 at a.
Since 2x-conjugate(a)=a, its values are the asserted conjugate weights.
In particular H_u(x)=1, so s_u and v_u are nonzero, the latter by
L651's Gram lower bound.

L650's formula for arbitrary polynomials gives the first equality in
(1), with residue term R^(-1)sum r_a W_a H_u(a)=A_u. L651's negative
part matrix has norm at most epsilon_n. Its bound ||L(R*zeta)||<=M/sigma
and |B_u(x)|<=1 give the last bound in (1). Orthogonal decomposition
gives the norm identity. Combining these with
sqrt(1-epsilon_n^2)||s_u||<=||v_u||<=||s_u|| proves (2).
No positive pairing is substituted for its normalized response.

### 2. Exact repeated-anchor Taylor polynomial

Fix the family in (3). It is admissible: the pole x lies strictly
inside R-eta, has integer residue m=n/3, and there is no separation
condition to check. At u=1 write w=z-x. Then

    f_1(x+w)=product_(j<n) (1+A_j*w)/(1+C_j*w),
    A_j=t_j/(U+d*t_j),   C_j=1/(d+t_j).

For every j, 0<=A_j<C_j<=4/5, because
C_j-A_j=(U-t_j^2)/[(d+t_j)(U+d*t_j)]>0.
Let

    Phi(h)=f_1(x-h)=product_(j<n)(1-A_j*h)/(1-C_j*h)
           =sum_(k>=0) a_k h^k.

All a_k are nonnegative: each factor is
1+(C_j-A_j)h/(1-C_j h). This power series converges absolutely
for |h|<5/4. Since P=(z-x)^m, the remainder is exactly

    H_1(z)=sum_(0<=k<m) a_k(x-z)^k.                      (7)

Take h=R-d=1/8 and H=1/4. Nonnegativity gives the complete tail bound

    sum_(k>=m) a_k h^k <=2^(-m)Phi(H)
        <=2^(-m)(5/4)^n=(125/128)^m<1.                  (8)

Indeed each numerator 1-A_j H is at most one and positive, and
each denominator 1-C_j H is at least 4/5. This bounds the infinite
tail, with no numerical truncation or approximation to its sum.

For C>A>=0 and Ch<1, integrating the derivative of
log(1-Ah)-log(1-Ch), or its convergent series, gives
log[(1-Ah)/(1-Ch)]>=h(C-A). Set

    g(t)=1/(d+t)-t/(U+d*t).

Its derivative is -1/(d+t)^2-U/(U+dt)^2<0. The n grid points
split into four blocks of n/4 points, each bounded above by its
right endpoint l/4. Therefore

    log Phi(1/8)>= (1/8)sum_(j<n)g(t_j)
                    >=(n/32)sum_(l=1)^4 g(l/4)
                    =lambda_* n.

The four values are exactly 26/47,60/161,85/362,76/603.
Their sum is greater than 32/25 by rational arithmetic, proving
lambda_*>1/25. Since s_1(-1)=H_1(-R), (7)--(8) give its lower
bound in (3) before division by sqrt(m). For any polynomial of
degree <m, Fourier orthogonality and Cauchy--Schwarz give
|s(-1)|<=sqrt(m)||s||_2. Finally n>=24 implies exp(n/25)>2:
already 1+24/25+(24/25)^2/2>2. This proves both inequalities (3).

### 3. Normalized response and the precise scope of the stop

For this single pole, W_x=1, A_1=m/R and D_single,n=m^2/(U-d^2).
L651 gives 1-epsilon_n^2>=5/13 and delta>1/16. Square the upper
bound in (2), using (a+b)^2<=2a^2+2b^2 and (3). It follows that

    K_n(1)<= (26/5)m^2 [ (4m/R^2)exp(-2n/25)
                         +sigma^(-2)exp(-2delta*n) ].

Division by the exact diagonal proves (4), since
2/25-1/16=7/400>0 and 2delta-1/16>1/16. This controls the whole
correction even though the unnormalized polynomial is exponentially
large. Every constant and onset used here is uniform on this sequence.

The joint target is not bounded above by this one-vector response.
Indeed s=1 gives J s=zeta^(-1), and b_u(0)=0 makes b_u/zeta analytic
of norm one. L650's response formula has zero negative-part correction
and gives -m/R. This vector lies in the joint space for every m>=1.
Taking its squared response and dividing by D_single,n gives (5).

Crucially (4) tests u=1 only. An isolated angle has zero angular
measure; neither continuity for each n nor this pointwise upper bound
establishes an upper bound for mean_u K_n(u). No angular obstruction
or failure of L651's S_n inequality is inferred. The decision supported
by (4) is to abandon a uniform pointwise norm estimate for the chosen
Hermite remainder and remove unnecessary multiplicity conditions in
any subsequent value-interpolation test.

### 4. Required normalization and confluent cases

For Z={x}, r_x=1, the remainder is the constant f_u(x)=1, giving
norm one and response -1/R. Thus (3) arises from the imposed higher
jets, not from single-pole normalization.

For L650's close pair, degree less than two and the two prescribed
values give the polynomial in (6). L650 (11) proves uniformly in u

    |W_a-1|<=exp(6n*2^(-n))-1.

For n>=10, 6n*2^(-n)<1/16. The nonnegative exponential series gives
exp(v)-1<=v/(1-v) for 0<=v<1. Hence the absolute value of the
divided difference in (6) is at most (32/5)n. Since
||R*zeta-x||=sqrt(U+d^2)=sqrt(221)/8, the triangle inequality gives

    ||s_u||<=1+(4sqrt(221)/5)n<=13n,

where sqrt(221)<15. Also A_u=(1+|W_a|^2)/R>=1/R. Apply (2) with
M=2 to obtain (6). Because n exp(-delta n)->0, its right side is
at least 1/(26Rn) beyond an onset independent of u. L650 (8) gives
D_single,n<40. The resulting polynomial lower bound is sufficient
for the requested exponential rate on this particular pair only.

For fixed n,M,u, the matrix of multiplication by D_u modulo P has
entries continuous in the coefficients of P (reduce powers by its
monic equation). Its determinant remains nonzero when roots merge
in |z|<=R-eta, by the same relative-primality argument as above.
The adjugate formula therefore makes the remainder coefficients
continuous at those mergers. If two residues r_1,r_2 merge, P tends
to a polynomial with their summed multiplicity. If all merge at x,
the limit is the Taylor polynomial of order M-1 used above. This
covers unequal integer residues without a separation denominator.
It does not control the cost as n and M grow; (3) explicitly prevents
one particular cheap bound in that regime.

### 5. Verification and qualifications

The exact finite check is
`python3 scripts/one-sided-hankel/reflected-remainder-cost-check.py`.
Its full certificate is
`scripts/one-sided-hankel/reflected-remainder-cost-check.json`.
It checks the rational constants, reconstructs repeated-anchor Taylor
remainders, verifies every modular coefficient, and evaluates the full
polynomial norm and negative-part correction at four finite sizes.
The uniform claims follow from the proof above; no floating-point
screen or finite list establishes them. Separate critical audits of
this result and the inherited L650/L651 inputs remain outstanding.

## Mathlib

Full matching coverage of this reflected remainder and its cost bound
has not been checked. The cited Fourier/projection/residue facts are
supporting inputs. Unknown availability is not evidence of absence.
No formal theorem supplying the open angular bound or Xi positivity
is assumed.
