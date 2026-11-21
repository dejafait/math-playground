# Central discrete/mixed pairing attempt — step602

Work in progress under the pre-existing SPECIALIZE assessment
`drafts/literature/2026-11-05-central-discrete-pairing-test.md`.
The main gap is actual-Xi all-degree mixed positivity. The bounded target
is exact compatibility of L791's three central quotients with the (R2)
discrete/mixed sufficient regime, with variable positive parameters and
both pairings. A uniform obstruction stops this regime; exact unbounded
feasibility or a discriminating surviving necessary condition permits
further development. Separation and signed transfer remain independent.

L791's full enclosure/normalization and audit, L817's fixed-tuple stop,
L818's strict-growing-gap stop and step601's completed primary-source
comparison have been read. No source reproof, root scan or new evaluator
is planned. L791's analytic/data/software qualifications are retained.

Candidate elimination: set a=1/(A+1), c=1/(C+1), x=1/(B+1),
y=1/(D+1), all in (0,1), and p=a+c, r=ac, s=x+y, t=xy.
The three exact equations become

    1-p+r = q_0(1-s+t),
    1+s+t = q_1(1+p+r),
    1+2s+4t = q_1*q_2(1+2p+4r).

These are affine constraints. At this initial checkpoint the pending test
was whether positivity, quadratic-root feasibility and the paired gap
restrictions contradict them uniformly; no conclusion was yet claimed.

Completed: L819 records the full elimination and exact interval proof of
the cap d<=151. The final rational certificate passes 36 checks. The
first-pass auxiliary positivity-bound failure and all midpoint diagnostics
are preserved under scripts/central-jacobi; none of the midpoint values
is a proof premise. See the canonical lemma and step602 history for the
result and limitations. Independent audit remains pending.
