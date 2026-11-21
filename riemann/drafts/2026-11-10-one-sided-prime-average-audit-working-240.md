# L984 conceptual audit — working record, step240

10 November 2026. The gate-approved target is exactly review238's
L984 audit, with source approval completed in step239. This is a
RESEARCH/proof_audit, not another source-approval turn. The supplied
overview and DAG were used before the detailed L984/L018/L980-L982
reads. Existing unrelated notebook changes are preserved.

Main gap: no independent one-sided bound (H) for the actual prime
averages, and no actual-Xi mixed positivity. Intermediate target:
verify the conditional interface in L984. Downstream use: a checked
sufficiency test for a later arithmetic estimate. Accept only with
all finite-cutoff, normalization, sign, prefix, multiplicity, radius
and same-germ obligations discharged; record any essential failure.

Partial audit reasoning saved before continuation selection:

- L981 is uniform over all real upper endpoints; the fixed-index
  limit in L982 can therefore be taken separately for each k.
  Triangle inequality gives 2*t_k at X_n; summing finitely gives
  2*T<=4*exp(-630), including n=2 and full prime-power endpoints.
- The exact split has -S_f and +1. The upper estimate for the sum
  of S_f consequently gives a lower estimate for c_n. The polynomial
  smooth trend, including its finite prefix, is paid with epsilon/2.
- H(0)=1. Differentiating the local ordinary-Li logarithm and
  subtracting lambda_1*z gives the stated cumulative coefficients.
- A minimal interior zero exists by compactness and isolation.
  Its pole residue in F is m*w/(1-w), nonzero for every m>=1.
  The quotient is regular at positive R because xi is nonzero for
  real s>=1. It is the same quotient on the overlap with the Taylor
  disk, so continuation is of the original germ.
- The correction has radius sqrt(R)>R, preserves the pole and makes
  every coefficient nonnegative, including the two initial zeros.
  Pringsheim therefore applies without a global logarithm or an
  infinite degree/cutoff limit interchange.

No failed essential step found so far; canonical audit write-up and
final documentation checks remain. No mathematical script is needed.
The arithmetic bound remains unpaid. Required different continuation
will be nominated as REVIEW_REQUIRED if it leaves the approved scope;
no new mathematics will be derived or approved during this audit.
