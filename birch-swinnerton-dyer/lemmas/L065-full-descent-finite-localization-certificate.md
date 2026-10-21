# L065 — Full p-descent input for the depth-one localization test

## Hypotheses

Retain every L026 premise: E/Q is non-CM; p>=5 is good ordinary;
E[p] is surjective; p divides neither #E(F_p), the Manin constant nor
any Tamagawa factor; E(Q_p)[p]=0; a residual Kurihara number in
Sakamoto's N_(1,0) is independently nonzero with the compatible Neron
plus-period and discrete-logarithm conventions; L(E,1)=0; w(E)=+1;
and a_2 of the fixed primitive ordinary cyclotomic series is
independently certified nonzero. Keep the coordinate of that series.
Use audited L061/L062, with D=Sel(Q,E[p^infinity]), its maximal
divisible subgroup D_div, and first whole-Kato-system index k.

Supply independently D=D_div. This is precisely L062's exponent
premise for e=0; neither descent nor L026 supplies it. Set n=1.
Supply the exact arithmetic evidence specified below. No candidate
class, complete Selmer computation or successful local value is
asserted to have been produced in this notebook.

The prior IMPORT assessment is
[the approved certificate scope](../drafts/literature/2026-10-15-explicit-descent-certificate-import.md),
with its completed primary-source comparison. This statement imports
the known representation and specifies its handoff; it adds no descent
algorithm or nonvanishing theorem.

## Conclusion

A full descent representative satisfying items 1–4 below certifies a
class c in the classical Sel_p(E/Q). Item 5 has two possible outcomes:

- A certified nonidentity local power class at p proves loc_p(c)!=0
  in E(Q_p)/pE(Q_p). Under the independently supplied D=D_div, L062
  then gives k=1, rank_Q_p(lambda_p)=1 and a one-dimensional strict
  Selmer kernel.
- The identity local power class proves loc_p(c)=0 for this c. This
  witness fails; it does not select k=2 or exclude another successful c.

Missing or uncertified data give neither conclusion. In particular,
global nontriviality alone is not a successful test. Even a successful
test gives no rational Kummer membership of the strict line, rational
rank two, finite Sha, or arbitrary complex-order/rank comparison.

## Proof

