# Six-pair closure working checkpoint676

Invocation-start EXPLORE assessment675 licenses only the six selected
pairs. No arithmetic, arbitrary-mode assembly or numerical service is
being claimed. Existing source coverage675/670 and audited C998g(6)-(8)
are reused. No external source search is needed for this bounded test.

Provisional mechanism: F_n(t)=integral cos(k_n s)/(t+s) ds,
L(t)=log((a+t)/t), r_n=F_n-L. For t>0,
r_n''+lambda_n*r_n=c_n/(t+a)^2+b_n/(t+a)-lambda_n*L,
where lambda_n=k_n^2,c_n=1-cos(k_n*a),b_n=k_n*sin(k_n*a).
Subtracting L before integration by parts removes the common t^-2
forcing. r_n and its first derivative have finite limits at zero.

To finish: prove the cutoff Wronskian identity and its parameter
derivative for diagonals; integrate all remaining single-output moments
out into fixed weights Q(s),A1(s),A2(s). Q must be specified explicitly
by elementary logs and a one-variable logarithmic primitive, rather
than hiding a product of two Carleman outputs. Check all six formulas,
endpoint traces and normalization before writing a canonical result.

The completed reasoning is now canonical in C998h, Section4 for
cutoffs, Section5 for the two Wronskian identities and Section1 for the
explicit shared weights. Provisional expressions here are superseded
by that full proof, not additional established inputs. Algebra checks
included the sign before D(1/z), the orientation of W_nm, differentiation
with respect to k^2 and the n*pi/2 parity coefficient table. No numerical
check was substituted for those identities. Independent audit is pending.
The original entry error<=1e-10 and work<=20m remain entirely unproved.
All signed/global RH gaps remain open.
