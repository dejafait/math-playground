# First-period allocation: bounded calculation working record

Gate at invocation: the unchanged EXPLORE assessment
`drafts/literature/2026-11-01-theta-first-period-integral-test.md`.
Actual task: calculation; classification POTENTIALLY_NEW only relative
to its completed source comparison, without an originality claim.

Main gap: actual-Xi all-degree signs at unbounded heights. The sole
intermediate target is the sign of integral_0^(2pi/11) G_11(a) da,
with exactly L609's allocation. A negative upper bound refutes
nonnegativity of every complete outer group. A nonnegative lower bound
rejects this witness only. A straddling interval/cap exhaustion is
inconclusive. Return after this one run; no frequency/period sweep.
The floor, other groups, total first sign and higher signs remain open.

Reuse L609, L604/C604a/C604b, L016/L019, L564's complete envelope
and L605's origin regularity and their source-proof qualifications.
Checked the completed period-grouping comparison, the existing fixed-a
stop and independent audit: none already decides this integral.
No cross-notebook input. Preserve all existing files/certificates.

## Inclusion plan, saved before the calculation

Let A=2pi/11, H(u)=integral_u^infinity v k(v)dv and x=11. Set
S(a)=integral_0^a k(b)cos(xb)db, T(a)=integral_0^a H(b)cos(xb)db,
U(a)=integral_0^a b H(b)sin(xb)db and
V(a)=integral_0^a b k(b)sin(xb)db. From L609's unchanged complete K,
write C=cos(xa), E=C+xa sin(xa). Distributing its two products gives

Z^2 G(a) = 4(a+H(a)k'(a)/k(a)^2)S(a)^2
          +4{E[k(a)T(a)-H(a)S(a)]
                 -x C[k(a)U(a)-H(a)V(a)]}.

This is a finite algebraic factorization, retaining both cosine and
both sine terms of K; no sign or discarded endpoint term is introduced.
The four primitives exactly integrate the full b triangle for each a.
At a=0 they all vanish, k(0)>0, and the expression is continuous and
zero by L605; there is no division by a, S, or k(b).

Parameterize a=A r on 0<=r<=1. For each fixed actual A, da=A dr.
Use r_i=i/N and d=A/N. All A uncertainty is retained in d and in
the boxes [lower(A i/N),upper(A(i+1)/N)]. This covers the irrational
endpoint without deleting a sliver. Integrating a uniform box F_i
over its actual cell yields d F_i, whose interval product includes
both the uncertain integrand and the Jacobian. Overlaps between
interval endpoint enclosures do not cause gaps: the true parameter
cells partition [0,A] for the one true A.

Compute H(A) and integral_A^infinity k by L609's second-derivative
midpoint rule on u=A+(8-A)s, 0<=s<=1, plus its complete spatial
tails. Each uncertain midpoint encloses the actual midpoint, each
whole cell encloses the actual cell, and the actual cell width is
enclosed by (8-A)/M. Use upper width cubed times the complete
second-derivative magnitude divided by 24, separately for uk and k.
The endpoint u=8 is constructed as a convex combination to stay
within the inherited [0,8] domain. No analytic quadrature is used.

Descend over the head grid from H(A). On cell [u_i,u_(i+1)], let
f_i enclose u k(u)>=0 and H_right enclose H(u_(i+1)). Then every
H(u) is in [H_right.lo,H_right.hi+(d f_i).hi]; the left endpoint
is enclosed by H_right+d f_i. Positivity, not an assumed numerical
accuracy, proves this induction. Each numerical k box must have a
strictly positive lower endpoint; no division before that check.

For any one of the four signed primitive integrands f, suppose P_i
encloses integral_0^u_i f. On the entire current cell, the partial
increment is enclosed by [0,d.hi] times a whole-cell enclosure of f.
Thus P_i+[0,d.hi]f_i encloses P(a) for every a in that cell,
including its moving b=a boundary. Update P_(i+1)=P_i+d f_i.
This retains the boundary triangle even for negative integrands.
Insert these whole-cell primitives, H, k, k', sin, cos and a into
the displayed formula; sum d times its interval over every cell.
Normalize once by Z^2, Z=2(integral_0^A k+integral_A^infinity k),
after numerical separation of Z from zero. Dependency only widens.

Use the imported directed Decimal implementation from `certify.py`,
unchanged, including exact negation, widened nearest exp, squares,
Machin pi, all five theta terms and evaluated n>=6 tails. Sin/cos
midpoint boxes propagate by simultaneous angle addition; initial and
step arguments lie within its Taylor domain |t|<=5, while box radii
use the global derivative bound 1. No direct Taylor call at 2pi.
All series/spatial tails, nested boxes, midpoint and rounding errors
are propagated; no tolerance or floating preview is evidence.

## Declared finite caps

One run: N=65536 head/outer cells, M=4096 tail cells, precision 45,
five theta terms, cutoff 8; at most N+2M=73728 kernel calls and
four direct initial/step sincos calls (in fact two). No adaptive
restart or parameter enlargement. Store every head and tail cell in
`scripts/theta-allocation/first-period-certificate.json`, including
integral/error bounds and runtime signals. Expected finite workload;
cap or exceptional-arithmetic failure leaves the target inconclusive.
The original singleton certificate and audit are never overwritten.

Pending: implementation, this one run, complete selected evidence
inspection and scoped documentation validation. The algebra/inclusion
plan is mathematical work on the gate-approved target; it supplies no
integral sign before those checks.

## Completion

The single run completed within every declared cap. Its interval is
strictly positive, rejecting the selected negative-witness proposal.
The complete proof, bounds, imported citations, error propagation and
qualifications are canonical in C609a; no further parameter was tried.
All load-bearing aggregate/arithmetic/runtime evidence was inspected
using the shared JSON inspector. The exact-rational check covers every
stored domain cell and aggregate, without rerunning quadrature, and
passes. Neither this consistency check nor the original source imports
are relabeled an independent proof audit. Current routing is solely
in PROGRESS.md; a new independent audit scope is proposed separately.
Scoped documentation validation passes (642 nodes, 1572 edges; local
coverage, links, acyclicity and overview limits). The main assembly
is unchanged, so PROOF.md is deliberately untouched this step.
