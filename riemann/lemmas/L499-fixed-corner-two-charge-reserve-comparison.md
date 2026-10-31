# L499 — Fixed-corner reserve pays both resultant charges

## Hypotheses

Use the exact frozen-cutoff definitions of L494–L498 at

    t=.16836, x=6000284561421.5, N=691004,
    P={primes p<=307}, ell0=24.18022820120389,
    sigma=.5+(t/4)*log(sqrt(1+x*x)/(4*pi))-t/(2*(1+x*x)).

Every finite decimal is an exact rational. Set

    L=log(x/(4*pi)), w_q=exp(t*log(q)^2/4)*q^(-sigma),
    r_p=w_p, R_+=product_(p in P)(1+r_p),
    J_+=sum_(p in P) log(p)*r_p/(1-r_p), c=.500000000001,
    epsilon=6e-7, epsilon_1=((6e-7+1.3e-6)*8.770232)/.14142.

The purely finite bounds use the completed L496 elementary-input audit
and L497/L498 mass audit. For interpretation as a statement about H_t,
retain L494's imported Polymath Theorem 1.3 normalization and saddle
estimates, L495's resultant identities and L496's imported Planat v2
Lemma 6.3 base-phase theorem. Those manuscript proofs remain unaudited.
In particular the interpretation uses ell=4*Theta_hat'>ell0 and
|nu'|<c, with every derivative spatial at fixed t,N, including cutoff
equality. No transport or source numerical ledger is assumed.

## Conclusion

