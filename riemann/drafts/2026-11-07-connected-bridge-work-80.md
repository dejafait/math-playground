# Connected finite bridge — working record

Invocation target: the unchanged ready EXPLORE target in
`literature/2026-11-07-paired-fiber-finite-replacement-test.md`.
Essential inputs are L847's actual full form and L879's stationary
phase line. The paired clean strip remains conditional. Prior
attempt65/69 and L887–L891 are comparisons, not additional sign inputs.

The nominated field is v=(h*rho(x)*eta(Y),-h*Y*rho(x)*eta(Y)),
Y=(y-y0)/h, with rho=1 near [alpha,beta], compact support in (l,r),
and eta(Y)=exp(-Y^2/(1-Y^2)) for |Y|<1, zero otherwise.
The nominal h is min(y0-c,d-y0,1)/4. No supplied numerical graph or
uniform derivative bound determines its mass sign or endpoint J.
The test must retain that finite value; a smaller-width result must
be explicitly qualified and cannot certify the nominal endpoint.

Pre-estimate checkpoint: after rescaling y, the first derivative
column of Dv is h*rho'*(eta,-Y*eta), while the second is
rho*(eta',-eta-Y*eta'). Thus a narrow connected bridge has an O(1)
derivative perturbation over the whole middle cell. The corresponding
rank-one limiting determinant need not be nonzero for arbitrary Du.
At Y=0 its phase defect is nonzero at an interior point sufficiently
near either contact: at a contact Re[(I-iDu)^(-1)]_22=1/(1+k^2)>0.
This suggests a full middle-cell cost of order h, competing with
interface flux of order h^3. These orders are not yet a finite proof.

Bounded objective: derive a finite actual-G error bound over the
entire rescaled support and an explicit sufficient width threshold.
If proved, report a scoped obstruction only for widths satisfying
it, including the nominal width only when that inequality holds.
Do not assume endpoint nondegeneracy or infer graph realization.
No second construction or new source search is authorized this turn.

Checkpoint after the full-support calculation: write Dv_h=D0+h*D1,
where D0 has zero first column. At h=0 freeze only the actual base
graph on y=y0. Its determinant is affine in the second column of D0;
both components of that column have zero Y integral. Consequently
integral_{-1}^1 q0(x,Y)dY=2*Q(x,y0), for every x, including contacts.
The triangle inequality gives a nonnegative full coefficient m after
integrating in x. It is strictly positive: at Y=0 and x just inside
the middle cell near alpha, q0/Q=1+i*(H^(-1))_22 and
Re[(H^(-1))_22]>0, by continuity from the triangular contact matrix.
Thus a rectangle of positive measure fails alignment with Q.

This avoids any use of the unaudited interface formulas. Over the
compact rescaled full strip, both complex densities are smooth in h.
A uniform bound C for their h derivatives gives the finite bound
(2*pi)^2*Delta B >= h*(m-2*(r-l)*C*h). Hence every sufficiently
thin member increases mass, with no contact-slope restriction and
without needing endpoint invertibility for the inequality itself.
The nominal width remains undecided unless it meets this finite test.
An additional positive minimum of the limiting determinant supplies
a sufficient endpoint test; it is not implied by J of the base graph.

Final proof and qualifications are canonical in
`../lemmas/L892-connected-thin-bridge-full-mass-obstruction.md`.
This working note preserves the abandoned interface-flux estimate;
no flux sign or nominal-width mass sign was established.
