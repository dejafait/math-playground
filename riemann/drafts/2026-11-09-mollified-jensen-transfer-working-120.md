# Mollified endpoint transfer — retained working checkpoint, step120

Completed later in this step: the canonical proof is L957. The initial
reasoning below is preserved as a checkpoint, not a second proof or
current-status record. The complete specialization awaits separate audit.

Approved scope: the exact target in
`literature/2026-11-09-mollified-jensen-endpoint-transfer-119.md`.
This is an established-method specialization; no arithmetic moment
reproof or RH claim is intended. Main gap: L030–L032/C032a mixed signs.

Attempt in progress. Fix S=2T, X=S^(1/4), P(u)=u, and
M_X(s)=sum_{n<=X} mu(n)(1-log(n)/log(X)) n^(-s), F=ζ M_X.
Young Lemma3 at zero shifts gives c=1+1/theta=5. A smooth majorant
of [T-2,2T+2], with transition S/log S, should give second moment
at most 5T+O(T/log T). Candidate displacement coefficient is
log(5)/(4pi), below 1/4; this checkpoint is not a completed proof.

Remaining checks: choose zero-free horizontal boundaries just outside
the padded window, keep X fixed, and prove uniform O(log T) horizontal
argument bounds by Jensen applied to the real part of F along a line.
Use right edge 4, where ζ and M have uniformly absolutely convergent
logarithmic Dirichlet series and integrated real log O(1). For the
left edge limit, factor finitely many local zeros and prove L1
continuity of their logarithms before using concavity of log.
Then retain all nonnegative product zero orders and compare the closed
disk intervals using L018's one-right-zero-per-conjugate-pair convention.

Continue only if W_T<=T/4 eventually and disk-free endpoints follow
with every boundary error o(T). Otherwise retain the failure and park
this specialization. Critical counts and global/mixed signs stay open.
