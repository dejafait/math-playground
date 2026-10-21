# Lemma 373: weak discriminant control permits an unbounded multiplicity deficit even with simple zeros

## Hypotheses

For real analytic functions F,G on an open neighborhood of an eventual
ray [H,infinity), use ordinary real derivatives and define

\[
 \mathscr L(u)=u'^2-uu'',\qquad
 B=2F'G'-FG''-F''G,\qquad
 D=B^2-4\mathscr L(F)\mathscr L(G).
\]

Both functions are required to be nonzero as analytic functions, but
common zeros are allowed. Write N_F^mult([H,X]) for the number of real
zeros of F with full analytic multiplicity, including both endpoints,
and N_G([H,X]) for the number of distinct real zeros of G, also including
both endpoints. The proposed implication assumes D≤0 and
\(\mathscr L(G)>0\) at every point of the ray and asks for a finite C,
allowed to depend on F,G,H but not X, such that
N_F^mult([H,X])≥N_G([H,X])−C for every X≥H.

## Conclusion

The real entire pair

\[
 F(t)=\sin t,\qquad G(t)=\sin(2t)                         \tag{1}
\]

refutes that implication on every eventual ray. In fact, all real zeros
of both functions are simple, and on the whole real axis

\[
 \mathscr L(F)=1,\qquad \mathscr L(G)=4,\qquad
 D=4\sin^4t\,(\cos^2t-4)\le0.                          \tag{2}
\]

For every fixed real H, put h=H/π. For all sufficiently large positive
integers n, the exact deficit on the closed interval [H,nπ] is

\[
 N_G([H,n\pi])-N_F^{\rm mult}([H,n\pi])
   =n+\lceil h\rceil-\lceil2h\rceil\longrightarrow+\infty. \tag{3}
\]

Thus counting multiplicities, or additionally requiring simplicity of F,
does not repair the generic implication. The pair has common zeros;
this result does not address an implication that excludes them. It is
not the actual F_0,G pair, not an actual-theta sign result, and not a
counterexample to RH.

## Proof

The prior EXPLORE assessment is
`drafts/literature/2026-10-06-multiplicity-count-implication.md`.
This is POTENTIALLY_NEW in that assessment's process sense only: no
covering theorem was found, and no historical originality is claimed.
L371 already refutes the distinct-count version using double F zeros;
its example does not give an unbounded multiplicity deficit. The pair
here supplies that different obstruction and also has simple F zeros.

