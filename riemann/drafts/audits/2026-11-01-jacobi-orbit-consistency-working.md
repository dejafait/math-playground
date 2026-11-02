# Jacobi orbit consistency audit — working record, 2026-11-01

Approved target: Planat–Sole v1 (5.10), (5.12), including all real L,
V=0 and the L019 normalization. The prior SPECIALIZE assessment is
`drafts/literature/2026-11-01-jacobi-orbit-consistency-audit.md`.
This is a source reproduction/application audit, not a new sign mechanism.

The main gap remains actual-Xi all-degree signs at unbounded heights.
The intermediate target is a well-defined theta-specific differential
state for a future coupled two-point calculation. Continue only if the
unsquared equations and reconstruction pass everywhere; a mismatch or
unjustified exceptional point parks this package. The integrated Stein
tail, Fourier compensation and higher signs are independent open gaps.

Reused the October 26 comparison and November 1 discovery assessment.
Scoped searches found no previous independent (5.10)/(5.12) audit.
The corrected auxiliary-Jacobi stop concerns L600's zero-mode correction,
not this actual theta-defined orbit; its missing bilinear identity remains
unresolved. Existing changes and unfinished work are preserved.

Primary source retrieval: Planat–Sole arXiv:2608.19160v1, (1.1),
(5.1)–(5.12), Lemma 5.1 and Proposition 5.3 with their complete proofs;
Romik arXiv:1807.06130v2, (1)–(3) and (28), printed pp.1–2,14.
No new literature comparison is needed. Import the ordinary-x Jacobi
ODE and (5.7)>0; their upstream proofs remain unaudited.

Partial replay saved before completion: with x=exp(L), Y=theta_3(x),
b=x Y_x/Y=(a-1)/4 and L derivatives marked by primes,

    Y Y_xx - 3 Y_x^2 = Y^2 U/(8x^2),
    Y^2 Y_xxx - 15 Y Y_x Y_xx + 30 Y_x^3 = Y^3 V/(4x^3).

Thus the imported Jacobi equation gives 4(V^2+U^3)=A^2 U^2.
The definitions give U'=2aU+2V everywhere. Differentiating
A^2=4(U+chi^2), with chi=V/U, gives exactly
chi(chi'-a chi+U)=0; division at chi=0 is not permissible.

Pending check: analytic continuation is legitimate only after proving
chi is not identically zero on the connected real domain. The theta
series give A>=pi x and, using imported (5.7), U=O(x^2 exp(-pi x))
as x tends to infinity. This will rule out chi identically zero through
A^2=4(U+chi^2). All divisions are by x,Y,A,U or positive constants,
except the explicitly restricted temporary division by chi.

The kernel replay uses Phi(L/4)=x^(1/4)Y[b'+b^2+b/2].
The L019 coordinate is L=2u, hence k(u)=4Phi(u/2), with the
positive real fourth root of A. Endpoint/parity and all constants
will be recorded in the canonical result after the remaining checks.

Completed: the finite theta-series bounds prove chi is not identically
zero; analytic continuation covers every V=0. The modular point and
reconstruction pass with L=2u. Full proof and exact source qualifications
are canonical in `lemmas/L608-actual-jacobi-orbit-consistency.md`.
The sole direct local input is L019; L605 is a normalization comparison,
and L233/L604/L607 are relevance or limitation references, not premises.
No numerical experiment, mathematical script, Fourier estimate or new
source theorem was used. This is a local input validation, not progress
beyond the source's claimed conclusions.
