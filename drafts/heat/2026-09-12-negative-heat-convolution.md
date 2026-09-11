# Negative heat convolution — 2026-09-12

Checkpoint: prior L134–L136 work is complete and preserved. Current step derives the Gaussian convolution for negative heat and audits cancellation only.

Candidate: for a>0, F(-a,z)=(4πa)^(-1/2)∫_R exp(-v²/(4a))F(0,z+v)dv. Fubini should follow from |cos((z+v)u)|≤exp(|Im z|u), independent of real v, and the L058 kernel bound. The Gaussian characteristic integral gives exp(-au²). Uniform compact convergence as a↓0 follows directly in the theta integral, but is not uniform relative control at centers escaping to infinity.

Resume checks: prove the Gaussian characteristic identity by integration by parts; derive a disk-majorant integral and isolate the exact center cancellation factor. Test the inference from positive averaging with f(z)=d+cos(bz), choosing d>0 so its negative-heat average vanishes at a prescribed nonreal center while f itself does not. This comparison is not a theta kernel or a counterexample to the desired theta estimate. All candidate statements remain unproved until audited.

Completed: L137 establishes the convolution, disk-majorant inequality with explicit cancellation factor, and uniform absolute O(a) convergence on horizontal strips. The finite-measure comparison verifies exact cancellation. No uniform relative theta bound or common strip has been proved; the candidate reasoning above is superseded by the audited lemma.
