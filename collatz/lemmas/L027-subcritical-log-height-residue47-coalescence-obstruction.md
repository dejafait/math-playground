# L027 — Subcritical logarithmic height clocks fail on residue 47

## Hypotheses

For positive integers use T(n)=n/2 when n is even and
T(n)=(3n+1)/2 when n is odd. Let S be the positive integers congruent
to 20 modulo 27. Logarithms are natural. Fix real numbers

\[
0<C<1/\log(12),\qquad B\ge0.
\]

No convergence, least-root or companion assumption is imposed.
Both clocks count shortcut steps and include zero.

## Conclusion

There are unbounded odd positive integers n=47+243k, k>=0, with
v_2(n+1)=4, for which no c in S and integers s,t satisfy

\[
0<c<n,\qquad 0\le s,t\le C\log(n)+B,\qquad
T^s(c)=T^t(n).                                           \tag{1}
\]

More explicitly, put delta=1-C log(12)>0 and

\[
L_0=\max\left(6,\left\lceil
\frac{C\log(4)+B}{\delta}\right\rceil\right).
\]

For every integer L>=L_0 one can select such a root n_L with

\[
12^L<n_L\le12^L+162\cdot6^L<4\cdot12^L.                 \tag{2}
\]

Consequently a cover using (1)'s two clocks cannot hold outside any
finite base on this cylinder with these fixed C,B. This does not
exclude the endpoint coefficient 1/log(12), larger coefficients,
other clocks or convergence of the selected roots.

## Proof

