# Actual reciprocal Jensen zero-persistence audit1502

Assessment1500, approved in step1501, is the unchanged SPECIALIZE gate.
The main gap is actual-Xi all-degree positivity. This step only tests the
one-fixed-nonreal-zero obstruction and the logical strength of H_d=o(d).
No upper bound, new zero or creative payment mechanism is assumed.

## Saved reasoning before completion

Set Q_d(u)=J_d(u/d)/gamma_0. The imported compact limit is Q_d->F.
For u!=0, Q_d(u)=(u/d)^d R_d(d/u)/gamma_0. Since gamma_0,gamma_d>0,
both polynomials have exact degree d and no zero at zero. Inversion
preserves multiplicity, so H_d/d=sum_(Q_d(u)=0)|Im(1/u)|.

For each epsilon>0 smaller than |Im(1/w)|, choose a fixed small disk
about a hypothetical nonreal F zero w, containing no other F zero and
avoiding zero, with |Im(1/u)|>=|Im(1/w)|-epsilon on the disk. Compact
convergence and Rouche give exactly m roots there for every sufficiently
large d. Retain these m nonnegative terms, take liminf, then epsilon->0.
This order of quantifiers requires no shrinking-disk convergence rate.

To complete: verify actual Theta convention/order, all hypotheses of
Corollary3.2 at shift zero, and both RH directions. L018/L021 give
F(-z^2)=Xi(z)/gamma_0 and F(x)>0 for x>=0. Thus absence of nonreal F
zeros forces all F zeros negative and then all Xi zeros real. Conversely
RH plus the imported Jensen criterion makes every J_d, hence R_d,
hyperbolic and H_d=0. Record this as a known-method specialization and
an equivalent criterion, never an RH resolution. No mathematical script
or numerical experiment is needed.

## Completion

Completed the displayed checks in canonical C028b. The proposed lower
bound and both directions hold, including multiple roots and all integer
degrees d>=3 in the limiting statement. The actual total-height upper
bound is still unproved. No conjugate-pair strengthening, sum over many
F zeros, rate, or further mechanism was attempted. Source coverage and
prior failure comparisons were reused; O'Sullivan Section1/Section3.1
and Tao Theorem37 were inspected at their direct primary URLs to check
the application. See C028b for the full proof and precise citations.
