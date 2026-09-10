# Lemma 58: heat deformation and local zero motion

**Hypotheses.** K is the exact theta kernel of Lemma 19. For (λ,z)∈C² define

F(λ,z)=Ξ_λ(z)=∫₀^∞ exp(λu²)K(u)cos(zu)du.

**Conclusion.** F is jointly entire. Every mixed derivative is given by differentiating its integrand, locally uniformly in both variables. In particular F_λ=-F_zz and F(0,z)=Ξ(z). For real λ, F is even in z, respects complex conjugation, and F(λ,0)>0.

If λ₀,x₀ are real, F(λ₀,x₀)=0 and F_z(λ₀,x₀)≠0, there is a unique local analytic zero branch x(λ) through x₀. It is real and simple for real λ sufficiently near λ₀ and satisfies

x'(λ)=F_zz(λ,x(λ))/F_z(λ,x(λ))

= [∫₀^∞u² exp(λu²)K(u)cos(x(λ)u)du] /
  [∫₀^∞u exp(λu²)K(u)sin(x(λ)u)du].

These are local assertions, with no assumption or conclusion that every zero is real at any parameter.

## Proof

### Explicit uniform domination

By the positive summand formula in Lemma 19, for u≥0,

0<K(u)≤8π² exp(9u/2-π exp(2u)) Σ_{n≥1} n⁴ exp(-π(n²-1)).

Set q=exp(-π). Since n²-1≥n-1, a valid explicit constant is

C=8π²(1+11q+11q²+q³)/(1-q)^5,

so K(u)≤C exp(9u/2-π exp(2u)). The series identity Σ_{n≥1}n⁴q^(n-1)=(1+11q+11q²+q³)/(1-q)^5 follows by applying q d/dq four times to the geometric series and dividing by q; absolute convergence justifies these operations.

Fix L,R≥0 and derivative orders a,b≥0, and put p=2a+b. On |λ|≤L, |z|≤R the absolute value of the differentiated integrand is bounded by

C u^p exp(Lu²+(R+9/2)u-π exp(2u)).                         (1)

Indeed λ differentiation supplies u^(2a), z differentiation supplies u^b and a signed sine or cosine, and both trigonometric functions have modulus at most exp(Ru).

For an explicit integrable bound put B=R+11/2 and

U=max(1, 3(L+B)/(2π)).

The exponential series gives u^p≤p! exp(u) and exp(2u)≥(4/3)u³. For u≥U,

(π/2)exp(2u)≥(2π/3)u³≥(L+B)u²≥Lu²+Bu.

Thus (1) is at most C p! exp(-(π/2)exp(2u))≤C p! exp(-πu) on this tail. On [0,U] it is at most C p! exp(LU²+BU). These two bounds provide an explicit integrable majorant for each mixed derivative on every compact parameter set.

Integrals truncated at finite u are jointly holomorphic, as follows by integrating the locally uniformly convergent exponential and trigonometric power series. The bound proves their locally uniform convergence on C², so the Weierstrass theorem for holomorphic functions gives joint entirety. The derivative bounds, or dominated differentiation followed by the same locally uniform convergence, give the stated mixed derivative formulas. Consequently

F_λ=∫₀^∞u² exp(λu²)K(u)cos(zu)du=-F_zz.

Lemma 20 identifies F(0,z). Evenness and conjugation follow directly from the integrand, and strict positivity at zero follows from K>0. Joint holomorphy in particular gives real analytic, hence smooth, parameter dependence on the real λ-axis.

### Local zero branch

Apply the holomorphic implicit function theorem at (λ₀,x₀). It supplies neighborhoods and a holomorphic x(λ), unique among zeros in a sufficiently small neighborhood of x₀, with F(λ,x(λ))=0. Shrink these neighborhoods so F_z stays nonzero along the branch. For real λ, complex conjugation produces another zero near x₀; choose a conjugation-invariant z-neighborhood. Uniqueness gives x(λ)=overline{x(λ)}, proving reality. Differentiating the identity gives

0=F_λ+F_z x'=-F_zz+F_z x',

which proves the quotient and, using the integral derivatives, its displayed integral form. The denominator is nonzero exactly because the branch is simple.

### Scope at λ=0

In particular, any simple real zero already known at λ=0 persists as a real simple zero for a sufficiently small two-sided interval in λ. No uniform interval over infinitely many zeros follows. Conversely, a branch starting at another parameter reaches zero by this argument only if continuation to zero is separately justified. If along such continuation x(λ) has a finite limit x_* at a finite endpoint λ_* and F_z(λ_*,x_*)≠0, continuity and the implicit function theorem extend it through the endpoint. The local argument does not rule out a multiple zero or escape to infinity, nor does it account for other zeros not on the chosen branch.

Positivity of K gives no sign to the oscillatory integrals in the velocity formula. No sum over other zeros is used: a global product and convergence justification for deformed transforms would be additional work.

For an exact illustration of the logical limitation of the PDE and local motion law alone, the real even polynomial P(λ,z)=z²+2(c-λ), with real c, satisfies P_λ=-P_zz. At λ>c its two zeros are simple and real with x'=1/x=P_zz/P_z; at λ=c they collide, and at λ<c they are nonreal. Choosing c>0 shows that reality at a positive parameter plus this local law does not imply reality at zero. This polynomial is not claimed to have the theta integral representation or its positivity at z=0; it tests only the proposed inference from the PDE and local law. No counterexample to RH or to a theorem using additional theta structure is asserted. ∎

## Verification and formalization obligations

The proof is analytic; no numerical certificate is needed. The mixed derivative sign, explicit tail cutoff, conjugation argument, and polynomial collision can each be checked directly from the displayed formulas. Formalization would require the geometric-series derivative identity, the two-piece majorant (1) for every a,b,L,R, holomorphic parameter integration and its derivatives, and the holomorphic implicit function theorem with local uniqueness. No global real-zero theorem or assertion that the zeros of Ξ are simple is an input or an output.
