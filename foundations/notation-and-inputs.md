# Starting theorems and definitions

For Re(s)>1, define ζ(s)=Σ_{n≥1} n^{-s}, where n^{-s}=exp(-s log n) with the real logarithm. Use the standard meromorphic continuation theorem for the Riemann zeta function: this extends to C with its only pole a simple pole at 1. Use Riemann's functional equation

ζ(s)=2(2π)^{s-1} sin(πs/2) Γ(1-s) ζ(1-s).

Reference: the standard named Riemann functional equation, also [NIST DLMF 25.4.2](https://dlmf.nist.gov/25.4.E2). Other starting tools are the identity theorem for meromorphic functions, the fundamental theorem of arithmetic, absolute convergence and rearrangement of series, and the standard theorem that Γ is holomorphic and nonzero on Re(s)>0. Further named inputs used below are the Weierstrass theorem for locally uniform holomorphic limits, the fundamental theorem of algebra, the Gaussian integral, Poisson summation for Schwartz functions, and Euler’s gamma integral Γ(z)=∫_0^∞e^{-u}u^{z-1}du for Re(z)>0. The standard named Hadamard factorization theorem is used in Lemma 24 only after proving its finite-order hypothesis. No RH-equivalent result is an input.

File paths in lemma text and reproduction commands are relative to the repository root. Run certificate commands from that root. Lemma numbers are stable identifiers; locate their files through the root DAG.
