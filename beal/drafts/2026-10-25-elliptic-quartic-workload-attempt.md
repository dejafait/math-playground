# Elliptic quartic-descent workload attempt

2026-10-25. Completed under the unchanged SPECIALIZE assessment
`drafts/literature/2026-10-25-marked-elliptic-explicit-two-descent.md`.
The intermediate target is an elliptic upper rank one for use in L127;
the main residual Beal exclusion and point/lift obligations stay open.

L112 supplies the exact model and lower rank one. ATTEMPTS/050–052
were checked; no backend probe or renewed rank-zero search is involved.
The imported method is Cremona, corrected second edition, III.3.1–3.2
and III.3.6, pp.91–94. This is instance arithmetic, not a new method.

The exact candidate normalization is x=4X, y=8Y+4, giving
Y²+Y=X³−179685X+27177356. The minimal invariants to certify are
c4=8624880, c6=−23481235800. Their descent pair is
I=8624880, J=−46962471600. The larger dyadic pair should be
omitted by the sufficient criterion on p.92; verify every divisibility.

Important scratch correction: dividing the original c4,c6 by 6⁴,6⁶
gives integers but a nonintegral discriminant, hence is not a valid
integral normalization. Exploratory floor divisions were discarded;
no certificate or lemma used them. The script must check exact
divisibility, Kraus conditions and the rational transformation identity.

Continuation/abandonment test: exact rational isolation of the three
resolvent roots and outward coefficient bounds; stop the unsieved
implementation if the 200000 row or 2000000 triple cap is exceeded.
Analytic counts need not visit every row. No Selmer or rank upper bound
can be claimed from a workload stop.

Completion: L128 is the canonical proof. Exact arithmetic certifies
3834148 raw rows and a triple lower bound 2199936, exceeding the
respective caps. No enumeration ran. The certificate has 19 passing
checks, no failures; all relevant fields were inspected in full.
ATTEMPTS/053 preserves the stop. A different traversal through
syzygy-admissible seminvariants is proposed for separate source review.
