# L004 — Exact affine lifts of a binary counter require exponential dimension

## Hypotheses

Fix an integer w ≥ 1, put N=2^w and M=2^(w−1), and let C={0,…,N−1}. The cyclic counter is T(c)=c+1 modulo N. Write b_i(c)∈F₂ for the i-th binary digit of c, with i=0 the least significant digit, and b(c)=(b_0(c),…,b_(w−1)(c)).

An exact affine lift with affine decoding consists of a nonnegative integer d, an arbitrary map φ:C→F₂^d, an affine transition F(z)=Az+a on F₂^d, and an affine decoder D:F₂^d→F₂^w such that, for every c∈C,

    φ(T(c)) = Aφ(c)+a,       D(φ(c)) = b(c).

The equations include the wrap from N−1 to 0. Neither efficiency nor any algebraic form is assumed for the encoding φ. The matrix A need not be invertible away from the encoded orbit. All vector-space operations in the lift and decoder are over F₂.

## Conclusion

The minimum possible dimension is exactly

    d_min(w) = 2^(w−1).

The lower bound already holds if only the most significant bit must have an affine decoder. A lift attaining the bound recovers every bit by a coordinate projection.

Consequently these exact lifts cannot have dimension bounded by one fixed polynomial in w. This rejects polynomial-dimensional, explicitly stored F₂-affine states as a universal way to compress counter runs. It is a bound on this representation, not a lower bound for counter evaluation, general circuits, all implicit representations, or arbitrary computation certificates. It establishes no separation between P and NP.

## Proof

**An invariant space of scalar functions.** Let H be the F₂-vector space of all functions C→F₂. For f∈H define the cyclic shift Sf by (Sf)(c)=f(T(c)), and set Δ=S+I. If φ_1,…,φ_d are the coordinate functions of any lift, let

    V = span_F₂{1, φ_1,…,φ_d} ⊆ H,

where 1 is the constant-one function. Thus dim V≤d+1. The affine update gives Sφ_i=Σ_j A_ij φ_j+a_i·1, while S1=1. Therefore V is invariant under S and under Δ. The affine decoder places the top-bit function h=b_(w−1) in V. Only this decoded bit is needed for the lower bound.

**The top bit forces a long difference chain.** Because M is a power of two, repeated squaring in characteristic two gives

    (S+I)^M = S^M+I.

Indeed, for any commuting operators X,Y in characteristic two, (X+Y)^2=X²+Y²; iterate this identity w−1 times. Advancing the cyclic counter by M flips its most significant bit, including when the addition wraps. Hence

    Δ^M h = S^M h+h = 1,
    Δ^(M+1) h = Δ1 = 0.

The M+1 functions h,Δh,…,Δ^M h are linearly independent. To see this, suppose a nontrivial relation Σ_(j=0)^M α_j Δ^j h=0 holds, and choose the least j₀ with α_j₀≠0. Apply Δ^(M−j₀). The j₀ term is α_j₀ Δ^M h=1, since the only nonzero scalar in F₂ is 1. All later terms vanish because their exponents exceed M; all earlier coefficients are zero. This gives 1=0, a contradiction. All these functions belong to V by invariance, so

    M+1 ≤ dim V ≤ d+1,

which proves d≥M. This reasoning allows dependent coordinate functions, a nonlinear or nonuniform encoding, a singular A, and an affine rather than linear decoder.

**A matching lift.** For 0≤k≤M define

    p_k(c) = binom(c,k) modulo 2,

using binom(c,k)=0 for k>c, and take φ(c)=(p_1(c),…,p_M(c)). The omitted coordinate p_0 is identically 1. Pascal's identity gives, for c<N−1,

    p_1(c+1) = p_1(c)+1,
    p_k(c+1) = p_k(c)+p_(k−1)(c)       (2≤k≤M).

Use these formulas to define the affine map F on every z∈F₂^M. They also give the correct cyclic wrap. In F₂[u], repeated squaring yields (1+u)^N=1+u^N. Thus binom(N,k) is even for 1≤k≤M<N. Applying Pascal's identity at c=N−1 shows that the update sends φ(N−1) to the zero vector, which equals φ(0). Therefore φ(T(c))=F(φ(c)) for all c∈C.

For bit decoding, factor the same polynomial using the binary digits of c:

    (1+u)^c = ∏_(j=0)^(w−1) (1+u^(2^j))^(b_j(c))    in F₂[u].

The coefficient of u^(2^i) on the left is p_(2^i)(c). In the product on the right, powers below 2^i sum to at most 2^i−1, and powers above 2^i are too large. Therefore the only possible selection producing exponent 2^i is its own factor, and this coefficient is exactly b_i(c). Since 2^i≤M for every i<w, every bit is recovered by the coordinate projection

    D(z)_i = z_(2^i).

This is a linear, hence affine, decoder. There are exactly M coordinates, proving attainability and the claimed minimum. For w=1 the construction is just φ(c)=c, F(z)=z+1; the lower-bound chain is h,1, so the same proof includes the smallest case.

**Required bound and scope.** The contemplated intermediate target was d≤K(w+1)^k for fixed constants K,k across all widths. The exact bound d=2^(w−1) exceeds every such polynomial. For a full counter cycle of length T=2^w it is T/2: explicit lifted coordinates retain a linear-in-horizon cost, despite a horizon describable in w+1 bits. Repeated squaring of an explicitly stored affine matrix runs in time polynomial in d and log T; this dimension result prevents that generic method from obtaining polynomial-in-w cost by a small lift of the stated kind.

The main NP requirement is a bound polynomial in the full language input length n, not in w alone. If w=O(log(n+1)) with one fixed implicit constant, this dimension can still be polynomial in n. If a proposed representation must cover the full cycle at width w=ceil(q log₂(n+1)), with q≥1 and n≥1, its dimension is at least (n+1)^q/2. Allowing arbitrary q then prevents one fixed polynomial bound in n for explicitly stored coordinates. This is a conditional comparison of scales, not an assertion that every computation or every certificate for the diagonal language must realize such a full cyclic subsystem.

This is not an intrinsic cost of counting. A counter at time t is simply c+t modulo 2^w, computed by ordinary binary addition in polynomial time in w+log(t+1). The exponentially many lift coordinates above can also have a short implicit description; the dimension bound is not a lower bound on the length or evaluation cost of every such description. Changing the coefficient ring, the exactness requirement, the global affine update, or the decoder changes the hypotheses. Nor is a cyclic-counter macrostep asserted to be one transition of an arbitrary Turing machine. The result obstructs a proposed representation for this simple dynamical system; it supplies neither a universal trace verifier nor a lower bound for every verifier of the diagonal language.

**Finite sanity check.** `python3 scripts/affine-counter/check_small_cases.py` independently computes binomial-coordinate vectors and cyclic difference ranks for 1≤w≤8. It checks every transition including wrap, every decoded bit, and rank M+1 of the difference chain. The recorded output is in [the small-case report](../scripts/affine-counter/small-cases.txt). These finite checks detect indexing or boundary errors; the proof for every w is the symbolic argument above.

## Mathlib

Coverage: **not checked** for the full minimum-dimension statement or the supporting function-space, binomial, and characteristic-two identities. No matching Mathlib theorem, absence claim, or unverified identifier is asserted. All required mathematical identities and the dimension argument are proved above; no external theorem is used as a substitute for the full result.
