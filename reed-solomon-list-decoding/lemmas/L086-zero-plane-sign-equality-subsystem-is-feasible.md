# L086 — The zero-plane sign/equality subsystem is rationally feasible

## Hypotheses

Keep L083's prescribed n=1024,w=68 family, L021's original pair
prescription and L053's positive singleton rho. All matrices are divided
by rho. Retain L073's included-anchor five/six/seven PSD base, L075's
entire immutable dictionary and original seven-column RREF/completion,
and L076's original four-parameter affine column family. In particular

    p8=16792471/1181138102168120460>0,
    t=(t56,t63,t69,t78), f=c+A_family*t, f>=0 (all 85 rows).

Set only t78=s, where s is exactly L083's stationary value. Write
u=(t56,t63,t69). Preserve all 90 weighted kernel equations, 500 full
unordered types/3000 presentations, original anchor and pair scaling,
36 forced eight/eight entries and 45 free entries. All ancestor PSD,
uniqueness, source-normalization and whole-kernel-exhaustion qualifications
remain imported. This is not a recursive critical review of those inputs.

Index the 45 free moments lexicographically by (r,q) with 0<=r,q<=8,
r+q>=8, and retain precisely L084's positive diagonal scaling

    V_rq=C(8,r)C(60,r)C(8,q)C(948,q)>0,
    Y_88(8-r,8-q)=p8*z_rq/V_rq.

Require z>=0 and exactly L084's 28 selected equalities E*z=b_I(u),
where I={9a+b:0<=a<=6,0<=b<=3}. No inequality from the other 53 modes,
scalar upper row, other-anchor condition or global moment extension is
imposed in this subsystem. All three coordinates of u remain free.

## Conclusion

This subsystem has an explicitly specified rational witness. All 85
domain rows hold: exactly indices 26,27,56 vanish and 82 factors are
positive. All 45 scaled and raw moments are nonnegative: 27 are positive
and precisely indices

    2,4,5,10,15,16,21,22,23,28,29,30,31,36,37,38,39,40

are zero. All 28 original selected equalities and their 28 unnormalized
raw Schur equalities hold exactly. Thus signs alone do not repair the
equality-only exclusion stopped by L084.

This is an informative negative result for that exclusion diagnostic,
RESEARCH / REPRODUCTION under the prior SPECIALIZE assessment. It is
local progress using known rational LP methods, with no claim of
source-level mathematical novelty. The other 53 PSD modes, scalar upper
rows, other anchors, global consistency, other pair/base/family choices
and RS realization remain undecided. The arbitrary-center 67/68-agreement
gap and bracket 955–957 are unchanged. The separate critical proof review
below retains this finite specialization with the same ancestral qualifications.

## Proof

