# Corollary C028k: affine Meixner-Pollaczek three-coefficient admissibility stop

## Hypotheses

Use the unchanged actual polynomial and exact real coefficient identities
of C028a, for an integer d>=5:

    P_d(x)=sum_(j=0)^d binom(d,j)*b_j*x^(d-j), b_0=1,
    v=b_1^2-b_2=S_2>0,
    b_3-3*b_1*b_2+2*b_1^3=2*S_3=2*tau>0.

The actual-Xi constants v,tau are fixed independently of d. No RH,
real-root, simplicity or numerical-evaluator hypothesis is imposed.
Choose lambda>0, 0<phi<pi, real m and real sigma!=0, common to every
basis degree 0<=n<=d, and define, using the standard Meixner-Pollaczek
normalization,

    q_n(x)=sigma^n*n!/(2*sin(phi))^n
                           *P_n^(lambda)((x-m)/sigma;phi).

Let mu be the pushforward under x=m+sigma*z of the probability measure
proportional to |Gamma(lambda+i*z)|^2*exp((2*phi-pi)*z) dz on R.
Write h_n=integral q_n^2 dmu and P_d=sum_(n=0)^d a_n*q_n.
Call the parameters feasible if a_(d-1)=a_(d-2)=a_(d-3)=0.
Parameters may depend arbitrarily on d, including signed scales,
unbounded parameters and approaches to the excluded boundaries.

## Conclusion

The reference is well defined, monic and orthogonal, with

    r=sigma^2/(4*sin(phi)^2), c=sigma*cot(phi), r>c^2/4,
    h_n=r^n*n!*(2*lambda)_n>0,
    h_n/h_(n-1)=r*n*(n+2*lambda-1)  (n>=1).

Here (u)_n is the rising factorial and h_0=1. Feasible parameters exist
in degree d if and only if

    rho:=tau^2/v^3 < M_d:=(d-1)^2/((d+1)*(d-2)^2).       (1)

In particular there is no feasible unbounded sequence of degrees.
For example every integer

    d>=max{5,ceil(16*v^3/(9*tau^2))}

is infeasible. This stops the stipulated three-match reference diagnostic
before the fourth/fifth retained cost B_d is needed. It does not exclude
unmatched references, other positive measures or other height methods.
It gives no lower bound on actual imaginary root heights and no RH result.
The finite specialization passed independent audit1598; the qualifications
above remain essential.

## Proof

### Imported formulas and all admitted affine parameters

