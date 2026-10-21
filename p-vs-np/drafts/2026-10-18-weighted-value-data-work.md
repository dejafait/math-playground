# Weighted value data — step 329 work checkpoint

Approved target and coverage: `drafts/literature/2026-10-18-common-order-weighted-value-data.md` (unchanged EXPLORE). Main gap: unrestricted SAT. Test: polynomial full-bit local H data for supplied common-order faithful affine value graphs; no arbitrary-ER availability claim.

Provisional calculation, not yet a completed result: at level k write edge labels l=a+b*y and m=c+d*y. Put q=ac+(ad+bc+bd)*y. Then lm=q+bd*(y*y+y). For child suffixes f,g and K with K(A)=fy+yf, the ordered correction is l*d*K*g+b*d*sigma*f*g. A pair recurrence with q*W_child should therefore correct fg to its increasing multilinear pointwise product. Recursive W appears only on the right of q; local corrections use x-only suffixes and L035, never recursive W operands. Check terminals, exact signed wrappers (weighted terminal complement is invalid), independent copies and framing before declaring success.

Intended graph test: pair states advance a level, or enter a disjoint local correction and exit to one fresh sink. No correction returns to pair states. Counting edge pairs, rather than paths, should bound all blocks. Full proof and final ledger remain to be written. Preserve all prior unfinished notebook work.

Completed checkpoint: the provisional calculation and graph test are
now written with full hypotheses and an all-size proof in canonical
L085. The earlier paragraphs preserve pre-completion reasoning, not
an outstanding task list. No implementation or finite graph check was
performed; independent critical audit remains pending. Current status
and the single continuation are solely in PROGRESS.md.
