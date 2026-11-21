# Step 299 — first-prime remainder comparison, working record

The exact target and its prior EXPLORE approval are in
`drafts/literature/2026-11-04-beckner-first-prime-remainder-budget.md`.
This is one mathematical attempt, with the source identity imported.
The main gap is unconditional actual-Xi mixed positivity. The bounded
test is Q_2 <= R_B/2 at L=4log3, for complex smooth zero extensions
with both exact global exponential moments. A proof pays only the
first prime; a certified strict smooth witness stops this allocation
and window. Other primes, spatial/digamma corrections, arbitrary
complements and support propagation remain unresolved.

L743 (1) supplies the arithmetic coefficient; L744 (6) supplies the
downstream complete-energy normalization. Their prime-only and
carrier-scope stops have been checked and do not decide this target.
No conclusion of L742 or L745, and no spectral endpoint assertion,
is an input. Prior notebook changes are preserved.

Initial approach: exploit the literal weighted difference integral,
including exterior pairs, by logarithmic radial coordinates on the
two half-lines. A trial calculation, if used, is only a lead until
its smoothness, exact moments, complete integral and strict margin
are justified. If no proof or certificate results, preserve the
specific obstruction and report EXPLORATION, not a sign conclusion.

Writing y=+/-exp(t), v_+/-(t)=exp(t/2)h(+/-exp(t)), changes
the same-sign kernel to 1/(2|sinh((t-u)/2)|) and the opposite-sign
kernel to 1/(2cosh((t-u)/2)). This is a direct nonnegative change
of variables, not a Fourier or endpoint import. For even h, v_+=v_-=v,
R_B=(1/4) integral |v(t)-v(u)|^2 k(t-u) dt du with
k(s)=csch(|s|/2)+sech(s/2)=4 sum_(m>=0) exp(-(2m+1/2)|s|).
Zero extension in t retains every exterior pair. For odd h the
opposite-sign term uses |v(t)+v(u)|^2. The shift form and moments
split by centered parity. The odd resource gap needs a complete
argument before it can be used; the even constrained comparison is
the unresolved test.

`scripts/beckner-budget/neutral-even-preview-299.py` records a
nonrigorous midpoint screen, including exact exterior diagonal
potential W(r)=atanh(sqrt(r/b))+atan(sqrt(r/b)), b=2log3.
At n=128,256,512 the discrete maxima Q_2/R_B are about
0.2760,0.2982,0.3167, below 1/2 but increasing with center resolution.
These are not continuum bounds or certified witnesses. The center
singularity motivates a logarithmic-cell screen, with exact pair
integrals, before any interpretation of the threshold.

The logarithmic-cell preview also remains below 1/2 and has no
continuum error certificate. It does not exclude a multiscale witness.

Promising analytic construction, saved before completing the proof:
take a nonnegative even center profile h_0,N=|y|^(-1/2)v_N(log|y|),
where v_N is a smoothed long interval indicator. Its entire remainder
is uniformly bounded: translation L1 variation <=2|s| in the above
kernel gives R_B<=4 sum_(m>=0)(2m+1/2)^(-2)<=20. It equals
|y|^(-1/2) on the scales u_j=delta exp(-j), j=1,...,N,
delta=a/16. Pair it with the nonnegative even packets
sum_j j^(-1)u_j^(-1/2)[phi((y-a)/u_j)+phi((-y-a)/u_j)],
phi a fixed nonzero smooth bump in (1,2). The shift correlation with
the center is exactly 2 A H_N, A=integral phi(v)/sqrt(v) dv.
Beckner plus Fourier scaling bounds each translated packet's resource
by j*||phi||_2^2+C_phi. Disjoint nonnegative packets have nonpositive
resource cross terms, so their weighted sum costs at most
2||phi||_2^2 H_N+O(1), whereas the raw center costs O(1).

A fixed even correction beta supported in
3a/2<|y|<7a/4 pays the cosh moment exactly. It has no delay-a
interaction with the raw supports, and is a fixed positive distance
from them. Raw L1 norms are uniformly bounded, so the correction
costs O(1) in the full resource. This would give, for a fixed positive
lambda, Q_2-R_B/2 >= (2 c lambda A-lambda^2 d)H_N-C,
c=sqrt(2)log2, d=||phi||_2^2. Setting lambda=c A/d makes the
coefficient positive. Every finite-N function is smooth with a center
hole. No singular limiting function need be admitted to the class.

The completed analytic construction, all factors, plateau/support
margins, source normalization and a specified finite-N threshold are
now canonical in L746. It gives Q_2-R_B/2>1 for that finite smooth
exact-neutral witness. The construction is unaudited pending the
separate conceptual review; no complete-energy or RH claim follows.
The initially considered odd-sector lower bound was not needed and
is not asserted as a separate result. The saved numerical previews
remain inconclusive, with no certified continuum eigenvalue bound.
