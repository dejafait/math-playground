# Spatial weak logarithmic potential — completed source comparison

TARGET: Assess a spatially regularized finite-polynomial logarithmic-potential balance through L487's collision, starting from Hall–Ho Proposition 4.1 and retaining the finite-degree correction.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded exact/stronger-result searches and local heat/collision duplicate checks are recorded below; primary off-root and divisor-current proof cases inspected. No matching nonlinear collision-balance theorem was established by this search.
SOURCE_EVIDENCE: Hall–Ho, Letters Math. Phys. 115:60 (2025), Proposition 4.1 full proof and Section 4.1.3, https://link.springer.com/article/10.1007/s11005-025-01946-9 ; El Amrani–Jeddi, Proyecciones 32 (2013), 1–13, unnumbered theorem p. 2 and proof cases pp. 4–8, https://www.scielo.cl/pdf/proy/v32n1/art01.pdf . Demailly detailed text remained inaccessible and is not an essential input.
COMPARISON: Known logarithmic differential/divisor calculus handles multiple roots linearly; Hall–Ho retains the finite-degree correction but proves its nonlinear PDE off roots. These tools support a finite regularized specialization, not an imported collision balance, product of distributions, coercive inequality or Xi transfer.
GAP: A later mathematical test must derive the exact epsilon balance, prove real-time/spatial integrability and convergence, and determine whether separate nonlinear terms or only a grouped expression have limits; terminal-slice and spacetime assertions require distinct justification.
REASON: Essential source comparison is complete for the bounded finite-polynomial test specified in the separate continuation assessment; no new balance was derived or approved as a theorem in this literature-only turn.
LITERATURE_REASON: Essential new lead and changed observable: weak spatial potential at zeros, outside both Rodgers–Tao's real-simple regime and Hall–Ho's stated off-root identity.

Main gap: actual-Xi all-degree signs at unbounded heights. Intermediate
target: determine whether a precisely regularized potential has a weak
heat balance at a multiple zero, with every finite-degree term retained.
Downstream use: such a balance might measure creation of nonreal-root
mass without singular pair labels. Sign/coercivity, actual-Xi transfer,
global tails and zero time would remain separate even if it exists.

Concrete proposed discriminator for a later turn, not a derived result:
use L487's displayed degree-four H_lambda, a smooth compactly supported
spatial test in the complex plane near one terminal double zero, and
the regularized observable

    S_epsilon(lambda,z)=(1/4)log(|H_lambda(z)|^2+epsilon^2), epsilon>0.

Ask whether the exact regularized finite-degree balance admits a
distributional limit through lambda=0 and what collision contribution
survives. First assess standard potential theory and the actual proof
of Proposition 4.1, rather than multiplying singular distributions or
asserting that an off-root formula extends by continuity. Account for
the heat sign/time scaling explicitly. No formula for that balance,
limit or sign is asserted in this nomination.

Continue only if a precise source-supported limiting convention yields
a separately checkable finite test. Park if a nonlinear singular product
is undefined, essential coverage is persistently inaccessible, or only
an off-root formula is available with no defensible limiting prescription.
A scalar identity alone will not establish coercivity or exclude a
collision. The completed review's energy stop and L487's bounded
comparison stop remain intact; this changes the observable, not their
hypotheses by fiat. Read L487's complete relevant proof before using it
mathematically; it is a test object, not an Xi input. No cross-notebook
result is needed. Mathlib coverage is not checked.

The preceding text preserves the original nomination and its original
unresolved questions. The comparison below supersedes its source gate,
not its mathematical obligations.

## Sources actually inspected and applicability

Hall–Ho, version of record 26 May 2025, Proposition 4.1, equation (4.2)
and full proof: for degree N, S=log|p|^2/N and p_tau=p_zz/(2N),
S_tau=(S_z)^2/2+S_zz/(2N) away from roots. The proof uses a local
logarithm branch and Wirtinger derivatives. Section 4.1.3 requires
regularity for transport and labels a weak extension as an expectation.
Its Lipschitz limiting-density setting does not cover the atomic test.
The finite N correction must remain. The real parameter and heat sign
must be converted explicitly; this review makes no converted formula.
[Primary text](https://link.springer.com/article/10.1007/s11005-025-01946-9).

El Amrani–Jeddi, *A geometric proof of the Lelong-Poincare formula*,
Proyecciones 32(1) (2013), 1–13, DOI 10.4067/S0716-09172013000100001:
the unnumbered theorem p. 2 assumes a connected complex manifold and a
holomorphic function not identically zero. It defines the logarithmic
differential as a current and its antiholomorphic derivative as the
divisor current. Read the integrability proof pp. 4–5 (uniform translated
simple-pole bound and Fubini), branching/test-form proof pp. 5–7, and
repeated-factor reduction p. 8. Multiplicities are retained. These are
linear current statements, with no squared-gradient product or heat
collision theorem. Restricting complex parameter integrability to a
real-time slice is not an automatic consequence.
[Primary PDF](https://www.scielo.cl/pdf/proy/v32n1/art01.pdf).

Demailly's *Complex Analytic and Differential Geometry*, title/version
page (21 June 2012) retrieved, but subsequent detailed page requests
timed out. Indexed extracts of I.5 and III.2.15 are leads, not inspected
proofs or relied-on coverage. The accessible El Amrani–Jeddi source
replaces that lead for this bounded test. Its theorem does not settle
the proposed epsilon limit. Ordinary dominated convergence, Fubini,
smooth chain rules and distributional differentiation are the standard
tools permitted; their hypotheses still need proof in the specialization.

## Search, duplicates, and decision

Queries included `Hall Ho heat flow conjecture polynomials logarithmic
potential Proposition 4.1`, `logarithmic potential heat collision weak
polynomial distribution`, `logarithmic potential heat flow regularization
Hall Ho`, and `Poincare-Lelong regularization holomorphic epsilon`.
Followed the exact primary Lelong-Poincare lead to its publisher PDF.
Large-N/random-polynomial search leads were not inspected and supply
no coverage. An unsuccessful exact search is not originality evidence.

The scoped check read the earlier pair-energy assessment, its attempt
record, the direct spatial-barrier stop, and relevant heat-energy source
assessment passages. None already establishes this weak-potential
balance. L487's hypotheses and complete exact-evolution/zero-location
subsection were read; its later negative-energy calculations are not
inputs here. Its local audit paragraph and the overview differ in audit
wording; this source step does not adjudicate that status.

There is a defensible prescription to TEST: keep epsilon positive until
after spatial testing, use the same epsilon in every term, and define
any limiting grouped expression only by that specified approximation.
This is a proposed convention, not a theorem that a limit exists or is
independent of regularization. The potential, its linear derivatives,
individual nonlinear terms, and a grouped balance are different claims.
No assertion about a collision-supported term follows from the
off-root equation or the divisor identity alone.

The [finite test assessment](2026-11-01-weak-log-potential-finite-test.md)
records the exact continuation for separate next-turn approval. It
authorizes only specialization of known calculus if accepted. Continue
only with a rigorously defined balance/limit or an informative failure
of this prescribed test. Park this mechanism if it gives only a
tautological grouped limit without a separately checkable collision
quantity or any plausible route to sign control. Do not repeat the
pair-energy or bounded-Gronwall tests. No creative mechanism is ready:
a coercive observable and actual-Xi-specific input are still absent.
Mathlib full matching/supporting coverage is not checked; unknown is
not evidence of absence. No lemma, script or argument-overview changes.
