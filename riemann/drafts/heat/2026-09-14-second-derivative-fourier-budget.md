# Second-derivative Fourier budget checkpoint — 2026-09-14

The current task is to bound L230's finite paired Fourier sum in b.
Writing t=k/e, both phase curvatures are comparable to t because
alpha''=-(av)^2/(4 alpha^3), beta''=-[a(v+1)]^2/(4 beta^3).
The interval length is comparable to M=h/N. The standard bound is
O(M sqrt(t)+1/sqrt(t)), capped by O(M).

Draft calculation: preserve the pair as exp(2 pi i t alpha) times
1-exp(2 pi i t ell). Since ell=O(1), ell'=O(1/N), this gains
min(1,t) for t<=1 after partial summation. For t>=1 use the two
separate bounds. Summing the resulting estimates is expected to
leave a logarithmic high-frequency cost and no saving at e=k=1.
Unproved checkpoint: check the variation, summed powers, and comparison
with B_0 before making any lemma claim. Resume with those checks.

Completed in L231: the paired amplitude bound and frequency sums are
proved. The second-derivative test yields no saving for k>=e; the
uniform sawtooth estimate is stronger but still insufficient. No
cancellation claim has been promoted from this draft.
