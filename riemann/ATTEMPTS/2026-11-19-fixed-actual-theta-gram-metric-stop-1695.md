# Fixed actual-theta Gram metric stop1695

WHY IT FAILS: For precisely the full measure K(|u|)du/Z, scale d and
upper Cholesky similarity S_d*A_d*S_d^(-1),
[C028o](../lemmas/C028o-actual-theta-gram-companion-cost-floor.md)
identifies the entire known Schmeisser cost and shows its ratio to d
tends to infinity. Its quadratic residual alone suffices; the unbounded
support implication is justified using finite polynomial moments.
Thus this cost cannot pay the C028b requirement H_d=o(d). This is a
floor on an upper majorant, with no lower bound on actual root heights
and no RH conclusion. Independent audit1697 in C028o confirms the
coordinate map, full cost, degree scaling and finite-moment argument. Other metrics
or scales are outside this attempt, and no variant is tested here.
