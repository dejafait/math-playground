# Approved spectral-block compression attempt728

Invocation-start assessment726/comparison727 is SPECIALIZE and its
COVERED_TARGET is the unchanged Next action. Main gap: L030-L032/C032a
actual-Xi positivity and signed S3. This attempt only prepares C998u's G
for a possible later full derivative-measure scalar; it supplies no sign.

Plan saved before construction: retain j=0 exactly; use disjoint blocks
j=2^k,...,2^(k+1)-1 for k=0,...,71 and omit j>=2^72 with the audited
uniform-tail majorant. Retain blocks with fewer than18 atoms exactly;
otherwise use17-node Gaussian quadrature. Bound rhohat>5 on each
artificial interval [2J,4J], J=2^k, whose endpoints are not atoms.
The Koyama bound summed over blocks is at most30*5^-34 before B^2;
this uses G(0)<5,16/pi<6. The tail contributes B^2/(4*2^72-3).
These rough bounds leave room for certified coefficient/rate errors.

Concrete construction being tested: normalized moments of the discrete
positive measure (1/J)sum_(j=J)^(2J-1) x_j^-2 delta_(x_j),
x_j=(j+1/4)/J in(1,2). Compute nonnegative powers by exact telescoping
power-sum identities; inverse powers by the inspected Euler--Maclaurin
formula with explicit periodic-Bernoulli bound, preserving both endpoints.
Use outward Decimal intervals, monic orthogonalization, sign-isolated
roots, and positive Christoffel weights. A numerical root guess alone
will not certify anything. Every non-enclosed step stops the certificate.

Continuation/abandonment test: B^2 sup_[0,ell]|G-Gtilde|<=1e-7,
strictly positive certified weights/rates, explicit rank, precision,
storage and construction work<=10^8. Count moment preparation and
validation; remain explicit if the operation model or bytes are unpaid.
Existing raw-prefix stop724 and the earlier implementation stops remain.
The remaining9e-7, density quadrature, h preparation, d0 C(0), other
entries/endpoints, C744q/H2 and Xi/global assembly remain unresolved.

Environment check: numpy available; flint/Arb, mpmath, sympy and scipy
unavailable in the current Python. Do not assume an external root solver
or install dependencies. The assessed orthogonal-polynomial construction
can instead be tested using interval coefficient evaluation and sign
brackets; completion is not claimed at this checkpoint.

## Completed attempt

Canonical proof and qualifications are in
[C998v](../lemmas/C998v-zero-inclusive-dyadic-gaussian-kernel-compression.md).
This is known-method specialization, not a new general theorem. The
analytic block/rank/tail bound and coefficient enclosures now supply a
1171-term positive approximation with weighted uniform error<7.353e-9.
It includes zero and pays only kernel approximation. All prior stops
remain specific to their recorded prescriptions.

At100 digits, naive interval orthogonalization lost enough precision
that p_17's endpoint signs were undecidable already for J=32; the
first-pass JSON retains that actual failure. At256 digits with256
logarithm-series terms, all67 blocks completed. The constructor retains
all moments, polynomials, norms, node/weight enclosures and output
constants. The exact Fraction replay checked all1139 Gaussian nodes
and passed4764 checks. Neither replay nor numerical preview proves
the analytic moment/source arguments; their full derivation is in C998v.

The original acceptance test is unfinished: the31,149,701 Decimal
arithmetic operations,19,229,836 selected comparisons and122,819
high-level Fraction calls are incomplete subtotals. Numpy root guesses,
integer internals, all assignments/control, allocation/output and the
exact replay lack a complete cost ledger. The saved constructor file
occupies10,038,511 bytes; this is not a memory upper bound. No affordable
construction, density quadrature or full scalar is claimed.

Continue the unchanged, already covered target by a separate conceptual
audit of C998v's moment/root/error claims and the all-work ledger. Retain
the successful constants and first-pass failure; do not rerun broad
searches or assume that rank implies affordable construction. Stop this
implementation if a complete ledger exceeds10^8, or park its unsupported
cost claim if essential work cannot be enclosed. The signed remote-plus-
induced S3 mechanism is still absent, so no justified creative central
target is nominated merely to satisfy scheduling preferences.
