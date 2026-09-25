# Repeated-cube factorization test — 2026-09-25

This is one focused informal step, not a candidate proof of Beal.

## Starting state and relevance

The shared instructions, local goal, checkpoint, whole overview, DAG, relevant proofs, and prior attempt were read before choosing work. Existing changes and both completed branches are preserved. The checkpoint selected the remaining ordered family a^3+b^3=c^p for primes p >= 5. L002 and C002a do not exclude this family; L001 rules out using unrestricted congruences alone. No existing lemma records its factorization conditions.

The gap addressed is nonexistence in this one residual family, within the larger unproved uniform residual-signature exclusion. The intermediate target is an exact, reversible split of (a+b)(a^2-ab+b^2)=c^p into perfect-power conditions, including the exceptional prime 3, with an explicit description of the remaining simultaneous constraint. This could supply the integer input for a descent, a constrained square-discriminant argument, or a modular method. Such a further exclusion and all other residual families remain unresolved.

The test is to derive the exact gcd and 3-adic valuations, prove both directions with positivity and primitivity retained, and check whether separate factor conditions already force a contradiction. Continue with a global simultaneous constraint if the reduction is sound but admits single-factor witnesses; abandon any exclusion based solely on the quadratic factor if such a witness exists. The actual required threshold is zero primitive solutions for every p in the selected range; an equivalent system or a growing interval is not that threshold.

## Reasoning saved before completion

Write s=a+b and q=a^2-ab+b^2=s^2-3ab. Coprimality of a,b implies gcd(s,q) divides 3. If 3 divides s, neither a nor b is divisible by 3 and q=3(3k^2-ab) for s=3k, so v_3(q)=1 exactly. Thus the anticipated branches are s=u^p, q=v^p, c=uv with 3 not dividing uv, or s=3^(p-1)u^p, q=3v^p, c=3uv with 3 not dividing v. The latter allows 3 to divide u; the exact expected relation is v_3(s)=p v_3(c)-1.

With d=a-b the identity 4q=s^2+3d^2 should provide a reversible discriminant condition, provided parity, |d|<s, and gcd((s+d)/2,(s-d)/2)=1 are handled. In the gcd-one branch the proposed equation is u^(2p)+3d^2=4v^p. In the gcd-three branch it is d^2+3^(2p-3)u^(2p)=4v^p. No descent or square exclusion has yet been obtained from these equations.

The explicit test pairs (a,b)=(62,149) and (211,236) appear to give q=7^5 and q=3*7^5 respectively. Their sums must also have the required power shape; that simultaneous condition remains to be checked. These are proposed controls, not Beal solutions.

## Source and redundancy check

Mauldin's [primary problem page](https://sites.math.unt.edu/~mauldin/beal.html) was reread and retains the positive-integer statement; the nominated AMS endpoint again failed retrieval. Bennett–Mihailescu–Siksek, [The Generalized Fermat Equation, section 2, PDF pages 3–4](https://samirsiksek.github.io/siksek.github.io/papers/bealconj.pdf#page=3), explicitly recalls the standard gcd-of-factors observation and exceptional-prime valuation. The elementary split is therefore not claimed as a new literature result. A full proof specialized to this notebook's exact positive primitive family will be recorded locally.

A bounded primary-source search also located Nuno Freitas, [On the Fermat-type Equation x^3+y^3=z^p](https://arxiv.org/abs/1601.06361), whose abstract states an exclusion when -3 is a nonsquare modulo p. Only the abstract was read at this stage. This is a possible subsequent global input, not an applied theorem or a new exclusion in this step; its theorem hypotheses and proof scope still need audit.

## Completion

[L003](../lemmas/L003-repeated-cube-factorization.md) proves the factor conditions and their full converse. It permits every n>=2 because the proof does not use primality; only n=p>=5 prime is the selected Beal family. The converse obtains parity from 4q=s^2+3d^2, positivity from |d|<s, and coprimality from the factor gcd together with the exact valuation of q. In the second branch 3 may divide u. Every prime divisor of v is 1 modulo 3, by an order-three element in the residue field.

The two proposed quadratic-factor witnesses pass exactly, and both fail their required sum-power condition. Conversely, (p,u,v)=(5,4,13) in the first branch and (5,3,37) in the second satisfy the factor-power, coprimality, prime-support, and real positivity constraints but have nonsquare discriminants. These examples distinguish the two factors from the unresolved simultaneous condition. The single-factor shortcut is closed in [Attempt 002](../ATTEMPTS/002-repeated-cube-single-factor-exclusion.md); the overall factorization route is not declared impossible.

The achieved bounds are v in [4^(-1/p)u^2,u^2) in the first branch and in [4^(-1/p)3^(2-3/p)u^2,3^(2-3/p)u^2) in the second. Each width grows with u^2 for a fixed p. These are not upper height bounds and do not meet the required zero-solution threshold. The second branch also gives s>=3^(p-1), which is a lower bound only. There is no decreasing-height construction or complete candidate.

The exact-arithmetic checks in `python3 scripts/repeated-cube-factorization/check_factorization.py` passed 19,948 coprime pairs with 1<=a<=b<=256, including 4,979 factor-gcd-three cases and sum valuations up to five. Three genuine n=2 solutions exercise both converses and the base-one boundary. Twelve formal factor-data cases exercise the ramified valuation allocation, including 3 dividing u; they are not claimed to arise from cube solutions. The two single-factor witnesses and two nonsquare-discriminant controls also pass. The [results](../scripts/repeated-cube-factorization/results.json) are checks of the algebra, not an exhaustive Beal exclusion.

Outcome: ADVANCE, limited to a relevant exact intermediate input and its qualifications; exploration turns outstanding: 0/3. The missing global exclusion has been localized, not solved. A precise audit of the located Freitas theorem is motivated by its claimed global reach beyond these elementary constraints; its abstract alone is not an applied theorem. Mathlib coverage is not checked.
