# L126 — Every full dyadic residual-relation basis has superlinear support

## Hypotheses

Work over F₂. Retain the entire original endpoints of L125:
A=Prod(F_N,G_N), B=Prod(G_N,F_N), where N=2^k, k>=0, F_N has
parallel 1/x layers and G_N is the N-edge x path. The coordinate order
of each endpoint is `s,f0,...,fN,h0,...,hN,t`. All three constant
product connectors, zero-residual vertices and final coordinates remain.
Use right closure, the residual columns R_A,R_B, and

    E_N={(u,v):u R_A=v R_B}.

Scalar support is the number of expanded nonzero entries in the two
original endpoint blocks. With g(J)=|V(J)|+2|E(J)|, the fixed endpoint
size is S=g(A)+g(B)=16N+20. The quantified generators must span the
**full** E_N, not only a paired reachable subspace. There is no restriction
on their chosen basis, signs (in F₂), cancellations or induced shift.

## Conclusion

Every row basis H of E_N, and every finite row generating set for E_N,
satisfies

    sum_(h in H) wt(h) >= 8+4(1+sqrt(2))^k.                (1)

Consequently its total scalar support divided by S is unbounded as k
increases. No O(N) expanded-support basis of the full E_N exists. In
particular, adding any requirement on the induced shift, accepting
boundaries or literal singleton realization cannot make the assessed
joint O(N) target hold. The obstruction already occurs in the maps.

At N=16, complete original-coordinate enumeration gives core threshold
span ranks `[0,0,1,6,16]` and full ranks `[0,6,8,13,23]` for thresholds
0 through 4. This confirms the finite discriminant, but (1) is proved
below for all k, independently of extrapolating those finite ranks.

This stops full-relation generating bases for these particular endpoints.
It does not exclude a smaller invariant paired subspace receiving the
boundaries, a different common source, general mixed-orientation chains,
or certificates for general operands. It proves no unrestricted circuit
lower bound or resolution of P versus NP. The separate conceptual audit
in §7 validates this restricted conclusion; no complete main-problem
candidate is claimed.

## Proof

### 1. Assessed scope and original-coordinate parameters

The unchanged pre-existing EXPLORE assessment
`drafts/literature/2026-10-28-residual-relation-generators.md` covers a
basis-independent obstruction to this exact joint target. The inspected
qualitative simulation and sparse-null-basis results do not supply its
binary quantitative conclusion. The cancellation-free Sierpinski bound
is not imported for arbitrary generators. The short multilinear support
argument below is supplied because the missing quantitative implication
must be established, not assumed from those comparisons. This use of the
assessment does not certify originality of that argument or the result.

Use L125 §2's full relation parametrization. Let P_N have row j the
coefficients of (1+z)^j for 0<=j<N, in increasing degree order. Reverse
the nonzero f/h index orders in the two endpoint blocks. The core rows
are exactly

    (A_f,A_h; B_f,B_h)=(r,(r+b)P_N; b,rP_N),             (2)

with arbitrary r,b in F₂^N. The remaining disjoint coordinate factors
are six free unit rows at the two copies of s,f_N,h_N and the paired
final row (t,t). Thus these 2N+7 parameters give a linear bijection onto
E_N. No coordinate has been removed from the support measure.

For a binary index j with bit set J subset {1,...,k}, introduce the
squarefree monomial X_J=product_(i in J) X_i. For a row a in F₂^N put

    f_a(X)=sum_(j=0)^(N-1) a_j X_bits(j).

This is a vector-space identification with multilinear polynomials,
not a claim about products after reduction. Write s(f) for its number
of nonzero monomials and f*(X)=f(1+X_1,...,1+X_k). Then

    s(f_a)=wt(a),    f_(aP_N)=f_a*.                      (3)

Indeed, in F₂, successive squaring gives
`(1+z)^j=product_(i in bits(j))(1+z^(2^i))` (bits numbered from zero
in this identity). Every subset yields a different exponent. Thus
P_N[j,ell]=1 exactly when bits(ell) is a subset of bits(j), which is
also the coefficient rule for product_(i in bits(j))(1+X_i). This
proves (3), including its row orientation and every coefficient.

### 2. Multilinear support-product inequality

For every nonzero multilinear polynomial f over F₂ in k variables,
with ordinary total degree d, we prove

    s(f) s(f*) >= 2^d.                                  (4)

