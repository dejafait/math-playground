# Lemma 61: bounded-domain forward continuation

**Hypotheses.** Let F(λ,z) be the exact heat-deformed theta transform of Lemma 58. Let a<b be finite real numbers and D⊂C a bounded open set. Assume

F(λ,z)≠0 for every λ∈[a,b] and z∈∂D,

and that every zero of F(a,·) in D is real. Multiplicities at a are allowed; the zero set may be empty. No regularity of ∂D or conjugation symmetry of D is assumed.

**Conclusion.** For every λ∈[a,b], all zeros of F(λ,·) in D are real. Their total number counted with multiplicity is finite and independent of λ. For every λ∈(a,b], every such zero is simple. These conclusions concern only D and require the stated boundary hypothesis throughout the interval.

## Proof

### Finite local accounting without boundary regularity

By Lemma 58, F is jointly entire and F(λ,0)>0 for real λ. Thus each slice F(λ,·) is not identically zero. Its zeros are isolated and have finite multiplicity. Since the closure of D is compact and contains no boundary zeros, it contains only finitely many zeros at any fixed parameter τ∈[a,b]. Otherwise compactness would give a finite accumulation point of zeros of a nonzero entire function.

If D is empty the theorem is immediate. Otherwise, at τ choose pairwise disjoint closed discs about all these zeros, lying in D, with no other zeros in each disc and no zeros on its circle. Write their open interiors as B_1,…,B_k and their multiplicities as m_1,…,m_k. The set

E=closure(D) \ (B_1∪⋯∪B_k)

is compact and zero-free for F(τ,·). Uniform continuity on a compact parameter neighborhood times closure(D) implies that F(λ,·) remains nonzero on E for λ sufficiently close to τ: its change in modulus is smaller than the positive minimum of |F(τ,·)| on E. In particular this estimate holds on each disc boundary. Rouché's theorem on each circle then gives exactly m_j zeros in B_j counted with multiplicity for all such λ. Every zero in D lies in those discs, since the remainder lies in E. If k=0 the same minimum argument applies on the entire closure of D and there remain no zeros.

Consequently the finite total zero count N(λ) in D is locally constant on [a,b] in its relative topology. A locally constant function on an interval is constant, proving the counting assertion. This uses circles only; no contour integral on ∂D is required.

### Closedness and right persistence of reality

Let S be the set of parameters in [a,b] at which all zeros in D are real. This set is closed. Indeed, if τ is not in S, take a nonreal zero and a small closed disc around it contained in D, disjoint from the real axis, with zero-free circle. Uniform convergence and Rouché preserve at least one zero in that disc for every sufficiently nearby parameter. Such parameters are also outside S. This proves that its complement is relatively open, including at the interval endpoints.

For τ∈S with τ<b, there is δ>0 such that [τ,τ+δ]∩[a,b]⊂S. Use the finitely many discs and the zero-free remainder at τ as above, now centered at real zeros. For a simple zero, Lemma 58 gives a real simple local branch; shrink the parameter interval so the branch lies in its disc, and the count one proves it is the only zero there. For a double zero, Lemma 59 gives all nearby zeros real for sufficiently small positive λ-τ. For multiplicity m≥3 the same assertion is supplied by Lemma 60. The discs can be chosen within the respective local neighborhoods, with the parameters subsequently shrunk so all those branches stay inside them. Taking the minimum of the finitely many parameter radii, and also the radius controlling E, proves right persistence. If there are no zeros, the zero-free remainder argument alone proves it. At τ itself reality is part of τ∈S.

To obtain the full interval, put

c=sup{t∈[a,b] : [a,t]⊂S}.

The set is nonempty since a∈S. Every r<c lies in S by the definition of supremum, and c∈S by closedness (also when c=a). Hence [a,c]⊂S. If c<b, right persistence at c extends this initial interval, contradicting its supremum. Thus c=b and S=[a,b]. This step uses right persistence, not an unjustified claim of two-sided openness.

### Simplicity after the initial parameter

Suppose τ∈(a,b] has a multiple zero x in D. We have just proved x is real. Its multiplicity is finite. Lemma 59 for multiplicity two, or Lemma 60 for greater multiplicity, produces nonreal zeros arbitrarily close to x at parameters just below τ. Choose their local disc inside D and a parameter strictly between a and τ, close enough that those nonreal zeros are in that disc. This contradicts the reality already proved throughout [a,b]. Thus every zero in D is simple at every parameter strictly greater than a, including b. ∎

## Why the direction cannot be reversed

The initial real configuration is an assumption, not a conclusion about the theta transform at any specific parameter. Moreover the local splitting results are directed: a real multiple zero resolves into real zeros as λ increases, but produces nonreal pairs as λ decreases. Thus the right-persistence step above has no corresponding left-persistence statement at multiple zeros.

The polynomial example in Lemma 58 makes this directional obstruction exact even in a boundary-free bounded domain. Take P(λ,z)=z²+2(1-λ), λ∈[0,2], and D={|z|<2}. It satisfies P_λ=-P_zz; all its roots have modulus at most sqrt(2)<2 throughout this interval, so its boundary is zero-free. Its zeros at λ=2 are real, but at λ=0 they are nonreal. At λ=1 they collide. This polynomial tests only an inference from the heat equation and local zero laws; it is not the exact theta family and supplies no counterexample to RH.

For the exact family, no boundary-free exhaustion of the plane over a parameter interval has been established here. Boundedness prevents loss of zeros to infinity within this theorem; it provides no uniform control as D grows. Even an independently known real configuration at a positive parameter would therefore not give downward continuation to λ=0 by this result. Positive-parameter collision exclusion remains unproved.

## Verification and formalization obligations

This proof is analytic and requires no numerical certificate. The compact remainder controls all zeros, including the case of no zeros, and replaces any unjustified use of an argument principle on an irregular boundary. The direct mathematical inputs are the analytic and simple-zero assertions of Lemma 58 and the splitting assertions of Lemmas 59 and 60. Standard named inputs are the isolated-zero theorem, Rouché's theorem, compactness and uniform continuity, and the connectedness/completeness of real intervals.

Formalization would require finite isolation of zeros in a compact set, uniform parameter perturbation on its zero-free remainder, local constancy of the multiplicity count, closedness and right persistence of the real-zero configurations, the initial-interval supremum argument, and the use of negative-side splitting to exclude multiple zeros after a. No assertion about all zeros in the plane or reality at λ=0 is proved.
