# Completion-stripped residual: absolute convexity envelope limit

The approved unchanged-disk E/G calculation yields the precise
[C645b bound](../lemmas/C645b-completion-stripped-residual-envelope-limit.md),
accepted by a separate conceptual audit on 1 November 2026. This is an informative negative result for the
displayed upper-envelope certificate, not a new unconditional zeta theorem
or a lower bound on the actual residual norm.

WHY IT FAILS: Uniform positive-real control of P, digamma control and
convexity give an envelope whose exponent exceeds the derivative upper
exponent by delta/4; the unchanged contraction has lambda<5delta/24.
Its normalized sufficient test therefore diverges at floor(log gamma),
even after removing the completion. This does not imply actual residual
failure, PSD or existence of off-line zeros. A useful continuation needs
a residual saving or different signed control, not merely a derivative
lower bound or renaming the norm. C645b quantifies the necessary saving
scale and preserves the separate C645a and C644a stops. Do not repeat the
same absolute-envelope calculation without materially new input.

Audit qualification: the proved divergence uses the factorwise bound
q_delta^N. The exact finite Blaschke product is smaller; no corresponding
divergence was proved for it. Retaining that product is an independently
testable refinement requiring a separate source gate, not permission to
repeat the q_delta calculation or infer success of the actual residual.


Exact-product refinement (1 November 2026, separate audit pending):
[C645c](../lemmas/C645c-exact-blaschke-product-rate-comparison.md)
resolves the previously open rate comparison in the favorable direction:
the derivative-upper-bound benchmark tends to zero. This removes only
the forced-divergence reason for the exact-product test; actual envelope
success is undecided without derivative lower control. The original
q_delta stop above remains valid. This is a local elementary
specialization, not a signed result or an RH advance beyond the sources.
