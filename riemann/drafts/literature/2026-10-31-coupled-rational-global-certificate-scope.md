# Coupled rational certificate: completed source comparison

TARGET: Test whether V(w)=P4(w)/q(w), with q=x^2/2+6y^2+X^2/2+6Y^2 and P4 any real homogeneous quartic, permits L592's global clipping inequalities and cone condition with trace(HK)<1/288.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded exact-denominator, rational/homogeneous-storage and stronger periodic-clipping searches completed; scoped local duplicate/failure comparison and ready sufficient-method reviews reused. No inspected source decides this family or threshold; queries and read/unread distinctions follow, without a novelty inference.
SOURCE_EVIDENCE: Reused Chernyavsky et al., arXiv:2110.03079v1, Lemma 2.1/(2.4)--(2.11); newly read Section 3.1/(3.4)--(3.10), Remark 3.1, printed pp.14--16, and Theorem 3.1/Remark 3.2, p.18. Compared Ahmadi--El Khadir, arXiv:1803.01877v4, Lemma 2.1, Theorems 3.1/4.2/4.3 and relevant proofs, pp.4--9. Prior C1/growth, occupation and nonpolynomial comparisons are reused as detailed below.
COMPARISON: Fixed-denominator rational divergence fields are explicitly covered as a sufficient method; admissibility at denominator zeros still needs verification. Rational Lyapunov converses require a stable prescribed vector field and variable degrees, not this fixed family. L590/L592 stop narrower storage classes; L593 stops its fixed comparison marginal, not the present certificates. SOS feasibility is sufficient, with no fixed-degree completeness import.
GAP: The general method is covered, but exact global C1/growth and zero-set applicability, both global branches, all closed-I cone inequalities and cost below 1/288 remain unproved and untested. No inspected source supplies a matching certificate or whole-family lower bound.
REASON: Essential source coverage is now ready for a separate bounded specialization of the unchanged TARGET. Import the known sufficient method and verify the local difference; no new result, certificate, derivative calculation, lemma or mathematical script is produced here. Newly ready coverage awaits separate supervisor approval before research.
SCOPE: Only V=P4/q with the exact TARGET denominator, arbitrary real homogeneous quartic P4 and V(0)=0; w=(x,y,X,Y), dot_w=(y,z,Y,Z), v=(x,y,z,X,Y,Z), symmetric real H, L592's exact K,A and closed I, both global branches and full-trace cost. No extra parity, positivity of V, degree increase, new denominator, state cutoff, sharpness or Xi transfer is assumed.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED covered a changed coupled rational family. The missing fixed-denominator/origin and polynomial-positivity comparisons are completed here; ready divergence and occupation assessments are reused, rather than repeated for a quota.

## Gap, intermediate target and unchanged test

The main gap remains actual-Xi all-degree signs at unbounded heights.
The intermediate target is a sufficient periodic clipping certificate
at the stated threshold. Its plausible downstream use is to exclude
periodic bulk meeting that budget when K-C(h) belongs to the actual
finite cone C_I. Coupled storage could escape the stopped one-height
classes. Even success leaves periodic fourth/probability assembly and
controlled nonlinear Xi transfer unresolved; it is not an Xi sign or RH.

Use the coordinates and exact spectral K,A(u), I=[-1/2,1/2] in L592.
The proposed V has value zero at w=0. Seek a real symmetric six-by-six H
and a real homogeneous quartic P4, with no imposed parity beyond that
degree. The desired conditions, exactly as in L592, are

    v^T H v-DV(v)>=0,
    v^T H v-DV(v)-(xz-y^2)>=0                 for every v in R^6,
    trace(H A(u))>=0                         for every u in I,
    trace(HK)<1/288.

These specify the unchanged proposed target; no feasible H,P4 is
established. The later specialization must retain origin/growth
conditions, both clipping branches and every cross-lag entry. Clearing
a denominator cannot silently delete w=0, where z,Z remain arbitrary.
Floating optimization failure cannot rule out the family.

## Reused assessments and local overlap

