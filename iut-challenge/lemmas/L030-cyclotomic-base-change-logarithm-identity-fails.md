# L030 — The cyclotomic base-change logarithm identity fails

## Hypotheses

Fix an algebraic closure of Q_3, choose pi with pi^27=3 and a primitive
twentieth root zeta=zeta_20, and put K=Q_3(pi), U=Q_3(zeta), L=KU.
Normalize v_3(3)=1. Let J=log(O_K^times), J_L=log(O_L^times), and let
A=O_U J denote the finite O_U-linear span of J inside L. Logarithms
are continuous unit logarithms killing finite unit torsion; on principal
units they are the convergent series. No O_U-stability of J_L is assumed.

Use L016's **complete** description of J, including its deep ideal and
separator. The unchanged prior SPECIALIZE assessment is
`drafts/literature/2026-10-08-cyclotomic-base-change-logarithm.md`.
Import **Pete L. Clark, Algebraic Number Theory II: Valuations, Local
Fields and Adeles**, author-hosted undated 161-page version inspected
2026-10-08, **Proposition 2.5/Corollary 2.6**, pp. 63–64,
**Proposition 2.9/Corollary 2.10**, p. 65, and **Proposition 2.30**,
p. 76 ([primary notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf)).
These supply unramified classification/base change, Eisenstein integral
models and prime-to-residue-characteristic torsion lifting with order
preservation. The continuous logarithm and deep log/exp inputs used in
L016 are **Hess–Pauli–Pohst, Computing the Multiplicative Group of
Residue Class Rings**, author-hosted undated 18-page manuscript,
**section 3, Theorems 3.1/3.3**, pp. 3–5, and **Proposition 5.1(i,iii–iv)**,
pp. 9–10 ([primary manuscript](https://page.math.tu-berlin.de/~kant/publications/papers/hepapo.pdf)).
The general theorems are imported, not reproved; only the field-specific
comparison below is derived.

## Conclusion

The proposed equality J_L=A is **false**. In fact the actual unit logarithm

\[
x=\log(1+\zeta\pi)\in J_L
\]

does not belong to A. Writing y=sum_(r=0)^26 c_r pi^r with c_r in U,
the U-linear functional

\[
\Phi(y)=3c_0-\frac{31}{3}c_1+9c_{15}-9c_{18}
\]

satisfies Phi(A) subset O_U and

\[
\Phi(x)\in\frac{\zeta^{27}-31\zeta}{3}+O_U,
\qquad v_3(\Phi(x))=-1.
\]

This stops naive scalar extension of the old logarithm lattice. It does
not compute the complete new lattice J_L, claim either opposite
containment, establish packet admissibility or source-realized actions,
or demonstrate an essential IUT flaw or failure of finite B>=A.

## Proof

### Field hypotheses and common coordinates

Since 3 does not divide 20, the cited unramified classification and
prime-to-3 root-lifting theorem identify U as the unramified extension
of degree ord_20(3)=4: the successive powers modulo 20 are 3,9,7,1.
Its residue field is F_81, its uniformizer is 3, and the reduction
bar(zeta) retains order 20. In particular O_U is a closed valuation ring
and v_3 takes integral values on U^times.

The polynomial X^27-3 is Eisenstein over O_U. The cited integral-model
theorem gives L=U(pi), [L:U]=27, O_L=O_U[pi] and uniformizer pi,
with v_3(pi)=1/27. Thus 1,pi,...,pi^26 form the required U-basis.
For coefficients in U, the fractional valuation parts r/27 are distinct,
so there is no cancellation among least-valued coordinate terms.
In particular H_L=pi^14 O_L has coordinates c_r in 3O_U for r<14
and c_r in O_U for r>=14. This is a common coordinate model for A
and J_L; it does not impose a module structure on J_L.

### Integrality on the complete scalar span

L016 proves J=H+sum_(j=1)^13 Z_3 q_j, where H=pi^14 O_K,
using all principal-unit layers and a proved infinite tail. It proves
that the restriction phi of Phi to K takes the following values on
the **entire** generating list:

\[
(\phi(q_1),\ldots,\phi(q_{13}))
=(0,0,4,0,0,0,0,0,3,0,0,0,0),
\qquad \phi(H)\subset Z_3.
\]

On the power-basis generators of H, the only nonzero values are
9,-31,9,-9 at r=0,1,15,18. Hence phi(J) subset Z_3 is a
complete-image assertion, not a test of sampled units.
Every a in A is a finite sum sum_i b_i j_i with b_i in O_U and
j_i in J. U-linearity gives Phi(a)=sum_i b_i phi(j_i) in O_U.
This proves the required obstruction on all of A without computing J_L.
No all-unit description of the left side is necessary for a one-sided
noncontainment: the witness below is itself a genuine logarithm.

### Exact leading terms and the infinite remainder

The point 1+zeta pi is a principal unit. Its logarithm is

\[
x=\sum_{k=1}^{\infty}\frac{(-1)^{k+1}\zeta^k\pi^k}{k}.
\]

This series converges since its term valuation is k/27-v_3(k),
which tends to infinity. Phi is a continuous U-linear functional,
so it may be applied term by term. For k=27m+r with 0<=r<=26,
write alpha_0=3, alpha_1=-31/3, alpha_15=9, alpha_18=-9 and all
other alpha_r=0. The term's Phi value is exactly

\[
\alpha_r\frac{(-1)^{k+1}3^m\zeta^k}{k}.
\]

Here are **all** cases for a nonzero contribution:

| Coordinate r | Range | Valuation of the Phi term |
| --- | --- | --- |
| 0 | k=27m, m>=1 | m-2-v_3(m) |
| 1 | k=27m+1, m>=0 | m-1 |
| 15 | k=27m+15, m>=0 | m+1 |
| 18 | k=27m+18, m>=0 | m |

For r=0 and m>=2, v_3(m)<=m-2. To see this, if h=v_3(m)=0,
the bound follows from m>=2; if h>=1, m>=3^h>=h+2,
the last inequality following by induction starting at h=1.
Thus the only nonintegral contributions are k=1 and k=27.
Both signs are positive, and their sum is
(zeta^27-31zeta)/3. Every other contribution belongs to O_U,
and their valuations tend to infinity (also in the r=0 case,
since v_3(m)<=log_3(m)). Their sum therefore belongs to the closed
ring O_U. This proves the asserted coset with a complete infinite
remainder bound, not just a finite approximation.

A separate uniform tail check relates this computation to L016's
controlled-tail method. For k in [3^h,3^(h+1)), h>=5,
the integer pi-valuation of the logarithm term is
k-27v_3(k)>=3^h-27h. The latter starts at 108>=14,
increases by 2*3^h-27>0, and tends to infinity. Thus all terms
omitted after k=242 sum inside H_L. On H_L, the four possible
Phi contributions have valuations at least 2,0,2,2 respectively,
so Phi(H_L) subset O_U. This independently controls the omitted
tail used by the finite certificate.

### Noncancellation in the residue field

Modulo 3O_U the numerator zeta^27-31zeta reduces to

\[
\bar\zeta(\bar\zeta^{26}-1).
\]

Its first factor is nonzero. Its second factor is nonzero because
bar(zeta) has order exactly 20, and 20 does not divide 26.
The numerator is therefore an O_U-unit, and its quotient by 3
has valuation -1. An O_U-valued remainder cannot cancel this
valuation. Hence v_3(Phi(x))=-1, whereas Phi(A) subset O_U.
It follows that x is outside A and the equality is false.

### Verification and scope

Run `python3 scripts/cyclotomic-log/check_scalar_transport.py`.
The full certificate is `scripts/cyclotomic-log/scalar-transport.json`.
It checks the 40 old generating-column separator values, all 351
stored old finite-sum congruences, every one of the 242 finite new
logarithm terms, their exact polynomial decomposition using zeta^20=1,
and the tail threshold 108 versus required 14. There are zero failed
finite checks; the mathematical comparison fails with actual separator
valuation -1 versus required >=0. The infinite-case bounds and the
order-20 residue argument are proved above rather than inferred from
this certificate. The existing certificate for L016 is input evidence,
not a replacement for its canonical all-unit and analytic proofs.

Classification is POTENTIALLY_NEW only in the prior assessment's
bounded-search sense. The inspected sources provide the field and
logarithm inputs but do not decide this exact scalar-extension identity;
no certified originality or progress beyond all existing literature is
claimed. The initial result was queued for the separate critical audit
recorded below.
L029's stop on the unchanged packet is preserved; this changed-field
test does not repair the actual/native input, action, global realization,
pilot transport, essentiality or normalized finite B>=A gaps.

### Separate critical audit, 2026-10-08

The gate-approved audit found no failed hypothesis, finite congruence or
infinite-series case. It validates this local noncontainment, without
adding an IUT application or a new logarithm-image theorem. The unchanged
coverage is `drafts/literature/2026-10-08-cyclotomic-logarithm-critical-audit.md`.

The complete-image input was checked from L016's proof, not its certificate
success flag. Its residue signs remove O_K^times/U_1; at each of the
thirteen subsequent layers the leading coefficient of 1+pi^j generates
F_3. Successively removing these classes leaves U_14. The imported inverse
log/exp theorem applies strictly at 14/27>1/2. Compactness of O_K^times
and continuity of log make J closed; additive integer stability then
gives Z_3-stability. Together with the proved H-valued infinite tails,
these facts justify both directions of the complete-image equality used
here. Only this part of L016 is needed; its diagonalized membership tests,
L015's outer radius estimate and the original IUT comparison are not
additional premises of this separator argument.

The independent checker `python3 scripts/cyclotomic-log/audit_scalar_transport.py`
parses every representative from L016's printed table and recomputes all
351 finite coordinate sums and error valuations from their defining
series. It compares every stored old sum and representative with that
recomputation, reconstructs all 27 deep-ideal columns, and verifies all
40 exact separator values. It also reconstructs every one of the 242
finite new-log terms, checks each against its residue-class valuation
formula, and compares the full old witness certificate's terms and
polynomials with the recomputation. These complete checks, not sampled
entries or previews, have zero failures. The full rational evidence and
failures list are in `scripts/cyclotomic-log/scalar-transport-audit.json`.
The observed separator valuation is -1 versus required >=0; the tail
bound is 108 versus required >=14. Polynomial lists modulo zeta^20=1
are only exact evaluation identities, not an assertion that twenty
coordinates are linearly independent in U.

Continuity and all infinite cases were checked separately. For a nonzero
y=sum c_r pi^r, the distinct fractional valuation parts imply
v_3(c_r)>=v_3(y)-r/27 for every nonzero coordinate. Thus
v_3(Phi(y))>=v_3(y)-28/27, which explicitly justifies termwise passage
to the convergent logarithm. For r=15, k=3(9m+5) has valuation exactly
one; for r=18, k=9(3m+2) has valuation exactly two. For r=1 it is a
unit. For r=0, k=27m has valuation 3+v_3(m), and the proof's inequality
v_3(m)<=m-2 includes m=2 and m=3. It follows for every m, not merely
the checked finite range, that k=1 and k=27 are the only nonintegral
terms. All remaining nonzero terms tend to zero and sum in the closed
ring O_U. The separate uniform tail proof is valid for both fields
because absolute ramification is 27; residue degree four does not
change this bound or the strict log/exp threshold.

Finally, the imported unramified classification and Eisenstein theorem
apply over the complete DVR O_U, and prime-to-3 reduction preserves the
order of zeta. The two exceptional terms have positive logarithm signs
and scalar values -31/3 and 1/3 at exponents 1 and 27. Reducing their
numerator gives bar(zeta)(bar(zeta)^26-1), which is nonzero because the
order is 20. An integral remainder cannot cancel valuation -1. The
actual input is a principal-unit logarithm, and U-linearity makes Phi
integral on every finite O_U-linear combination of the complete old J.
This proves the claimed obstruction with no assumption of O_U-stability
of J_L, opposite containment, complete new lattice or transported action.

## Mathlib

Full matching cyclotomic base-change logarithm failure: **not checked**.
Supporting unramified/Eisenstein, logarithm, valuation, module-span and
root-reduction coverage: **not checked**. The primary citations above
are supporting mathematical inputs; unknown Mathlib availability is
not evidence of absence.
