# Residual Atiyah normal-rank calculation — step 590

Invocation-start coverage is the unchanged SPECIALIZE assessment
`literature/2026-10-27-residual-atiyah-normal-rank-constraint.md`.
The main gap is uniform primitive realization; F is still hypothetical.
The approved intermediate target is placement of the actual residual
Atiyah map and comparison of its normal rank with 704-s+2t.

The specific new input relative to ATTEMPTS/068 is L175's audited
rank-one point projection, used together with L174's audited rank-15
Gram form. ATTEMPTS/092–095 remain parked under their recorded tests.
The bounded continuation test is a nonzero normal-rank constraint;
claims needing a point norm, metric compatibility or actual bracket
evaluation must stop at the missing datum. No script is needed.

## Saved calculation before canonical write-up

Put f=mathfrak a_perp, T=(A|ker R)^(-1), and K_N=H^1(B,N).
The actual adjoint identity Q(x,iv)=S(Rx,v), orthogonality of
f to iI(K_T), and the nondegenerate orthogonal tangent/normal
splitting imply Rf lands in K_N. Hence f=i(Rf)+T(Af), an actual
Q-orthogonal decomposition, not a new Leray splitting.

Let ell(u)=q(phi(u),k). For nonempty Z, Af=-2pi i ell w_k.
Consequently its point Gram form is c ell tensor ell, where
c=(-2pi i)^2 Q_U(w_k,w_k) is unknown and may be zero.
The normal pulled-back form is G-c ell tensor ell, with rank(G)=15.
Imported sum/composition rank inequalities give normal Gram rank
at least 14 and actual normal-map rank at least that rank. For
empty Z its Gram rank is exactly 15. No equality with map rank
is justified, and no point self-pairing has been evaluated.

The completed canonical write-up in L176 verifies 704-s+2t>=14 uniformly,
s<=690+2t. L116's t<=48, t!=47 and t=48 => (s,h^1(N))=(800,0)
eliminates t=48 and yields t<=46 and s<=782. This is a conditional
cardinality restriction, not nonexistence of F. These implications
are now recorded in the canonical proof; a separate critical audit
is nominated rather than computing sharper unevaluated data.
