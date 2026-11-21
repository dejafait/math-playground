# Highest original spatial moment: bounded attempt, step 75

Invocation-start assessment: `drafts/literature/2026-11-02-displaced-highest-spatial-moment.md`, EXPLORE. The supplied assessment is reused unchanged. The sole target is the uniform bound max_(|u|=1)|c_(M-1)(u)| >= C*n*exp(-n/32)*sqrt(D) for the full L666 family, or an admissible countersequence. Original residues, all factors, the radial multiplier, and the same displacement vector for all angles are retained.

Main gap: actual-Xi all-degree mixed positivity. A positive result would supply the leading spatial coefficient needed for the known endpoint Mahler bound and then L658's sufficient H threshold. Support and actual-Xi realization/signs remain independent.

Initial proof inputs read: L666's definitions, rational continuation and admissibility; L658's statement and endpoint source qualifications. Method comparisons: L669's fixed-angle countersequence, L670/L671 clearing-certificate stops, and the two-attempt L666 scalar-energy stop. These do not decide the present highest-moment angular maximum. Existing uncommitted work is preserved.

Plan saved before extended work: inspect the exact full angular rational response with k=M-1. First determine whether its radial cost already makes an admissible simple sequence a candidate negative; if needed analyze angular compensation without replacing it by a fixed angle or by c_0. Any finite numerical screen is diagnostic only. A passing conclusion requires a uniform bound with constants/onset, a useful rigorous intermediate estimate with the precise remaining loss, or a rigorous countersequence whose ratio to the required scale tends to zero. No source theorem or lower-degree coercivity is assumed beyond the saved assessment.

Unresolved at save time: signed angular cancellation, the (a/R)^(M-1) magnitude and phase, comparison to original D, and n-uniform error control. No new bound is yet claimed.

## Contour candidate saved before certification

The zero-displacement screen suggests a negative already for e_m=0; its sampled maxima and D values are not proof. Set alpha=27/10, h=alpha/n, b=9/100, r=9/20, A_n=2qh=r-27/(20n), and k=n/3-1. On the rectangle a=x+s+iy, |s|<=b, |y|<=A_n, define F_n(a,u)=W_a(u)*(a/R)^k and K_n(a)=1/(1+exp(2pi(a-x)/h)). F_n is holomorphic there because |a|>=29/25>1. K_n has exactly the nonanchor lattice poles, each of residue -h/(2pi). Thus sum_m F_n(a_m,u)=(i/h) integral_boundary F_n K_n da.

Proposed decisive bound: for g(a,u)=integral_0^1 log|[(x-tu)/(a-tu)]*[(Uu-ta)/(Uu-tx)]|dt+(1/3)log(|a|/R), certify g-(20/9)max(s,0)<=-7/200 on the two vertical sides |s|=b, |y|<=r and horizontal sides |y|=r, |s|<=b. The 20/9 damping uses only pi>3. A rational power-series mesh with explicit interpolation error will test this complete compact boundary, not just its samples.

If that certificate passes, the finite-product Riemann error is <17, the missing one radial power costs <1, and moving horizontal height from r to A_n costs at most 27/2 using |partial_y g|<10. Hence |F_n K_n|<=2 exp(32-7n/200), uniformly on the actual contour and all angles. Its perimeter/h<=4n/5. The nonanchor sum would then be <=(8/5)n exp(32-7n/200); the separate anchor is (x/R)^k. Since D>=64/21 and (1/3)log(11/10)>19/600>1/32, these bounds would give an explicit normalized ratio tending to zero. The compact certificate and all these analytic inequalities still require verification before claiming this negative.

## Completion — 3 November 2026

The rational compact certificate passed at -2385744893/62500000000 < -7/200, including 12,558 samples, complete mesh coverage and 17 arithmetic checks. The full proof, finite-n charges, ratio limit, source qualifications and Mathlib status are now canonical in `lemmas/L682-highest-spatial-moment-countersequence.md`; the provisional derivation above is retained as working history. The negative uses the original e_m=0 sequence and retires only this sufficient highest-coefficient certificate. A separate conceptual audit is nominated with REVIEW_REQUIRED. No additional mechanism was attempted.
