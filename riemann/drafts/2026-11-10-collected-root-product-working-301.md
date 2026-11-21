# Fixed-radius collected coefficient test — working record

Completed in this step: the proof and all qualifications are canonical
in lemmas/C999a-collected-diamond-steinig-mass-uniform-decay.md.
The saved checkpoint below preserves the intermediate reasoning;
its then-remaining proof obligations have now been discharged.
Exact independent Newton/direct coefficient checks n=1,...,8 are in
scripts/diamond_steinig/root_pair_301_certificate.json, with no failures.
The arithmetic interface remains uncovered and is not attempted here.

10 November 2026, step301. Prior coverage: review300, SPECIALIZE;
exact target and formal observable are unchanged from invocation.
This is a research/calculation specialization, expected REPRODUCTION.

Checkpoint before completing the proof: set E_Y(t)=1+sum_(j=1)^(2n)
Y_j t^j/j!, and let F=log E_Y formally. The untruncated polynomial
P_n=2n[t^(2n)]F+n^2([t^n]F)^2 retains exactly T_n's coefficients
on vectors of length at most n. Ordered pairs, full exponents and
factorials must be verified explicitly. Its other coefficients cannot
be discarded inside a supremum norm.

At any complex specialization |Y_j|<=1, factor the actual degree-d
polynomial as product_(i=1)^d(1-x_i t), with multiplicity. Then
P_n=2 sum_(i<j)(x_i*x_j)^n. Imported Landau and multiplicativity
give product_i max(1,2|x_i|)<=sqrt(sum_(j=0)^(2n)4^j/(j!)^2).
The infinite scalar sum is at most 97/9+100/189=2137/189<12:
terms j=0..3 sum to 97/9; starting at j=4 their successive ratios
are at most 4/25, with initial term 4/9. Thus every pair obeys
|x_i*x_j|<=sqrt(3)/2<1. Constants and linear polynomials give P_n=0.
This implies |P_n|<=2n(2n-1)(sqrt(3)/2)^n on the full torus.

Remaining proof work at this checkpoint: justify coefficient equality
for every retained full vector, apply normalized Fourier recovery to
P_n (not its truncation), bound support by p(2n), and derive the
all-n zero-rate conclusion from the imported partition bound. Check
n=1, actual-degree drops, repeated/boundary roots and the mu length
interpretation. No arithmetic interface is authorized this turn.

The main gap remains actual-Xi positivity/signed forcing and L984(H).
A favorable coefficient result pays none of the factor norms, signed
correlations, reconstruction, prime powers, compensation, endpoints,
complements or regulator/infinite-zero control. L998/L999 are contrasts;
no RH assumption, cross-notebook input or novelty claim is involved.
