# Whole-line exponential-tilt variance test — 2026-09-23

## Target and discriminating test

The main gap is actual-theta all-degree mixed reciprocal-node positivity. The intermediate target is r Var_r(U)≤m(r), for the density proportional to K(u)e^{ru} on the whole real line and m(r)=E_r[U]. This is exactly G′(r²)≤0 in L242. A positive Stieltjes representation would imply this sign and supply the mixed forms; this first sign alone supplies neither the representation nor higher-order positivity.

The concrete mechanism is the inverse-curvature estimate Var_r(U)≤E_r[1/W″(U)], where W=−log K. Exponential tilting leaves W″ unchanged. Continue this comparison only if E_r[1/W″]≤m(r)/r can hold throughout r>0; abandon it if the actual theta density gives a strict reversed comparison on an interval. This tests the integrated comparison, rather than repeating L243's pointwise cosh obstruction.

Redundancy screen: L048 provides the unchanged positive curvature; L049 already rules out strict log-concavity alone as a generic first-sign theorem, and L055–L057 block stronger generic conditions as all-degree criteria. L242 identifies the first-sign gap, and L243 concerns a different tilted potential and a different observable. None proves the actual whole-line integrated inverse-curvature comparison fails. Prior uncommitted results and all inactive branches are retained.

## Saved reasoning and result

At r=0 the required comparison is E_0[1/W″]≤Var_0(U). The reverse variance inequality is strict unless the potential is quadratic. The theta curvature grows at infinity, so equality is impossible. The elementary integration-by-parts proof and continuity argument are now stored in [L244](../lemmas/L244-exponential-tilt-inverse-curvature-gap.md).

**WHY IT FAILS.** The inverse-curvature upper bound has a fixed strictly positive slack at zero tilt, whereas the desired mean/parameter threshold tends to the exact untilted variance. Consequently the upper bound exceeds the required threshold throughout a nonempty interval of positive tilts. Preserving curvature repairs the hypothesis of the variance estimate but not its strength. This does not show r Var_r(U)>m(r), and is not a negative actual mixed form or a disproof of RH.

Decision: NEGATIVE; stop the inverse-curvature comparison mechanism in both tested representations. Two consecutive curvature tests have failed, so another rearrangement of the same estimate is not a justified continuation. A materially different diagnostic can use the completed-zeta formula on the real axis and absolutely convergent Dirichlet estimates to test the first sign for all sufficiently large r. This would still leave a compact parameter interval and every stronger Stieltjes/mixed-positivity condition unresolved. One bounded test resolved; zero consecutive unresolved exploration turns. No candidate.
