# Far-left horizontal theta-Mellin segment: research nomination

TARGET: Attempt the standalone far-left theta-Mellin bound T_F(s)<=600u^(5/2)sqrt(47Q/(20pi))(1+10u/Q)exp(-Q/(20u)) on all D, including the h=0 improper endpoint, using complete-series Gaussian majorants and endpoint/phase case analysis.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step530's exact-target, Gaussian-sum and endpoint search and narrow duplicate/failure comparison in 2026-11-05-mellin-far-left-horizontal-segment-scope.md. No matching theorem or novelty claim is inferred.
SOURCE_EVIDENCE: NIST DLMF v1.2.8 (2026-09-15), 20.2.3/20.2(ii), 2.10(i)/2.10.1, 5.9.1 and its hypotheses, 5.2.1 and 2.5(i)/2.5.1; bramble_trace paper23 v1 (18 October 2026), Section3 Lemma2 (10)–(14), https://rstation.ai/problems/riemann_hypothesis/papers/23. Exact inspected statements, links, applicability and access qualifications are in step530's completed scope assessment.
COMPARISON: Theta analyticity, finite effective summation with an explicit remainder and gamma-moment integrals supply standard methods, but neither a uniform phase estimate nor this normalization and exact allowance. This source-component reproduction needs new local verification, not automatic theorem import.
GAP: Establish the integral limit and full-series control on the entire interval, including the complex-power angular factor, and pay the stated threshold uniformly on all D; alternatively isolate a rigorous obstruction to the chosen sufficient-majorant method.
REASON: The independent observable is fully specified and accessible primary methods suffice for a bounded test without the parked global identity, continued vertical endpoint or unread supplements. Citation alone cannot verify its parameter-specific hypotheses or constants.
SCOPE: Newly written ready continuation, subject to separate supervisor approval next turn. No far-left estimate or mathematical specialization was derived during the literature-only review. Classify a future attempt as REPRODUCTION, not creative work.

Use exactly L797's D and x=u+ih, L798's phase and principal branches,
L799's normally convergent complete P series, and L802's endpoint
geometry:

    D={s: |s|>=6000, Re(s)>=-|s|/(8 log|s|)},
    F(x)=x(pi exp(2x)-9/4)=s,
    Q=pi exp(2u), d=3/(16u), A=2F'(x)/x,
    a=exp(-i Arg(A)/2), z_L=x-da=v_L+i y_L,
    S_s(z)=2s Log(z)+(9/2)z-pi exp(2z), C=sqrt(2pi/A).

The sole observable and threshold, with existence part of the target, are

    J_F(s;epsilon)=integral_epsilon^(u/2)
        exp(2s Log(v+i y_L))P(v+i y_L) dv,
    T_F(s)=|lim_(epsilon down to 0) J_F(s;epsilon)|
               / |4pi^2 exp(S_s(x)) C|,
    T_F(s)<=600u^(5/2)sqrt(47Q/(20pi))
                  (1+10u/Q)exp(-Q/(20u)), s in D.

The rational square-root factor is the source's 4.7/(2pi). This chosen
split is not identified with an unprinted source contour piece.
L800/L801 are downstream context only. No other notebook, global contour
equality or continuation of M is an input.

The bounded attempt must address these obligations coherently:

1. Match endpoint geometry and principal Log on the full interval.
   Use the actual saddle relation in the h=0 improper-endpoint case;
   for h nonzero verify the actual endpoint. Pointwise convergence and
   uniform payment are separate obligations, especially as h tends to zero.
2. Control the complete P series. Euler–Maclaurin (DLMF2.10.1) requires
   smoothness, derivative integrability, endpoints and the infinite limit
   before using its remainder. Gamma integrals (5.9.1) require Re(nu)>0,
   mu>0, Re(z)>0 and principal powers. Any simpler real sum-integral
   comparison must be proved with all constants. Do not assume complex
   signs, the source circle estimate, L799's diameter eta or L802's tau>3.
3. Retain the angular factor of the complex power, complete phase and
   exact |C| normalization. Give an effective phase/endpoint argument on
   every subinterval. L802's concavity is proved only for v>=u/2; a single
   left tangent is not preapproved here. Justify any series/integral
   interchange with an absolute majorant.
4. Pay the allowance for both closed boundaries of D, both signs of h,
   h=0 and all u>3 without an upper cutoff. Samples or an estimate for
   fixed h do not establish the uniform claim.

Continue only with a full uniform proof of limit and bound, or an
informative rigorous obstruction to this sufficient method. A failed
majorant is not a counterexample to T_F or RH; preserve its precise
failure and require materially new input before retrying. Save unfinished
reasoning before lengthy work. No numerical script is required.

The main gap is actual-Xi all-degree mixed positivity. Success could
supply one finite component for separately assessed assembly with
L800/L801/L802. The vertical endpoint, contour identity, full budget,
quotient/inversion, certificates and sufficient signs remain unresolved.
No RH candidate is asserted. The global-import stop remains valid;
Derivations42/43/65/87 are not imported and access searches are not
repeated. Full matching Mathlib coverage is unchecked.
