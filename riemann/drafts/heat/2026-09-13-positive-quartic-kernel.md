# Positive quartic kernel checkpoint — 2026-09-13

L180 is complete. For this step write k=n1*n2*n3*n4, a±=(t±−π/2)/(2π),
t−=2T−h, t+=2T. The phase derivative is log(k/a(t)^2).
Thus stationary integer products are exactly a−²≤k≤a+².
Planned analytic bounds (not yet promoted): uniform kernel O(N/h),
nonstationary kernel O(1/(h*distance(log k,[2log a−,2log a+]))).
Separate a 1/N frequency collar before counting by fixing three indices.
Resume by proving these bounds via derivative splitting and integration by
parts, then count stationary and exterior contributions with bounded weights.

Completed: L181 proves the kernel bounds and the stationary/collar/exterior
counts. The stationary portion is only O(N) by absolute summation; the
exterior is O(N^(1/2)log(2N)). No sharper signed estimate is promoted.
The next research action is recorded only in PROGRESS.md.
