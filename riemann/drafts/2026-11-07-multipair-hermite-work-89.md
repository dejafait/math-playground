# Quantitative multipair certificate — working record, step89

Approved target: the exact TARGET of the 2026-11-07 quantitative multipair
Hermite assessment (SPECIALIZE before invocation). This is a calculation
specializing known interpolation and finite-form stability, not a new
actual-Xi positivity mechanism.

Main gap: L030-L032/C032a all-degree mixed positivity for actual Xi.
Bounded test: construct a common degree, an injective real interpolation
basis, a uniform negative margin on its whole span, and an explicit
tail/logarithmic-coefficient error budget. Stop if only separate negative
vectors or qualitative one-pair detection results.

Reasoning saved before the complete proof: use a finite head E containing
all nodes with modulus at least r, where 0<r<min |w_l|. Use L032's
q_(l,N) for every selected distinct conjugate pair. Its head evaluation
is i/w_l at w_l, -i/conj(w_l) at its conjugate and zero elsewhere, so the
head quadratic form in coordinates x is -2 sum mu_l x_l^2. A product
bound on the Lagrange polynomials supplies C_l with
|q_(l,N)(z)| <= C_l (r/|w_l|)^N on |z|<=r. Cauchy-Schwarz should bound
the entire compressed tail by T sum C_l^2 (r/|w_l|)^(2N) times ||x||^2.
Choose one explicit N using the largest ratio and the smallest
multiplicity. Track coefficient l1 norms separately to turn moment
errors into a whole-subspace bound. These are proposed calculations,
not yet a checked result in this working record.

Inputs checked narrowly: L030/L032 in full, L024/L025 for the separate
Xi interpretation, L034/L057 as safeguards, and step88's source history.
No new external source is needed; reuse the supplied finite Hermite and
min-max assessment. Finite signatures do not give the infinite-tail
constants automatically. Tail mass, exact head data and multiplicities
are conditional inputs; actual-Xi availability remains unpaid.

Completed calculation is now canonical in L895. The explicit degree
choice bounds the entire compressed tail by delta <= mu_*, leaving
gamma = 2 mu_* - delta >= mu_* on R^m. The coefficient l1 product bound
gives B^2 and moment-error norm <= epsilon B^2, hence the stated
logarithmic-coefficient tolerance. The proof checks T=0, nodes at radius
r in the head, multiplicities, injectivity, min-max dimension and the
power-sum shift two. No scripts or numerical previews were used. These
notes preserve the initial proposal; L895 is the sole full proof.
