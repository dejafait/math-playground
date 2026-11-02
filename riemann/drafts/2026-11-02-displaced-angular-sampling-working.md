# Exact signed angular observation: bounded attempt

Invocation-start gate: `literature/2026-11-02-displaced-signed-angular-sampling.md`
(EXPLORE), unchanged target. The main gap is actual-Xi mixed positivity
and unbounded-height signs. The intermediate target is the uniform
displaced-family inequality H >= (log D)/2-n/32+log n-C. Its downstream
use is L658's paid arc; arbitrary support, realization and signs remain
independent gaps.

Keep L649's full rational product and original unit residues, n=12q+3,
q>=1, H_0=27/(10n), nonanchor ordinates H_0*(m+1/2)+epsilon_m for
-2q<=m<2q, independent real |epsilon_m|<=H_0/8, and the fixed anchor.
All M=n/3 spatial moments remain in G and the squared-residue diagonal
D remains exact. L664 Section 5 supplies H>=log max|c_0| when c_0 is
nonzero; this does not require symmetry of the displaced set.

Bounded test: seek an exact signed rational observation lower bound
max|c_0| >= c*n*exp(-n/32)*sqrt(D), or a proved obstruction to the
specific observation transfer at that budget. L661's audited envelope
is available for comparison, not a substitute diagonal. No exponential
surrogate, positive cross-entry claim or unproved logarithmic L2
transfer is permitted. L649, C645o, L650 and L665's distinct stopped
methods were checked; L665 is a contrast, not an audited new premise.

Initial checkpoint: examine the common angular poles and exact rational
observation before selecting a signed estimate. No response bound,
countersequence, or general sampling application has yet been proved.

## Partial reduction saved before the numerical test

Put J=n-1, p_j=t_j*x/U, and include in the quadrature's interior
pole completion 0, all p_j, and t_j/conjugate(a) for every nonanchor
a and 1<=j<n. All these points are distinct: the p_j are real,
the other points are nonreal, and equality of two latter points forces
their t_j to agree by comparing real parts of the reciprocals, then
their a to agree. Their moduli are below 4/5. There are K=1+MJ points.
The exact rational W_a has only simple possible poles at p_j and
a/t_j, is finite at 0 and infinity, and has no unit-circle pole.
The original anchor term is W_x=1; cancelled poles need not be restored.

Consequently Danchenko--Semin v1 Theorem 2, r=s=1, applies to W_a
and their combined c_0, with the same completed pole set. It gives
weights w_l=1/(2*mu(z_l)) at the 2K roots B(z_l)^2=exp(i*phi),
and exactly E_0=sum_l w_l |sum_a W_a(z_l)/R|^2 and
D=sum_l w_l sum_a |W_a(z_l)|^2/(U-|a|^2). Taking F=1 gives
sum w_l=1. This is a signed observation identity, not coercivity.
The full specialization and hypotheses are now canonical in L666.
No primary theorem is reproved.

The bounded numerical test will optimize independent permitted shifts
against E_0/D using the actual finite products, then check denser angular
sampling and the common rational quadrature. All such floating-point
values are diagnostics; no asymptotic bound or interval certification
will be inferred. The target squared benchmark is n^2*exp(-n/16),
up to a uniform positive factor. The maximum of |c_0| may still be
larger than its L2 norm, so failure of this sufficient norm test would
not by itself refute the scalar maximum or H.

## Completed bounded test

The canonical proof and exact citation are in
[L666](../lemmas/L666-displaced-signed-rational-angular-observation.md).
Its sampling specialization preserves the combined signed c_0 and
exact D, with 2+2M(n-1) observations and normalized positive weights.
The still-missing coercivity estimate is L666 (5); the identity alone
does not provide a rate. This is a reproduction of a known theorem's
specialization, not a new sampling lower bound or certified novelty.

The full finite diagnostic and reproduction command are in L666
Section 5. Both independent-displacement starts were run for each of
n=27,51,99. Rational shifts, optimization traces and all quadrature rows
are retained in `scripts/one-sided-hankel/displaced-signed-angular-sampling.json`.
The L2/benchmark ratios are approximately .00530, .00766, .01241;
these cannot decide an unspecified uniform c or onset. Dense sampling
and exact-formula quadrature agree numerically, with no diagnostic
failure. Their floating arithmetic, finite optimization and sampled
maxima are expressly not a rigorous certificate.

Outcome: EXPLORATION. No uniform response bound or countersequence was
proved, and no numerical value enters the canonical proof. One
mathematical exploration turn has been spent on this sampling mechanism.
The source coverage remains ready and unchanged. An analytic estimate
of the signed unit-residue sample ratio, uniform in n and all allowed
shifts, is the unresolved continuation within the same approved target.
Repeating finite screens alone is not a sufficient continuation.
