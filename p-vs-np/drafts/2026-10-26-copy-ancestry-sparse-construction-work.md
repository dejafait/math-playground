# Sparse construction work — step 521, 2026-10-26

Approved target: construct forward/backward simulations for job-7 W=R in
all three modes, with total support at most C*S. Main gap: uniform P versus
NP; intended local use: a compact equality certificate, with independent
occurrence reception, Dcomm and complete finite costs still unresolved.

The pre-existing SPECIALIZE assessment is
`drafts/literature/2026-10-26-copy-ancestry-sparse-construction.md`.
Reused its completed source comparison, the October 25 selected-copy and
linear-algebra assessments, and Attempts 044–046. Relevant full proof
passages read: L035 (2)/(4) and four-copy realization; L036 (5)–(9);
L038 label/gadget/right-closure transport; L097 §22; L110 §§1–5,21 and
terminal qualifications in §24; L108 §§11,13 boundary qualifications.
No finite archived input data, sibling notebook or mathematical script read
or run. Existing unfinished changes are preserved.

Working proposal, not yet a result: for each mode graph H, restrict first
to entry-reachable vertices U. Its inclusion J should give H[U] -> H.
Then project to the exit-coreachable part T of H[U], giving H[U] -> H[T].
Use copy/edge/gadget ancestry to number W's and R's trim identically, so
the global chain is W <- W[U] -> T <- R[U] -> R. The two reasons for
deletion thus use different arrows. Empty T may be a zero-dimensional
intermediate with empty boundary vectors, not an invalid rooted endpoint.

Still to prove: all raw adjacency and boundary equations; compatibility
with finite right closure; a common occurrence-level trim in free/zero/
axiom modes, including no-path/coincident/nonextremal roots and fresh word
interiors; full support/intermediate-size/index/checking-work ledger.
Candidate support count is |U_W|+|U_R|+2|T| <= 2(|V_W|+|V_R|), summed
over modes. This estimate is provisional until the maps and common trim
are established. Continue only on complete equations and a uniform bound;
a failed equation would reject this map family, not all simulations.

Completed result: the four-arrow construction, complete equations, all-mode
ancestry argument and total-support bound 2*S are recorded canonically in
`lemmas/L111-job7-copy-ancestry-sparse-simulations.md`. The empty-core
intermediate was made a one-state zero representation with zero boundaries,
avoiding a zero-dimensional/root convention. This resolves the provisional
obligations above at the informal symbolic level; separate critical audit
and finite receiving/cost obligations remain. No numerical experiment or
production change was made. The result is local REPRODUCTION, not a new
semantic identity or a global complexity advance.
