# L092 — Normal-closure degrees and distinct source thresholds

## Hypotheses

Fix one survivor E/Q of audited L089, with the same c,h,d_*,e_*,
closure and two domains. For each of its six orderings o retain exactly
L090's literal full-coordinate field G_o, ambient M and native
T=F_tpd=Q(E[2])=Q(t_o). All normal closures are over F_mod=Q.
Use L090's proved full ambient group and complete stabilizers:

    Gal(M/Q)=GL_2(Z/4) x GL_2(Z/15),
    |Gal(M/G_o)|=8, |core(Gal(M/G_o))|=2.

For the source comparisons retain L091's qualified April 2020
reproduction/def= setting, d=6 and epsilon_d=1. The two numerical
thresholds are C_0=2|GL_2(F_3)||GL_2(F_5)| and
 delta=2^12*3^3*5*d. These are comparison constants, not assumptions
that the changed field satisfies the source's hypotheses. T is not
the source's ell-division field K; no prime-seven substitution is made.

## Conclusion

For every such ordering, the exact degrees and primary valuations are:

| Quantity | Value | v_2 | v_3 | v_5 |
| --- | ---: | ---: | ---: | ---: |
| [M:Q] | 2211840 | 14 | 3 | 1 |
| [G_o:Q] | 276480 | 11 | 3 | 1 |
| [G_o:T] | 46080 | 10 | 2 | 1 |
| [G_o^nor:Q] | 1105920 | 13 | 3 | 1 |
| [G_o^nor:T] | 184320 | 12 | 2 | 1 |
| C_0 | 46080 | 10 | 2 | 1 |
| delta | 3317760 | 13 | 4 | 1 |

Thus [G_o^nor:T]/C_0=4, while [G_o^nor:Q]/delta=1/3.
The original literal field saturates C_0; the normal closure exceeds
that relative bound but remains below the corollary's absolute bound.
This establishes no local ramification/different failure, preservation
theorem, complete repair, essential IUT flaw or finite B>=A conclusion.
The separate step367 critical audit below validates this specialization
with the stated source qualifications.

## Proof

### Known inputs and bounded test

