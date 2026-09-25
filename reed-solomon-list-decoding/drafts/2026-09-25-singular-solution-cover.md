# Singular solution cover audit — 2026-09-25

## Gap, proposed target, and discriminating test

The fixed scalar solution cover remains the missing geometric input to
L002: L004 controls each nonsingular graph closure but does not show that
singular solutions occur in polynomially many controlled charts. The target
for this step is a cover of every degree-at-most-d solution of a nonzero
Q(X,Y_0,...,Y_r), with total Y-degree at most B, X-degree at most D,
and characteristic zero or p>max(d,B), by dimension-at-most-r sets of
polynomial total cumulative degree for fixed r,B.

The shared and local instructions, full overview, DAG, existing changes,
L002–L004, and prior source/threshold and chart audits were inspected.
Unfinished work is preserved. No existing local lemma supplies singular
coverage. The earlier failed q-polynomial transfer does not address this
field-independent construction. The [prize page](https://proximityprize.org/)
was rechecked on September 25: the base-field threshold and field-existence
proviso agree with the frozen target. The ABF26 comparison remains open.
The source passage under review is
[TR26-169, September 5 version, proof of Theorem 5.5 and Corollary 6.1,
printed pp. 24–26](https://eccc.weizmann.ac.il/report/2026/169/download#page=24).

A plausible use is to apply L002 whenever interpolation supplies such a Q
for every received word. Interpolation with constant r,B and D=O(n), full
field scope, concrete constants, and the exact finite-code boundary remain
separate gaps. The test passes only if the derivative descent covers every
singular solution and both the number of anchors and the sum of chart
degrees are polynomial in D,d for fixed r,B. Failure of termination,
uncontrolled branching, or a needed exponent growing with d would reject
this mechanism.

## Saved working argument and completed result

Assume 0<=r<=d and B>=1. Start with Q_0=Q. While Q_j depends on some Y_i,
choose its highest such index r_j and set Q_(j+1)=partial Q_j/partial Y_(r_j).
The characteristic condition keeps this derivative nonzero. Total Y-degree
drops at least one, so after at most B steps the chain ends at a nonzero
polynomial of X alone. For any solution P of Q_0, there is a first index
j+1 at which the chain evaluates nonzero on the full Hasse jet of P.
Thus P solves Q_j and its highest-variable partial evaluates nonzero.

That evaluated partial has X-degree at most D+(B-1)d. A fixed set of
N=D+(B-1)d+1 distinct anchors in the algebraic closure detects it. At one
anchor P therefore belongs to the nonsingular chart of Q_j. Applying the
fixed-parameter bound of L004 gives at most B N charts, each of dimension
at most r and bounded degree. Derivative charts may include solutions
outside Q_0=0; that is allowed by L002 and must remain explicit.

The saved uniform estimate was: let A=D+B, L=max(0,2d-1), E=A(1+B L),
T=A L+1. The summed degree is at most B^2 N(E T)^r. The bound may be
sharpened by summing the decreasing Y-degree, but that is unnecessary for
the polynomial test. Anchors need not lie in the original finite field.
The working argument was saved before detailed proof work. Its completed
proof is now [L005](../lemmas/L005-singular-solutions-in-a-finite-chart-cover.md),
which establishes this bound. The cover is for a supplied, fixed scalar
Q. It needs neither primitivity in an auxiliary parameter nor a theorem
about exceptional parameter values.

## Checks and qualifications

The proof treats a single deterministic derivative chain. It does not
assume the highest-variable partial stays at the original differential
order, or that every solution is nonsingular for the original Q. The
first nonzero evaluation along the chain supplies the required earlier
equation. Each chart is closed after retaining its nonzero partial and
imposing its base and residual equations, as L004 requires.

Exact algebraic checks are included in L005. The family Q=Y_r^b reaches
the final derivative stage and has an r-dimensional solution space.
Q=Y_0Y_1 requires the derivative order to drop for its zero solution.
Q=Y_1^2-Y_0 shows that a derivative chart can contain extra constants.
Over F_p, Q=(X^p-X)Y_0 shows why all base-field anchors can fail even
when p>d,B; anchors in the algebraic closure resolve this without a
larger-field hypothesis on the code.

The characteristic checks separate two issues: Q=Y_0^p kills the raw
partial-derivative descent when B=p, whereas Q=Y_1 with d>=p actually
has dimension floor(d/p)+1 and defeats a dimension-one finite cover.
The former is a failure of this mechanism, not a counterexample to all
cover constructions. Empty solutions, d=r=0, omitted identically-zero
anchor partials, and the no-lift case were also checked in the proof.
These are exact calculations; no numerical samples or new script were
needed. Mathlib coverage is not checked, and the source theorem is
distinguished from the explicit bound proved here.

## Comparison with the required threshold and assessment

If, for every scalar received word, an additional interpolation theorem
supplies a nonzero Q with these common bounds containing all candidates
at A_agree>=k agreements, set d=k-1. L002 and L005 then give

\[
 B_m((n-A_{\rm agree})/n)
 \le \left\lfloor B^2N(E T)^r\sum_{a=0}^r n^a\right\rfloor^m.
\]

A sufficient threshold condition is therefore

\[
 q\ge (\varepsilon^*)^{-1}
       \left[B^2N(E T)^r\sum_{a=0}^r n^a\right]^m.
\]

For fixed r,B,m and D,d=O(n), the bracket is O(n^(5r+1)). This remains
a quantitative additional field-size condition. It is not implied by
epsilon* q>=1, and a certificate for fixed positive slack would not
locate the exact boundary. No new unconditional safe radius follows
before the interpolation input is established.

The polynomial coverage test passes. This step is ADVANCE, with an
exploration streak of 0/3, because it establishes the missing scalar
cover including singular solutions. The reason to retain this route is
that the cover can now be used directly by the existing agreement count.
The substantive unchecked input is interpolation with constant r,B and
D=O(n) at fixed slack, rather than further refinement of local chart
degrees. The field and source-scope qualifications remain. No complete
candidate resolution of the grand challenge appeared.
