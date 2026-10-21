# Cofactor-weighted energy: working checkpoint

The saved EXPLORE assessment is being reused for the exact approved
Parseval/Cauchy–Schwarz test. No new literature is required.

For incidence distribution I(v), write J_r for the squared norm of its
projection to the first r moment coordinates, r=2,3. Orthogonality gives
Q^-3 sum_{u_3!=0}|F_66(u)R(u)|^2 = J_3-J_2/Q. The cubic error is at most
sqrt((Q-1)/Q * (J_3-J_2/Q)); the signs and cofactor remain coupled here.
This is an exact collision identity, not yet an effective bound.

A possible effective fallback bounds cycle products in this weighted L2
norm. For c>=3, keep three cycle sums in Hölder and cap the others by
770; their normalized sixth moment is 6n^3-9n^2+4n, by Newton uniqueness
of triples. For c=1,2 use the second/fourth moments n and 2n^2-n.
Then use the complete cubic cofactor cap 769 and the signed sieve only
at the final L2 triangle inequality. Exact integer square-root ceilings
33,1448,80207 give a uniform list upper cap between 56 and 57 times
threshold (about 56.386), an improvement on the old support upper cap
above 1050 times threshold, but insufficient for family safety.

Completed in L017: the full proof, exact rational certificate and
order-8/F_17 cyclotomic audit are saved. Both collision projections and
the signed sieve normalization passed. The effective loss is the L2
triangle inequality over signed cycles. Stop that estimate; the remaining
precise test is to bound the signed collision energy at L017's margin
threshold. No actual large list has been enumerated and the full-code
radius is unchanged. The result reproduces standard tools and is an
informative negative threshold comparison.
