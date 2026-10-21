# Conductor-36 cusp-class compression — source/scope assessment

TARGET: Test whether complete cusp-class compression with certified Gamma_0(36) transports for every endpoint of the saved integral Manin presentation gives maximum Fourier cutoff at most 4860 and total primitive Fourier terms at most 1000000 at full tail budget 2^-38.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: BSD-177 searched numerical modular symbols/equivalent cusps/transport and Gamma0 cusp representatives/numerical compression; inspected Cremona's cumulative cusp-list algorithm, Wuthrich's transport construction and official Sage's matrix-return contract; compared L049, the full-generator assessment, the prior recovery audit, ATTEMPTS/025--026 and BSD-176's attempt/history. No completed compressed certificate appears in those scoped artifacts; no global absence or novelty claim.
SOURCE_EVIDENCE: Cremona corrected second edition (1997), Proposition 2.2.3 and every proof implication pp.16--17, and cumulative-list Implementation p.17; Wuthrich arXiv:1608.06423v2 (version stamp 23 March 2017), Section 5.1 (11) and complete ordinary matrix/point construction pp.11--12, equation (2) and Lemma 4 with proof pp.6--7; official Sage Cusp.is_gamma0_equiv documentation including infinity/matrix examples accessed 2026-10-12. Reuse audited L049's oriented Hecke closing, L051's reduced-phase arithmetic and the saved full-table source assessment.
COMPARISON: Equivalence testing, representative caching and transport evaluation are known algorithms; the difference is complete finite composition/replay and measured workload for the saved N=36 domain. Equivalent cusp labels alone do not equate primitive values. No source establishes cutoff 4860 or term limit 1000000 for this plan.
GAP: Construct and independently replay representatives, every endpoint correction and all interior points, propagate full weighted normalized tail widths, and measure distinct primitive terms. No compressed plan, improved bound, analytic table or universal complexity claim is established by this review.
REASON: Essential primary coverage now supports a bounded known-method implementation test; import the identities without new lemmas or reproofs. The changed domain and composition evidence contract are approved, while mathematical execution and critical audit remain separate.
LITERATURE_REASON: BSD-176 proposed a changed representative/transport composition scope with REVIEW_REQUIRED; this turn compares that scope using reused recovery coverage and newly inspected exact algorithm passages rather than repeating unchanged broad literature.
SCOPE: Supplied E=[0,0,0,0,1], N=36, weight two/trivial character, all 72 saved integral generators and both actual oriented endpoints, including infinity, zero and nonunitary cusps. Ordinary Gamma_0(36) transports, full good-prime representative closing, exact positive-height points and reduced real phases only; no new cusp expansion, twist or Atkin-Lehner method.

## Primary imports and qualifications

