# Grouped-ratio certificate: unfinished checkpoint

The approved target is the complete L481 ratio polynomial, with L477's
fixed cutoff M=floor(sqrt(T/(2pi))). No frequencies may be removed.
The relevant ready assessment is
`literature/2026-10-31-grouped-ratio-nazarov-certificate.md`.

Working reduction, not yet accepted: reduced ratios r=a/b have positive
coefficient log(r)^2 H_floor(M/max(a,b))/sqrt(ab), with r=1 absent.
For M>=5 the proposed exact logarithmic minimum gap is
g=log((M-1)^2/(M(M-2))). Prove this by separating cross-determinant
one from determinant at least two. The two near-unit fractions attain it.
Then H=Tg/(2pi)=1+Theta(1/M), uniformly in the floor remainder.
The source's excess-length loss cannot be replaced by a fixed constant.

The proposed ascending-rank coefficient sum has scale
Theta(M^(-1/2)(log M)^3). Lower bound: the first roughly M/2 ratios
are 1/M,1/(M-1),..., with comparable coefficients. Upper bound:
handle r<4/M by a harmonic sum and a uniform coefficient bound;
prove rank(r)>=c M^2 r for 4/M<=r<=1/2 by counting coprime pairs
with numerator <=rM/2 and denominator >=M/2. Use
sum_(a<=A) phi(a)/a>=A/4 from the elementary prime union bound.
For r>=1/2 the rank is >=cM^2. All estimates and endpoints still
need a complete written check.

If these calculations hold, the full-interval source certificate has
scale Theta(M^(-6)(log M)^3)=Theta(T^(-3)(log T)^3), far below
T(log T)^3. This would stop only this certificate, with no upper bound
on the actual ratio L1 norm and no assertion about chirped cancellation.
Next routing must be nominated separately; no future target is approved
by this unfinished reasoning.

Completed later in the same step: the full analytic checks and all
endpoint/rank/rescaling details are now canonical in L572,
`../lemmas/L572-grouped-ratio-short-interval-certificate-stop.md`.
The predicted certificate scale holds; this scratch checkpoint is
preserved as unfinished reasoning at the time it was saved, not as
an additional proof or an independent audit.
