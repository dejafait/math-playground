# Collar-preserving linear phase: bounded attempt working record

Invocation target and gate: exactly the TARGET in the unchanged EXPLORE
assessment `drafts/literature/2026-11-06-collar-preserving-linear-phase-correction.md`.
One proof_attempt/creative; no global sign or nonlinear inference.
Main gap: L030–L032/C032a all-degree mixed positivity. A solution of the
full relative first variation would supply only a feasibility input for
a later global phase mechanism. An obstruction must state its cutoff scope.

Read the supplied overview/DAG/assessment, then L847 full graph/form and
homotopy, L848 prescribed data and qualifications, and L849 branch and
cutoff (18). Reused the ready source comparison and checked the recorded
product and averaged-extension failures. Their scopes do not settle this
linear problem. Existing notebook work is preserved.

Working reduction, to check before promoting: write F(Phi_u)=P+iQ,
A=Du, and f=Im q_u. Contracting the closed full form with the real
radial variation suggests

    D(Im q)_u[v] = -div(M v),  M=P I+Q adj(A),
    det M=|F|^2-Q f.

The standard pullback-differentiation theorem is already covered by
Guillemin–Sternberg Section13.13; only its actual graph specialization
is being derived. No division by a zero is allowed. On the accepted
off-diagonal positive collar det M=|F|^2>0. Where the cutoff is zero,
M=(Re F_0) I. Thus a zero-mean divergence theorem alone is insufficient.

Current test: examine whether the flat exterior's Re F_0 nodal sets
force an incompatible flux condition, or whether the positive collar
permits a smooth supported correction. Exact range, zero/degeneracy
compatibility and admissible cutoff choice are unresolved. This note
is interruption recovery, not a completed proof or result.

Inherited inputs: L847/L848/L849, L018/L775 actual G,R,C; L778(2)–(5)
and step433 analytic/trusted-software qualifications through L848.
No cross-notebook input, mathematical script or certificate has been used.

## Bounded test result, before final write-up

The contraction calculation checks the displayed operator, including all
zeros. The residual has zero integral and vanishes near the diagonal;
Teixeira Theorem3 applies after identifying the collar complement with
a planar annulus. It gives a smooth supported ordinary flux, which can
be averaged under exchange. It does not give a smooth M-preimage.

The direct pointwise-inversion route fails for every allowed cutoff:
the whole antipodal line lies in its flat exterior, where M=P I.
Exact rational reuse of the L778 evaluator gives R_1<256 and
G(-x)>1/100 on [0,256]. Along that line Re F starts nonnegative at
(pi/2,-pi/2) and is strictly negative at (pi,0), so M vanishes at
some exterior point. The computation is saved, with every interval,
in `scripts/actual-g-radial-graph/linear-phase-exterior-bounds.json`.
The displayed lower margins are 0.00106733597846 for the saddle test
and 0.0127187664132 for G(-x), both required only to be positive.
All seven exact checks pass; no terminal failures. The inherited
analytic/software input was not rebuilt. This is not a full linear
range obstruction: at a regular P-zero the derivative of P still
contributes to div(Pv).

No admissible v or violated full-range compatibility was obtained.
The canonical write-up will retain the full equation, source
specialization, exact certificate method and restricted inversion stop.
Outcome remains EXPLORATION against the invocation's stronger test.

Final canonical record: L850 in
`lemmas/L850-collar-linear-phase-flux-and-exterior-degeneracy.md`.
It contains the full proof, source hypotheses, certificate method and
limits. This working note is not a second canonical proof. Continue
only with the unresolved smooth flux lifting under the unchanged gate;
do not retry an everywhere-invertible M or infer a full range obstruction.
