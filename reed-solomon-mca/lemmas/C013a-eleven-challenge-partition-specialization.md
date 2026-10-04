# C013a — A partition attaining eleven bad parameters

## Hypotheses

Let F=F_(97^20), let H be the order-sixteen subgroup of F_97^*, and
let C=RS[F,H,8]. Use the event in
[the pinned model](../foundations/02-pinned-affine-line-model.md) on
1/4<=delta<5/16. Partition H as
\[
 A=\{1,8,22,27,89\},\quad
 B=\{18,33,50,85,96\},\quad
 J=\{12,47,64,70,75,79\}.
\]
Put Q(X)=product_(x in J)(X-x), and use the L013 inputs
a_x=xQ(x), b_x=-Q(x) on A, with both zero elsewhere.

## Conclusion

This pair has exactly eleven bad parameters:
\[
 B(a,b)=A\cup B\cup\{77\}.
\]
Consequently E_C(delta)>=11/97^20 on the four-omission cell.
This strengthens the previously achieved lower bound ten; eleven is
still below the count sixteen needed to exceed the allowable fifteen.

## Proof

Apply L013 to this particular partition. Its hypotheses give the
actual nonpersistent locator and original same-support event, and its
fiber theorem holds over the whole extension field. It remains to check
the six ratios and the residual root; no general locator theorem is
being reproved.

The two monic block polynomials are, in F_97[X],
\[
 U=X^5+47X^4+94X^3+84X^2+73X+89,
 \qquad V=X^5+9X^4+66X^2+52X+75.
\]
Their evaluations give

| x in J | 12 | 47 | 64 | 70 | 75 | 79 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| U(x)/V(x) | 54 | 55 | 55 | 55 | 55 | 11 |

The denominators are nonzero because J is disjoint from B. Thus the
unique fiber of size at least four is J_55={47,64,70,75}; its ratio is
nonzero and differs from one. Direct polynomial multiplication gives
\[
 \frac{U(X)-55V(X)}{1-55}
 =X^5+55X^4+27X^3+X^2+57X+46
 =(X+20)(X-47)(X-64)(X-70)(X-75).                       \tag{1}
\]
L013's size-four fiber case therefore supplies the unique additional
parameter -20=77. This is outside A union B. Its error support is J_55;
the ten other supports and their same-support failure are already
proved in L013. Its exact count theorem excludes all further parameters
over F_(97^20), so extension-field splitting has not been inferred from
a prime-field sample.

Taking this pair in the maximum defining E_C gives the stated lower
bound. The field-budget inequality remains
15*2^128<=97^20<16*2^128; this application alone does not decide safety.

The exact auxiliary command
`python3 scripts/coefficient-feasibility/five_coordinate.py` checks (1),
the actual signed minors, the divided difference, the coefficient power
residuals, and exact F_(97^20) root splitting. It separately tests the
original event on all 2517 admissible supports for these inputs. The
proof uses the displayed fiber calculation and L013, with the finite
search serving only to find the partition.

## Mathlib

Coverage of this full partition specialization: **not checked**. No
matching theorem or Lean verification is claimed. Supporting resultant
products are **present** in the previously inspected
[Resultant.Basic at commit 300d0e535721bc098547106fc297d8ba2a63f6bb](https://github.com/leanprover-community/mathlib4/blob/300d0e535721bc098547106fc297d8ba2a63f6bb/Mathlib/RingTheory/Polynomial/Resultant/Basic.lean),
including
[Polynomial.resultant_prod_left](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Resultant/Basic.html#Polynomial.resultant_prod_left).
That source contains supporting algebra, rather than this MCA statement;
the full result is **absent from that source checked**. Supporting
finite-field arithmetic coverage elsewhere is **not checked**.

This is an application of the established local L013, classified as
reproduction. No originality claim or July ABF26 correspondence is made.
