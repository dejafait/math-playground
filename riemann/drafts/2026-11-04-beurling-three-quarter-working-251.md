# Beurling coefficient-1 specialization — working step 251

Approved target and prior coverage:
`drafts/literature/2026-11-04-beurling-three-quarter-specialization.md`
(SPECIALIZE, supplied at invocation). Completed work will be REPRODUCTION.

Main gap: unconditional actual-Xi mixed positivity. The bounded target is
one discrete, self-generated generalized-prime diagnostic at b=3/4.
Its downstream use is to test whether this multiplicative consistency
and a coarse O(x) remainder already exclude the power defect; no ordinary
prime, prefix-energy or Xi transfer is intended.

Continue only if the nominated cutoff template satisfies every
Broucke–Vindas Theorem 1.2 hypothesis, weighted prime counts retain
coefficient 1, higher prime powers are o(x^(3/4)), and the same-system
convolution is O(x) at all real endpoints. Stop on an unpaid hypothesis
or any need for unproved regularity of generalized integers.

Initial proof plan (not yet verified): bound pi-F by 1, use finite
partial summation to obtain theta=x-x^(3/4)+O(log x); use the actual
first prime to truncate the power sum and bound higher powers by
O(sqrt(x) log x). Extend |R(t)|<=C t^(3/4) and psi(t)<=A t to t>=1
using local finiteness. Then finite partial summation with the system's
own Lambda should bound the convolution by 4ACx. Keep the logarithmic
term and atoms at equality. No N_P estimate, Euler-product continuation,
prescribed zero or zero multiplicity is assumed.

The omitted source comparison and the canonical L734 proof/stop have
been read. L734 is comparison context only: its ordinary kernel and
positive power profile are not inputs to the new system. The source
construction is imported rather than reproved; no additional literature
review is needed for the unchanged target. Mathlib coverage is unknown.

Completed: the full proof is canonical in
`lemmas/L735-discrete-beurling-self-generated-power-diagnostic.md`.
Every proposed obligation above was resolved. The power tail uses the
actual log p_1, and compact-range control follows from local finiteness.
The final bound is B=4C(A+1/e), with A=1+C and C defined there.
This working plan is preserved as a record of the pre-proof checkpoint;
it is not a second proof or a current next-action record.
