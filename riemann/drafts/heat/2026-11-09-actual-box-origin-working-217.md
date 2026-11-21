# Fixed-box origin test, step217

Invocation-start EXPLORE gate:
`drafts/literature/2026-11-09-actual-box-origin-feasibility-test.md`.
The supplied assessment has been read. Reuse its Laurent citations and
L921's separately audited finite algebra; no new literature is needed.

The main gap is L030-L032/C032a mixed positivity. This attempt tests
only the fixed panel0 outer ratio boxes at a stipulated d=2 contact.
Infeasibility or J>=0 could screen L918's origin residual. Independent
compact residual/flux, initialization and global gaps remain unpaid.

The one fixed calculation will form exact rational ratio intervals
from all fourteen saved endpoints, then interval-enclose the unchanged
finite logarithm/inverse polynomials. If the leading logarithmic
block has positive determinant Delta, the first two null rows give a
direction proportional to

    v=(S3*S5-S4^2, S3*S4-S2*S5, Delta),
    Delta=S2*S4-S3^2.

This uses no c0/c1 division and no inverse unless Delta>0 is proved.
Every unit full null vector must then be +/-v/sqrt(v.v), and J has
the sign of v^T K v, K_ij=(i+j+2)a_(i+j+2)+a_(i+j+1).
The third row, all PSD constraints, boxes and c2!=0 are retained in
the target: proving a sufficient bound without them would be sound,
whereas ignoring them cannot validate a negative witness.

Stop at the first decisive interval that remains unsigned. Do not
refine, subdivide, sweep, change normalization or restore theta
correlations. A failed sufficient sign bound is inconclusive, not a
counterexample. Save full exact arithmetic and all failures. Only a
complete accepted certificate/witness warrants continuation of this
fixed target. L917/L922 determinant stops and L921's unboxed negative
witness remain preserved.

Inputs: L019/L037/L058/L874/L917/L918/L921; panel0 of
`scripts/heat/low-time-h2-uniform-195.json`. Decimal correctness is
inherited only for the original enclosures; Fraction operations here
are exact. No actual contact or representing measure is assumed to
exist. L918's complete residual argument remains unaudited. Mathlib
matching/supporting coverage is unchecked. No cross-notebook input.

## Completed fixed calculation

`python3 scripts/heat/actual-box-origin-217.py` saves complete rational
evidence in `scripts/heat/actual-box-origin-217.json`. It parses the
fourteen endpoint strings as Fractions, saves them verbatim with the
source hash, and divides exactly as stipulated. The input is M_(2k),
not the stored factorial-normalized coefficients. Only after forming
the independent y boxes does it set e_k=y_k/(2k)!.

The formal coefficient polynomials are the unchanged L917/L921 ones.
The program checks all six logarithm polynomials against the finite
power-series logarithm and all seven reciprocal convolution residuals;
all residual polynomials vanish. Evaluating these fixed polynomials by
exact rational interval addition, multiplication and integer powers
includes every point of the independent box. No binary float, new
theta integration, domain subdivision or point substitution is used.

The leading block passes: S2 is inside [3.7143e-5,3.7205e-5] and
Delta is inside [9.71e-16,6.75e-15], with both lower endpoints
strictly positive. L921's audited null-row reduction, equivalently
Cramer's rule for that certified invertible block, gives the v direction
specified above. Its third entry is Delta>0. Thus every target contact's
unit c has that direction up to sign, without a bound on |c2| or a
division by c0/c1. This is a consequence of the first two rows only;
the third row and all PSD hypotheses remain restrictions of the target.

The program groups v^T K v into the three diagonal terms K_ii*v_i^2
and the three terms 2*K_ij*v_i*v_j for i<j. The squared interval rule
retains zero when an interval straddles zero. It adds all six bounds,
and separately bounds v.v. The complete saved endpoints satisfy

    -8.897e-38 < lower(N) < 0 < upper(N) < 1.328e-37,
    9.44e-31 < lower(v.v) <= upper(v.v) < 4.557e-29.

Here N=v^T K v. The required lower(N)>=0 fails. Full endpoint signs
and comparisons against these exact rational short brackets are saved
in `signs_from_complete_endpoints` and `verified_short_brackets`; they
were checked in full, not inferred from an output preview. A direct
dump of the large `/bounds` field truncated and was not treated as
verification. The program compares the complete values on disk.

This stronger sufficient test would have proved J>=0 using fewer
premises if its lower bound passed. Its failure decides neither the
full three-row feasible set nor J on that set. In particular the negative
interval endpoint is not an attained value, and no feasible or negative
witness, actual contact, or infeasibility certificate has been obtained.
This is one mathematical EXPLORATION attempt, not an informative
negative theorem. Stop this fixed attempt without tuning. The previously
saved L917/L922 and L921 stops are unchanged. No new canonical lemma
or change to the argument in PROOF.md/DAG.md is warranted.
