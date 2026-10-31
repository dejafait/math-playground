# Individual prime Stieltjes specialization: saved calculation

2026-10-30. Approved target and source gate:
`drafts/literature/2026-10-30-weil-individual-prime-stieltjes-specialization.md`.
Reuse Galerne (2016), Section 2 Lemma 1/Theorem 1 pp.951–953,
and the completed local comparison. No source refresh or new mechanism.

Main gap: L516 (6)'s signed eigenvalue-relative cancellation, then
actual-Xi positivity. Intermediate target: split L516 (3)'s aggregate
limit into absolutely convergent individual prime pairings under
L521's unchanged fixed-nullvector hypotheses. Possible use: expose
arithmetic terms for a later signed test. Pass only if moving tests,
both signs, centered dilation, sqrt(r), and equality atoms agree with
L516. Stop at a failed normalization or weak-* pairing. No signs,
family uniformity, H1 assertion, nullvector existence or Xi transfer.

Inputs read: L515 continuous compact zero extension; L516 statement
and proof through the aggregate/equality calculation; L521 hypotheses,
conclusion and audited closure; completed comparison's Correlation
applicability; scoped recovery record. No duplicate individual formula
in these paths; Abel and raw-adjoint stops remain. Mathlib unchecked.

Provisional derivation, to finish and check in the canonical result:
write v(x)=f(x+a), where f is L521's zero extension on (0,2a).
For a signed shift t=+/-d and h=t(1-1/r), change variables separately:

 <v,(T_(t/r)-T_t)U_r v>
   = integral [v(y+h)-v(y)] sqrt(r)v(r(y+t)) dy.

Thus dividing by r-1 gives (t/r) times the h-difference measure
paired with sqrt(r)v(r(y+t)). Galerne handles h of either sign.
The candidate limit is t integral v(y+t) Dv(dy), hence the pair
is d integral [v(y+d)-v(y-d)] Dv(dy). Need fully justify moving
C0 tests, coordinate conversion y->y+a, support equality and the
finite-sum passage. No new result beyond this approved application
has been attempted.

Completed: the provisional normalization passed and the full proof is
canonical in `lemmas/L522-individual-prime-stieltjes-dilation-limits.md`.
The bound used for moving tests is V times their supremum-norm error;
the latter tends to zero by compact continuity. The transported dilation
is W_r f(y)=sqrt(r)f(a+r(y-a)), not endpoint-centered dilation.
Both equality cutoffs have zero limit, without dropping their finite-r
terms. The finite prime sum agrees with L516. No sign or family saving
was attempted. The next application-audit scope is REVIEW_REQUIRED.
