# Lemma 59: local splitting at a real double zero

**Hypotheses.** Let F(λ,z) be the exact heat-deformed theta transform of Lemma 58. Suppose λ₀,x₀ are real and

F(λ₀,x₀)=F_z(λ₀,x₀)=0,  A=F_zz(λ₀,x₀)≠0.

Put B=F_zzz(λ₀,x₀) and c=2B/(3A); these numbers are real.

**Conclusion.** There exist r,ε,C>0 and holomorphic functions w₊,w₋ on |s|<ε such that all zeros of F(λ₀+s²,z) in |z-x₀|<r, counted with multiplicity, are x₀+w₊(s) and x₀+w₋(s). They satisfy

w₊(s)=sqrt(2)s+cs²+R₊(s),
w₋(s)=-sqrt(2)s+cs²+R₋(s),

|R₊(s)|, |R₋(s)|≤C|s|³.

For 0<t<ε² the two zeros at λ=λ₀+t are distinct, simple, and real, with expansions x₀±sqrt(2t)+ct+O(t^(3/2)). For -ε²<t<0 they are distinct, simple, nonreal conjugates, with expansions x₀±i sqrt(2|t|)+ct+O(|t|^(3/2)). The constants and neighborhoods are local to the hypothetical double zero. This is a conditional statement; no such double zero of the exact family is asserted to exist.

## Proof

Lemma 58 supplies joint holomorphy, conjugation for real parameters, and F_λ=-F_zz. Differentiate the latter in z to get F_λz=-F_zzz. Taylor expansion at (λ₀,x₀), writing t=λ-λ₀ and w=z-x₀, therefore has the terms

F(λ₀+t,x₀+w)=A(w²/2-t)+B(w³/6-tw)+E(t,w),

where E is a convergent power series whose monomials t^j w^k all have 2j+k≥4. Indeed the constant and w terms vanish by hypothesis, and the four displayed monomials are all remaining monomials of weight below four. Absolute convergence holds on a sufficiently small complex polydisc.

For v in a bounded neighborhood of either sqrt(2) or -sqrt(2), substitute t=s² and w=sv. Dividing the resulting power series by s² gives a holomorphic function even at s=0:

G(s,v)=A(v²/2-1)+sB(v³/6-v)+s²H(s,v),

with H holomorphic locally. This follows term by term from the weights and normal convergence on smaller polydiscs; in particular it is a convergent analytic identity, not a formal asymptotic substitution.

At v₀=±sqrt(2), G(0,v₀)=0 and G_v(0,v₀)=Av₀≠0. The holomorphic implicit function theorem gives holomorphic v₊(s),v₋(s) near zero, taking these respective initial values. At either initial value,

v'(0)=-B(v₀³/6-v₀)/(Av₀)=2B/(3A)=c.

Set w₊(s)=sv₊(s), w₋(s)=sv₋(s). Their expansions are the stated ones. More precisely each (w₊(s)-sqrt(2)s-cs²)/s³ and (w₋(s)+sqrt(2)s-cs²)/s³ extends holomorphically across zero. On a closed disc strictly inside their domain these quotients are bounded; their maximum moduli give one finite C. Shrink ε to lie inside that disc. This proves the claimed uniform bound for complex s, and hence the precise order of the real-parameter remainders.

Choose r>0 so F(λ₀,z) has exactly its double zero x₀ in the closed disc |z-x₀|≤r and is nonzero on its boundary. Such a choice follows from A≠0 and the isolated-zero theorem. Its boundary modulus has a positive minimum. Uniform continuity in λ on that boundary makes |F(λ₀+s²,z)-F(λ₀,z)| smaller than this minimum for sufficiently small |s|. Rouché's theorem then counts exactly two zeros with multiplicity inside the disc. Shrinking ε again puts both constructed zeros inside. For s≠0 they are distinct since

w₊(s)-w₋(s)=2sqrt(2)s+O(s³).

Thus these are all the local zeros, each simple; at s=0 they represent the original zero twice.

For real s, the coefficients of G obey complex conjugation, and uniqueness of each implicit branch through the real initial values gives v₊(s),v₋(s) real. This proves the t>0 assertion by choosing s=sqrt(t).

For t<0 choose s=i sqrt(|t|). The displayed remainder bound gives imaginary parts ±sqrt(2|t|)+O(|t|^(3/2)), since ct is real. They are nonzero and opposite in sign after another uniform shrinking of ε. Conjugation preserves F(λ₀+t,z) and the disc; since it has exactly two zeros, the two nonreal zeros must be conjugates. Substitution yields the negative-t expansions. ∎

## Qualification: no global collision exclusion

In increasing λ, this local double collision resolves into real zeros. In decreasing λ, two real zeros collide and become nonreal. Consequently a downward continuation from a parameter with real zeros would require an additional argument to exclude collisions at positive λ before reaching zero. This lemma gives the direction of an assumed collision, not a restriction on where it occurs. It neither proves such collisions occur nor excludes them for the exact theta family. Higher multiplicities, continuation of infinitely many branches, and possible escape to infinity are also outside its statement. No global real-zero theorem or simplicity assertion about Ξ is used.

## Verification and formalization obligations

The proof uses only Lemma 58 and the standard holomorphic implicit function, isolated-zero, and Rouché theorems. The heat sign forces the leading polynomial A(v²/2-1), and substituting v₀²=2 in its first derivative gives c=2B/(3A); these algebraic checks fix both the direction and the drift coefficient. The analytic quotient bound proves a uniform O(|t|^(3/2)) remainder, with no numerical approximation required. Formalization would need the convergent two-variable Taylor rescaling and divisibility, the two implicit branches and their derivative, the bounded removable quotients, the uniform boundary perturbation and multiplicity count, and the conjugation and imaginary-part estimates.
