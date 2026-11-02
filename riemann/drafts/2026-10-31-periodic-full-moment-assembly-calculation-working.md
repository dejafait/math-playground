# Periodic probability assembly: calculation checkpoint

Approved target: the exact TARGET in the supplied
`literature/2026-10-31-periodic-full-moment-probability-assembly.md`.
Reuse its SPECIALIZE coverage and recorded packet/exact-law/budget stops.

Proposed finite construction, before canonical verification: use L586
to choose one fixed L>=1 with K-R/L in the restricted spectral cone.
Choose finite unit-jet representations of K and K-R/L once. For
ell>=L interpolate these representations with coefficients 1-L/ell
and L/ell. The combined covariance is K-R/ell and the sum of weights
is bounded by one fixed W_2. No varying-node selection theorem is needed.

Give the L585 paths amplitude ell^2 and masses a_i ell^(-4). Their
covariance is R and their fourth tensor is ell^4 q. Give the second
dictionary amplitude sqrt(B ell), B=max(1,4W_2), and masses b_j(ell)/B.
Their covariance is ell K-R, mass <=1/4, fourth entries bounded by
B W_2 ell^2, and phasewise support <=sqrt(B ell). Fill with the zero
path after requiring W_4 ell^(-4)<=1/4. Check ell^3>=B for support.
All second moments should then be exactly ell K, including the four
zero odd entries; use only L473's qualified reference asymptotics to
deduce all 147 tolerances on one real-H ray.

This is a standard finite-mixture specialization. Positive clipped
mass and actual-Xi transfer do not follow. L586's separate critical
audit and L473's imported arithmetic proofs remain pending. No
numerical paths, weights or onset are supplied. Full proof to be saved
canonically only after the mass, homogeneity and quantifiers checks.

Completed: the finite interpolation, mixture masses, every-phase support,
all 21 second and 126 fourth entries, and common real-H onset are proved
in `../lemmas/L587-bounded-periodic-full-moment-probability-assembly.md`.
No mathematical script was needed: all inequalities are finite exact
algebra. L586/L587 still require a separate critical application audit.
