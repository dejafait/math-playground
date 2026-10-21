# L082 — Published seven-primary Sha vanishing for the conductor-389 curve

## Hypotheses

Let E/Q be the elliptic curve

\[
y^2+y=x^3+x^2-2x,\qquad [a_1,a_2,a_3,a_4,a_6]=[0,1,1,-2,0].
\]

Use L030's minimal conductor-389 model, L034's published identification
with Cremona 389A1/389a1, and L033's good ordinary reduction at p=7.
Import the computational theorem of William Stein and Christian Wuthrich,
*Algorithms for the arithmetic of elliptic curves using Iwasawa theory*,
Math. Comp. **82** (2013), 1757–1792,
[Theorem 12.3, printed p.1788](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=32).
The original computation is a cited mathematical input, not a computation
independently replayed in this notebook. No BSD conjecture, full Sha
finiteness, L026 premise package or global descent certificate is assumed.

## Conclusion

\[
\Sha(E/\mathbf Q)[7]=0,
\qquad \Sha(E/\mathbf Q)[7^\infty]=0.
\]

This is a known fixed-case result, assembled locally by applicability and
an elementary group argument. It is not a new discovery beyond the cited
source. No conclusion about other primary components, full Sha finiteness,
the refined formula or arbitrary-curve rank equality is asserted. The
separate fixed critical audit below passes, with the original published
computations still unreplayed.

## Proof

**Exact source and model.** Immediately before Theorem 12.3 the authors
identify their curve as 389a. The theorem proves vanishing of its
p-torsion for every good ordinary p<48859 except 16231, as well as at two.
Its proof is the fixed computation described in Section 12.4,
printed pp.1787–1788, using the ordinary Algorithm 11.1,
printed pp.1783–1784. The separate statement about the conjectural BSD
order modulo p is not used as evidence for the vanishing theorem.

The needed exact label match is L034's inspected Cremona input:
*Algorithms for Modular Elliptic Curves*, corrected second edition (1997),
Table 2, printed p.257, row 389A1, with the group interpretation in
Chapter 4, printed p.105; the author's
[ecdata generator table](https://johncremona.github.io/ecdata/)
identifies that entry with [0,1,1,-2,0]. Thus we use the specified curve,
not an inference that equal rank and conductor imply isomorphism.
The general Weierstrass convention converts that vector into precisely
the equation in the hypotheses. L030 independently supplies minimality
and conductor 389. No change of variables or transfer to another model
is needed.

**Prime applicability.** L033's complete reduction count gives
#E(F_7)=13. Since the minimal discriminant is 389, seven is good;
its trace is 7+1-13=-5, which is nonzero modulo seven, so it is ordinary.
The inequalities 7<48859 and 7!=16231 place it in the theorem's proved
range. Apply Theorem 12.3 to obtain Sha(E/Q)[7]=0.

**From torsion to the primary subgroup.** For any abelian group A,
define A[7^infinity] as the union of the subgroups A[7^n], n>=1.
If a nonzero x belonged to this union, choose the least n>=1 with
7^n x=0. Minimality gives y=7^(n-1)x!=0, while 7y=0.
Thus A[7] would be nonzero. Apply the contrapositive with
A=Sha(E/Q). This proves the second conclusion without any assumption
that A or its primary subgroup is finite, and excludes divisible
seven-primary torsion as well as finite seven-primary torsion.

**Qualification and downstream use.** The regulator, residual and
leading-term computations underlying the published theorem have not
been independently replayed here. They are part of the cited theorem's
proof; no new regulator valuation is claimed. Its exact-target source
comparison is retained in
[drafts/literature/2026-10-18-fixed-seven-integral-leading-term.md](../drafts/literature/2026-10-18-fixed-seven-integral-leading-term.md).
Reproving that computation is unnecessary for this import. In particular,
this does not upgrade L004's general rationalized divisibility to an
integral theorem, or use L081's local point test as a regulator.
The result supplies a fixed arithmetic input independent of the unfinished
unit/class calculations. L034's fixed finiteness conclusion is strengthened
to triviality here; no additional independent-point or analytic-order
argument is required for this strengthening. The general rank/order gap
and the other arithmetic certificate obligations remain unresolved.

**Separate critical audit, 2026-10-18 (step 313).** The approved audit
checks this application, not a new execution of the published algorithm.
Theorem 12.3, its preceding identification and entire short proof, and
Remark 12.4 on printed p.1788 agree with the import above. Section 12.4,
printed p.1787, separates its proved torsion bound from its additional
conjectural-order consistency check. The proof of Theorem 12.3 refers to
that computation; it is not a theorem conditional on accepting BSD.
Neither the consistency statement nor the exceptional-prime regulator
discussion is used as a substitute for the proved conclusion at seven.

There is no model transfer hidden in the shorthand 389a. The source's
Section 12.4 uses optimal representatives. Cremona's linked ecdata
documentation, **TABLE ONE: CURVES**, identifies the optimal representative
below conductor 370000 as curve 1, with its stated exception at 990h;
**TABLE TWO: GENERATORS** explicitly identifies 389a1 with
[0,1,1,-2,0]. Thus the source's representative is L034's exact equation.
This confirms the existing label match using the authors' conventions,
rather than uniqueness inferred from conductor and rank. The minimality
argument in L030 is also checked: its discriminant has local valuations
zero or one, so none can decrease by twelve while remaining nonnegative.
The listed invariants give discriminant 389 and good reduction at seven.

The complete seven-row count in L033 has two affine solutions for each
x except x=2, which has none; the sole point at infinity gives thirteen.
For example the possible values of y^2+y modulo seven are 0,2,5,6;
at x=2 the right side is 1. Hence the trace is -5, a unit modulo seven.
Together with 7<48859 and 7!=16231 this meets the exact theorem range.
L034 supplies the independently published rank-two identification, but
its finiteness result, cyclotomic height and coefficient squeeze are
not used to prove this import's torsion conclusion. No new caller-supplied
regulator or residual condition is concealed: those computations belong
to the published fixed theorem, whose execution remains unreplayed.

The group argument above is valid for every abelian group. For n=1 its
nonzero element y is x itself. For n>1, y=0 would contradict the least
choice of n. Thus every nonzero element killed by a power of seven would
contradict the imported vanishing at seven. A divisible seven-primary
group has no exemption from this elementwise argument; no bound on n,
finite generation, order of Sha or prior finiteness is needed.

All four audit tests pass: exact model, prime range, source qualification,
and primary-group passage. This validates a known fixed arithmetic input,
not a new Sha theorem. L030, L033 and the model-identification use of L034
remain exactly the direct local inputs listed in DAG.md; no dependency
on L081, L026 or unfinished order/descent work has been added. Full Sha
finiteness, a rational-direction construction for arbitrary curves, and
complex-order/rank equality in general remain outside the result.

## Mathlib

Full matching theorem and supporting coverage: **not checked**.
The proof input is the precisely cited published theorem; no claim of
Mathlib availability or absence is made.
