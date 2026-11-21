# Complex kernel attempt1851 — working record

Approved target: test Re K(z,w)<0 for Re z,Re w>=13 and
|Im z|,|Im w|<=1/2, exactly C034d(29). Reuse EXPLORE
assessment1850 and source-notes1850; no new source scope or contour
transfer. Main gap: L030-L032/C032a actual-Xi all-degree positivity.
Possible use: a signed retained-core contour integral, with its actual
deformation, origin/cutoff remainder and C034c(20) still unpaid.

The test must cover both unbounded real coordinates, all independent
imaginary signs and finite edges, or exhibit a certified violating
pair. Finite sampling or inconclusive coefficient bounds do not decide
it. Preserve stops1847/1843/1839 and their earlier cited evidence.

Read C034d in full, including its audit, C034c hypotheses and (16)-(20),
source-notes1850 and the three immediate stops. No duplicate exact
complex sign is reported by the reused assessment. C034d's real
monotonicity is not usable for independent complex arguments.

Proposed bounded certificate: t=z^2, u=w^2; clear the exact rational
denominators, inspect the numerator coefficients (possibly after a
fixed positive real shift), and bound the argument of each rational
monomial on the full domain. This is algebraic sign certification of
the already covered target, not a general positivity theorem or a
contour identity. No result is asserted yet. The local python3 has no
SymPy; use exact integer polynomial arithmetic rather than a new
package. Save the full coefficient certificate and inspect every
load-bearing value before claiming a sign.

Standalone inputs: only C034d's rational definition and ordinary
complex derivatives. Downstream actual-divisor, multiplicity,
conjugation, ordinate0 exclusion, gamma>14, strict strip, count,
through100/retained real zero, reciprocal-square tail, heat/fixed-j
errors, both fixed-v1 qualifications, zero drift/killing and Gaussian
half-variance remain unchanged. No RH, profile positivity, global
Sobolev membership, contour cancellation or Xi realization is assumed.

First exact evidence: with H(t)=t^2(t+1)^4(t+2)^4, clearing
denominators gives -K=96 P(t,u)/(H(t)H(u)). The raw numerator
has twelve negative coefficients, so a direct positive-coefficient
test fails. After t=T+1,u=U+1 the complete 9x9 coefficient matrix
has exactly one negative entry, -100 at (7,7), with +105 at both
(8,6) and (6,8). All other entries are nonnegative. Full matrices
and the negative-entry list have been inspected in certificate1851.

Candidate completion (not yet independently audited): Re T>=671/4
and |arg T|<=52/671. For c=1,2,3, arg(T+c) has the same sign
and magnitude between (4/5)|arg T| and |arg T|. Thus each factor
T^i/H(T+1), 0<=i<=8, has an angle of magnitude at most
(10-i)|arg T|. All nonnegative terms have angle at most
1040/671<31/20, giving positive real part; the three exceptional
terms have angle at most312/671<1/2. Their positive pair has
real part > (7/8)*105*(|T|^8|U|^6+|T|^6|U|^8)/|H H|,
which dominates100|T|^7|U|^7/|H H| by the elementary square
(|T|-|U|)^2>=0. Need exact derivative/cross-multiplication checks,
an explicit positive cosine bound, all denominator checks, and a
canonical proof. No numerical sampling is used.

Completed: the full proof and exact whole-domain margin are now canonical
in [C034e](../lemmas/C034e-complex-strip-rational-kernel-sign.md).
All20 finite algebra/scalar checks pass, and complete load-bearing
matrix, identity differences and rational bounds were inspected.
The result is pending separate critical audit; no contour/curvature
closure was attempted. The working evidence above is retained as the
attempt record, not a second canonical proof.
