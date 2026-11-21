# Corollary C030b: finite mixed positivity from the source heat blocks

## Hypotheses

Use the actual Xi zeros and the multiplicity convention of C030a. Thus
one alpha_j is chosen from each negation pair, counted with its zero
multiplicity, and

\[
 \lambda_j=\alpha_j^2,\qquad \beta_j=\lambda_j^{-1},\qquad
 S_m=\sum_j\beta_j^m,\qquad
 \mathcal H(t)=\sum_j e^{-\lambda_jt}.
\]

For a real polynomial q(X)=sum_(r=0)^d c_r X^r, use L030's
absolutely convergent algebraic-square form

\[
 Q(q)=\sum_j\beta_j^2q(\beta_j)^2
     =\sum_{r,s=0}^d c_rc_s S_{r+s+2},\qquad
 H_d=[S_{r+s+2}]_{0\le r,s\le d}.
\]

Import the precise external results cited in the proof. In particular,
Polson's v24 finite-block theorem is a preprint theorem input, and
Platt–Trudgian's zero verification is an external rigorous verification.
Neither source proof nor its numerical/analytic estimates is independently
reaudited here. This is a specialization of these inputs through the
separately audited C030a, not an independent proof of the source signs.

## Conclusion

For every integer 0<=d<=29999999, H_d is positive definite. Hence
Q(q)>0 for every nonzero real polynomial of degree at most 29999999;
Q(0)=0. This is a finite actual-Xi result relative to the cited inputs.

The conditional height version is as follows. For an arbitrary integer
d>=0, put N=d+1 and

\[
 T_N=20000N\sqrt{1+\log N}.
\]

If all nontrivial zeros rho with 0<Im(rho)<=T_N lie on the critical
line, then H_d>0 and Q(q)>0 for every nonzero real q of degree at most
d. When d=2 (N=3), the source also permits verification through height
10000 instead. These are sufficient height conditions, not optimized
ones. No simplicity assumption is made.

The largest derivative order needed at the finite cap is 59999998;
the largest moment index in its conclusion is 60000000. No assertion
for arbitrary degrees, no semidefinite variant of C030a and no actual
common-graph realization is established.

## Proof

