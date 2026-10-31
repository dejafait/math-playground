# L495 — Pointwise true-double-zero resultant charges

## Hypotheses

Use H_t, M_t, alpha, B, f_N and R_N from L494, including the imported
Polymath approximation and its normalization. Let t,x be real with

    .16836<=t<=.1718, x>=6000284561421.5,
    t*log(x/(4*pi))<=5.17.

Freeze t and N=floor(sqrt(x/(4*pi)+t/16)) when differentiating in x.
Continue the finite model and remainder with this same N near the
centre even at a cutoff transition. Write

    z=(1+i*x)/2, nu=z+(t/2)*alpha(z)=sigma+i*eta,
    b_q=exp(t*log(q)^2/4), S_N=sum_(1<=q<=N) b_q*q^(-nu),
    Theta=arg M_t(z), B=M_t(conj(z)), q=H_t/B.

Take a fixed finite prime set P and assume r_p=b_p*p^(-sigma)<1 for
every p in P. Both source prime sets, p<=307 and p<=29, are allowed
under these hypotheses. Define

    A_p=b_p*p^(-nu), E_prod=product_(p in P)(1-A_p),
    rho=|E_prod|, psi=arg E_prod, Theta_hat=Theta-psi,
    S_hat=E_prod*S_N, Z=exp(i*Theta_hat)*S_hat.

Since |A_p|<1, E_prod is nonzero. Arguments are locally chosen
differentiable real phases; their derivatives do not depend on adding
integer multiples of 2*pi. Assume

    ell=4*Theta_hat'>0.

This is a pointwise positivity hypothesis, not a certified numerical
floor. The finite product expansion has real coefficients independent
of x at fixed t,N:

    S_hat=sum_m beta_m*m^(-nu),
    beta_m=sum_(d|m, d squarefree over P, m/d<=N)
                  mu(d)*(product_(p|d)b_p)*b_(m/d),
    L_hat=sum_m beta_m*m^(-nu)*log m,
    W=exp(i*Theta_hat)*L_hat.

The sums have finite support. The squarefree factor is the product of
the prime heat weights, not b_d. Finally set

    V=2 Re(exp(i*Theta)*S_N), V_hat=2 Re Z,
    G_tilde=Z-W/ell+conj(W)/ell,
    G_star=V_hat/2-i*V_hat'/(2*Theta_hat').

## Conclusion

At every such point,

    G_tilde-G_star=(4i/ell)*[-sigma'*Re W+(eta'-1/2)*Im W],       (1)
    |G_tilde-G_star|<=(4/ell)(|sigma'|+|eta'-1/2|)*|L_hat|.       (2)

