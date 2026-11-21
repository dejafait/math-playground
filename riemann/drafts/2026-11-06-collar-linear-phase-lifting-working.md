# Relative linear phase: second bounded attempt

Invocation-start target and coverage: the unchanged existential equation in
`literature/2026-11-06-collar-preserving-linear-phase-correction.md`
(EXPLORE). Main gap: L030–L032/C032a actual-Xi mixed positivity.
This attempt tests smooth relative flux lifting, not pointwise inversion.
Success would be one feasibility input for a later nonlinear correction;
nonlinear convergence, global sign and all other orders remain independent.

The supplied overview/DAG and assessment were used directly. Read the full
L850 reduction and accepted L849 construction; checked L847's full form,
L848's prescribed data and the restricted L850 inversion-stop record.
Directly recomputing the contracted form verifies the sign
D(Im q)[v]=-div(Mv), M=P I+Q adj(Du), and
det M=|F|^2-Q Im q. This is a prerequisite check, not an independent audit
of L850's numerical certificate or of every assertion in that lemma.

In the flat exterior, F=4C g(t)g(s) sin^2((t-s)/2),
g(t)=G(R exp(it))/(R exp(it)), and the equation is div(Pv)=Q.
A regular P-zero does not itself obstruct the equation: its restriction
is grad P dot v=Q. A closed nodal boundary contained wholly in the exterior
would force integral Q=0 in the enclosed domain. No such violated
compatibility has yet been proved. Exterior nodal arcs reaching the cutoff
transition do not supply it without controlling the intervening flux.

Planned discriminating test: retain the actual cutoff transition and look
for a full-range compatibility obstruction or a smooth supported flux lift.
No claim of ellipticity, global invertibility, a global phase branch or
sufficiency of zero total integral is made. The existential cutoff choice
is retained. If this second attempt supplies neither a solution nor useful
range evidence, reassess before repeating this mechanism.

This working record preserves partial reasoning before further work.

## Exact exterior lift obtained; transition remains open

The nonrigorous low-mode screen suggested a positive three-mode quadratic
margin. The subsequent exact rational certificate proves a margin greater
than 1/4000, with all eight checks passing and no failures. It uses the
full L778 evaluator error and brackets R between 184.82837518 and
184.82837520. Artifacts are under `scripts/actual-g-radial-graph/`, named
`exterior-phase-diagnostic.json` (not proof) and
`exterior-phase-certificate.json` (qualified exact certificate).

The inequality makes the continuous phase of g strictly decreasing except
at integer multiples of 2pi. On the cylinder off the diagonal, the sum
of the two phases and the half-separation form smooth coordinates. In
these coordinates P=H cos(x), Q=H sin(x), with H>0. If mu is the coordinate
area density and A=mu H, the explicit field
V_x=-1, V_y=A^(-1) integral_(pi/2)^y partial_x A(x,eta) d eta
solves div(Pv)=Q through every P-zero. It divides only by A>0.
This is a genuine smooth lift on the entire flat exterior, not a full
torus correction. Exchange averaging preserves its equation.

Multiplying that symmetric field by 1-chi gives a global admissible trial
variation zero on the collar, exact in the exterior. Its remaining source
is supported in the two cutoff transition strips; symmetry and total
zero integral give zero integral in each strip separately. A supported
solution there is sufficient, but has not been shown to exist, and is not
claimed necessary for a general global correction. Canonical details will
be in L851. The actual global target, transition degeneracies and nonlinear
sign questions remain unresolved. This supplies a materially new input
for further work, not permission to repeat ordinary divergence/inversion.
