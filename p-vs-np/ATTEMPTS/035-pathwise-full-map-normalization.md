# Attempt 035 — Pathwise cutoff with full composed-map caching

The target was a uniform polynomial full-bit/time bound for L101
normalization cached by (source line, full composed V→V map), with
at most floor(log₂ Q) renamings on every source path and original Q
fixed before transformation. Equal full actions share requests.

**WHY IT FAILS.** [L103](../lemmas/L103-pathwise-full-map-normalization-obstruction.md)
constructs h layers of 2^h renaming choices on disjoint h-pair blocks.
Legal axiom/MP merges realize every combination at the initial axiom,
giving 2^(h²) distinct full functions and distinct requested formula
strings. Every such request emits an ordinary axiom record. All-start
path depth is at most h, while the complete original occurrence/source
input satisfies 2^h≤Q_h≤C(h+2)^6 2^h. The record count therefore
exceeds every fixed polynomial in Q. The separate step-404 all-size
informal critical audit in L103 finds no substantive defect in source
legality, realized requests, record materialization or the original
ledger. No finite test is its proof and no implementation is verified.

Stop this specified cache's universal bound. Preserve L101 and Attempts
032–034. The family has a short independent ordinary proof, deliberately
retained in its final attachment. Alternative normalization, selecting
that proof and other witnesses are outside the tested procedure. This
is not proof-system or SAT hardness. Any stronger target requires its
own coverage. Current routing is recorded only in PROGRESS.md.
