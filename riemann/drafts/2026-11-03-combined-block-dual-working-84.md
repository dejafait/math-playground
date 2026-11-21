# Combined spatial block dual — working step 84

The unchanged invocation-start EXPLORE assessment is
`drafts/literature/2026-11-03-inner-spatial-rational-response.md`.
The target remains its exact original-D joint resolvent estimate for
the full L666 displacement cube. The main gap is actual-Xi mixed
positivity; a successful norm bound could feed the unaudited L683
transfer, with H/support, realization and actual signs still separate.

Test a polynomial spatial dual p(v) that vanishes at a selected set
of discarded nodes and retains the signed response of the others.
For r=1/32, A=R/r=44 and C(p)=sum_k |p_k| A^k, Cauchy coefficient
extraction should give

    V >= |sum_a W_a(u) p(a)| / (R C(p)).

Keep the angular maximum and permit arbitrary further polynomial
factors, rather than assuming positivity of the retained block.
Continue this certificate only if its full cost permits a response
of order n exp(-n/48) sqrt(D). A uniform upper bound showing that
the certificate misses this scale is a certificate-specific stop,
not an upper bound on V or a full-cube countersequence.

Tentative obstruction: normalize p on the disk |v|<=A and remove its
K prescribed node zeros by finite disk factors
A(v-b)/(A^2-conjugate(b)*v). The maximum modulus principle would bound
every retained value by C(p) times the product of those factors.
L666's vertical diameter is <9/10, giving each factor <1/48 on the
whole family. L661's audited envelope is |W_a(u)|<=exp(91n/5000+3),
while the unchanged anchor gives D>=64/21. Thus K>=n/90 appears to
make even the best signed/angular certificate exponentially too small.
The removable-zero and coefficient-cost arguments, exact constants,
and distinction from a response upper bound still need checking.

Local comparisons: L686's stop uses a single anchor and an additive
undisplaced error; the present test retains an arbitrary block and
uses no baseline subtraction. L670/L671 concern complete angular
clearings and their coefficient/Mahler costs. L650's close-pair
example is not this separated L666 family. The prior assessment's
rational norm comparisons provide no missing original-D lower bound.
No new source or script is needed for this bounded test.

Completed: the proposed cost obstruction is proved in
[L687](../lemmas/L687-spatial-block-polynomial-dual-cost-stop.md).
The exact normalized upper bound for this lower certificate is
5*exp(-79*n/30000) when K>=n/90. The proof permits arbitrary extra
polynomial factors and angular optimization. It gives no upper bound
for V. This parks the specified block-elimination certificate; the
unchanged norm target remains ready, with a proposed Taylor multiplier
retaining all residues as a different bounded test. That multiplier's
signed response and tails are unproved; no such estimate was derived
in this step.
