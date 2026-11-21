# C761a — the fixed projected CCM trial misses the normalized observable test

## Hypotheses

Use the exact trial k and all241 projected coefficients v=P_120 k of
audited L761, in its common-scalar convention, with lambda=sqrt(13),
L=log(13). Use exactly the complex linear rows b, ell and the ground
vector xi of audited L760, at z=i/4; in particular b(xi)=1. No inversion
parity of v is assumed. The ground least eigenvalue is simple and even
as certified there. The upstream infinite-prolate mode, transport and
ground errors are retained in full.

This is a computer-assisted finite calculation. Assume exact Python
integer semantics and the upstream directed Decimal arithmetic contract
stated in L760/L761. It is not a formal verification of the interpreter.
Source definitions are imported from Connes--Consani--Moscovici,
*Zeta Spectral Triples*, [arXiv:2511.22755v1](https://arxiv.org/html/2511.22755v1),
Proposition5.9/(5.25), normalization before Lemma5.4, Theorem5.10,
and (7.2),(7.5)-(7.6); the compact extension is specified in Connes,
[arXiv:2602.04022v1](https://arxiv.org/html/2602.04022v1#S6.SS3),
sections6.3-6.4/(20), footnote20. L760/L761 justify their applicability
in this cell. No prolate theorem or source identity is reproved here.

## Conclusion

The projected trial boundary denominator is nonzero, with

    4.72968*10^-29 < |b(v)| < 4.72969*10^-29.

For the exact normalized discrepancy

    d=|ell(v)/b(v)-ell(xi)|/max(1,|ell(xi)|),

one has

    0.48616229937498 < d < 0.48616229937499.

Thus this trial fails the selected d<=1/10 discriminator in this cell.
This is negative evidence for this finite observable comparison, not a
disproof of a limiting trial theorem, Xi positivity, or RH. The trial
has not been fitted or replaced. Nonzero b(v) alone says nothing about
an unprojected L2 boundary trace or uniform control in either parameter.

## Proof

### Finite complex rows and complete input error

Write t=1/4, nu_j=2pi j/L, p=2sinh(L/8)/sqrt(L). Directly from the
cited Fourier row, for every -120<=j<=120,

    b_j=1/sqrt(L),
    ell_j=p(t-i nu_j)/(nu_j^2+t^2).

Indeed sin(i tL/2)=i sinh(tL/2), and multiplying
i p/(-nu_j+i t) by its conjugate denominator gives this expression.
These are bilinear coefficient evaluations; the complex coefficient
of v is not conjugated. Its definition already uses the conjugation
in the basis inner product. The odd imaginary row is retained.

Read every exact-trial rectangle from
`scripts/spectral-triples/ccm-trial-certificate-369.json` at
`/projection/exact_trial_coefficients`, and the complete ground interval
from `scripts/spectral-triples/commutator-certificate-364.json` at
`/row/fourier_at_boundary_normalized_ground`. The latter encloses the
real ell(xi), including the error in its very small boundary overlap.
Its value lies between2.32333*10^28 and2.32334*10^28, hence exceeds1.
L761 bounds the full projected mode/transport error below1.276*10^-91.
Each saved component rectangle already includes this error; the program
checks all component inflations against the saved polynomial rectangles
and this full error, with the exact zeroth imaginary component zero.
It never replaces coefficients by point diagnostics or assumes errors
independent. Rectangular interval inclusion is valid with correlated
errors; the resulting enclosure is conservative.

Sum all241 complex boundary and observable contributions. With
B=B_r+iB_i and E=E_r+iE_i enclosing b(v),ell(v), first enclose

    |B|=sqrt(B_r^2+B_i^2).

The resulting strict positive lower bound proves nonvanishing before
division. Only then evaluate

    E/B=((E_r B_r+E_i B_i)+i(E_i B_r-E_r B_i))/(B_r^2+B_i^2).

The denominator interval is positive. Subtract the complete ground
interval, take complex modulus and divide by its positive real value
(which equals max(1,|ell(xi)|) here). These enclosing operations prove
the two brackets in the conclusion. For scale, Re(E/B) is between
1.19381*10^28 and1.19382*10^28, whereas the ground value is as above.
The actual rectangle's possible imaginary component is retained through
the modulus. No boundary value of the unprojected error is evaluated.

### Arithmetic certificate and second evaluation

Reproduce from the active notebook:

    python3 scripts/spectral-triples/ccm-boundary-observable-373.py
    python3 scripts/spectral-triples/ccm-boundary-observable-check-373.py

Each writes its matching JSON, with complete directions, row intervals,
contributions, scalar intervals, checks, hashes and failures. The first
reports CERTIFIED_OBSERVABLE_MISS; the second reports
INDEPENDENT_OBSERVABLE_MISS_CONFIRMED. Both have no failures. The failed
1/10 mathematical threshold is recorded explicitly as a miss, not hidden
as a software failure or converted into a success by changing the test.

The first program uses integer endpoint intervals on the grid10^-340.
Saved decimal inputs are parsed as exact fractions and rounded outward
to that grid. Addition/subtraction are exact; multiplication and division
take extrema over all four endpoint products/quotients with integer
floor/ceiling. Division rejects an interval meeting zero. Squaring an
interval crossing zero uses zero as its lower endpoint; square-root
bounds use integer square roots of the scaled integer endpoints, rounding
the upper endpoint up when necessary. These rules inductively enclose
every exact operation. No floating point arithmetic is used.

The certified L and pi intervals are reused from L761. For sinh(a),
a=L/8 in (0,1), sum its positive series through degree199. The first
omitted term is a^201/201!; all subsequent term ratios are below1/2.
Twice the interval upper bound of this term therefore bounds the entire
positive remainder. It is added to the upper endpoint only. This
establishes the prefactor enclosure without assuming a transcendental
point value. All directions and both complex components are then summed
as described above, with the small denominator error propagated openly.
The certificate checks the hashes binding the upstream certificates to
their completed independent audits. It uses those audited results;
it does not replace their analytic proofs with success flags.

The second program extracts only the reviewed Ball interval class from
the earlier independent L761 audit, without executing that audit. It
uses260-digit floor/ceiling Decimal contexts instead of integer grid
arithmetic. It independently computes the prefactor as
(exp(a)-exp(-a))/sqrt(L), padding the correctly rounded exponential and
square-root endpoints by adjacent representable values. Thus its
transcendental path differs from the positive-series implementation.
It recomputes every row and contribution, sums all241 complex directions,
excludes zero before dividing, and independently proves the same two
coarse brackets and threshold miss. Complete corresponding intervals
are checked for intersection. Intersection is a consistency check;
the force of the verification is the enclosing construction in each
implementation and their independent strict brackets. Only Rounded and
Inexact Decimal flags occur; exponent-range and invalid-operation flags
are rejected. The second implementation still shares the audited input
certificates and stated software trust assumptions.

This is a finite specialization of known definitions and interval
methods. It adds a local discriminating result absent from the cited
passages, without claiming certified originality. The original96-mode
failure and112-mode success remain unchanged. Full-vector comparison,
uniform boundary control, simple-even family hypotheses, both N and
lambda limits, actual-Xi signs and RH remain open.

## Mathlib

Full matching coverage and supporting complex interval/Fourier coverage
were not checked. Unknown availability is not evidence of absence.
No Mathlib theorem or computation of zeta zeros is used here.
