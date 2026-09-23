# Lemma 167: centered-primitive cutoff covariance

**Hypotheses.** Use W, Q and E_T from L166, with window [N,2N],
N=sqrt(T/(2π)). Let χ∈C³(R) be zero below 1 and one above 2.
Fix M>0. Put L=log T, bar W=E_T W, and
P(t)=∫_T^t(W(s)−bar W)ds. Constants are independent of large T.

**Conclusion.** P(T)=P(2T)=0 and exactly

E_T[χ''(Q/M)(W−bar W)]=−E_T[P χ'''(Q/M)Q']/M.          (1)

Moreover c T L⁴≤||P||∞≤C T L⁴. Available derivative bounds give

|E_T[χ''(Q/M)(W−bar W)]|
 ≤ ||χ'''||∞ ||P||∞ E_T[|Q'|1_(M<Q<2M)]/M
 ≤ C_χ T L⁴/M.                                         (2)

The direct bound is O_χ(L⁴). Neither bound establishes o(1) for fixed
M and χ. No lower bound on the actual covariance is asserted.

**Proof.**

All defining sums are finite and smooth. Centering gives both zero
endpoint values. Since (χ''(Q/M))'=χ'''(Q/M)Q'/M, ordinary
integration by parts, divided by T, proves (1), with no boundary term.
Continuity and the constant extensions of χ make χ''' vanish outside
(1,2), including its endpoints, giving the support in (2).

For the primitive scale put g(u)=W(Tu)−bar W and
p(u)=∫_1^u g(v)dv, for 1≤u≤2. Then P(Tu)=T p(u),
p(1)=p(2)=0. L166 gives ∫|g|≥c L⁴ and sup|g|≤C L⁴.
Its Gaussian profile gives W(t)≤C L⁴ and |W'(t)|≤C W(t)/t,
so sup|g'|≤C L⁴. The upper bound ||p||∞≤∫|g|≤C L⁴ follows.
For the lower bound, Cauchy–Schwarz on an interval of length one and
integration by parts yield

c² L⁸≤(∫|g|)²≤∫g²=[p g]_1^2−∫p g'
 ≤||p||∞∫|g'|≤C L⁴||p||∞.

This proves the stated two-sided scale for P, for the actual W.

L156's carrier-removed sum H has Q=|H|², E_T|H|²≤C and
E_T|H'|²≤C. Thus Q'=2 Re(H' conjugate(H)) and
E_T|Q'|≤2(E_T|H|² E_T|H'|²)^(1/2)≤C.
Use this and the upper bound on P in (1) to obtain (2).
Retaining transition support also gives
E_T[|Q'|1_(M<Q<2M)]≤2 sqrt(2M)(E_T|H'|²)^(1/2)
≤C sqrt(M), still without T decay for fixed M.
The direct estimate follows from ||χ''||∞ and L166's L1 deviation.
For fixed M, the desired o(1) error is exactly equivalent to

E_T[(P/(T L⁴))χ'''(Q/M)Q']=o(1/(T L⁴)),                (3)

by substitution into (1). This signed estimate remains unproved. ∎

## Scope, verification

The primitive lower bound does not force overlap with the transition set
or exclude signed cancellation. A growing upper bound is not a growing
error lower bound. This step supplies neither a tail theorem nor RH.

Verification is analytic: endpoint centering, the chain-rule sign, C³
regularity, the change t=Tu, the energy identity, Gaussian derivative
control, and normalized Cauchy–Schwarz are checked above. All sums are
finite; no limiting interchange or numerical verification is required.

**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
