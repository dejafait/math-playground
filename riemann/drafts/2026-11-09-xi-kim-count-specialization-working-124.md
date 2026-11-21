# Step124 working checkpoint: Xi finite-rectangle count

The exact step114 SPECIALIZE target is active. This is a mathematical
theorem application, not a new literature assessment. Inputs read:
L018, L023, L024; L957 statement and endpoint proof/audit; Kim1996
definitions pp819–820, Theorem1 p821 and Section2 pp822–823. The
step123 source/failure comparison is retained. No global finite
nonreal census, RH, simplicity or sign estimate is assumed.

Genus at most one follows from L024's Hadamard representation, hence
genus1* with quadratic parameter zero. Jensen containment in Kim
Section2 puts every nonreal Xi' zero inside a closed disk of radius
strictly less than 1/2. Thus the strip-wide counts equal counts in
the fixed-height rectangle. A vertical line through a disk-free real
endpoint misses every disk. Any disk meeting the rectangle has its
real diameter strictly inside (a,b), so its radius is also <(b-a)/2.
This identifies Kim's rectangle with the same counted zero sets.

Boundary reduction still being checked: L957 excludes Xi zeros but
does not exclude Xi' zeros. With q=Xi'/Xi, differentiate L024's
locally convergent logarithmic derivative. At a real point outside
the closed disk union every real-zero term of q' is negative and
every conjugate-pair term is negative. Xi has at least one zero:
otherwise its even order-one product would be constant, whereas
the completion at positive even integers grows without bound.
Therefore q'<0 there. An endpoint zero of q is simple, crosses
downward, and has Kim critical multiplicity zero.

Pending algebra: let e_a,e_b be endpoint Xi' indicators, N,N' the
closed-interval real counts, and B0=(sgn0 q(a)-sgn0 q(b))/2. Moving
the endpoints inward gives interior signs s_a=sgn0 q(a)-e_a and
s_b=sgn0 q(b)+e_b, interior derivative count N'-e_a-e_b, and
B_in=B0-(e_a+e_b)/2. Consequently the expected closed-count term
is B_closed=B0+(e_a+e_b)/2, with
2K=N'-N-B_closed and N'+2J'=N+2J+B_closed.
Verify before canonicalizing. This would yield K=J-J' and identify
K=0 as the unproved one-step no-loss threshold, not as RH.

Next within this attempt: finish the endpoint multiplicity and
local-finiteness justification, then write one canonical known-method
specialization if they pass. No mathematical script is needed.

## Completion

The preceding working checkpoint is preserved. The endpoint algebra
and local-finiteness checks passed and are now canonical in L958,
including the effective closed-count term B_closed. This completes
one known-method theorem application, pending a separate conceptual
audit; K=0 and higher/global transfer remain open. PROGRESS contains
the sole current next action; the working plan above is historical.

Validation: `python3 ../scripts/docs/check_structure.py --problem riemann`
passed with 1058 nodes and 2599 unique edges, complete local file
coverage and acyclicity. The scoped tracked-file whitespace check
also passed. Direct mathematical review matched the four L958 DAG
inputs to genus, actual-Xi strip/product and endpoint existence;
contrast and goal references add no dependency. Structural checks
do not validate the imported theorem or the endpoint proof. No
mathematical script or numerical certificate was used.
