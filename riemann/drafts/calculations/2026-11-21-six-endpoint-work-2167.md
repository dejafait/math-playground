# Fixed six-endpoint calculation2167: saved before execution

Approved target and unchanged settings: review2166. No source refresh,
parameter tuning, zero table, or H2 assembly is part of this attempt.
Main gap remains L030-L032/C032a. The intermediate output would be
uniform signs at six endpoints, hence placement by continuity; C919e
and C919d/C919c are downstream uses, not premises of the integrals.

The planned exact implementation is
`scripts/h2-head/six_endpoint_2167.py`, with a complete JSON certificate.
Only L019 and L058 supply mathematical premises. Standard Simpson and
Taylor error theorems and Decimal contracts are imported from the
unchanged ready assessment. All specialized bounds must pass before
the lengthy 262145-node pass. Stop on any failed prerequisite or sign.

Kernel truncation: write a_n=pi*n^2 and the two finite summands as
8*a_n^2*exp(lambda*u^2+9*u/2-a_n*exp(2*u)) and
-12*a_n*exp(lambda*u^2+5*u/2-a_n*exp(2*u)). Use absolute bounds on
their first four derivatives on exactly1024 closed spatial cells.
For p=2j, j=0,...,8, divide by j! for the time coefficients at1/40.
The derivatives of a summand's exponent are bounded by
A1=2*lambda*r+b+2*v_hi, A2=2*lambda+4*v_hi,
A3=8*v_hi, A4=16*v_hi. The exponential derivative polynomials are
1,A1,A1^2+A2,A1^3+3*A1*A2+A3,
A1^4+6*A1^2*A2+3*A2^2+4*A1*A3+A4.
Leibniz with the exact power derivatives and |cos^(s)(x*u)|<=x^s
gives complete fourth-derivative bounds, not sampled derivatives.

Omitted-index bound on[0,4], p<=18, lambda<=1/20:
use pi>3, pi^2<10, exp(2u)>=1+2u and lambda*u^2<=u/5.
For n>=5, the integrand's positive envelope is at most
80*n^4*exp(-3*n^2)*u^p*exp(-145*u).
Writing n=5+m gives sum n^4 exp(-3*n^2)
<=625*exp(-75)*sum(m+1)^4 exp(-30*m)
<=187500*exp(-75), since exp(-30)<1/2 and the geometric fourth
moment at1/2 is300. Integrating to infinity gives
B_index(p)=15000000*exp(-75)*p!/145^(p+1).

Full spatial bound: L058's prefactor is<200, using exp(3)>20,
pi<22/7 and its geometric identity. For u>=4, p<=18,
u^p<=exp(p*u) and lambda*u^2+(p+9/2)*u<=2*u^3
<=(3/2)*exp(2u). The first inequality reduces to
u/20+45/2<=2*u^2, true at4 and increasing thereafter.
Thus the weighted complete kernel is at most200*exp(-3*exp(2u)/2).
Convexity and exp(8)>256 bound its integral by
B_space=(200/768)*exp(-384). Retain this bound for all coefficients
after division by j!, and for the complete ninth time derivative.
On[0,4], that derivative's absolute integral is bounded by the1024
cell sum of width*r^18 times the lambda=1/20 positive envelope.
Add both tails before multiplying by(1/40)^9/9!.

Arithmetic plan: 80-digit directed Decimal operations, neighbors of
correctly rounded exp, Machin pi from exact rational atan remainders.
Use degree31 sine/cosine Taylor polynomials at the exact small mesh
angle x*h and the Lagrange bound (x*h)^32/32!. Propagate interval
sine/cosine by addition formulas; widening is retained in every
quadrature coefficient. All 128 closed time cells are polynomial
ranges via interval Horner, with all coefficient and Taylor errors.

No sign or useful error size is claimed before execution. A backend
trust assumption remains; runtime, flags and contexts will be saved.
Full matching Mathlib coverage is unchecked. Canonical proof and
qualifications will be saved only for the actual completed result.

Completed outcome: PASS at the original settings, with no refinement.
The result and complete proof are now canonical in C919f; the two
execution certificates and the full-record inspection are under
`scripts/h2-head/` with suffix2167. All six uniform signs passed.
The2124 exact-record/internal checks do not replace a separate
conceptual audit. No H2 assembly or global conclusion was attempted.
