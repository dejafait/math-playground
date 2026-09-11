# Lemma 127: forward splitting and height at a nonreal multiple zero

**Hypotheses.** Let F be the theta heat family of L058, λ₀ real, and f(z)=F(λ₀,z). Suppose w=a+ib, b>0, is a zero of exact multiplicity m≥2. Put h(z)=f(z)/(z-w)^m, with its removable value at w, and A=h'(w)/h(w). For the upper-height inequality additionally suppose every zero ρ of f has Im ρ≤b.

**Conclusion.** Let α₁<⋯<α_m be the real simple roots of the polynomial P_m defined in L060. In a fixed sufficiently small disc about w the m forward zeros, for t>0 sufficiently small, are simple and have expansions

z_k(λ₀+t)=w+α_k sqrt(t)+2A t+O(t^(3/2)).                 (1)

The remainder is uniform over these finitely many branches. Consequently their local maximum height satisfies

max_k Im z_k(λ₀+t)=b+2 Im(A)t+O(t^(3/2)).               (2)

For a highest zero as hypothesized,

2 Im A ≤ -m/b-mb/(a²+b²)<0.                            (3)

Thus (2) gives a strictly negative right derivative of this local maximum, with the bound (3). The order-t term is the first nonzero imaginary-height correction in this highest-zero case. Without the highest-zero assumption it is the first *potentially* nonzero correction; if Im A=0 this statement does not identify the first later nonzero term, which need not exist.

## Proof

### Rescaling and the common order-t displacement

Write c=h(w)≠0. The spatial Taylor expansion starts as

f(w+u)=c u^m+c A u^(m+1)+O(u^(m+2)).

Joint holomorphy and F_λ=-F_zz from L058 give
∂_λ^j∂_z^k F(λ₀,w)=(-1)^j f^(2j+k)(w). Hence substitution t=s², u=sv in the convergent joint Taylor series gives the holomorphic extension

G(s,v)=s^(-m)F(λ₀+s²,w+sv)
      =c[P_m(v)+s A P_(m+1)(v)+O(s²)].                 (4)

The remainder is holomorphic and locally uniform for bounded v. Indeed all Taylor terms of weight 2j+k<m vanish, and after substitution the normally convergent series is divisible by s^m. Cauchy estimates on smaller s and v discs justify both division and the two displayed coefficients, exactly as in the rescaling proof of L060; that argument requires no reality of w.

L060 proves reality and simplicity of the roots of P_m and the recurrence P_(m+1)=vP_m-2mP_(m-1). Direct differentiation of its coefficient formula gives P_m'=mP_(m-1). At each root α_k,

P_(m+1)(α_k)=-2P_m'(α_k).

The holomorphic implicit function theorem in (4) therefore supplies a branch v_k(s) with

v_k(0)=α_k,  v_k'(0)=-A P_(m+1)(α_k)/P_m'(α_k)=2A.

Multiplication by s proves (1), with an O(s³) holomorphic remainder. Choose a spatial disc isolating the multiplicity-m zero of f. Uniform convergence on its boundary and Rouché's theorem keep exactly m zeros inside for small s. The constructed branches are inside and distinct for s≠0 because their v_k(0) are distinct. They exhaust the zeros and are simple. Taking s=sqrt(t)>0 makes the leading displacement real. The finite uniform error proves (2), even though the branch achieving the maximum can change.

### Residual product and the sign

First a≠0: for real y the defining integral is
F(λ₀,iy)=∫₀^∞ exp(λ₀u²)K(u)cosh(yu)du>0,
with convergence supplied by L058. Evenness and conjugation therefore give a distinct quartet w,-w,conjugate(w),-conjugate(w), each of multiplicity m.

Remove all m copies of the pair {w,-w} in L063 and write

f(z)=(1-z²/w²)^m H(z).

The residual product H is nonzero near w. Since
h(z)=(-1/w²)^m(z+w)^m H(z),

2A=m/w+2H'(w)/H(w).

For the remaining pair representatives α, with multiplicity, the normal logarithmic differentiation justified in L064 gives

2A=m/w+2 Σ_α [1/(w-α)+1/(w+α)].                       (5)

That proof applies to this residual product unchanged: away from finitely many factors its logarithms and derivatives are uniformly bounded by constants times |α|^(-2). Thus the paired series converges absolutely; no unpaired complex reciprocal sum is asserted.

Extracting the m copies of the conjugate pair in (5) gives the finite contribution

m[1/w+1/(ib)+1/a],

whose imaginary part is -mb/(a²+b²)-m/b. For any remaining pair α=u+iv, the highest-zero assumption gives -b≤v≤b. Its imaginary contribution is

-2(b-v)/[(a-u)²+(b-v)²]-2(b+v)/[(a+u)²+(b+v)²]≤0.

The denominators are nonzero because all copies of the distinguished quartet were removed. Absolute convergence of the paired series permits summation of these nonpositive imaginary parts and proves (3). This also explains why the local height rate has a factor m, rather than the simple-zero factor one. ∎

## Qualifications and verification

All radii, parameter intervals, and remainder constants depend on the fixed zero and slice. No uniform estimate over infinitely many zeros or derivative of the whole-plane strip supremum follows. No existence of a highest zero, parameter-local global strip bound, or RH assertion is made. The order-sqrt(t) spatial derivative diverges on noncentral branches, but its leading part is real and does not invalidate the finite height derivative.

The analytic proof checks normal rescaling, the implicit derivative, local zero counting, and convergence before taking signs. `python3 scripts/heat/check_multiple_zero_coefficient.py` independently checks the polynomial identities with exact rational coefficients for m=2,...,30; the all-m proof is the coefficient identity above, not extrapolation from these checks.

Formalization would require the normally convergent weighted expansion through weight m+1 at a complex center, implicit branches with a uniform cubic remainder, the local Rouché count, the residual-product logarithmic derivative with multiplicity, and taking the maximum of finitely many expansions with equal linear coefficient.