All supports in (4) count distinct squarefree monomials after cancellation.
Assign degree -infinity to zero only for the following case distinctions.
The transformation * preserves multilinearity and is an involution. It
cannot increase total degree; applying it twice shows that it preserves
the degree of every nonzero polynomial. Also s(p+q)<=s(p)+s(q).

Induct on the number k of variables. At k=0 a nonzero polynomial is 1,
so both sides of (4) equal 1. For k>0 write uniquely

    f=f0+X_k f1,
    f*=(f0+f1)*+X_k f1*,

where the starred polynomials on the right use the other k-1 variables.
Set a=s(f0), b=s(f1), c=s(f0*), e=s((f0+f1)*), h=s(f1*).
The blocks without and with X_k are disjoint, so the product on the
left of (4) is exactly (a+b)(e+h). Linearity of * and the support
triangle inequality give c<=e+h.

If deg(f0)=d, f0 is nonzero and induction gives ac>=2^d. Then
`(a+b)(e+h)>=ac`, proving the claim in this case. This also covers
f1=0, and covers the constant-degree case d=0.

Otherwise deg(f0)<d, so f1 is nonzero, d>=1, and deg(f1)=d-1.
There are two exhaustive possibilities:

* If deg(f0)=d-1, induction gives ac>=2^(d-1) and bh>=2^(d-1).
  Since e+h>=c and e+h>=h,
  `(a+b)(e+h)>=ac+bh>=2^d`.
* If deg(f0)<d-1, including f0=0, then deg(f0+f1)=d-1. Put
  t=s(f0+f1), so t<=a+b. Induction gives te>=2^(d-1) and
  bh>=2^(d-1). Hence
  `(a+b)(e+h)=(a+b)e+(a+b)h>=te+bh>=2^d`.

All induction applications are to nonzero polynomials in fewer
variables, with their degrees stated. This proves (4); neither a
cancellation-free circuit model nor a product-form restriction is used.

### 3. A uniform weight filtration for the entire relation core

Take any core row in (2). Write

    a=wt(r), b0=wt(b), c=wt((r+b)P_N), h=wt(rP_N),
    W=a+b0+c+h.

If r is nonzero and d_r=deg(f_r), (3)–(4) give ah>=2^d_r. Thus

    W>=a+h>=2 sqrt(ah)>=2*(sqrt(2))^d_r.                 (5)

If b is nonzero and d_b=deg(f_b), use
`bP_N=(r+b)P_N+rP_N`, whence wt(bP_N)<=c+h. Applying (4) to b gives

    2^d_b <= b0*wt(bP_N) <= b0(c+h),
    W>=b0+c+h>=2 sqrt(b0(c+h))>=2*(sqrt(2))^d_b.         (6)

Equations (5) and (6) are separate inequalities; they do not add two
bounds charging the same entries. Each nonzero parameter r_j or b_j
therefore implies

    W >= 2*(sqrt(2))^popcount(j).                        (7)

For completeness, this supplies the sought uniform rank inequality.
Let r_w be the rank of the span of all core rows of weight <=w.
For w<2 it is zero. For integer w>=2 let D(w) be the largest integer
d>=0 with 4*2^d<=w^2. By (7), every such row has both parameter
blocks supported only on indices of popcount <=D(w). All those rows
and their span lie in a parameter subspace of dimension

    r_w <= 2 sum_(i=0)^min(k,D(w)) binom(k,i).            (8)

This bound need not be sharp; for k=4,w=4 it gives 22, whereas the
complete calculation gives 16. That difference is not used to assert
an exact uniform rank formula. The full relation's threshold-span rank
is r_w+6*[w>=1]+[w>=2], by its disjoint unit/final factors: projection
cannot increase weight, and every low-weight pure factor vector is
itself a full relation vector.

### 4. Every basis must pay for every parameter direction

Let H be any basis of E_N. Express its rows in the 2N+7 parameters of
§1, using columns for the six unit parameters, the paired-final
parameter, the N entries of r, and the N entries of b. The resulting
square matrix is invertible because the parametrization is a bijection
and H is a basis. Its determinant is nonzero. In the finite Leibniz
determinant formula, at least one permutation has a nonzero product of
selected entries; otherwise every term and hence the determinant would
be zero. Fix that permutation. It selects exactly one nonzero parameter
entry in each row and uses each parameter column exactly once.

