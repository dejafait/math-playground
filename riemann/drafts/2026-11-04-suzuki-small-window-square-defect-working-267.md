# Suzuki small-window square defect — working record (267)

Approved target: the exact Next action in the supplied SPECIALIZE
assessment `literature/2026-11-04-suzuki-small-window-square-defect.md`.
Inputs read: L018's convention, L618's operator hypotheses and support
reduction; Suzuki 1907.07302v2 (1.11), (1.13), Propositions 3.1–3.2,
(3.8)–(3.10), (3.13). No L618 norm replay.

The main gap is actual-Xi mixed positivity. This one diagnostic tests
the sufficient square order K_2[t]^2 <= K_4[t]^2, not the bare implication
between global contractivity statements. A negative witness stops this
order. An uncontrolled remainder parks the diagnostic without a sweep.

Preserved reasoning before completing the proof: causality and lambda(1)=1
reduce K_theta(x) to g_theta(x) for 0<=x<log 2. Formula (3.13) and
Proposition 3.2 suggest a_theta=(2*pi)^theta/Gamma(theta) and
K_theta(x)=a_theta*x^(theta-1)+O_theta(x^theta), theta=2,4.
The integral term in (3.13) is of order x^theta because its Bessel
quotient is bounded near zero. This still needs an explicit uniform
bound in the canonical proof, including the weaker O(x) display in the
printed Proposition 3.2 proof.

For u=x+t, the constant vector gives
K_theta[t]f_t(x)=(2t)^(-1/2)*integral_0^u K_theta(v)dv on [-t,t].
The anticipated norm leading term is
a_theta^2*(2t)^(2theta)/(theta^2*(2theta+1)).
The square defect should therefore start with -64*pi^4*t^4/5;
the theta=4 norm starts at order t^8. These are working values pending
the full uniform error calculation; no numerical certificate is used.

Completed: the uniform error calculation and positive existential
onset are now in canonical L739, with the anticipated coefficients
confirmed. The square-order mechanism has a negative witness;
the bare contractivity implication remains unresolved. This working
record preserves the unfinished-stage reasoning, not a second proof.
