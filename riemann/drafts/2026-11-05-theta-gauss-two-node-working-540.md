# Step540 working checkpoint

Approved unchanged target: the two-node actual-theta rule and cubic
common-interlacing test in `literature/2026-11-05-theta-gauss-two-node-test.md`.
The supplied source gate is reused; this is RESEARCH/REPRODUCTION.
No new literature or degree extension is planned.

Inputs inspected: L019/L021, L795, the selected L791 step478 normalization
and provenance, L778 evaluator/software contracts and L796 actual-data
checks. Complete gamma(0..3) endpoints were read with the JSON inspector.
Existing unfinished files remain intact. No cross-notebook input.

Let t_j=(2j)! gamma(j)/(j! gamma(0)). The monic raw-moment node
polynomial is q(v)=v^2-A v+B with
D=t_2-t_1^2, A=(t_3-t_1 t_2)/D, B=A t_1-t_2.
Nodes are (A +/- sqrt(A^2-4B))/2, ordered increasingly; weights are
(v_2-t_1)/(v_2-v_1) and (t_1-v_1)/(v_2-v_1).
These formulas are pending exact checking, not established evidence.
For reference F_(3,sqrt(v))(x)=1-3vx/2+v^2x^2/4-v^3x^3/120.
Its scaled roots use the roots of y^3-30y^2+180y-120.

Next within this attempt: verify inherited hashes and selected PASS fields,
one exact-rational outward evaluation, symbolic moment and coefficient
identities, and both weak-alternation gaps. Strict incompatibility stops
this precise fallback; a pass proves only that finite premise. If dependence
prevents decision permit at most one rearrangement, then stop inconclusive.
All-degree mixed positivity and any degree-uniform bridge remain open.

Completed: formulas and exactness verified; first gap positive and second
strictly negative. Full proof is canonical L805; full arithmetic is
`scripts/theta-gauss/two-node-certificate-540.json`. The pending language
above preserves the pre-calculation checkpoint, not the current status.
