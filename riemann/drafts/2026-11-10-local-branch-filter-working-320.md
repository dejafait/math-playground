# Local branch filter attempt — step320

10 November 2026. RESEARCH under the pre-invocation EXPLORE assessment
`drafts/literature/2026-11-10-local-frequency-branch-recovery-review-318.md`.
The supplied assessment is reused unchanged. No source gate is being
derived and approved during this attempt.

Main gap: actual-Xi positivity L030-L032/C032a, signed forcing L966/L968,
and the compensated hypothesis L984(H) remain unpaid. The sole target is
the saved bounded complex-linear local branch-recovery operator, from
C([7/4,9/4]) to C([15/8,17/8]), for every finite complex slope measure.
Its possible downstream use is branch information for a later localization
or continuation test; it is not actual reconstruction or a positivity proof.

Passing test: one operator sequence has a fixed positive absolute
slope-TV error exponent and meets EVERY positive exponential operator-norm
allowance, uniformly on the closed output interval and for all large n.
An exact-range incompatible lower tradeoff would stop the target. Failure
of a single filter is inconclusive. Keep all quartet terms, both short
intervals, beta reflection and K's constant subtraction.

Inputs read: L997 hypotheses and (4)-(8); C997a hypotheses, (1)-(2),
exact quartet/phase reduction and (18)-(19). Recorded fixed-bump,
dual-rate, interpolation, Chebyshev and whole-boundary propagation stops
are scope comparisons, not premises for an all-operator obstruction.

Initial reasoning saved before the quantitative attempt: realize the
finite response directly as the sum of two Fourier measures, paying TV
from the finite integrals rather than inferring it from a signal sup norm.
Test a local sign filter with a genuine finite-measure kernel so its action
extends to all continuous inputs. The nearest endpoint margin is 1/8;
the upper short interval carries exp(c*n/8), so a merely formal sign
approximation rate is insufficient. Investigate the full accessible
interval before discarding its asymmetric part. No operator or rate is
claimed at this checkpoint. No cross-notebook input or numerical evidence.

## Construction reached before full write-up

Use shifts Delta=3/(4n), m=floor((n-6)/12), degree d=2m+1. Then
d*Delta<=1/8. For n>=48 all upper frequencies obey
sin(t*Delta)>=24/25, while the negative frequencies obey the opposite
inequality. This uses the complete upper support [7n/4,9(n+2)/4], not
a limiting carrier. The lower interval has TV O(n*exp(-n/16))*||mu||.

Set s=24/25, r=1/49, z(x)=(1250*x^2-1201)/49. If P_j is defined by
(1-2*z*u+u^2)^(-1/2)=sum_j P_j(z)u^j, the candidate sign polynomial is
F_m(x)=(50/49)*x*sum_(j=0)^m (-1/49)^j P_j(z(x)). The generalized
binomial theorem gives |P_j(z)|<=1 on [-1,1] and <=49^j on
[-1201/49,1]. Hence |F_m|<=50(m+1)/49 on [-1,1], and its sign error
on |x|>=24/25 is <=(25/24)*49^(-(m+1)). These bounds require the
complete coefficient proof in the canonical file; no unproved optimal
approximation theorem or Legendre asymptotic is being imported.

Take the finite-shift operator with multiplier (1+F_m(sin(t*Delta)))/2.
Its Fourier-coefficient l1 bound gives norm <=n^2. On the upper interval
the error rate is rho=log(49)/12-9/32>1/32; lower-interval error is
O(n^3*exp(-n/16))*||mu||. Thus polynomial factors can be absorbed into
one fixed exp(-n/32) bound. All of this remains unaudited until the full
finite-measure realization, factors, and endpoint accounting are checked.

## Completed disposition

The complete construction and all-n proof are now canonical in
[C997c](../lemmas/C997c-local-positive-branch-recovery.md), including the
original K, both intervals and both beta terms. The finite-shift norm is
at most n^2 for n>=48 and the absolute slope-TV error is at most
C*exp(-n/32). The exact scalar certificate has 18 passing checks; its
complete checks were inspected. It supports arithmetic only.

Outcome ADVANCE / REPRODUCTION: an elementary polynomial sign-filter
specialization pays the local operator contract. Independent audit is
pending and no originality or actual-Xi consequence is claimed. This
does not revive the stopped fixed-bump, Chebyshev, interpolation or
whole-boundary certificates. The continuation is separate source/scope
approval for a critical audit; its new assessment is REVIEW_REQUIRED.
