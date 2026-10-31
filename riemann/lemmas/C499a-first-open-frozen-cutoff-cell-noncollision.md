# C499a — Two-charge reserve on the first open frozen-cutoff cell

## Hypotheses

Use the exact H_t, finite model, remainder and normalization of L494,
the resultant definitions of L495, and the phase floor of L496. Fix

    t=.16836, X=6000284561421.5, N=691004,
    Y=4*pi*((N+1)^2-t/16), X<=x<Y,
    P={primes p<=307}, ell0=24.18022820120389,
    sigma(x)=.5+(t/4)*log(sqrt(1+x*x)/(4*pi))-t/(2*(1+x*x)).

All finite decimals are exact rationals. Derivatives are spatial at
fixed t,N. In the notation of L495 put

    b_q=exp(t*log(q)^2/4),
    beta_m=sum_(d|m, d squarefree over P, 1<=m/d<=N)
                mu(d)*(product_(p|d)b_p)*b_(m/d),
    c_m(x)=beta_m*m^(-sigma(x)),
    h(m)=max(1,2*log(m)/ell0-1),
    w_q(x)=b_q*q^(-sigma(x)), r_p(x)=w_p(x),
    epsilon=6e-7, epsilon_1=((6e-7+1.3e-6)*8.770232)/.14142,
    c=.500000000001.

For the actual H_t interpretation retain L494's imported Polymath
Theorem 1.3 normalization and saddle estimates, and L496's imported
Planat v2 Lemma 6.3 base-phase theorem. Their manuscript proofs remain
unaudited. The completed local L496, L497/L498 and L499 audits are
retained inputs; this corollary does not rerun their coefficient or
elementary-function certificates. In particular the finite mass statement
below is distinct from its qualified interpretation for H_t.

## Conclusion

On the whole stated half-open interval the cutoff is N=691004 and
the complete weighted coefficient mass obeys

    sum_(m>=2) |c_m(x)|*h(m) <= 1-r0,
    r0=14176540015048665224252705167939023
        /33554432000000000000000000000000000000 > .00042249.

