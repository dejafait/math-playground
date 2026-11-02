# Uniform-frequency resonant packet mixture: uniform threshold failure

The complete proof, application-audited on 2026-10-31 with selector
independence explicitly required for the whole random tuple, is
[L578](../lemmas/L578-resonant-packet-mixture-clipped-obstruction.md).
It treats the entire approved deterministic A,C,D in [0,4] family,
every relative phase and selector probability, with U uniform on
[-1/4,1/4] and a nonnegative single-wave spectral remainder.

WHY IT FAILS: Nonnegative completion to the uniform spectrum forces
p(A^2+C^2/2)<=1. The coherent packet's positive Laguerre form can occur
only on a phase arc of normalized length less than 2/9; its pointwise
height is at most U^2 AC. These give the uniform bound
E Q<=1/(216sqrt(2))<5/1512<1/288, including the exact selector weights.
The single-wave remainder contributes no clipped mass. Parameter grids,
phase choices or optimization within this family cannot change the
obstruction. This does not stop other frequency laws, extra harmonics,
finite-K-only matching or general stationary realization. The prior
independent L576/L577 stops remain preserved. Full fourth constraints,
derivative-preserving completion and actual-Hardy/Xi transfer remain open.
