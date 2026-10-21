# Pair Jacobian rank — source review in progress

2026-10-20. Literature only; no rank computation or new mathematical
claim has been attempted. Target: the exact upper-bound action in
`drafts/literature/2026-10-20-pair-jacobian-rank-bound.md`.

Main gap: integer exclusion in the rational-plus-minus-three-pair branch
of ordered (3,5,11), with the other signatures still independent.
Intermediate target: a certified unconditional Jacobian rank upper
bound for L110, diagnostically below two. Such a bound could enable
later Chabauty; it does not recover the forgotten rational root or
resolve either L095 integer system.

Read L110's model/interface and exceptional charts, history/380, the
earlier explicit-model source assessment and the scoped rank/backend
failure records ATTEMPTS/032 and 045. They do not contain a rank result
for this curve. The old degree-twelve elliptic-unit obstruction is a
different Jacobian and is not imported here. L108 is untouched.

Sources inspected so far: Stoll, Acta Arith. 98 (2001), 245–277,
DOI 10.4064/aa98-3-4, introduction equation (1.1), Section 3 prerequisites,
Section 4 odd-degree setup and Lemma 4.1/Proposition 4.2; Magma online
handbook entries TwoSelmerGroup, TwoTorsionSubgroup, RankBound,
ClassGroup/proof bounds and Chabauty. The exact passages and final
decision will be recorded in the canonical literature assessment.

The public University of Sydney Magma calculator page is accessible
and advertises V2.29-10, a 60-second limit and 50,000-byte input limit.
This is a new possible bounded execution interface, not an executed
calculation or assurance that this instance will finish. Local PATH
probes found no magma, sage or gp; repeating that old prerequisite is
not mathematical evidence. Check the public submission interface by
read-only retrieval before approving a concrete future attempt.

Continue only if a bounded, reproducible, unconditional descent request
can be specified and its complete response retained. Timeout, transport
failure, conditional bounds or incomplete class/unit data do not give a
rank result. An upper bound at least two does not give a lower bound.

Completed: see the canonical upper-bound assessment and history/381.
No rank calculation followed these working notes. The independent
lower-bound proposal remains REVIEW_REQUIRED for the next invocation.