If the selected column is one of the six unit parameters, that row has
weight at least one. If it is the final parameter, the row contains
both final coordinates and has weight at least two. If the selected
column is r_j or b_j, the row's core weight is at least the quantity
in (7). The original full row has at least that weight, since its
unit and final coordinates are disjoint from its core.

There is only one charge per row. Summing these lower bounds over the
fixed permutation gives

    sum_(h in H) wt(h)
      >= 6+2+2 sum_(j=0)^(2^k-1) 2*(sqrt(2))^popcount(j)
       = 8+4 sum_(i=0)^k binom(k,i)(sqrt(2))^i
       = 8+4(1+sqrt(2))^k.

This proves (1) for arbitrary bases, without assuming their vectors
are degree-triangular or have L125's product form. Any finite generating
set contains a basis obtained by repeatedly retaining a row outside
the span of those retained. Its total support is at least that of this
subset, proving the generating-set statement as well.

For S=16*2^k+20<=36*2^k, (1) implies

    sum_(h in H) wt(h)/S >= (1/9)*((1+sqrt(2))/2)^k.     (9)

The base is strictly greater than one. Thus no constant bounds these
ratios for all k. A pair of maps whose paired rows span E_N has total
expanded support equal to the sum of those paired-row weights, so it
also obeys this obstruction. No additional occurrence or shift charge
can reduce that required support.

### 5. Complete finite discriminant and independent checks

At N=16 each original endpoint has 36 coordinates. The constructor
`scripts/batched-incidence/check_weight_filtration.py` constructs every
literal edge, computes right constant closure, and obtains every state
residual from the finite recurrence R=beta+zMR. It verifies all 32
independent parameter rows from (2) and residual-column rank 33.
L122 §2 fixes the original graphs; they are not replaced by residual
polynomials with a smaller coordinate set.

For w=0,...,4 the script enumerates every w-subset of the 72 original
coordinates. The row is in E_16 precisely when the XOR of the selected
residual polynomials is zero. It retains every passing row. The numbers
of subsets checked total sum_(w=0)^4 binom(72,w)=1,091,059; there is no
enumeration of the 2^32 parameter core and no truncation of a search.

| Exact weight w | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| Full passing rows | 1 | 6 | 17 | 42 | 136 |
| Pure core passing rows | 1 | 0 | 1 | 10 | 30 |
| Core threshold-span rank | 0 | 0 | 1 | 6 | 16 |
| Full threshold-span rank | 0 | 6 | 8 | 13 | 23 |

Insertion by binary elimination raises rank exactly when a row is
outside the previous span. Since every passing row is inserted and
every chosen pivot row is retained, the ranks are of the complete
threshold spans, not candidate subsets. Pure-core enumeration and
projection of all full passing rows give the same spans by the
disjoint-coordinate decomposition.

The separate `audit_weight_filtration.py` imports no constructor code.
It receives every original occurrence, verifies each closure and
transition row, derives the residuals from the explicit formulas in
L125 §2, and checks R=beta+zMR. A second complete enumeration joins
equal syndromes of singletons/pairs: every sorted triple has its first
two indices followed by its last one, and every sorted quadruple has
its first two followed by its last two. Matching syndromes with these
strict index inequalities finds every relation exactly once. The audit
compares the full lists with the constructor and uses least-index
elimination instead of the constructor's greatest-index elimination.
It checks the independence and spanning of every saved rank witness.

The audit also checks (3)–(4) for all 65,809 nonzero multilinear
polynomials over F₂ with k=0,...,4, saving every coefficient vector,
translated vector, degree, actual support product and required bound.
These are finite checks of the new ingredient; the induction in §2,
not this enumeration, establishes the all-k assertion. The saved N=16
low-weight rows also pass (5)–(7) in their original coordinates. All
finite checks pass with no hidden failure or tolerance.

Full certificates are
`scripts/batched-incidence/output-544/weight-filtration.json` and
`scripts/batched-incidence/output-544/audit.json`. Reproduce with:

```bash
python3 scripts/batched-incidence/check_weight_filtration.py \
  --n 16 --max-weight 4 \
  --output /tmp/p-vs-np-weight-filtration-544/weight-filtration.json
python3 scripts/batched-incidence/audit_weight_filtration.py \
  /tmp/p-vs-np-weight-filtration-544/weight-filtration.json \
  --output /tmp/p-vs-np-weight-filtration-544/audit.json
```

