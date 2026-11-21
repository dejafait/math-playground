# Fixed-point terminal splitting — step129 working checkpoint

Approved input: `drafts/literature/2026-11-10-xi-completion-terminal-splitting-128.md`
(SPECIALIZE, saved before invocation). Only its fixed interior point,
actual completion factor, finite-order cases and explicit Re(H'/H)>0
are in scope. Reuse its inspected Rouche coverage; no fresh source
claim or global homotopy is needed.

Write epsilon=1-u>0, s=s0+iw, f(w)=Xi(x+w), h=H'/H.
Multiplying H G_u=xi'-epsilon h xi by i gives
f'(w)-i epsilon h(s0+iw)f(w). Re(s)<1/2 means Im(w)>0.
For a noncommon root, f'(w)=c w^m+O(w^(m+1)), c real nonzero;
the scaled limiting equation is v^m=i h(s0)f(0)/c.
Its right side has imaginary part of sign f(0)/c. No limiting root
is real, so sufficiently small disjoint Rouche disks fix their sides.
Parity gives exactly L958's kappa. Need write the fixed-disk total
count and scaled disks together to exclude any omitted branches.

For f(w)=w^r A(w), r>=2, the family has the exact factor w^(r-1)
times r A+w A'-i epsilon h w A, whose value at zero is r A(0)!=0.
Need a uniform small disk for epsilon near zero: all r-1 roots
remain at zero on the boundary, and there are no local moving roots.

Provisional route decision: if these estimates close, stop the local
splitting mechanism as independent sign control. It re-encodes the
existing critical weight and establishes no K estimate or RH result.
No endpoint, global parameter index, height-uniform scale or sum of
perturbation limits is within scope. Canonical proof to be L959 if
completed; keep unfinished cases explicit if any estimate fails.

Completed: the fixed-circle total count and disjoint scaled circles
account for every noncommon branch; the common-factor bracket is
uniformly nonzero on a fixed small disk. Full proof and qualifications
are canonical in `lemmas/L959-xi-terminal-splitting-recovers-critical-weight.md`.
No local case remains unfinished. Independent critical review remains
pending; the main mixed-positivity and critical-sign gaps remain open.
