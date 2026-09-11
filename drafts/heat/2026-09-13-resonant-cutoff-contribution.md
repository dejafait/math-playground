# Exact resonant cutoff contribution — 2026-09-13

Checkpoint before final proof audit. Use L158's finite window and write
Z=Σ_{rm=sn,r≠s,m≠n} A_r A_s A_m A_n. The resonant part of K is −Z.
If F=Σ_k(Σ_{rm=k}A_r A_m)^2 and D=Σ A_n², then Z=F−D²:
on rm=sn, r=s forces m=n, so exactly D² is excluded.
All amplitudes are positive. L151's pointwise full Gaussian diagonal bound,
scaled by T³, gives 0≤Z≤C log(2T). L156 gives E_T Q≤C.
Consequently R_res=E_T[χ'(Q/M)Z]/M≥0, with upper bound
C log(2T) min(1,1/M)/M using support M<Q<2M and Markov.
This is only an upper bound, not logarithmic growth of R_res. The cutoff
cannot be factored from Z, and nonzero total frequency does not justify
orthogonality after multiplication by χ'(Q/M).
Resume by auditing normalization, excluded diagonal, and direct graph inputs;
then store the exact decomposition and the remaining unproved estimate.

Completed as L159. Audited ordered multiplicities, both signs, the pointwise
use of L151, and Markov with the cutoff support. The exact finite integer
regression passed. The remaining nonresonant estimate is explicitly unproved.
