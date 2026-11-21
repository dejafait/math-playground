# Nomination: one signed mixed-covariance quarter-budget test

TARGET: Test whether C999l's zero-tail predictor comparison has signed mixed covariance B D_tail^-1 B*<=M_cert/4 on all free endpoint modes n>=512, retaining full U and both T orientations and paying complete input and output tails at K=65536.
CHECKED: 2026-11-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed assessment561/step562 searched exact signed Weil/Galerkin mixed covariance, stronger form Schur criteria and quantitative tail methods, and compared the recorded scalar/derivative/response-prefix/automatic-factorization stops. No matching bound was located; no originality is inferred.
SOURCE_EVIDENCE: Direct primary sources reopened in recovery563: [Friedrich-Gunther-Klotz1708.01545v1](https://arxiv.org/pdf/1708.01545v1), Definition4.1, Proposition5.4/Theorem6.1 and both proofs pp5/9-10; [Li paper45 displayed v2](https://rstation.ai/problems/riemann_hypothesis/papers/45), Sections4-5 (4.4)-(5.5); [Dritschel-Rovnyak0903.3639v1](https://arxiv.org/pdf/0903.3639v1), LemmaA.1 and both proofs pp28-29; [Behrndt et al.1403.5704v1](https://arxiv.org/pdf/1403.5704v1), Corollary3.5 p12. Reuse completed561 and ready553/555/559 for the other inspected proof cases and [Teschl GSM99](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf), Theorems2.13/2.18 pp71-72/77. C744v/w and C999j/k/l supply local contracts, not a mixed-input bound.
COMPARISON: Standard weighted covariance and form Schur results cover the method. The complete signed mixed map, its infinite neutral-coordinate specialization and quarter-budget enclosure are new local obligations; no source or prior output-tail estimate supplies them. No complementary sign follows automatically.
GAP: Certify the exact full mixed covariance against M_cert/4, with every input column and inverse-action output tail paid; the independent complementary comparison >=D_tail/4 remains outside this test.
REASON: Step562's completed source review justifies a single quantitative established-route test rather than generic boundedness or automatic factorization. This newly written ready continuation requires the supervisor's separate approval before research; no lemma, script or numerical inequality is established here.
SCOPE: ell=log(3)/2; independent complex endpoint free coordinates; head2:511, tail n>=512, exact two low-mode moment corrections; original D/S/T/U; C999l's exact Galerkin predictor on the head and zero on the free tail; unchanged C999k reference d0=6.14/fraction1/2/penalty256; fixed K=65536; no tuning or complementary sign premise.

## Exact proposed test and domains

The main gap remains L030-L032/C032a actual-Xi positivity. This
intermediate target would quantify what one particular head/complement
interface costs. Its plausible downstream use is a Schur assembly with
an independently proved complementary lower form; it need not settle
that other claim or the global RH gaps to be useful.

Let Z_H be C999l(1), independently for each endpoint, and let x in
C^1020 collect the two head vectors. For a finitely supported pair
y=(y_f,y_h) on n>=512 define Z_T by the SAME existing moment ratios,

    (Z_T y)_n=y_n (n>=512),
    (Z_T y)_p=-sum_(n>=512,n mod2=p)r_n y_n (p=0,1),
    (Z_T y)_n=0 (2<=n<512).

These formulas define the proposed finite-support starting space;
the future proof must justify their continuous extension and exact
parametrization on the weighted infinite space. Do not assume the
raw projection preserves neutrality or that physical head and tail
are orthogonal: their low-mode corrections overlap.

Use the imported positive increasing lower weights of C999l Section3,

    d_n=log(n/(2ell))-2ell^2/(9n^2), n>=512,
    ||y||_tail^2=sum_(n>=512)d_n(|y_f,n|^2+|y_h,n|^2).

D_tail is this diagonal on the two free tails, NOT the full local
energy of Z_T y. Its form domain Y_D is the completion in this norm.
Establish Z_T:Y_D->V0, density of the finite starting space in the
relevant form norm, and the full forcing/residual applicability using
the existing local contracts. No new essential general theorem is
missing for this specialization, but none of these new applicability
claims is proved by this nomination. Boundary evaluation on arbitrary
Y_D inputs must not be assumed from C999l's finite-head functionals.

Set f=Z_H x_f+Z_T y_f, h=Z_H x_h+Z_T y_h and g=g_G(x), where
g_G is C999l(3)'s exact predictor. It is zero for x=0. Define the
proposed sufficient comparison, initially on finite inputs, by

    F(x,y)=Q_actual(f,g_G(x),h)
                  -<R^-1 rho(x,y),rho(x,y)>,
    rho(x,y)=Tf+T*h-Lg_G(x), L=D+S+256C*C.

The extension of C999l(5) to these endpoints is an applicability
obligation of the research test. It is not a new assertion here.
Let M_cert be the exact certified lower head matrix in C999l Section5,
including every scalar/assembly allowance and its Section7 audit, so
F(x,0)>=x*M_cert x and M_cert>=.000999 I under the retained contracts.
Do not use a diagnostic eigenvalue or an unadjusted floating matrix.

Define B by polarization with matrix convention

    F(x,y)-F(x,0)-F(0,y)=2 Re(x* B y).

This fixes its sign/orientation and includes ALL low-mode D cross
terms, full S and U, both T orientations, the middle trial cross
terms and the reference-residual cross product. It is a definition,
not a derived simplified formula. Prove any formula used to compute B
and its continuous extension. The new quantitative test is exactly

    G_mix=B D_tail^-1 B* <= M_cert/4,

or equivalently ||M_cert^-1/2 B D_tail^-1/2||<=1/2 after the
domain/extension checks. This bound is NOT known or claimed.

The standard form Schur criterion, cited in assessment561, would still
require the independent claim F(0,y)>=||y||_tail^2/4 for assembly
with this budget. That complementary claim is deliberately unresolved
and is not an input to estimating B. The quarter is a fixed sufficient
budget, not a predicted value, an optimized threshold or a consequence
of C999l's finite margin. A failed budget is not a negative direction
of Q_min or a disproof of RH.

## One bounded verification procedure

First check the weighted neutral spaces and domain specialization.
Use existing inverse order and closed-form representation by precise
citation, without reproving those standard theorems. Work with the
complete lifted residual and original form, not a new scalar A0 floor.

For n=512,...,65535 and each endpoint orientation, enclose the entire
signed column b_n=B e_n, combining all its contributions before forming
its weighted outer product. The finite covariance is the sum of these
outer products with weights1/d_n. Cross products between U, local
terms, predictor terms and inverse-action terms WITHIN a column cannot
be discarded. There is no covariance between distinct input coordinates
in this column sum because D_tail^-1 is diagonal.

Pay the entire remaining input covariance n>=65536 by an analytic
operator-order bound. C744w's exact shifts, full response divided
differences and C999l's finite-head boundary expansion are available
starting formulas; the input-tail specialization must be proved.
Leading functionals may act on finite head data, but an unproved
boundary trace of arbitrary infinite input is not licensed. Complete
prime lists, response series, constant-mode normalization and low-mode
moment corrections must all be retained.

The output inverse action is a separate infinite obligation. One
permitted finite route is to enclose R^-1 rho_H for the head forcing
through output65535, then bound its full output remainder by the
audited head-residual estimates and positive reference weights.
Propagate that remainder using the covered bounded T/T* maps and
neutral-coordinate norms when forming mixed columns. Any alternate
exact Parseval total-covariance evaluation must justify its functions
and convergence. Neither truncating this action nor reading a small
saved residual preview pays its error. Predictor/factor/solve and
IEEE754/Decimal arithmetic errors remain chargeable in operator order.

Certify M_cert/4-G_mix>=0 after ALL allowances for a pass. A rigorous
finite-column lower covariance exceeding M_cert/4 in one head direction
rejects this fixed sufficient budget, since omitted weighted column
Grams are nonnegative. An overlap with the threshold or unpaid input
or output remainder is inconclusive. Stop after this one test: no
larger predictor, altered reference, input split or allocation tuning.
Save unfinished reasoning before lengthy calculation, full certificates
on disk, and report actual/required bounds, failures and paths.

Essential local inputs: C744v/w's full operator/domain/entry contracts;
C744z Sections1-3 and scalar/derivative/response-prefix stops; C999j's
strong-domain identity; C999k Sections1-2/6; C999l Sections1-7 with
559/561 certificates; ready553/555/558/559 and completed561/step562.
Retain whole-core and unreplayed c_* qualifications and analytic,
IEEE754 and Decimal contracts. Complement coercivity, C744q margin,
H2 slack/existence, non-neutral coverage and global assembly remain
unresolved. No RH/H2 or cross-notebook premise is introduced.

Full matching Mathlib coverage is unchecked, not asserted absent.
This is REPRODUCTION using an established quantitative method. The
infinite mixed covariance and its two tail directions make development
difficult, but no independently justified new central creative mechanism
has emerged. Do not relabel a standard specialization as creative.


## Separate source approval and URL recovery — step563, 12 November 2026

This literature-only recovery preserves the exact TARGET, SCOPE, fixed
quarter allocation and K=65536. It repairs missing direct URLs in this
assessment; it establishes no numerical bound or new mathematical result.
The initial nomination's request for separate source approval is addressed
by this review. SPECIALIZE remains ready for one REPRODUCTION test.

Reopened the primary sources linked in SOURCE_EVIDENCE. Friedrich,
Gunther and Klotz's Definition4.1 requires a square-root range inclusion.
Proposition5.4 and Theorem6.1, with both proof directions, require positive
diagonals and a contraction factorization, or positive type and a
nonnegative Schur remainder. These conditions cannot supply an unproved
complement sign. Their linear-space formulation covers forms; it does
not establish the proposed weighted coordinate extension or its bounds.
The served v1 PDF retains the internal 30July2018 date noted in561.

Dritschel–Rovnyak LemmaA.1 and both proof directions were reopened:
the operator must be bounded on a Hilbert space and the splitting must
use a closed subspace. Its square-root factorization requires a
contraction and nonnegative diagonals. It cannot be applied directly
to an unbounded raw diagonal; weighted-map continuity remains a local
specialization obligation.

Li's displayed v2 (9November2026), Sections4-5 (4.4)-(5.5), was reopened
including the complete-form closure argument. The method uses an
increasing strictly positive complementary diagonal, a bounded mixed
map, complete Parseval covariance with cross products retained, and
monotone inverse weights for the remaining input covariance. These are
method coverage, not transferable constants or positivity for this
notebook's residual comparison. No source numerical certificate was
replayed or imported. Behrndt et al. Corollary3.5 was reopened: inverse
order is for nonnegative selfadjoint relations in a separable Hilbert
space. Reuse the previous representation and nonnegative-case proof
coverage in553/555/559/561 rather than reprove it.

Reuse561's discovery and duplicate/failure comparison; no new broad
search is justified by a missing-URL repair. In particular, scalar,
derivative, response-prefix and automatic-factorization failures remain
evidence, while none decides the signed mixed-covariance test. No source
provides its quarter bound. The infinite neutral parametrization,
forcing/domain applicability and complete input/output estimates must
be checked in the research attempt before claiming the inequality.
A domain failure or unpaid tail is inconclusive for the numerical budget;
a certified finite-column excess rejects that fixed sufficient budget.
A pass still requires the independent complementary lower comparison
before any Schur assembly. Full matching Mathlib coverage remains
unchecked. No creative mechanism is nominated: this is an established
method specialization with unresolved quantitative and domain obligations.
