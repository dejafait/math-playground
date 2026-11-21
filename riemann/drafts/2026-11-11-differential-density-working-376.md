# Differential-density cost attempt — step376 working record

11 November 2026. One RESEARCH attempt under the unchanged, separately
approved EXPLORE review374. Main gap: actual-Xi positivity and signed
forcing (L030-L032/C032a, L966/L968, L984(H)). The bounded test is the
normalized complete-kernel target action at exp(-n/64), not RH.

Inputs inspected: C997c(1),(4)-(6); C997s(1),(2) and step373's exact
antiderivative audit; review373's primary source contracts; stops364,
367,371,372. Existing unfinished notebook work is preserved. No source
refresh, cross-notebook input, numerical degree sweep or script is planned.

Partial mechanism, NOT YET A VERIFIED RESULT: write d=n+1 and
a_b(z)=b+iz for b=-1/8,-7/8. The upper endpoint exponents in c are
lambda_(b,alpha,j)=-n/4+alpha*a_b(gamma_j), alpha=n,n+2.
Each polynomial coefficient has degree d and nonzero leading term.
The lower window is a multiple of exp(-nc/4). The proposed monic
operator is

    P_n(X)=(X+n/4) product_(b,alpha,j)(X-lambda_(b,alpha,j))^(n+2),
    m=1+4(n+1)(n+2).

For v=P_n(-partial_c)phi, compact support removes all boundary terms
and the bilinear Laplace transform has the factor P_n(z). Need to check
nonzero v and every multiplicity; no coefficient conjugation is allowed.

Candidate cost obstruction: normalize v by its ACTUAL nonzero L1 norm,
and center its Laplace transform at c=2. On |z|=25n the centered
transform has modulus at most exp(25n/4). All forced roots have
|lambda|<=5n. Polynomial division plus maximum modulus would give
sup_(|z|<=5n)|centered transform| <= exp(25n/4)*2^(-m).
The target endpoint exponents have modulus <=4n. Cauchy on radius n
could then pay all target polynomial derivatives with the same factor.
Check the primitive coefficients, the lower-window cancellation, exact
constants and limit before recording a mathematical conclusion.

This would be an upper bound on the normalized response, not an upper
bound on a denominator or a small lower certificate. Its intended scope
is the full constant-coefficient endpoint-annihilator image. It would
not exclude general band-orthogonal densities, paid-leakage witnesses,
variable-coefficient operators or arbitrary band measures.

The bounded attempt now has a candidate quantitative obstruction. The
four endpoint root families have distinct real parts and n+1 distinct
imaginary parts each. Every nonzero constant-coefficient common
annihilator must contain each root to order n+2; thus M=4(n+1)(n+2)
zeros are mandatory even if the lower-window root is not. The centered
transform estimate above uses M in that case. For target primitive
coefficients, r!|q_r| <= (2^(n+3)+1)/(n+1). Cauchy on radius n therefore
bounds the four upper endpoint actions by

    F_n=4(2^(n+3)+1)(2^(n+2)-1)/(n+1)
          * exp(65n/4)*2^(-M).

For n>=12, exp(n/64)F_n <= exp(-n^2), using log(2)>=1/2.
The possible surviving lower window has modulus <=
8 exp(1/2)(n+2)exp(-3n/16), so its scaled contribution also tends to
zero. This is an actual normalized-action UPPER bound, uniform over
all cutoffs in this constant-coefficient image, not a denominator proxy.

For a concrete nonzero family choose Boman's finite convolution with
the standard unit-mass bump eta, Psi=1_[2-3/32,2+3/32]*eta_(1/64),
and phi_m=Psi*(eta_(1/(128m)))^(*m), where eta_h(x)=eta(x/h)/h.
Its support is [2-15/128,2+15/128], it equals one on
[2-1/16,2+1/16], and derivatives through m cost (C m)^r with
C=max(1,128||eta'||_1). For the full monic P_n, coefficient control
gives ||P_n(-D)phi_m||_1 <= (C m+5n)^m/4. Its integral is
P_n(0) integral phi_m, nonzero; an explicit norm lower bound is
(n/32)(15n/8)^(m-1). Neither bound is substituted for the actual norm.

These calculations will be written fully in C997t, with exact support,
adjoint, multiplicity and primitive details. Independent audit remains
pending. The scope is all constant-coefficient common-annihilator
densities, not all densities satisfying only the n+1 band equations.

Completed write-up: [C997t](../lemmas/C997t-common-differential-annihilator-target-action-stop.md).
The earlier partial reasoning above is preserved; the canonical result
uses M mandatory roots and pays the lower window when its extra root
is absent. Independent conceptual audit is pending, with a separately
proposed continuation assessment. No numerical script was needed.
