# Compact tilted-primitive specialization — step83 working record

Completed: the full argument and qualifications are now canonical in
`lemmas/C947a-tilted-primitive-unique-simple-compact-zero.md` (relative
to the notebook). The partial outline below is retained as saved work.

Approved target: establish or refute that the unchanged U_(1/10) has
exactly one simple zero in (1/4,4), using L946 and L947. The prior
SPECIALIZE assessment is
`drafts/literature/2026-11-09-tilted-primitive-compact-zero-scope-81.md`.

Partial reasoning saved before final proof assembly: L938 continuity
and the compact FTC give U'(E)=exp(E/10)v(E). At any stationary point
c in (1/4,4), L946 gives v(c)=0 and v'(c)>0. The derivative definition
then gives v<0 immediately to the left and v>0 immediately to the
right; MVT makes c a strict local minimum of U. Hence U cannot have
an interior local maximum. If a zero r had U'(r)<=0, its immediate
left neighborhood would contain a positive U value, either by the
derivative definition or the strict-minimum conclusion. Since
U(1/4)<0 and U(r)=0, a positive maximum on [1/4,r] would be interior,
a contradiction. Thus every zero has U'(r)>0. For arbitrary zeros
r<s, a positive value immediately right of r forces a positive
interior maximum on [r,s], again a contradiction. IVT supplies
existence from the strict endpoint signs. This avoids any assumption
that the zero set is finite or discrete.

Work outstanding when this outline was saved: assemble the full hypotheses and cited
calculus applications in a canonical corollary, check all endpoint,
tangency and arbitrary-pair cases, and update the compact checkpoint.
This outline is not a numerical audit. The result must retain L947's
unaudited numerical implementation and L938/L946 execution contracts.
No new numerical calculation, global count, tail join or parameter
sign inference is authorized. The raw-U domain and ratio/field stops
remain unchanged. No cross-notebook input is used.
