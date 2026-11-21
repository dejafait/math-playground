# Gaussian estimates supporting the near-zero block input — coverage1183

TARGET: Audit Polson v24 Lemma 7.6 equations (23)-(25) for every N>=1 and real polynomial q of degree at most 2N-1, including the complex evaluation bound, C_N<2sqrt(N), and the Fourier bound 4^N exp(-y^2/12)||q||_G^2.
CHECKED: 2026-11-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Comparison1183 searched exact Polson/Lemma7.7 records and recent Mehler/Gaussian-polynomial records in the active notebook, reused comparison1108 and application audit1116, and searched exact theorem phrases externally. No independent matching audit was located; queries and limits are in completed comparison1183, not a novelty claim.
SOURCE_EVIDENCE: Nicholas G. Polson, On Hilbert's 8th Problem, arXiv:1708.02653v24 (11 September2026), https://arxiv.org/pdf/1708.02653v24, Lemma7.6/(23)-(25) and its full proof printed p19; Lemma7.7/(26) and full proof pp19-20 for downstream use. NIST DLMF18.18.28 https://dlmf.nist.gov/18.18.E28 and18.39(i)/18.39.14 normalization https://dlmf.nist.gov/18.39#i were directly inspected on2026-11-16.
COMPARISON: Every requested estimate is already claimed by the cited preprint. DLMF supplies Mehler's identity and Hermite normalization; it does not directly certify the preprint's degree-dependent constants or contour calculation. Independent checking is justified to validate a load-bearing imported input, not to rebrand known mathematics as a discovery.
GAP: Mathematical validation of complex specialization, the finite-degree Cauchy-Schwarz estimate, the bound on C_N and the shifted-contour Gaussian integral is outstanding. Source access and theorem-level comparison for this bounded audit are complete; no full Lemma7.7 or zeta-source certification is authorized.
REASON: This is one independently testable component of Lemma7.7 with all required primary material accessible. A pass supports reliability of C030b's finite input; a failure identifies a precise input requiring correction. Newly written coverage1183 requires separate approval next turn before the mathematical audit.
SCOPE: One source-proof audit of(23)-(25) under the exact real-polynomial hypotheses below; standard Hermite orthogonality, Mehler identity, Cauchy-Schwarz and Cauchy's contour theorem may be cited. No new sign mechanism, cap extension, all-degree block assertion, source-script replay, Lemma6.1 audit, full explicit-formula audit or full Lemma7.7 assembly.

## Source statements to check, not established here

Fix N an integer >=1 and q in R[X], deg(q)<=2N-1; q=0 is included.
Set ||q||_G^2=integral_R exp(-x^2)|q(x)|^2 dx, without a probability
normalization. Polson equation(23) asserts for z=x+iy and 0<r<1:

    exp(-Re(z^2)) |q(z)|^2
      <= r^(-(2N-1))/(sqrt(pi)*sqrt(1-r^2))
         * exp(-(1-r)*x^2/(1+r)+(1+r)*y^2/(1-r)) * ||q||_G^2.

Equation(24) uses

    r_N=1-1/(2N),
    C_N=r_N^(-(2N-1))/(sqrt(pi)*sqrt(1-r_N^2)) < 2*sqrt(N),
    exp(-x^2)|q(x)|^2 <= C_N||q||_G^2   (x real).

Equation(25) asserts, for every real frequency y,

    |integral_R q(x)^2 exp(-x^2) exp(-iyx) dx|
      <= 4^N exp(-y^2/12)||q||_G^2.

There is no parity condition for this audit. The eventual application
q(x)=x^epsilon p(x^2), epsilon=0 or1 and deg(p)<=N-1, lies within
the source degree restriction; application to Lemma7.7 is future work.
These source estimates are uniform in all coefficients, not estimates
for a chosen test polynomial. N=1 and y=0 must be included.

## Inspected standard inputs and audit obligations

[DLMF18.18.28](https://dlmf.nist.gov/18.18.E28) states Mehler's sum
with |r|<1. [DLMF18.39(i)](https://dlmf.nist.gov/18.39#i), the paragraph
after18.39.15, gives the physicists' Hermite weight exp(-x^2) and
squared norms 2^j*j!*sqrt(pi). Keep the same H_j convention throughout.
The preprint uses h_j=H_j/(2^j*j!*sqrt(pi))^(1/2).

Independently check the finite Hermite expansion and its norm factor;
the weighted infinite kernel used to dominate the partial sum; and the
complex-conjugate specialization in(23). DLMF labels its spatial
variables real, so justify the required complex identity and convergence
instead of invoking its real-variable positivity claim. This is a
specific proof obligation, not an identified source error or an approved
new theorem. Cite the standard identity and justify only its use here.

For(24) check the scalar estimates in the source proof, including N=1.
For(25) examine its displacement z=x-iy/6 when y>=0, vertical-edge
limits for a fixed polynomial and frequency, and the subsequent bound
using(23) at r=1/2. Keep every exponential and Gaussian normalization;
verify the constant 4^N and exponent -y^2/12, then the negative-y case.
Coefficient-uniform conclusions must follow from the norm bound;
no unnecessary uniform contour limit in all polynomials is presumed.
Do not replace algebraic q(z)^2 by a modulus square until taking an
absolute-value estimate at the stated step.

Success is a complete exact proof audit of all three bounds under these
hypotheses; failure is a precise invalid inequality, missing hypothesis
or counterexample. Neither a sample plot nor a finite numerical sweep
establishes the requested coefficient-uniform statement. Preserve partial
reasoning if the audit stops, and do not label an unresolved check passed.

## Relevance, limitations and approval boundary

The main gap remains L030-L032/C032a's actual-Xi mixed positivity in
every degree, together with independent actual-theta/realization gaps.
C030a and C030b/audit1116 supply the local finite transfer/application;
their proofs need not be reread to audit this Gaussian estimate.
Comparison1183 extracts the exact Lemma7.7 lower bound and its required
0.7 uniform margin. A successful audit here checks one necessary source
component only: the explicit formula, archimedean estimate, scalar
near-zero margin and far-time source proof remain imported and unaudited
independently. No RH inference or new result beyond the sources follows.

Prior source reading1108 is reused; prior application audit1116/1182 is
not repeated. The stopped finite-block automatic-extension route1117 is
unaffected. Mathlib coverage for the full bounds has not been checked;
availability is unknown, not asserted absent. There is no cross-notebook
input. This assessment records source coverage, not a completed proof
audit; separate approval is still required before research invocation.
