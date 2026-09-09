# Attempt: the coarse zero strip and positive scalar sums imply mixed positivity

Date: 2026-09-09

Outcome: failed generic inference; the actual determinant remains uncomputed in sign.

For the actual Ξ, Lemma 26 puts every zero in |Re α|>4 and |Im α|<1/2, and Lemma 27 deduces S_k>0 for k=1,…,6. The first mixed Hankel determinant is D=S_2S_4-S_3², reduced exactly to moments in Lemma 33. The attempted shortcut was to infer D≥0 from the same argument bounds and scalar signs.

Take only the conjugate nodes c=(10+i/4)^{-2} and conj(c). Their T_k are positive for k=1,…,6 and their corresponding zero pairs obey the same geometric restrictions, yet T_2T_4-T_3²=-4|c|⁴(Im c)²<0.

**WHY IT FAILS.** Squaring and combining different power sums introduces the factor (c-conj(c))², which is negative rather than positive for a nonreal conjugate pair. Small arguments suffice to make individual real parts positive but do not turn this algebraic square into an absolute-value square. The example disproves the proposed consequence of strip geometry and scalar signs alone. It does not establish that the actual Ξ determinant is negative, nor does it claim the example has the full positive theta representation. The sign for Ξ requires a further estimate specific to its moments or zero distribution.

Next lemma: obtain certified bounds for the actual theta moments through M_8 and propagate them into D, or identify an analytic inequality strong enough to determine D directly. Uncertified decimal quadrature is insufficient.
