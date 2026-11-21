# Fixed exponential-wavelet calculation — working857

One approved RESEARCH/REPRODUCTION attempt at assessment855, approved856.
The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
Test only the specified compact detail spaces at T=log(3)/16 and
T=log(3)/32 in (0,4log(3)), roots (-1/2,-1/2,1/2,1/2),
empty zeros, Q_i=1, source origin0. A finite paid cross-scale bound
could inform later assembly; arbitrary scales, coarse/non-neutral
directions, uniformity and Xi transfer remain independent gaps.

Inputs read: L744 hypotheses, complete smooth formula(6), symbol bound(8);
L741 definitions and short-window qualification; ready assessment804;
assessment854 and source-working855/856 for duplicate/failure coverage.
L750/L752/C998z, conditional L742 and C759d remain stop evidence,
not sign inputs. No unchanged startup file was reread.

Required threshold: both complete Q metrics positive and beta<1/2.
A certified pair ratio>=1/2 rejects that strict estimate. Missing metrics
or incomplete analytic/roundoff control is inconclusive and ends this
one test without retuning. Preserve all partial construction and errors.

Current: construction, source-unit conversion, support enumeration,
exact moments and H2 extension are under verification; no numerical
value or sign is established. No parameter sweep or alternative generator.

## Partial reasoning saved before certificate run

Physical coordinate y=x/T, a=T/2. Let b_a be the convolution of
four exp(±ay) times the indicator of [0,1] factors, two of each sign. Source normalization
only multiplies the compact generator by a positive scale constant.
For A_k=integral b_a(y)b_a(y-k)dy/integral b_a(y)^2dy, the raw filter
is G=-z product_l(1-exp(T alpha_l)z) A(-z). It has indices[-8,2]
and nonzero extremes, hence support[-8T,6T]. Strict interior shifts
are r=5,...,28 and r=5,...,60, dimensions24 and56.

Hhigh supplies two zeros at each t=±i/2, so both pole moments and
their first moment derivatives vanish exactly. b_a and the filtered
generators are compact C2 piecewise exponential-polynomials, in H2;
supported mollification passes L744(6) by its symbol bound and bounded
finite shifts/pole functionals. Distinct finite translates are independent:
their Fourier transform is a nonzero analytic generator times a finite
Laurent polynomial. No positivity at this new length is inferred.

The diagnostic full blocks suggest beta~.9998, not a certified value.
The one selected rational witness, saved as witness-857.json, has
palindromic coefficients at both scales and common physical center L/2.
Use raw generators, since independent positive scale constants cancel
the ratio. This is pair selection within the prescribed full spaces,
not a parameter retuning. A rigorous pair ratio>1/2 suffices to stop
the universal strict estimate, without proving both full metrics.

Certificate under construction: directed60-digit Decimal intervals;
exact b8 autocorrelations from inverse Laplace(s²-a²)^(-4) positive
Taylor series; verified Gauss-Legendre24 node brackets; full digamma
via recurrence and DLMF remainder; every prime power n<81;
holomorphic Gauss error via Cauchy disks; all Fourier tails from
|F_j(t)|<=C_j/t^4. Full certificate will be saved to disk.
No sign is established until complete error evidence has been inspected.

## Completed result

C998 is the canonical full statement/proof. The final certificate uses
only L744's first-order DLMF remainder; the earlier tighter engineering
calculation is not an input. Its conservative ratio lower bound is
0.9716769..., with both pair Q values positive and
4H²-Q(u)Q(v)>1.3034. All19 certificate checks pass, with no failures.
This rejects the fixed strict half budget and ends the test.
The upper ratio enclosure crosses1 and proves no sign failure.
No full metric certification, alternative pair search or retuning follows.

Outcome NEGATIVE, RESEARCH/REPRODUCTION, actual task calculation.
Separate conceptual-audit coverage is nominated as REVIEW_REQUIRED;
PROOF.md's main argument did not change. Complete routine documentation
validation and final artifact/hash checks remain before checkpoint.

Completion checks: all19 certificate checks and both saved hashes match;
all526 panels and31 prime-power terms are present. The complete pair
Q/H intervals, ratio and discriminant were inspected with the JSON
inspector, not accepted from previews. Scoped documentation validation
passed:1230 nodes,3050 unique edges, acyclic, complete coverage and valid
links/compact overviews. Only the new C998 row was added to the supplied
DAG; pre-existing changes were retained. The one transient broken-link
error in this working note was repaired before the successful check.