The compared Sturm separation theorem, MIT 18.034 Spring 2009,
[Lecture 9, Theorem 9.1, printed pp. 1–2](https://ocw.mit.edu/courses/18-034-honors-differential-equations-spring-2009/0cdeb657491010f0f8c60aa49f2d5248_MIT18_034s09_lec09.pdf),
requires independent solutions of one regular second-order homogeneous
equation. That is not a premise of the proposed implication. This is
a source comparison, not an imported theorem in this proof. Direct
verification is necessary to decide the weaker arbitrary-pair target.

Set s=sin t and c=cos t. All physical jets in (1) are

\[
 F=s,\quad F'=c,\quad F''=-s,\qquad
 G=2sc,\quad G'=2(c^2-s^2),\quad G''=-8sc.
\]

Thus \(\mathscr L(F)=c^2+s^2=1\), and directly from G=sin(2t),
\(\mathscr L(G)=4\cos^2(2t)+4\sin^2(2t)=4\). Moreover

\[
 \begin{aligned}
 B&=4c(c^2-s^2)+8s^2c+2s^2c\\
  &=4c^3+6s^2c=2c(3-c^2).
 \end{aligned}
\]

Writing x=c² gives the exact polynomial factorization

\[
 \begin{aligned}
 D&=4c^2(3-c^2)^2-16\\
  &=4(x^3-6x^2+9x-4)\\
  &=4(x-1)^2(x-4)=4s^4(c^2-4).
 \end{aligned}
\]

Since 0≤c²≤1, the final factor c²−4 is at most −3. Consequently
D≤0 everywhere, with equality exactly when s=0. No division by
F,G or a Wronskian, and no differentiation of a normalized envelope,
is involved.

For completeness, the Wronskian of this pair is

\[
 W=FG'-F'G=2s(c^2-s^2)-2sc^2=-2s^3.
\]

It vanishes at every common zero; a separation proof requiring its
nonvanishing therefore cannot apply. At t=kπ the full jets are

\[
 (F,F',F'',G,G',G'')=(0,(-1)^k,0,0,2,0).
\]

In particular both zeros are simple, L(F)=1, L(G)=4, B=4(−1)^k
and D=0 there. The weak inequality is satisfied at these points with
the strict response inequality intact. At the other G zeros,
t=(k+1/2)π, one has F=(−1)^k, F'=0, G'=−2 and B=0, so
D=−16. The global factorization already covers these points and all
remaining points; they require no omitted limiting case.

The complete real zero sets are

\[
 \{t:F(t)=0\}=\{k\pi:k\in\mathbb Z\},\qquad
 \{t:G(t)=0\}=\{k\pi/2:k\in\mathbb Z\}.
\]

The corresponding derivatives are (−1)^k and 2(−1)^k, respectively,
and are nonzero. Hence every listed zero has analytic multiplicity
one and the lists exhaust the real zeros. This also verifies that F,G
are nonzero real analytic functions on a neighborhood of every ray.

Fix any H∈R. For every integer n large enough that both ranges below
are nonempty, the F indices in [H,nπ] run from ceil(h) through n,
and the G indices from ceil(2h) through 2n. Therefore

\[
 N_F^{\rm mult}([H,n\pi])=n-\lceil h\rceil+1,\qquad
 N_G([H,n\pi])=2n-\lceil2h\rceil+1.
\]

Ceilings include a zero at H whenever H lies in the corresponding zero
set. The upper endpoint nπ is common and is counted once in each
count. This proves (3), including negative H and arbitrary fractional
endpoints. The two ceiling terms are fixed finite integers. Thus, for
any proposed finite C, taking n large enough makes the deficit exceed
C at X=nπ≥H. Since H was arbitrary, increasing the onset finitely
cannot repair the bound. ∎

**Qualification and verification.** The proof consists of exact
trigonometric algebra and complete zero lists; no numerical evidence or
mathematical script is needed. It stops only the stated generic count
implication. In particular it supplies no bound for the actual-family
discriminant, no signed arithmetic comparison, and no new zero-exclusion
range. The separate critical audit below retains this conclusion; this
is not a complete RH argument or a claim of progress beyond the checked
literature.

**Critical audit, 2026-10-07.** Under the prior EXPLORE assessment
`drafts/literature/2026-10-07-multiplicity-counterexample-audit.md`,
all six ordinary jets, both Laguerre forms and the mixed coefficient
were independently recalculated. As a second expansion, with y=sin²t,
B²=4(1−y)(2+y)²=16−12y²−4y³, so
D=−4sin⁴t(3+sin²t). This agrees with (2), is strictly negative off
πZ, and is zero exactly at the common zeros. The explicit common-zero
jets above give nonzero first derivatives for both functions; the
remaining G zeros give D=−16. Thus neither the weak sign nor strict
L(G)>0 loses a degeneracy case. These are physical derivatives with no
envelope or quotient assumption; L370's convention agrees but its
actual-family estimates are not inputs.

The zero lists and their nonzero first derivatives independently verify
full analytic multiplicity one. For arbitrary fixed real H and any
finite real C, choose a positive integer
n>max{H/π, C−ceil(H/π)+ceil(2H/π)}. Both displayed index ranges are
then nonempty, X=nπ≥H, and (3) exceeds C. This checks the precise
quantifiers, including negative H, a zero at either endpoint, and every
finite onset change. The proof needs only this unbounded sequence of
upper endpoints to refute a bound asserted for all X≥H.

No error or new mathematical result was found. The audit is REPRODUCTION
of the saved obstruction, not another counterexample or a claim of
originality. L371 is comparison context only. Common-zero exclusion,
the actual-family discriminant premise, and any actual-family count
comparison remain outside this audited statement. No dependency is
added to the independent DAG node.

## Mathlib

Full matching counterexample: **not checked**. Elementary trigonometric
differentiation and zero-set facts support the manual proof, but no
Mathlib theorem has been imported or claimed to match this statement.
Unknown coverage is not evidence of absence.
