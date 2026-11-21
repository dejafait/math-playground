# Enlarged finite theta domain: formal inverse stop

The complete proof is [L906](../lemmas/L906-finite-theta-domain-formal-inverse-fails.md).
This is a source specialization and a local domain obstruction, not an
RH counterexample or a new positive realization.

WHY IT FAILS: On V=span{w,Dw}, the kernel representative w satisfies
Lw=0 but LDw(1)>1/6. Consequently T(Lu)=-LDu assigns different outputs
to the same input represented by 0 and w. Smoothness and rapid endpoint
decay do not remove this explicit ambiguity. The one-point test uses
the source's defining series, all differentiated tails, and inversion;
it does not rely on the source's printed small-t asymptotic bound.

Retire this prescription on V. Reopening needs a materially different,
specified domain or representative selection whose well-definedness
and spectral applicability can be independently tested. No inclusion
V subset H_finite is proved; restricted inverses, H_finite, nonlocal
metrics and other domains are not ruled out. Step144 independently
audited L906's source normalization, signs, complete differentiated
tail, endpoint proof, exact certificate and representative argument;
the scoped retirement survives that audit.
