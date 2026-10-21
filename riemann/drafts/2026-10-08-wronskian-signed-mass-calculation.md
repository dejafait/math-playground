# Signed-mass application — working checkpoint

Gate-approved target: Prove quantitative lower bounds for both signed masses of the actual normalized Wronskian on every sufficiently high dyadic interval using L380, L381 and the fixed-strip envelope of L320.

Main gap: global actual-theta mixed positivity and the total L367 margin.
Intermediate target: each normalized positive/negative mass is at least
c_* H^(-3/8) log H, with c_*>0 uniform in H. Potential downstream use:
Wronskian sign changes for later localization; exclusion of common-zero resets
is independent. Continue if this scale dominates the entire first-mean error;
otherwise stop this certificate with its precise failed comparison.

Prior SPECIALIZE coverage in
`drafts/literature/2026-10-08-wronskian-signed-mass-application.md` is reused.
The completed comparison's primary Holder endpoint qualifications, duplicate
checks and first-mean/common-reset warnings were read. No new source search
or fourth moment is needed. Essential inputs: L320 (4), L366 (1)-(2),
L368 (3)-(7), L380 (2), and audited L381 (1).

Working calculation: fix R=3/4 and completion disk radius rho=1/8. L320
gives exponent 17/8 with gamma decay on each disk; the real center A has
power 7/4 with the same decay, so Cauchy yields F_0/A and F_0'/A bounded
by C T^(3/8). Response jets are O(A T^2 L^j). Therefore Wcal is bounded
by C H^(3/8) on [H,2H]. With normalized dt/H, Q_H=<Wcal^2> is at least
(c/2)log H eventually, and the known endpoint inequality Q_H<=||Wcal||inf
<|Wcal|> gives <|Wcal|> >= c/(2C) H^(-3/8)log H. The mean error divided
by this lower scale is O(H^(-1/8)log H), tending to zero. The identities
<Wcal_+>=(<|Wcal|>+M_H)/2 and <Wcal_->=(<|Wcal|>-M_H)/2 then separate
both masses from zero. Constants/onset are existential, uniform in H.

Before canonical completion: write bounded height shifts, exact derivative
normalization, the full response series, complete first-mean terms and
second-moment little-o absorption. No division by zeta, discriminant,
simplicity, disjointness or common-zero-count assumption is used.

## Completed application

The complete disk, response-jet and signed-part estimates are now canonical
in `lemmas/L382-actual-wronskian-dyadic-signed-masses.md`. The proposed
thresholds are achieved; the working checkpoint above is preserved. This
is a local REPRODUCTION / ADVANCE, with no fourth moment or originality
claim. L382 awaits separate critical audit; its newly proposed continuation
has REVIEW_REQUIRED coverage and is not approved in this step.