### Assessed inputs and the quantitative difference

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-05-residue47-log-height-coalescence.md`.
Use audited L026 exactly as stated: for integer L>=6, its positive
roots satisfying

\[
n\equiv47\pmod{3^{L+4}},\qquad
81n+97\equiv0\pmod{2^{L+1}},\qquad n>12^L               \tag{3}
\]

have valuation 4 and admit no smaller positive residue-20 companion
with either clock at most L. Its conclusion concerns actual paths,
not merely formal parity words. Its proof already treats equality
and both zero clocks. L025 and Rozier's finite parity coding enter
only through that input and are not reproved here.

The other input is the standard named Chinese Remainder Theorem:
one prescribed class for each of two coprime positive integer moduli
gives one class modulo their product. L026 alone gave unbounded
roots at separately fixed horizons; that would not bound a clock
growing with n. The present difference is the controlled selection
(2) and the real-parameter horizon comparison below. This is a local
quantitative specialization of the assessed machinery, with no claim
of certified originality or a new external coalescence theorem.

### Selecting a root without excessive height

Fix an integer L>=6. Since gcd(81,2^(L+1))=1, the second congruence
in (3) specifies one binary residue class. The binary and ternary
moduli are coprime. CRT therefore gives one simultaneous class
modulo

\[
M_L=2^{L+1}3^{L+4}=162\cdot6^L.
\]

Take its representative r_L with 0<=r_L<M_L and put H_L=12^L.
Define the integer

\[
q_L=\left\lfloor\frac{H_L-r_L}{M_L}\right\rfloor+1,
\qquad n_L=r_L+M_L q_L.
\]

The floor inequalities give
q_L>(H_L-r_L)/M_L and q_L<=(H_L-r_L)/M_L+1. Hence

\[
H_L<n_L\le H_L+M_L.                                    \tag{4}
\]

Thus n_L is positive, satisfies both congruences, and satisfies the
strict size guard in (3). This explicit representative selection
uses no assumption about a least positive CRT root. Moreover,

\[
\frac{M_L}{H_L}=\frac{162}{2^L}\le\frac{81}{32},
\qquad
H_L+M_L\le\frac{113}{32}H_L<4H_L.                       \tag{5}
\]

This proves (2) for all L>=6. In particular n_L>12^6>47. Its
ternary congruence implies n_L=47 modulo 243, so n_L=47+243k
for an integer k>=0. L026 supplies oddness, v_2(n_L+1)=4 and
the actual input prefix O^4 E O^(L-5). Finally n_L>12^L implies
that these selected roots are unbounded as L tends to infinity.

### Comparing the full height clock with the integer horizon

Now fix C,B as in the hypotheses and let L>=L_0 be an integer.
The strict upper bound in (2), monotonicity of the natural logarithm,
and C>0 give

\[
\begin{aligned}
C\log(n_L)+B
&<C L\log(12)+C\log(4)+B\\
&=L-\delta L+C\log(4)+B\\
&\le L.
\end{aligned}                                           \tag{6}
\]

The final inequality follows from delta L>=C log(4)+B, by the
definition of L_0. Every nonnegative integer s,t allowed in (1)
is therefore at most L; no rounding convention can enlarge the
allowed set beyond L. Applying L026 at n_L excludes (1), with
the same strict comparison c<n_L and actual parities on both paths.
Zero clocks remain included. This applies separately to each n_L
and to every companion and path selected for that root.

For any finite base, the unbounded roots eventually lie outside it.
The claim therefore obstructs the stated cover. The roots vary with
L; no single infinite nonconvergent orbit is constructed. At the
endpoint coefficient delta=0, the preceding horizon comparison
does not apply. No endpoint or larger-coefficient assertion follows,
and universal eventual descent remains unproved.

### Independent critical audit, 2026-10-05

The audit checked the entire argument against L026's integer-horizon
statement and its already audited proof. No defect was found. L026 is
the only direct local mathematical input; its auxiliary finite checks
are not needed again for this representative-selection application.
CRT is used in its named standard form, not reproved.

For every integer L>=6, both moduli are positive and coprime, and 81
is a unit modulo the binary modulus. Thus r_L exists in the stated
half-open interval. For x=(H_L-r_L)/M_L the inequalities
x<floor(x)+1<=x+1 hold even when x is an integer or is negative.
Consequently the construction selects a root strictly above H_L,
including the case H_L itself belongs to the CRT class. Adding M_L q_L
preserves both congruences. The product constant is exactly
2*3^4=162; its ratio to H_L is 162/2^L, whose maximum for L>=6
is 81/32. Hence 1+81/32=113/32<4 gives the claimed strict upper
bound without a large-L exception. Positivity and n_L>47 give k>=0;
the ternary modulus is divisible by 243. All hypotheses of L026 hold,
so oddness, valuation 4, and the actual-path exclusion apply to these
particular roots, not merely to unspecified members of the CRT class.

For each fixed pair of finite real numbers C,B in the stated domain,
delta>0 and L_0 is a finite integer. The ceiling gives
delta L>=C log(4)+B for every integer L>=L_0. Strict monotonicity of
logarithm and C>0 preserve the strict first inequality in (6), even
when the ceiling argument is already an integer or B=0. Thus the
allowed real clock is strictly below L, which certainly places every
allowed nonnegative integer s,t within L026's inclusive horizon.
There is no independent parity or path choice to assume: L026 excludes
all companions and both actual paths for each such root, retaining
strict order against n_L and both zero clocks.

Finally n_L>12^L implies n_L tends to infinity; monotonicity or
distinctness at consecutive L is unnecessary. Given any finite base,
all sufficiently large selected roots exceed its maximum. The order
of quantifiers is fixed C,B, then every integer L>=L_0, then a root
n_L excluding every eligible c,s,t. No root is fixed while L tends
to infinity, and no bound uniform as C approaches 1/log(12) is claimed.
At equality delta=0, this proof gives no conclusion. The audit confirms
the existing subcritical obstruction only; it supplies no stronger
coefficient, new theorem, Collatz counterexample or complete candidate.

## Mathlib

Full logarithmic-clock residue-20 coalescence obstruction: **not
checked**. Supporting CRT, logarithmic inequalities and floor/ceiling
facts: **not checked**. Named CRT and the explicit elementary estimates
are the standard inputs; L026 is an informal local input. No Lean
verification or numerical proof is claimed. Unknown coverage does
not assert absence.
