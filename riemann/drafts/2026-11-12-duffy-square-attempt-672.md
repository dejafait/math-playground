# Duffy square-service attempt672

Completed under unchanged SPECIALIZE assessment670. Main gap is
L030-L032/C032a actual-Xi positivity and signed S3 coupling. The one
approved intermediate target is a finite-cell square contribution with
entry error<=1e-10 and scalar work<=20000000. It could support a later
full residual-Gram/inverse ledger; the other products and signs remain open.

C998e(6)-(8) has been checked against C998a's exact parity map and
C999q's exact neutral completion: partial fractions, the two conjugated
mixed terms, absolute triple-integral domination and the first-slot-linear
projection convention agree. This is a scoped audit, not approval of
all C998e bounds or its inverse/service claims.

Working specialization: split the square into s>=u and u>=s and put
s=ax,u=axy. The transformed kernel is
W(x,y)=[-log(y)-log((1+x)/(1+xy))]/(1-y), equivalently the integral
of 1/[z(1+xz)] with z=y+(1-y)t, 0<=t<=1. The latter expression
controls y=1 without subtracting nearby logarithms. The real trace has
W>=0 and W<=-log(y)/(1-y). Both parity products and the factor a/4
must be retained. This derivation and its bounds still need canonical
write-up and exact finite checks.

One proposed rule only: omit 0<y<2^-48; use radial (321-point) Gauss
on [0,1], and (n_j+1)-point Gauss on y in[2^-j,2^(1-j)], j=1..48,
n_j=32+ceil(144*2^-j). Use rho=2 for uniform one-variable ellipse
bounds, real traces rather than conjugation of complex arguments.
Proposed finite precision is 256 fractional bits; constants, weights,
nodes, scalar enclosures and their propagation are not yet paid.

Pre-batch discriminator: the direct coefficient contraction evaluates
all six exact parity densities at each scaled abscissa a*x*y, sharing
cosine bases and caching all unscaled a*x values. Count the nonzero
coefficient multiplications alone before attempting scalar evaluators.
If this mandatory count already exceeds20000000, stop this prescription
without a batch, sweep or claim of universal complexity. Preserve657,
660,662. No full residual size, inverse debt, S3 sign or RH claim.

Inputs: C998a/audit655, complete654/655; C999q exact Z; frozen652 pin
2b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6.
C998f/audit669's separate setup reserve is not used in this square count.
Inherited analytic/arithmetic/source-to-Xi/whole-core/c_* contracts and
all other full-Gram, higher/mixed, H2 and global gaps remain unresolved.

Completion: the full proof is now canonical in C998g. The exact rational
planning certificate672 passes its finite checks and establishes the
prescribed432945540-multiplication work failure. It does not execute
quadrature or establish any finite-arithmetic scalar/node/weight error.
The earlier working obligations above are retained as the attempt record;
the canonical result distinguishes the proved analytic ledger from the
unpaid finite implementation. Next mechanism requires new source review.
