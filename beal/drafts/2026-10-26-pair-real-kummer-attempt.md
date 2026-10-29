# Real-place Kummer filter — bounded attempt

Started 2026-10-26 under the unchanged SPECIALIZE assessment
`drafts/literature/2026-10-26-pair-real-kummer-filter.md`.

Main gap: exclude residual primitive Beal solutions. Intermediate target:
certify positive real restriction codimension in L139’s ambient norm kernel.
This could lower a rank bound for later filtered descent; rank at most one,
point control and all lifting/signature obligations remain independent.

Inputs: L135’s four isolating intervals and maximal-order coordinates,
L136’s 182 full accepted records, L137’s seven S indices, L138’s actual
odd model and transport, audited L139, and Stoll Lemma 4.8. No cross-notebook
input. Preserve unfinished L108 and ATTEMPTS/050,059–061.

Protocol: retain exactly the prior elements with even valuations outside S;
append only -1,2,3,5,11. Certify signed norms and interval signs, the five-root
order, the complete real local image, and quotient rank. Caps: 187 candidates,
64 bisections per root, 4096-bit exact rational arithmetic, five coordinates
and at most 192 columns. Positive codimension permits a bound; zero ends
this fixed witness test; failed certification or caps permit no bound.

Completed: all 182 prior records were consumed; 34 pass and 148 fail the
support-parity filter. With five rational elements there are 39 witnesses.
The complete real image has dimension two and the witness quotient rank
is two. The bound becomes rank J(Q)<=8+c<=10, still nine above one.

Full proof, hypotheses, citation, decisive witness data and qualifications
are canonical in `lemmas/L140-pair-real-kummer-filter.md`. Full producer
and replay evidence is in `scripts/pair-genus-two/real-kummer-certificate.json`
and `real-kummer-verification.json`; independent replay passes 1118 checks.
Actual/cap: 39/187 witness rows, 5/5 coordinates, 43/192 columns,
(0,0,2,0)/64 bisections per root and 135/4096 observed rational bits.
No failures, upstream reruns, finite-place tests or enlarged search occurred.

The two-dimensional real norm quotient is fully detected, so this place
has no further dimension to remove from the same ambient group. Separate
critical-audit coverage is REVIEW_REQUIRED; the mathematical audit and
all independent point/recovery/signature obligations remain pending.
