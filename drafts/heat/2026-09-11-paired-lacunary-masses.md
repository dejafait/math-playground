# Draft: separated consecutive pairs — 2026-09-11

Use pair endpoints e_j=n_j+1 and place tail-budgeted unit jumps strictly
past selected e_j. Let A=sum (M_j+N_j)/n_j^2 and choose increasing J_h
with tail beyond J_h at most 2^-h. Set P(k)=1+sum 1_(e_(J_h)<k),
F(k)=P(k)+1-1/(k+1). Pair masses both see exactly the jumps from
strictly earlier pairs. Weighted integrability follows by nonnegative
interchange. Endpoints are doubling separated, so baseline near
increments are at most two. If a mass location l is in (k,2k), every
previous pair endpoint is <k, while its own endpoint is >=l. Thus
P(l)=P(k). The correction gives near extra sum <=2A. Far sum <=4D.

Checkpoint: construction drafted, not yet a proved input. Resume by
auditing the second location l=n_j+1, the possibility of a previous
endpoint in [k,l), n_1=1, and applicability of the L111 cutoff. The
intended result concerns pairs only; arbitrary counts remain unproved.

Audit completed: Lemma 114 stores the proved paired-location result.
The preceding endpoint is at most n_j/4<k for either near mass
location. The jump after the second location therefore preserves both
cancellations. Near baseline, near masses and far bounds are 4, 2A
and 4D. This file retains the draft checkpoint only.