### 6. Threshold and remaining qualifications

The required threshold was O(S), equivalently O(N), for the expanded
basis/maps in a joint sparse realization. Inequality (9) disproves
that threshold for every generating set of the full E_N, extending
L125's stop from its specified basis to this quantified class. No
assumption about the shift or the accepting boundaries is needed for
this necessary support obstruction.

It does not show that every boundary-receiving invariant subspace is
E_N. It does not show that every common source must span E_N. It does
not address arbitrary scalar chains, general r/G or F, mixed letters,
actual endpoint reception, full wire/work/live costs, certificate
availability, L087 W₂ or unrestricted ER/Frege/SAT. Those gaps remain.
Finite support minima and the full weight filtration at larger N are
not established. The separate conceptual audit in §7 checks (4), the
Pascal orientation and the single-charge determinant argument. It permits
using this full-relation obstruction without extending its quantifiers.

### 7. Separate conceptual audit — 2026-10-28, step 547

**Verdict: the stated full-relation obstruction passes.** This is an
audit/reproduction of §§1–6, not a stronger theorem, a claim of novelty,
or a resolution of the main problem. The pre-existing ready assessment
`drafts/literature/2026-10-28-full-relation-support-conceptual-audit.md`
and its step-545 source notes are reused. In particular, no
characteristic-zero/large-characteristic sparse-shift theorem is silently
applied over F₂. The proof of (4) remains the explicit local induction.

**Literal endpoints and all parameter directions.** The audit checks
L122 §2's closed rows, including the three constant product connectors.
For A, the terminal h row gives R_A(h_(N-1))=z; the preceding h rows
then give z^(N-i). Its f rows give
`z*(sum_(j=i+1)^(N-1) z^(N+1)y^(N-1-j)+z^N)`
`=z^(N+1)*(1+z sum_(q=0)^(N-2-i) y^q)`
`=z^(N+1)y^(N-1-i)`, where the sum is empty at i=N-1.
For B, the f recurrence first gives z*y^(N-1-i). Its terminal h row
then gives `z*(1+z sum_(q=0)^(N-1) y^q)=z*y^N`; earlier h rows give
z^(N-i)y^N. Thus every residual formula in L125 §2 follows from the
entire closed representation, rather than from equality of its accepted
polynomial alone. The rows s,f_N,h_N have beta entry zero and zero M
row, hence residual zero; t has residual one. These are closed-state
residuals: a constant-only raw suffix is not an extra beta value.

To check the reversal and absence of a transpose in (2), let
`U_a(z)=sum_(j=0)^(N-1) a_j z^j`. In reversed block order an arbitrary
core row `(r,c;b,d)` is a relation exactly when

    z^(N+1)U_(rP_N)(z)+z U_c(z)
      = z U_(bP_N)(z)+z(1+z^N)U_d(z).

The low-degree part has degrees 1 through N; the high-degree part has
degrees N+1 through 2N. They are disjoint, so necessarily and sufficiently
`d=rP_N` and `c=bP_N+d`. Constants force equality of the two final
coordinates. The six zero-residual coordinates are individually free.
This proves the full, bijective parametrization, with no deleted or
identified original coordinate. Each endpoint has 2N+4 vertices and
3N+3 occurrences, so S=16N+20. For k=0, N=1, the same empty-sum
recurrences and disjoint degree ranges remain valid.

**Support product and every induction case.** The simultaneous formal
substitution X_i->1+X_i is linear, preserves multilinearity and squares
to the identity over F₂. Its preservation of degree follows either from
this involution and non-increase of degree, or from the unchanged top
homogeneous part. In `f=f0+X_k f1`, the blocks are disjoint, so
`deg(f)=max(deg(f0),1+deg(f1))`, with the usual zero convention.
The same disjointness after translation proves the exact support product
`(a+b)(e+h)` used in §2; `c<=e+h` is only a triangle inequality and
does not exclude cancellations.

