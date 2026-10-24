# Second ordered E,E rate — working checkpoint

Completed in YM-20261022-404-second-ee-quantitative-remainder. The
canonical proof is L261; it obtains O(N^2 log(eN)), pending a separate
critical audit. The initial unfinished reasoning below is preserved.

Approved target: complete remainder against L169(2), for both actual
probes, at most C_i N^(5/2)log(eN)^2. Essential imported inputs are
L166 exact order/removals, L169 coefficient, L260(5) compact residual
comparison, L164 bulk extension/image comparison and L248 raw/heat
matching. Their upstream qualifications remain. No numerical sign needed.

Attempt in progress: normalize R_N=a Sigma A; F remains undifferenced.
For e compact, q(e-x)=r^-4/(1+|e_T-x_T|) has tail O(1/R), and its
truncated first moment is O(log(eR)). Cut action sources at fixed
physical clearance r<=cN. There y is interior, so symmetry of each
relative component permits the compact-observation Sigma-g error
O(N^-2) uniformly over all actual prefix inputs z. Summing at most N
inputs and the omitted lower half-line gives |F-Phi_-g|<=C/N.
L260(5) times the actual prefix b^-1 has row sum O(log(eN)/N);
the prefix error times r^-4 has the same bound. Far original and
infinite products cost O(1/N), including every boundary stencil.
Smooth exterior freezing costs a times the truncated joint first
moment. Full normalization should give O(N^2 log(eN)).

Still to verify before claiming: exact source/row placement of the
component image bound, normal end rows in the prefix, collar count,
all action exterior slots and polynomial full-heat summability.
No fourth-trace product estimate or qualitative varying-cutoff limit
is being used. Third-trace rate and all construction gaps remain.
