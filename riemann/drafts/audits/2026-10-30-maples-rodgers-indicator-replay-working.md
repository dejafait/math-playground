# Restricted Maples--Rodgers indicator replay

Research / conceptual audit, 2026-10-30. The unchanged prior SPECIALIZE
assessment is drafts/literature/2026-10-30-maples-rodgers-indicator-audit-coverage.md.
Existing notebook edits are preserved. No kernel application is undertaken.

The primary v2 HTML was reread at Theorem 2.4, Proposition 2.5, (8),
and Section 4 through (23). The count-only imports are Theorem 2.4
and Corollary 4.2. Their arithmetic proofs remain cited, not audited.
No local canonical lemma already names Maples--Rodgers/1404.3080.
The previous joint-Blaschke source/failure records were checked;
this is a restricted source replay, not a revival of that method.

Unfinished reasoning saved before completing uniformity checks:

- Put alpha=(sigma-1/2)log T and A_gamma(T)=(beta-1/2)log T.
  Use the upper-tail indicator only; (19) for arbitrary weights is
  not a premise. Negative ordinates and beta<1/2 cost fixed symmetry
  factors, with multiplicities preserved.
- At padding U=n^2 T, A_gamma(U)=A_gamma(T)log U/log T.
  Theorem 2.4 with b=1/2 should give a Q-weighted selected count
  O(T log T exp(-alpha/2)); check strict bin endpoints.
- Set a=2pi H/log T. The convolution of q_T=Q(./T)/T
  and Q(./a)=a q_a equals a q_(T+a). Check a/T uniformly bounded.
- Corollary 4.2 with exponent 3 and eta=Q_H should give the
  unselected third moment O(H^3). Must explicitly bound
  ||M_1 Q_H||_1 and epsilon_T(Q_H)log T, rather than merely
  repeat the source's assertion that epsilon tends to zero.
- The two Holder steps should give selected second moment
  O((H exp(-alpha/2))^(1/2)(H^3)^(1/2))
  =O(H^2 exp(-alpha/4)). The one-sided window has normalized
  length H/(2pi), so an explicit constant times Q_H dominates it.

The bullets above preserve the unfinished checkpoint, not current claims.
The completed replay is now canonical in
[L485](../../lemmas/L485-maples-rodgers-restricted-local-density-second-moment.md).
It recovers the exact uniform known estimate, including compact T,
strict endpoints and multiplicities. Its far-tail check also identifies
and repairs the source's incorrect convergence assertion at maximal H;
the proof retains the error term. No kernel application was performed.
The new continuation assessment is REVIEW_REQUIRED and makes no
mathematical approval in this turn. Arithmetic source proofs and Mathlib
coverage remain unaudited/unchecked as specified in L485.
