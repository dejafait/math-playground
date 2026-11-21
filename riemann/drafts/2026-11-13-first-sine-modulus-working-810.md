# Approved first-sine modulus calculation — step810

Invocation-start coverage: `drafts/literature/2026-11-13-low-energy-first-sine-modulus-test-809.md`, SPECIALIZE; exact fixed pair, no sweep. Classification REPRODUCTION.

Write u(x)=sin(pi*x) on(0,1), zero elsewhere, v(x)=u(-x).
Then s1=u-v and |s1|=u+v. Both are continuous piecewise C1 with
zero traces, hence in H_0^1(-1,1), with norm1. Their weak derivatives
have no delta masses because their values match at each join.

For d>0 the correlation difference is 2H(d), where H=u*u is supported
in[0,2]. Put h=min(d,2-d). On this interval direct integration gives
H(d)=(sin(pi*h)/pi-h*cos(pi*h))/2>=0.
Near0, H(d)=O(d^3), so k(d)H(d) is integrable for
k(d)=2exp(-d/2)/(1-exp(-2d)). L741's full-line regularized multiplier
identity and C759a's domain identify the archimedean difference as
-2 integral kH; the scalar subtraction cancels because the norms agree.
Pending canonical write-up: justify use on these H1 tests by the
full-line logarithmic multiplier convergence, rather than calling the
modulus smooth.

Tonelli and the convolution Laplace transform give
integral exp(-b*d)H(d)dd=[pi*(1+exp(-b))/(b^2+pi^2)]^2.
Thus the gamma defect is -4 sum over b=2j+1/2 of these terms.
Keep512 terms and bound the unsigned omitted sum by
4*pi^2*[B^-4+B^-3/6], B=1024+1/2. The gamma-defect radius is
four times this bound. Every prime contribution is -4*a_n*H(log n)
for n=2,3,4,5,7. Both poles give 4*(Iplus^2+Iminus^2), where
Iplus/minus=pi*(1+exp(plus/minus1/2))/(pi^2+1/4).

Completed: the full certificate encloses Delta1 between0.00111835
and0.00111838, above the required threshold0, with all7 checks passing.
The exact capped positive-eta decrease stops. Full proof, domain
justification and qualifications are canonical in C759e; the script
and certificate are `scripts/spectral-triples/first-sine-modulus-810.py`
and `.json`. Separate conceptual audit remains pending; parity/Xi
assumptions remain open. This draft preserves the calculation route,
not a second canonical proof or current next-action record.
