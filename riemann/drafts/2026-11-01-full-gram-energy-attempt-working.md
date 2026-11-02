# Full-Gram logarithmic-degree energy: bounded mathematical attempt

1 November 2026. Completed bounded attempt under the invocation-start EXPLORE
assessment `literature/2026-11-01-full-gram-log-degree-energy.md`.
The target is its exact six-term relative half-budget, with theta=1/100,
all complex shifts, the exact phase and every tail coordinate retained.
No new source comparison, global sign or RH claim is being made.

Main gap: actual-Xi pointwise initial signs at unbounded heights and
all-degree mixed positivity. A successful relative bound would supply
an averaged coefficient-uniform detector margin after L622 transfer;
it would not prove pointwise positivity. Continue only with a complete
half-budget or a rigorous obstruction. An oversized upper bound is
inconclusive. Stop an uncontrolled growing-prime/tail/signed-jet estimate.

Read the full supplied assessment and overview/DAG. Checked the relevant
freezing and finite-prefix stop records and reused the collective
arithmetic and L622 transfer assessments. Existing unfinished work is
preserved. No cross-notebook input is used.

Initial application checks: L623's prime autocorrelation, full Gram
identity (1), finite-inverse lower bound and its transfer-scale arithmetic
are consistent. In L624 (1), common multiples r=lcm(m,n)d give r/m=kd
and r/n=hd, hence exactly the stated two increment orientations. Its
local formula (5) is analytic and nonzero for the stated compact shift
domain; exponent-polynomial derivatives remain summable for fixed N.
In (8), finite coefficient expansion and L622's Hermitian convention
give the real part of the complete six-term sum. This checks the used
identities, not any uniform derivative bound or the unused conclusions.

Current test: write the zero-shift image as the analytic torus polynomial
P times the full product of (1-z_p/sqrt(p))^(-2). The image has infinite
logarithmic degree even when P has degree <=log N. A direct multiplier
supremum bound may lose growing-prime uniformity; whether the finite
polynomial image prevents that loss is the present mathematical issue.
No quantitative energy estimate or signed comparison has yet been proved.

## Calculation checkpoint

The next calculation gives a candidate first-jet estimate, not the signed
half-budget. Put t=p^(-1/2), x=t^2, C=(1-x)^3/(1+x),
rho=2t/(1+x), s=(1-x)/(1+x). The weighted circle polynomials are
1, (z-rho)/s, and z^(k-2)(z-t)^2/sqrt(C) for k>=2.
After multiplication by sqrt(C)/(1-tz)^2 these form an orthonormal
rational basis f_k. Tensor products indexed by n<=N span the complete
Gram image of coefficient polynomials of length N, including its tails.

For H_p=tz/(1-tz), the basis matrix has diagonal
h0=x(2+x)/(1-x^2), h1=x^2/(1-x^2), hk=0 (k>=2), one lowering
entry H_(0,1)=-t^3/(1-t^4), and raising entries bounded by
(4/3)t^(k-l). Exact boundary entries are retained in the final proof.
For H=sum_(p<=N)(log p)H_p, M=log N, and
S1=sum log(p)/(p-1), S2=sum (log p)^2 p/(p-1)^2,
S3=sum (log p)p^(-3/2)/(1-p^(-2)), the raising part has norm
at most (4/3)sqrt(M S1+S2) on that finite input subspace.
The output is infinite: Cauchy--Schwarz uses
sum_(p^j|m)log p=log m, followed by an absolutely convergent sum over
m=np^j with no m<=N cutoff. The diagonal and lowering bounds are
2S1 and S3. Elementary estimates S1<=2M+3, S2<=2M S1, S3<6
would give ||Hf||<=(8M+16)||f||.

For the analytic arithmetic normalization, partial_j log C_N(0)
equals mu=sum(log p)h0. Subtracting mu changes the diagonal bound
to (4/3)M, giving ||(H-mu)f||<=((16/3)M+10)||f|| and the same
relative bound for each first scalar shift derivative of L624 (1).
At N=floor(T^(1/100)), the scaled bounds approach 0.08 and 4/75.
Higher and mixed derivatives do not follow by iterating this estimate:
Hf is no longer in the finite coefficient-polynomial image. This
remaining obstruction to the argument is explicitly retained.

## Completed result and continuation boundary

The complete first-jet proof, exact local boundary entries, full infinite
raising sum, constants and normalization are now canonical in
[L627](../lemmas/L627-full-divisor-first-shift-energy-bound.md).
Its estimates (1) and (2) give a relevant local ADVANCE, pending separate
critical audit, within the already assessed target. They are not a proof
of the relative half-budget or a claim of progress beyond the literature
checked. No mathematical script or finite-tail experiment was used.

The material new input is control of the first full-space derivative,
including the analytic normalization, uniformly in the prime support.
The approved target and its assessment remain unchanged. A continuation
must check the exact local matrix and obtain higher weighted moments or
another justified higher-jet estimate; it may not apply the restricted
first-jet norm bound to its own infinite-output vector. No signed error,
negative eigenvalue, sign certificate or RH candidate has been obtained.