Read the ready reviews `2026-10-31-general-periodic-clipping-dual-scope.md`,
`2026-10-31-coupled-four-state-flux-scope.md` and
`2026-10-31-rational-periodic-storage-test.md` in this directory.
Reuse their inspected C1 divergence/zero-flux proof cases, including
Fantuzzi, [arXiv:2201.00362v1, Lemma 5/(7)--(10), p.3](https://arxiv.org/pdf/2201.00362v1).
The bounded Lipschitz-domain, W^(1,p), integrable chain-rule derivative
and endpoint-flux obligations remain. The vector-state sufficient
method already covers four storage coordinates. Its general theorem
does not need a local reproof.

Reuse the same reviews' inspected nonpolynomial positive-denominator
comparison (arXiv:1512.05599v2, Section 5), compact-autonomous-flow
duality and occupation-measure sharpness comparisons. None supplies
the zero extension, fixed cost, prescribed covariance or path
realization. They have not become matching converses merely because
the proposed field is rational. No additional source audit is claimed.

Narrow local reads: L592's hypotheses and Sections 1--4; L593's
hypotheses, conclusion and source-import paragraph; L590's hypotheses,
conclusion and origin paragraph; L586's definitions and spectral
generators. Read the rational-storage and fixed-ellipse ATTEMPTS stops.
Scoped text searches of these storage/coupled assessments found no
previous test of this exact P4/q family. This is a duplicate screen,
not a theorem that no overlap exists.

L590 stops W+c*x^3*y/(x^2+y^2) with its specified extension; L592
stops W+U(x,y). Their witness cancellations must not be assumed for
the present family. Audited L593 rules out bounded full-K completions
of its particular elliptical marginal cancelling every allowed
homogeneous storage; it neither constructs a certificate nor rules
out a different witness law. These stops remain preserved. L589's
quadratic stop is reused through the assessments, without rereading
or optimizing that stopped class. No cross-notebook input is used.

## Newly inspected primary source cases

A. Chernyavsky, J. J. Bramburger, G. Fantuzzi and D. Goluskin,
[*Convex relaxations of integral variational problems: pointwise dual
relaxation and sum-of-squares optimization*, arXiv:2110.03079v1,
6 October 2021](https://arxiv.org/pdf/2110.03079v1).
The sufficient identity is reused from Lemma 2.1/(2.4)--(2.11).
Newly inspected Section 3.1/(3.4)--(3.10), printed pp.14--16:
Remark 3.1 explicitly allows a tunable polynomial numerator and fixed
nonnegative polynomial denominator D. Its recipe multiplies interior
constraints by D^2 and boundary constraints by D, then strengthens
polynomial inequalities to SOS. Denominator zeros must not make the
field inadmissible. Read this complete qualification, not just the
recipe. Theorem 3.1/Remark 3.2, p.18, require Archimedean quadratic
modules implying compact pointwise feasible sets for convergence.
Those hypotheses are not furnished for the global R^6 target. Thus
the rational sufficient method matches, but origin admissibility,
threshold feasibility and fixed-degree SOS completeness are not imports.
This is the missing method-level overlap, not a new certificate.

A. A. Ahmadi and B. El Khadir,
[*On Algebraic Proofs of Stability for Homogeneous Vector Fields*,
arXiv:1803.01877v4, 16 August 2018](https://arxiv.org/pdf/1803.01877v4).
Read Lemma 2.1 and proof, pp.4--5: for positive even k, globally C1
functions homogeneous for all real scalars admit p/||x||^r
approximations in the sphere value/gradient norm, with variable even
r and deg(p)=r+k. This does not fix r=2 or cover arbitrary
positive-scalar homogeneous, potentially noneven storage. Theorem 3.1
and its proof, pp.6--7, require a prescribed C1 homogeneous vector
field and asymptotic stability; they yield positive-definite numerator
of degree 2r+2 over (sum x_i^2)^r, with variable r. Theorems 4.2/4.3
and their proof, pp.8--9, obtain SOS Lyapunov certificates for
homogeneous polynomial dynamics, allowing degree changes. The proof
uses powers of a strict Lyapunov function and positive-definite forms.
These hypotheses are not established for the paired-jet clipping
target; no converse or fixed-quartic completeness applies. The
quotient/positive-denominator proof case and exact Gram-matrix
characterization (7) are useful comparisons only. No general density
or Lyapunov theorem needs reproving here.

The displayed versions, statements and specified proof cases were
read; their manuscripts and upstream cited theorems were not
independently audited. No theorem is imported from a search snippet.

## Obligations for the separate mathematical attempt

Use the ordinary C1 chain rule and fundamental theorem of calculus,
with the known sufficient divergence method. Verify this exact zero
extension's global C1 regularity, quadratic growth and linear-gradient
growth before using it. The four-state path and its derivative use
only jets already in L592; check periodic endpoints at lag one for
every P>0, including paths through w=0. A bounded image for each
individual path is not a common compact state restriction.

If the source's denominator-clearing recipe is specialized, retain
both original branches at every zero of q. In particular w=0 is a
two-dimensional set in the six-coordinate domain, not just v=0.
Prove whatever equivalence is actually used after the extension has
been checked. No derivative formula, cleared polynomial, positivity
reduction or regularity proof is supplied in this source-only turn.

An exact SOS/PSD identity can certify nonnegativity of a polynomial;
SOS infeasibility does not imply polynomial infeasibility. The
inspected Lyapunov and variational convergence theorems do not make
one Gram search complete for this target. Exact arithmetic or rigorous
enclosures must check recovered identities, PSD and cost. If the
family is to be excluded, the lower bound must cover all P4,H in
SCOPE, not merely a solver's sufficient subclass or finite sample.

The full closed-I constraint trace(H A(u))>=0 is an independent
obligation. Polynomial certificates in state variables do not certify
its trigonometric spectral entries. Reuse the general-periodic review's
full-trace/cone and exact Taylor-tail coverage where applicable;
sampled frequencies and ambient PSD cone substitutions do not suffice.
No new frequency enclosure is calculated here. Mathlib coverage of
the full target remains not checked; unknown is not absent.

## Bounded search record and unread leads

Queries on 2026-10-31 included:

- `"rational auxiliary functions" polynomial optimization bounds`;
- `"homogeneous" "rational" "storage functions" sum of squares`;
- `"Laguerre" "periodic" "positive part" inequality`;
- `homogeneous rational Lyapunov functions polynomial divided power quadratic origin differentiable Ahmadi El Khadir`;
- `"rational" "Lyapunov" "sum of squares" homogeneous denominator`;
- `"rational storage" homogeneous quartic quadratic dissipativity`;
- `"periodic" "clipping" "rational" covariance inequality`;
- `"homogeneous" "quartic" "quadratic" "auxiliary function" bounds`;
- `"rational" "storage" "positive part" inequality`;
- `"x^2/2" "6y^2" "storage"`;
- `"quartic" "rational" "periodic" "differential inequalities"`;
- `"Laguerre inequality" "periodic" "integral" "positive part"`.

The named-author rational-Lyapunov lead was read as specified above.
Exact-family and stronger-clipping searches produced no inspected
matching theorem. This is bounded search evidence, not evidence of
novelty or nonexistence. Search-only leads about robust domains of
attraction, rational quadratic differential forms and newer planar
Lyapunov constructions were not read or used. General RH-claim and
third-party snippets are not theorem evidence. No essential source
blocker remains for the sufficient test; no new source is needed merely
to repeat the covered method.

## Decision and one continuation

Bounded continuation test after separate approval: an exact feasible
certificate with all global/cone inequalities and strict cost below
1/288 warrants continuing; a rigorous family-wide lower bound at or
above that threshold stops this family. An unresolved feasibility
calculation is only exploration and must retain its concrete evidence.
Do not simultaneously search for a different marginal or assert Xi
transfer. No certificate, new lemma or mathematical script for this
target has been produced in this literature turn or the L593 audit.

This nomination is established-route intermediate development, not a
protected central-Xi creative attempt. The blocker to the latter is
still a controlled nonlinear transfer to actual Xi; relabeling this
surrogate family would not resolve it. The original REVIEW_REQUIRED
nomination is retained as TARGET, now with SPECIALIZE source coverage;
the supervisor separately approves this newly changed assessment next
turn. The exact target, not another approval or literature search, is
the sole recommended mathematical continuation after that approval.

Essential inputs for resumption: L592's exact K,A,I, branches and cost;
L586's finite-cone interface; L593 and L590 as failure comparisons.
Regularity, all zero-set cases, global positivity, spectral positivity,
strict cost and subsequent Xi transfer remain unresolved. Do not
change the denominator, increase degree, impose a smaller domain or
claim a complete RH candidate during the bounded test.
