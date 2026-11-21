# Exact projection weighting — step446 working record

Approved target: the fixed (r,R)=(3,2048) diagonal-similarity calculation,
including convergence and the repeated-evaluation diagonal limit. Reuse
the invocation-start SPECIALIZE assessment
`literature/2026-11-04-exact-projection-similarity-review.md`.

The main gap is actual-Xi all-degree mixed positivity. A paid identity
would let a later signed-inertia argument concern the actual Fredholm
determinant; no inertia bound or half-plane membership is attempted here.
Continue only if every index, residue and node factor fits an invertible
real diagonal similarity; otherwise preserve the mismatch and stop this
formula. No parameter sweep or additional Taylor-index test.

Inputs read: L777 exact b=p/F, U and Y, row start i=r+1, and Laurent
bound; L779 fixed-pair grouping/residues and finite-rank determinant
conventions; L780 balancing/negative-block consistency constraint.
Step443's proposed h_r,K,E,Q,J and step444's closed nondiscriminating
test were checked. No matching earlier exact weighting proof was found
in the targeted L777–L781/working-note search. This is no novelty claim.

Preserved derivation, pending canonical write-up: with row l=r+1+a
and inner column h=1+b, the coefficient is beta_(r+1+a+b), hence
S_ij=alpha_i^r sum_(a,b>=0) beta_(r+1+a+b) alpha_i^a alpha_j^b.
The inner double sum is K_ij for the proposed h_r. On |x|,|y|<=t<sigma,
its absolute majorant is M_b sigma^(-r-1)/(1-t/sigma)^2; the same
majorant permits regrouping and the analytic diagonal limit. Thus
S=diag(alpha_i^r)K. Since alpha_i<0 and d_i!=0,
C S=(-1)^r J E^2 K, so E^-1(I-C S)E=I-JQ. At r=3 the common
sign is negative; E is positive and invertible. No arithmetic certificate
is needed for this exact series calculation. Existing input software
and analytic qualifications are retained; full matching Mathlib unchecked.

Completed: the full proof and precise citations are canonical in
`../lemmas/L782-exact-fixed-pair-projection-weighting.md`. All projection
factors fit; no mismatch was found. The next action is an independent
critical replay of the same preapproved calculation, using L782 as the
proposed proof, not a new inertia calculation. No new assessment or
source scope is nominated.