Both L495 charges together have a uniform upper bound

    (4/ell)(|sigma'|+|eta'-1/2|)*|L_hat|
      +rho*epsilon/2
      +(2/ell)(|E_prod'|*epsilon+rho*epsilon_1)
      < .000020830490 < r0,

where ell=4*Theta_hat'>ell0. The remaining reserve exceeds .00040166.
Consequently, under the retained analytic inputs, no x in [X,Y) has
H_t(x)=H_t'(x)=0. A zero in this interval, if present, is simple.

This specializes the known fixed-t,N spatial mechanism in Michel
Planat, *Collective Contraction in the de Bruijn–Newman Heat Flow:
Off-Zero Logarithmic Derivatives and Certified Barrier Refinements*,
[arXiv:2609.37164v2, 7 October 2026, Section 6.6, (40)–(41),
Proposition 6.8 and the first-partial-cutoff paragraph after (43)](https://arxiv.org/html/2609.37164v2#S6.SS6),
with [Section 6.7, (44), Lemma 6.10/(45), the full-support moment
envelope and frozen-cutoff Cauchy proof](https://arxiv.org/html/2609.37164v2#S6.SS7).
The source already gives this spatial mechanism and stronger conditional
transport statements. The local difference is to use the audited exact
sigma, constant ell0 and L499 corner envelopes on this precisely bounded
cell. The proof below checks those applicability obligations; no new
mechanism or progress beyond the inspected source method is claimed.

The right endpoint Y is excluded. No entering jump, full-cell fall
credit or multi-cell source ledger is used. This result leaves other
cells/times, H1, zero time and actual-Xi all-degree positivity unresolved.
The separate critical audit in Section 6 accepts the interval proof and
complete scalar certificate with these qualifications. This is not a
complete RH candidate.

## Proof

### 1. Exact cell and uniform analytic domain

L499 verifies, with the exact parameters above,

    N^2<=X/(4*pi)+t/16<(N+1)^2, 4*pi*N^2<X.

The endpoint certificate described in Section 5 verifies X<Y. Since
x/(4*pi)+t/16 is strictly increasing, for every X<=x<Y it lies in
[N^2,(N+1)^2). The square root is nonnegative, so its floor is N.
At x=Y it equals (N+1)^2, giving cutoff N+1. Thus the endpoint cannot
be included by this fixed-N argument.

Write L_X=log(X/(4*pi)). For X<=x<=Y, monotonicity and
log(1+u)<=u for u>=0 give

    log(x/(4*pi))<=L_X+log(Y/X)<=L_X+(Y-X)/X.

The scalar certificate encloses pi and L_X using L499's audited input
intervals and obtains

    6000290041249.8045187868265 < Y
                               < 6000290041249.8045187868266,
    5479828.3045187868265380786 < Y-X
                              < 5479828.3045187868265380787,
    t*(L_X+(Y-X)/X) < 4.5275042354580522005720508 < 5.17.

Hence every centre of [X,Y) satisfies L494's and L496's closed domain,
including x=X. L496 supplies r_p(x)<1, |nu'(x)|<c and ell(x)>ell0.
L494 supplies the same epsilon and epsilon_1 at every centre. Its
fixed-index Cauchy disk may cross the upper cutoff when x is near Y;
the full (epsilon+1.3e-6)*8.770232/.14142 bound is retained. Staying
inside the cell at the centre does not permit dropping that disk charge.

### 2. Full-support damping with a fixed weight

The exact sigma derivative in L496 is

    sigma'(x)=t*x*(x*x+5)/(4*(1+x*x)^2)>0.

All beta_m depend only on the now fixed t,N,P, and the support is
contained in the finite set of outputs m=dq with q<=N and d squarefree
over P. Thus, putting Delta=sigma(x)-sigma(X)>=0,

    c_m(x)=c_m(X)*m^(-Delta),
    |c_m(x)|*h(m)<=|c_m(X)|*h(m)   (m>=2).

This equality also holds when a signed grouped coefficient vanishes;
no coefficientwise positivity hypothesis is required. The function h
is positive and independent of x. Summing over the entire finite support
and using the completed L497/L498 mass bound, as assembled in L499,
proves

    M(x):=sum_(m>=2)|c_m(x)|*h(m)<=M(X)<=1-r0.             (1)

Outputs above N, 160N and exp(ell0) remain included. The mass is not
replaced by a prefix, nor is a varying separator weight substituted for
h. There is no infinite-limit interchange.

### 3. Uniform positive envelopes for the two charges

Use the following constants, all evaluated at the anchor X:

    R0=product_p(1+r_p(X)),
    J0=sum_p log(p)*r_p(X)/(1-r_p(X)),
    S0=L_X/2+sum_p log p,
    K0=R0*(53/3)*S0, D0=R0*c*J0.

These are precisely L499's audited constants. At fixed t,
w_q(x)=w_q(X)*q^(-Delta)<=w_q(X), including q=1, and similarly
r_p(x)<=r_p(X)<1. L499 proves sum_(q<=N)w_q(X)<=53/3.
Every output has

    log(dq)<=log N+sum_p log p<S0,

using 4*pi*N^2<X. In particular S0 is a constant frozen at X;
no growing L(x)/2 is inserted. Finite triangle inequality and the
complete positive squarefree expansion therefore give

    |L_hat(x)|
      <=sum_d product_(p|d)r_p(x)*sum_(q<=N)w_q(x)*log(dq)
      <=R0*(53/3)*S0=K0.                                 (2)

All squarefree channels are included, even when their products exceed
the mass certificate's explicit edge. The m=1 term has zero logarithm.
Likewise |1-A_p(x)|<=1+r_p(x) gives rho(x)<=R0. Since r/(1-r)
is increasing for 0<=r<1 and |1-A_p|>=1-r_p>0, L495's exact
product derivative formula gives

    |E_prod'(x)|
      <=rho(x)*|nu'(x)|*sum_p log(p)*r_p(x)/(1-r_p(x))
      <=R0*c*J0=D0.                                      (3)

Equations (2) and (3) are positive envelopes. They make no assertion
that the oscillatory |L_hat|, rho or |E_prod'| itself decreases.

Both exact corrections in L495 are positive here:

    sigma'=t*Q(x)/4, eta'-1/2=t*C(x)/4,
    Q(x)=x*(x*x+5)/(1+x*x)^2,
    C(x)=(7*x*x-5)/(1+x*x)^2.

Differentiating these rational functions gives

    Q'(x)=(5-12*x*x-x^4)/(1+x*x)^3<0,
    C'(x)=2*x*(17-7*x*x)/(1+x*x)^3<0   (x>=2).

For x>=2 both denominators are positive, Q,C>0, the first numerator
is at most 5-48-16<0 and the second has 17-7*x*x<=17-28<0.
Thus Q(x)<=Q(X) and C(x)<=C(X) throughout the cell. Combining
these inequalities with (2), (3), rho<=R0 and ell>ell0 bounds the
sum of the two charges by the constants

    U_s=t*(Q(X)+C(X))*K0/ell0,
    U_r=R0*epsilon/2+2*(D0*epsilon+R0*epsilon_1)/ell0.      (4)

Every substituted factor is nonnegative and every denominator is
positive. These are exactly the two L499 envelopes, whose accepted
scalar comparison gives

    U_s+U_r < .000020830490,
    r0-U_s-U_r > .00040166.                              (5)

This transfers both charges uniformly, retaining both saddle
corrections and the full reflected frozen-index Cauchy error.

### 4. Resultant lower bound and contradiction

For completeness, the application of L499's resultant inequality is
pointwise with the new (1). Write theta=Theta_hat and nu=sigma+i*eta.
Expanding L495's G_tilde and using real beta_m gives

    G_tilde=sum_m c_m(x)*[
          exp(i*theta-i*eta*log m)*(1-log(m)/ell)
          +exp(-i*theta+i*eta*log m)*log(m)/ell].

Only d=q=1 contributes to c_1=1, so its summand is exp(i*theta)
of modulus one. For u=log(m)/ell>=0 the remaining weight is bounded by

    |1-u|+u=max(1,2u-1)<=max(1,2*log(m)/ell0-1)=h(m).

The first identity follows separately for u<=1 and u>=1; the last
inequality uses ell>ell0>0. Finite triangle inequality and (1) give
|G_tilde(x)|>=1-M(x)>=r0. If H_t(x)=H_t'(x)=0, L495 (2) and (3),
with the uniform L494 remainder bounds, instead give

    |G_tilde(x)|<=|G_tilde-G_star|+|G_star|<=U_s+U_r<r0.

This contradiction proves precisely the qualified noncollision claim
on [X,Y). There is no continuity argument across Y and no assumption
that any zero is simple before deriving the contradiction.

### 5. Scalar certificate, checks and limits

Reproduce from the notebook with

    python3 scripts/heat/first-frozen-cell-certificate.py

The complete output is
`scripts/heat/first-frozen-cell-certificate.json`. It records the exact
parameters, prior-certificate hashes, every actual/required comparison,
the endpoint/domain enclosures, both inherited charge intervals and
the remaining margin. There are 24 checks and zero failures. Exact
domain, total-charge and margin fields were inspected in full; previews
of other fields are not proof of their correctness.

The program uses exact unrounded Fraction endpoint arithmetic: sums
and differences use opposite endpoints where required, products take
all four endpoint products, and reciprocals reverse endpoints after
excluding zero from the denominator interval. Thus all operations
preserve inclusion even with correlated inputs. Python integers do
not overflow. Decimal output is directed rounding for display only;
all comparisons use rational endpoints. The only transcendental inputs
are the pi and L_X enclosures already audited in L496 and retained
in the accepted L499 certificate. No new exponential, logarithm,
phase sampling or coefficient-ledger run is used.

The current L499 certificate's hash must match the input recorded by
its independent audit. All inherited exact parameters are compared.
The script checks the new endpoint/domain arithmetic and checks that
the retained intervals enclose the exact arithmetic expressions for
(4), their sum, r0 and its difference from that sum. Directed summaries
are

    U_s+U_r <= .000020830489779465538884432261,
    r0-U_s-U_r >= .00040166332609107773910199603.

Hash linkage and prior PASS records identify the accepted inputs;
they do not prove their mathematical validity anew. This original
producer execution was not the independent audit recorded in Section 6.
The source saddle/base-phase proofs, multi-cell transport, other times,
H1, zero time and RH remain unresolved. The earlier energy, inverse-gap,
direct-barrier, collective-bridge and approval-loop stops are preserved.

### 6. Separate critical interval audit, 2026-10-30

The pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-30-c499a-critical-audit-coverage.md` covers
this independent audit. The interval application is accepted without
repair. This verifies a local reproduction of the cited spatial method;
it does not advance beyond the inspected source mechanism or audit
the imported saddle/base-phase manuscripts.

**Analytic application.** The exact corner cutoff and positive width
give the entire cell by monotonicity of x/(4*pi)+t/16, with equality
at Y belonging to N+1. The logarithmic comparison in Section 1 bounds
the whole closed interval [X,Y], so the analytic centre domain holds
uniformly on [X,Y), including X. At each centre the derivative freezes
the same N; its disk may cross Y, requiring the full entering-pair
Cauchy charge. No numerical sampling or disk-containment shortcut is
used. The retained L494 and L496 domains agree exactly with this use.

At fixed t,N,P, each real beta_m is constant and the union of outputs
dq is finite. The increasing exact sigma multiplies each signed
coefficient by the positive m^(-Delta), preserving its absolute-value
factorization also at zero. The fixed positive h(m) then transfers the
complete L497/L498 bound. This includes all outputs above the explicit
ledger edge; it needs neither coefficient positivity nor a limit.

The inequality log N<L_X/2 fixes S0 at the anchor. The complete positive
squarefree expansion gives (2) at every centre because both r_p and
w_q decrease; it does not assert that the oscillatory functions decrease.
In (3), nonvanishing follows from r_p<1, and the increasing function
r/(1-r) and |nu'|<c bound the complex product derivative in the
correct direction. For the two rational corrections, the quotient-rule
numerators reduce respectively to 5-12x^2-x^4 and 2x(17-7x^2);
both are negative for x>=2 while Q,C are positive. Thus both absolute
saddle corrections decrease. All charge factors are nonnegative and
ell>ell0>0, justifying every upper-envelope substitution in (4).

Finally, expansion of L495's literal G_tilde gives Section 4's two
exponentials because beta_m is real. Only d=q=1 supplies c_1=1.
For 0<=u<=1 the weight is one and for u>=1 it is 2u-1, with agreement
at u=1. Since ell>ell0>0, log(m)/ell<=log(m)/ell0 gives the fixed
h(m) upper bound without requiring ell to increase with x. The full
mass therefore yields |G_tilde|>=r0;
L495 supplies the contradictory upper bound only at a true double
zero, using exactly the same normalization and fixed-index derivative.
No simplicity premise or continuation across the cutoff enters.

**Complete independent scalar consumption.** Reproduce by

    python3 scripts/heat/c499a-certificate-audit.py

The independent consumer imports and executes no producer routines,
and leaves the original certificate unchanged. It reconstructs all
seven domain fields, all twelve envelope fields and all 24 original
actual/required comparison records with exact equality. Each predicate
is recomputed before its stored flag is compared. It also checks all
parameters, both elementary intervals, current producer/input hashes,
the retained L499 audit's input hashes, K0 and D0 containment, the exact
reserve fraction and every displayed endpoint/domain/charge/margin
bound. The prior mass and transcendental audits remain mathematical
inputs; hash agreement is provenance, not a replacement for them.

Arithmetic uses unrounded rational endpoints: addition sums endpoints,
negation reverses them, multiplication takes the minimum and maximum
of all four products, and division reverses reciprocal endpoints after
excluding zero. These operations preserve inclusion with correlated
inputs. Python integers do not overflow; directed Decimal rounding is
used only for displays. No new elementary-function or coefficient
evaluation is needed for this audit.

The full consumer evidence is
`scripts/heat/c499a-certificate-audit.json`: 72 independent checks,
zero failures, and all reconstructed fields and comparison records.
The exact charge and margin endpoints were additionally inspected in
full. They verify the Section 5 bounds, in particular

    U_s+U_r <= .000020830489779465538884432261,
    r0-U_s-U_r >= .00040166332609107773910199603 > .00040166.

This accepts precisely the stated qualified noncollision interval.
The endpoint Y, other cells/times, H1, zero time and all-degree
actual-Xi positivity remain open, as do the manuscript-proof audits.
No new mathematical input or edge is introduced by this audit.

## Mathlib

Full matching coverage was not checked and remains unknown. Supporting
mathematics is finite coefficient factorization, monotonicity of real
powers and logarithms, differentiation of rational functions, triangle
inequalities and exact rational interval arithmetic. No Lean theorem
is claimed to formalize this interval result or its imported saddle and
phase inputs. Unknown coverage is not evidence of absence.