The invocation-start assessment is
`drafts/literature/2026-10-20-normal-closure-degree-test.md` (SPECIALIZE).
It reuses the inspected source proof-use ledger in
`drafts/literature/2026-10-20-normal-closure-repair-scope.md`.
No general closure or torsion theorem is reproved. Import Milne,
[Fields and Galois Theory v5.10, September 2022](https://www.jmilne.org/math/CourseNotes/FT.pdf),
Theorem 3.17(b–d) and Remark 3.18(a,b), printed pp.39–40: finite
Galois correspondence, indices, composita and conjugates. L090 proves
M/Q finite Galois and computes the full core in that actual group;
its fixed field is G_o^nor. Consequently these imports apply directly.

The constants are those of Mochizuki, IUT IV, April 2020,
[inspected reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf),
Theorem 1.10 proof (i)–(ii), pp.23–24, (E3)–(E5), and Corollary
2.2(ii), pp.41–43, with its degree use on p.44. Authentication against
current author/journal bytes remains unresolved. The proof-use ledger
separates this relative group-size input from the absolute delta.

The intermediate target addresses whether a normal-closure repair
retains these degree inputs, while original finite B>=A remains the
main gap. Its downstream use is to decide which estimate needs a new
argument. Continue only if exact indices and both ratios can be given;
abandon the computation if L090's actual ambient/core hypotheses fail.
Do not infer any local bound or failure from these global numbers.

### Cardinalities and field indices

Counting ordered independent columns over F_p gives

    |GL_2(F_p)|=(p^2-1)(p^2-p).

The first column has p^2-1 choices and the second avoids its p-element
span. Thus |GL_2(F_2)|=6, |GL_2(F_3)|=48=2^4*3, and
|GL_2(F_5)|=480=2^5*3*5. Reduction modulo two from GL_2(Z/4)
is onto: any lift of an invertible mod-two matrix has odd determinant.
Its kernel consists of all Id+2X for X in M_2(F_2), so has order 16.
Hence |GL_2(Z/4)|=96=2^5*3. CRT identifies GL_2(Z/15) with
GL_2(F_3) x GL_2(F_5). L090's actual product therefore has order

    [M:Q]=96*48*480=2^14*3^3*5=2211840.

L090 also supplies the surjective mod-two action whose full division
field is T=Q(E[2]), whence [T:Q]=6. In particular T is an actual
subfield of each G_o and of its normal closure; it is not merely a
parameter-degree upper bound. Finite Galois correspondence gives
[M:G_o]=8 and [M:G_o^nor]=2. Tower degrees now give

    [G_o:Q]=[M:Q]/8=2^11*3^3*5,
    [G_o:T]=[M:Q]/(8*6)=2^10*3^2*5,
    [G_o^nor:Q]=[M:Q]/2=2^13*3^3*5,
    [G_o^nor:T]=[M:Q]/(2*6)=2^12*3^2*5.

These computations use the full order-two core, including both scalar
sectors in L090, rather than a guessed radical degree. All six fields
have these degrees because their stabilizer orders and core agree.

### Two different comparisons

Directly from the inspected constants,

    C_0=2*48*480=2^10*3^2*5=46080,
    delta=2^12*3^3*5*6=2^13*3^4*5=3317760.

The ratios in the conclusion follow by exact cancellation. Specifically
the relative closure degree has two more factors of two than C_0,
whereas its absolute degree has one fewer factor of three than delta.
The absolute slack is delta-[G_o^nor:Q]=2211840. Retaining that slack
is necessary: exceeding C_0 does not refute the separate absolute
inequality. Conversely satisfying that absolute inequality does not
restore the specific relative group-size input or prove the other
initial-data clauses. Local inertia, differents and applicability of
Proposition 1.3 require independent hypotheses and calculations.

The meaningful arithmetic check is reproducible from this directory:
`python3 scripts/normal-closure-degree/check.py`.
It writes the complete small certificate to
`scripts/normal-closure-degree/certificate.json` and prints actual and
required bounds, all primary valuations, failures and the path. It
checks only the arithmetic conditional on L090, not those hypotheses
or any local assertion. All displayed equalities are justified above;
the certificate is supplementary evidence.

### Separate critical audit — 2026-10-20, step367

**Scope and verdict.** The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-20-normal-closure-degree-critical-audit.md`.
The specialization passes without correction or additional direct
input. This audit uses audited L090, the cited Milne correspondence,
and the reused qualified source readings; it approves no repair theorem.

**Actual group and all orderings.** L090 identifies M with the full
60-division field of the original survivor. Full level-120 image
projects onto the displayed product by CRT and reduction modulo four.
Its order is a product because the joint image is full, not merely
because its marginal images are full. Reduction modulo two is onto;
its kernel consists of the sixteen distinct matrices Id+2X for
X in M_2(F_2), each of odd determinant. Thus the mod-four order is
16*6=96. The independent-column counts at three and five give 48
and 480. The determinant-one restriction in L090 belongs to the
subgroup fixing k, not to Gal(M/Q).

The orderings (123),(213) give the alpha character, (132),(312)
the beta character, and (231),(321) the gamma character. Reversing
a difference multiplies its radical by iota, fixed in U, so these
repeated characters are exact. Each of the eight radical-sign triples
gives precisely one element in each kernel: b is that character times
Id modulo fifteen. Both uniform scalar signs occur; opposite signs
on the 3- and 5-primary modules cannot fix full torsion.
The common intersection requires all three signs to agree, leaving
exactly +++ with b=Id and --- with b=-Id. L090 proves that every
ambient conjugate is one of these three kernels and that all occur,
using the actual equations and complete torsion coordinates. Hence
this order-two intersection is the core in the whole ambient group,
not just in U. All six cases have kernel order eight and this core.

**Tower direction and complete factorization.** The actual mod-two
image is GL_2(F_2), so its full division field T has degree six.
L090's equality T=Q(t_o) puts this same T inside every G_o and its
normal closure. Milne's finite Galois hypotheses hold for M/Q.
The orders eight and two are [M:G_o] and [M:G_o^nor], respectively,
not degrees over Q. Factor the actual ambient order:

    96*48*480=(2^5*3)(2^4*3)(2^5*3*5)=2^14*3^3*5.

Division by eight gives the literal absolute degree 2^11*3^3*5;
division by two gives the closure absolute degree 2^13*3^3*5.
Dividing each separately by [T:Q]=2*3 gives 2^10*3^2*5 and
2^12*3^2*5. These verify every field-degree value and every primary
valuation in the conclusion. The other two rows factor as
C_0=2^10*3^2*5 and delta=2^13*3^4*5. There is no unlisted
prime factor in any row.

**Source bases and limits.** The inspected Theorem 1.10 proof
(i)–(ii), pp.23–24, uses the allowance from adjoining full 15-torsion
and iota over the tripodal field: the relative constant C_0.
Corollary 2.2(ii), pp.41–43, defines delta=2^12*3^3*5*d;
its proof p.44 uses an absolute degree allowance. Here d=6 bounds
parameter degree, whereas [T:Q]=6 was independently established.
The exact comparisons are

    [G_o^nor:T]/C_0=2^(12-10)=4,
    [G_o^nor:Q]/delta=3^(3-4)=1/3.

The absolute slack is 3317760-1105920=2211840. Comparing the
absolute degree with C_0, or the relative degree with delta, would
test neither source use. The normal closure fails the relative
allowance and satisfies the absolute allowance. This asserts neither
that the source theorem applies to the changed field nor that any
source conclusion or local bound fails. T is not the height-selected
ell-division field K.

The arithmetic script was rerun and its complete seven-value,
21-valuation certificate checked against the factorization above.
It reports both ratios and no arithmetic failures. Its group/core
premises are justified mathematically above, not by the script.
No new mathematical program is needed.

The April reproduction/current-version authentication and def=
interpretation remain qualified. Local inertia/differents, other
field choices, the height-selected prime, independent initial data,
native input/action/factorization/pilot and essentiality are unresolved.
Original finite B>=A remains open. The assembly and DAG are unchanged;
this canonical audit supersedes the overview's pending-audit wording
without changing its argument. This is REPRODUCTION, with no claim
beyond the sources checked and no complete-solution candidate.

## Mathlib

Full matching coverage for this exact specialization is unchecked.
Supporting finite Galois correspondence and finite general-linear-group
cardinality coverage has not been checked in Mathlib in this step.
No absence or formal verification claim is made. This is a local
specialization of known methods (REPRODUCTION), not a claimed advance
beyond the inspected literature. Alternative models/repairs, the
height-selected prime, independent initial data, native input/action,
marked factorization/pilot transport and essentiality remain unresolved.