[Cremona, Algorithms for Modular Elliptic Curves, corrected second
edition (1997), Proposition 2.2.3, pp.16--17 and Implementation p.17](https://johncremona.github.io/book/fulltext/chapter2.pdf#page=10)
covers reduced cusp fractions, all equivalence criteria and constructive
congruence solvability. All three implications were inspected. The
implementation accumulates representatives as cusps are encountered;
no precomputed global cusp catalog is necessary. Apply this to the
complete saved endpoint list, retaining a witness for each assignment
and inequivalence checks for distinct representatives. Completeness here
means coverage of that finite domain, not a newly asserted global catalog.

[Wuthrich, Numerical modular symbols for elliptic curves,
arXiv:1608.06423v2, Section 5.1, (11), pp.11--12](https://arxiv.org/pdf/1608.06423v2#page=11)
applies when r'=gamma(r), gamma in Gamma_0(N), and tau is interior.
Its orientation is lambda({r' -> r})=lambda(tau)-lambda(gamma(tau)).
This supplies the correction between an actual endpoint and its cached
representative, not equality of their infinity-based primitives.
The source constructs transports from Bezout lifts and the stabilizer
of infinity, then balances the two heights using the lower-left entry.
Its stated optimal-point expression needs that entry nonzero. The
C=0 branch must instead retain a directly checked interior point or an
exactly justified zero identity; no division by zero or blanket deletion
of nonhyperbolic matrices is authorized. Matrix entries must be
recomputed from the product: the extracted congruence sign discrepancy
recorded in the prior L049 audit is not a trusted implementation formula.

[Wuthrich, equation (2), Lemma 4 and proof, pp.6--7](https://arxiv.org/pdf/1608.06423v2#page=6)
requires positive height and positive error. The complete tail is
exp(-2*pi*H*y)/(exp(2*pi*y)-1), using |a_n|<=n. This covers each new
interior point; it does not certify finite floating-point evaluations.
Use L051's audited reduced phases and positive attenuation with checked
argument/remainder bounds. No generic software correctness is imported.
The optional unitary-cusp conjugation and mixed-cusp optimization later
in Section 5.1 were read as stronger leads, but are outside this approval.
The reused Section 8.5/Theorem 13 semistable complexity result excludes
this conductor; it cannot establish the requested execution thresholds.

[Official Sage Cusp.is_gamma0_equiv](https://doc.sagemath.org/html/en/reference/modfrm/sage/modular/cusps.html#sage.modular.cusps.Cusp.is_gamma0_equiv)
documents matrix witnesses, least absolute lower-left entry and an
infinity example, citing Cremona Proposition 2.2.3. This confirms known
algorithmic overlap and infinity support, not an independent certificate.
No Sage execution or source-code correctness audit was performed. Other
search hits and the published Wuthrich version remain unread leads.
Full matching Mathlib coverage remains not checked, as in L049; no
absence claim is made. These citations remain source notes; canonical
mathematical proofs are unchanged in L049 and the retained inputs.

## Approved finite evidence contract

Essential inputs: L038's saved N=36 presentation and full production
replay; audited L049's transport/closing/tails; L050's exact minimal
model/conductor; audited L051 coefficients through 4860 and reduced-phase
method; audited L052's all-cusp clearing integer 24. No cross-notebook
input. The new L038 instance still awaits separate critical audit.

Recover the domain from scripts/conductor36-table/presentation.json,
not from a reduced basis or prior table values. Every one of the 144
endpoint occurrences must have an exact homogeneous cusp identity,
representative assignment and orientation. Preserve the actual infinity
endpoint even if other endpoints share its class. Use P(infinity)=0,
include zero normally, and retain every transport correction. Replay
all determinant-one and C divisible by 36 checks, cusp actions, matrix
products/inverses and every positive-height point, independently of the
producer. Do not infer individual values from relation agreement.

For finite representatives retain L049's full good-prime closing and
all ell+1 terms, with eligibility checked on the new representative
and closing denominators. Cached primitives must have exact point keys;
periodicity or other reductions require exact witnessed identities.
Replay each original endpoint's composition of the imported (11), then
its own oriented generator difference. Recompute all weights before
combining errors; caching cannot erase repeated contributions to error.

For the workload test use the complete normalized two-sided tail width
per original generator, after every absolute weight and division by a
certified positive lower target-period bound. Require that width at most
2^-38. Count sum of H over distinct required primitive evaluations and
report maximum H, actual/required bounds and failures in full certificates.
This conservative convention prevents mistaking a per-primitive budget
or a one-sided radius for the full table budget. Finite arithmetic and
period uncertainty must also be enclosed before any table recovery;
this planning test alone does not perform or certify that recovery.

Continue only if complete independent endpoint/point/tail replay has
zero failures, maximum H<=4860 and total distinct primitive terms<=1000000.
Otherwise preserve the actual plan and reassess its failed threshold or
coverage. Successful planning still requires all sums, positive-period
replay, 24-scaled integer isolation including zero, all source/saturated
relations and a separate critical audit. ATTEMPTS/025's rectangle failure
and ATTEMPTS/026's direct workload stop are preserved; neither prohibits
this different test. No analytic nonvanishing, useful coefficient,
rational direction, Sha result or BSD candidate follows; this CM curve
cannot meet L027's non-CM premise.
