# Lemma 128: bounded-domain upper-height derivative

**Hypotheses.** Let F be the theta heat family of L058, λ₀ real, and f(z)=F(λ₀,z). Let Ω be a bounded open subset of C such that f has no zero on ∂Ω. Suppose Ω contains a zero and

B=max{Im w: w∈Ω, f(w)=0}>0.

Let T be the set of distinct zeros in Ω at height B. For w∈T let m_w be its exact multiplicity and set h_w(z)=f(z)/(z-w)^(m_w), removing the singularity at w. Define

c_w=2 Im(h_w'(w)/h_w(w)).

**Conclusion.** There is ε>0 such that for 0≤t<ε the zeros in Ω form a nonempty finite multiset, no zero lies on ∂Ω, and their maximum height B_Ω(t) satisfies

B_Ω(t)=B+t max_{w∈T} c_w+O(t^(3/2)).                    (1)

In particular its upper right Dini derivative, defined as limsup_{t↓0}(B_Ω(t)−B)/t, is an ordinary right derivative and equals max_{w∈T}c_w.

If additionally every zero ρ of f in the whole plane has Im ρ≤B, then, writing w=a_w+iB,

D⁺B_Ω(0) ≤ max_{w∈T}[−m_w/B−m_w B/(a_w²+B²)] < −1/B. (2)

The global-height hypothesis in (2) is separate from boundary isolation. Neither is implied by merely being a highest zero inside Ω.

## Proof

### Compact isolation prevents incoming zeros

L058 gives joint holomorphy and f(0)>0, so f is not identically zero. Its zeros in the compact set closure Ω are finite: an infinite set would have an accumulation point in C and force f to vanish identically. By boundary nonvanishing all these zeros lie in Ω. Thus B and the nonempty finite set T are well-defined, with each multiplicity finite.

Choose pairwise disjoint closed discs around all distinct zeros in Ω, contained in Ω, each containing just its center as a zero of f. Their boundary circles have no zeros. The compact set

K=closure Ω minus the union of the open discs

has no zero of f, so min_K |f|=η>0. Joint continuity on compact sets gives, for all sufficiently small real |t|,

sup_{z∈K}|F(λ₀+t,z)−f(z)|<η/2.

Consequently there are no zeros on K, including ∂Ω. On every disc boundary this estimate is smaller than |f|, so Rouché's theorem keeps exactly the center's original multiplicity of zeros in the disc. These discs exhaust the zeros in Ω at each such t. This argument needs no regularity or connectedness of ∂Ω and never applies an argument principle to that boundary.

If there are initial zeros below height B, their heights have a strictly positive minimum gap from B. Shrink their discs so their entire closures lie below B−δ for some δ>0. Apply the preceding compact argument with these final discs. The top clusters stay near height B as t↓0 by the local expansions below, and thus exceed B−δ for small positive t. Lower clusters cannot attain the maximum. If there are no lower zeros, this exclusion is unnecessary.

### Finitely many top clusters

For m_w=1, L064 supplies a holomorphic simple branch with derivative f''(w)/f'(w). Since f(z)=(z-w)h_w(z), this ratio equals 2h_w'(w)/h_w(w). Its height is therefore

B+c_w t+O(t²).

For m_w≥2, L127 supplies all forward branches in an isolating disc with height maximum

B+c_w t+O(t^(3/2)).

The hypothesis B>0 makes these centers nonreal, as required there. Its local disc can be used in the compact construction above; after shrinking the time interval Rouché ensures all branches counted there are exactly the constructed ones. There are only finitely many centers and branches. Hence one common time interval and a finite common remainder constant work for all the top clusters. For 0<t≤1 the simple-branch O(t²) is also O(t^(3/2)).

For any finitely many real numbers c_w and errors |r_w(t)|≤Ct^(3/2),

|max_w(c_w t+r_w(t))−t max_w c_w|≤Ct^(3/2),

because t>0. Applying this after excluding the lower clusters proves (1) and its right derivative assertion. No derivative of an infinite supremum is taken.

### Conditional sign

Under the additional global bound, each member of T is a highest zero of the full slice. Its real part is nonzero: the positive theta integral F(λ₀,iy)>0, justified in L058 and used in L127, rules out imaginary-axis zeros. For m_w=1, L066 gives

c_w≤−1/B−B/(a_w²+B²).

For m_w≥2, L127 gives the same bound with the multiplicity factor m_w. Taking the finite maximum proves the first inequality in (2). Each quantity is strictly less than −1/B since m_w≥1, B>0, and a_w is finite. The maximum of this finite nonempty set retains strictness. ∎

## Qualifications and verification

Boundary nonvanishing is an explicit sufficient isolation condition at the initial slice; compact continuity proves its persistence for a short parameter interval. No assumed moving-boundary condition is hidden in the proof. A bounded domain maximum alone supplies the derivative formula, not its sign: zeros outside the domain still enter h_w'/h_w.

The constants η, ε, δ when needed, and the expansion remainders depend on the chosen domain and slice. For an exhaustion by growing domains none is shown uniform. In particular (1) cannot be passed through an infinite supremum, and (2) does not apply at an unattained whole-plane supremum. The result does not prove RH or an inequality for the whole-plane moving strip height.

Verification is analytic: compact zero finiteness, the zero-free remainder, the Rouché counts, exclusion of lower clusters, the factor two for simple zeros, and the finite-maximum estimate were checked explicitly above. No numerical certificate is needed. The coefficient identities reused from L127 can be checked with `python3 scripts/heat/check_multiple_zero_coefficient.py`; they are not a substitute for its all-m proof.

Formalization would require compact nonvanishing persistence, disjoint isolating discs and local zero counts, the finite lower-height gap, uniformization of finitely many asymptotic bounds, and the finite maximum right-derivative rule. No global uniformity statement is an obligation claimed proved here.
