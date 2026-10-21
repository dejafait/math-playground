# Paired-container test — reasoning checkpoint

Approved target: determine invariance of C=3^(-4)O intersect ker(Tr) under Kondo's reference paired actions, using L024's actual M=J intersect ker(Tr). Reuse the unchanged SPECIALIZE assessment dated 2026-10-06. Main gap remains original finite B>=A.

The displayed source words abelianize on e_i=y_(2i), f_i=y_(2i+1), i=1,...,13, to pair transvections f_i -> f_i+e_i and e_i -> e_i-f_i; the adjacent map sends e_i -> e_i-f_i+f_(i+1), e_(i+1) -> e_(i+1)+f_i-f_(i+1), fixing the f's. L019's reference transport acts on actual J, and L024 makes these an integral basis of M. Over F_3 a nonzero invariant subspace contains one e_i or f_i by a single-pair difference, then both, then both neighboring pairs by the adjacent differences. Thus it is all M/3M.

Normalize a hypothetical stable full lattice N by a power of 3 so N is contained in M but not in 3M. Its image modulo 3 is all; Nakayama on M/N gives N=M. This supplies scalar homothety within the same trace-zero rational space, not an abstract module isomorphism. The compact closure in GL(M) and closedness of C can be checked, although the direct proof only needs subgroup stability.

Set D=O intersect ker(Tr)=sum_(r=1)^26 Z_3 pi^r. By the COMPLETE L016 table and H, the pi^13 coordinate of J is integral; q_13=pi^12+pi^13 is trace zero, so this coordinate on M is exactly Z_3. Hence any equality M=3^k D forces k=0. But q_4=pi^4+pi^8+(pi^9+pi^12+pi^24)/3 belongs to M and not D. Thus M is not homothetic to D or C. Completed full write-up: L025 concludes noninvariance and uses determinant one to obtain a forward generator and a field-basis point witnessing failure. No prescribed coordinates for presentation generators are used.

Continue only after these transport, irreducibility and same-space homothety arguments check out. No script is needed: the load-bearing field facts are in L016's proved complete table. A concrete point in pi I, any sharp radius, native/actual-ind3 membership, original initial data, higher powers, pilot transport, essentiality and B>=A remain unproved. This is a field-specific specialization of inspected inputs, not a claimed essential IUT flaw or certified novelty.

Completed result is canonical in lemmas/L025-source-paired-actions-do-not-preserve-trace-zero-container.md. The next critical-audit target has REVIEW_REQUIRED coverage; no audit or mathematical extension was invoked here. Scoped documentation validation passed with 25 nodes and 32 edges; this structural check is not a proof audit.
