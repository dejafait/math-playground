# Corollary 426c: a negative conditional anchor and an unsuccessful smaller-complement test

## Hypotheses

Use L426's unchanged conditional mean A, integral I and complete
prime-Haar response G, with L423's fixed mixture and the literal
two-stage selector. Let a,b be C426a's exact enclosing response
endpoints. Reuse its audited endpoint enclosures and C426b's audited
A(30), negative core [a,c0], delta0 and complete positive-moment
upper bounds U_r for r=1,...,8. These are enclosing endpoints;
attainability is not assumed.

Assume correct Python integer, Fraction and isqrt execution and the
outward interval, elementary-function and angular-jet contracts of
L037, L426 and audited C426a/C426b. All new numerical enclosures below
use 24 decimal places. The new calculation has a complete finite-record
consistency check, not a separate independent critical audit.

## Conclusion

Under these contracts,

    -8235954246166947438111/10^24 <= A(1)
       <= -1378199607890403295227/(2*10^23).

In particular -83/10000 < A(1) < -68/10000. This is a conditional
anchor, not a uniformly negative core.

The finite transport certificate also gives A(g)<=M0 on [c0,b], where

    M0 = 24107617920878437523629679947014046007643491165395769
         /22945853251371236526501036032000000000000000000000000,
    21/20 < M0 < 53/50 < M_*.

Here M_* is C426b's particular global complement bound. For the
retained certified core, pbar(c0)=1, so its comparison is M0>0.
For each of the other 31 saved cutoffs, the new full-core upper
enclosure contains positive values, and therefore does not certify
a negative core. None of these 32 comparisons succeeds. This is a
failure of the bounded calculation; it is not a universal obstruction
to every smaller-M certificate or a sign determination of I.

The combined charged work is 261020 callbacks out of 262144,
including inherited work and this step's consistency check. The 1124
remaining callbacks cannot evaluate one more complete response-
derivative slab on the retained partition (5496 callbacks). Park this
implementation. Retain I in [-.194,.114]; no occupation obstruction,
actual-law realization, clipping, regulator margin, positivity range,
zero exclusion or RH conclusion follows.

## Proof

This is a RESEARCH / REPRODUCTION / calculation under the unchanged
prior SPECIALIZE assessment
`drafts/literature/2026-10-17-bulk-haar-signed-core-response-tail.md`.
It is local specialization of known methods, not a discovery beyond
the checked sources. The new work tests only the previously untried
smaller full-complement option.

