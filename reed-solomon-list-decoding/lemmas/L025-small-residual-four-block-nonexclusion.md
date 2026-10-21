# L025 — Fixed small-residual four-block inequalities do not exclude the extension

## Hypotheses

Use L022's exact rational pair values p_i, 0<=i<=68, with p_0=1,
p_1=...=p_4=0 and lambda=p_68>0, at n=1024,w=68,v=956,d=10.
Use L023's unchanged assignment on every actual ordered orbit (i,j,t,s):

\[
\max(0,i+j-68)\le t\le\min(i,j),\qquad
\max(0,i+j-956)\le s\le\min(i,j),\qquad h=i+j-t-s.
\]

First set y=0 if any of i,j,h is in {1,2,3,4}; otherwise set y=p_b
if the sorted distance multiset is (0,b,b); otherwise set
y=p_i p_j p_h/lambda. No feasibility or realization is assumed.
Different original t-s variables remain distinct.

The four (weight,length) pairs are (t,i),(j-t,68-i),(s,i),(j-s,956-i).
Complement each block independently, replacing b by u=min(b,n_a-b),
and select exactly the orbits with S=sum u<=10. Define R by the fixed
recursion: remove zero-weight blocks; use 1 at S<5; at S=5 use
min floor(n_a/u_a) over positive blocks; at S>5 use

\[
R=\min_{a:u_a>0}\left\lfloor\frac{n_a}{u_a}R(\mathrm{child}_a)\right\rfloor.
\]

The child replaces (u_a,n_a) by (u_a-1,n_a-1), then complements and
removes zero weights again. The empty block tuple has R=1.

## Conclusion

Every one of the 12768 selected original ordered orbits satisfies

\[
R p_i-D y_{ij}^{ts}\ge0,\qquad
D=\binom it\binom{68-i}{j-t}\binom is\binom{956-i}{j-s}>0.
\]

There are 12386 strictly positive slacks and 382 zero slacks, with global
minimum zero at (0,0,0,0). The objective remains L022's
M=(U+1)/2, U=binomial(1024,64)/binomial(68,64), with
1.383<M/T<1.384 and floor(M)>T, T=65537^28/2^128.

These are **weakened** Theorem 12 constraints using certified upper
coefficients R. Their complete pass parks only this fixed diagnostic.
It does not establish the selected inequalities with exact four-block
maxima, omitted rows, any new PSD block, full-SDP feasibility, packing
or RS-list realization, or safety/unsafety at 67 or 68 agreements.
The uniform 955<=t_star(m)<=957 bracket is unchanged.

## Proof

