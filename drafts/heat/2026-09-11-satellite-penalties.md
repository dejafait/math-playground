# Satellite penalty checkpoint — 2026-09-11

The existing work through Lemma 72 is complete and preserved. Current step: test its satellites at η_n=(5/12)ε_n.

Draft calculation (not yet a proved DAG input): put t=2^{-n}. The center score is 1−(29/24)t. The satellite beats it because δ_n−η_n(2X_nd_n+d_n²)=d_n²[1−(5/12)(2+ε_n)]>0. Earlier clusters have height <1−(3/2)t. The next cluster has height <1−(7/16)t and penalty at least (5/6)t, giving score <1−(61/48)t, below the center. Clusters at least two later have penalty at least (10/3)t. These comparisons should give the exact satellite maximizing pair.

Resume by checking all constants, then writing the full proof. At a satellite all higher zeros lie in later clusters. Horizontal distances are at least 2^m/3, yielding S≤12·4^{-n} and E≤24·8^{-n}. Prove these bounds for the infinite sum, supplement with exact rational checks, update DAG/history/PROGRESS, and run structure validation. General favorable-sequence existence remains unproved.

Completed: Lemma 73 proves these comparisons and bounds. The supplementary rational checks passed. The sole active next action is in PROGRESS.md.
