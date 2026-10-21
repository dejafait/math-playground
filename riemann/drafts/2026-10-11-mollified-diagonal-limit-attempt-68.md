# Fixed-N diagonal limit attempt — step 68

Prior gate: `literature/2026-10-11-mollified-carrier-diagonal-limit.md`
(EXPLORE, unchanged). Actual task: proof_attempt. Main RH gap is global
actual-theta mixed positivity; the approved intermediate target is exactly
the fixed-N limit in L396 (1), retaining all weights and collisions.
An evaluated carrier coefficient could enter a later complete mollified
mean; its balanced coefficient and the global sign/count gaps are independent.

Checkpoint before further work: put k=rs, ell=log H and lambda=log Y=ell/100.
The collision implies b divides ka, mn=ka/b, and sqrt(abmn)=sqrt(k)*a.
Thus introduce the absolutely convergent series

    F_k(s,t;alpha,beta)=sum_(b|ka) mu(a)mu(b) a^(-1-s)b^(-t)
                           sum_(mn=ka/b) m^(-alpha)n^(-beta).

For a prime not dividing k, squarefree a,b have exponents (0,0),
(1,0), (1,1). The provisional local factor originally written here
mistakenly summed repeated squarefree b exponents as a geometric series.
Correcting this before use, its actual finite local factor is

    1+p^(-1-s-t)-p^(-1-s-alpha)-p^(-1-s-beta).

This suggests F_k=zeta(1+s+t) A_k(s,t;alpha,beta)/
[zeta(1+s+alpha)zeta(1+s+beta)], with A_k bounded on positive
Mellin lines and small derivative disks. The desired limit may be zero;
this is provisional until the exceptional-prime factors and entire
Mellin tails are proved. Do not substitute a source's different coefficient.

Test: establish a uniform o(1) bound for the double Perron integral after
the two degree-two cutoff factors and both normalized q_H derivatives.
Use only the already assessed classical reciprocal-zeta input. Continue
if full-tail bounds and Cauchy derivatives give o(1); stop the certificate
if an order-one uncontrolled signed remainder or boundary interchange remains.
No script, numerics, cancellation conjecture, RH or growing-N assumption is used.

Full-tail strategy: take Re s=Re t=c=1/lambda, and
|alpha|,|beta|<=c/4. The arithmetic factor is uniformly bounded.
The numerator zeta has the absolute bound O(1/c). For small s the
two reciprocal factors have product O(|s|^2); away from s=0 the
standard reciprocal-zeta bound on Re>=1 makes their product
O(log^2(2+|Im s|)), independently of c. The t integral costs c^(-2).
The s integral costs O(log(1/c)). Including lambda^(-4) gives
O(c log(1/c)). Cauchy derivatives cost c^(-j) and normalized
ell^(-j) cancel them since ell=100/c. Exceptional-prime local
factors and Perron interchange are still to be written rigorously.

## Completed bounded attempt

The full proof is canonical in [L397](../lemmas/L397-fixed-head-mollified-carrier-diagonal-vanishes.md).
The corrected finite local factor, including all primes dividing rs,
produces a bounded arithmetic factor. The original positive Mellin lines
suffice: no contour displacement or coupled residue evaluation is needed.
The complete estimate is O_N(log log H/log H), against the required o(1),
including all nine normalized shift-derivative terms. The limit is zero.
L396 then gives the fixed-head carrier mean o(1). No balanced or complete
signed mean, growing-N statement or sign/count/RH result was attempted.

Known-source input is the already assessed reciprocal-zeta bound used in
Young's proof of Lemma 7, p. 546, citing Titchmarsh (3.11.8); that primary
proof case was retrieved for exact source tracing. Further direct bounded
page extraction from the Titchmarsh PDF timed out and shell downloading
had no network access. The existing adequate assessment was reused; no
new or stronger source theorem is asserted to have been inspected.
No mathematical script or numerical certificate was needed. Hand checks
verified all four exceptional-prime exponent cases, the arithmetic-factor
identity and the Cauchy normalization. The initial squarefree-factor
mistake was corrected before its use, as recorded above.

Outcome: ADVANCE / RESEARCH / POTENTIALLY_NEW. The local limit was not a
matching result in the sources checked; this is not a claim of originality
or a complete solution. Separate critical audit remains required. The
new audit continuation is REVIEW_REQUIRED and must receive its own gate
approval in a later turn; this does not retract the completed attempt.