If deg(f0)=d, the nonzero f0 supplies `ac>=2^d` and both factors of
`(a+b)(e+h)` dominate those of ac. This includes f1=0 and all d=0
cases. Otherwise f1 is nonzero of degree d-1 and d>=1. When
deg(f0)=d-1, both induction inputs are nonzero and the separate terms
`a(e+h)>=ac` and `b(e+h)>=bh` prove the claimed sum of two
2^(d-1) bounds. When deg(f0)<d-1, f0+f1 is nonzero of degree d-1;
with t=s(f0+f1)<=a+b, the separate terms
`(a+b)e>=te` and `(a+b)h>=bh` give the same bound. This includes
f0=0, for which t=b and e=h. These cases exhaust the degrees; all
induction calls reduce the variable count. The nonzero base case at
k=0 is exactly f=1. No zero polynomial receives an induction bound.

**Pascal coordinates and cancellation.** Successive squaring in F₂
gives P_N[j,ell]=1 precisely for bit-subsets ell of j. Row multiplication
therefore makes the coefficient at ell the sum over j containing ell,
exactly the coefficient of X_ell in f_a(1+X). This independently checks
the row orientation of (3). The binary-popcount degree is the ordinary
total degree of f_a, not the degree of the univariate U_a(z).
For r!=0, (5) follows from ah>=2^d_r. For b!=0, linearity gives
`bP_N=(r+b)P_N+rP_N` even when terms cancel, hence
`wt(bP_N)<=c+h`; this is the correct direction for (6). Each use of
AM–GM has nonnegative real factors. A nonzero r_j or b_j only implies
that the corresponding degree is at least popcount(j); that implication
suffices for (7). Neither the proof nor the audit adds (5) and (6).
The zero core has no such constraint; every nonzero core has weight
at least two. These facts also justify the degree-subspace containment
and dimension bound (8). Projection onto any disjoint factor cannot
increase support, and each pure factor row is itself a relation, which
proves the full threshold-rank formula stated after (8).

**One charge per basis row.** The audited parametrization turns any
full E_N basis into an invertible (2N+7)-square matrix. A nonzero
determinant has a nonzero Leibniz term, including in characteristic two.
That term uses every parameter column exactly once and every row exactly
once. A selected unit coordinate costs at least 1, the selected final
parameter costs 2, and a selected r_j or b_j costs at least
`2*(sqrt(2))^popcount(j)` in that row's core. The other coordinates
cannot cancel a core entry because they are disjoint. No row receives
two charges. Summation gives precisely `8+4(1+sqrt(2))^k`, and
extracting a basis subset from any finite generating set preserves this
lower bound. The division by S in (9) uses S<=36*2^k for every k>=0;
the resulting base (1+sqrt(2))/2 is greater than one. Full spanning is
essential: the determinant cannot be asserted for a smaller subspace.

**Complete finite evidence received.** Both existing scripts were read
in full, then rerun into `scripts/batched-incidence/output-547/`.
The constructor examined all 1,091,059/1,091,059 original-coordinate
subsets of weight at most four. The independently coded syndrome join
received every one of the 202/202 passing rows, all rank witnesses and
every original occurrence/closure/residual equation. Its complete
multilinear check examined 65,809/65,809 nonzero polynomials for k=0,...,4.
The core/full threshold ranks remain `[0,0,1,6,16]` and `[0,6,8,13,23]`.
There are no failures.

The entire regenerated constructor certificate was compared by nested
value equality to `scripts/batched-incidence/output-544/weight-filtration.json`; the entire
regenerated audit certificate was similarly compared to
`scripts/batched-incidence/output-544/audit.json`, excluding only the input-path field and checking
both old and new path bindings explicitly. Thus all relevant saved
values, including all 65,809 polynomial records, were checked rather
than inferred from previews or status flags. Full replay certificates
and `replay-comparison.json` are in `scripts/batched-incidence/output-547/`.
The finite replay supports §5 only; the conceptual argument above is
what validates the all-k conclusion.

Reproduce the finite replay with the two commands in §5, replacing both
output directories by `scripts/batched-incidence/output-547/`. The
separate exact-comparison receipt records its source/destination paths,
every equality check, actual/required counts and failures. No numerical
live/work/wire bound or complete Dcomm receipt was tested by this audit.
The smaller-subspace and general-chain gaps in §6 remain open.

## Mathlib

Full matching quantitative coverage has not been checked. Finite binary
linear algebra, multilinear polynomial substitution, the determinant
formula and support cardinalities would be supporting ingredients, not
a received theorem for (1) or (4). No Mathlib theorem is used to certify
the finite calculations. Unknown availability is not evidence of absence.
