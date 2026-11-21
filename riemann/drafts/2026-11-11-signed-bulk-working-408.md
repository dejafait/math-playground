# Signed complete-kernel endpoint specialization — step408 working note

Approved target: review406 (SPECIALIZE, separately approved step407).
Inputs: C997c complete kernel and C997s windows/frequency set/cap; reused
Vanlessen arXiv:math/0504604v2 Thm2.4(b), Thm3.32, Section5.2 and DLMF
Table18.3.1 from review405. No broader asymptotic target is authorized.

Main gap: actual-Xi positivity and unpaid forcing/H; intermediate E_n open.
Attempt: N=n+1, x=t/(4N), translate positive-leading p_N with
L_N^(2)=(-1)^N sqrt((N+1)(N+2)) p_N. After multiplying exp(-t/2)/N,
the explicit amplitude has order N^(-3/2) on the fixed bulk.
Integrate only the explicit leading cosine by an endpoint primitive with
denominators lambda+is theta'(t), lambda=+/-3/8+iz; their real parts
have modulus at least1/4. The source O(1/N) term is integrated absolutely,
never differentiated. Both windows and beta terms, and exact -1 integral,
will be retained. Expected error scale is N^(-5/2) times the complete
exponential envelope, subsequently multiplied by 1+exp(sqrt(n)) for a
capped residual. Normalization, phase, derivative bounds and envelope
constants still require completion; this note establishes no theorem.

Continue if a finite uniform constant follows beyond one existential
onset; stop if uniformity fails. A large capped error does not bound E_n
from below or disprove cancellation. Growing truncation is outside scope.

Completed in canonical C999d, still unaudited. The finite-window formula
and uniform error follow; its capped error allowance misses the required
rate. See that canonical proof for all signs, constants and qualifications.
