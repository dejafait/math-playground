# Recentered Jensen audit — 2026-09-11

Checkpoint: prior L134 work is complete and preserved. The present step audits only the proposed deduction of logarithmic local counts, not a new zero-motion argument.

Candidate reduction (unproved at this checkpoint): under a common strip |Im z|≤H, center the unit window at c=x+1/2+i(H+1). Choose r=1+sqrt(1/4+(2H+1)^2) and outer radius 2r. The window lies strictly inside the inner disk. Jensen bounds its full count by log(M(2r)/|F(c)|)/log 2 when F(c)≠0. A uniform polynomial bound for this ratio would suffice. A common strip ensures nonvanishing at c, but not a quantitative lower bound as |x|→∞.

The integral has |cos(zu)|≤exp(|Im z|u), so L063's integral majorant supplies an upper bound independent of x on these disks. The positive lower bound at zero in L130 does not translate through an oscillatory cosine. Resume by verifying constants, boundary circles, compact-x uniformity, and distinguishing the relative maximum/value condition from the stronger condition using the coarse absolute upper bound. Do not promote the missing condition to a proved theta estimate.

Completed: L135 proves the conditional reduction and compact-window bound. The uniform logarithmic ratio estimate remains explicitly unproved; the failed inference from existing normalization is archived under ATTEMPTS.
