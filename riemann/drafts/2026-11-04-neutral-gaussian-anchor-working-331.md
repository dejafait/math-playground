# Fixed-test Gaussian anchor: working checkpoint, step 331

Approved target and source gate: the unchanged SPECIALIZE assessment
`literature/2026-11-04-neutral-gaussian-anchor-specialization.md`.
Main gap: complete actual-Xi neutral Weil positivity. This attempt only
supplies a possible positive-time starting sign; backward propagation is
independent. L751/L752's stopped absorption mechanism is not reopened.

Inputs read: L753 in full, L018, L024, the source comparison's primary
statement scopes and duplicate/failure record. No external reread or
mathematical script is required for this reproduction.

Provisional comparison: write A(z)=F(z)F^#(z), a=H^2-1/4,
b=gamma_*^2, delta=a-b>0. L753(10) and L024 give
sum |A(z_rho)|<infinity. On the whole complement |Re z|>H,
Re(z^2)>a, so its absolute contribution is at most
B_H exp(-2a tau), where B_H=sum_complement |A(z_rho)|.
The finite certified window is nonnegative and contains
c_*=multiplicity(gamma_*)|F(gamma_*)|^2>0 times exp(-2b tau).
Thus the required comparison is B_H exp(-2delta tau)<c_*.
Check reality, multiplicities, finiteness, B_H=0 and endpoint choices
before promoting this to the canonical proof. L753 may be used at any
individual tau by choosing a finite T>tau; no uniform derivative bound
on [0,infinity) is asserted.

Acceptance test: a summable bound for every complementary zero and
eventual ratio below one, with strict separation and nonvanishing kept
as hypotheses. No assertion for tests invisible on the certified window,
no numerical onset, no density extension, and no tau=0 sign.

Completed: the comparison and all listed threshold/reality checks are
written in C753a, with the full proof and source qualifications there.
No failure or unresolved analytic interchange was found in this attempt;
the new corollary awaits its separate critical audit. No mathematical
script or new external source was used.
