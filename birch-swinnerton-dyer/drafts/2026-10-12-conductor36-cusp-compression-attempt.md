# BSD-178 — approved finite cusp-compression test

The unchanged SPECIALIZE assessment is
`drafts/literature/2026-10-12-conductor36-cusp-class-compression.md`.
This is one implementation attempt, not additional literature work.
The main gap remains rank equality for arbitrary analytic order >=2.
The intermediate target is the complete compressed endpoint plan under
the exact saved cutoff/term/two-sided-tail limits. Its downstream use
would be a feasible full conductor-36 normalized integration table, not
a useful L027 coefficient on this CM curve or a BSD candidate.

Essential inputs are L038's saved N=36 presentation (its new instance
still awaits separate audit), audited L049 transport/closing/tails,
L050's exact curve and conductor, audited L051 finite coefficients and
positive period, and audited L052's clearing integer 24. No other
notebook is used. The source assessment has already compared known
algorithms and ATTEMPTS/025--026; these stops remain preserved.

Plan: collect every original homogeneous endpoint, start the cumulative
representative list with actual infinity, then encounter finite endpoints
in increasing denominator and numerator. Test equivalence using the
Bezout stabilizer congruence from Cremona Proposition 2.2.3; record both
assignments and independent pairwise inequivalence witnesses. For each
endpoint r and representative s construct gamma(s)=r. Wuthrich (11),
with L049's orientation, gives P(r)=P(s)+P(gamma tau)-P(tau).
Finite representatives use L049's full ell=37 closing, with every term;
P(infinity)=0. Positive balanced points are used for C!=0 and i for C=0.
Only witnessed integer real translations identify primitive keys.

Before workload measurement, replay every original generator as its own
endpoint difference. Reconstruct the occurrences, signed coefficients
and absolute error weights; repeated cached occurrences retain their
contribution to the conservative error sum. Choose a common primitive
radius from the maximum occurrence weight sum and L051's certified
positive lower total-period bound, then assign the first H meeting the
complete rational tail bound. Recompute each generator's normalized
two-sided tail width. This excludes finite arithmetic/period uncertainty
from a table-certification claim: those stages remain unperformed.

Continue only with zero complete-replay failures, max H<=4860 and
sum H over distinct required primitives<=1000000, and normalized full
tail width<=2^-38 on all 72 original generators. Otherwise preserve the
complete certificate and actual failed bounds; reassess the mechanism.
No new Fourier sums or point counts are authorized by this planning step.

Completed: the separate producer and verifier preserve the original
presentation, direct plan and all prior analytic evidence. Full finite
replay passes; both workload limits fail. See canonical
[L053](../lemmas/L053-conductor36-cusp-compression-workload-stop.md)
for the complete proof, exact weights/widths, all input qualifications and
the independently replayed cutoff obstruction. Outcome is
NEGATIVE/RESEARCH/REPRODUCTION, actual task implementation. This is a
useful local execution decision, not progress beyond the known methods
or a BSD candidate. No analytic table, coefficient or integer recovery
is claimed. A separate critical audit of this new finite plan is pending.

Stop this fixed ordinary ell=37 compressed schedule under its prescribed
tail convention, retaining ATTEMPTS/027. The next candidate is source
review of coupled T_5 closing on the same twelve cusp classes. This
changes the mechanism and is not yet covered or approved; its new
assessment is REVIEW_REQUIRED. PROOF's main mathematical assembly is
unchanged; DAG records L053's actual direct inputs only. Exploration
usage stays zero after this informative negative result. All independent
rational-direction, Sha, useful-coefficient and complex-order gaps remain.

Final inspection initially compared the structural actual/required
counter dictionaries for literal equality and failed: actual also has
the supplemental `segments` key (626), which required does not contain.
The corrected check compares every required count individually and
checks that `segments` is the only extra key; it passes. This did not
change the complete verifier, certificate or mathematical decision.
