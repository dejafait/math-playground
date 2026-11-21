# Step 197: actual signed remainder versus residue

Approved target: the unchanged EXPLORE assessment
`literature/2026-11-03-signed-bump-remainder-rate.md`, exactly its TARGET.
Main gap: actual-Xi all-degree mixed positivity. This bounded calculation
tests the positive-bump residue comparison at the original spatial peak.
Independent complementary-defect, other-response, angular, full-charge,
H/support and realization gaps remain.

Inputs checked: L714's audited R_n=P_n+K_n and its as-yet unaudited
Section 4 residue-rate proof; L719's audited saddle/phase interface;
L721's audited signed limsup and derivative bounds. The prior step-175
reduction, common-phase and gamma/Rice failures are distinct and remain
preserved. No replacement bump, endpoint law or interpolated size is used.

Continuation test: certify a strict gap between r(b)=Re S(b) and the
actual residue rate, with b=sup supp chi. Then the exact signed sum has
the larger limsup, but no full limit or eventual nonvanishing follows.
If the numerical bounds overlap, retain the exact overlap rather than
substituting the absolute contour envelope.

Partial reasoning saved before certification: diagnostic quadrature only
suggests r(omega) about 0.00570 and the residue rate about 0.000168.
No diagnostic value is proof. A rational saddle comparison at
s0=(73/40)(1-i), using L719's rectangle and |Phi_ss|<1/2, costs at most
1/3200 in real phase. Exact logarithm quadrature for that fixed s0 can
therefore certify r(omega)>1/200. Separately certify the residue upper
rate <1/5000 using its actual support b<=omega+1/3000. Verify the
positive-bump endpoint argument and bounded-derivative Riemann sum
before using L714 (6). No bound for the outer signed integral is inferred
until L721 is explicitly applied. Script and proof are still pending.

Completed: [L722](../lemmas/L722-actual-signed-remainder-residue-rate-gap.md)
contains the full proof and certificate reproduction command. All ten
exact checks pass; the full checks object was inspected. The actual
signed R_n has limsup r(b)>1/200 and the actual P_n full rate is below
1/5000. The ratio has limsup rate >3/625. This supplies competing
signed growth on an infinite subsequence, not a full limit or a bound
for the other complete-family responses. Outcome NEGATIVE for the
proposed exponentially subordinate remainder certificate; critical
audit of the new local result remains pending.
