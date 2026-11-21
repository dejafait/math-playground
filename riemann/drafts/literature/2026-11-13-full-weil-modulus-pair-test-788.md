# Complete Weil form: fixed disjoint-bump modulus diagnostic

TARGET: Test whether Delta=Q(u+v)-Q(u-v)<=0 for the complete actual-zeta Weil form on (-1,1), with u(x)=b(100(x+1/2)), v(x)=b(100(x-1/2)) and b(s)=exp(-1/(1-s^2)) for |s|<1 and zero otherwise, retaining both pole terms and every prime power.
CHECKED: 2026-11-13
DECISION: EXPLORE
SEARCH_EVIDENCE: Recovery review787 step788 compared hybrid, Gaussian and spectral/ground-state mechanisms and searched exact Weil modulus/positivity-preserving terminology; scoped Suzuki/spectral/ground-state/modulus records supplied no matching completed pair test. No originality or exhaustive absence claim.
SOURCE_EVIDENCE: L744(6) and C744m(3) give the complete smooth form, with source normalization already assessed in review492. Suzuki 2606.09096v2 introduction's Weil formula, (4.4)-(4.6), Sections5.1-5.3 distinguish the limiting form from the full one; 2610.32704v1 Theorems1.1-1.2 require RH. References and limits are in completed recovery review787.
COMPARISON: Positive limiting-form semigroup theory and a positive full quadratic form do not supply this signed modulus defect. Liu TheoremA already covers positivity at this support, so no new Q>=0 certificate is sought. The proposed test is a standard finite smooth specialization with all actual arithmetic terms, not an RH counterexample or a generic-model test.
GAP: Delta has not been evaluated. A fixed-pair sign cannot establish full modulus contraction, ground-state parity/simplicity, an approximation to Xi or signs on arbitrary supports. Semigroup interpretation requires separate criterion coverage if pursued.
REASON: This is an independently testable actual-form inequality beyond the stopped abstract Gaussian comparison and blocked event-cell interface. A strict wrong-sign defect would decide whether the proposed limiting-form extension can hold on this support, while leaving positive Weil energy intact.
SCOPE: Exactly the specified two bumps, half-width1, full unneutralized smooth Q, and the zero defect threshold; one attempt only after separate next-turn approval. No support sweep, neutralization, larger spectra, generic positivity theorem, semigroup conclusion or source-certificate replay is covered.

## Exact object and relevance

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
The candidate intermediate mechanism is sign control of ground states
by an order-preserving full-form semigroup. Before spending effort on
that mechanism, test its modulus comparison on this single smooth pair.
This is a proposed diagnostic, not an established sign or equivalence.

Define the actual Q by the complete formula in C744m(3), or equivalently
L744(6) after translation to (0,2), **before** any neutrality restriction:

    F_f(t)=integral f(x)exp(-itx)dx,
    C_f(d)=integral f(x+d)conj(f(x))dx,
    m(t)=Re psi(1/4+it/2)-log pi,
    Q(f)=integral m(t)|F_f(t)|^2 dt/(2pi)
         +2 Re(F_f(i/2)conj(F_f(-i/2)))
         -2 sum_(n>=2) Lambda(n)/sqrt(n) Re C_f(log n).

The bump b and u,v are exactly as in TARGET. Work with real tests
u+v and u-v, using zero extension. Verify compact smoothness and their
disjoint supports explicitly; no norm cap, cell boundary, parity or
neutral condition is imposed. In particular the poles must be retained.
If the physical-space Weil formula is used, retain its regularizing
scalar and integral subtraction until their cancellation is justified.

Use Q for the actual Riemann zeta function, not an adjustable spectrum
or a reference kernel. Enumerate every prime-power contribution allowed
by the two tests' support, and justify any vanishing correlation with
explicit support/logarithm bounds. Do not silently replace the form by
the limiting logarithmic form, delete poles, or assume a Fourier cutoff.

## One bounded mathematical discriminator

The proposed modulus contraction requires Delta<=0. Actual Delta is
uncomputed. Obtain a rigorous sign by exact integral identities and
uniform bounds on the entire relevant kernel, or a validated enclosure
including the full integral and all retained terms. A plot, a discretized
matrix, a Taylor preview or a sampled kernel is insufficient. Prefer an
analytic sign argument if available; no mathematical script is required
by this nomination. Import the stated Weil formula rather than reprove
the explicit formula.

If Delta>0 is certified, abandon the full-form modulus-contraction
extension on this support and record its precise failure; it would not
show Q(u-v)<0, nonpositive ground energy or an off-line zeta zero.
If Delta<=0 is certified, retain only the fixed-pair result and stop:
do not infer contraction for every f, or enlarge the family this turn.
If no sign is obtained with the full costs, save the exact remaining
bound and stop the attempt. Another unchanged evaluation is not a new
mechanism. No expected sign is supplied as evidence.

## Coverage, inputs and qualifications

Essential local definitions are L018, L744(6) and C744m(3). C744m's
external positivity theorem is an overlap comparison, not a premise
needed to evaluate Delta. The reviewed source formula holds for smooth
compact complex tests, hence includes the real pair without changing
hypotheses. The physical-space formula is printed in
[Suzuki2606.09096v2, introduction](https://arxiv.org/html/2606.09096v2#S1.SS1).
The limiting form in (4.4) and its Section5 argument are motivation,
not a substitute kernel. Source versions and primary-read limits are
recorded in review787, completed step788. No reproof of a known
positivity or semigroup theorem is needed for this scalar calculation.

Reused Gaussian/hybrid obstructions retain their scope. L057 prevents
a finite test from being promoted to all-degree positivity. Even a
successful ground-state mechanism would still need the full-domain
extension, convergence to actual Xi with multiplicities and a proof
of all required signs. None is assumed. There is no cross-notebook
input. Full matching Mathlib coverage has not been checked.

Classify the future finite-kernel calculation REPRODUCTION; neither
a failed search nor use of the actual zeta coefficients certifies
novelty. This newly written ready nomination must receive its separate
approval next turn. No mathematical result is derived or approved as
true in this literature-only step, and no creative routing is claimed.
