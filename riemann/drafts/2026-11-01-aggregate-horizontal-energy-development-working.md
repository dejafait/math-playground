# Two-packet energy: analytic development checkpoint

The unchanged approved EXPLORE target is the complete two-packet test
in `literature/2026-11-01-aggregate-horizontal-energy-test.md`.
L614 is read in full. Its (3) keeps the signed residual; its (6)
keeps all ordered multiplicities, including coincident real labels.
The previous reduction and floating diagnostic are preserved.

Main gap: actual-Xi all-degree signs at unbounded heights. Intermediate
target: prove or refute E>=M for the remaining inverse-order 1:2 branch.
A successful bounded test could support a later general energy/count
inequality; general extension, weight removal, charge conversion and
Xi signs are independent unresolved steps.

This attempt will compare the signed cross contribution directly with
the self-packet hyperbolic surplus. Start from L614 (5)--(6), using only
the already assessed triangular Fourier pair and finite norm identity.
An analytic lower bound covering the whole remaining parameter domain,
or a rigorous strict counterexample with all multiplicities, is decisive.
Failure of a sufficient bound or a nonnegative sample is not a verdict.

Source coverage and the L612/L613 contrasts are reused. No external
theorem is assumed to give M<=E. No new source review is needed for this
covered calculation. No mathematical result is asserted at this initial
checkpoint; partial reasoning will be retained here if the attempt ends.

## Small-depth route (provisional calculation)

For u<=1/20, L614 (8) reduces the inverse-order case to v=0.
Put f(a)=K(a)^2. The triangular Fourier identity gives

    F(a,u)>=f(a)-(u^2/2)f''(a)-R,
    R<=(2*pi*u)^4*cosh(2*pi*u)/360.

Thus E-M>=16f+u^2(8*pi^2/3-8f'')-16R. For 1/2<=a<=4/5,
f>=1/(4*pi^2), and |f''|<=2*pi^2/3; this is positive at
u<=1/20. For a>=4/5 use 16f/u^2>=6400f and write
s=sin(pi*a), c=cos(pi*a). Then

    6400f-8f''
      =[6400/(pi^2*a^2)+16/a^2-48/(pi^2*a^4)]s^2
         +64sc/(pi*a^3)-16c^2/a^2
      >=-25-100/253.

The last bound follows by completing the square, since the s^2
coefficient is >=6325/(pi^2*a^2). Also
16R/u^2 <= (32/45)*pi^4*(1/400)*cosh(pi/10)<0.19.
Together with pi>3.14 the remaining coefficient is positive.
These bounds require checking in the canonical proof before use.

For u>=1/20 the remaining set is compact. A directed interval proof
of L614 (6), using v=r*u with 0<=r<=1, would complement the analytic
small-depth argument. Such a cover must retain every box and rigorous
elementary-function bounds; a sampled grid would not suffice. Package
probes found neither mpmath nor python-flint in the available tested
interpreters; any certificate must use standard-library arithmetic or
remain unfinished. No new package installation is needed.

## Completed result

The complete proof is canonical in
[C614a](../lemmas/C614a-two-packet-horizontal-energy-domination.md).
The small-depth estimates were checked with exact rational constants.
For u>=1/2, the additional reduction E>=16[H(1/2)+F(a,1/2)] follows
from L614 (7); 256 interval cells bound its surplus above 3. The remaining
u in [3/64,1/2], v=r*u region is exhausted by 8,553 accepted interval
boxes, each with E-M>1/100000. All ordered multiplicities are retained.

The first direct cover up to u=2 hit its 300,000-box work cap. It is
preserved in `scripts/aggregate-energy/two-packet-cover-first-incomplete.json`;
it was not a sign counterexample or a full proof. The large-depth
reduction enabled the completed, smaller cover saved as
`scripts/aggregate-energy/two-packet-cover.json`. The standard-library
script includes outward rounding, rational Machin bounds, explicit
Taylor tails and a traversal checking the complete partition. It uses
no numerical library transcendental evaluations.

Outcome: local ADVANCE on the stipulated finite family, not a general
energy inequality or zeta advance. Independent proof/code audit is still
pending. Continue the same approved finite target by auditing C614a and
the L614 reductions it uses; the exact claim, assumptions and source
assessment are unchanged. No broader continuation has been approved.
