# Marked Jacobian rational two-torsion — work in progress

2026-10-24. Approved target: determine J(Q)[2] for L113 by complete even branch partitions, including complement exchange. Prior SPECIALIZE assessment: drafts/literature/2026-10-24-marked-jacobian-rational-two-torsion.md.

Main gap: global positive primitive integer nonexistence; this target may fix a torsion term in a later Jacobian descent/rank bound. Inputs: L113 smooth actual marked model, L114 support convention, audited L115 entire irreducible octic, audited L116 field discriminant. Reuse primary even-partition theorem and finite quadratic-field coverage already assessed. ATTEMPTS/050 concerns another Jacobian; ATTEMPTS/052 class backend and ATTEMPTS/055 finite pruning remain parked.

Bound: all signed squarefree divisors of 330 except 1. Need complete factorization and quartic/complement certificates for every candidate, plus partition generators. Accept only complete exact evidence; park any uncertified absence case. No group value is yet claimed. Preserve all prior work. Full supported arithmetic, point control, degree-nine recovery, remaining factors, both L095 systems and minus-eleven remain unresolved.

## Completed bounded calculation

L126 is the canonical proof. The full producer certificate is scripts/pair-genus-two/marked-jacobian-two-torsion-certificate.json (122/122 checks); the independent replay is scripts/pair-genus-two/marked-jacobian-two-torsion-replay.json (1,520/1,520 checks). Complete modular factorizations at 7,13,19,29,31,43 and exact split witnesses cover every one of the 31 quadratic candidates and rule out quartic divisors. The full relevant modular witness and covering fields were inspected. The resulting exact group is J(Q)[2]={0}, with no nonzero generators. Separate critical audit is pending.

Implementation choice: active Python had no SymPy; an already installed Python 2.7/SymPy 0.7.4.1 provided exploratory factor suggestions. Its assertions are not proof inputs. The final standard-library certificate proves irreducibility of every suggested modular factor and the complete products, and the independent standard-library replay verifies every recorded identity. This complete absence method fits the approved exact-factorization target; no Trager norm or factorization-algorithm correctness assertion is needed. In particular d=33 is excluded at 29, rather than treating original irreducibility at 19 as sufficient for every quadratic field.

Outcome: a local input by reproduction of known methods, not a new general theorem or a Beal resolution. Mathematical exploration usage remains zero. Next continuation is a separate approval of the critical-audit scope, registered REVIEW_REQUIRED; original stops and unresolved assumptions remain intact.
