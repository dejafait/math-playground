# Step 088 — common-locator attempt, saved reasoning

Completion note: the saved working claim below was proved in canonical
L042; full hypotheses, all five minor terms, citations and qualifications
are in `../lemmas/L042-nine-union-common-locator-nonpersistence.md`.
The initial checkpoint is retained as reasoning history. Separate
critical audit is pending; no global count improvement follows.

Approved target: Determine exactly when L041's tau=1 local converse has a persistent locator at its common coordinate, retaining arbitrary extension-field weights and original finite parameters.

Main gap: arbitrary sixteen-error equality, with global interval 11/q–16/q
and allowable fifteen. Inputs: L010's determinant definition/pointwise
identities and L041's gated local converse. Reuse the prior SPECIALIZE
assessment `literature/2026-10-08-nine-union-common-locator.md`; L016's
fixed-label count and L011's persistence assumption do not answer this
target. ATTEMPTS/008–009 stop different fixed-triple generators.

Working claim, pending full write-up: persistence never occurs. Rename
the common coordinate h and double-only coordinate d, so the first two
supports are {h,d,a,b} and {h,d,c,e}. Subtract h times each previous
column, working right to left in L(T,h). Expansion along the last row
gives the four-by-four Hankel determinant of r_j=s_(j+1)-h*s_j,
j=1,...,7. This is an exact determinant identity, not an identification
with an unproved reciprocal decoder convention.

Use z=(T-gamma_0)/(gamma_1-gamma_0) only as an invertible affine
polynomial substitution. The modified moments are represented on
W={d,a,b,c,e} with weights w_a,w_b=(1-z)u_a,(1-z)u_b,
w_c,w_e=z*v_c,z*v_e and w_d=(1-z)u_d+z*v_d, where
u_x=e_0(x)*x*(x-h), v_x=e_1(x)*x*(x-h); every present u,v is nonzero.
The four-by-four determinant is z(1-z) times
R(z)=A*z(1-z)+w_d(z)*(B*z+C*(1-z)). Cauchy–Binet defines A
as the nonzero squared Vandermonde on {a,b,c,e} times
u_a*u_b*v_c*v_e. B and C are the remaining explicit sums.
If R were identically zero, R(0)=u_d*C and R(1)=v_d*B force
C=B=0, leaving the nonzero polynomial A*z(1-z). Thus L(T,h)
cannot be zero. The two common-coordinate weights are annihilated by
the column transformation; the double-only weight gates retain u_d,v_d.

Continuation test: verify all five minor terms and the exact sign,
then prove the contradiction without dividing by a possibly zero B,C
or evaluating away an exceptional parameter. This answers only the
approved persistence gate. No completion, global extraction, count
improvement or rationality of the excluded direction is assumed.