If H_t(x)=H_t'(x)=0 and |R_N(x)|<=epsilon,
|R_N'(x)|<=epsilon_1, then

    |G_star|<=rho*epsilon/2
                 +(2/ell)(|E_prod'|*epsilon+rho*epsilon_1).     (3)

L494 supplies, throughout the stated closed domain,

    epsilon=6*10^(-7),
    epsilon_1=((6*10^(-7)+1.3*10^(-6))*8.770232)/.14142
               <1.18*10^(-4).                                 (4)

Both printed charges of Michel Planat, *Collective Contraction in
the de Bruijn–Newman Heat Flow: Off-Zero Logarithmic Derivatives and
Certified Barrier Refinements*,
[arXiv:2609.37164v2, 7 October 2026, Section 6.7, pp.26–28,
equation (44), Lemma 6.10 and equation (45)](https://arxiv.org/html/2609.37164v2#S6.SS7),
survive this conceptual audit. This reproduces inspected source claims
and checks applicability of L494. The full derivation is retained
because normalization and phase loss were the designated audit questions;
it is not a new mechanism.

No coefficient majorant, |E_prod|, |E_prod'|, |L_hat| or positive
numerical phase floor is certified here. Neither M<1 alone nor (2)–(4)
excludes a collision. A separately proved lower bound 1-M for |G_tilde|
must strictly exceed the sum of the right sides of (2) and (3) to yield
that contradiction. No ledger, separator H1 or global endpoint is imported.

## Proof

### 1. Normalization and finite differentiation

The real-axis identities in L494, with u=conj(z), give

    q=f_N+R_N,
    f_N=conj(S_N)+exp(2i*Theta)*S_N=exp(i*Theta)*V.             (5)

Conjugation of alpha and M_t holds on their specified branches.
The quotient M_t(z)/M_t(conj(z)) is exp(2i*Theta), since the
denominator is the conjugate of the numerator. V is real as a
differentiable function on the real neighbourhood with frozen N.
The nonzero prefactor B permits differentiating q.

Writing E_prod=rho*exp(i*psi) gives the exact cancellation

    Z=rho*exp(i*Theta)*S_N, V_hat=rho*V.                      (6)

Multiplication of the finite product and sum gives beta_m as stated.
All heat weights depend on t alone, so at fixed t,N,

    S_hat'=-nu'*L_hat.                                      (7)

No variable-cutoff derivative or infinite interchange occurs.

### 2. All phase derivatives

The exact prefactor derivative from L494 is
(M_t'/M_t)(z)=alpha(z)+(t/2)*alpha(z)*alpha'(z). Since z'=i/2,

    Theta'=(1/2) Re(alpha(z)+(t/2)*alpha(z)*alpha'(z)),
    nu'=(i/2)*(1+(t/2)*alpha'(z)).                           (8)

The complex derivative of alpha and its values at z are

    alpha'(z)=-1/(2*z^2)-1/(z-1)^2+1/(2*z)=C_alpha-i*Q_alpha,
    C_alpha=(7*x^2-5)/(1+x^2)^2,
    Q_alpha=x*(x^2+5)/(1+x^2)^2.

Substitution in (8) retains both saddle corrections:

    sigma'=t*Q_alpha/4, eta'=1/2+t*C_alpha/4.                (9)

For the Euler phase put J=sum_(p in P) log(p)*A_p/(1-A_p).
Each factor has A_p'=-nu'*log(p)*A_p, whence

    E_prod'/E_prod=nu'*J,
    rho'/rho=Re(nu'*J), psi'=Im(nu'*J),
    Theta_hat'=Theta'-Im(nu'*J),
    ell=2 Re(alpha+(t/2)*alpha*alpha')-4 Im(nu'*J).           (10)

These identities account for the Euler argument and modulus separately.
In particular ell is not replaced by the unmollified phase or by
log(x/(4*pi)). Nonvanishing persists locally by continuity, legitimizing
the local argument derivatives. Positivity of ell at the centre is the
explicit assumption used for division.

### 3. Exact normalization of the first charge

Let a=Theta_hat'=ell/4. Equation (7) gives Z'=i*a*Z-nu'*W, so

    V_hat'/2=-a*Im Z-sigma'*Re W+eta'*Im W.                 (11)

The literal definition of G_star, with denominator 2*a, becomes

    G_star=Re Z+i*(Im Z+(sigma'/a)*Re W-(eta'/a)*Im W).

Equation (44) gives

    G_tilde=Re Z+i*(Im Z-(1/(2*a))*Im W).

Subtracting proves (1). Since |Re W|,|Im W|<=|W|=|L_hat|,
(2) follows. No factor of two, Euler-phase term or extra Im Z
term is missing.

### 4. True-double-zero projection

At H_t(x)=H_t'(x)=0, nonzero B gives

    q(x)=0, q'(x)=H_t'(x)/B(x)-H_t(x)*B'(x)/B(x)^2=0.

Equation (5) implies f_N=-R_N and f_N'=-R_N' at the centre. Moreover

    |V|=|f_N|<=epsilon,
    f_N'=exp(i*Theta)*(V'+i*Theta'*V),
    |f_N'|^2=(V')^2+(Theta'*V)^2.

Both V' and Theta'*V are real. Thus |V'|<=epsilon_1; the phase
term does not require an extra |Theta'|*epsilon charge.
For nonzero differentiable E_prod,

    rho'=Re(E_prod'*conj(E_prod))/rho, |rho'|<=|E_prod'|.

Equation (6) and the product rule imply

    |V_hat|<=rho*epsilon,
    |V_hat'|<=|E_prod'|*epsilon+rho*epsilon_1.

The triangle inequality for G_star and 1/(2*Theta_hat')=2/ell
prove (3). No scalar remainder bound has been differentiated. L494's
holomorphic fixed-N Cauchy estimate, including cutoff equality and
both crossing directions, is exactly the derivative input for (4).

### 5. Audit scope

The complete primary Lemma 6.10 proof and its preceding definitions
agree with (5)–(11); no repair is required. L494's original certificate
`scripts/heat/frozen-cutoff-cauchy-certificate.json` and its consumer
`scripts/heat/l494-certificate-audit.json` remain the arithmetic
evidence for (4), not rerun in this algebraic audit. No new numerical
certificate is asserted.

This verifies the inspected pointwise source argument, not the whole
Planat manuscript or the Polymath saddle proof imported by L494.
The newly written local transcription has not yet received a separate
independent audit. No printed numerical phase, mass or reserve is
accepted here. Strict reserve, finite interior collisions, other times
and zero-time control remain open; actual-Xi positivity and RH remain
unresolved.

## Mathlib

Full matching coverage was not checked and remains unknown. The proof
uses finite product/sum differentiation, local complex argument
derivatives at nonzero values, real and imaginary projections, and
elementary modulus inequalities. No specific Mathlib theorem is claimed
to formalize this full resultant or the imported heat approximation.
Unknown availability is not asserted absence.
