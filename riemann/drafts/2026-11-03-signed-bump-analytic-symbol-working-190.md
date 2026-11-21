# Integer-size analytic-symbol attempt — step 190

Invocation-start coverage: `literature/2026-11-03-signed-bump-analytic-symbol.md`
is EXPLORE for exactly the saved target. This is a mathematical attempt,
not another source review. Existing notebook changes are preserved.

Main gap: actual-Xi all-degree mixed positivity; locally the signed fixed
bump and complementary Jensen defect remain unpaid. Intermediate target:
the nominated elliptic factorial analytic symbol for p_n on a fixed complex
neighborhood of the original I. Its possible downstream use is a later
support-edge transfer theorem, which remains an independent gap.

Continue only with a uniform admissible contour, isolated nondegenerate
saddle, explicit separation and product remainders. A rigorous incompatible
contour condition is negative evidence for that template only; an unresolved
margin is inconclusive. No logarithmic limit or sampled picture suffices.

Inputs read: original L703 hypotheses; audited L714 finite inverse and
coefficient/root inputs; audited L715 F and L716 ratio including its tail
scope. Reused the supplied primary-source comparison and checked the five
preserved signed-bump/absolute-contour/blend failure records. No new external
theorem, noninteger size continuation or analytic bump is assumed.

## Work saved before the contour test

Candidate exact variable: s=(z+d)/u, with z the L714 rational Laplace
variable. Define R_n(s)=product_(k=1)^(n-1)(U+s*k/n) /
product_(j=0)^(n-1)(s+j/n). Its only poles are -j/n. A positively
oriented finite loop enclosing those poles and excluding alpha/u should
represent p_n by the residue integral of
exp(n*(u*s-d)*v/A)*R_n(s)/(alpha-u*s), times n*D_n/A.
The sign and normalization will be checked directly against L714 residues.

Candidate phase: Phi(s;v)=u*s*v/A+integral_0^1
[Log(U+s*t)-Log(s+t)]dt. Branch domains and any period around the
pole segment require care; only local expressions are proposed here.
The saddle equation is u*v/A=integral_0^1
[1/(s+t)-t/(U+s*t)]dt. This is a starting representation,
not a contour certificate or an asserted asymptotic.

The system python lacks mpmath. Any diagnostic uses the standard library,
saves all numerical output, and is explicitly noncertifying. No package
installation or numerical claim as proof is planned.

## Intermediate evidence saved

The noncertifying Newton/circle screen is saved in
`scripts/one-sided-hankel/analytic-symbol-contour-diagnostic-190.json`.
It suggested a circle centered at zero; its samples are not proof.
An independent exact rational certificate, using the audited L716 moment
formula, now encloses s(v)=-z_v F'(z_v) throughout the maximal real bump
interval: 9/5<Re(s)<37/20 and -37/20<Im(s)<-9/5. All fifteen checks in
`scripts/one-sided-hankel/analytic-symbol-saddle-certificate-190.json`
pass, with their complete exact check values inspected. Thus
5/2<|s|<21/8<11/4=|alpha/u|.

New contour mechanism: for radius r with r^2>U, each matched numerator /
denominator logarithmic-modulus factor is concave in c=cos(theta), since
U/(U^2+r^2*t^2+2*U*r*t*c) >=
1/(r^2+t^2+2*r*t*c). The difference after cross multiplication is
(r^2-U)*(U-t^2)>0. The lower semicircle's exponential contributes strict
concavity; the upper semicircle has a strictly smaller linear term.
This controls the entire finite product without a logarithm across its
negative-real numerator zeros. A common local logarithm exists at the
saddle. Full proof and qualifications are being saved canonically in L719.

The full analytic-symbol expansion remains unproved at this checkpoint.
The planned local conclusion is the contour/gap and its normalization,
not the signed bump rate or an RH claim.

## Completed attempt

The canonical partial proof is now in L719. It includes the exact complex
phase, beta=1/2, elliptic leading amplitude with O(1/n) relative error and
factorial local log-product estimates, in addition to the uniform contour.
These are not a complete analytic-symbol remainder theorem. The next
attempt remains the unchanged covered target, with the new input available
provisionally and its separate critical review still required. No signed
outer-rate or RH conclusion is asserted. The fifteen exact scalar checks
and scoped documentation validation pass. Outcome: ADVANCE, limited to
this unaudited intermediate input; full reasoning stays canonical in L719.
