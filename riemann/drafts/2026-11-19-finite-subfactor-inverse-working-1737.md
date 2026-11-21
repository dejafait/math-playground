# Finite-subfactor inverse working record1737

Approved target: test the signed inverse of the restriction of C032j's
ell_1(t)dt to I=[1,3/2], for positivity reflection by the qualified nu_1.
Reuse SPECIALIZE assessment1736 and source-notes1736, without new literature.

Main gap remains actual-Xi all-degree positivity. A counterexample would
stop automatic positivity pullback through nu_1 in a common-factor/tail
approach; continuum factorization, the tail argument and Xi realization
would remain separate. Continue only if finite variation, mass one,
a negative Borel witness and all-Borel positive output all hold.

Construction to check: P=1_I ell_1(t)dt, m=P(X). Levy integrability gives
m<infinity; strict positivity of ell_1 gives m>0. For the imported
measure exponential E, pi=exp(-m) E(P) and
lambda=exp(m) E(-P). Total variation is at most exp(2m), mass one.
The n-th convolution is carried by [n,3n/2]. Hence only n=1
contributes on I and lambda(I)=-exp(m)m<0.

Residual Levy measure R=ell_1(t)dt-P is positive with the original
min(1,t) integrability. Bertoin supplies its zero-drift, zero-killing
probability mu. Positive-measure Laplace uniqueness gives nu_1=pi*mu.
The imported signed inverse identity lambda*pi=delta_0 then gives
nu_1*lambda=mu by finite-signed convolution associativity. This avoids
using a positive-measure uniqueness theorem directly on signed inputs.

Checks remaining at save: state every retained external qualification;
explain the reflected Trabs convention; distinguish lambda on X from
width eta on W; record the exact citations and complete all-Borel
justifications in canonical C033i. No claim of original discovery,
full cancellation, moments, continuum factorization or RH is intended.

Completed in canonical C033i in this step, with the listed checks
written out. Result: conditional counterexample to unrestricted
positivity reflection, pending separate critical audit. No abandoned
or unfinished earlier reasoning was discarded.
