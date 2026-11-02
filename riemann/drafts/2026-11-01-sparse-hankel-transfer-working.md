# Sparse Hankel principal-part application — working checkpoint

Approved target: Establish the full principal-part reduction and boundary lower bound for C645g's sparse positive-residue family under exact grid interpolation.

Invocation-start coverage is SPECIALIZE in
`drafts/literature/2026-11-01-sparse-hankel-principal-part-transfer.md`.
Main gap: actual-Xi signs/all-degree mixed positivity. This bounded
synthetic bridge does not supply an actual census, realization or upper
bound. Existing unfinished notebook work is preserved.

Planned applicability argument: put A(z)=B_n(x)(F(z)-P(z))/B_n(z).
Every grid zero of the denominator is simple; exact interpolation gives
a numerator zero there. At each genuine simple pole a, the residue is
r_a B_n(x)/B_n(a). Subtract Q(z)=q(z/R), retaining q's 1/R;
all these principal parts cancel. The remainder should extend
holomorphically to a neighborhood of the whole closed disk, hence its
rescaling is a bounded analytic multiplier of every H2 input. This
would give H_g=H_q, not just equality on the constant input.
Then ||H_q||<=||g||_infinity=|B_n(x)| max|F-P| gives the proposed
threshold by C645g. This is pending verification, not an audit verdict.

Checks to finish: complete pole list and boundary collar; all n grid
nodes including zero; exact transformed residues and anchor modulus;
bounded analytic remainder (no uniform bound required); arbitrary H2
inputs; one-sided operator-to-symbol comparison. A surviving singularity
or failed multiplier premise stops this application. C645f's factor
calculations are comparisons; its restricted family theorem is not an
input for the larger census. C645d's scalar cancellation is preserved.

Completed: the local proof is now canonical in
`lemmas/C645h-sparse-hankel-principal-part-boundary-transfer.md`.
It checks all grid nodes and genuine poles, the neighborhood extension,
the multiplier for every H2 input and the exact one-sided norm comparison.
The stated transfer and threshold follow with no additional R factor.
This is a reproduction/specialization pending independent audit, not
a source-proof audit or an actual-Xi result. No mathematical script was
needed. Next nominate the exact C645h proof audit for separate approval.
