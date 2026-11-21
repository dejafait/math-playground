# Residual envelope — working calculation, 6 November 2026

Invocation-start approved target: the exact TARGET in
`literature/2026-11-06-residual-product-envelope-specialization.md`.
Main gap: actual-Xi all-degree mixed positivity. This calculation only
targets L835's fixed k=6002 analytic ratio, for a possible later overlap.

Candidate construction saved before detailed verification: let
J=k+1, T=gamma_J, a=R/(4T^2)=R/p_J<1 and b=0.34536, d=8.08344.
The first omitted factor has ratio bound (1+s*a)/(1-a). The remaining
positive-height representatives have gamma>T. Partial summation suggests

    S(T)=sum_(gamma>T) gamma^(-2)
      <=log(T/(2*pi))/(pi*T)
        +(b*(log(T)+1/2)+d-J)/T^2 = V(T).

This uses the complete inclusive count N(T)=J, not an assumed RH tail.
The candidate bound is

    log(M_s/m_1) <= log((1+s*a)/(1-a))
                       +(s+1)*R*V(T)/(4*(1-a)).

Still to verify: half-open endpoint identity, vanishing boundary term,
positive lower infinite product, square-map multiplicities, finite
rational enclosure interface and full finite-product overlap expression.
No certified ordinates or numerical overlap are present. No numerical
zero computation or sweep is authorized by this scope. A finite
evaluable formula suffices for this turn's target; a later independent
audit must precede using a new result as reviewed mathematics.

## Completed attempt

The candidate construction and all pending mathematical checks above
are completed in canonical `../lemmas/L836-residual-product-effective-envelope.md`.
The result is an unaudited standard-method specialization: an explicit
bound, an endpoint-only certified-data interface, and a sufficient overlap
test paying the complete finite-product cost. No numerical inputs or
overlap certificate were obtained. The historical candidate derivation
above is preserved; the canonical file governs its final qualifications.
No mathematical script or external source refresh was needed. Separate
conceptual scrutiny is nominated, not performed or self-approved here.
