# Negative-middle near degree — bounded proof attempt

Approved target: Test whether C464b remains valid with M_nr replaced by the near degree from conjugate blocks satisfying |gamma-t|<d, while M and U_t remain unchanged.

The invocation-start assessment is
`drafts/literature/2026-10-26-negative-middle-near-degree-coverage.md`
(SPECIALIZE). The main gap remains initial actual-Xi signs at unbounded
heights and global mixed positivity. This attempt could make future
control of only the geometrically offending near blocks useful for an
upper-tail estimate; it supplies no such control or initial signs.

Read all of L464 and C464b, C464b's audit working record and the
zero-block compensation failure. Reuse their source comparisons. Only
L464 is needed as a non-elementary input: its exact positive-scalar
factorization and abstract coefficient comparison suffice. This is a
REPRODUCTION specialization, not a new product mechanism or a claim
of originality. The old low-order compensation obstruction is retained.

Checkpoint before completing the proof: split the finite near polynomial
as A H, putting real blocks and conjugate blocks with |gamma-t|>=d in
A. Their coefficients are nonnegative, including equality; A is monic
of degree r=M-K_t. H has degree K_t and root bound 17/4. For every
shift j in [0,r], the comparison denominator is
`p-j-K_t+1 = p-M+(r-j)+1`, so the proposed threshold appears to
suffice simultaneously. The leading coefficient of A supplies the
strict summand. Check K_t=0 separately and retain the original far
product throughout. Abandon or narrow if any shift or degeneracy needs
an extra sign premise or changed U_t.

Completed: C464c contains the full specialization proof. Every shifted
comparison satisfies both degree and denominator requirements with the
original U_t. Equality blocks remain in the nonnegative finite multiplier;
K_t=0 and M=0 use a direct convolution, and central zeros cause no
normalization division. No extra hypothesis was needed. This establishes
a local parameter-sensitive tail bound, without an improved count or
initial signs. A separate critical audit is still pending; no script
or numerical sampling was needed for this exact finite argument.
