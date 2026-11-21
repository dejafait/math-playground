# Two-atom moment test — working record, step413

The unchanged EXPLORE gate is
`drafts/literature/2026-11-04-two-atom-moment-turan-countermodel-test.md`.
Main gap: actual-Xi all-degree mixed positivity and exceptional signs.
Intermediate target: the exact 255-point grid in that gate, followed by
complete all-order closure for at most its first eligible survivor.
Downstream use: test whether adding positive moments defeats L772's
generic obstruction; actual-theta realization remains independent.

Reuse the step411/412 theorem comparison and L021 conventions. L772
and its step408/410 evidence are contrasts, not all-order inputs for
this family. No cross-notebook input and no new source search.

First compute every D_(5,4) exactly. Only negative determinants are
screened at depths 1–4, indices 0–8, with initial entries through 12
and the original zero boundary on the left. A finite survivor is not
an all-order countermodel. Select by increasing p, then increasing j.
No survivor ends this grid; otherwise attempt the approved analytic
and stopping closure for only that survivor and save any unpaid bound.
No grid expansion or extra finite-depth sampling substitutes for closure.

Exact screen completed: 255 points, 253 positive determinants, no zero
determinants, two negative determinants. (p,j)=(6,4) fails at depth4,
index4. The unique survivor and hence selected case is (7,4):
r=7/16, w=16. All determinants agree between rational elimination
and the independent 120-term formula. Complete coefficients, shrinking
dependency layers and failures are in
`scripts/coefficient-countermodel/two-atom-grid-413.json`.

The selected determinant is
-532464112879658032522559819 /
80585079141022492739604823382757913108729036800000000.
All 36 screened entries are positive. This is not an all-order result.

For the pending certificate use the exact curvature interpolation
h0(z)=log((2z+1)(2z+2)/((2z)(2z-1)))
       -[log(1+16 r^(z-1))-2log(1+16 r^z)+log(1+16 r^(z+1))].
The initial ratio at positive integers is exp(-h0(n)). A large disk
centered at n with radius proportional to n should permit the saved
Xie–Zhang–Zhang Corollary2.6; its lower bound, logarithm branches,
initial-integer agreement and finite boundary closure remain unpaid.
The source's already-assessed formulas were retrieved for application,
not for a new literature comparison. Mathematical exploration usage:
one bounded attempt underway. Existing notebook changes are preserved.

## Completed closure test

At the selected point c_4(4)>10, so b^[5]_4<0. The obstruction is
actual finite negativity, not an analytic sufficient-bound failure.
Therefore no large-disk/tail construction is attempted: it could not
complete the requested joint property. All 255 determinant signs and
all recorded finite layers were replayed with integer arithmetic.
The complete result, proof, exact ratios, convergence and normalization
checks now live in `lemmas/L773-two-atom-grid-turan-failure.md`.
The final certificate is `scripts/coefficient-countermodel/two-atom-closure-413.json`.
Its first-pass interval diagnostic for the rejected (6,4) case is
retained separately; the canonical proof explains the corrected bound.
Outcome NEGATIVE: this grid is exhausted. No all-order countermodel,
general moment-sign theorem, actual-theta transfer or RH candidate.
