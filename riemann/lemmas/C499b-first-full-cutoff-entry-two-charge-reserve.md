# C499b — Two-charge reserve after the first full cutoff entry

## Hypotheses

Use the exact heat function, normalization and remainder of L494, the
resultants of L495, and L496's phase floor. Fix

    t=.16836, X=6000284561421.5, n=691004, q=n+1=691005,
    Y=4*pi*(q^2-t/16), P={primes p<=307},
    ell0=24.18022820120389, c=.500000000001,
    sigma(x)=.5+(t/4)*log(sqrt(1+x*x)/(4*pi))-t/(2*(1+x*x)),
    b_j=exp(t*log(j)^2/4), w_j(x)=b_j*j^(-sigma(x)),
    r_p(x)=w_p(x), r_d(x)=product_(p|d)r_p(x), r_1(x)=1,
    h(m)=max(1,2*log(m)/ell0-1).

Here d ranges over squarefree products of the 63 primes in P. For
k=n or q, use the real grouped coefficients of the finite k model,

    c_m^(k)(x)=sum_(d*j=m, 1<=j<=k) mu(d)*r_d(x)*w_j(x),
    M_k(x)=sum_(m>=2)|c_m^(k)(x)|*h(m).

All sums have their full finite output support, with no restriction
m<=k, m<=160n or m<=exp(ell0). All finite decimals are exact rational
numbers. At Y the canonical index is q; every spatial derivative there
freezes t and this NEW index q. The OLD n model at Y is used only as
a finite coefficient comparison, never as the true-function remainder.

Retain the audited L499 exact corner reserve and positive envelopes,
and C499a's audited fixed-index transfer calculations. For the actual
H_t interpretation retain L494's imported Polymath Theorem 1.3 saddle
normalization/estimates and L496's imported Planat v2 Lemma 6.3
base-phase theorem. Their manuscript proofs remain unaudited. Put

    epsilon=6e-7,
    epsilon_1=((6e-7+1.3e-6)*8.770232)/.14142,
    r0=14176540015048665224252705167939023
        /33554432000000000000000000000000000000.

## Conclusion

The complete entering-channel quantity satisfies

    J(q,Y)=w_q(Y)*sum_d r_d(Y)*h(d*q)
          < .000031423761288557.

With the enlarged full-support logarithmic envelope below, the upper
bounds U_s,new and U_r,new for BOTH L495 charges obey

    J(q,Y)+U_s,new+U_r,new
      < .000052254251068023 < r0,
    r0-J(q,Y)-U_s,new-U_r,new > .000370239564802521.

Consequently, under the retained analytic inputs,
H_t(Y) and H_t'(Y) cannot both vanish. This proves precisely one new
boundary point in addition to C499a's half-open interval, without any
full-cell or partial-cell fall credit. It does not assert a uniform
post-entry interval, later crossings, other times, H1 or zero time.
Actual-Xi all-degree signs and RH remain open.

