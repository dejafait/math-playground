# Twenty-word simultaneous feasibility attempt — working record

Approved exact target and pre-invocation coverage:
`drafts/literature/2026-10-10-twenty-cyclic-height-feasibility.md`.
Main gap is universal eventual descent. Test L046 (1)–(4) at twenty
indices with the stated log20 seed and 1380/1034 term; seek an
all-parameter contradiction or a rigorously certified simultaneous tuple.
Essential inputs L041, L046, L049; no optional inequality is assumed.
Source and duplicate comparison reuses the supplied ready assessment,
L046's full proof/audit, L041's seed/own-index/endpoint/count passages,
and Attempts 019/021/023. No affine-coding reproof is planned.

Current reasoning: the scalar transfer discards closure. Investigate
consequences of the retained exact endpoints and integer total counts,
with all own-index guards. A finite count ceiling may permit a certified
lower bound on N log2-K log3; closure may then force a substantially
smaller minimum height. Such bounds must be derived from this subsystem,
not assumed from its larger optional relaxation. No verdict yet.
Parity/integer realization, unrestricted cycles, divergence and descent
remain unresolved even if this restricted system is excluded.

## Candidate contradiction saved before certification

The retained factor 48/25 transfer gives R=sum_{j=0}^{19}(48/25)^j
<503775 and N<(399/5)R log N+72R+2. Monotonicity at 10^9
with log(10^9)<21 should give N<10^9. From the exact endpoint,
write n_i=s_i-23/11 and
eta_i=23/11-(12/11)(16/27)^J_i-(16/27)^J_i(2/3)^H_i.
Then 0<eta_i<23/11 and n_(i+1)=(G_i/2^a_i)(n_i+eta_i).
Closure gives Lambda=sum log(1+eta_i/n_i)<460/(11 n_0).
Candidate rational comparison p=9809721694, q=6189245291 satisfies
0<q log3-p log2<log2/(2*10^9). Since N,K are integers below
10^9 and N/K>log3/log2>p/q, Nq-Kp>=1 gives
Lambda>log2/(2q)>1/(3q). Thus s_0<(1380q+23)/11,
whose logarithm is below 28. The retained geometric transfer would
then give K<(15/4)*503775*29<225640000, contradicting K>=K_0.
All numerical inequalities await exact certificates; no integer orbit
or general cycle theorem is inferred. No additional hypothesis is used.

## Completed bounded attempt

The candidate contradiction is written in canonical L050. All thirteen
exact comparisons pass. An initial failure in log20<3 used the inadequate
lower bound e>27/10; e>163/60 fixes it, with the original failure retained.
Complete certificate checks and logarithm enclosures were read. The
rational witness is used only for logarithm separation, not as a cycle.
No additional subsystem constraint was imposed. Result is a local
REPRODUCTION/ADVANCE pending separate critical audit; no complete Collatz
candidate or claim of originality is made. See L050 for the full proof.
