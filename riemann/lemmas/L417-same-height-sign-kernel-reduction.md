# Lemma 417: a same-height sign-kernel reduction, with feasibility unresolved

## Hypotheses

Fix a sufficiently large real H, write ell=log H, and give [H,2H]
the probability measure dt/H. Use L414's exact definitions of P,V,
ell_F,Ccal,Bcal,Delta,omega,U, with the actual envelope and curvature.
Keep the actual response at each t, including a,h and

    v_j(t)=(G/A)^(j)(t)/(T(t)^2 L(t)^j), j=0,1,2.

The derivatives precede division. Write X0(t) for the actual critical
triple (f,f'/L,f''/L^2), and abbreviate its exact physical quantities by
B(t)=Bcal(t), D(t)=Delta(t). Here D is normalized Delta, not L370's
unnormalized physical discriminant. These functions are continuous and
bounded on the fixed compact interval. Set P={D>0}, N={D<=0}.
Expectations below use dt/H; sets of zero measure are immaterial.

The selected constraint list is exactly L416's list, including the
inherited L414/L415 constraints, not extra conditional moment constraints.
Its actual even moments and bounds are the already sourced inputs recorded
there. The actual first B mean is L369 (2), and the actual cubic mean is
L409 (2), with the constants b0=zeta(3)/(4pi), beta_*=beta>0.

Restrict this attempt to measurable probability kernels supported on
{X0(t),-X0(t)} at each t. This is an additional ansatz, not a restriction
on all laws allowed by the approved problem. No single global critical
function is required for the conditional output states.

## Conclusion

Every such sign kernel preserves pointwise all six raw second moments,
the first Delta moment, all 23 quartic observables, U^2, U^(3/2), and
|Bcal|^3. It also preserves all pointwise envelopes, exact curvature,
the actual response graph, and the uniform height marginal.

Among kernels avoiding {Delta>0,Bcal<0}, the attainable pairs of the
first Bcal and cubic moments are exactly the pairs

    ( E_P |B| + E_N m|B|,
      E_P D|B| + E_N D m|B| ),                     (1)

where m:N->[−1,1] is any measurable function. Values at B=0 have no
effect. Thus the whole remaining test for this ansatz is to find m_H
for all sufficiently large real H such that (1) equals

    ( -b0+O(e_H), beta_* ell^2+o(ell^2) ),
    e_H=ell^(-1)+H^(-1/2)ell^2,                    (2)

with a fixed first-error constant. No such choice is established here.

For every fixed H and every real u,v, the exact maximum of the
linear functional u E Bcal+v E(Delta Bcal)/ell^2 in this ansatz is

    h_H(u,v)=E_P[|B|(u+v D/ell^2)]
                +E_N[|B| |u+v D/ell^2|].           (3)

The minimum is obtained by replacing the plus before E_N by minus.
These are attained scalar extrema, not a claim that independently chosen
scalar extrema or scalar interval memberships give a simultaneous pair.
No general moment strong-duality or purification theorem is asserted.

This leaves feasibility of the approved target unresolved. In particular,
failure even of this entire sign ansatz would not exclude kernels with
other critical triples at the same actual response. The calculation is
an exploratory reduction, not a feasible-law theorem, a separating gap,
an actual clipped-mean evaluation, or progress beyond the checked known
tools. It has not received a separate critical audit.

## Proof

### Exact conditional construction and preservation

The step-150 SPECIALIZE assessment already covers the prescribed graph,
conditional kernels and finite moment list. This is an elementary
specialization of that framework. It needs no new theorem about zeta,
actual conditional independence, source retrieval, or purification.

At a fixed t, L414's conversion is linear in X. Replacing X0 by -X0
therefore replaces P by -P and omega by -omega, while V is unchanged.
The exact definitions give

    ell_F(-X0)=ell_F(X0), Bcal(-X0)=-B,
    Delta(-X0)=D, U(-X0)=U(X0).

These are identities before any asymptotic replacement. In particular the
q=(log A)'' terms and every actual response derivative are retained.
Every X_i X_j is invariant, including xy and yz. So are Delta^2,
Delta Bcal^2 and the six diagonal and fifteen off-diagonal products
Delta omega_i omega_j. The first Delta and all three listed absolute
observables are invariant too. Their conditional expectations equal the
actual integrands at each height, not just their leading terms.

Consequently all six actual second-moment errors in L416 (1) survive
unchanged: the four O(1) errors and both power-saving odd-index errors.
The same is true of every sourced even-moment tolerance. The output
absolute P_j values equal their actual values; all response coordinates
and their bounds are unchanged. Thus the fixed constants and eventual
onset of the actual inputs work for this ansatz as well. There is no
height relocation or response-amplitude calibration.

If X0=0 both actions coincide and B=D=0. At other heights, for any
measurable p(t) in [0,1], use the kernel

    nu_t=p(t) delta_(X0(t))+(1-p(t)) delta_(-X0(t)).

It is a measurable probability kernel; each fiber has mass one, so the
height marginal is exactly uniform. Conditional output B is (2p−1)B,
whereas output Delta is always D. On P, avoidance forces output B>=0.
If B!=0 this forces the action having Bcal=|B| with probability one;
if B=0 either action is allowed and contributes zero. On N both actions
are allowed. For any measurable m:N->[−1,1], choose on B!=0

    p(t)=(1+m(t) sign(B(t)))/2.

Choose p=1/2 when B=0. Its conditional B mean is m|B|, and its
conditional Delta B mean is D m|B|. Conversely every sign kernel has
this form at B!=0. This proves the exact pair description (1), including
the boundary D=0. All observables are absolutely integrable at fixed H,
since actual continuous data on this compact interval are bounded.

L369 and L409 show that preserving the actual two odd means exactly
would be sufficient for (2), but exact preservation is not required.
Equation (2) uses precisely their allowed asymptotic errors, without
silently imposing finer coefficients or critical first moments.

### Sharp scalar tests and what they do not decide

For any m with |m|<=1, the pointwise inequality

    m |B|(u+v D/ell^2)<=|B| |u+v D/ell^2|

gives (3)'s upper bound by integration on N. Equality holds for the
measurable choice m=sign(u+v D/ell^2), with any value at zero. Choosing
the negative sign gives the minimum. This proves sharpness for each
one-dimensional objective directly, without assuming a theorem about
closure of an infinite-dimensional moment set.

The integration argument is the weak-duality mechanism covered by
D. Bertsimas and I. Popescu, *Optimal Inequalities in Probability Theory:
A Convex Optimization Approach*, SIAM J. Optim. 15 (2005), 780--804,
DOI [10.1137/S1052623401399903](https://doi.org/10.1137/S1052623401399903),
Section 2, Theorem 2.1, pp. 784--785, inspected in the step-138 assessment.
Its general theorem is imported, not reproved; the displayed elementary
inequality and its equality case identify the particular test here.
Theorem 2.2's strong-duality hypotheses are not invoked. Aumann's
selection and Jaskiewicz--Nowak's purification inputs from step 150 are
unneeded because this kernel and its scalar maximizers are explicit.

For example put

    P0=E_P |B|, N0=E_N |B|,
    P1=E_P D|B|, N1=E_N |D| |B|.

All four are nonnegative and finite. The separate necessary intervals
for (1) are

    P0-N0 <= E Bcal <= P0+N0,
    P1-N1 <= E(Delta Bcal) <= P1+N1.                 (4)

Each interval is individually attainable; their Cartesian product is
not asserted attainable. In particular the negative first mean requires
P0-N0<=-b0+O(e_H). Neither L369's uncut first mean nor L409's uncut
cubic mean computes P0-N0. The positive quartic coefficient of
E(Delta Bcal^2) also is not an evaluation of this clipped absolute
integral. No such implication is used here.

There is a precise error-robust rejection test for the sign ansatz:
if along an unbounded sequence H there are real u_H,v_H with
|u_H|+|v_H|<=1 and a fixed delta>0 satisfying

    -u_H b0+v_H beta_*-h_H(u_H,v_H)>=delta,          (5)

then no family can satisfy (2) for every sufficiently large real H.
Indeed its left functional would be -u_H b0+v_H beta_*+O(e_H)+o(1),
while (3) bounds it above by h_H. Since e_H tends to zero and the first-error
constant is fixed, (5) contradicts the bound on that sequence. This
only gives a conditional rejection test: no u_H,v_H and no positive
gap in (5) have been established for the actual functions. Conversely,
not finding (5) is not an existence proof. Even a proved gap would
reject only the two-action ansatz, not all prescribed-response laws.

### Why a pointwise radial repair is unavailable under exact preservation

A tempting extension is X=S X0, with a random real scalar S conditional
on t, retaining pointwise the critical second matrix and U^2. Where
X0!=0, the trace of that matrix forces E(S^2|t)=1, while U0^2>0 and
fourth-degree homogeneity force E(S^4|t)=1. Hence

    E((S^2-1)^2|t)=1-2+1=0,

so S^2=1 almost surely. Where X0=0 the radial output is zero anyway.
Thus such a radial extension reduces to the same sign kernel. This is
the elementary equality case of the second/fourth-moment inequality;
the calculation is included to discharge the conditional specialization,
not as a new general theorem. The approved problem requires only
integrated moments and asymptotic errors. It does not impose these
stronger pointwise preservation requirements, so this calculation does
not obstruct more general rescaling or changes of critical direction.

The attempt ends here: the known even information transfers exactly,
but no supported choice meeting both odd constraints, and no robust
gap, has been proved. All actual clipping, regulator-margin, global
realization, common-zero and mixed-positivity gaps remain independent.

## Mathlib

Full matching coverage for this prescribed-response conditional problem
has not been checked. The general sign-mixture and nonnegative-integral
arguments are elementary, but that observation is not a claim of a full
Mathlib theorem or formal verification. No numerical evidence, fitted
moments or mathematical script is used.