The sum of upper bounds for both L495 charges is strictly smaller
than the audited reserve:

    (4/ell)(|sigma'|+|eta'-1/2|)*|L_hat|
       +rho*epsilon/2
       +(2/ell)(|E_prod'|*epsilon+rho*epsilon_1)
      < .000020830490
      < r0,

    r0=14176540015048665224252705167939023
        /33554432000000000000000000000000000000
      >.00042249.

The remaining reserve exceeds .00040166. Under the retained analytic
inputs, H_t(x) and its spatial derivative cannot both vanish at this
one corner. A zero there, if present, is simple. This does not exclude
collisions on a neighbourhood, at other times or heights, or at zero
time, and does not prove actual-Xi all-degree positivity or RH.

This is a local numerical reproduction of Michel Planat, *Collective
Contraction in the de Bruijn–Newman Heat Flow: Off-Zero Logarithmic
Derivatives and Certified Barrier Refinements*,
[arXiv:2609.37164v2, 7 October 2026, Section 6.6, equations (40)–(43),
Proposition 6.8, and Section 6.7, equation (44), Lemma 6.10/(45) and
the subsequent logarithmic-moment envelope](https://arxiv.org/html/2609.37164v2#S6.SS7).
The source already reports a stronger comparison with transport charges.
No advance beyond that known method, certification of its transport
ledger, or manuscript-level validation is claimed. The separate local
critical audit below accepts this specialization and its complete scalar
certificate, retaining the analytic source qualifications.

## Proof

### 1. Positive-channel estimates with the full output support

L496's audited interval inputs verify every prime radius r_p<1 and
give the exact sigma, not its rounded decimal. At this corner the
certificate below also checks

    4*pi*N^2<x,
    sigma-t*L/8>53/50.

Hence log q<=log N<L/2 for 1<=q<=N, and

    w_q=exp(-(sigma-t*log(q)/4)*log q)<=q^(-53/50).

The positive decreasing function u^(-53/50) satisfies
q^(-53/50)<=integral_(q-1)^q u^(-53/50)du for q>=2. Therefore

    A=sum_(q=1)^N w_q
      <=1+integral_1^N u^(-53/50)du
      <=1+integral_1^infinity u^(-53/50)du=53/3<20.       (1)

This is the fixed-corner specialization of the source's power-sum
integral envelope, with a convenient rational exponent. Its short
derivation specifies the changed exponent and justifies using the
infinite positive integral, rather than importing a source decimal.

For each squarefree d supported on P set r_d=product_(p|d)r_p.
The coefficient formula in L497 gives

    c_m=beta_m*m^(-sigma)
       =sum_(d*q=m, q<=N) mu(d)*r_d*w_q.

Every possible output has log m<=log N+sum_p log p<S, where
S=L/2+sum_p log p. Triangle inequality, finite distributivity and
the complete squarefree Euler expansion give

    |L_hat|<=sum_m |c_m|*log m
            <=sum_d r_d*sum_(q<=N) w_q*log(d*q)
            <=R_+*(53/3)*S=:K.                           (2)

All 2^63 channels are covered by the finite identity
sum_d r_d=product_p(1+r_p); none is discarded because its output
exceeds N, 160N or exp(ell0). The m=1 logarithm is zero and causes
no exceptional term. No oscillatory cancellation is assumed.

For the actual complex Euler factors, |1-A_p|<=1+r_p gives
rho<=R_+. From L495 (10),

    |E_prod'|=rho*|nu'*J|
      <=R_+*c*sum_p log(p)*r_p/(1-r_p)=:D.                (3)

Here |1-A_p|>=1-r_p>0 justifies every denominator. The product
derivative and the modulus derivative are not identified; (3) bounds
the former, which is sufficient for L495 (3). Phases need not be
computed or sampled.

### 2. Both saddle corrections and both charges

L495 (9) supplies the exact rational identities

    Q_alpha=x*(x^2+5)/(1+x^2)^2>0,
    C_alpha=(7*x^2-5)/(1+x^2)^2>0,
    sigma'=t*Q_alpha/4>0,
    eta'-1/2=t*C_alpha/4>0.

Both corrections are retained. Since ell>ell0>0, all factors on
the right are nonnegative, and L495 (2)–(3) are bounded above by

    U_s=4*(t*Q_alpha/4+t*C_alpha/4)*K/ell0,
    U_r=R_+*epsilon/2+2*(D*epsilon+R_+*epsilon_1)/ell0.    (4)

In particular epsilon_1 is L494's full frozen-index Cauchy bound;
it is not a derivative of a scalar error or a shortened source charge.
Substitution of ell0 occurs only in positive denominators, so its
direction is valid for both charges.

### 3. Exact scalar evidence

Reproduce from the notebook with

    python3 scripts/heat/fixed-corner-two-charge.py

The complete certificate is `scripts/heat/fixed-corner-two-charge.json`.
It consumes every one of the 63 audited L496 prime rows, checks the
prime list by integer trial division through isqrt(p), and records
each logarithm, radius, positive denominator and J_+ summand. The
source SHA-256 must equal the source hash retained by the completed
L496 independent audit. It uses those already audited elementary
intervals without another transcendental evaluation or phase assertion.
Its finite arithmetic also checks the exact cutoff inequalities
N^2<=x/(4*pi)+t/16<(N+1)^2 and t*L<5.17. Thus L494's closed-domain
and L496's phase interfaces apply at the stated corner.

The new arithmetic uses Fraction endpoints on the rational grid
1/10^50. Addition and subtraction use endpoint addition and subtraction;
products use all four endpoint products. Mathematical integer floor
rounds each lower endpoint downward, and ceiling rounds each upper
endpoint upward. Reciprocals reverse the endpoints after checking that
the denominator interval avoids zero. All quantities here divided by
intervals have positive denominators. Exact input endpoints are retained
until their first arithmetic operation; subsequent outward rounding
preserves inclusion. Python integers do not overflow. Correlated inputs
are enclosed independently, increasing bounds rather than assuming
independence. No floating-point comparison enters any proof bound.

The 153 checks pass with no failures. Directed decimal summaries are

    R_+ < 2.06660258608259507995960,
    J_+ < 1.35578778137848033654031,
    K   < 10814.1740658517837477489 < 23000,
    D   < 1.40093726759077762876295,
    U_s < 1.25487373797593299173727e-11,
    U_r < .0000208304772307281591251024,
    U_s+U_r < .0000208304897794655388844323
             < .000020830490.

These displayed upper decimals round upward; the complete rational
endpoints and all actual/required comparisons are in the certificate.
The mass audit's prefix, complement, sum and reserve fields are checked
against the exact fractions

    prefix_upper=.698591427320603743332620581311,
    complement_upper=21688332681815698/72057594037927936,
    r0=1-prefix_upper-complement_upper.

Their difference is strictly positive; the certificate encloses
r0-U_s-U_r with lower endpoint greater than
.000401663326091077739101996>.00040166. Source final decimals are
not used in this comparison. The retained source audits are mathematical
inputs, not newly rerun or established by their stored PASS labels.
The new script checks their linkage and arithmetic application; its
own execution is not an independent critical audit.

### 4. Why this reserve is the relevant lower bound

It remains to connect the coefficient budget to the precise G_tilde
in L495, rather than infer noncollision from mass<1 alone. Write
theta=Theta_hat. With real beta_m and nu=sigma+i*eta, its defining
formula gives

    G_tilde=sum_m c_m*[exp(i*theta-i*eta*log m)*(1-log(m)/ell)
                    +exp(-i*theta+i*eta*log m)*log(m)/ell].

The m=1 coefficient is c_1=1, so that term is exp(i*theta) and
has modulus one. For every m>=2 put u=log(m)/ell>=0. Then

    |1-u|+u=max(1,2u-1)
       <=max(1,2*log(m)/ell0-1)=h_ell0(m).

The equality follows by the cases u<=1 and u>=1; the inequality
uses ell>=ell0>0. Triangle inequality and the full finite mass bound
from L497/L498 therefore prove

    |G_tilde|>=1-sum_(m>=2)|c_m|*h_ell0(m)>=r0.           (5)

If H_t=H_t'=0, L495 (2) and (3), with the Cauchy bounds of L494,
give |G_tilde|<=|G_tilde-G_star|+|G_star|<=U_s+U_r<r0,
contradicting (5). This proves precisely the stated pointwise,
qualified conclusion. The computation provides no transport budget,
interval exclusion, H1, other-time or zero-time control. The original
energy, inverse-gap, contraction and approval-loop stops are neither
reopened nor treated as a global ban.

### 5. Separate local critical audit, 2026-10-30

The audit used the pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-30-l499-critical-audit-coverage.md` and the
already inspected source statements/proof cases. It accepts the fixed
corner and stated constants without repair. This is verification of a
known-method local reproduction, not progress beyond the cited source.

**Proof and hypotheses.** L494's closed domain contains this exact t,x;
the complete rational cutoff tests give N=691004. Its spatial Cauchy
bound is used at fixed t,N, with the full epsilon_1 in (4). L496's
audited elementary inputs use precisely the sigma in the hypotheses;
the actual-phase interpretation still imports its base-phase theorem.
The prime radii, derivative cap and phase floor are not inferred from
the new producer's flags. The prior completed L496 and L497/L498 audits
are retained mathematical inputs, not rerun manuscript proofs.

For (1), t>0, log(q)<L/2 and sigma-t*L/8>53/50 give the required
direction of the exponent comparison, including q=1. The decreasing
power integral and its infinite positive tail justify 53/3. The
coefficient formula includes every squarefree divisor and every q<=N;
finite distributivity covers the complete output support in (2), not
just the mass ledger's initial edge. In (3), |1-A_p|>=1-r_p>0
justifies the reciprocal and the complex product derivative bound.
L495 (9) has both positive saddle corrections. All right sides in
(4) are nonnegative, so ell>ell0 gives upper bounds in the stated
direction. No phase was sampled or Euler modulus differentiated as
though it were the complex product.

For (5), expanding L495's literal G_tilde gives exactly the two terms
displayed in Section 4. The real coefficients permit conjugation term
by term. Only d=q=1 contributes to c_1, which equals one, and its
logarithmic term vanishes. When 0<=u<=1, |1-u|+u=1; when u>=1 it
equals 2u-1, agreeing at u=1. Monotonicity of this maximum and
ell>ell0>0 give precisely h_ell0, including outputs beyond exp(ell0).
Thus the full audited mass upper bound gives |G_tilde|>=r0. At a
true double zero, L495 (2)-(3) supply the opposite upper bound with
the same normalization and frozen derivative. No mass lower bound,
neighbourhood assertion or assumption of simplicity enters this step.

**Complete independent scalar consumption.** Reproduce by

    python3 scripts/heat/l499-certificate-audit.py

The new consumer imports or executes no producer routines. It uses
rational endpoint pairs, all four products, reciprocal endpoint reversal,
and explicit mathematical floor/ceiling on integer grids. For a grid
Q, rounding a rational a downward is floor(Q*a)/Q and upward is
-floor(-Q*a)/Q; these preserve interval inclusion also for negative
operands. Every reciprocal interval is checked to avoid zero; the
present application has positive divisors. Python integers do not
overflow. Mathematical comparisons never use floating-point values.

On the original 10^50 grid it reconstructs every field of every one
of the 63 prime rows, all 16 scalar fields and all 153 actual/required
comparison records, with exact equality. It checks the exact parameters,
all elementary input entries, all input hashes and producer hash. An
independent Eratosthenes sieve verifies the complete ordered prime set.
Reconstruction checks every comparison's predicate before comparing its
stored flag. A separately evaluated 10^90-grid replay traverses the
primes in reverse order; every resulting row/scalar interval lies
inside the producer's corresponding interval, and all strict inequalities
hold again. The finer run reuses the audited transcendental enclosures;
it is not a fresh transcendental or signed-coefficient replay.

The full evidence is `scripts/heat/l499-certificate-audit.json`: 582
audit checks, zero failures, both complete sets of comparisons, finer
prime rows and bounds, exact provenance hashes and qualifications.
Directed finer-grid summaries are

    U_s+U_r < .000020830489779465538884432261,
    r0 > .00042249381587054327798642829,
    r0-U_s-U_r > .00040166332609107773910199603 > .00040166.

The exact rational charge and margin endpoints were also inspected in
full. This accepts the strict pointwise comparison and its local
resultant connection. Saddle/base-phase manuscript proofs, transport,
H1, other collisions and times, zero time and RH remain unresolved.

## Mathlib

Full matching coverage was not checked and remains unknown. Supporting
mathematics comprises finite Euler expansion and triangle inequalities,
elementary differentiation/integration of real powers, and exact integer
interval arithmetic. No Lean formalization of the heat approximation,
source base-phase theorem, numerical certificate or pointwise resultant
conclusion is claimed. Unknown coverage is not evidence of absence.
