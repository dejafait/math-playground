# Fixed torsion-field integral arithmetic: source review, step 281

This is literature work only. No field discriminant or order has been
computed. The main gap remains rank E(Q)=ord_(s=1)L(E,s) for arbitrary
analytic order at least two. Complete arithmetic in L067's field is a
prerequisite for L066 item 2, not a sufficient descent or rank certificate.

## Inspected primary mathematics

Del Corso--Dvornicich--Simon, *Decomposition of primes in non-maximal
orders*, Acta Arithmetica **120** (2005), 231--244,
[publisher PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/82018):
Section 2, pp. 232--234; Proposition 4; Section 4, Proposition 9 and
Theorem 2, pp. 238--240. For primitive irreducible
F=a0*x^n+a1*x^(n-1)+...+an over a Dedekind ring R, with a0 nonzero,
define Ti(x)=a0*x^i+...+ai. In L=Frac(R)[x]/F,
RF=R+T1(alpha)R+...+T_(n-1)(alpha)R is an order, with
disc(RF)=disc(F). Proposition 4 proves this by its triangular basis
change. Proposition 9 says, for an order O and prime p, that
(rad(pO):rad(pO))=O exactly when O is p-maximal; otherwise the enlargement
has p-power index. Theorem 2 gives a homogeneous-factor gcd test and an
explicit first enlargement. Its proof identifies the multiplier lattice
through ideal containment and the least-common-multiple condition.
Section 3's Proposition 5 treats the factor at infinity by reciprocal
polynomials; it cannot be dropped at a leading-coefficient prime.
These statements apply over R=Z. L067 supplies the required primitive
irreducible H of degree 48 with leading coefficient 343. This is a
proposed application, not an evaluated instance.

Stein, *Algebraic Number Theory*, Section 4.3.3,
[Theorem 4.3.5 (Pohst--Zassenhaus)](https://wstein.org/books/ant/ant/node29.html),
was read as a second statement of the general radical--idealizer criterion.
Its displayed proof establishes only the p-power index bound and explicitly
leaves maximality to be completed. Do not describe it as a complete proof
of the stopping implication. Import the named criterion using the precise
primary Proposition 9 above; this notebook does not reprove it.

## Inspected implementation sources and alternatives

[PARI stable manual, general number fields](https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html),
entries nfbasis, nfcertify, nfdisc and nfinit, read 2026-10-17:
Round 4 is the default global basis algorithm. Restricted prime lists
certify only local maximality. nfcertify returning an empty vector certifies
the basis/discriminant; unresolved composite entries do not. Nonintegral
or nonmonic input changes the polynomial and requires retaining coordinate
transport. Buchmann--Lenstra processing of coprime composite factors can
avoid some complete factorizations, but successful certification is still
required. These are alternatives, not installed or executed computations.
Nor is nfcertify a certificate of units or class-group completeness.

SymPy 1.14.0, [numberfields.basis.py](https://raw.githubusercontent.com/sympy/sympy/1.14.0/sympy/polys/numberfields/basis.py),
lines 10--85 and 176--232, was inspected completely in those ranges.
Its first enlargement uses the Dedekind gcd; subsequent enlargements compute
the Frobenius kernel and multiplier constraints until stabilization.
The nilradical routine uses x -> x^q with q a power of p at least the
dimension, including small p; it does not substitute a trace-kernel test.
The implementation also normalizes nonmonic input. Its returned radical
dictionary is deliberately limited and is not a complete certificate.
[Poly root-scaling documentation](https://docs.sympy.org/latest/modules/polys/reference.html#sympy.polys.polytools.Poly.make_monic_over_integers_by_scaling_roots)
confirms that a monic integral presentation plus its scale is an alternative.

The Magma handbook was retrieved only through its introductory order and
optimized-representation passages; the maximal-order algorithm section
could not be retrieved reliably. It is an unread implementation lead.
Belabas's indexed textbook result on Round 2 was found, but the essential
pages repeatedly failed retrieval. It is not needed for the imported
criterion and is not counted as inspected proof coverage. Simon's 2001
*The index of nonmonic polynomials* was located through the author's page
and publisher abstract only; no additional theorem is imported from it.

## Local comparison, feasibility and limits

Inspected L067's whole field identification and certificate contract,
L066 item 2, its ready Section 5 audit coverage, ATTEMPTS/034 and /036.
Targeted local searches found no earlier maximal-order certificate. The
external exact 389/seven-torsion/degree-48 query found no inspected matching
computation; this does not establish absence or novelty. Preserve the
stopped incidence columns and all current norm evidence.

Neither gp, sage nor magma is on PATH or at the checked conventional
gp/sage locations. System python3 has no sympy or cypari2 module. The
earlier fixed-field attempt also records missing sympy/flint. No package
was installed, and no arithmetic routine ran. Direct shell download failed
DNS; primary-paper text was readable through the web tool. No essential
source blocker remains for the proposed first test.

The nonmonic order is the preferred starting representation: it retains
L067's exact t coordinate and avoids assuming t integral or producing a
large root-scaled power order. This is a choice to test, not a runtime
prediction. Full maximality would additionally need all possible index
primes covered and radical--idealizer terminal certificates, or an
independently certified global basis from a known implementation. A
7-maximal order alone does not supply that evidence. No argument here
identifies its S-class group with that of the maximal S-order. A smaller
localization-based certificate remains unapproved; its group comparison
would need separate coverage. No claim about ramification support is used.

## Proposed bounded first test (not executed)

Inputs: audited L067 certificate and field/basis transports; L066 item 2
is motivation only. Recheck the 49 H coefficients, content, degree,
leading coefficient and consistency with h. Build all 48 displayed RF
basis elements and their rational change matrix/inverse in Q[t]/h.
Retain all 110592 multiplication coefficients, the identity vector,
all 2304 trace-Gram entries, the nonzero exact determinant, and a separate
polynomial-resultant discriminant with full elimination witnesses.
An independent verifier must check every entry, integral closure of
the lattice under multiplication, both matrix inverses, and the equality
of these two exact discriminants. Here “closure” means ring closure,
not integral closedness/maximality.

Fix one producer stage and one independent replay stage, each with
180 seconds internal and 181 seconds external watchdog, total new output
at most 134217728 bytes. Save partial evidence on interruption; do not
raise limits, resume a timed-out stage, or retrospectively split it.
Complete equality certifies the starting order and its order discriminant
only. Any wrong coefficient, nonintegral product, missing entry, determinant
disagreement or cap failure stops the test and supplies a named failure.
Factorization, overorder iteration, field-discriminant naming, S-units,
S-class groups and a Selmer bound are outside this first test.

Successful starting-order evidence would enable a later separately
assessed index-prime/maximality test. Lack of a feasible complete result
parks this representation and requires a different independently testable
arithmetic target. All L026 premises, complete global power classes,
descent functions/local bounds, successful localization, rational
membership, divisible Sha and arbitrary-curve comparison remain unresolved.
Full/supporting Mathlib coverage was not checked; no absence is inferred.