NIST DLMF v1.2.8, [(18.19.6)-(18.19.9)](https://dlmf.nist.gov/18.19),
gives the positive weight above for lambda>0, 0<phi<pi, standard leading
coefficient k_n=(2*sin(phi))^n/n! and squared norm

    H_n=2*pi*Gamma(n+2*lambda)/((2*sin(phi))^(2*lambda)*n!).

Koekoek and Swarttouw, *The Askey-scheme of hypergeometric orthogonal
polynomials and its q-analogue*, report98-17 (1998),
[Section1.7, p37, (1.7.1)-(1.7.4)](https://tudelft.roelofkoekoek.nl/documents/as98.pdf),
supplies the same orthogonality and explicitly monic recurrence; compare
[DLMF (18.22.7)-(18.22.8)](https://dlmf.nist.gov/18.22#E8).
These inspected formulas, covered in source-notes1595, are imported,
not reproved. Their finite affine specialization is the present task.

The leading coefficient gives monicity even when sigma<0. Pushforward
integration divides the standard squared norm by H_0 and multiplies it
by sigma^(2n)*(n!)^2/(2*sin(phi))^(2n), giving the stated h_n. Reflection
of a positive measure introduces no signed Jacobian. The weight has
infinite support and all moments: [DLMF (5.11.9)](https://dlmf.nist.gov/5.11#E9)
gives |Gamma(lambda+i*z)|^2 asymptotic to
2*pi*|z|^(2*lambda-1)*exp(-pi*|z|). The resulting exponential rates
are 2*(pi-phi)>0 at positive infinity and 2*phi>0 at negative infinity.
This check is for each admitted finite tuple; uniform tails in d are
neither asserted nor needed. Gamma has no pole at lambda+i*z here.

The imported monic recurrence becomes exactly

    x*q_n=q_(n+1)+[m-(n+lambda)*c]*q_n
                    +r*n*(n+2*lambda-1)*q_(n-1).         (2)

The n=0 backward term is zero. The parameter identity
4*r-c^2=sigma^2>0 includes both scale signs. Conversely every real c
and r>c^2/4 arises: choose either sigma=+/-sqrt(4*r-c^2) and take
the unique phi in (0,pi) with cot(phi)=c/sigma. Then
sigma^2/(4*sin(phi)^2)=(sigma^2+c^2)/4=r. Thus this change of variables
loses no admitted parameters and admits none of the excluded boundaries.

### Finite matching equations

Let J be the d-by-d real symmetric tridiagonal matrix with diagonal
A_i=m-(i+lambda)*c, i=0,...,d-1, and squared off-diagonal entries
beta_n=r*n*(n+2*lambda-1)>0, n=1,...,d-1. Expansion of det(xI-J)
along its last row gives exactly (2), starting with 1 and x-A_0;
hence det(xI-J)=q_d. This finite identity needs no spectral asymptotic.

Put mu_*=m-c*(lambda+(d-1)/2), the average diagonal of J. For
K=J-mu_*I, its diagonal is D_i=c*((d-1)/2-i), whose sum and cubic
sum vanish by i <-> d-1-i symmetry. Direct matrix multiplication gives

    tr(K^2)=sum_i D_i^2+2*sum_(n=1)^(d-1) beta_n,
    tr(K^3)=sum_i D_i^3
                   +3*sum_(n=1)^(d-1) beta_n*(D_(n-1)+D_n).

In the second formula each edge contributes its two possible diagonal
vertices, each in three cyclic positions; a tridiagonal path has no
three-edge cycle. The elementary sums used are

    sum_i ((d-1)/2-i)^2=d*(d^2-1)/12,
    sum_(n=1)^(d-1) n*(n+2*lambda-1)
                         =d*(d-1)*(d+3*lambda-2)/3,
    sum_(n=1)^(d-1) n*(n+2*lambda-1)*(d-2*n)
                         =-d*(d-1)*(d-2)*(d+2*lambda-1)/6.

For clarity the last identity splits into sum n^2*(d-2*n)
=-d^2*(d-1)*(d-2)/6 and (2*lambda-1)*sum n*(d-2*n), where
sum n*(d-2*n)=-d*(d-1)*(d-2)/6. The usual sums of n,n^2,n^3
give these identities directly. Consequently

    tr(K^2)=d*(d-1)*[c^2*(d+1)/12
                                     +(2*r/3)*(d+3*lambda-2)],
    tr(K^3)=-c*r*d*(d-1)*(d-2)*(d+2*lambda-1)/2.         (3)

Newton's identities applied to the top three coefficients of P_d give
formal root-power sums p_1=-d*b_1,
p_2=d^2*b_1^2-d*(d-1)*b_2 and
p_3=-d^3*b_1^3+3*d*binom(d,2)*b_1*b_2-3*binom(d,3)*b_3.
Their mean is -b_1 and their second/third centered sums are respectively
d*(d-1)*v and -d*(d-1)*(d-2)*tau. These are algebraic identities;
they impose no actual root-reality hypothesis.

Monicity makes the three required cancellations equivalent to equality
of the first three subleading coefficients of q_d and P_d. Newton's
identities are invertible through order three, so this is in turn
equivalent to matching the mean and the two centered sums. Using (3),
the exact necessary and sufficient equations are

    m-c*(lambda+(d-1)/2)=-b_1,
    v=c^2*(d+1)/12+(2*r/3)*(d+3*lambda-2),
    tau=c*r*(d+2*lambda-1)/2.                           (4)

All binomial factors and divisors here are nonzero for d>=5. No fourth
or fifth actual coefficient has entered. Since tau>0, r>0 and
d+2*lambda-1>0, every feasible choice has c>0.

### Exact feasibility range, including boundary approaches

Set k=r/c^2>1/4 and

    V=(d+1)/12+(2*k/3)*(d+3*lambda-2)>0,
    f(k,lambda)=k^2*(d+2*lambda-1)^2/(4*V^3).

Equations (4) require c^2=v/V and rho=f(k,lambda). Conversely these
relations, with c=sqrt(v/V), r=k*c^2 and the translation in (4), imply
all of (4): the squared cubic equation holds by f=rho, and both its
sides are positive, so its unsquared form holds too.

For fixed k>1/4, the logarithmic derivative is

    d/dlambda log f
       =[d+1-2*k*(5*d+6*lambda-1)]
                              /[3*V*(d+2*lambda-1)]<0.  (5)

Indeed its numerator is strictly less than
d+1-(5*d+6*lambda-1)/2=(-3*d+3-6*lambda)/2<0.
Thus f(k,lambda)<f(k,0); evaluation at zero is only a continuous
comparison, not an admissible weight. Write A=(d+1)/12 and
B=2*(d-2)/3. Then f(k,0)=k^2*(d-1)^2/(4*(A+B*k)^3), with

    d/dk log f(k,0)=(2*A-B*k)/(k*(A+B*k)).

It increases up to k_0=2*A/B=(d+1)/(4*(d-2))>1/4 and decreases
thereafter. Since A+B*k_0=3*A=(d+1)/4, its maximum is exactly M_d
in (1). Therefore every admitted tuple satisfies f(k,lambda)<M_d.

For sufficiency suppose 0<rho<M_d. At the fixed k_0, continuity as
lambda decreases to zero gives some strictly positive lambda with
f(k_0,lambda)>rho. For that fixed lambda, f(k,lambda) is continuous
for k>=k_0 and tends to zero as k tends to infinity. The intermediate
value theorem gives a finite k>=k_0>1/4 with f(k,lambda)=rho.
Reconstruct c,r,m as above and choose either signed sigma and its
interior angle using the inverse parameterization following (2).
This produces admitted feasible parameters. Equality rho=M_d is
impossible because (5) makes the bound strict. This proves (1) and
covers all admissible parameter sequences without compactness assumptions.

For d>=5, (d-1)/(d-2)<=4/3, so

    M_d<=16/(9*(d+1)) -> 0.

The fixed rho=tau^2/v^3 is strictly positive. In particular the displayed
degree threshold in the conclusion makes 16/(9*(d+1))<rho, excluding
feasibility there and at every larger degree. This also excludes every
unbounded subsequence, including parameters approaching any boundary.

Schmeisser, *Estimates for the Imaginary Parts of the Zeros of a
Polynomial*, Mathematica Balkanica16 (2002),203-217,
[Theorem1/Corollary1, pp205-207](https://www.math.bas.bg/infres/MathBalk/MB-16/MB-16-203-217.pdf),
is the downstream upper-height interface already specified in C028a.
The present measure meets its hypotheses, but the stipulated first
three cancellations fail eventually. The approved feasibility-first
test therefore stops without evaluating B_d or the full sum. A failed
upper-bound construction supplies no lower bound on actual heights.
The other reference/flow stops are comparisons only, not premises.

### Verification and qualifications

Run `python3 scripts/affine-pollaczek/feasibility_1596.py`. The complete
certificate is `scripts/affine-pollaczek/feasibility-1596.json`:
224 exact rational checks pass, comparing recurrence coefficients with
the mean and centered sums, the edge sum, the optimization value and
the derivative algebra. Degrees 5,6,9,17, positive lambda and both signs
of c (also c=0 as a recurrence check) are covered. These finite checks
are cross-checks, not the proof of (1), sufficiency or all-degree bounds;
the general calculation and all boundary qualifications are written above.
No actual-Xi numerical evaluator or root sample is used. The attempt
uses classical formulas under SPECIALIZE assessment1595 and is classified
REPRODUCTION; no originality beyond the sources checked is asserted.
The independent audit below checks the proof and the complete certificate.

### Independent finite audit1598 (2026-11-18)

Under the unchanged SPECIALIZE assessment1596, the full proof was replayed
against C028a and the inspected primary formulas in source-notes1595.
No mathematical correction or added hypothesis was needed. This verifies
the existing local specialization; no originality claim is made. It
supplies no actual-Xi signs or total-height payment beyond the cited inputs.

For the norm, H_n/H_0=(2*lambda)_n/n!. Multiplication by the squared
monic factor sigma^(2n)*(n!)^2/(2*sin(phi))^(2n) therefore gives exactly
r^n*n!*(2*lambda)_n. This uses pushforward integration, which works for
either scale sign without a signed density factor. The two weight tails
have exponential factors exp(-2*(pi-phi)*z) as z tends to positive
infinity and exp(-2*phi*|z|) as z tends to negative infinity. Both decay
for every admitted angle. The norm and recurrence require no uniform
limit in the parameters.

The finite determinant computation was independently checked by its
permutation expansion. Through order three below the leading term, its
only nonidentity permutations are single adjacent transpositions. With
A_i=m-(i+lambda)*c, let E_j be the elementary symmetric sums of the A_i.
The coefficients at degrees d-1,d-2,d-3 are respectively

    -E_1,
    E_2-sum_n beta_n,
    -E_3+sum_n beta_n*(E_1-A_(n-1)-A_n).

Two disjoint transpositions first occur at degree d-4, so no omitted
permutation contributes here. Newton identities applied to these
coefficients reproduce the mean and both centered traces (3).
For the actual polynomial the centered third sum is precisely

    -d*(d-1)*(d-2)/2 * (b_3-3*b_1*b_2+2*b_1^3)
      =-d*(d-1)*(d-2)*tau.

Thus the factor 1/2 in the last equation of (4) and its sign are correct.
This is an algebraic power-sum comparison, even if actual roots are
nonreal. Triangular monicity gives the converse as well: equality of
these three coefficients makes P_d-q_d have degree at most d-4, hence
all three indicated expansion coefficients vanish. One is not merely
checking necessary moment constraints on an unrelated measure.

For the optimization, write D=d+2*lambda-1. Direct differentiation gives

    partial_lambda log f=4/D-6*k/V
      =(d+1-2*k*(5*d+6*lambda-1))/(3*V*D).

Both denominator factors are positive. Substituting k>1/4 into its
numerator gives a strict upper bound (-3*d+3-6*lambda)/2<0.
The comparison to lambda=0 is therefore strict, independently of how
close an admitted tuple is to that boundary. At lambda=0 the derivative
in k has the single positive sign change 2*A-B*k=0, at the admitted
k_0>1/4, giving exactly M_d. This is a global upper bound, not an
asymptotic valid only on a compact parameter set.

For every 0<rho<M_d, choose a positive lambda with f(k_0,lambda)>rho.
At this fixed lambda, f(k,lambda) tends to zero as k tends to infinity;
continuity on [k_0,infinity) attains rho at some finite k. Taking
c=sqrt(v/V)>0 and r=k*c^2 makes the variance equation exact. The equality
f=rho gives the square of the cubic equation; tau>0 and c*r*D/2>0
recover its required positive sign. The translation then matches the
mean. Finally 4*r-c^2>0 gives sigma_+=sqrt(4*r-c^2) and
sigma_-=-sigma_+. If phi_+ has cot(phi_+)=c/sigma_+, then
phi_-=pi-phi_+ has cot(phi_-)=c/sigma_-. Both are interior angles and
both reconstruct the same c,r. In particular negative sigma is not
lost by requiring c>0. The finite certificate's negative-c examples
check recurrence algebra; they are not the proof about negative scales.

At rho=M_d the strict lambda comparison forbids feasibility. For
d>=max{5,ceil(16/(9*rho))}, one has d+1>16/(9*rho), including integer
equality in the ceiling argument. Hence M_d<=16/(9*(d+1))<rho.
No parameter escape or unbounded subsequence avoids this pointwise
degree bound. This accepts the stipulated matched-family stop, with
unmatched references and all actual-height conclusions still outside it.

Run `python3 scripts/affine-pollaczek/audit_1598.py`. It replays the old
script in a temporary directory and checks byte-for-byte equality with
the saved certificate, preserving the original. An independent
determinant-coefficient calculation, rather than that script's polynomial
recurrence, recomputes the finite power-sum checks. All 224 complete
saved records, including actual/required values, labels and pass fields,
agree; there are zero failures. Full independent records and evidence
conditions are in `scripts/affine-pollaczek/audit-1598.json`. These
finite checks support the audit but do not establish the all-degree
inequality, its strict endpoints or its converse; those are justified
above for the full stated domain. Mathlib coverage remains unknown.

## Mathlib

Not checked. Full matching coverage for this finite affine specialization
and its admissibility criterion is unknown; no absence or formal
verification claim is made. The orthogonality/recurrence inputs are
imported by the precise primary citations above, and the remaining
finite algebra and inequalities are provided in full.
