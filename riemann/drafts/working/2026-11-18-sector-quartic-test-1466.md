# Approved sector-quartic attempt1466 — partial reasoning

Gate: unchanged assessment1464, EXPLORE, approved in review1465.
The exact saved quartic witness/impossibility target is being attempted.
Main gap: actual-Xi all-degree positivity and exceptional-root deficit.
Acceptance: a fully certified restricted witness with counts (2,4), or
impossibility for the whole stated class. No degree sweep is authorized.

New calculation: for a normalized quadratic factor 1+a z+b z^2,
write t=b/a^2. The sector condition on a nonreal conjugate root pair
gives 1/4<t<=5/18. The inverse differential operator on degree<=4
has normalized moments 1,-1,2(1-t),-6(1-2t),24(1-3t+t^2).
Its 3-by-3 Hankel determinant at t=5/18 is 131/729>0, with
leading 2-by-2 minor 4/9>0. This suggests positivity on every
nonnegative quartic, which would exclude the required witness.

At the partial checkpoint, the interval, sum-of-squares argument,
composition and multiplicities were pending; the value at one endpoint
was not yet a proved count law.
Sympy is unavailable; exact rational arithmetic suffices and no package
installation is needed. No actual-Xi correspondence is assumed.

## Completion

The proof is now canonical in C020n. Its exact determinant expansion in
delta=5/18-t has coefficients 131/729,178/27,44/3,40, all positive.
Together with the leading minor >=4/9, this proves positive definiteness
on the whole interval. The factor/SOS/composition argument excludes the
requested (2,4) witness and, with the assumed universal preservation,
gives quartic contraction. Full rational algebra is saved and inspected
in certificate1466. A separate critical audit is nominated; this working
file preserves the partial reasoning and is not the canonical proof.
