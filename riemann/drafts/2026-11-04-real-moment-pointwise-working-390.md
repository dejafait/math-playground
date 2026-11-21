# Approved real-integrand test — step390 working note

The invocation-start assessment `literature/2026-11-04-actual-toeplitz-signed-integral-review.md` covers exactly the current Next action. Preserve all earlier work. No alternative target is being tested.

Main gap: actual-Xi all-degree coefficient/mixed positivity. Intermediate target: the factorial-exact permutation average at k=r-1, u=(1,...,1,t), even r. A negative leading coefficient extending to an open ordered set stops only direct pointwise signing; integrated compensation and RH remain unresolved.

Inputs read: L018, L019, L021. L019 gives continuous strictly positive actual K and superexponential decay; L021 gives finite positive moments. Existing L765 norm stop is contrast only; supplied assessment already checked local overlap and literature.

Partial algebra to verify: put c_n=1/(2n)!, d_i=r-1-i. Factoring 8^(-r)4^(-r(r-1)) from the determinant leaves the row integral with entries c_(d_i+j) u_i^(2(d_i+j)). Permutation average is 1/r! times the sum over variable assignments. At the one-outlier family, it is 1/r times the sum over the r possible outlier rows. Its unique highest t-degree term is row0/column(r-1), degree4r-4, with sign (-1)^(r-1) and cofactor det[c_(r-2-i+j)]_(i,j=0)^(r-2). Need verify strict positivity of that specific inverse-even-factorial minor using the already covered Katkova statement, the normalization, convergence and open-neighborhood argument. No completed sign result claimed yet.

Completed: the above was the pre-work checkpoint, not the final status.
All listed checks are resolved in canonical L766; this draft preserves
the partial reasoning only. The NEGATIVE result and future source gate
are recorded in PROGRESS.md and history/2026-11-04-actual-real-moment-pointwise-test-390.md.
