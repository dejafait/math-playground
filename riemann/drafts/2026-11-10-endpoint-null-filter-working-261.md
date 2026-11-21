# Endpoint-null filter working record — step261

Approved target: review259's exact normalized three-degree family and
fixed quartet, on the common interval [n,2n]. Classification intended:
REPRODUCTION. Main gap: actual-Xi signed positivity; this is only a
synthetic viability test, with arithmetic/criterion transfer unpaid.

Startup overview/DAG and source assessment reused; parent review258,
L985's exact connection, L987's checked finite-transform argument and
step233/235/244 stops inspected. No scope change or parameter sweep.

Checkpoint before longer reasoning: use the scaled uniform additive
asymptotic for all three degrees. Their limiting phase increments are
pi/3 at u=n and pi/2 at u=2n. The resulting real row planes intersect,
so a uniform lower bound for the leading cross product is not automatic.
Separate eventual exact nonvanishing from conditioning on favorable
integer subsequences. Neither is proved by this checkpoint.

Plan within the approved target: derive the explicit leading cross
product and the complete signed finite transform with errors retained;
test integer signs without assuming frequency independence. Preserve
all -1 corrections and the conjugate pair of real part1/4. Exact
definition on all sufficiently large integers remains an independent
obligation even if a favorable subsequence can be proved.

Continuation test: eventual definition, sufficient normalized errors,
and a positive exponential signed subsequence would pass the diagnostic.
Infinite exact degeneracy, proved zero rate or a rigorous normalization
obstruction would stop it. An uncontrolled phase collision leaves it
unfinished and is not evidence of a zero response or a failure of RH.

Further working checkpoint (not yet a canonical proof): the leading
rows are v=(cos(phi),cos(phi+pi/3),cos(phi+2pi/3)) and
w=(cos(psi),-sin(psi),-cos(psi)), with
phi=n*(sqrt(3)/2+pi/3)-13*pi/12 and
psi=n*(1+pi/2)-pi. If h=v cross w, then
h dot (sin(psi),cos(psi),-sin(psi))=cos(phi+pi/3).
Near (phi,psi)=(-pi/3,0), h=(-1,1,-1), so the surviving
transform has a positive sign because Re(1/((1/4+i*tau)^2+1/4))<0.
The orbit on each residue class modulo12 is two-dimensionally
equidistributed by Lindemann-Weierstrass and the checked Weyl criterion;
the quartet factor satisfies exp(2*i*tau*n)=exp(2*i*tau*psi)
at the prescribed even integer tau. Full remainder still to write.

Possible resolution of exact nonvanishing: the elementary three-term
Laguerre recurrence for p_j=L_j^2, applied to parallel shifted rows
b=lambda*a, gives p_n(n)=2-2/lambda and p_n(2n)=lambda-1.
Row norms force |lambda| comparable to exp(n/2), so both middle
polynomials are exponentially small relative to their bulk amplitude.
The M=2 source expansion would then give two zero phase conditions
with O(n^-2) error. Working first corrections are
gamma1=-55*sqrt(3)/432+45/(8*(3*sqrt(3)+2*pi)),
gamma2=-5/6+15/(8*(2+pi)). They imply integer A,B with
A=6*sqrt(3)*n/pi+12*gamma1/(pi*n)+O(n^-2),
B=2*n/pi+2*gamma2/(pi*n)+O(n^-2), hence
A^2-27*B^2 -> (125+810*sqrt(3)/(3*sqrt(3)+2*pi)
                         -405/(2+pi))/pi^2.
This proposed limit is nonconstant rational in pi over Q(sqrt(3));
transcendence would exclude an integer limit. Check M=2 coefficients,
signs and exact recurrence before promoting this reasoning. No source
expansion remainder is differentiated, and no numerical test proves
the asymptotic claim. Everything remains within review259's family.

## Completion and unresolved coefficient diagnostic

The rigorous first-order work and exact degeneracy reduction are now
canonical in L990. They prove rate1/2 on defined integer indices,
including an infinite positive subsequence, not cofinite definition.
The source-to-common-interval error and normalized coefficients are
controlled there; all quartet terms and -1 corrections are retained.

The proposed second-order proof above is NOT established. In the
displayed DLMF18.15.19-20 formula, taking the stated B_0 term and
J_2's first sine correction literally gives beta(t)=(B_0-15/8)/xi
and phase Phi-beta/nu. Expanding at degree n (nu=4n+6) gives the
two proposed gamma values above. A finite 90-digit Decimal recurrence
diagnostic, with a truncated pi value and no interval enclosure, is
saved in `scripts/endpoint-null-filter/phase-check-261.json`.
The complete ten rows were inspected. At the upper endpoint the
n^2 residual is about36.6356 for n512 and -73.1905 for n1024;
the latter finite inferred phase coefficient is -0.541033689,
whereas the proposed gamma2 is -0.468660337. These figures flag
a normalization/derivation discrepancy; they do not rigorously
refute a source asymptotic or prove the observed behavior persists.

The finite inferred coefficient is close to -13/24. Formally doubling
the displayed B_0 contribution would instead give gamma1=13*sqrt(3)/108,
gamma2=-13/24 and integer-norm limit169/pi^2. This is an unverified
normalization lead only, not a correction to the published theorem
and not an approved input to a nonvanishing proof. Preserve both the
original calculation and the discrepancy. A primary coefficient check
is now essential before this second-order branch can proceed.

The first-order statement in L990 uses only an additive O(1/n)
kernel expansion, so it does not use either proposed second-order
coefficient. No failure of that first-order argument is inferred.
Exact cofinite definition, actual-zero realization, other-zero control,
criterion transfer and both complements remain open. No whole RH
candidate, zero-rate stop, or normalization impossibility is claimed.
