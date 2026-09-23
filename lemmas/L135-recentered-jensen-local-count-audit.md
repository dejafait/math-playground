# Lemma 135: recentered Jensen local-count audit

**Hypotheses.** Let F(λ,z) be the theta heat deformation of L058, and fix L≥0 and H>0. Assume, as an additional hypothesis, that all zeros of every real slice |λ|≤L lie in |Im z|≤H. Counts include full multiplicities. For real x define

c_x=x+1/2+i(H+1),
r=1+sqrt(1/4+(2H+1)²),
M_λ(x)=max_{|z−c_x|≤2r}|F(λ,z)|,
D_λ(x)=log(M_λ(x)/|F(λ,c_x)|).

**Conclusion.** The denominator is nonzero and D_λ(x)≥0. The full unit-window count satisfies

#{ρ: Re ρ∈[x,x+1)} ≤ D_λ(x)/log 2.                 (1)

In particular, the additional, unproved estimate

D_λ(x)≤B log(2+|x|) for all real x and |λ|≤L         (2)

with a common B>0 implies the logarithmic local count used in L133, with C=B/log 2.

There is an established upper bound M_λ(x)≤U, independent of x and λ. Explicitly, with C the kernel constant in L058, set

Y=H+1+2r,
U=(C/2)exp(2L²/π) exp((Y/2+4)log(Y/2+4)).

Thus the stronger extra lower bound

|F(λ,c_x)|≥U(2+|x|)^(−B)                            (3)

would imply (2). Neither (2) nor (3) is established here for theta slices. Under the strip hypothesis, D is uniformly bounded when x ranges over any fixed compact interval; the unresolved issue is its rate at infinity.

**Proof.**

The strip hypothesis puts c_x strictly above every zero, so F(λ,c_x)≠0. The maximum defining M includes c_x, giving D≥0. Every zero in the stated window has horizontal distance at most 1/2 from c_x and vertical distance at most 2H+1. It therefore lies in |z−c_x|<r.

For fixed λ,x apply the standard named Jensen formula to F(λ,c_x+w) on any radius s>2r whose boundary has no zeros. Each zero at distance at most r contributes at least log(s/r), with its full multiplicity. Bounding the boundary average of log|F| by the logarithm of the disk maximum yields

N_λ(x)log(s/r)≤log max_{|z−c_x|≤s}|F(λ,z)|−log|F(λ,c_x)|.

Choose zero-free boundary radii decreasing to 2r, possible by local finiteness for a nonzero entire function. Disk maxima converge to M_λ(x) by continuity on a slightly larger compact disk. This proves (1), including all window endpoints allowed by its half-open convention. Substitution of (2) proves the stated local count.

For the upper bound, the integral and positive kernel of L058 give, for real |λ|≤L and |Im z|≤Y,

|F(λ,z)|≤∫₀^∞exp(Lu²)K(u)exp(Yu)du.

The completed-square and factorial integral estimate in the proof of L063 bounds this last expression by U: that calculation uses only the exponential factor exp(Yu), so its radial variable can be replaced by Y≥1 here. On the translated disk |Im z|≤H+1+2r=Y, proving M≤U. Taking logarithms proves that (3) implies (2).

Finally fix X<∞. Joint continuity from L058 and nonvanishing at c_x on the compact set {|λ|≤L, |x|≤X} imply a positive minimum m_X for |F(λ,c_x)|. Hence 0≤D≤log(U/m_X) there. Compactness gives no rate for m_X as X grows. This completes all asserted unconditional implications under the stated strip hypothesis. ∎

## Audit of the missing estimate

The relative maximum-to-center estimate (2) is the precise sufficient quantitative input for this fixed-radius Jensen argument. It is not asserted to be necessary for a logarithmic count: Jensen also sees zeros outside the unit window, and its maximum bound can overestimate the boundary average. Condition (3) is stronger still, because the coarse U ignores horizontal decay of the function. Failure to prove (3) would not disprove (2).

L130's positive normalization at zero cannot be used at c_x. The integrand contains cos((x+1/2+i(H+1))u); its real part oscillates, so the positive first-summand argument at zero is unavailable. Even though the strip hypothesis makes the center zero-free, it gives no quantitative modulus estimate by itself in this proof. The origin-centered global count also cannot be subtracted to give a bound on a translated unit window: subtracting two upper bounds does not bound the difference of the counts.

Accordingly the established growth and normalization estimates yield this conditional reduction, not a uniform logarithmic local count. A common strip is itself an additional assumption in this statement. No claim is made that the full theta structure cannot prove (2) by further analysis. No zero-reality or RH conclusion follows.

## Verification

Analytic verification checked translated rectangle containment, nonvanishing centers, Jensen multiplicities and boundary-radius limits, the imaginary-part version of the existing integral majorant, and compact-parameter minima. No numerical certificate is needed. Conditions (2) and (3) must remain hypotheses, not established theta inputs.

**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
