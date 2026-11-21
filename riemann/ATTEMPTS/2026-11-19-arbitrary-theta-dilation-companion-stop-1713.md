# Arbitrary positive theta dilation companion cost — stop1713

WHY IT FAILS: [C028p](../lemmas/C028p-arbitrary-theta-dilation-companion-cost-floor.md)
proves K_d(s)>=min{sqrt(S_2)/2,4*S_3/(27*S_2)}*d for every d>=3
and every s>0 in the nominated full-theta Gram family. The quadratic
and actual cubic residuals trade off: positive recurrence norm ratios
prevent both costs being small at any scale. Thus allowing arbitrary
degree-dependent positive dilation does not provide the proposed
o(d) majorant. This known-method specialization passed the independent
audit1715 in C028p and supplies no lower bound on actual H_d. It extends
the fixed-scale stop1695 without replacing or discarding that evidence.
Changed measure shapes and signed methods are outside this result;
reopening this exact cost requires a mathematical error or changed
input, rather than another scale search.