**Imported methods and why specialization is needed.** The pre-invocation
assessment is `drafts/literature/2026-10-18-zero-plane-affine-sign-feasibility.md`.
Import Michel X. Goemans, *Advanced Algorithms*, Lecture 3, 19 September
2001, Theorems 1 and 3, printed pp.1–2,
[MIT primary notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/b23096080e3d2142c3c8337bdcd9d3c7_lect9_19.pdf),
for the finite linear feasibility alternative with free variables.
Import MIT 6.854 (2020 compilation),
[Notes 11](https://courses.csail.mit.edu/6.854/20/Notes/n11-lp.html),
Introduction, Linear Equalities and Basic Feasible Solutions, for
free-variable splitting, slacks and rational standard-form certificates.
For the concrete simplex step use Goemans, *An Introduction to Linear
Programming*, October 1994, The Simplex Method, printed pp.7–8,
[primary notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/908fe54d659623efadda2d033b895caf_notes_lp.pdf).
The artificial-sum initialization follows Giacomo Nannicini and Ebrahim
Nasrabadi, MIT 15.053, Spring 2013, *Recitation 3 solutions*, Problem
3.A–B, pp.4–6,
[primary worked notes](https://ocw.mit.edu/courses/15-053-optimization-methods-in-management-science-spring-2013/05885823def0372adb5eae09c7f5490d_MIT15_053S13_rec03sol.pdf).
That example is not imported as a termination theorem. The recorded
finite witness and direct substitution establish feasibility independently
of convergence or any solver status. No general theorem is reproved;
none of these sources contains this particular subsystem verdict.

**Original selected rows are affine on the entire plane.** For i=9a+b
put D_i=C(68-2a,8-a)C(956-2b,8-b)>0. Reconstruct E from

    E_(i,rq)=-beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q)/(D_i*V_rq),

where beta is the original finite binomial sum in L082. Use the original
source base B_i, cross c_i(t), inverse action x_i(t), forced term F_i(t)
and full anchor H_i, before positive normalization. The original bound is

    b_i(t)=F_i(t)-H_i-c_i(t)^T*x_i(t)/(p8*D_i),
    B_i*x_i(t)=c_i(t).

Every source range equation is checked coefficientwise, including empty
and singular blocks. Substitution of t78=s gives exactly L084's ten
coefficients in order 1,u1,u2,u3,u1^2,u1*u2,u1*u3,u2^2,u2*u3,u3^2.
For each of the 28 selected rows all six quadratic coefficients vanish.
The original selected cross vectors are constant on the plane, in
agreement with L085's existing constancy result; L085 is a consistency
comparison here, not an additional mathematical input. No affine claim
is made for the other modes' generalized Schur bounds.

**Complete equality locus and all inequalities.** In augmented original
coordinates w=(1,u,z) and reduced coordinates v=(1,u,h), h in R^18,
use L084's affine particular solution P and homogeneous matrix N.
Write L for w=L*v, G for the 28-by-49 equality matrix with rows
(-b_i's four affine coefficients,E_i), and R for the selector of
(1,u,z_nonpivot). The saved matrix K satisfies, in every entry,

    G*L=0, R*L=I_22, L*R-I_49=K*G.

The last identity proves the reverse implication: if G*w=0 then
w=L*(R*w). Thus the 21 reduced variables describe every point of the
original equality locus. All six quadratic columns of P also vanish.
No slice, variable bound or additional nonnegativity on h is introduced.
The matrices agree with the complete step-306 lift/reverse evidence.

Let H be the 130-by-49 matrix whose first 85 rows are the original
plane factors padded with 45 zeros, and whose last 45 rows select z.
The pulled-back rows are H*L; every row, including zero/duplicate rows,
is retained. For a row d0+d*x>=0, x=(u,h) in R^21, use x=x_plus-x_minus
with both parts nonnegative and the equality

    -d*x_plus+d*x_minus+slack=d0, slack>=0.

Multiply that entire equality by +1 if d0>=0 and -1 otherwise. Append
one positive artificial column per oriented row. The exact standard
matrix therefore has 130 rows and 302 columns, ordered 21 positive
parts, 21 negative parts, 130 slacks, 130 artificials. The initial basis
is the artificial identity and its right side is nonnegative.

**Explicit finite rational witness.** The canonical witness is the
full numerator/denominator array `witness/original` in
`scripts/finite-support/affine-sign-phase-one-results.json`.
Its raw array is `witness/raw_moments`; no rounded values are used.
These arrays can equivalently be specified by the following finite
deterministic recipe, which fixes them without an optimization oracle.
Start with the standard tableau above and minimize the artificial sum.
At each step enter the least indexed nonbasic column with strictly
negative reduced cost. Use the exact minimum nonnegative ratio; among
ties leave the least indexed basic variable. Perform exact rational
Gauss–Jordan pivoting on that strictly positive pivot. All column
numbers remain fixed. Stop when the artificial objective is zero.
This particular recipe reaches zero after exactly 230 pivots, within
the predeclared 10000-pivot/300-second limits. Initial and final complete
tableaux, bases, all pivots and row transformations are saved in
`scripts/finite-support/affine-sign-phase-one-initial-state.json` and
`scripts/finite-support/affine-sign-phase-one-state.json`, with the full
trace also in the results certificate. No second run or reconstruction
scheme is used. The artificial columns of each transformed tableau
are the complete row transformation of the original oriented rows.

Set every nonbasic standard coordinate to zero and each basic coordinate
to its final rational right side. Write this 302-vector as a. The
certificate checks directly, against the original standard matrix,

    a>=0, a_artificial=0, A_standard*a_without_artificials=b_standard.

Set x_j=a_j-a_(21+j), v=(1,x), and w=L*v. Independently of the tableau,
direct exact substitution checks all 85 original domain factors, all
45 scaled moments, all 45 raw moments and all 28 selected equalities.
The minima of both the domain factors and raw moments are exactly zero
against the required lower bound zero; the strict-positive and zero
indices are exactly those stated in the conclusion. All 28 original
equality residuals are zero, without tolerance.

For each selected i the unnormalized raw check is

    sum_(rq) beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q)*Y_(rq)
      +p8*D_i*b_i(u)=0.

Indeed this equals p8*D_i*(b_i(u)-E_i*z), since Y_(rq)=p8*z_(rq)/V_rq.
The independent verifier reconstructs these raw rows directly rather
than assuming saved reduced residuals. The full anchor is included in
b_i. It also reconstructs the selected affine bounds from original
source cross and inverse arrays before comparing any saved rows.

Reproduce from the active notebook:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/affine_sign_phase_one.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_affine_sign_phase_one.py

The constructor records 776 passing exact checks and no failures.
The independent verifier invokes neither the constructor nor an
optimizer and records 139 passing checks, no failures. Its full evidence
is `scripts/finite-support/affine-sign-phase-one-verification.json`.
These are original-coordinate arithmetic checks within this attempt;
a dedicated critical proof review remains separate. The verifier's
second invocation only added the zero-index lists to its report and
did not rerun Phase I or change the witness. Inherited source/base,
dictionary and kernel contracts retain their recorded qualifications.

**Separate critical proof review — step 310, 2026-10-18.** Reuse the
pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-18-affine-sign-witness-critical-audit.md` and
the precise rational-certificate and simplex citations above. This is
a conditional audit of the finite specialization, not a new theorem
about linear programming or a recursive approval of the ancestor PSD,
whole-kernel, uniqueness or source-normalization claims. Reproduce:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/critical_audit_affine_sign_phase_one.py

The audit retains the stated witness. It reuses the inspected L084 audit
implementation to reconstruct the original system in a separate file,
`scripts/finite-support/affine-sign-critical-ancestor-reconstruction.json`:
all 3673 checks pass. This reconstructs rho and the original pairs, p8,
the seven-column RREF and completion, the 85-factor affine family, all
90 original/weighted kernel equations, 500 full types and all 3000
presentations, 36 forced and 45 free moments, original beta coefficients,
all source range identities and the full anchor. The complete selected
right sides and particular solution have six zero quadratic coefficients
per row. Source decomposition and PSD remain qualified inputs, even
though these finite coordinate contracts have been reconstructed.

The original/raw verifier is rerun with its output redirected to
`scripts/finite-support/affine-sign-critical-original-verification.json`.
All 139 checks pass; every reconstructed row, bound, witness coordinate
and residual agrees with the saved verification, not just its verdict.
The audit then performs 1646 additional checks, with complete evidence
in `scripts/finite-support/affine-sign-phase-one-critical-audit.json`.
All these reports have no failures. No constructor or optimizer is run.

In particular, the audit reconstructs L,R,K from the complete original
equality data and verifies G L=0, R L=I and L R-I=K G entrywise.
For an independent raw-coordinate check put

    S=diag(1,1,1,1,p8/V_1,...,p8/V_45),
    D=diag(p8*D_i) on the 28 selected modes,
    G_raw=-D*G*S^(-1), L_raw=S*L,
    R_raw=R*S^(-1), K_raw=-S*K*D^(-1).

Every diagonal entry of S and D is positive. The raw equalities are
reconstructed from the unnormalized beta rows, and the audit verifies

    G_raw*L_raw=0, R_raw*L_raw=I,
    L_raw*R_raw-I=K_raw*G_raw.

Thus both directions of the complete equality lift hold also in raw
coordinates; no sign-changing or singular variable scaling is hidden.

All 130 pulled-back rows are retained in the original standard-form
conversion. The entire initial tableau equals the reconstructed
130-by-172 standard matrix augmented by I_130, with nonnegative right
side and the artificial basis. The audit replays exactly the saved
230 pivots. At each step it checks the saved positive pivot, the least
indexed nonbasic negative reduced cost, the minimum nonnegative ratio
and least indexed leaving basic variable, every resulting basic sign,
the complete basis identity, and the objective change identity

    objective_after = objective_before + ratio*entering_reduced_cost.

It consumes the fixed trace and makes no new feasibility search.
The complete final tableau, right side, basis and artificial-column
row transform agree with the saved state. Each replayed operation is
invertible, so these artificial columns are the entire transformation
of the original oriented rows. The recorded elapsed-time and pivot
limits agree with the declared bounds; the audit checks this recorded
provenance, not an independent historical wall-clock measurement.

The final 302-vector has nonnegative entries and all 130 artificial
entries zero. It satisfies every original standard equation. Its
positive-minus-negative coordinates map through L to exactly the saved
49-coordinate witness and through S to exactly the raw witness. Direct
original/raw substitution, independently of this provenance, retains
all 85 domain rows, 45 signs and 56 selected equality residuals. The
domain and raw-moment minima are exactly zero, matching the required
bound zero; all equality residuals are zero. The positive counts and
complete zero-index lists in the conclusion agree. These exact tests
establish only the prescribed subsystem result. The other 53 modes
were not evaluated at this witness during the audit.

The strict Farkas alternative cannot reject this nonempty subsystem.
This does not supply a completion of the remaining modes: those
inequalities were deliberately omitted, so no claim about them follows.
Preserve ATTEMPTS/052–053,060–068 and their different scopes. The result
parks only sign/equality exclusion over this entire original plane.

## Mathlib

Full matching finite rational subsystem/witness result: not checked.
Supporting Farkas, rational simplex and elimination coverage: not
checked. Unknown availability is not evidence of absence. General
methods are imported by the precise citations above; the exact finite
specialization supplies no claim of progress beyond those sources.
