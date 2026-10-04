# C016a — Central vanishing removes the first prime-deletion lifting obstruction

## Hypotheses

Retain all hypotheses, coefficient-compatible arithmetic systems,
normalizations and fixed primes of L016. In particular E/Q is non-CM,
p >= 5 is good ordinary, the representation on E[p] is surjective,
p does not divide #E(F_p), the Manin constant or any Tamagawa factor,
and E(Q_p)[p] = 0. The distinct primes ell_1,ell_2 belong to P_(2,0),
and N = ell_1 ell_2 is delta-minimal modulo p. Its nonzero mod-p
Kurihara number is an additional premise, not a consequence of analytic
rank two. Assume also

\[
L(E,1)=0.
\tag{1}
\]

Write S_m = Sel(Q,E[p^m]), R_2 = Z/p^2 Z, and use L016's scalar
tau, prescribed components c_1,c_2 and residual basis e_1,e_2.
Neither finite p-primary Sha nor positive rational rank is assumed.
This is the exact theorem application approved in
[the saved SPECIALIZE assessment](../drafts/literature/2026-10-04-prime-deletion-p3-initial-fitting.md).

## Conclusion

The actual arithmetic obstruction satisfies tau = 0. Consequently both
prescribed prime-deletion components c_1,c_2 are classical and form an
R_2-basis of S_2. Their residual error vectors h_1,h_2 vanish, and

\[
\rho:S_2\longrightarrow S_1\text{ is onto},\qquad
\Sha(E/\mathbf Q)[p]=p\Sha(E/\mathbf Q)[p^2].
\tag{2}
\]

The p-primary Selmer group Sel(Q,E[p^infinity]) is infinite.
The achieved rational-rank bound is still only rank E(Q) <= 2.
No positive rational-rank lower bound, finite p-primary Sha, compatible
classical lifts at all depths or rational Kummer membership is concluded.
No P_(3,0) eligibility for the fixed primes is needed.

## Proof

**Match the nonvanishing premise to the cited theorem.** Use Chan-Ho
Kim, *The structure of Selmer groups and the Iwasawa main conjecture
for elliptic curves*, publisher-hosted author text dated 2025-05-12,
[Sections 1.2.2 and 1.4, printed pp. 4--6](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=4),
and [Corollary 1.11, printed pp. 8--9](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf#page=8).
These inputs were read in the saved assessment; they are imported here
without reproof.

At either ell_i, P_(2,0) gives ell_i congruent to 1 modulo p^2 and
E(F_(ell_i))[p^2] cyclic of order p^2. Thus its residual p-torsion is
cyclic, and p^2 divides #E(F_(ell_i)) = ell_i + 1 - a_(ell_i)(E).
In particular ell_i satisfies Kim's mod-p auxiliary-prime conditions,
and his coefficient ring at N has a quotient F_p. Hence N is an
admissible nonvanishing witness in his collection of Kurihara numbers.

Choose the same Neron plus period and compatible primitive roots in
the modular-symbol definitions of both sources. The mod-p number is
the sum of the plus modular symbol at a/N times the two discrete
logarithms, reduced modulo p, over a in (Z/N Z)^times. Reduction of
Kim's tilde-delta_N gives that sum. Sakamoto's definition in
[*p-Selmer group and modular symbols*, Section 1.1, printed pp. 1892--1893](https://ems.press/content/serial-article-files/29299?nt=1#page=2)
uses the same mod-p sum; [Lemma 4.2, printed p. 1917](https://ems.press/content/serial-article-files/29299?nt=1#page=27)
supplies its comparison with the residual rank-zero scalar used in L016.
Changing the logarithm generators only multiplies the sum by nonzero
mod-p factors. The ordinary normalization factors are units under the
retained non-anomalous hypothesis, as recorded in Sakamoto's
[Remark 3.1, printed p. 1908](https://ems.press/content/serial-article-files/29299?nt=1#page=18).
Therefore the assumed nonzero mod-p number implies

\[
\widetilde\delta_N\ne0,\qquad
\operatorname{ord}(\widetilde{\boldsymbol\delta})<\infty.
\tag{3}
\]

Only a witness is required for (3). Minimality modulo p and the count
of two prime factors are used by L016, but are not identified with
the minimum of Kim's integral collection, the complex vanishing order
or a cyclotomic derivative degree.

The other hypotheses of Kim's Corollary 1.11 are p >= 5, surjectivity
on E[p] and the Manin constant prime to p; all are retained explicitly.
Apply that corollary by citation:

\[
\operatorname{Sel}(\mathbf Q,E[p^\infty])\text{ is finite}
\quad\Longleftrightarrow\quad L(E,1)\ne0.
\tag{4}
\]

Equation (1) therefore makes this p-primary Selmer group infinite.
It does not assert that the whole Sha group is infinite or that
the rational rank is positive.

**Exclude the nonzero-tau alternative.** If tau != 0, L016 gives

\[
\operatorname{rank}E(\mathbf Q)=0,\qquad
\Sha(E/\mathbf Q)[p^\infty]\simeq\mathbf F_p^2.
\tag{5}
\]

Taking the filtered colimit of the standard finite Kummer sequences
under coefficient inclusions gives the exact sequence

\[
0\longrightarrow E(\mathbf Q)\otimes\mathbf Q_p/\mathbf Z_p
\longrightarrow\operatorname{Sel}(\mathbf Q,E[p^\infty])
\longrightarrow\Sha(E/\mathbf Q)[p^\infty]\longrightarrow0.
\tag{6}
\]

Filtered colimits preserve exactness; the point-quotient maps here
are multiplication by p and the Sha maps are inclusions. The finite
Kummer inputs are the ones recorded in the standard foundations,
Milne, *Elliptic Curves*, second edition (2021),
[Chapter IV, equation (29), printed p. 113](https://www.jmilne.org/math/Books/EC2.pdf#page=118).
By finite generation and the rank-zero statement in (5), E(Q) is
finite and its tensor product with Q_p/Z_p is zero. Equations (5)--(6)
would then make the p-primary Selmer group F_p^2, hence finite.
This contradicts (1) and (4). Thus tau = 0.

Apply the zero alternative of L016 to obtain the stated basis,
vanishing errors and coefficient surjectivity. L015's Kummer descent
criterion then gives the Sha equality in (2). This uses no depth-three
component or initial Fitting calculation: the stronger assessed
arithmetic converse already excludes the entire nonzero branch.

The continuation test is met for this first obstruction only.
The formal nonzero-tau models in L016--L017 remain valid for their
tested packages; they are not full arithmetic families with (1) and
the hypotheses of (4). Classical Selmer membership does not mark the
rational Kummer subspace. The required r >= 2 and uniform production
of the auxiliary premise from m(E) = 2 remain unresolved.
This is an applicability specialization of known results, classified
as REPRODUCTION; no progress beyond the checked literature is claimed.

## Mathlib

Full library coverage of this central-vanishing/tau implication:
**not checked**. Supporting Kummer colimits, Kurihara normalizations,
coefficient Selmer maps and rational Kummer membership: **not checked**.
Kim's Corollary 1.11 matches (4); his Sections 1.2.2/1.4 and
Sakamoto's Section 1.1, Remark 3.1 and Lemma 4.2 support applicability.
Milne's cited Kummer sequence supports (6). These are direct arithmetic
references, not asserted Mathlib matches or a full-statement match for
the tau corollary. No absence or originality inference is made.
