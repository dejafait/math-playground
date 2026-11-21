# Boundary-fiber compatibility — working checkpoint, 7 November 2026

Approved target: test L881's two-simple-boundary-zero alternative against
L880 in both coordinate directions, including all simultaneous/diagonal
vertices. Invocation-start EXPLORE coverage is
`drafts/literature/2026-11-06-odd-contact-boundary-fiber-compatibility.md`.

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
A stronger necessary condition or boundary exclusion could narrow L879's
odd-contact mass-gap branch toward L868. Exterior alternatives, actual
graph realization, compactness, sharp period and Xi transfer remain open.
Continue only with a stricter compatibility condition or exclusion;
compatible necessary data alone are not a graph construction.

Inputs read: L847's actual form/orientation; L879's hypotheses and phase
line; L880's complete original proof and all vertex cases; L881's
hypotheses, coefficient, audited count and both-coordinate consequences.
Reused supplied source assessment and session43/two-period stops, plus
histories 47 and 50. No new external theorem or numerical input needed.

Unfinished reasoning: let the original vertical label be zeta, angle a.
Its complementary curve has exactly two simple boundary zeros zeta and
eta, angles a and b (necessarily distinct). L880's vertex expansions
are kappa*x*t at (a,b) and kappa*x*t*(x-t)^2 at (a,a).
Reversing the wedge comparison should give exact horizontal contact
segments, hence single seeds and complete horizontal fibers by L880.
This still requires a written exact-sector argument, not just jets.
The horizontal zeta fiber then has its own L881 boundary alternative,
with a second simple vertical label theta. Need test whether theta=eta
is forced, whether further odd contacts can occur, and whether these
conditions contradict anything. No conclusion yet and no graph claimed.

Preserve the full J, squared diagonal, coincident arguments and arbitrary
other G multiplicities; never infer a product graph from finitely many
fixed fibers. No assumption of positive density or analytic u.

Second checkpoint: the reversed wedges |t|<|x|/2 compare opposite signs
of t in kappa*x*t and kappa*x*t*(x-t)^2. They contain no actual divisor
zeros, so continuity forces z2=eta (or zeta at the diagonal) on t=0,
x nonzero. These are single seeds; L880 supplies both horizontal circles.
The horizontal zeta circle has boundary labels zeta,theta, both simple.
The same reversed-axis argument supplies the vertical theta circle.

Any additional single odd-contact seed would yield another full fiber,
contradicting one of the two zero-free/two-boundary complementary curves.
At any simple boundary contact of either unmatched fiber, the same local
bridge would yield such a forbidden extra fiber. Thus if eta!=theta,
each unmatched own label is exterior and its count 2*N_in+N_bd=4 has
the two forced simple boundary labels, plus either one interior simple
zero or one additional boundary double zero. If eta=theta all four
fibers are in the boundary alternative with the same pair. None of
these necessary alternatives has yet been excluded or realized.
Canonical proof still to write; especially retain distinct same-angle
labels, both coordinate orders, and explain why eta!=theta actually
forces three distinct angles using the zero-free original curves.

Completion: the canonical argument is now in unaudited L882. The
exact bridges and label/defect dichotomy were obtained; theta=eta was
not forced. Original zero-free complementary curves also make each
selected label radially minimal, which handles coincident arguments
and places any required extra zero on a new ray. The intermediate
reasoning above is retained as written; full qualifications and proof
are in the lemma, and current status/routing are solely in PROGRESS.md.
