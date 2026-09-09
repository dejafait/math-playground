# Attempt: continue Euler-product positivity into the critical strip

Date: 2026-09-09

Outcome: failed; Lemmas 5–11 in PROOF.md retain the valid boundary proof and the exact obstructions.

For σ>1 the absolutely convergent Euler logarithm and 3+4cos θ+cos 2θ≥0 prove ζ(σ)³|ζ(σ+it)|⁴|ζ(σ+2it)|≥1. At the boundary, local orders rule out a zero at 1+it for t≠0. The attempted extension was to continue the same inequality into 0<σ<1 and use it to rule out further zeros.

Lemma 10 shows that the real prime-logarithm sum diverges for 0<σ≤1 and the complex series is not absolutely convergent there. More decisively, with every factor replaced by its modulus, the product is continuous near (σ,t)=(0,0) and equals 1/256 at that point. It is therefore <1 in an open neighborhood, including σ>0 and t≠0. With the original signed first factor it is nonpositive near there.

**WHY IT FAILS.** Analytic continuation preserves identities between analytic functions, not real inequalities derived from a positive series outside its convergence domain. The required nonnegative prime representation diverges, and the proposed inequality is itself false at interior points by continuity from ζ(0)=-1/2. Thus neither a branch choice nor merely putting an absolute value on the first factor repairs the inference. This failure does not challenge the boundary proof, which uses the inequality only for σ>1.

Next lemma: construct the alternating Dirichlet series on Re(s)>0 with uniform tail bounds and identify its precise relation to ζ.
