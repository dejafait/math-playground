# Odd single-factor contact — bounded specialization

6 November 2026. Invocation-start target and SPECIALIZE coverage are
`drafts/literature/2026-11-06-odd-divisor-contact-scope.md`.
Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity.
This attempt tests only the approved necessary local restriction for
a global nonnegative collar extension, with all L858 qualifications.

Inputs read: L847 full form and angular Jacobian, L849 hypotheses and
exact smaller-collar conclusion, L858 hypotheses and accepted common-zero
exclusion. L855 is a contrast, not an input. Targeted duplicate/failure
search found no matching odd-contact restriction; the full-phase
two-period and automatic-linking stops remain preserved.

At a hypothetical contact p, let j be the vanishing G coordinate and
k the other one. Set zeta=z_j(p), eta=z_k(p), with zeta!=eta,
G(eta)!=0, and G(zeta+w)=w^n g(w), g(0)!=0, n finite odd.
L858 supplies J(p)!=0 since f(p)=0. On theta=p+t e_j,
z_j(theta)-zeta=v_j t+o(t), v_j=zeta(partial_j u_j(p)+i)!=0.
The full surviving coefficient is
-C g(z_j-zeta) G(z_k) (z_1-z_2)^2 J/(z_1^2 z_2^2),
continuous with nonzero value at p. Thus q(p+t e_j)/t^n tends
to a nonzero complex constant. Reality of q makes the limit real;
nonnegativity and odd n force opposite weak signs from the two sides,
which is impossible. This uses only first-order curve information and
continuity of J, not Cn regularity or a rank-two inverse theorem.

Completed: the full specialization, both coordinate choices and the
two-sided limit argument are canonical in C858b. This scratch record
is retained as the saved working checkpoint, not a second proof.
No claim about even/simultaneous contacts, forced contact, global
existence/nonexistence, or new Xi signs follows. The changed even-contact
feasibility target is nominated separately with REVIEW_REQUIRED;
no mathematical work on that target is included in this attempt.