This is a standalone known-method specialization of Michel Planat,
*Collective Contraction in the de Bruijn–Newman Heat Flow: Off-Zero
Logarithmic Derivatives and Certified Barrier Refinements*,
[arXiv:2609.37164v2, 7 October 2026, Section 6.1 Remark 6.2;
Section 6.6 (40)–(43), Lemmas 6.7/6.9 and the first-partial-cell case;
Section 6.7 (44)–(45), Lemma 6.10 and the subsequent full-support
moment and frozen-cutoff discussion](https://arxiv.org/html/2609.37164v2#S6.SS6).
The source already treats signed entering updates and both charges.
The difference here is this single boundary certificate using the
local audited r0 and constant ell0. No source transport decimal or
stronger transport ledger is imported, and no progress beyond that
source method is claimed. The separate independent critical audit in
Section 7 accepts this local proof and complete certificate, with the
retained manuscript-proof qualifications.

## Proof

### 1. Exact boundary and analytic domain

The definition of Y, with pi>0, gives the EXACT identity

    Y/(4*pi)+t/16=q^2.

Since q is a nonnegative integer, floor(sqrt(q^2))=q, including equality.
This is algebraic cancellation in the defining expression, not a floor
deduced from rounded endpoint values. The scalar certificate below
uses the already audited pi and L_X=log(X/(4*pi)) intervals and verifies
Y>X and

    t*(L_X+(Y-X)/X) < 4.527504235458053 < 5.17.

Indeed log(Y/(4*pi))=L_X+log(Y/X)<=L_X+(Y-X)/X, using
log u<=u-1 for u>0. Therefore (t,Y) lies in the closed centre domains
of L494 and L496. In particular ell=4*Theta_hat'>ell0 and |nu'|<c
hold at Y, independently of the finite index. Every r_p(Y)<1.
L494 applies with the canonical NEW index q, frozen throughout its
derivative disk. Its full epsilon_1 includes the unmollified entering
pair even when the disk crosses the boundary. Nothing paid for below
by J(q,Y) removes that separate Cauchy allowance.

### 2. Old mass and complete signed update

L496 gives sigma'(x)=t*x*(x*x+5)/(4*(1+x*x)^2)>0. For the old
finite n model its real beta_m is independent of x. Thus, on the
closed segment [X,Y], with Delta=sigma(Y)-sigma(X)>=0,

    c_m^(n)(Y)=c_m^(n)(X)*m^(-Delta),
    M_n(Y)<=M_n(X)<=1-r0.

The last inequality is L499's complete audited mass reserve. This is
the finite damping calculation of C499a, which is valid also at Y;
its open-cell noncollision conclusion is not being extended by
continuity. Coefficients equal to zero cause no exception.

At the SAME point Y compare the two exact signed finite sums. Subtracting
their definitions, every primitive j<=n cancels, leaving precisely

    c_m^(q)(Y)-c_m^(n)(Y)
       =sum_(d*q=m) mu(d)*r_d(Y)*w_q(Y).

There is one channel for each of the 2^63 squarefree d, including d=1.
The map d -> d*q is injective. An old coefficient at that output can
have either sign or vanish; no sign of it is assumed. Apply triangle
inequality to the signed update, THEN sum with h(m)>0. Since q>1,
none of the entering outputs is m=1, and this gives

    M_q(Y)<=M_n(Y)+w_q(Y)*sum_d r_d(Y)*h(d*q)
           <=1-r0+J(q,Y).                              (1)

In particular overlapping old outputs have not been counted as absent,
and grouping before the comparison does not yield cancellation credit.
There is exactly one new primitive index, so no block multiplicity
is omitted. The source's first-partial-cell restriction is respected:
the old mass is used without any spatial fall subtraction.

### 3. Full entering norm and enlarged logarithmic support

Define constants at the anchor X,

    R0=product_p(1+r_p(X)),
    J0=sum_p log(p)*r_p(X)/(1-r_p(X)), D0=R0*c*J0,
    a=w_q(X), S1=log(q)+sum_p log p,
    hcap=1+2*S1/ell0,
    Jcap=a*R0*hcap,
    A1cap=53/3+a, K1=R0*A1cap*S1.

Since sigma increases, w_j(Y)<=w_j(X) and r_p(Y)<=r_p(X).
Every entering output has log(d*q)<=S1. For s>=0,
max(1,2s/ell0-1)<=1+2s/ell0. Consequently

    h(d*q)<=hcap,
    J(q,Y)<=a*hcap*sum_d r_d(X)=Jcap.                (2)

The last equality is the full finite Euler expansion
sum_d r_d(X)=product_p(1+r_p(X)). In particular it retains outputs
above n, 160n, exp(ell0), and every product of all 63 primes.
It uses a deliberately coarse maximum-output envelope; no enumeration
cutoff, positive-tail omission or source J0 decimal is involved.

L499's primitive bound is sum_(j<=n)w_j(X)<=53/3. It yields

    sum_(j<=q)w_j(Y)<=53/3+a=A1cap.

Every output in the NEW finite model has log(d*j)<=S1. Expanding
all squarefree channels before the positive triangle bound, exactly
as in L499's full-support estimate, therefore gives

    |L_hat_new(Y)|
      <=sum_d r_d(Y)*sum_(j<=q)w_j(Y)*log(d*j)
      <=R0*A1cap*S1=K1.                              (3)

The j=d=1 logarithm is zero. All logarithms in this sum are nonnegative.
The old K0 and its old support cap are not reused for the new model;
the primitive sum AND maximum logarithm have both been enlarged.
No monotonicity of oscillatory |L_hat| itself is claimed.

Also rho(Y)<=R0. Since |1-A_p|>=1-r_p>0, L495's product-derivative
formula and the increasing function r/(1-r) on [0,1) give

    |E_prod'(Y)|<=R0*c*J0=D0.                        (4)

This is the complex product derivative, which bounds the modulus
derivative when L495 uses it. No new factors enter the Euler prime
set when the primitive cutoff changes.

### 4. Both charges and strict comparison

Use L495's two exact saddle corrections, with

    Q(x)=x*(x*x+5)/(1+x*x)^2,
    C(x)=(7*x*x-5)/(1+x*x)^2,
    sigma'=t*Q/4, eta'-1/2=t*C/4.

C499a's rational differentiation verifies Q,C>0 and Q',C'<0 for
x>=2: their derivative numerators are 5-12*x*x-x^4 and
2*x*(17-7*x*x), respectively, over (1+x*x)^3. Since Y>X>2,
Q(Y)<=Q(X), C(Y)<=C(X). Equations (3)–(4), ell>ell0, and L494's
FULL error and derivative bounds thus give L495's two charges the
nonnegative upper envelopes

    U_s,new=t*(Q(X)+C(X))*K1/ell0,
    U_r,new=R0*epsilon/2
               +2*(D0*epsilon+R0*epsilon_1)/ell0.       (5)

Only the K envelope changes from L499; the unchanged remainder-charge
formula is justified by the unchanged P, R0, D0 and uniform analytic
domain, not by any assertion of oscillatory monotonicity. All denominators
used for upper substitutions are positive.

The complete outward rational certificate gives

    a < .000000596314200997666,
    S1 < 296.197762161536,
    K1 < 10814.174447541029,
    Jcap < .000031423761288557,
    U_s,new < .000000000012548738,
    U_r,new < .000020830477230729,
    Jcap+U_s,new+U_r,new < .000052254251068023,
    r0-Jcap-U_s,new-U_r,new > .000370239564802521.        (6)

Each displayed upper decimal rounds upward and the last lower decimal
rounds downward. The strict comparison uses complete rational endpoints,
not the displayed decimals. The certificate is described in Section 6.

### 5. Resultant contradiction with the NEW frozen model

All c_m^(q)(Y) are real and c_1^(q)(Y)=1, since d*j=1 requires
d=j=1. Expanding the literal L495 G_tilde at the NEW index gives
an m=1 term exp(i*Theta_hat) of modulus one. For m>=2 the sum of
the two exponential coefficient moduli is

    |1-log(m)/ell|+log(m)/ell
      =max(1,2*log(m)/ell-1)<=h(m),

using ell>ell0>0. This is L499's two-case resultant estimate, valid
for every output, with no reality assumption on those exponentials.
Equations (1)–(2) therefore imply

    |G_tilde(Y)|>=1-M_q(Y)>=r0-Jcap.

If H_t(Y)=H_t'(Y)=0, the canonical q-index L494 bounds and L495's
pointwise identities instead give

    |G_tilde(Y)|<=|G_tilde-G_star|+|G_star|
                <=U_s,new+U_r,new<r0-Jcap,

by (6). This contradiction proves exactly the qualified boundary
noncollision claim. It uses neither endpoint simplicity by continuity
nor an old-index true remainder nor a derivative of the variable-cutoff
finite model. Finite support justifies every rearrangement above.

### 6. Certificate construction, consumption and limitations

Reproduce from the notebook with

    python3 scripts/heat/first-cutoff-entry-certificate.py

The full artifact is `scripts/heat/first-cutoff-entry-certificate.json`.
It records exact parameters, both input hashes and the prior L499
independent audit's current-input linkage, all 63 prime-row checks,
all new elementary evaluations and tails, the algebraic cutoff identity,
closed-domain bounds, enlarged full-support envelopes and complete
actual/required comparisons. There are 91 checks and zero failures.
The complete domain, new elementary evaluations and envelope fields
were inspected, including the exact cost and margin endpoints. Stored
PASS labels and hashes identify the retained audited inputs; they do
not reprove those inputs or provide an independent audit of this result.

Arithmetic uses Python integers and Fraction endpoints, rounding each
operation outward to the grid 10^(-60). Products use the minimum and
maximum of all four endpoint products; reciprocals reverse endpoints
after excluding zero. Exact inputs are retained until arithmetic;
negative lower endpoints round by mathematical floor. These rules
preserve inclusion with correlated inputs. No float enters a proof
bound; directed Decimal output is for display only.

The only newly evaluated elementary inputs are log q and the exponential
for a=w_q(X). Write q=2^19*v with v=691005/524288 in [1,2]. For
v in [1,2], z=(v-1)/(v+1) is in [0,1/3], and

    log v=2*sum_(j=0)^infinity z^(2j+1)/(2j+1).

The first 100 terms are enclosed by interval recurrence. The positive
omitted tail is at most

    2*z^201/[201*(1-z^2)].

The certificate uses the upper endpoint of the computed z^201 interval,
which still bounds this tail even when its lower endpoint has rounded
to zero. The same series at v=2 encloses log 2. The exact identity
log q=19*log 2+log v therefore supplies its enclosure. The audited
sigma(X) interval then encloses e=t*(log q)^2/4-sigma(X)*log q<0.

For each endpoint e evaluate the positive Taylor series for exp(u),
u=|e|, through degree 180. After the first omitted term, successive
term ratios are at most u/182<1. If T180 encloses u^180/180!, the
positive tail is at most

    T180_upper*(u/181)/(1-u/182).

Adding it upward and reciprocating bounds exp(e). Monotonicity of exp
combines the two endpoint evaluations. All sums, last terms, ratio caps,
tails and reciprocals are in the artifact; there is no assumed
transcendental decimal. Pi, L_X, sigma(X), prime logarithms/radii and
r0 remain the accepted L499/L496/mass-audit inputs.

The intentionally coarse h cap is already sufficient; no optimization,
phase sampling, core-only jump or further cell is needed for this test.
This execution is the producer, not a later independent critical audit.
Imported saddle/base-phase source proofs and all the scope limitations
in the conclusion remain open. No complete RH candidate is asserted.

### 7. Separate independent critical audit, 2026-11-01

The pre-existing SPECIALIZE assessment
`drafts/literature/2026-11-01-first-cutoff-entry-critical-audit-coverage.md`
covers exactly this audit. The argument and all stated bounds survive
without mathematical repair. Acceptance establishes a verified local
known-method input, not a result beyond the cited source mechanism.

**Support and analytic interface.** At the new centre Y the defining
identity fixes the canonical index q exactly; the independent rational
domain comparison gives t*(L_X+(Y-X)/X)<4.527504235458053<5.17 and
Y>X. Thus the closed L494/L496 domains include Y. Their phase floor
and prime set are independent of the primitive index, whereas the true
remainder and every derivative in L495 use the frozen NEW q. The
OLD beta_m remain x-independent finite coefficients: their damping
identity applies through Y, including signed or zero coefficients.
This verifies precisely the separation needed in (1); it never asserts
that R_n(Y) is the canonical remainder. The signed update has one
primitive entry and one injective output d*q for each squarefree d.
Triangle inequality handles every overlap, and c_1 remains one.

For (2)–(4), r_d is the product of prime heat radii, not b_d*d^(-sigma).
Finite distributivity retains every one of the 2^63 channels. The
maximum logarithm is log(q)+sum_p log p for the entire NEW model,
and its primitive cap is 53/3+w_q(X). Both changes are necessary and
both appear in K1. All logs are nonnegative. The denominator 1-r_p
is positive, and the product derivative bound applies to the complex
Euler product before bounding its modulus derivative. Direct rational
differentiation confirms the two negative derivative numerators stated
in Section 4 for x>=2. Positivity of every factor permits the endpoint
substitutions in both charges. The full reflected Cauchy entering-pair
allowance is retained in epsilon_1 independently of the mollified Jcap.
No spatial fall, variable-cutoff differentiation or oscillatory
monotonicity is used.

Expanding the literal new-model L495 resultant gives the two factors
1-u and u, where u=log(m)/ell>=0. Their total modulus weight is
1 for u<=1 and 2u-1 for u>=1; hence h bounds every nonconstant
output. This checks the last logical link: the finite budget gives
|G_tilde|>=r0-Jcap, while a true double zero gives the incompatible
upper bound Us,new+Ur,new. It does not infer collision exclusion from
coefficient mass alone.

**Independent complete arithmetic.** Reproduce with

    python3 scripts/heat/c499b-certificate-audit.py

The consumer imports no producer routine and preserves the producer
and its original JSON. Its complete evidence is saved in
`scripts/heat/c499b-certificate-audit.json`: 397 independent checks,
zero failures, all 91 producer comparisons consumed. It reads full
rational values, enforces positive denominators and rejects floats.
An independent sieve checks all 63 primes; every accepted logarithm
and radius is compared with the retained L496 input. It rebuilds the
full Euler product, derivative sum, logarithmic sum, all new envelopes,
domain comparisons, both charges and exact mass-reserve identity.
Current input and producer hashes identify the accepted artifacts;
they do not substitute for the earlier elementary/mass proofs.
The old expensive signed convolution is not rerun.

The consumer uses unrounded exact Fraction endpoints for every
arithmetic reconstruction. Four-corner interval products and reversed
reciprocal endpoints retain inclusion, including correlated quantities;
all denominators used here are positive. Stored producer intervals
must contain the rebuilt endpoints. Decimal output is display only.

For each logarithm it directly sums all 100 exact powers, independently
of the producer's rounded recurrence. For 0<=z<=1/3, every omitted
term has denominator at least 201, so its positive sum is bounded by
2*z^201/[201*(1-z^2)]. The recorded first-power upper endpoint is
checked against the exact z^201, and its tail is at least this bound.
The complete half-sum and final outward enclosure are separately
checked. The range reduction uses exactly q=2^19*(691005/524288).
For each of the TWO negative exponent endpoints the consumer directly
forms u^j/j! for every 0<=j<=180. The first omitted term is
u^181/181!; all subsequent ratios are at most u/182<1, so the
geometric bound in Section 6 includes the entire omitted tail.
The consumer checks the full sum, last term, ratio, tail, positive
enclosure and reciprocal against these exact values, then combines
the two endpoints by monotonicity of exp. The standard series are
[NIST DLMF 4.6.4](https://dlmf.nist.gov/4.6.E4) and
[NIST DLMF 4.2.19](https://dlmf.nist.gov/4.2.E19); the stated positive
real ranges and tail inequalities justify this specialization.

The complete rational comparison is

    cost_upper = 26127125534011085993122375648856459703153089352670711171
                 /500000000000000000000000000000000000000000000000000000000000,
    margin_lower = 185119782401260553000091772156402514729792162112173038829
                   /500000000000000000000000000000000000000000000000000000000000.

In particular cost_upper<.000052254251068023<r0 and
margin_lower>.000370239564802521. Every stronger displayed decimal
in (6), and the domain decimal in Section 1, passes a strict rational
comparison, not merely the producer's coarser .000369 margin test.
The full bounds and failures fields were inspected after the consumer
completed. This establishes only the qualified single-boundary claim;
the imported saddle/base-phase manuscript proofs, later crossings/times,
H1, zero time and actual-Xi signs remain independent open obligations.
No mathematical input or DAG edge is added by the audit.

## Mathlib

Full matching and supporting coverage was not checked and is unknown.
The specialization uses finite signed coefficient updates, finite Euler
expansions, monotonic real powers, triangle inequalities, elementary
logarithm/exponential series with explicit tails, and rational interval
arithmetic. No named Mathlib theorem is claimed to formalize this full
boundary certificate or its imported analytic inputs. Unknown coverage
is not evidence of absence.
