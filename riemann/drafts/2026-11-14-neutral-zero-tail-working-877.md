# Approved U12 tail specialization — working877

Invocation-start assessment876 is SPECIALIZE and matches the exact target.
One REPRODUCTION attempt; no finite Gram sign or RH claim.

Provisional analytic route, saved before final verification: exact moments
have |mu_p|>1 for p=1,2, while every |mu_k|<=16. Each neutral b therefore
has sine coefficient l1 norm <17. For either two-vector retained sector,
the full sine norm minus the cutoff loss gives Gram >=(T/5)I: only three
sine modes occur and the region where chi differs from1 has length T/10.
The L2 projection coefficients for any further b then have l1 norm <68,
so every exact e has sine coefficient l1 norm <1173.

Check the inherited cutoff bounds |theta'|<=5, |theta''|<=352. With
4<T<5, delta>1/10 and k*pi/T<12, obtain phi second derivative sup
<37000, hence ||phi||1+||phi''||1<200000. Cauchy--Schwarz over ten
coordinates would give ||f||1+||f''||1<10^9||c||2. L753(10), R=T,
b=1/2, N=2 would then yield A<=36*10^9||c||2.

Apply the cited BPT Lemma1 to phi(t)=t^-4, H=3*10^12, pass to infinity
with nonnegative partial sums, and double for both height signs. Proposed
coarse envelope: 91/(27H^3)+1687/(50H^4), using log H<30, pi>3.
Multiply by (36*10^9)^2 and check the strict comparison with 2*10^-16
by exact rational arithmetic. Pending: verify all inequalities and source
endpoint/convergence cases, write canonical result, then checkpoint.

Downstream use: pay the unverified-zero remainder of a later exact U12
finite Gram certificate. Its finite lower margin, finite-input errors,
infinite complement, non-neutral terms and global assembly are unresolved.
Continue only after all constants are verified; usefulness requires a
separate margin greater than this tail and every finite error. No sweep.

Completed877: the canonical proof is C750d. All proposed analytic bounds
were justified, and eleven exact scalar checks passed in
`scripts/neutral-zero-tail/certificate-877.json`. The result is an explicit
coefficient-space tail epsilon_*<2e-16, without any finite Gram margin.
The new proof awaits a separate audit; the finite-data route stays parked.
