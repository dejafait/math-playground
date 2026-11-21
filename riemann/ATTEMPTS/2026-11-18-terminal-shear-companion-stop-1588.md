# One terminal shear: compression payment stop1588

The approved test was the exact family
B=D(I+t E_(d,d-1))A_d(I+t E_(d,d-1))^(-1)D^(-1), with arbitrary
positive diagonal D and real t depending on d. The full finite proof is
[C028i](../lemmas/C028i-terminal-shear-companion-compression-floor.md).

WHY IT FAILS: The new skew cross terms cancel in their squared sum.
After minimizing the positive diagonal ratio x, the substitution
k=sqrt(1+t^2*y^2), r=y/k reduces its lower bound to the existing
unsheared cost, with additional nonnegative terms. Consequently the
last-three compression has exactly the same optimized minimum as
C028h and the same fixed c*d floor for every d>=3. The full cost is
at least this compression, so this single shear cannot supply o(d).
This does not lower-bound actual root heights. It stops neither general
similarities nor RH. C028h's earlier diagonal-only stop remains intact.
The new specialization is pending an independent finite audit.

Audit1590 (2026-11-18): the separate full hand replay in C028i passes
without correction, including exterior support, inverse/order, skew-norm
factor, unrestricted substitution and every equality case at d=3 and
above. The specified stop is now audited and parked. The original
pending label above records its status at construction. No broader
similarity obstruction or lower bound on actual heights follows.