**Imported inputs and applicability.** Import the closed-cell real
trapezoidal remainder from [NIST DLMF 3.5.1--3.5.3](https://dlmf.nist.gov/3.5.i)
and the real mean-value bound from [DLMF 1.4.11](https://dlmf.nist.gov/1.4.E11),
as inspected in the assessment. Certified strict selector cells are
C^2 on their closed angular intervals; no differentiability through
a selector tie is asserted. L426 (17)--(18) provides response
derivatives and compact domination even for the unresolved angular
set, since the selector is independent of g.

Reuse Markov's inequality from S. Sheffield, *MIT 18.175 Lecture 8*,
undated PDF accessed 2026-10-17, [one-based PDF pp. 40--41](https://math.mit.edu/~sheffield/175/Lecture8.pdf#page=40):
G is bounded and positive, and the thresholds c^r are positive.
The complete Euler moments U_r and their finite positive expansions
are exactly the audited C426b records, not moments of truncated
response products. Their underlying absolutely convergent Euler
input is [DLMF 27.4.1--27.4.3 and 27.4.10](https://dlmf.nist.gov/27.4).
No new Euler or probability theorem is reproved here. Retain every
coefficient interval and omitted-prime tail from those records.

**The anchor.** Reuse all 1848 audited step-196 angular cells and
their closed-cell state jets. Of these, 1824 have strict selectors;
the remaining 24 have total normalized angular mass epsilon=3/65536.
Evaluate L426 (17) at g=1 using C426a's validated angular-jet
operations. For a strict cell of mass m, average the three state
jets and use its endpoint trapezoid with error

    m (2 pi m)^2 sup|f''|/12.

Intersect with the direct state range times m. Each unresolved cell
keeps its full mass times [-R(1),R(1)], where
R(g)=(1+sqrt(3g/80))/2 is L426 (13). All endpoint values, angular
second derivatives, radii and intersections are saved in
`scripts/discriminant/bulk-smaller-complement-199.json`, under
`anchors/0/cells`. The exact sum is the displayed A(1) enclosure.
The existing jets are reused as inputs, without a new selector
evaluation for each closed cell. New point selectors are counted.

**Response derivatives on the whole range.** Partition [a,b] at

    a, 1/5, 3/10, 1/2, 1, 2, 4, 6, 10, 15, 20, 25, 30, 35, b.

These are 14 response slabs, not sampling points substituted for
the response distribution. On each strict angular cell and response
slab evaluate the interval extension of the exact derivative

    exp(-t g)[p+(2q-tp)g-tq g^2],
    t=3(x^2+y^2), p=3(y^2+xz), q=-18y^2(x^2+xz).

Here (x,y,z)=P u for precisely the saved selected state. The entire
response slab enters every occurrence of g. All exponential arguments
are nonnegative. Average the three states and sum with their exact
angular masses. This encloses the derivative of the integral over
the fixed strict angular set; call that integral B(g), and denote its
slab derivative bounds by l_j,u_j.

Also retain a derivative bound on every unresolved angular cell.
With T=13/4, B_*=1/4+3/sqrt(80), C_*=(3/2)(1+1/sqrt(80)),
L426 (18) gives on a nonnegative slab

    |f'(g)| <= B_*+(2C_*+T B_*)g+T C_* g^2.

Include these full-mass contributions in `full_derivative`. All 76608
strict-state derivative records, 336 fallback derivative records and
25872 cell records are saved. Thus a full sup|A'| is available on
every slab. A sharper valid transport enclosure uses the unresolved
integral's direct range, as follows; no unresolved mass is dropped.

**Two-sided transport.** Put C(g)=A(g)-B(g). From the complete
unresolved mass and (13), |C(g)|<=epsilon R(g). For each certified
full anchor A(h)<=v_h, h in {a,1,30,b}, therefore
B(h)<=v_h+epsilon R(h). Integrate the slab derivative upper bounds
forward and the lower bounds backward. At each response node g_j
take the minimum of the four resulting upper bounds, denoted e_j.
Each inequality bounds this same B, so taking the minimum is valid.

On a closed slab [g_j,g_(j+1)] every g satisfies

    B(g)<=min(e_j+u_j(g-g_j),
               e_(j+1)-l_j(g_(j+1)-g)).

For a closed subinterval [v,w] in that slab, maximize this minimum
over its endpoints and, when present, the intersection of the two
affine functions. This is exhaustive: the minimum is piecewise
affine with at most one corner. Add epsilon R(w), since R is
increasing for g>=0, to obtain a bound on A throughout [v,w].
Take the maximum over all intersecting slabs. This constructs whole
core and whole complement bounds, retaining full response support.
The saved full derivative bounds are valid independently; using
the direct unresolved range here improves their transport consequence.

**The 32 comparisons.** Use exactly C426b's original 32 rational
cutoffs. For every one, compute the core upper bound by the preceding
whole-interval rule. At c0 intersect it with the already proved
negative-core upper bound -delta0. Compute the full complement upper
bound, replace a negative upper bound by zero if necessary, and
intersect with the independently valid M_*. At c0 the smaller bound
is exactly M0 above. At c=1 the core upper bound exceeds 1/20,
despite the negative anchor A(1); the interval between anchors is
not certified negative. All 31 other saved cutoffs likewise have
positive full-core upper bounds. This states failure of these
enclosures, not positive values of A anywhere in those cores.

For each cutoff recompute

    pbar=min(1,U_1/c,...,U_8/c^8).

Every value matches its saved C426b value exactly. At c0<1 all
eight capped moment bounds equal 1; its comparison is consequently
M0, independent of delta0, and is positive. The remaining cutoffs
have no certified negative core, so no signed comparison is claimed
for them. Their smaller complement bounds alone cannot sign I.

**Verification, accounting and stop.** Commands:

    python3 scripts/discriminant/certify_bulk_smaller_complement_199.py
    python3 scripts/discriminant/check_bulk_smaller_complement_199.py

The generator resumes saved work and returns a saved completed
certificate without repeating evaluations. The checker reads every
new cell/state record, verifies partitions, state averaging and exact
aggregates, and recomputes every transport envelope and all 32 full
comparisons. All seven consistency checks pass in
`scripts/discriminant/bulk-smaller-complement-check-199.json`.
It does not independently replay the exponential, selector or Q-jet
callbacks; those remain under the stated audited implementation
contracts. A preview or this finite consistency check is not an
independent critical audit of the new result.

The anchor uses 1833 new point selectors and 10971 state/angular-jet
callbacks. The slabs use 76944 response-derivative callbacks, including
all fallback bounds. Additionally charge every auxiliary Q-range
evaluation, even on strict cells: 4270 in the generator and 589 in
the checker. The initial generator omitted that auxiliary value-bound
charge from its counter; the checker reconstructs and records it from
the full finite loop structure. This changes no interval or stop
decision. There were no failed numerical executions in this step.
Including the corrected inherited 166413 callbacks gives

    166413+1833+10971+76944+4270+589=261020<262144.

The five distinct response centers across the inherited and new
calculations, 14 new transport slabs (15 including the old tiny core),
32 reused cutoffs, 1848 leaves and 24 decimal places meet the original
caps. The inherited nondegenerate core already meets the feasibility
condition. Remaining work cannot evaluate one complete additional
derivative slab on this partition. The attempt stops without retrying
M_*, sampling, joint subdivision or signed polynomial expectations.
This bounded failure and the partial anchor do not change the main
argument or any RH range.

## Mathlib

Full matching coverage for this literal selector-specific numerical
certificate is not checked. Supporting integration, mean-value,
Markov or interval results would not verify its numerical margins.
No Lean verification or absence claim is made.