Nicholas G. Polson, *On Hilbert's 8th Problem*,
[arXiv:1708.02653v24, 11 September 2026](https://arxiv.org/pdf/1708.02653v24),
Section 3, equation (2), printed p6, specifies one squared exponent
per pair {rho,1-rho}, counted with multiplicity; Definition 5.1,
printed p8, defines the resulting trace W. Section 7.1, printed p16,
uses c_j(t)=(-1)^j W^(j)(t); Section 7.3, printed p18, defines

\[
 H_N^\epsilon(t)=[c_{r+s+\epsilon}(t)]_{0\le r,s<N}.
\]

Theorem 7.4 and Corollary 7.5, printed p18, give the following source
inputs: verification through T_N implies H_N^0(t)>0 and H_N^1(t)>0
for every t>0; N=3 separately permits height10000; and both strict
blocks hold for every 1<=N<=30000000 using the cited verification.
The proof joins the near-zero and far-time ranges on printed p22,
using Lemmas 7.6–7.9 on pp19–21. The source assertion includes every
positive time and N=1. We invoke that assertion, not only individual
derivative signs or a block at a selected time.

C030a equation (6) gives the exact identity

\[
 W(t)=\mathcal H(t)=\sum_{\Im\rho>0}e^{(\rho-1/2)^2t}
                 =\tfrac12\sum_\rho e^{(\rho-1/2)^2t}.
\]

Indeed alpha=gamma-i(b-1/2) for rho=b+i gamma, so
lambda=-(rho-1/2)^2. Squaring removes the choice of sign in a
negation pair. A critical-line pair contributes one real squared
node, and an off-line quartet contributes two conjugate squared
nodes; all contributions retain their original multiplicities.
No unverified node has been assumed real and no factor two remains.
The locally uniform derivative convergence already proved in C030a
then identifies the source block exactly as

\[
 H_N^0(t)=
 [(-1)^{r+s}\mathcal H^{(r+s)}(t)]_{0\le r,s<N}=B_N(t).
\]

For the conditional statement, apply Theorem 7.4 under its stated
height hypothesis with N=d+1. It supplies B_(d+1)(t)>0 for every
t>0, precisely C030a's hypothesis (P). C030a therefore gives H_d>0.
The same argument uses the source's separate N=3 clause when d=2.
The shifted block H_N^1 is additional source information and is not
needed here. Neither t=0 nor t=infinity is a matrix argument.

For the finite assertion, Corollary 7.5 supplies that same premise
for every integer 1<=N<=30000000. Its verification comparison is
T_30000000<2.6e12<3e12. The rigorous verification used here is Dave
Platt and Tim Trudgian, *The Riemann hypothesis is true up to
3\cdot10^12*, [arXiv:2004.09765v1, 21 April 2020](https://arxiv.org/pdf/2004.09765v1),
Theorem 1 and Section 2, printed p2; published in *Bulletin of the
London Mathematical Society* **53** (2021), 792–797,
[doi:10.1112/blms.12460](https://doi.org/10.1112/blms.12460).
Their theorem verifies all zeros through height3000175332800,
which exceeds 3e12. Section 2 describes interval arithmetic and a
Turing-method count of all zeros; a finite table of selected zeros
is not being substituted for this theorem. The source corollary's
bound and its analytic estimates are imported, not recomputed here.

The integer correspondence 1<=N<=30000000 with N=d+1 is exactly
0<=d<=29999999. Applying C030a separately at each such d proves
H_d>0. Its signed-derivative block uses orders through 2(N-1)=2d;
the mixed matrix uses S_(r+s+2), hence indices through 2d+2. At the
cap these are respectively 59999998 and 60000000.

Finally L030 identifies c^T H_d c with Q(q), with no conjugation.
A nonzero q has a nonzero real coefficient vector, so H_d>0 proves
the strict conclusion. In degree one the expression remains

\[
 c_0^2S_2+2c_0c_1S_3+c_1^2S_4.
\]

Thus neither a factorial normalization nor a modulus-square replacement
has changed the observable. The zero polynomial gives zero directly.
The existing small-degree results L033/L038/L041 are duplicate
contrasts, not ingredients or new claims of this application.

This supplies a finite portion of L030-L032/C032a's mixed-form gap.
The quantified premise needed for every degree is still missing:
one cannot pass from the fixed cap above to all d. Common-graph
realization is also independent. The local advance is the explicit
citation-based application; no result beyond the checked sources
or complete candidate proof of RH is claimed.

### Finite application audit — 16 November 2026, step1116

The application passes the separate audit approved by coverage1114
and approval1115, relative to the stated external theorem inputs.
This secures the written specialization; it does not independently
certify Polson's analytic estimates or the Platt–Trudgian computation.

- Directly checked Polson Section 3 equation (2), Definition 5.1,
  Section 7.1, Section 7.3 and Theorem 7.4/Corollary 7.5, plus the
  joining proof on printed p22. The block definition is in Section
  7.3, not Section 7.1; the citation above is corrected. The complete
  supporting proof-case coverage recorded in comparison1108 is reused.
- The map rho=1/2+i alpha sends {alpha,-alpha} to {rho,1-rho}.
  Each pair has the same multiplicity on both sides, and its exponent
  is -alpha^2. Thus the source and local traces coincide term by term.
  An off-line quartet still gives two conjugate nodes, rather than
  one real node. C030a's audited derivative convergence identifies
  every entry of H_N^0 with B_N, with no factorial or factor two.
- Theorem 7.4 supplies strict full-block positivity at every t>0,
  exactly hypothesis (P); the joining proof covers both positive-time
  ranges, including N=1 and the exceptional N=3 clause. No endpoint
  matrix, shifted block, simplicity assumption or signs-only premise
  is introduced. Platt–Trudgian Theorem 1 and Section 2 cover all
  zeros through the stated height, not only a selected list.
- With N=d+1, the source interval of integers is precisely the stated
  degree range. At its endpoints d=0 and d=29999999, the needed block
  sizes are 1 and 30000000. The largest indices are 2d=59999998 and
  2d+2=60000000. The conditional T_N and d=2 height10000 clauses are
  unchanged source hypotheses. The finite height comparison is the
  one imported from Corollary 7.5, below the verification theorem's
  height; no large-matrix computation is claimed.
- L030's finite coefficient expansion is exactly c^T H_d c, including
  2c_0c_1 S_3. A nonzero real polynomial gives a nonzero vector; the
  source block premise and C030a therefore give precisely the strict
  finite conclusion. There is no limit in d, no degree-uniform bound
  establishing additional orders, and no common-graph consequence.

No mathematical conclusion is withdrawn. This is local verification
of a reproduction, not progress beyond the cited sources. The
all-degree sign gap and actual common-graph realization remain open.

## Mathlib

Not checked for the full finite mixed-positivity statement, the cited
source block theorem, or its zero-verification input. Availability is
unknown, not asserted absent. This informal specialization has not
been formalized. Reference:
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
