# Step 165: approved response-weighted second-moment comparison

The unchanged SPECIALIZE assessment is
`drafts/literature/2026-10-16-response-modulus-weighted-second-moment.md`.
The exact target is its TARGET, also recorded in the invocation checkpoint.
The main gap is global mixed positivity; this bounded diagnostic tests only
whether one added actual correlation excludes L421's fixed-g0 law.

Inputs read: L381 (7),(9),(12) and sharp bracketing; L389 (3);
L416's selected six moments; L419 (3)--(4); L421 (4)--(9), including
all high/intermediate/bulk components. The scoped step-163 audit and
radial-lift failure were checked. Neither gives this coefficient.

Completed result and full proofs are canonical in
[L422](../lemmas/L422-response-modulus-second-moment-separates-fixed-weight-law.md).
The actual coefficient is the positive absolutely convergent gcd sum;
the law coefficient is the fixed-g0 expression for every allowed k.
Both full response tails, sharp endpoints and all three law components
are retained. The separate critical audit remains pending.

The determinant comparison makes B_k nondecreasing. Certified rational
intervals put T strictly between B_13 and B_14, with distance greater
than 1/1000 from every integer-k coefficient. The script and full
certificate are in `scripts/discriminant/`, as specified in L422;
the preserved initial floating exploration is explicitly not proof.

The continuation test is met by a proved all-k mismatch, not merely
a convenient numerical choice. This ends this bounded calculation.
Its result supplies an additional constraint for later covariance-weight
design; no different weight has been constructed or approved here.
L421 remains valid for its original list. Clipping, the full-error
regulator margin and global mixed positivity are independently open.