**Precise named imports.** Schaefer–Stoll, *How to do a p-descent on an
elliptic curve*, Trans. AMS 356 (2004), 1209–1231,
[DOI](https://doi.org/10.1090/S0002-9947-03-03366-X): use the
[author long version dated 13 June 2001](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
whose numbering is fixed here. Proposition 4.6 (p. 7) and Section 5,
equation (5.1) (pp. 8–9), give the finite local-condition intersection.
Proposition 6.4 and Corollary 7.1 (pp. 12–13) give global and local
injectivity for the full nonzero torsion set. Proposition 7.8,
Corollary 7.9 and Proposition 7.10 (pp. 18–19) identify the cohomology
image by the scalar-action and incidence-norm kernels, including
unramified classes. Schaefer, *Computing a Selmer group of a Jacobian
using functions on the curve*, Math. Ann. 310 (1998), 447–471,
[corrected arXiv:1507.08325v1](https://arxiv.org/pdf/1507.08325v1),
Theorem 2.3 and its following field extension (pp. 6–7), identify
divisor evaluation with the Weil-pairing/Kummer composition. These
results are imported without reproof; the earlier assessment records
the inspected essential proof cases and assumptions.

**Applicability.** Take K=Q, theta=[p], E'=E and the entire set
X=E[p] minus {O}. Its size p^2-1 is prime to p, as required for the
full-set injectivity application of Proposition 6.4; the same argument
applies over each completion. The origin gives the divisor-class base
point. Section 5's multiplication-by-p setup supplies the evaluation
functions and the specialization of Schaefer's assumptions; injectivity
is supplied by Corollary 7.1, rather than assumed for an arbitrary
smaller torsion set. No CM or rational-isogeny special case is used.
If formulas require a short Weierstrass equation, provide the rational
change of variables and transport all torsion, functions and divisors
through it. The unchanged curve and [p] determine the Kummer quotient;
no Neron-period normalization is introduced into descent evaluation.

Write R for the finite etale algebra of Galois-equivariant functions on
X, and R_v=R tensor Q_v. It has dimension p^2-1. This R is neither
L061's A=E[p^infinity] nor its Selmer group D. Write

  iota_v:H^1(Q_v,E[p]) -> R_v^*/R_v^{*p}

for the injective imported map, and similarly iota globally. Its
composite with the finite Kummer injection delta_v is F_v. Choose
the equivariant functions f_T with divisor p(T)-p(O) as in Section 5;
F_v evaluates them on degree-zero divisors supported away from X and
O. Constants multiplying these functions cancel on degree-zero
divisors. All maps and arithmetic below must use the same choices.

**Finite supplied certificate.** The following are verification
obligations, not computed evidence or a claim that a generic computation
has finished.

1. Supply E, p, a finite set S containing p and every bad prime, and
   exact presentations of R and its local factors at S, with certified
   identifications with the full torsion scheme X. Supply the functions
   f_T, their divisor identities and Galois compatibility. The rational
   scalar action and source-defined dual/incidence algebras and maps
   must also be identified if the kernel description is used.

2. Supply alpha in R^*, together with a certificate that [alpha] belongs
   to iota(H^1(Q,E[p];S)). Here H^1(;S) means cohomology unramified
   outside S. One permissible format supplies the exact scalar-action
   and incidence-norm kernel checks of Corollary 7.9, using Proposition
   7.10's norm map, and membership in R(S,p) under that corollary's
   identification. Kernel equalities are equalities of power classes,
   with exact witnesses or certified quotient coordinates, rather than
   equalities of chosen representatives. R(S,p) consists of classes
   whose valuations outside primes above S are multiples of p;
   factorization and ideal evidence must certify this for the supplied
   alpha. Alternatively a certified actual cohomology preimage with
   its unramifiedness evidence is acceptable. Merely assigning a
   Selmer label to alpha is not a certificate. A complete unit/class-
   group basis is unnecessary for checking one supplied element; if
   used, its needed arithmetic assertions must be independently
   certified, not inferred from an algorithm name.

3. For each v in S supply exact local power-class arithmetic and a
   certificate that [alpha_v] is in F_v(E(Q_v)/pE(Q_v)). For example,
   supply a good Q_v-rational degree-zero divisor Z_v on E and verify
   [alpha_v]=[F_v(Z_v)], where the right side denotes evaluation on
   that divisor. A certified expression in finitely many evaluated
   local divisor classes also suffices, with coefficients modulo p.
   Supports must avoid all zeros/poles of the functions. Local points
   or divisors and their evaluations need rigorous finite evidence,
   such as certified defining equations and Hensel neighborhoods with
   proved power-class reductions. Decimal approximations and lists of
   purported generators without their arithmetic justification do not
   suffice. All local quotient presentations used must be faithful,
   with enough certified reduction evidence to check the asserted
   equalities. No complete local-image enumeration is required when
   an individual membership witness is supplied.

4. Account for all other classical local conditions. Since S contains
   all bad primes and p, Proposition 4.6 applies to [p]: outside S
   the unramified condition in item 2 is the classical one. At the
   real place positive-degree p-primary cohomology vanishes for odd
   p, as in audited L061. Thus it gives no extra omitted condition.
   The preceding checks use full cohomology and actual classical
   images; no fake scalar quotient, isogeny Selmer group, or relaxed
   condition can replace them.

5. At p additionally supply the exact identity test for [alpha_p] in
   R_p^*/R_p^{*p}. In a certified faithful finite power-class
   presentation this is the test whether its complete coordinate
   vector is zero. A nonzero coordinate must come with the underlying
   quotient justification; a finite-precision residue by itself is
   insufficient. An identity claim likewise requires justified power
   membership, not merely lack of detected nonzero coordinates. The
   test concerns the same class at depth one, without coefficient
   reduction, division by p or rationalization.

**Handoff.** By item 2 and global injectivity there is a unique
cohomology class c with iota(c)=[alpha], unramified outside S. Items
3–4 and the imported finite-intersection theorem place c in the
classical Sel_p. For v in S the evaluation identity and injectivity of
iota_v identify its localization with the finite Kummer class of the
supplied local divisor expression. Consequently

  [alpha_p]=1  if and only if  loc_p(c)=0 in E(Q_p)/pE(Q_p).

The forward direction uses both local cohomology injectivity and the
finite Kummer injection; it is not a test in a quotient with an
uncontrolled kernel. If [alpha_p]!=1, L062 applies at e=0,n=1 using
the independent D=D_div and every retained L026 premise. It gives
exactly the successful-branch conclusions stated above. If [alpha_p]=1,
only this class fails: c=0 is always such a failure in either branch.
No inverse-limit surjectivity, nonzero whole-system component or global
rational point is supplied by this certificate format.

The good divisors Z_v are local witnesses and need not arise from a
single global rational point. Requiring that would unnecessarily replace
the approved target by rational-point production. Conversely, allowing
local witnesses never identifies c with a global rational Kummer class.
ATTEMPTS/033's scalar reconstruction obstruction and L024's actual-pair
and m>2h premises are unchanged; no prescribed prime-deletion class
has been reconstructed. The capped L064 scalar route remains stopped.

This completes a conditional known-method import, not a new theorem
beyond the checked sources. No arithmetic instance or nonzero witness
exists here. Its finite-data specification and applicability assembly
pass the separate critical audit below, under exactly the supplied-input
hypotheses; this is not an arithmetic production result.

**Separate critical audit (2026-10-15).** The approved audit finds no
failed implication or additional premise. The scope is
[the prior IMPORT assessment](../drafts/literature/2026-10-15-full-descent-certificate-critical-audit.md).
This establishes the existing assembly as a checked conditional input,
not a new descent theorem. The source results above remain imports,
with their earlier essential proof-case inspection reused.

For injectivity, X is Galois-stable and spans E[p] over every base
field in question. Its cardinality p^2-1 is prime to p even when the
local Galois action has smaller orbits. These are exactly Proposition
6.4's hypotheses, and Corollary 7.1 explicitly includes completions.
The argument does not require residual surjectivity over Q_p. For the
image condition, Corollary 7.9 gives both scalar and incidence kernels
and the intersection with R(S,p); Proposition 7.10 identifies the actual
incidence norm. Item 2 requires these maps on the full identified
algebras. A check in a smaller quotient cannot satisfy that item.
The alternative cohomology-preimage format must independently prove
unramifiedness; no implication from a mere representative label is used.

Schaefer's Assumption I is satisfied because the origin identifies
E(K) with degree-zero divisor classes represented over K, for K=Q
and each completion. The torsion divisors (T)-(O) form the equivariant
spanning set for the dual kernel of [p]. Section 5 of Schaefer--Stoll
supplies good representatives and the stated function construction;
Schaefer's Theorem 2.3 and field-extension statement identify evaluation
with Kummer followed by the Weil-pairing map. Injectivity is supplied
separately by the full-set result, rather than inferred from that
evaluation identity. Constants cancel because the evaluating divisor
has degree zero. A rational divisor may have nonrational geometric
support; in that case evaluation includes all conjugates, equivalently
the residue-field norms with multiplicities. The supplied exact
evaluation must implement that divisor evaluation, not a selection of
geometric points. This spells out the existing good-divisor condition.

Here is the full membership implication independently of any local
nonvanishing assumption. Item 2 gives a unique c in H^1(Q,E[p];S).
For v in S, let P_v denote the E(Q_v) class of the good divisor
expression in item 3. Naturality and the evaluation identity give

  iota_v(res_v(c)) = [alpha_v] = iota_v(delta_v([P_v])).

Injectivity of iota_v implies res_v(c)=delta_v([P_v]), so c satisfies
the classical condition at v. Outside S the good-reduction prime is
different from p, and Lemma 4.5/Proposition 4.6 identify that condition
with unramifiedness. Enlarging S to all bad primes is permitted; it
does not omit a place at which the source requires a test. The real
cohomology is zero for odd p: it is killed by two and is p-primary.
Thus c is classical at every place before item 5 is used. The P_v
need not be localizations of one global rational point.

At p the same displayed identity and the finite Kummer injection give
[alpha_p]=1 if and only if [P_p]=0 in E(Q_p)/pE(Q_p). A faithful
power-class presentation must distinguish identity from every
nonidentity class in every factor actually used. The obligation to
certify this is explicit in items 3 and 5. Neither a precision threshold
nor a successful algorithm is inferred from the cited evaluation
theorem. Hensel neighborhoods are admissible evidence only together
with proved power-class reductions and the claimed points/divisors;
unjustified floating approximations fail the certificate conditions.
There is no asserted upper bound on the cost of supplying these data.

Finally write alpha_1 and beta_1 for L061's natural global and local
coefficient isomorphisms. All L026 premises are unchanged, including
global residual surjectivity, E(Q_p)[p]=0 and the independently nonzero
quadratic coefficient and residual family. Hence

  beta_1(loc_p(c)) = f(alpha_1(c)).

In L061's k=2 branch f(D) is finite. The additional D=D_div makes
f(D) divisible as well, so f(D)=0. Since beta_1 is injective, a
nonidentity [alpha_p] contradicts precisely that branch. Applying
L062 with e=0 and n=1 therefore gives k=1 and its stated rank and
strict-kernel dimensions. No coefficient transition, integral Tate
surjectivity or new Kim theorem is involved. Identity yields only a
failed witness: c=0 satisfies the identity test in either branch.
Global nontriviality also gives no nonidentity conclusion at p.

All direct mathematical inputs remain L061 and L062; the descent
theorems are the precise named imports above. No DAG change is needed.
D=D_div, an actual full class and its successful exact local test are
still unproduced. Even acceptance supplies neither a global rational
Kummer direction nor the complex-order comparison. Mathlib coverage
remains as stated below.

## Mathlib

Full p-descent image characterization, evaluation identity, exact
number-field/local power-class algorithms, and the combined L062
application: not checked. Supporting Kummer, finite-etale-algebra and
local-cohomology coverage: not checked. Unknown availability is not
evidence of absence. The named arithmetic theorems above are imports;
only their applicability and the existing L062 handoff are justified.
