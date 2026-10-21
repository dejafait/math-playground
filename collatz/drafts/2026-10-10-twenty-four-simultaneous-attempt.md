# Twenty-four-word simultaneous attempt

Approved target: exactly L051 (1)–(4) at r=24, under the unchanged
SPECIALIZE assessment `drafts/literature/2026-10-10-twenty-four-simultaneous-feasibility.md`.
Main gap: universal eventual descent. A contradiction here would extend
only the restricted postspell cycle exclusion; a fully guarded real
witness would instead identify a limitation of these necessary conditions.

Inputs read: L051's full system and product argument, L052's own-count
and transfer proof, L046's real-domain substitution and L041's own-index
bridge. Attempts 023/024 stop weaker fixed comparisons, not this system.
Known-source coverage is reused without new browsing or general reproof.

Work in progress: retain own counts and exact closing information at 24;
first assess the quantitative room left by L052's estimates, then test
whether the unchanged integer pair and the coupled endpoints close it.
Every tail is independent, every height guard has its own index, all 24
endpoints are required, and counts/scaling remain integer. No parity or
positive-integer realization of real heights will be inferred. The test
accepts only an all-parameter contradiction or a complete guarded witness;
otherwise record the precise unresolved constraint and stop this turn.

Published computational and transcendence qualifications persist; full
matching Mathlib and external Lean verification remain unchecked. Entry,
unrestricted cycles, divergence and descent remain unresolved.

## Provisional argument to certify

The unchanged rho=189/100 and odd-count factor 14/5 give R_24<4850000.
The seed/length estimate should give N<6900000000 on the whole ray;
positive Lambda gives K<2N/3. With the unchanged p,q this suffices for
Lambda>1/(4q), hence h_0<28 and K<393820000<394000000. It also gives
h_0>15 from the required lower bound on K.

If two distinct indexed heights were at most 30, split the cyclic
transfer sum at them. The bound R_j+R_(24-j)<=1+R_23 and R_23<2570000
would give K<(14/5)*31*2570001<225640000. Thus only index zero can
have h<=30. The product mass then has one small-height term and a
tail bounded by 10^-11.

Keep z=Nq-Kp. The identity 630138897*q-397573379*p=1 gives
K=397573379*z modulo q. In the necessary K interval, the finite range
1<=z<63 appears to permit only z=32, K=343857546. Its separation
and improved mass give h_0<21, contradicting its required K via the
coarse transfer sum. For z>=63 the same bounds appear to give h_0<98/5.
Propagate exact integer floors of both own-index guards from that upper
height, retaining the endpoint's -2 log2 and a rigorously bounded
positive shift. Exploratory arithmetic gives a total odd-count ceiling
below 225640000. This needs full rational certification and a written
induction, not floating-point extrapolation.

The decimal preliminary files are exploratory only. The first attempted
count 225644606 had a large positive linear form at the chosen ceiling
and an inadmissibly small estimated height; its negative greedy counts
are invalid as a witness and unused. Neither preliminary file establishes
feasibility or any part of the final proof.

## Completed attempt

The full proof is now canonical in
[L053](../lemmas/L053-twenty-four-word-simultaneous-infeasibility.md).
The exact certificate `scripts/postspell-word-count/twenty-four-height-certificate.json`
has 29 successful strict comparisons, a verified Bezout identity, all 62
residues and all 24 integer-floor rows. In the z=32 case the count would
be 343857546 but less than 298760000. For z>=63 it is at most 224363706,
below the required 225640000, with margin 1276294. The proof retains all
guards and endpoints and excludes the entire system, not just a screen.
The mathematical attempt is complete; separate critical review remains.
