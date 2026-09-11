# Lemma 66: imaginary motion at a highest simple zero

**Hypotheses.** In a real theta heat slice of Lemma 64, let w=a+ib be a simple zero with a≠0 and b>0. Its distinct quartet is Q={w,-w,conjugate(w),-conjugate(w)}. For the sign assertion additionally suppose every zero ρ of this slice satisfies Im(ρ)≤b. Multiplicities of other zeros are unrestricted.

**Conclusion.** The contribution of the other three members of Q to the imaginary velocity of the local branch through w is

Im V_Q(w) = -1/b - b/(a²+b²).                              (1)

Without the maximal-height hypothesis this formula still holds. Under that hypothesis, write R for the contribution of all zeros outside Q, grouped into opposite pairs as in Lemma 64. Then

Im R≤0,
(d/dλ) Im z(λ)|_{λ=λ₀} ≤ -1/b-b/(a²+b²)<0.               (2)

Moreover Im R<0 if there is any zero outside Q. These are conditional, instantaneous inequalities at a simple zero, not an existence assertion about highest zeros.

## Proof

Simplicity, evenness and conjugation give multiplicity one to all four members of Q. Lemma 64 gives the velocity as twice the sum of reciprocal differences, with the distinguished opposite member separated and all remaining zeros paired. Extracting the finite quartet contribution yields

V_Q(w)=2/(w-(-w))+2/(w-conjugate(w))+2/(w+conjugate(w))
      =1/w+1/(ib)+1/a.

Taking imaginary parts proves (1). All denominators are nonzero by a≠0 and b>0.

Choose representatives α=u+iv of the remaining opposite pairs, with multiplicity. The maximal-height hypothesis applied to both α and -α gives -b≤v≤b. Their contribution has imaginary part

Im[2/(w-α)+2/(w+α)]
 = -2(b-v)/[(a-u)²+(b-v)²]
   -2(b+v)/[(a+u)²+(b+v)²].                             (3)

Both denominators are positive: these remaining zeros are distinct from w. Both numerators are nonnegative, and at least one is positive since their sum is 2b>0. Thus every remaining pair has strictly negative imaginary contribution.

Lemma 64 supplies absolute convergence of the complex paired series, so its imaginary part is the sum of the imaginary parts of the pairs. Equation (3) and this convergence prove Im R≤0, strictly if any term exists. There is no illicit use of an unpaired complex reciprocal series. Indeed, under the present sign hypothesis even the unpaired imaginary contributions are absolutely summable: within each pair the sum of their absolute values equals minus the imaginary part of the pair, bounded by its complex modulus. Summing the latter bound uses exactly the convergence already proved. Combining with (1) gives (2). ∎

## Qualifications

A zero of maximal positive imaginary part need not exist merely because the imaginary parts are bounded above. This lemma does not prove attainment, a finite strip bound for arbitrary real heat parameters, or a uniform estimate for zeros escaping to infinity. The distinguished zero must be simple; collisions require separate analysis. Other zeros at height b cause no sign problem: their individual imaginary contribution is zero, and their opposite partners are below b.

The exclusion a=0 is part of the distinct-quartet hypothesis. The proof does not need an additional imaginary-axis nonvanishing theorem. No claim that a hypothetical quartet occurs in a theta slice is made. The strict decrease at a highest simple zero does not imply that every nonreal zero disappears before λ=0, and supplies neither initial global reality nor RH.

## Verification and formalization obligations

The proof uses Lemma 64 directly; Lemma 65 is motivation only. Check the three reciprocal differences, the heat-parameter sign inherited from Lemma 64, and both inequalities -b≤v≤b. Run `python3 scripts/heat/check_highest_zero_motion.py` for exact rational checks of (1) and (3), including equal-height zeros and multiplicities. These algebraic checks are not theta-zero evidence. Formalization would require extraction of a finite quartet from an absolutely convergent paired series, the imaginary reciprocal identity, and summation of the nonpositive real terms. No parameter differentiation of an infinite series is used.
