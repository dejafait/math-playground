# C499c — Phase-sensitive 256-index endpoint reserve

## Hypotheses

Use the exact H_t, M_t, alpha and frozen-index remainder of L494,
the literal resultant G_tilde of L495, and L496's phase interface.
Fix exact rational decimals and integers

    t=.16836, X=6000284561421.5, n=691004, N=691260,
    Y=4*pi*(N^2-t/16), P={primes<=307},
    ell0=24.18022820120389, c=.500000000001,
    epsilon=6e-7,
    epsilon_1=((6e-7+1.3e-6)*8.770232)/.14142,
    r0=14176540015048665224252705167939023
       /33554432000000000000000000000000000000.

Retain L499's audited full old-model coefficient mass and positive
envelopes R0,J0,D0 at X. L497/L498 enter through that accepted mass,
not through a new coefficient replay. All comparisons below are at
the SAME actual nu(Y), Euler product, phase and ell(Y). The n model
at Y is a finite comparison only. The true remainder and all spatial
derivatives there freeze the canonical NEW index N, including equality.

For the interpretation concerning H_t, retain Polymath,
*Effective approximation of heat flow evolution of the Riemann xi
function, and a new upper bound for the de Bruijn–Newman constant*,
Research in the Mathematical Sciences 6 (2019), article 31,
[arXiv:1904.12438v2, Theorem 1.3 and (3)–(24)](https://arxiv.org/html/1904.12438v2),
and Michel Planat, *Collective Contraction in the de Bruijn–Newman
Heat Flow: Off-Zero Logarithmic Derivatives and Certified Barrier
Refinements*, [arXiv:2609.37164v2, Lemma 6.3 and Sections 6.6–6.7,
(40)–(45), Lemma 6.10](https://arxiv.org/html/2609.37164v2#S6.SS7).
Their saddle/base-phase manuscript proofs remain unaudited. The local
reproductions L494–L496/L499 retain their stated audit qualifications.

## Conclusion

The complete literal resultant increment obeys

    |G_tilde_N(Y)-G_tilde_n(Y)| <= B_G
       < .000000050913372122.

Both charges for the NEW model have the full-support upper envelopes
U_s,B,U_r,B proved below, with

    B_G+U_s,B+U_r,B < .000020881403151711 < r0,
    r0-B_G-U_s,B-U_r,B > .000401612412718832.

Consequently, under the retained analytic inputs, H_t(Y) and H_t'(Y)
cannot both vanish. This is one endpoint only. It does not exclude
intermediate-cell collisions, later blocks, other times, H1 or zero time,
and it does not prove actual-Xi all-degree signs or RH.

A complete positive absolute-channel block envelope computed with the
same support is in (.000701363160671208,.000701363160671209).
Its ratio to the certified modulus enclosure exceeds 13775. This is a
comparison of a conservative envelope with the actual complex increment,
not a lower bound for an absolute norm or an optimal cancellation factor.
The coarser maximum-support envelope exceeds .00804038. Both absolute
envelopes exceed r0 and cannot by themselves certify this comparison.

This is a finite computational specialization of the cited resultant
and charge method, not a new asymptotic or transport mechanism. The
separate critical audit in Section 6 accepts this local proof and its
complete rational certificate, retaining the analytic input qualifications.

## Proof

### 1. Closed domain, old-model lower bound and exact index

Y/(4*pi)+t/16=N^2 exactly. Hence its nonnegative square root has
floor N at equality. The certificate verifies Y>X and

    t*(log(X/(4*pi))+(Y-X)/X)<5.17.

Since log(Y/X)<=(Y-X)/X, L494 and L496 apply on the closed segment
[X,Y]. Every Euler factor is nonzero, ell>ell0 and |nu'|<c there.
L494's full epsilon_1 applies with N frozen at Y; the entering pair
in that Cauchy allowance is kept independently of the finite increment.

For the fixed old model write its real coefficients as beta_m and set
c_m(x)=beta_m*m^(-sigma(x)), h(m)=max(1,2*log(m)/ell0-1).
L496 gives sigma'(x)=t*x*(x^2+5)/(4*(1+x^2)^2)>0. Thus, for every
old output including those above n and every coefficient of either sign,

    |c_m(Y)|=|c_m(X)|*m^(-(sigma(Y)-sigma(X)))<=|c_m(X)|.

L499 therefore implies sum_(m>=2)|c_m(Y)|h(m)<=1-r0.
Its literal resultant expansion has m=1 term exp(i*Theta_hat), of
modulus one. Each other term, putting u=log(m)/ell>=0, has modulus
at most |c_m(Y)|*(|1-u|+u). As |1-u|+u=max(1,2u-1)<=h(m),

    |G_tilde_n(Y)|>=r0.                                  (1)

This is a finite coefficient argument. It does not extend C499a's
half-open noncollision conclusion by continuity or use the n remainder
at Y. No fall credit is taken.

### 2. Exact factored implementation of the complete increment

At Y put z=(1+iY)/2, nu=sigma+i*eta, E=product_p(1-A_p),
A_p=b_p*p^(-nu), J=sum_p log(p)*A_p/(1-A_p), rho=|E|, and

    DeltaS=sum_(n<j<=N) b_j*j^(-nu),
    DeltaL=sum_(n<j<=N) b_j*j^(-nu)*log j.

Formal differentiation of the finite Euler polynomial in nu gives
dE/dnu=E*J. Its logarithmically weighted expansion is consequently
Elog=-E*J: each squarefree coefficient is
mu(d)*product_(p|d)b_p, multiplied by log d. Finite distributivity
now gives, with the exact product of PRIME heat weights,

    DeltaShat=E*DeltaS,
    DeltaLhat=E*DeltaL+Elog*DeltaS=E*(DeltaL-J*DeltaS).       (2)

All squarefree d and all 256 j occur, including overlaps and outputs
beyond previous cutoffs. No b_d replaces product b_p. No infinite
interchange or output truncation occurs.

Writing v=exp(i*Theta) and E=rho*exp(i*psi), one has
exp(i*Theta_hat)*E=rho*v, independently of argument choices modulo
2*pi. Therefore the EXACT increments are

    DeltaZ=rho*v*DeltaS,
    DeltaW=rho*v*(DeltaL-J*DeltaS),
    DeltaG=DeltaZ-DeltaW/ell+conj(DeltaW)/ell.              (3)

The certificate encloses (3) before taking modulus. It separately
computes Elog by the product-rule recurrence
Elog_new=Elog_old*(1-A_p)-E_old*log(p)*A_p and evaluates (2) with
exp(i*Theta_hat)=v*conj(E)/rho. The two enclosures agree. This is a
consistency check, not an independent proof audit.

### 3. Branch-safe phase and phase-derivative evaluation

Define a=arg z=pi/2-atan(1/Y), Lstar=log(1+Y^2)/2-log(4*pi).
Direct substitution into L494's alpha and M_t gives

    Re alpha=Lstar/2-1/(1+Y^2),
    Im alpha=a/2-3Y/(1+Y^2),
    sigma=1/2+(t/2)Re alpha, eta=Y/2+(t/2)Im alpha,
    Theta=pi-a/4+(Y/4)*(Lstar-1)
                     +(t/2)*Re alpha*Im alpha  (mod 2*pi). (4)

To verify the last identity, arg(z-1)=pi-a and
Im[(z/2-1/2)Log(z/2)]=-a/4+(Y/4)log(|z|/2).
The other exponential terms in M_0 contribute
-(Y/4)log pi-Y/4; its positive real prefactor contributes no phase.
Finally Im(t*alpha^2/4)=(t/2)Re alpha*Im alpha. Thus (4) computes
the unit phase of the literal M_t, without evaluating a tiny modulus
or selecting the branch of the argument of a rounded complex number.

L495's exact derivative identities give, at this same Y,

    Q=Y*(Y^2+5)/(1+Y^2)^2, C=(7Y^2-5)/(1+Y^2)^2,
    alpha'=C-iQ, nu'=tQ/4+i*(1/2+tC/4),
    ell=2*Re(alpha+(t/2)*alpha*alpha')-4*Im(nu'*J).        (5)

The resulting interval for ell is contained in (27.7359997688,
27.7359997689), strictly above ell0. It is not replaced by the base
logarithm or an arbitrary phase. All elementary inputs use exact sigma.

### 4. Separate full-support charge and absolute-channel envelopes

Let w_j=b_j*j^(-sigma(Y)), A_B=sum_(n<j<=N) w_j,
S_B=log N+sum_p log p, and

    K_B=R0*(53/3+A_B)*S_B.

Old primitive weights at Y decrease from X. L499 bounds their sum by
53/3. Every NEW output has log(d*j)<=S_B. Expanding all channels
positively gives |Lhat_N(Y)|<=K_B. The zero logarithm at d=j=1
causes no exception. This support and primitive envelope are enlarged
from the old model, independently of the small oscillatory increment.

Also rho<=R0 and |E'|<=R0*c*J0=D0, since each radius decreases
from X and |1-A_p|>=1-|A_p|>0. The same positive envelopes used
in L499 apply. The rational functions Q(x),C(x) of (5) are positive
and decreasing for x>=2: their derivative numerators are respectively
5-12x^2-x^4 and 2x*(17-7x^2), over (1+x^2)^3.
Hence both L495 charges are bounded above by

    U_s,B=t*(Q(X)+C(X))*K_B/ell0,
    U_r,B=R0*epsilon/2
                +2*(D0*epsilon+R0*epsilon_1)/ell0.        (6)

Both saddle corrections, the complex product derivative, rho, and the
full unmollified entering-pair Cauchy allowance are retained.

For comparison, triangle inequality on EACH channel of the resultant
increment bounds it by sum_j w_j sum_d r_d(Y)*h(d*j). For s>=0,
max(1,2s/ell0-1)<=1+2s/ell0. Finite positive product identities give

    sum_d r_d(Y)<=R0,
    sum_d r_d(Y)*log d
       =product_p(1+r_p(Y))*sum_p log(p)*r_p(Y)/(1+r_p(Y))
       <=R0*J0.

The final inequality follows by monotonicity of r/(1+r) and
r/(1+r)<=r/(1-r), using the anchor definition of J0. Thus a COMPLETE
absolute-channel envelope is

    A_abs=R0*sum_(n<j<=N) w_j*(1+2*(log j+J0)/ell0).      (7)

Replacing J0 by sum_p log p gives the coarser maximum-support bound.
Neither (7) nor the latter is the exact absolute norm; the comparisons
in the conclusion are precisely to these conservative envelopes.

### 5. Rational elementary certificate and its limits

Reproduce from the active notebook with

    python3 scripts/heat/phase-sensitive-256-block-certificate.py

The complete certificate is
`scripts/heat/phase-sensitive-256-block-certificate.json`.
Python's standard-library Fraction and unbounded integers are used;
python-flint is not installed and no floating-point numerical library
is used. The retained L499 elementary/corner certificate is matched
by SHA-256 to its independent audit, and every audited input hash is
checked. These are reused audited inputs, not newly proved by PASS flags.
The exact inherited parameter dictionary and r0 are checked.

All rational operations round outward to grid 10^(-60). Addition,
all four endpoint products, and reciprocal endpoint reversal preserve
inclusion; every division excludes zero. A square uses lower endpoint
zero when its input crosses zero. For nonnegative endpoints l,u,
integer square roots of floor(l*10^120), floor(u*10^120), with one
added to the upper integer, give an outward square-root enclosure.

Logs use a=2^k*v, 1<=v<2, and the positive atanh series
log v=2*sum_(j>=0) z^(2j+1)/(2j+1), z=(v-1)/(v+1).
After 100 terms its remaining positive tail is at most
2*z^201/(201*(1-z^2)). Log 2 uses the same formula with v=2.
Endpoint monotonicity handles interval arguments. Exponentials use
positive Taylor terms through degree 180 at the absolute argument u;
the tail is at most upper_term_180*(u/181)/(1-u/182).
All u<182 are checked; negative arguments invert positive endpoints.
These are the elementary enclosures already used in C499b, newly
evaluated for this block. Every evaluation and tail is stored.

For atan(1/Y), 0<u=1/Y<1, the alternating series gives
u-u^3/3<=atan u<=u. For every sine/cosine evaluation the program
chooses any integer k by rational midpoint arithmetic, then encloses
r=phase-2*k*pi and verifies |r|<=4. No claim that k is a uniquely
correct nearest integer is needed: periodicity holds for every integer.
It evaluates the real Taylor polynomials through degree 159 and adds
the symmetric Lagrange remainder |r|^160/160! for each. The derivative
of every order has magnitude at most one on the real segment.
This supplies an explicit remainder for the series in
[DLMF 4.19.1–2](https://dlmf.nist.gov/4.19). Large-argument uncertainty
is kept in r; no floating-point phase reduction is used. Every resulting
unit-phase squared-modulus interval is checked to contain one.

The 400 producer checks pass with no failures. All 63 prime rows,
256 primitive rows, 320 unit-phase evaluations, closed-domain tests,
actual ell, product-rule consistency, charge envelopes, threshold and
precision-width test are stored in full. Directed summaries include

    B_G < 5.091337212137412982549464e-8,
    U_s,B < 1.254886140805040147918351e-11,
    U_r,B < .000020830477230728159125102344,
    B_G+U_s,B+U_r,B < .000020881403151710941305329318,
    r0 > .00042249381587054327798642829,
    margin > .00040161241271883233668109897.

The cost interval width is below 10^(-30); no precision refinement was
needed. Complete rational endpoints for the actual ell, both coordinates
and modulus of DeltaG, and combined cost were inspected with the local
JSON inspector. These are the original producer's finite-specialization
computations; the independent review is recorded below, not an audit of
the imported manuscripts.

Finally (1) and (3) imply |G_tilde_N(Y)|>=r0-B_G.
If H_t(Y)=H_t'(Y)=0, L495 and (6) give
|G_tilde_N(Y)|<=U_s,B+U_r,B<r0-B_G, a contradiction.
No all-height, all-time, intermediate-cell or zero-time conclusion follows.

### 6. Independent conceptual and complete arithmetic audit, 2026-11-01

The pre-existing SPECIALIZE assessment
`drafts/literature/2026-11-01-c499c-independent-audit-coverage.md`
covers precisely this audit. The result is accepted without a mathematical
repair. This verifies a known-method finite specialization, not progress
beyond the checked source method or a new uniform transport theorem.

**Normalization and branch.** For Y>0 the literal z and z-1 lie in the
first and second quadrants. Their principal arguments are a and pi-a,
so the product z(z-1) has unit phase -1. Since

    z/2-1/2=-1/4+iY/4,
    Log(z/2)=log(|z|/2)+ia,

the imaginary part of their product is exactly the expression used in
(4). The factor pi^(-z/2) contributes -Y*log(pi)/4, and exp(-z/2)
contributes -Y/4. The heat factor contributes
t*Re(alpha)*Im(alpha)/2. This proves the claimed phase modulo 2*pi
directly from M_t, including every nonconstant factor. Separately,
1/(2z)=(1-iY)/(1+Y^2) and 1/(z-1)=(-2-2iY)/(1+Y^2), which give
both components of alpha in (4). The rational complex derivative in
L495 gives C-iQ, so (5) uses the derivative with respect to x after
z'=i/2, with its correct sign. The Euler contribution to ell is
-4*Im(nu'*J), not a modulus derivative or an unmollified phase.

For each of the 320 phases, the consumer reconstructs the exact signed
integer k and the interval phase-2*k*pi from the accepted enclosing pi
interval. It checks |r|<=4. Any integer is valid by periodicity; closeness
to a rounded principal argument is not assumed. The two polynomials
are the degree-159 Taylor polynomials (the cosine coefficient in degree
159 is zero). Taylor's real Lagrange theorem gives |r|^160/160! for
each remainder, since every real sine/cosine derivative has modulus at
most one. Their interval evaluations retain the phase uncertainty.
The unit-modulus containment check is only an additional consistency
test; the reconstructed input phase and Taylor enclosure establish the
correct unit phase.

**Finite algebra and old bound.** Differentiating each finite Euler
factor with respect to nu gives +log(p)*A_p, hence dE/dnu=E*J.
Differentiating its expanded finite polynomial gives minus its
logarithmically weighted polynomial. Thus Elog=-E*J and (2) include
every squarefree product with the product of the prime heat weights.
Coincident outputs combine by distributivity, without being discarded.
Nonvanishing E justifies exp(i*Theta_hat)=v*conj(E)/rho, proving (3)
with the same actual ell in both resultants. The second product-rule
evaluation tests arithmetic consistency only; this algebra supplies
the conceptual justification independently.

At fixed t and old n, beta_m is independent of x for every output.
The strictly positive sigma' damps |beta_m|m^(-sigma) even when
beta_m is negative or m>n. L499's full signed mass therefore bounds
the mass at Y. The m=1 term is exactly a unit complex number, and
|1-u|+u=max(1,2u-1) is nondecreasing for u>=0. Together with
ell>ell0>0 this proves (1). It is not an extrapolation of a half-open
noncollision statement. The symbolic equality defining Y fixes the
new cutoff N exactly; interval rounding never decides its floor.

**Domain and charges.** The reconstructed domain test certifies
Y>X and t*(log(X/(4*pi))+(Y-X)/X)<5.17. The elementary inequality
log(y)<=y-1 for y>0 therefore places the whole closed [X,Y] in
L494/L496's domain. Their full epsilon_1 is used with the new frozen
index N. Its separate entering-pair allowance is retained even though
the finite oscillatory increment is small. Every new logarithmic
output is bounded by log N+sum_p log p. Positive full-support expansion
and the old primitive cap 53/3 justify K_B. Decreasing prime radii
bound rho and |E'| by R0 and D0, respectively. Direct differentiation
of Q,C gives the numerators stated above, negative for x>=2; both
functions are positive there. Thus both replacements by their values
at X have the upper-bound direction needed in (6). No small bound for
DeltaG is substituted for the absolute logarithmic norm in either charge.
The same positivity and r/(1+r)<=r/(1-r) justify (7), which remains
an envelope rather than an exact absolute norm.

**Complete independent consumption.** Reproduce with

    python3 scripts/heat/c499c-certificate-audit.py

The consumer imports or executes no producer routines. It implements
real endpoint pairs with exact Fraction arithmetic, all four endpoint
products, reciprocal endpoint reversal and explicit floor/ceiling on
the 10^60 grid. It checks every reciprocal avoids zero and every computed
square-root endpoint satisfies its defining squared inequalities.
Every decoded rational denominator is positive and every decoded interval
is ordered. No floating-point mathematical data are accepted.

The elementary identities are the inspected
[DLMF 4.6.4](https://dlmf.nist.gov/4.6.E4), restricted to positive
arguments, [4.2.19](https://dlmf.nist.gov/4.2.E19) for the entire
exponential, [4.24.3](https://dlmf.nist.gov/4.24.E3) for arctangent
at real 0<1/Y<1, and [4.19.1–2](https://dlmf.nist.gov/4.19) for
sine/cosine. The logarithm's omitted positive terms are bounded by
replacing every denominator by 201 and summing their geometric powers.
For exp(u), the first omitted term is term_180*u/181 and the ratios
of all subsequent terms are at most u/182<1. These give exactly the
tails in Section 5; negative exponents use monotone reciprocal endpoints.
The arctangent alternating bounds and dyadic logarithm reduction retain
their domain conditions. None of these identities alone certifies the
rounded arithmetic; the consumer rebuilds each enclosure and tail.

An independent Eratosthenes sieve verifies all 63 ordered primes. The
consumer reconstructs all 256 consecutive primitive rows, all 261 log
records, all 638 exponential records and all 320 phase records, including
every stored field, parameter and reduced phase. It rebuilds both complex
coordinates and moduli, the products and logarithmic recurrence, actual
ell, complete support, both charges and every field of all 400 producer
assertions, testing their predicates before comparing their flags.
Current producer/input hashes match; the accepted L499 corner and its
complete input linkage are unchanged. L499's audited scalar/mass inputs
are reused, without rerunning its expensive signed convolution or treating
stored PASS flags as mathematical proofs.

The complete evidence is `scripts/heat/c499c-certificate-audit.json`:
2366 independent checks, zero failures, all reconstruction/comparison
records and current hashes. Exact reconstructed DeltaG coordinates and
modulus, ell, total cost, margin and empty failure list were also inspected
in full. In particular,

    B_G < 5.09133721213741298254946346e-8,
    U_s,B < 1.25488614080504014791835073e-11,
    U_r,B < .0000208304772307281591251023432,
    B_G+U_s,B+U_r,B < .0000208814031517109413053293171,
    r0-B_G-U_s,B-U_r,B > .000401612412718832336681098978.

These strict comparisons validate the final contradiction at the single
endpoint under the retained analytic imports. Manuscript proof audits,
uniform control between cells, other times, H1, zero time and RH remain
unresolved. No hypothesis, direct input or DAG edge changes in this audit.

## Mathlib

Full matching coverage was not checked and remains unknown. Supporting
mathematics is finite product differentiation/distributivity, complex
modulus and triangle inequalities, real Taylor remainder estimates,
and elementary interval arithmetic. No particular Mathlib theorem is
claimed to formalize the imported heat approximation, actual-phase
certificate or this endpoint conclusion. Unknown coverage is not absence.
