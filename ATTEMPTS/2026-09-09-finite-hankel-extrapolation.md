# Attempt: infer all-degree positivity from increasingly many finite Hankel tests

Date: 2026-09-09

Outcome: failed finite-to-infinite inference; the finite actual-Ξ certificates remain valid.

The actual H_1 and H_2 have rigorous positive interval certificates. Lemma 57 shows that, for every fixed N, a comparison function F_{a_N} can satisfy all H_d>0 through d=N, together with every generic kernel/growth/zero-geometry property in Lemma 55, and still have nonreal zeros.

The proof starts with G, whose half-line energy argument proves real zeros and hence strict positivity of every finite Hankel matrix. The small-shift functions F_a tend to G in every fixed Taylor coefficient, so finitely many positive determinants persist for sufficiently small a>0. The inserted nonreal zeros remain at imaginary parts ±1/10 while their real parts tend to infinity.

**WHY IT FAILS.** A fixed finite collection of strict positivity tests is stable under small changes of finitely many coefficients, while nonreal zeros can be introduced arbitrarily far along the strip. Thus no finite number of these tests, even combined with all the established generic structural conditions, supplies the all-degree condition. The quantifiers are crucial: for each N a possibly different a_N is chosen; no single nonreal-zero function is claimed to pass every degree, which would contradict the proved criterion. A successful RH argument must control the entire family uniformly, using more specific information about Ξ.

Next lemma: return to the exact theta-series arithmetic structure and look for a uniform mechanism; further finite certificates alone cannot bridge the established gap.
