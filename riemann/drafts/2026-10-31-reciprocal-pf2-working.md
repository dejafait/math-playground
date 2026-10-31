# Fixed reciprocal-PF2 diagnostic: work in progress

Approved target: the exact polynomial and simultaneous density/jet test in
`drafts/literature/2026-10-31-reciprocal-pf2-first-sign-model.md`.
Main gap: actual-Xi first sign at unbounded heights (C233a/L233), with
higher signs still independent. The fixed diagnostic can only obstruct
PF2-only transfer; it imports no actual-Xi realization or PF256 property.

Plan: determine the unique rational inverse as a finite even exponential
sum by exact partial fractions; check its transform and matching at zero;
certify positivity and curvature on the whole line, or reject the model.
Check the polynomial jet exactly. No parameter tuning is authorized.
Canonical result and certificate will retain all relevant evidence.

Existing unfinished changes are preserved. Prior source assessment and
comparison to L049/L055/L233/L356/L559 reused; these are contrasts, not
mathematical dependencies of the finite calculation.

Exact inversion candidate obtained with rational Gaussian arithmetic:
for x>=0, p=A exp(-x)+B exp(-2x)+exp(-10x)(C cos(x/4)+D sin(x/4)),
where A>0, B<0, C,D>0. Exact jets give p'(0+)=p'''(0+)=0.
The polynomial first sign at 10 is exactly negative.

Promising global proof: p >= (A+B-C-D)exp(-x)>0.
Writing curvature times exp(3x) as
b+exp(-8x)(u_r cos(x/4)+u_i sin(x/4))
 +exp(-9x)(v_r cos(x/4)+v_i sin(x/4))+k exp(-17x),
find b,k,v_r,v_i>0 and u_r,u_i<0.
On [0,1] drop positive v,k terms and use cos<=1, sin<=x/4;
exp(-8x)(-u_r-u_i*x/4) decreases because -u_i/4<=8*(-u_r).
Thus the lower bound is b+u_r>0. For x>=1, use |sin|,|cos|<=1
and exp(-8)<1/256, exp(-9)<1/512; the resulting rational lower
bound is positive. The complete exact identity/certificate remains to
be written and checked; these notes do not yet claim the conclusion.

Completed: both claims are proved in L560 with exact global bounds.
The certificate and script are under scripts/reciprocal-pf2/. The
log-concavity-only transfer is stopped; PF256 and actual Xi remain
outside the test. Independent audit is nominated under the separate
next assessment. No unresolved calculation is hidden in these notes.
