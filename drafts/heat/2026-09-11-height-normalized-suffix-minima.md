# Height-normalized suffix minima — 2026-09-11

Candidate obstruction, not yet a proved DAG input: take x_n=sqrt(n) log(n+2)
and h_n=1/log(n+2). Then h_n n²/x_n²=n/log³(n+2) diverges at every
index, so selecting indices cannot make the Lemma 84 sufficient bound
vanish. The normalization suggested by this factor is
q_n=n sqrt(h_n), since h_n n²/x_n²=(q_n/x_n)². But x_n/q_n tends
to zero, so no positive suffix minimum exists. More generally the same
failure holds for every positive q_n eventually at least c n sqrt(h_n).
This only obstructs these normalizations and the height-deficit bound;
it does not rule out using actual height increments or other estimates.

Resume: verify coordinate and height hypotheses, summability, divergence,
and the no-suffix-minimum assertion; store the precise scoped obstruction.

Audit completed: Lemma 85 proves the scoped obstruction, including the
broader eventual lower-bound class. This draft has no pending proof claim.
The unrestricted liminf question remains unresolved.