**Imported inequality.** Hyun Kwang Kim and Phan Thanh Toan,
[Improved Semidefinite Programming Bound on Sizes of Codes](https://arxiv.org/pdf/1212.3467v1),
arXiv:1212.3467v1, 14 December 2012, III.C.1, Theorem 12 (36),
printed pp. 9–10, gives D*y<=K*p_i, where K is the maximum size of a
binary distance-at-least-10 code with these four block weights and
lengths. Both orbit multinomials must be nonzero. The proof (37)–(39)
counts eligible third words for each ordered pair and includes repeated
words. L022's support application meets the binary constant-weight
hypotheses: selected 68-agreement supports have distance at least 10
for whole tuples, uniformly in m. Use foundations/04's normalization.
Since p_i>=0, substituting an upper bound R>=K yields a weaker necessary
row. No division by p_i is needed.

The appendix, printed pp. 18–19, Proposition 22(ii),(iii),(v),(vi) and
Proposition 25 (99), supplies the reduction and upper-bound rules used
here, but omits their proofs. The following implementation justification
does not claim a new coding bound or reprove Theorem 12.

**Recursion justification.** Complementing a fixed coordinate block is
a Hamming isometry. Deleting a zero-weight block is injective and leaves
every pair distance unchanged. Valid weights admit a word; removing all
blocks leaves exactly the empty word. At total weight S<5, any two words
have distance at most 2S<10, so the maximum is 1. At S=5, the distance
is 10 minus twice the common-support size; distinct words therefore
have disjoint supports in every block. A positive block allows at most
floor(n_a/u_a) words. Their minimum is attained by choosing that many
disjoint u_a-subsets in each block and combining equally indexed subsets.
Zero weights are removed before taking this minimum.

For S>5, let a code have M words and fix a positive block (u,n).
Its M*u incidences of ones are distributed among n positions. For each
position the subcode with a one there shortens injectively to the child
(u-1,n-1), with distance unchanged because the deleted coordinate was
equal in all its words. Its size is at most K(child). Summing over all
positions gives M*u<=n*K(child). Inductive R(child)>=K(child) and
integrality yield M<=floor(n*R(child)/u). Taking the minimum over every
positive block remains valid. Normalization gives 2u<=n and hence
2(u-1)<=n-1; the child loses exactly one total-weight unit, including
deletion at weight zero. Induction terminates; S<=10 has at most five
shortening levels before S=5. No packing table or exactness assertion
for R above S=5 is used, and every branch participates.

**Complete finite certificate.** `scripts/finite-support/four_block.py`
reconstructs L022's pair values from its formula and L021's saved witness.
It enumerates all 1500625 actual ordered orbits and retains precisely the
selected ones. `scripts/finite-support/four-block-results.json` stores
every selected original orbit, h, t-s, block lengths, original and
complemented weights, recursion record, R, D, assignment branch, value
and slack. It stores all 160731 recursive states and all 394494 shortening
branches, including branches not attaining the minimum. The recursive
cache does not identify any distinct original orbit variables.

For exact denominator clearing let a>0 clear all p_i and put A_i=a*p_i,
H=a^2*A_68>0 and P_i=A_i*a*A_68. Then P_i/H=p_i. On permitted
distinct-word orbits Y=A_i*A_j*A_h satisfies Y/H=y; forbidden orbits
have Y=0 and repeated-word orbits have Y=P_b. The stored slack numerator
is R*P_i-D*Y over H, valid even when p_i=0. Branch order is preserved.

**Independent audit.** `scripts/finite-support/audit_four_block.py`
imports no generator routine. It rebuilds pair binomials from factorials,
checks all 64 defining equations of the saved L021 witness by polynomial
convolution, and compares every pair value with L022 and L023. The
equation check is extra consistency evidence; L022 supplies the fixed
pair input. It regenerates admissibility through nonnegative multinomial
parts rather than trusting the generator's ranges, and independently
rechecks complementation and the cap. Every selected original row, and
no extra row, is present; all stored original indices and weights agree.

The source coefficient is independently reconstructed as

\[
D=\frac{
 \operatorname{multinomial}(68;i-t,j-t,t,68-i-j+t)
 \operatorname{multinomial}(956;i-s,j-s,s,956-i-j+s)}
 {\binom{68}i\binom{956}i}.
\]

Cancellation gives exactly the four-binomial D above. Every value is a
positive integer. This verifies the source normalization independently
of the generator's four-binomial product.

The audit reconstructs R in increasing total-weight order using rational
floor arithmetic. It checks both base cases, all actual child states,
strict weight descent, every branch coefficient and the minimum at every
state. Reachability from the selected rows verifies the exact recursive
closure with no missing or extra state. Maximum shortening depth is 5.
For every original row it independently computes the prescribed y and
checks the rational identity R*p_i-D*y against the saved numerator over
H, together with its sign. Every selected value also agrees with its
original L023 scalar record; all 7093 old L022 orbit-class values are
independently rechecked. No sampling, approximate arithmetic, replacement
of original t-s, or reliance on the minimum alone certifies these rows.

The independent counts are:

| Quantity | Count |
|---|---:|
| All actual ordered orbits | 1500625 |
| Selected rows | 12768 |
| Forbidden-first / repeated-second / product-third branches | 6964 / 130 / 5674 |
| Selected rows with a zero-length region | 48 |
| Selected rows with p_i=0 | 253 |
| Selected old L022 closure overlaps | 1054 |
| Selected L023 scalar overlaps | 12768 |
| Positive / zero / negative slacks | 12386 / 382 / 0 |

The three assignment branch counts are disjoint because forbidden-first
takes precedence; they do not exclude repeated words within that branch.
At residual weights 0 through 10, counts respectively are
138,6,548,30,1222,84,2152,180,3330,330,4748.
The complete audit in `scripts/finite-support/four-block-audit-results.json`
reports no failures or negative rows. It recomputes the objective, its
equality to L022's (U+1)/2, the ratio interval and the positive scaled
integer-floor excess. These complete rational checks establish the
conclusion. A pass with R does not certify a row with the possibly
smaller exact K, nor any omitted constraint or actual code/list.

Reproduce from the notebook with
`python3 scripts/finite-support/four_block.py`, then
`python3 scripts/finite-support/audit_four_block.py`.
Both print counts, exact minimum, violations, actual/required bounds and
certificate paths. The prior SPECIALIZE assessment is
`drafts/literature/2026-10-06-four-block-small-residual-test.md`.
This is REPRODUCTION of known constraints and a local informative negative
diagnostic, without a claim of mathematical novelty.

## Mathlib

Full matching Theorem 12, its multiply constant-weight recursion, and this
exact finite certificate: **not checked** in Mathlib. The coding inequality
is imported by the precise primary citation above. The appendix's omitted
elementary proofs are justified for implementation; no assumed library
result or numerical evidence fills a gap.
