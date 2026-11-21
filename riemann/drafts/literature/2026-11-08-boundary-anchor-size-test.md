# Boundary anchor versus the displayed interpolation envelope

TARGET: Test whether |C_(1/2)(x)|/[A_0(1/2)(1+|x|)^5 exp(-pi|x|/2)] tends to zero as |x| tends to infinity and consequently whether L900's displayed sufficient test fails for every fixed positive squared-height transfer.
CHECKED: 2026-11-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step119's boundary-margin search and exact duplicate/failure comparison are recorded in 2026-11-08-boundary-anchor-xi-defect-margin.md; reuse the ready frequency-interpolation comparison. No matching boundary-scale obstruction was located in the named local records; no novelty claim.
SOURCE_EVIDENCE: Gonek, Invent.Math.75(1984), Section2(20) and complete following Cauchy paragraph p127, https://sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf ; DLMF1.2.8 (2026-09-15), 25.4.3/4 https://dlmf.nist.gov/25.4 , 5.11.2/9 and sector/uniformity sentences https://dlmf.nist.gov/5.11 ; L898 identity/normalization, L899 positive normalizers and audited L900(1)-(2).
COMPARISON: Standard ordinary-derivative and gamma estimates cover the analytic inputs. The remaining work is the exact boundary translation and power/rate comparison for this normalized observer. No cited source states the proposed limit or the notebook-specific stopping conclusion.
GAP: The limit and fixed-distance consequence must still be proved, with all constants and both signs of x controlled. No effective onset, finite-band exclusion, shrinking-step obstruction or adverse Xi sign is supplied by this assessment.
REASON: A bounded standard specialization can decide whether the actual anchor can pay the displayed absolute budget, avoiding another unproductive lower-margin search. A smaller error bound or adaptive mechanism remains separate.
LITERATURE_REASON: The positive-margin review exposes a distinct, previously untested size-versus-budget question; its source inputs are covered here before any derivation.
SCOPE: Actual Xi/Phi/C_y/A_0 of L898-L900, real x tending to either infinity, fixed 0<=y<1/2 with 1/4-y^2>0, and the positive constant K actually displayed in L900. No RH, simplicity, new zero-free bound, division by zeta or Xi near a zero, numerical K, or computational certificate.
COVERED_TARGET: Test whether |C_(1/2)(x)|/[A_0(1/2)(1+|x|)^5 exp(-pi|x|/2)] tends to zero as |x| tends to infinity and consequently whether L900's displayed sufficient test fails for every fixed positive squared-height transfer.

The main gap remains L030-L032/C032a. This test could retire an
insufficient transfer budget while leaving mixed positivity and every
different signed mechanism open. It is source specialization,
classified REPRODUCTION if completed, not creative mathematics.

## Exact standard inputs and applicability

S. M. Gonek, *Mean values of the Riemann zeta-function and its
derivatives*, Invent.Math.75(1984),123-141, Section2(20), p127:
for fixed integer nu>=0 and epsilon>0 the ordinary derivative bound
has exponent (1-sigma)/2+epsilon on 0<=sigma<=1, including sigma=1,
for |t|>=1/2. The complete Cauchy derivation paragraph was read;
it is unconditional. Only nu=0,1 and sigma=1 are needed; fix one
small epsilon independently of x. Reuse the source comparison in
2026-11-08-frequency-weighted-xi-defect-interpolation.md; this changed
target has separate coverage here.

NIST DLMF, inspected version1.2.8, release15 September2026:
25.4.3/4 give the functional equation and completion. Equation5.11.9
gives the gamma modulus asymptotic as its imaginary part tends to
either infinity, uniformly for bounded real part. Equation5.11.2
gives the digamma expansion in |arg z|<=pi-delta for fixed delta>0.
Read the conditions as well as both equations. At s/2=(1+ix)/2
these are large-height, fixed-real-part inputs; no gamma pole or
s=1 pole is crossed in the proposed asymptotic calculation.
Use the stated digamma input to differentiate the completion, rather
than differentiate an uncontrolled asymptotic remainder.

## Work reserved for the mathematical turn

1. Translate L898's P_y=y C_y at y=1/2 to a boundary expression
   involving xi(1+ix) and its first derivative, checking functional
   equation, conjugation, direction and factors. Use a product form
   throughout; no reciprocal estimate is required.
2. Apply the imported completion/gamma and Gonek ordinary-derivative
   bounds to the full product, retaining every polynomial and
   exponential factor. Explicitly compare the resulting power with
   power5. A mere exponential envelope of the same power is not a pass.
3. Divide only by the fixed positive real A_0(1/2). If the proposed
   limit is proved, compare it with the strictly positive fixed number
   K(1/4-y^2) in L900's sufficient test, including its sign convention.
   Distinguish failure of that **displayed sufficient test** from
   failure of the actual sign or of every bound admitted by L900.

Continue only with a rigorous little-o comparison for both signs of x.
If the exponent or normalization does not allow it, preserve the exact
failed estimate and reassess; do not substitute an assumed lower margin.
Even a pass supplies no explicit finite onset and does not exclude a
shrinking transfer or a bounded-frequency sign certificate.

Direct essential local inputs are L898, L899 and L900; earlier Xi and
theta conventions are inherited through them. L320 need not be
reproved; no new growth theorem is sought. The zero-free baseline is
overlap context, not a needed estimate for the asymptotic size test.
No cross-notebook input. Full matching Mathlib coverage is unchecked;
availability is unknown.

This newly written ready coverage receives separate supervisor
approval next turn. No mathematical attempt or theorem derivation was
performed in step119. The genuine creative blocker is still a payable
signed gain beyond the exterior; this test should not be labeled
creative merely to satisfy scheduling preferences.
