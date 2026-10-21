# C001a — Universal safety through 955 errors on the fixed instance

## Hypotheses

Use the instance of C012a with Q=65537, F=F_(Q^28), H<=F_Q^*
of order n=1024, k=64, epsilon*=2^(-128), and any integer m>=1.
Messages have row degree strictly less than 64. Use the closed simultaneous
column-Hamming balls and worst-case list size B_m of the
[pinned model](../foundations/02-pinned-list-model.md). Let t_star(m) denote
the largest safe grid index at threshold epsilon*|F|.

## Conclusion

For every m>=1,

\[
 B_m(955/1024)\le
 428362352872699563702657106322646143607243699998589666549470379002425939061165475323889066117360
 <2^{318}<\varepsilon^*|F|,
 \qquad 955\le t_\star(m)\le957.
\]

Index 955 is the largest safe index **certified by L001's bound** on this
instance. At index 956 that upper bound exceeds the threshold; this does
not establish unsafety there. L019 establishes unsafety at 958. Consequently
the supremum of safe real radii lies in [956/1024,958/1024]; for each fixed
m the safe set is [0,(t_star(m)+1)/1024), with no attained real maximum.
The actual t_star(m), safety at 67 or 68 agreements, and comparison with
the unavailable ABF26 definition remain unresolved.

## Proof

**Applicability and known inputs.** C012a establishes the field and distinct
smooth subgroup, the admissible rate, and
2^320<epsilon*|F|=65537^28/2^128<2^321. L001 applies to every m directly
through common agreement columns; no exponent m is introduced. L019 supplies
t_star(m)<=957 on this same instance and threshold. These are established
local inputs, not new general list-decoding theorems. The prior
[SPECIALIZE assessment](../drafts/literature/2026-10-05-fixed-instance-support-bracket.md)
covers this exact finite-grid application; neither a Johnson theorem nor a
nested-floor refinement is applied or reproved here.

**Adjacent comparisons.** Put C=binomial(1024,64) and
U(t)=floor(C/binomial(1024-t,64)), for 0<=t<=960. Exact integer division gives

```text
binomial(69,64) = 11238513
U(955) = 428362352872699563702657106322646143607243699998589666549470379002425939061165475323889066117360
binomial(68,64) = 814385
U(956) = 5911400469643253979096668067252516781779963059980537398382691230233477959044083559469669112419568
```

Both divisions have remainder zero: multiplying each displayed U by its
displayed denominator gives C. Comparing integers yields
U(955)<2^318 and U(956)>2^321. Together with C012a's strict threshold bounds,
these prove U(955)<epsilon*|F|<U(956). In particular equality is not at issue.
L001 now proves safety at 955 for all centers and all m>=1.

**Maximality for this certificate.** For A>=64,
binomial(A+1,64)/binomial(A,64)=(A+1)/(A+1-64)>1.
Thus binomial(1024-t,64) decreases with t on the relevant grid and U(t)
is nondecreasing, even after flooring. Every t<=955 is certified safe,
and no t>=956 through 960 is certified by this inequality. L001's explicit
next-grid witness excludes 961 and monotonicity excludes all larger indices.
This proves maximality only for the stated certificate, not for the code's
actual safe set.

**Boundary assembly.** The threshold exceeds one, so L001 guarantees that
t_star(m) exists. The safety just proved and L019's unsafe index 958 give
955<=t_star(m)<=957. L001's closed-ball floor-cell argument gives the stated
safe real interval and its supremum bounds. These statements permit different
unknown t_star(m) for different m; uniform certificates do not imply equality
of those boundaries.

**Verification.** Run `python3 scripts/finite-support/fixed_instance_bracket.py`
from this notebook. It saves full exact evidence in
`scripts/finite-support/fixed-instance-bracket-results.json`: all 961
support-bound indices, integer quotient/remainder and ambient-threshold
comparisons, plus the pre-existing L019 averaging certificate comparison.
Factorial/product identities independently check the binomial values, and
all comparisons use integers. The two load-bearing adjacent entries were
inspected in full. There were no failures. The script checks arithmetic,
not exact list maxima; the proof above supplies the monotonicity and theorem
application.

## Mathlib

Full finite-instance corollary: **not checked** in Mathlib. The support bound
is the locally proved L001, not an assumed Mathlib result. The separate pinned
ArkLib boundary and floor-cell results cited in L001 and the pinned model
support the radius convention; they do not establish the new numeric bracket.
This is REPRODUCTION of established counting inputs, with local quantitative
progress and no claim of progress beyond the assessed mathematics.
