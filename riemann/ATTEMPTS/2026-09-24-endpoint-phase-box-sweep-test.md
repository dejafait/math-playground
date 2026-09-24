# Endpoint phase-box sweep test — 2026-09-24

Gap and target: the endpoint arithmetic margin at the prescribed a_n,
and the lower Laguerre indices needed for the global witness argument,
remain unproved. Test whether L339's fixed negative phase box can be
visited in every translated interval of length H=exp(2r). The proposed
intermediate target is a strict upper bound below one for the Haar
measure of the box swept by the prime-logarithm flow over [0,H]. A
covering deficit would stop this uniform return target itself, beyond
L340's obstruction to one Fourier certificate. A particular interval
near a_n, transfer to a_n, and all remaining positivity steps would
still be unresolved. If the volume bound does not fall below one,
this test alone supplies no obstruction and does not justify a return
claim.

Redundancy review: read GOAL.md, PROGRESS.md, the whole PROOF.md and
the global DAG before choosing work; inspected the existing changes.
L335 gives fixed-r recurrence, L336 and L340 obstruct sufficient
Fourier return certificates, and L339 supplies the fixed-width box.
The recorded bounds do not rule out actual visits in every interval
on the coupled scale. No swept-volume obstruction was found. This is
a geometric test of the target, not another estimate of its Fourier
coefficients. The September 21 admission condition is superseded by
GOAL.md; its mathematical evidence and all unfinished work are retained.

Unfinished reasoning saved before completing the proof: lift the
closed box to Q=[−ε,ε]^d, ε=1/10, with d primes through exp(6sqrt(r)),
and sweep along v=(log p). The Euclidean swept set should be covered
by Q and the outward-face prisms F_j+[0,H]v. Their volumes would give
μ(E_H)≤(ε/π)^d[1+H Σ_p log p/(2ε)]. L340's elementary lower bound
for d should make this exponentially small in exp(6sqrt(r))/sqrt(r)
when log H=2r+O(1). A strict deficit leaves an open complement.
Unique prime factorization and finite trigonometric approximation
should show the actual forward prime-logarithm orbit enters that
complement at arbitrarily large times, yielding actual empty
translated intervals, with r fixed first. Check the face-cover
argument, torus projection, density, quantifiers, and the distinction
from the prescribed coupled interval before claiming a result.
Zero consecutive unresolved exploration turns precede this test.

Result: [L341](../lemmas/L341-endpoint-phase-box-geometric-return-obstruction.md)
proves the saved swept-volume inequality. At the endpoint cutoff it
is at most exp(−c exp(6sqrt(r))/sqrt(r)), with
c=(log 2)log(10π)/24>0 and a sufficiently large unspecified starting r.
The open complement and an elementary finite Fourier proof of forward
orbit density give arbitrarily late actual empty intervals of length
exp(2r) for each fixed large r. Every length that guarantees a visit
in every translate, even only eventually, must satisfy
H≥(2ε/Σ_p log p)[(π/ε)^d−1], hence
log H≥c exp(6sqrt(r))/sqrt(r). This exceeds the required 2r by a
diverging factor. It does not locate an empty interval near a_n or
bound the first visit from a specified starting height.

WHY IT FAILS: the [canonical proof](../lemmas/L341-endpoint-phase-box-geometric-return-obstruction.md)
shows that the fixed-width box has exponentially small volume in the
number of constrained primes, while sweeping it for time exp(2r)
adds only H times its outgoing face volumes. The sweep cannot cover
the torus. Density then forces actual starting heights whose entire
intervals miss the box. Thus uniform full-box return at this scale
is false, regardless of the return certificate. The box is only a
sufficient negative-sign region; its complement may contain other
negative values, and a particular coupled interval remains undecided.

Assessment: NEGATIVE; stop the uniform full-box target at this scale.
Zero consecutive unresolved exploration turns; no RH candidate or
extension of the established sign/exclusion ranges. The main endpoint
and low-index gaps remain. A larger region defined by a weighted
angular budget is a distinct target: L339's normalized product proof
controls an aggregate logarithmic derivative, whereas its statement
imposes the same tolerance on every prime. Testing whether that
aggregate condition still forces negativity could avoid unnecessary
coordinate constraints. Its size, occurrence on the coupled interval,
and transfer to a_n would remain separate unresolved questions.
The sole concrete current action is in PROGRESS.md.

Verification: checked the explicit face covering, slice volumes,
torus projection with overlaps, closedness of the sweep, finite
Fourier mean for an arbitrary open box, unique factorization, and
the order of the fixed-r and large-height quantifiers. Substitution
of L340's prime-count lower bound gives both scale inequalities
with the stated c. These analytic proofs require no numerical
return-time or prime-table computation. Full Mathlib coverage is
not checked. The DAG records L339's conditional negative-sign
input and L340's elementary prime-count bound; no other prior
lemma is used as an unproved premise. All earlier work is preserved.
