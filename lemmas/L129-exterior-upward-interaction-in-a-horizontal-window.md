# Lemma 129: exterior upward interaction in a horizontal window

**Hypotheses.** Fix a real theta heat slice f(z)=F(λ₀,z) as in L063. Assume all its zeros satisfy |Im ρ|≤H for some finite H>0. All sums below are over the full zero multiset, counting multiplicities, not pair representatives. Let 0≤A<R and define

T(R)=Σ_{|Re ρ|>R}|ρ|^(-2),    C(A,R,H)=(R²+H²)/(R−A)².

For any point w=a+ib with |a|≤A and 0<b≤H, define

E_R(w)=2Σ_{|Re ρ|>R, Im ρ>b}(Im ρ−b)/|w−ρ|².

**Conclusion.** The tail T(R) is finite and tends to zero as R→∞, and uniformly over the indicated points,

E_R(w)≤2(H−b) C(A,R,H) T(R).                         (1)

The absolute exterior imaginary interaction also satisfies

Σ_{|Re ρ|>R}|Im(2/(w−ρ))|≤4H C(A,R,H) T(R).          (2)

In particular C≤8 if R≥2A and R≥H. For fixed A and H, C→1 as R→∞. With a fixed additive buffer d>0, C(A,A+d,H)=((A+d)²+H²)/d²; this estimate alone need not vanish as A→∞ after multiplication by T(A+d).

If w is a zero of exact multiplicity m≥1 and no zero with |Re ρ|≤R has height greater than b, set h(z)=f(z)/(z−w)^m with its removable value at w. Its local forward height rate c(w)=2 Im(h'(w)/h(w)) obeys

c(w)≤−m/b−mb/(a²+b²)+2(H−b) C(A,R,H) T(R).           (3)

For m=1 this is the ordinary branch height derivative; for m≥2 it is the right derivative of the maximum height of the local split cluster, as in L127. No assertion that a window maximum lies inside a smaller buffered window is made.

## Proof

L063 gives no zero at zero and reciprocal-square summability over pair representatives. The full sum is twice that sum. Its subseries T(R) is finite; given any positive tolerance, a finite set captures all but that tolerance of the full sum. Once R exceeds the real parts in this finite set, T(R) is below the tolerance. Thus T(R)→0 without requiring any indexing of moving zeros.

For an exterior zero ρ=u+iv put x=|u|>R. Since |a|≤A and |v|≤H,

|w−ρ|²≥(x−A)²,    |ρ|²≤x²+H².

Both x/(x−A)=1+A/(x−A) and H/(x−A) are nonincreasing for x>A. Squaring and adding gives

|w−ρ|^(-2)≤[(x²+H²)/(x−A)²]|ρ|^(-2)
             ≤C(A,R,H)|ρ|^(-2).                      (4)

The denominators are positive because R>A. Each upward numerator is at most 2(H−b). Summing (4) proves (1). Also

|Im(2/(w−ρ))|=2|v−b|/|w−ρ|²≤4H/|w−ρ|²,

which proves (2) and absolute convergence of that exterior sum. The constants and limits stated above follow directly from the formula for C; for C≤8 use R−A≥R/2 and R²+H²≤2R².

For (3), positivity on the imaginary axis in the theta integral, as used in L127, ensures a≠0. The four distinct points w, −w, conjugate(w), −conjugate(w) have multiplicity m and all lie inside |Re z|≤A. Removing the m copies of w from the product, the residual logarithmic derivative calculation in L127 gives a quartet contribution to c(w) of

−m/b−mb/(a²+b²).

That calculation also holds for m=1 by L064 and its product rule. All remaining imaginary terms are 2(Im ρ−b)/|w−ρ|². They may be summed individually: finitely many zeros lie in any compact set, the copies of w have been removed, and for large |ρ| the denominator is at least |ρ|²/4. The strip bound and reciprocal-square summability then majorize their absolute values by a summable tail. This is the same imaginary-sum justification as in L067; no unpaired complex reciprocal sum is used.

By the additional window hypothesis, every positive term is exterior. Drop all nonpositive terms, use (1), and obtain (3). The interpretation as a local height rate is supplied by L064 for a simple zero and L127 for a multiple zero. ∎

## Qualifications and verification

The estimates are static and conditional on the strip bound. They require no zero separation within the inner window, since all estimated denominators cross the horizontal buffer. With R=2A and A≥H, the exterior interaction tends to zero uniformly over |a|≤A as A→∞. This leaves entirely uncontrolled the positive interaction with zeros in A<|Re ρ|≤2A. Likewise, using (3) requires an inner zero at least as high as every zero in the larger window; existence of such a zero is not proved. Neither the window factor nor the tail limit supplies a time-uniform Taylor remainder or prevents incoming zeros from infinity.

No computation is needed: the verification consists of the monotone ratio comparison (4), the full-multiset factor, absolute imaginary summation, and the multiplicity-m quartet extraction. The result does not change the RH gap.

Formalization would require the uniform geometric comparison, the vanishing tail of a summable nonnegative multiset, splitting the absolutely convergent imaginary sum, and the local rate interpretation with multiplicities. Uniformity in the heat parameter is not claimed.
